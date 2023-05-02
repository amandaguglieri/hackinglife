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

enum4linux is used to exploit [null session attacks](windows-null-session-attack.md) by using this PERL script. Esentially it does something similar to  [winfo](winfo.md) and [enum](enum.md).

## Installation

Preinstalled in kali.

## Basic commands

```bash
# Enumerate shares
enum4linux.exe -S <target IP> 

# Enumerate users
enum4linux.exe -U <target IP>     

# Enumerate machine list
enum4linux.exe -M <target IP>

# Display the password policy in case you need to mount a network authentification attack
enum4linux.exe -enuP<target IP>

# Specify username to use (default “”)
enum4linux.exe -u <target IP>

# Specify password to use (default “”)
enum4linux.exe -p <target IP>     

# Also you can use brute force by adding a file
enum4linux.exe -s /usr/share/enum4linux/share-list.txt <target IP>   
  
# Do a nmblookup (similar to nbtstat)
enum4linux.exe -n <target IP>  
# In the result we see the <20> flag which means there are resources shared

# Enumerates the password policy in the remote system. This is useful to use brute force
enum4linux.exe -P <target IP>

# Enumerates available shares
enum4linux.exe -s <target IP>   //     
```

If you want to run all these commands in one line:

```
enum4linux.exe -a <target IP>
```
