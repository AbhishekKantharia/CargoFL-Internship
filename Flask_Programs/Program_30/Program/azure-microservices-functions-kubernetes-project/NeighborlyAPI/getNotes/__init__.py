import logging
import azure.functions as func
import json
import os
import pymongo
from bson.json_util import loads, dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:

        url = os.environ["myAzureCosmosMongoDBConnectionString"]
        client = pymongo.MongoClient(url)
        database = client['lab2db']
        collection = database['notes']

        result = collection.find({})
        result = dumps(result)
       
        return func.HttpResponse(result, mimetype="application/json", charset="utf-8", status_code=200)

    except:
            return func.HttpResponse("Bad Request", status_code=400)
   
