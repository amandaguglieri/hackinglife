---
title: DNSRecon - DNS Enumeration and Scanning Tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---

# DNSRecon

Preinstalled with Linux: dsnrecon is a simple python script that enables to gather  DNS-oriented  information on a given target.


## Basic usage


```bash
dnsrecon -d example.com 

# Another way to do it
dnsrecon -d example.com -t std
# -t: type os scan to perform. Standard one is std.


dnsrecon -d example.com -D wordlist.txt -t brt
# -t brt: type bruteforce
# -D: wordlist of subdomains.
# -d: domain
```

