from os import environ as env

from fastapi import Security, HTTPException
from fastapi.security import APIKeyQuery, APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

API_KEY = env["API_KEY"]
API_KEY_NAME = "access_token"
API_KEY_QUERY = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
API_KEY_HEADER = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_query: str = Security(API_KEY_QUERY),
        api_key_header: str = Security(API_KEY_HEADER),
):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )