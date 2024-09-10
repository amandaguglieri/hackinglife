---
title: dnsenum - A tool to enumerate DNS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---

# dnsenum - A tool to enumerate DNS

multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.


## Installation

Download from the github repo: [https://github.com/fwaeytens/dnsenum](https://github.com/fwaeytens/dnsenum).

## Basic usage

 Used for active fingerprinting:

```
dnsenum domain.com
```

One cool thing about dnsenum is that it can perform dns transfer zone, like [dig]](dig.md). 

It performs DNS brute force with /usr/share/dnsenum/dns.txt.

```bash
dnsenum --enum example.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -r
# -f Indicate the wordlist file
```