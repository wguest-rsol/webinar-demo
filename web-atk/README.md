# Web-atk container

## Description
This container provides the gobuster tool for demo 1

## Build Information
Build the container using the following instruction:

```sh
docker build -t "web-atk:latest" .
```

## Run Information
The run command can be used to use the container:

```sh
docker run -p 2222:22 -d --rm web-atk:latest
```

## Connection Information
Once running, the container can be connected to over SSH. 
The credentials to connect are:

user: attacker
password: HelloWorld!

From the host machine:
```sh
ssh attacker@localhost -p 2222
```

## Solution
Once connected, the gobuster tool can be used to enumerate the web server. To find the web server IP address, either inspect the container in docker or scan port 9000 on the local host.

```sh
gobuster dir -u http://target -w /home/attacker/common.txt -x "php"
```