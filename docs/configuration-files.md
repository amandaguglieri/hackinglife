---
title: Configuration files
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - linux
---

# Configuration files for some juicy services

## Exposed Credentials

Look for files with read permission and see if they contain any exposed credentials. This is very common with configuration files, log files, and user history files (bash_history in Linux and PSReadLine in Windows). 

```shell-session
/var/www/html/config.php
```
