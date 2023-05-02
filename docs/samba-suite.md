---
title: Samba Suite
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# Samba Suite

It’s used to enumerate info. It might be used in a [Null session attack](windows-null-session-attack.md).


## Installation

Download it from: https://www.samba.org/

## Basic commands

1.  **Enumerate File Server services**: 

```bash
nmblookup -A <target IP>
```

2.  Also with the smbclient we can **enumerate the shares** provides by a host:  

```bash
smbclient -L //<target IP> -N

# -L  Look at what services are available on a target
# <targetIP> Prepend the two slahes
# -N  Force the tool not to ask for a password
```

3.  Connect:

```bash
smbclient \\<tt IP>\sharedfolder -N
```

Be careful, sometimes the shell removes the slashes and you need to escape them.

4.  Once connected you can browse with the smb command line. To see allowed commands: help 
5.  When you know the path of a file and you want to retrieve it:
	- from kali: 
	```bash
	smbget smb://<target IP>/SharedFolder/flag_1.txt
	```
	- from  smb command line: 
	```smb
	get flag_1.txt
	```
