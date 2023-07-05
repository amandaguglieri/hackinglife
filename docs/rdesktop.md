---
title: rdesktop 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - windows
  - rdp
---

# rdesktop

rdesktop is an open source UNIX client for connecting to Windows Remote Desktop Services, capable of natively speaking Remote Desktop Protocol (RDP) in order to present the user's Windows desktop.

## Installation

Preinstalled in Kali.

```bash
sudo apt-get install rdesktop
```


## Basic usage

```bash
rdesktop $ip

# Mounting a Linux Folder Using rdesktop
rdesktop $ip -d <domain> -u <username> -p <'Password0@'> -r disk:linux='/home/user/rdesktop/files'
```
