---
title: medusa 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute forcing
  - windows
  - passwords
---

# Medusa

Medusa is a speedy, parallel, and modular, login brute-forcer. The goal is to support as many services which allow remote authentication as possible. The author considers following items as some of the key features of this application:

## Installation 

Pre-installed in Kali.

```bash
wget http://www.foofus.net/jmk/tools/medusa-2.2.tar.gz
./configure
make
make install
```

## Basic usage


```bash
# Brute force FTP logging
medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h $IP -M ftp -n 2121
# -u: username
# -U: list of Usernames
# -p: password
# -P: list of passwords
# -h: host /IP
# -M: protocol to bruteforce
# -n: for a different non-default port. For instance, port 2121 for ftp 
```

