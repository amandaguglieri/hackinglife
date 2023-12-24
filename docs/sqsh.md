---
title: sqsh
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - cheat sheet
  - mssql
---

## Installation

Pre-installed in Kali. Used to interact with MSSQL (Microsoft SQL Server) from Linux. 


```shell-session
 # Connect to mssql server
 sqsh -S $IP -U username -P Password123 -h
 # -h: disable headers and footers for a cleaner look.

# When using Windows Authentication, we need to specify the domain name or the hostname of the target machine. If we don't specify a domain or hostname, it will assume SQL Authentication.
sqsh -S $ip -U .\\<username> -P 'MyPassword!' -h
# For windows authentication we can use  SERVERNAME\\accountname or .\\accountname

```


When connected to msSQL, all commands will be executed after the GO command.