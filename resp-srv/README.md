# Resp-srv

## Description
This container is responsible for issuing LLMNR queries. It sends a query every 30 seconds.

## Build Information
To build the container use the following command:
```sh
docker build -t "resp-srv:latest" .
```

## Run Information


```sh
# Example run command
docker run -d --rm resp-srv:latest
```