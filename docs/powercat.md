---
title: Powercat - An alternative to netcat coded in PowerShell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanning
  - active recon
  - passiverecon
---

# Powercat - An alternative to netcat coded in PowerShell

Netcat comes pre-installed in most Linux distributions. There is also a version for windows:  download from [https://nmap.org/download.html](https://nmap.org/download.html). 

As for  Windows machines,  there's an alternative to netcat coded in PowerShell called [PowerCat](https://github.com/besimorhino/powercat). 


powercat is a powershell function. First you need to load the function before you can execute it. You can put one of the below commands into your powershell profile so powercat is automatically loaded when powershell starts.

```powershell
# Load The Function From Downloaded .ps1 File:
    . .\powercat.ps1
    
# Load The Function From URL:
    IEX (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')
```

But it's also installed in Kali at:

```bash
/usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 
```


Meaning that we can serve it from our kali:

```bash
cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 .

python3 -m http.server 80
```
