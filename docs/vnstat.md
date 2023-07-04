---
title: vnstat - Monitoring network impact
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - network
  - bash
  - tools
---

# vnstat - Monitoring network impact


## Installation

```bash
sudo apt install vnstat    
```


## Basic usage

Monitor the `eth0` network adapter before running a Nessus scan:

```shell-session
sudo vnstat -l -i eth0
```