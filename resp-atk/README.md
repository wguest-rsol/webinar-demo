# Resp-atk

## Description
This container provides a terminal to use the Responder tool.


## Build Information
Build the container with the command:

```sh
docker build -t "resp-atk:latest" .
```

## Run Information
To run the container, use the command:

```sh
docker run --rm -d -p 2223:22 resp-atk:latest
```

## Connection Information
You can connect to the container using the private key.

```sh
ssh -i id_rsa user@localhost -p 2223
```

Responder is in the /opt/ directory. You need to be root to run the command.

```sh
sudo su
```
The password for the user account is: HelloWorld!

## Solution
To run responder as root, use the command:
```sh
python3 /opt/Responder/Responder.py -I eth0 -v
```

Waiting 30 seconds should produce a hash.