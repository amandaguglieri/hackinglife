---
title: arjun
author: amandaguglieri
draft: false
TableOfContents: true
tag: api
---

# Arjun


## Installation


```bash
sudo git clone https://github.com/s0md3v/Arjun.git
```

Other ways:

```bash
pip3 install arjun
```


## Basic commands


```bash
# Run arjun againts a single URL
arjun -u https://api.example.com/endpoint

# arjun will provide you with likely parameters from a wordlist. Its results are based on the deviation of response lengths/codes
arjun --headers "Content-Type: application/json" -u http://api.example.com/register -m JSON --include='{$arjun}' --stable
# -m Get method parameters GET/POST/JDON/XML
# -i Import targets (a txt list)
# --include Specify injection point, for example:
		#  --include='<?xml><root>$arjun$</root>
		#  --include='{"root":{"a":"b",$arjun$}}'
```


Awesome wiki about arjun usage: [https://github.com/s0md3v/Arjun/wiki/Usage](https://github.com/s0md3v/Arjun/wiki/Usage).
