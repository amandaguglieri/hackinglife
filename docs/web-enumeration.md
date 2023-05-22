---
title: Web enumeration
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# Web enumeration


## Banner Grabbing / Web Server Headers


```shell-session
curl -IL https://<TARGET>
```


## Tools

- Enumeration of directories, as3 buckets, dns... : [Gobuster](gobuster.md)
- Fuzzing: [ffuf](ffuf.md), [Burpsuite](burpsuite.md)
- Version of web servers, supporting frameworks, and applications using the command-line: whatweb.
