import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
   
    request = req.get_json()

    if request:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = os.environ["myAzureCosmosMongoDBConnectionString"]
            client = pymongo.MongoClient(url)
            database = client['lab2db']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )