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
 
        request = req.get_json()
        if request:
            try:
                # add your connection string here
                url = os.environ["myAzureCosmosMongoDBConnectionString"]
                client = pymongo.MongoClient(url)
                database = client['lab2db']
                collection = database['notes']

                # replace the insert_one variable with what you think should be in the bracket
                collection.insert_one(request)

                # we are returnign the request body so you can take a look at the results
                return func.HttpResponse(req.get_body())

            except ValueError:
                return func.HttpResponse('Database connection error.', status_code=500)

        else:
            logging.exception("message")
            return func.HttpResponse(
                "Please pass the correct JSON format in the body of the request object",
                status_code=400
            )

    except:
            logging.exception("message")
            return func.HttpResponse("Bad Request", status_code=400)
