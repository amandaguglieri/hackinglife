---
title: evil-winrm 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - active directory
  - windows remote management
---

# Evil-WinRm

By default, installed on kali. [See winrm](5985-5986-winrm-windows-remote-management.md).


## Basic usage

Example from [HTB machine: Responder](htb-responder.md).

```bash
evil-winrm -i $ip -u <username -p <password>

evil-winrm -i <ip> -u Administrator -H "<passwordhash>"
# -H: Hash
```





