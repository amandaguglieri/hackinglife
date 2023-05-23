---
title: whatweb - A web scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# whatweb

WhatWeb recognises web technologies including content management systems (CMS), blogging platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded devices.

## Installation

Already installed in Kali.

Download from: [https://github.com/urbanadventurer/WhatWeb](https://github.com/urbanadventurer/WhatWeb)


## Basic usage

```bash
# version of web servers, supporting frameworks, and applications
whatweb <IP/TARGETURL>

# Automate web application enumeration across a network.
whatweb --no-errors 10.10.10.0/24
```

