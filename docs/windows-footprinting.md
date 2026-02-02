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

```
# List network interfaces
ipconfig /all

# ARP Table
arp -a

# Print Routing Table
route print

# Active TCP connections with TCP/UDP ports, no name resolution, return process ID
netstat -ano
```

Scanning ports in Powershell:

```powershell
foreach ($ports in 1..1024) {If (($a=Test-NetConnection 10.10.12.123 -Port $port -WarningAction SilentlyContinue).tcpTestSucceeded -eq $true){ "TCP port $port is open}}
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


###### Username and hostname
# Whoami and my privs
whoami
whoami /priv
# Which computer
hostname
# Group memberships of the current user
whoami /groups

###### Existing users and groups
# Users in the Computer
net user
# Users in the Computer (tells you if enabled or not)
Get-LocalUser
# Get specific Local user
Get-LocalUser SAMnameOfUser
# Localgroups in the Computer
Get-LocalGroup 
# Get specific Localgroup
Get-LocalGroupMember localgroupname
net localgroup "Remote Management Users"
```

## Enumerate Interesting Files

```powershell
###### File enumeration
# Retrieve files with certain extensions, like keepas
Get-ChildItem -Path C:\users -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue
Get-ChildItem -Path C:\users -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue

# Retrieve files containing certain string, like "password"
Get-ChildItem -Recurse -Path C:\ | Select-String "password" -List
```

## Enumerate History Files

```powershell
###### History files
# Retrieve history:
Get-History


# To retrieve the history from PSReadline. Long history short: Most Administrators use the Clear-History command to clear the PowerShell history. But this Cmdlet is only clearing PowerShell's own history, which can be retrieved with Get-History. Starting with PowerShell v5, v5.1, and v7, a module named PSReadline is included, which is used for line-editing and command history functionality.
(Get-PSReadlineOption).HistorySavePath


### Mitigations: Administrators can prevent PSReadline from recording commands by setting the -HistorySaveStyle option to SaveNothing with the [_Set-PSReadlineOption_](https://learn.microsoft.com/en-us/powershell/module/psreadline/set-psreadlineoption?view=powershell-7.2) Cmdlet. Alternatively, they can clear the history file manually.
```

## Enumerate local shares

```powershell
# Enumerate the local shares:
Get-SmbShare

# Then you can do a tree for further enumeration
tree "C:\Department Shares" /F /A

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

###### Running processes
# List running processes:
Get-Process


###### Installed services
# Several method for retrieving services:
# 1. GUI snap-in services.msc
# 2. Get-Service cmd-let
# 3. Get-Ciminstance cmd-let (super seeding Get-WmiObject)
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

```

The main thing to look for with Active Network Connections are entries listening on loopback addresses (127.0.0.1 and ::1) that are not listening on the IP Address (10.129.43.8) or broadcast (0.0.0.0, ::/0).


## Installed applications

```powershell
# Important: Review C:\ for applications not completely installed


# 32-bit applications 
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname

# 64-bit applications
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname

# Important: Review C:\ for applications not completely installed

```


## Enumerating LOGS: Event Viewer +  Script Block loggings

```
###### LOGS
# Retrieve Powershell (or any other applicaiton) Logs
# Open Event Viewer: Press `WIN + R`, type event.msc and press Enter 
# Navigate to the Powershell logs: In the event viewer go to Application and Services Logs > Microsoft > Windows > Powershell > Operational.
# Search relevant Script Blog Logging Events: You can fileter for relevant events by right clicking on Operaitonal and selecting `Filter Current Log`. In the filter window, set the EVENT ID to `4104` which is the id related to Script Block Loggins. Click ok. 
```
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

