---
title: fping - An improved ping tool 
author: amandaguglieri
draft: false
TableOfContents: true
tag: scanning,reconnaissance,ping
---

# fping - An improved ping tool

Linux tool which is an improved version of the ping utility:

```bash
fping -a -g IPRANGE
# -a: forces the tool to show only alive hosts.
# -g: tells the tool we want to perform a ping sweep instead of a standard ping.
```

Also you can use the [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing): 

```bash
fping -a -g 10.54.12.0/24
fping -a -g 10.54.12.0 10.54.12.255
```

