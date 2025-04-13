---
title: Archetype - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Archetype - A Hack the Box machine


```bash
nmap  -sC -sV $ip -Pn
```

Open ports: 135, 139, 445, 1433.

First, exploit 445. With smbclient, you will download the fileprod.dtsConfig with credentials for mssql database.

With those credentials you can follow instructions from this [impacket module](1433-mssql.md) and next instructions to exploit it and get a reverse shell with nc64.exe.

With that, you will get user.txt in Desktop.

For escalation of privileges, see technique [Recently accessed files and executed commands](windows-credentials.md). 

```ps
type C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

With admin credentials, you can use impacket's psexec.py module to get an interactive shell on the Windows host with admin rights.

```bash
python3 /usr/share/doc/python3-impacket/examples/psexec.py administrator:MEGACORP_4dm1n\!\!@10.129.95.187
```
 


