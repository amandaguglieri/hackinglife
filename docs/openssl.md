---
title: openSSL
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - openssl
---

# openSSL

```bash
openssl s_client -connect target.site:443
HEAD / HTTP/1.0
```


## Basic usage


```bash

# Pwnbox - Create a Self-Signed Certificate
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'
```