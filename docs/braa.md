---
title: braa - SNMP scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - enumeration
  - snmp
  - port 161
  - tools
---

# braa - SNMP scanner


## Installation

Download from the github repo: [https://github.com/mteg/braa](https://github.com/mteg/braa)

Also:

```shell-session
sudo apt install braa
```


## Basic usage


```shell-session
braa <community string>@<IP>:.1.3.6.*   

	# Example:
	# braa public@10.129.14.128:.1.3.6.*
```
