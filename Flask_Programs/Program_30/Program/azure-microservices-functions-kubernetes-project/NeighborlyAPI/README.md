# NeighborlyAPI

Helpful tricks and commands

## Docker Build  

docker build -t neighborly-api .

## Docker Run

docker run -p 8080:80 -it neighborly-api

## View Docker Container

http://localhost:8080/

## Azure Container Registry

Example Azure Container Registry Name: appregistrykwest

### Login

docker login

az acr login --name appregistrykwest

### Tagging 
docker tag neighborly-api appregistrykwest.azurecr.io/neighborly-api

### Push
docker push appregistrykwest.azurecr.io/neighborly-api

## Kubernetes

Example Kubernetes Name: azure-functions-cluster

### Get Credentials

az aks get-credentials --name azure-functions-cluster --resource-group udacitypractice

### Authenticate with Azure Container Registry from Azure Kubernetes Service

Example Azure Container Registry Name: appregistrykwest

This is a very important step!

https://docs.microsoft.com/en-us/azure/aks/cluster-container-registry-integration

az aks update -n azure-functions-cluster -g udacitypractice --attach-acr appregistrykwest

### Install

func kubernetes install --namespace keda 

### Deploy Options

These are instructions how to make your own deploy.yml file and apply to your Kubernetes service

func kubernetes deploy --name azure-functions-cluster --image-name appregistrykwest.azurecr.io/neighborly-api --dry-run > deploy.yml

func kubernetes deploy --name azure-functions-cluster --image-name appregistrykwest.azurecr.io/neighborly-api —polling-interval 3 —cooldown-period 5

kubectl apply -f deploy.yml
