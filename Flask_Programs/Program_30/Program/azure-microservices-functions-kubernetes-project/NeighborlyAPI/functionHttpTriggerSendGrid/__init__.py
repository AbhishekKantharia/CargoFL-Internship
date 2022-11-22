import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

  try:

    value = "Sending message from my Azure Functions HTTP Trigger"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "kathleen.elizabeth.west@gmail.com"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Message successfully sent.")

  except:
            logging.exception("message")
            return func.HttpResponse("Bad Request", status_code=400)