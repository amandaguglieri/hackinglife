---
title: Linux Privilege Checker
author: amandaguglieri
draft: false
TableOfContents: true
tags: pentesting, linux pentesting, privilege escalation
---

# Linux Privilege Checker 

Linux privilege checker is an enumeration tool with privilege escalation checking capabilities. 


## Installation

Download from: [http://www.securitysift.com/download/linuxprivchecker.py](http://www.securitysift.com/download/linuxprivchecker.py)

## Basic commands

You can run it on your system by typing:

```bash
 ./linuxprivchecker.py 
```

or 

```bash
python linuxprivchecker.py
```

Also, a nice way to serve this payload is copying this python file into /var/www/html and then run:

```bash
service apache2 start
```



