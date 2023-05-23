---
title: LinEnum - A tool to scan Linux system
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - linux pentesting
  - enumeration
---

# LinEnum - A tool to scan Linux system


## Installation

Clone github repo: [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)


## Basic usage

```shell-session
./LinEnum.sh -s-r report -e /tmp/ -t
# -k: Enter keyword
# -e: Enter export location
# -t: Include thorough (lengthy) tests
# -s: Supply current user password to check sudo perms (INSECURE)
# -r Enter report name
```
