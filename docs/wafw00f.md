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

WAFW00F does the following:

- Sends a _normal_ HTTP request and analyses the response; this identifies a number of WAF solutions.
- If that is not successful, it sends a number of (potentially malicious) HTTP requests and uses simple logic to deduce which WAF it is.
- If that is also not successful, it analyses the responses previously returned and uses another simple algorithm to guess if a WAF or security solution is actively responding to our attacks.


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