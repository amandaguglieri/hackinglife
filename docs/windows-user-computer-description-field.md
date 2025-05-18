---
title: Windows User/Computer Description Field
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
---
# Windows User/Computer Description Field

Though more common in Active Directory, it is possible for a sysadmin to store account details (such as a password) in a computer or user's account description field.

```powershell
Get-LocalUser 
```

We can also enumerate the computer description field via PowerShell using the [Get-WmiObject](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1) cmdlet with the [Win32_OperatingSystem](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-operatingsystem) class.

```powershell
Get-WmiObject -Class Win32_OperatingSystem | select Description
```