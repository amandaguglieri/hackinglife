---
title: Lazagne 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - passwords
---
# Lazagne

The **LaZagne project** is an open source application used to **retrieve lots of passwords** stored on a local computer. Each software stores its passwords using different techniques (plaintext, APIs, custom algorithms, databases, etc.). This tool has been developed for the purpose of finding these passwords for the most commonly-used software.

## Installation

Download from github repo: [https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne).

Download a standalone copy from [https://github.com/AlessandroZ/LaZagne/releases/](https://github.com/AlessandroZ/LaZagne/releases/).


## Basic usage

Once Lazagne.exe is on the target, we can open command prompt or PowerShell, navigate to the directory the file was uploaded to, and execute the following command:

```cmd-session
start .\lazagne.exe all
# -vv: to study what it is doing in the background.
```

From Linux, go to `/LaZagne/Linux` and run:

```shell-session
python3 laZagne.py all

# Also, for browsers:
python3 laZagne.py browsers
```