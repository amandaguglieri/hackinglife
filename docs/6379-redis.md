---
title: 6379 redis
author: amandaguglieri
draft: false
TableOfContents: true
---

## Description

Redis (REmote DIctionary Server) is an open-source advanced NoSQL key-value data store used as a database, cache, and message broker. The Redis command line interface (redis-cli) is a terminal program used to send commands to and read replies from the Redis server. Redis popularized the idea of a system that can be considered a store and a cache at the same time.Redis is an open-source, in-memory key-value data store. Whether you’ve installed Redis locally or you’re working with a remote instance, you need to connect to it in order to perform most operations.


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

First thing to know is that you can use “telnet” (usually on Redis default port 6379)

```bash
telnet localhost 6379
```

If you have redis-server installed locally, you can connect to the Redis instance with the redis-cli command.

If you want to connect to a remote Redis datastore, you can specify its host and port numbers with the -h and -p flags, respectively. Also, if you’ve configured your Redis database to require a password, you can include the -a flag followed by your password in order to authenticate:

```bash
redis-cli -h host -p port_number -a password
```

If you’ve set a Redis password, clients will be able to connect to Redis even if they don’t include the -a flag in their redis-cli command. However, they won’t be able to add, change, or query data until they authenticate. To authenticate after connecting, use the auth command followed by the password:

```bash
auth password
```

If the password passed to auth is valid, the command will return OK. Otherwise, it will return an error.


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

Redis has a concept of separated namespaces called “databases”. You can select the database number you want to use with “SELECT”. By default the database with index 0 is used. 

```redis
# Select database
redis 127.0.0.1:6379> SELECT 1

# To see all keys in a given database. First, you enter in it with "SELECT <number>" and then
redis 127.0.0.1:6379> keys *

# To retrieve a specific key
redis 127.0.0.1:6379> get flag
```


