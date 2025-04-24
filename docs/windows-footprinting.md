---
title: Footprinting Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
---
# Footprinting Windows

## System Information

```powershell
systeminfo
```

If `systeminfo` doesn't display hotfixes, they may be queriable with [WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) using the WMI-Command binary with [QFE (Quick Fix Engineering)](https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering) to display patches.

```
# In cmd
wmic qfe

# With powershell
Get-HotFix | ft -AutoSize
```

```cmd
# Tasklist: Using the tasklist command to look at running processes will give us a better idea of what applications are currently running on the system.
tasklist /svc
```

Print Windows version:

```powershell
[environment]::OSVersion.Version
```

It is essential to become familiar with standard Windows processes such as [Session Manager Subsystem (smss.exe)](https://en.wikipedia.org/wiki/Session_Manager_Subsystem), [Client Server Runtime Subsystem (csrss.exe)](https://en.wikipedia.org/wiki/Client/Server_Runtime_Subsystem), [WinLogon (winlogon.exe)](https://en.wikipedia.org/wiki/Winlogon), [Local Security Authority Subsystem Service (LSASS)](https://en.wikipedia.org/wiki/Local_Security_Authority_Subsystem_Service), and [Service Host (svchost.exe)](https://en.wikipedia.org/wiki/Svchost.exe), among others

Environment variables:

```cmd
# In cmd
set
# In addition to the PATH, set can also give up other helpful information such as the HOME DRIVE. In enterprises, this will often be a file share. Navigating to the file share itself may reveal other directories that can be accessed.

# Print path
PATH
```

Installed programs:

```
# With cmd
wmic product get name

# With Powershell
Get-WmiObject -Class Win32_Product |  select Name, Version
```


## Interface(s), IP Address(es), DNS Information

```cmd-session
ipconfig /all


# ARP Table
arp -a

# Routing Table
route print
```

## Users and groups

```
# Logged-In Users
query user

# Current User with cmd
echo %USERNAME%

# Current User with cmd and powershell
whoami

# Current User Privileges with cmd and powershell
whoami /priv

# Current User Group Information in cmd and powershell
whoami /groups

# Get All Users
net user

# Get All Groups
net localgroup

# Details About a Group
net localgroup administrators

# Get Password Policy & Other Account Information
net accounts


```

## Enumerate local shares

```powershell
# Enumerate the local shares:
Get-SmbShare
```

## Enumerating Protections

Many organizations utilize some sort of application whitelisting solution to control what types of applications and files certain users can run. This may be used to attempt to block non-admin users from running `cmd.exe` or `powershell.exe` or other binaries and file types not needed for their day-to-day work. A popular solution offered by Microsoft is [AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview). We can use the [GetAppLockerPolicy](https://docs.microsoft.com/en-us/powershell/module/applocker/get-applockerpolicy?view=windowsserver2019-ps) cmdlet to enumerate the local, effective (enforced), and domain AppLocker policies.

Some EDR tools detect on or even block usage of common binaries such as `net.exe`, `tasklist`, etc.

```powershell-session
Get-MpComputerStatus
```

#### List AppLocker Rules

```powershell-session
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
```

#### Test AppLocker Policy

```powershell-session
Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone
```

#### UAC

[See User Account Control (UAC).](uac-user-account-control.md)

**Confirming UAC is Enabled:**

```cmd-session
REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA
```

Output:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System
EnableLUA    REG_DWORD    0x1
```

REG_DWORD 0x1: The value 1 means UAC is turned ON.

## Processes

Display Running Processes:

```
# With Netstat
netstat -ano
```

The main thing to look for with Active Network Connections are entries listening on loopback addresses (127.0.0.1 and ::1) that are not listening on the IP Address (10.129.43.8) or broadcast (0.0.0.0, ::/0).

## PsService

We can use  [PsService](https://docs.microsoft.com/en-us/sysinternals/downloads/psservice), which is part of the Sysinternals suite, to check permissions on the service.

## Nmap and TTL
Nmap script

```
# To determine the OS
 sudo nmap -v -O $ip

# To see banners of existing open ports
sudo nmap -v $ip --script banner.nse
```

TTL technique
**`Time To Live` (TTL) counter** when utilizing ICMP to determine if the host is up. 

```
ping $ip
```

A typical response from a Windows host will either be 32 or 128. We can utilize this value since most hosts will never be more than 20 hops away from your point of origin, so there is little chance of the TTL counter dropping into the acceptable values of another OS type. More at [https://subinsb.com/default-device-ttl-values/](https://subinsb.com/default-device-ttl-values/).

