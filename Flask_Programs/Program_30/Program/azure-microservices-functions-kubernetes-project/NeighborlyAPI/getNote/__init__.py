import logging
import azure.functions as func
import json
import os
import pymongo
from bson.json_util import loads, dumps
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    try:
 
        id = req.params.get('id')
        url = os.environ["myAzureCosmosMongoDBConnectionString"]
        client = pymongo.MongoClient(url)
        database = client['lab2db']
        collection = database['notes']

        query = {'_id': ObjectId(id)}
        result = collection.find_one(query)
        result = dumps(result)
        
        return func.HttpResponse(result, mimetype="application/json", charset="utf-8", status_code=200)

    except:
            logging.exception("message")
            return func.HttpResponse("Bad Request", status_code=400)
