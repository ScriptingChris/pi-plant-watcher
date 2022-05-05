import logging
import json
import os
import azure.functions as func
from azure.data.tables import TableClient


CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=piplantstorage;AccountKey=A+uYWMFB/brmKQczn3QNqLleQQ6rQWXTmSJQ1ngI6j/zATehgXBAwdj+hCN58cNCqn8PNWmAla1rgdfKVv/tvA==;EndpointSuffix=core.windows.net' #os.getenv('CONNECTION_STRING')
TABLE_NAME = "PlantData"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    query = "PartitionKey eq 'rpi-chili'"
    table_client = TableClient.from_connection_string(conn_str=CONNECTION_STRING, table_name=TABLE_NAME)
    entities = table_client.query_entities(query)
    data_object = []
    for entity in entities:
        entity_object = {}
        for key in entity.keys():
            entity_object[key] = entity[key]
            logging.info(f"Key: {key}, Value: {entity[key]}")
        
        data_object.append(entity_object)


    if len(data_object) >= 1:
        json_object = json.dumps(data_object)
        return func.HttpResponse(
             json_object,
             status_code=200
        )
    else:
        return func.HttpResponse(
             "Not found",
             status_code=404
        )