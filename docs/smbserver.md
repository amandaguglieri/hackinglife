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

```bash
python3 smbserver.py -smb2support CompData /home/<nameofuser>/sharedfolder/
```

