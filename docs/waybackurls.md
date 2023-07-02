---
title: waybackurls
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - reconnaissance
  - tools
---

# waybackurls

[waybackurls](https://github.com/tomnomnom/waybackurls) inspects back URLs saved by Wayback Machine and look for specific keywords. 

## Installation

```shell-session
go install github.com/tomnomnom/waybackurls@latest
```


## Basic usage

```shell-session
waybackurls -dates https://example.com > waybackurls.txt

cat waybackurls.txt
```
