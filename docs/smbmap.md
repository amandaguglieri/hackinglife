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