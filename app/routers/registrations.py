from fastapi import APIRouter, Depends
from azure.data.tables import TableServiceClient
from fastapi.openapi.models import APIKey
from pydantic import BaseModel
from uuid import uuid4 as uuid
from os import environ as env
from app.config.auth import get_api_key

router = APIRouter()

table_name = env['TABLE_NAME']
conn_str = env['CONN_STR']
partition = env['PARTITION']


class ResigrationRequestBody(BaseModel):
    email: str
    going: bool
    count: int
    mailing_list_opt_int: bool


def get_client():
    client = TableServiceClient.from_connection_string(conn_str=conn_str)
    return client.get_table_client(table_name=table_name)


@router.get("/", tags=["registrations"])
def get_all_surveys(api_key: APIKey = Depends(get_api_key)):
    client = get_client()
    response = client.query_entities(query_filter="PartitionKey eq '{}'".format(partition))
    return list(response)


@router.get("/{item_id}", tags=["registrations"])
def get_surveys_by_id(item_id, api_key: APIKey = Depends(get_api_key)):
    client = get_client()
    return client.get_entity(partition, item_id)


@router.delete("/{item_id}", tags=["registrations"])
def get_surveys_by_id(item_id, api_key: APIKey = Depends(get_api_key)):
    client = get_client()
    return client.delete_entity(partition, item_id)


@router.post("/", tags=["registrations"])
def add_surveys(body: ResigrationRequestBody, api_key: APIKey = Depends(get_api_key)):
    client = get_client()
    registration = body.__dict__
    registration['PartitionKey'] = partition
    registration['RowKey'] = str(uuid())
    client.create_entity(entity=registration)
    return registration


@router.put("/{item_id}", tags=["registrations"])
def update_surveys(body: ResigrationRequestBody, item_id, api_key: APIKey = Depends(get_api_key)):
    client = get_client()
    registration = body.__dict__
    registration['PartitionKey'] = partition
    registration_final = client.upsert_entity(entity=registration)
    return registration_final
