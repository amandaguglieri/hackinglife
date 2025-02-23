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


## Interface(s), IP Address(es), DNS Information

```cmd-session
ipconfig /all
```


#### ARP Table

```cmd-session
arp -a
```

#### Routing Table

```cmd-session
route print
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

