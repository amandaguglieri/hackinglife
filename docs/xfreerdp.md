---
title: xfreerdp 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - windows
  - rdp
---

# xfreerdp

[xfreerdp](https://linux.die.net/man/1/xfreerdp) is an X11 [Remote Desktop Protocol (RDP)](3389-rdp.md) client which is part of the FreeRDP project. An RDP server is built-in to many editions of Windows. 

## Installation

To install xfreerdp, proceed with the following command:

```bash
sudo apt-get install freerdp2-x11
```

## Basic commands

```bash
# No password indicated. When prompted for one, click Enter and see if it allows us to login
xfreerdp [/d:domain] /u:<username> /v:$ip

xfreerdp [/d:domain] /u:<username> /p:<password> /v:$ip
# /v:{target_IP} : Specifies the target IP of the host we would like to connect to.

xfreerdp [/d:domain] /u:<username> /pth:<hash> /v:$ip
# /pth:<hash>   Pass the hash


```

