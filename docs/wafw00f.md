---
title: WafW00f - A firewall scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# WafW00f - A firewall scanner


[WafW00f](https://github.com/EnableSecurity/wafw00f) is a web application firewall (`WAF`) fingerprinting tool that sends requests and analyses responses to determine if a security solution is in place. 


## Installation

We can install it with the following command:

```shell-session
sudo apt install wafw00f -y
```

## Basic usage

```shell-session
wafw00f -v https://www.example.com

# -a: check all possible WAFs in place instead of stopping scanning at the first match.
# -i: read targets from an input file 
# -p proxy the requests 
```