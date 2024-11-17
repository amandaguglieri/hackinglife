---
title: fping - An improved ping tool 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - scanning
  - reconnaissance
  - ping
---
# fping - An improved ping tool

[https://fping.org/](https://fping.org/)

Linux tool which is an improved version of the ping utility:

```bash
fping -a -g -s -q $ipRange
fping -agsq $ipRange
# -a: forces the tool to show only alive hosts.
# -g: tells the tool we want to perform a ping sweep instead of a standard ping.
# -s: prints stats at the end of the scan
# -q: not to show per-target results
```

Also you can use the [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing): 

```bash
fping -a -g 10.54.12.0/24
fping -a -g 10.54.12.0 10.54.12.255
```

