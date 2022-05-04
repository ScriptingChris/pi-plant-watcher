import logging
import json
import os
import azure.functions as func
from azure.data.tables import TableClient


CONNECTION_STRING = os.getenv('CONNECTION_STRING')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    query = "PartitionKey eq 'RedMarker'"
    table_client = TableClient.from_connection_string(conn_str=CONNECTION_STRING, table_name="plant-data")
    entities = table_client.query_entities(query)
    for entity in entities:
        for key in entity.keys():
            print("Key: {}, Value: {}".format(key, entity[key]))










    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
