---
title: SeImpersonatePrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeImpersonate
---
# SeImpersonatePrivilege 

## 🤷 Abusing SeImpersonate and SeAssignPrimaryToke

In Windows, every process has a token that has information about the account that is running it. These tokens are not considered secure resources, as they are just locations within memory.

 To utilize the token, the `SeImpersonate` privilege is needed.  It is only given to administrative accounts.

We will often run into this privilege after gaining remote code execution via an application that runs in the context of a service account. 
 
**List our privileges**

```
whoami /priv
```

If the command `whoami /priv` confirms that [SeImpersonatePrivilege](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/seimpersonateprivilege-secreateglobalprivilege) is listed, we may  use it to impersonate a privileged account such as `NT AUTHORITY\SYSTEM`.

For that there are several tools such as [JuicyPotato](https://github.com/ohpe/juicy-potato), [PrintSpoofer](https://github.com/itm4n/PrintSpoofer), or [RoguePotato](https://github.com/antonioCoco/RoguePotato) to escalate to `SYSTEM` level privileges, depending on the target host.


### 🥔 JuicyPotato: SeImpersonate or SeAssignPrimaryToken

[RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG) and its [variants](https://github.com/decoder-it/lonelypotato) leverages the privilege escalation chain based on [`BITS`](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968799\(v=vs.85\).aspx) [service](https://github.com/breenmachine/RottenPotatoNG/blob/4eefb0dd89decb9763f2bf52c7a067440a9ec1f0/RottenPotatoEXE/MSFRottenPotato/MSFRottenPotato.cpp#L126) having the MiTM listener on `127.0.0.1:6666` and when you have `SeImpersonate` or `SeAssignPrimaryToken` privileges. During a Windows build review we found a setup where `BITS` was intentionally disabled and port `6666` was taken.

[See more on JuicyPotato](juicypotato.md)


### 🖨️ PrintNightmare

`PrintNightmare` is the nickname given to two vulnerabilities ([CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) and [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675)) found in the [Print Spooler service](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-prsod/7262f540-dd18-46a3-b645-8ea9b59753dc) that runs on all Windows operating systems.

[See more on PrintNightmare](printnightmare.md)


###  🏊 Print Spooler / PrintSpoofer: SeImpersonatePrivilege + Windows Print Spooler service
The Print Spooler exploitation leverages the Windows Print Spooler service in conjunction with the SeImpersonatePrivilege privilege. The goal is to impersonate a SYSTEM token to escalate privileges. Tools like PrintSpoofer automate this process effectively. Below are detailed steps for exploiting this vulnerability:

[See more on PrintSpoofer](printspoofer.md)

### 🥔 GodPotato: SeImpersonate 

Repo: https://github.com/BeichenDream/GodPotato


[See more on godpotato](godpotato.md)