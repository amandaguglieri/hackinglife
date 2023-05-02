---
title: httprint - A web server fingerprinting tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - enumeration
  - server enumeration
  - web server
  - fingerprinting
---

# httprint - A web server fingerprinting tool 

httprint is a web server fingerprinting tool. It relies on web server characteristics to accurately identify web servers, despite the fact that they may have been obfuscated by changing the server banner strings, or by plug-ins such as mod_security or servermask. 

httprint can also be used to detect web enabled devices which do not have a server banner string, such as wireless access points, routers, switches, cable modems, etc. 

```bash
httprint -P0 -h <target hosts> -s <signature file>
# -P0 for avoiding pinging the host
# -h target host
# -s set the signature file to use
```
