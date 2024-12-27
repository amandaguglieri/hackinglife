---
title: Snaffler - a tool for enumerating creds and shares in Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - windows
  - rdp
---
# Snaffler, a tool for enumerating creds and shares in Active Directory

[Snaffler](https://github.com/SnaffCon/Snaffler) is a tool for **pentesters** and **red teamers** to help find delicious candy needles (creds mostly, but it's flexible) in a bunch of horrible boring haystacks (a massive Windows/AD environment). _Broadly speaking_ - it gets a list of Windows computers from Active Directory, then spreads out its snaffly appendages to them all to figure out which ones have file shares, and whether you can read them.


## Basic usage

```bash
Snaffler.exe -s -d $domain -o snaffler.log -v data
# -s:  prints results to the console 
# -d: specifies the domain to search within
# -o: writes results to a logfile
# -v: verbosity level. "data" is best as it only displays results to the screen
```