import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            #url = "localhost"  # TODO: Update with appropriate MongoDB connection information
            url = os.environ["myAzureCosmosMongoDBConnectionString"]
            client = pymongo.MongoClient(url)
            database = client['lab2db']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
