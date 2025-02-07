# neo4j-ad

## Description
This container runs a neo4j database with Bloodound data.

## Build Information
Build the container using the command:

```sh
docker build -t "neo4j-ad:latest" .
```

## Run Information
Run the container using the command

```sh
docker run -d --rm -p 7687:7687 neo4j-ad:latest
```

## Connection Information
Launch bloodhound. On kali it is just the word "bloodhound":
```sh
bloodhound
```

Connection information:
Neo4j URL: bolt://localhost:7687
Username: neo4j
Password: HelloWorld!


## Solution
**First Question - AS-REP user**
1. Select "Analysis" tab
2. Select "Find AS-REP Roastable Users"
3. Select the "BLAB" node.
4. The Object ID is in the properties information.

**Second Question - Kerberoast**
1. Select "Analysis" tab
2. Select "List all Kerberoastable Accounts"
3. Select the SPLUNKSVC node
4. The Object ID is in the properties information.


**Third Question - GMSA**
1. From question 2, stay focused on the SPLUNKSVC node
2. From the "Node Info" page, select "Inbound Control Rights"
3. Find the edge titled, "ReadGMSAPassword"
4. Select the "Server Administrators" group
5. Select "Direct Members"
6. Select the "SDAVIS" user and review Object ID.