---
title: subfinder
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---
# Subfinder

`subfinder` is a subdomain discovery tool that returns valid subdomains for websites, using passive online sources. It has a simple, modular architecture and is optimized for speed. `subfinder` is built for doing one thing only - passive subdomain enumeration, and it does that very well.

This tool can scrape subdomains from open sources like [DNSdumpster](https://dnsdumpster.com/). 
## Installation

**Repo**: [https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) 

```bash
sudo apt install subfinder
```


## Basic commands

```shell-session
subfinder -d inlanefreight.com -v
```