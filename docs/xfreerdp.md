---
title: xfreerdp 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - windows
  - rdp
---

# xfreerdp

[xfreerdp](https://linux.die.net/man/1/xfreerdp) is an X11 [Remote Desktop Protocol (RDP)](3389-rdp.md) client which is part of the FreeRDP project. An RDP server is built-in to many editions of Windows. 

## Installation

To install xfreerdp, proceed with the following command:

```bash
sudo apt-get install freerdp2-x11
```


## Basic commands

```bash
# No password indicated. When prompted for one, click Enter and see if it allows us to login
xfreerdp [/d:domain] /u:<username> /v:$ip 

xfreerdp [/d:domain] /u:<username> /p:<password> /v:$ip
# /v:{target_IP} : Specifies  the target IP of the host we would like to connect to.

xfreerdp [/d:domain] /u:<username> /pth:<hash> /v:$ip /cert:ignore 
# /pth:<hash>   Pass the hash


```

### Troubleshoot in PtH attack

**Restricted Admin Mode**, which is disabled by default, should be enabled on the target host; otherwise, you will be presented with an error. This can be enabled by adding a new registry key `DisableRestrictedAdmin` (REG_DWORD) under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` with the value of 0. It can be done using the following command:

```powershell
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

Once the registry key is added, we can use xfreerdp with the option /pth to gain RDP access.


### Troubleshooting loging

If we obtain:

```
[ERROR][com.freerdp.core] - transport_connect_tls:freerdp_set_last_error_ex ERRCONNECT_TLS_CONNECT_FAILED [0x00020008]
```

if the server requires old-style login), we can try:

```bash
xfreerdp /v:10.129.37.186 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore /sec:rdp
```


We can also force older security:

```bash
xfreerdp /v:10.129.37.186 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore /sec:rdp /tls-seclevel:0
```

Other suggestions:

```
rdesktop -u htb-student -p HTB_@cademy_stdnt! [IP Address]
```