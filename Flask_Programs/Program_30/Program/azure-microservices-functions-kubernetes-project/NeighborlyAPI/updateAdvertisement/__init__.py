import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = os.environ["myAzureCosmosMongoDBConnectionString"]
            client = pymongo.MongoClient(url)
            database = client['lab2db']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            rec_id1 = collection.update_one(filter_query, update_query)

            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

