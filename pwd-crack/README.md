# pwd-crack

## Description
This machine provides hashcat and john to crack passwords. The "rockyou" wordlist is also provided.

***Known Issue***
Attempting to run this on an AMD PC does not work with hashcat.

## Build Information
Building the container is done with the command:

```sh
docker build -t "pwd-crack:latest" .
```

## Run Information
To run the container use the following command:
```sh
docker run -d --rm -p 2224:22 pwd-crack:latest
```

## Connection Information
To connect to the container, use the credentials:
- User: attacker
- Password: HelloWorld!

```sh
ssh attacker@localhost -p 2224
```

## Solution
To crack all four password hashes, here are the techniques to be used.

1. Crack using rockyou wordlist
2. Crack using a mask and the company name "Arctiq"
    hashcat -a 0 -m 0 -i --increment-min 6 hashes.txt -1 aA@rRtTiI1\!qQ ?1?1?1?1?1?1?1
3. Crack using list_maker.py with seasons and years.