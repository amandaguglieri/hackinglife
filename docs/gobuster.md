---
title: gobuster
author: amandaguglieri
draft: false
TableOfContents: true
---

# gobuster

Great tool to brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). Also, dictionaries are not API-specific. But here are some commands for Gobuster:

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 401 
# -b flag is to exclude from results an specific http response`
```