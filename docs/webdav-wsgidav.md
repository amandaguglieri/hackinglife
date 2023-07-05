---
title: WebDav- WsgiDAV - A generic and extendable WebDAV server 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - server
---

# WsgiDAV: A generic and extendable WebDAV server 

A generic and extendable WebDAV server written in Python and based on WSGI.

## Installation

Download from github repo: [https://github.com/mar10/wsgidav](https://github.com/mar10/wsgidav).


```bash
sudo pip install wsgidav cheroot
```

## Basis usage

```bash
sudo wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous 
```
