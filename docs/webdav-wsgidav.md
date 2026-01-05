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
When Microsoft is preventing SMB traffic, there is an alternative: running SMB over HTTP with `WebDav`. `WebDAV` [(RFC 4918)](https://datatracker.ietf.org/doc/html/rfc4918) is an extension of HTTP, the internet protocol that web browsers and web servers use to communicate with each other. The `WebDAV` protocol enables a webserver to behave like a fileserver, supporting collaborative content authoring. `WebDAV` can also use HTTPS.

When you use `SMB`, it will first attempt to connect using the SMB protocol, and if there's no SMB share available, it will try to connect using HTTP.

## Installation

Download from github repo: [https://github.com/mar10/wsgidav](https://github.com/mar10/wsgidav).


```bash
sudo pip install wsgidav cheroot

# Another method for installing it:
pip3 install wsgidav
```

## Basis usage

Create a folder to serve from there:

```bash
mkdir /home/kali/webdav

cd /home/kali/webdav

wsgidav --host=0.0.0.0 --port=80 --root=/home/kali/webdav --auth=anonymous 
```
