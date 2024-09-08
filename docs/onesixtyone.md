---
title: onesixtyone - Fast and simple SNMP scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - enumeration
  - snmp
  - port 161
  - tools
---

# onesixtyone - Fast and simple SNMP scanner

[See SNMP for details about the protocol](161-162-snmp.md).

## Installation

Download from github repo: [https://github.com/trailofbits/onesixtyone](https://github.com/trailofbits/onesixtyone).

```shell-session
sudo apt install onesixtyone
```

## Basic usage

```shell-session
onesixtyone -c /usr/share/seclists/Discovery/SNMP/snmp.txt $ip
```