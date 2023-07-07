	---
title: Powerview.ps1 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
  - enumeration
  - reconnaissance
  - tools
---

# Powerview.ps1 

Run from powershell.

Download from PowerSploit Github repo: [https://github.com/ZeroDayLab/PowerSploit](https://github.com/ZeroDayLab/PowerSploit).

```ps
Import-Module .\Powerview.ps1 
```


## Enumeration cheat sheet

```ps
# Enumerate users
Get-NetUser

# Enumerate computers in the domain
Get-NetComputer 
Get-NetComputer | select name
Get-NetComputer -OperatingSystem "Linux"

# Display info of current domain. Pay attention to the element forest, to see if there is a bigger structure
Get-NetDomain

# Get the ID for the current Domain (useful later for crafting Golden tickets)
Get-DomainID

# Display policies for the Domain and accounts, including for instance LockoutBadAccounts
Get-DomainPolicy

# Display Domain controller
Get-NetDomainController

# List users in the domain. Useful to search for non expiring passwords, groups belonging, what's their SPN, last time they changed their password... 
Get Net-User
Get Net-User john.doe

# List users associated to an Service Principal Name (SPN) 
Get Net-User -SPN

# List groups in the domain
Get-NetGroup

# List Group Policy Objects in domain
Get-NetGPO

# List Domain Trusts
Get-NetDomainTrust
```
