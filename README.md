## Setup

First you will need to configure the following environment variables:

- `API_KEY`: Api key can be anything. This will be used to temporarily secure the api.
- `CONN_STR`: This should be the connection string to an azure storage account. We use this to connect to the azure data table.
- `TABLE_NAME`: This should match a table name in the above mentioned storage account.
- `PARTITION`: Partition can be anything. This will be used as additional key added to each row in the table.

Next we create the python virtual environment and install the required dependencies.

```
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

Finally we can start the appliation.

```
uvicorn app.main:app --reload
```