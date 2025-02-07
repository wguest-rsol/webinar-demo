# Web-demo

## Description
Runs the web server for demos 1 and 2.

## Build Information
Build the container using the following instruction

```sh
docker build -t "web-demo:latest" .
```

## Run Information
The container can be run using the command

```sh
docker run -p 9000:80 -d --rm web-demo:latest
```

## Connection Information
On the host machine, the web server can be accessed on http://localhost:9000
