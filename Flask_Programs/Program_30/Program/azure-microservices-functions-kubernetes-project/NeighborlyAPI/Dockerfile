# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    host:logger:consoleLoggingMode=always \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    myAzureCosmosMongoDBConnectionString=<YOUR_ACCESS_KEY>

COPY requirements.txt /

EXPOSE 8080

RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot
