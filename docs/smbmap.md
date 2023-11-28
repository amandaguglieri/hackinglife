---
title: smbmap
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - smb
  - pass-the-hash
  - file upload
  - rce
  - tools
---

# SMBMap

SMBMap allows users to enumerate samba share drives across an entire domain. List share drives, drive permissions, share contents, upload/download functionality, file name auto-download pattern matching, and even execute remote commands.

## Installation

Installation from [https://github.com/ShawnDEvans/smbmap](https://github.com/ShawnDEvans/smbmap)

```bash
sudo pip3 install smbmap
smbmap
```


## Basic usage


```bash
# Enumerate network shares and access associated permissions.
smbmap -H $ip

# # Enumerate network shares and access associated permissions with recursivity
smbmap -H $ip -r

# Download a file from a specific share folder
smbmap -H $ip --download "folder\file.txt"

# Upload a file to a specific share folder
smbmap -H $ip --upload originfile.txt "targetfolder\file.txt"


```