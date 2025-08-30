---
title: Cascade - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - active
  - directory
  - windows
  - medium
---
# HTB Cascade

## Description

![](img/Cascade.png)

Cascade is a medium difficulty Windows machine configured as a Domain Controller. LDAP anonymous binds are enabled, and enumeration yields the password for user `r.thompson`, which gives access to a `TightVNC` registry backup. The backup is decrypted to gain the password for `s.smith`. This user has access to a .NET executable, which after decompilation and source code analysis reveals the password for the `ArkSvc` account. This account belongs to the `AD Recycle Bin` group, and is able to view deleted Active Directory objects. One of the deleted user accounts is found to contain a hardcoded password, which can be reused to login as the primary domain administrator.

## user.txt

Enumerate:

```bash
 sudo nmap -sC -sV $ip -Pn --top-ports 10000
```

Results: 

```
Host is up (0.037s latency).
Not shown: 8353 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-13 19:01:30Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: CASC-DC1; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
|_clock-skew: -7m01s
| smb2-time: 
|   date: 2025-01-13T19:02:22
|_  start_date: 2025-01-13T18:56:18

```

We enumerate users:

```bash
crackmapexec smb $ip --users
```

Results:

```
SMB         10.129.67.96    445    CASC-DC1         [+] Enumerated domain user(s)
SMB         10.129.67.96    445    CASC-DC1         cascade.local\CascGuest                      Built-in account for guest access to the computer/domain
SMB         10.129.67.96    445    CASC-DC1         cascade.local\arksvc                         
SMB         10.129.67.96    445    CASC-DC1         cascade.local\s.smith                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\r.thompson                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\util                           
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.wakefield                    
SMB         10.129.67.96    445    CASC-DC1         cascade.local\s.hickson                      
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.goodhand                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\a.turnbull                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\e.crowe                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\b.hanson                       
SMB         10.129.67.96    445    CASC-DC1         cascade.local\d.burman                       
SMB         10.129.67.96    445    CASC-DC1         cascade.local\BackupSvc                      
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.allen                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\i.croft  
```




```
~/tools/kerbrute/dist/kerbrute_linux_amd64 userenum -d cascade.local --dc $ip ~/borrar/users.txt 

```




```
python3 ~/tools/impacket/examples/GetNPUsers.py CASCADE.LOCAL/ -dc-ip $ip -no-pass -usersfile ~/borrar/users.txt | grep -v SessionError


python3 ~/tools/impacket/examples/GetNPUsers.py --dc-ip $ip CASCADE.LOCAL/Backupsvc -request 
```




```
ldapsearch -x -H ldaps://$ip -b "DC=CASCADE,DC=LOCAL" "(objectClass=user)"

ldapsearch -x -H ldap://$ip -b "DC=CASCADE,DC=LOCAL" "(objectClass=user)" cn mail sAMAccountName

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```




```

```

