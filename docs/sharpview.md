---
title: SharpView
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
# SharpView

(C#)   - Doesn't support filtering using Pipeline 
SharpView is a .NET port of  [PowerView](powerview.md). Many of the same functions supported by PowerView can be used with SharpView.

## Installation

Download github repo from: [https://github.com/tevora-threat/SharpView/](https://github.com/tevora-threat/SharpView/).


## Basic commands

```powershell
# Obtain help about a command
\SharpView.exe Get-DomainUser -Help

# Get information about a given user
.\SharpView.exe Get-DomainUser -Identity $username
```