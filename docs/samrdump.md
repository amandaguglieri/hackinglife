---
title: SAMRDump
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting windows 
---

# SAMRDump

[Impacket](impacket.md)’s [samrdump.py](https://github.com/fortra/impacket/blob/master/examples/samrdump.py) communicates with the Security Account Manager Remote (SAMR) interface to list system user accounts, available resource shares, and other sensitive information.

## Basic commands

```bash
# path: /usr/share/doc/python3-impacket/examples/samrdump.py
python3 samrdump.py $ip
```
