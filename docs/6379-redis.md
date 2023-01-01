---
title: 6379 redis
draft: false
TableOfContents: true
---

## Description

Redis (REmote DIctionary Server) is an open-source advanced NoSQL key-value data store used as a database, cache, and message broker. The data is stored in a dictionary format having key-value pairs. It is typically used for short term storage of data that needs fast retrieval. Redis does backup data to hard drives to provide consistency.

### The server

Redis runs as server-side software so its core functionality is in its server component. The server listens for connections from clients, programmatically or through the command-line interface.

### The CLI
The command-line interface (CLI) is a powerful tool that gives you complete access to Redis’s data and its functionalities if you are developing a software or tool that needs to interact with it.

### Database
The database is stored in the server's RAM to enable fast data access. Redis also writes the contents of the database to disk at varying intervals to persist it as a backup, in case of failure.


## To install it in your kali

### Prerequisites

If you're running a very minimal distribution (such as a Docker container) you may need to install lsb-release first:

```bash
sudo apt install lsb-release
```

Add the repository to the apt index, update it, and then install:

```bash
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update

sudo apt-get install redis
```

## To connect to a terminal

```bash
redis-cli -h 10.129.124.88
```

Upon a successful connection with the Redis server, we should be able to see a prompt in the terminal as:

```
IP:6379>
```

One of the basic Redis enumeration commands is info which returns information and statistics about the Redis server. 

## Dumping Database

Inside Redis the databases are numbers starting from 0. You can find if anyone is used in the output of the command info inside the "Keyspace" chunk:

```
# Keyspace
db0:keys=4, expires=0, avg_ttl=0
db1:keys=2, expires=0, avg_ttl=0
```

Or you can just get all the keyspaces (databases) with:

```redis
INFO keyspace
```

In that example the database 0 and 1 are being used. Database 0 contains 4 keys and database 1 contains 1. By default Redis will use database 0. In order to dump for example database 1 you need to do:

```redis
SELECT 1
# [ ... Indicate the database ... ]

KEYS *
# [ ... Get Keys ... ]

GET <KEY>
# [ ... Get Key ... ]
```


