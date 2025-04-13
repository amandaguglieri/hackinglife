---
title: Execution Policy bypasses
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# Execution Policy bypasses

Source: https://www.netspi.com/blog/technical-blog/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/

The PowerShell execution policy is the setting that determines which type of PowerShell scripts (if any) can be run on the system. By default it is set to “Restricted“, which basically means none. However, it’s important to understand that the setting was never meant to be a security control.

```powershell

# Check the execution policy:
Get-ExecutionPolicy

#  print the execution policy settings for each scope on a host.
Get-ExecutionPolicy -List
```

Example of output:

```
Scope ExecutionPolicy                                             ----- ---------------                                             MachinePolicy    Unrestricted
UserPolicy       Undefined
Process       Undefined
CurrentUser       Undefined
LocalMachine       Undefined  
```

## Use the "Bypass" Execution Policy Flag

```powershell
PowerShell.exe -ExecutionPolicy Bypass -File .runme.ps1
```

## Use the "Unrestricted" Execution Policy Flag

```powershell
PowerShell.exe -ExecutionPolicy UnRestricted -File .runme.ps1
```


## Set the ExecutionPolicy for the Process Scope

```
#This will change the policy for our current process using the -Scope parameter. Doing so will revert the policy once we vacate the process or terminate it. This is ideal because we won't be making a permanent change to the victim host.
Set-ExecutionPolicy Bypass -Scope Process	
```


## Set the ExecutionPolicy for the CurrentUser Scope via Command

```powershell
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted
```


## Set the ExecutionPolicy for the CurrentUser Scope via the Registry

```
HKEY_CURRENT_USERSoftwareMicrosoftPowerShell1ShellIdsMicrosoft.PowerShell
```