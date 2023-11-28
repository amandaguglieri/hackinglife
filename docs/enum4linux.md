---
title: enum4linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - enumeration
---

# enum4linux

enum4linux is used to exploit [null session attacks](windows-null-session-attack.md) by using this PERL script. The [original tool](https://github.com/CiscoCXSecurity/enum4linux) was written in Perl and [rewritten by Mark Lowe in Python](https://github.com/cddmp/enum4linux-ng). Essentially it does something similar to  [winfo](winfo.md) and [enum](enum.md).

## Installation

Preinstalled in kali. 
## Basic commands

```bash
# Enumerate shares
enum4linux.exe -S $ip

# Enumerate users
enum4linux.exe -U $ip     

# Enumerate machine list
enum4linux.exe -M $ip

# Display the password policy in case you need to mount a network authentification attack
enum4linux.exe -enuP $ip

# Specify username to use (default “”)
enum4linux.exe -u $ip

# Specify password to use (default “”)
enum4linux.exe -p $ip     

# Also you can use brute force by adding a file
enum4linux.exe -s /usr/share/enum4linux/share-list.txt $ip  
  
# Do a nmblookup (similar to nbtstat)
enum4linux.exe -n $ip  
# In the result we see the <20> flag which means there are resources shared

# Enumerates the password policy in the remote system. This is useful to use brute force
enum4linux.exe -P $ip

# Enumerates available shares
enum4linux.exe -s $ip     
```

If you want to run all these commands in one line:

```
enum4linux.exe -a $ip
```
