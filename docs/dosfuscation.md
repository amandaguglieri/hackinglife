---
title: DOSfuscation - Evasion tool for code obfuscating in Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - evasion
  - obfuscation
---

# DOSfuscation - Evasion tool for code obfuscating in Windows

Github repo: [https://github.com/danielbohannon/Invoke-DOSfuscation](https://github.com/danielbohannon/Invoke-DOSfuscation.md)

Invoke-DOSfuscation is a PowerShell v2.0+ compatible cmd.exe command obfuscation framework. (White paper: [https://www.fireeye.com/blog/threat-research/2018/03/dosfuscation-exploring-obfuscation-and-detection-techniques.html](https://www.fireeye.com/blog/threat-research/2018/03/dosfuscation-exploring-obfuscation-and-detection-techniques.html))

## Installation

```powershell-session
git clone https://github.com/danielbohannon/Invoke-DOSfuscation.git

cd Invoke-DOSfuscation
```


## Basic commands

```powershell-session
Import-Module .\Invoke-DOSfuscation.psd1

# Enter in the Dosfuscation terminal line
Invoke-DOSfuscation

#####
# Once in the specific terminal line
# 1. Get help
help
# 2. See tutorial
tutorial
# An example:
SET COMMAND type C:\Users\htb-student\Desktop\flag.txt
encoding
1
```

```
# Output:
typ%TEMP:~-3,-2% %CommonProgramFiles:~17,-11%:\Users\h%TMP:~-13,-12%b-stu%SystemRoot:~-4,-3%ent%TMP:~-19,-18%%ALLUSERSPROFILE:~-4,-3%esktop\flag.%TMP:~-13,-12%xt
```


```cmd-session
#  Running the obfuscated command on CMD, and we see that it indeed works as expected:
typ%TEMP:~-3,-2% %CommonProgramFiles:~17,-11%:\Users\h%TMP:~-13,-12%b-stu%SystemRoot:~-4,-3%ent%TMP:~-19,-18%%ALLUSERSPROFILE:~-4,-3%esktop\flag.%TMP:~-13,-12%xt
```


