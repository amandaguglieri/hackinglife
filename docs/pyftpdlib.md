---
title: pyftpdlib - A ftp server written in python 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - ftp server
  - python
---

# pyftpdlib

A simple FTP server written in python

## Installation

```bash
sudo pip3 install pyftpdlib
```


## Basic usage

By default pyftpdlib uses port 2121. With --port flag, indicate a different port. Anonymous authentication is enabled by default if we don't set a user and password.

```bash
sudo python3 -m pyftpdlib --port 21
```

With the option `--write` to allow clients to upload files to our attack host:


```bash
sudo python3 -m pyftpdlib --port 21 --write
```