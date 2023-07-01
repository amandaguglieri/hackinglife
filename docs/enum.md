---
title: enum
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - enumeration
---

# enum

Enum is a console-based Win32 information enumeration utility. Using null sessions, enum can retrieve userlists, machine lists, sharelists, namelists, group and member lists, password and LSA policy information. enum is also capable of a rudimentary brute force dictionary attack on individual accounts. 

## Installation

Download it from: [https://packetstormsecurity.com/search/?q=win32+enum&s=files](https://packetstormsecurity.com/search/?q=win32+enum&s=files).

## Basic commands
  
```bash
# Enumerates shares
enum.exe -s $ip     

# Enumerates users
enum.exe -u $ip

# Displays the password policy in case you need to mount a network authentification attack
enum.exe -p $ip 
```

