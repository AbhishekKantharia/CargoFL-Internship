# NeighborlyFrontEnd

This file lists some helpful notes for the project.

## Docker Build  

docker build -t neighborly-frontend .

## Docker Run

docker run -p 5000:5000 -it neighborly-frontend

## View Docker Container

http://localhost:5000/

## Azure Container Registry

### Login

docker login

az acr login --name <azure_container_registry_name>

### Tagging

docker tag neighborly-frontend <azure_container_registry_name>.azurecr.io/neighborly-frontend

### Push
docker push <azure_container_registry_name>.azurecr.io/neighborly-frontend