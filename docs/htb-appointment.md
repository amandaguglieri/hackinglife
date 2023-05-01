---
title: Appointment - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---


# Appointment - A HackTheBox machine


```bash
nmap -sC -A $ip -Pn
```

Only port 80 is open.

It's a login panel with an SQL injection vulnerability.

To access, enter in username: 1' OR '1'='1';#



