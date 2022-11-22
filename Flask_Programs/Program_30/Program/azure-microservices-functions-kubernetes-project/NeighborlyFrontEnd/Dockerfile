# For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.8-slim-buster

# Base the image on the built-in Azure Functions Python image
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7

ENV host:logger:consoleLoggingMode=always

WORKDIR /app
#COPY . /app

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

EXPOSE 5000

#RUN pip install -r requirements.txt
# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python"]
CMD ["app.py"]
