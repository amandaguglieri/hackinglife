---
title: winPEAS - Windows Privilege Escalation Awesome Scripts
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows 
  - privilege escalation
---

# Windows Privilege Escalation Awesome Scripts: winPEAS

And that is exactly what winPEAS stands for: windows Privilege Escalation Awesome Scripts. 

Download it from [https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS).

Releases: 
- [linpeas.sh](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas.sh)
- [linpeas_darwin_amd64](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_darwin_amd64)
- [linpeas_darwin_arm64](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_darwin_arm64)
- [linpeas_fat.sh](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_fat.sh)
- [linpeas_linux_386](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_linux_386)
- [linpeas_linux_amd64](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_linux_amd64)
- [linpeas_linux_arm](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_linux_arm)
- [linpeas_linux_arm64](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_linux_arm64)
- [linpeas_small.sh](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/linpeas_small.sh)
- [winPEAS.bat](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/winPEAS.bat)
- [winPEASx64.exe](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/winPEASx64.exe)
- [winPEASx86.exe](https://github.com/peass-ng/PEASS-ng/releases/download/20250110-31084f44/winPEASx86.exe)





## What it does

+ Check the Local Windows Privilege Escalation checklist from book.hacktricks.xyz that I'm copypasting below.
+ Provide information about how to exploit misconfigurations.

In the github repo, you will see two files: a .bat and an .exe version.


## Checklist for Local windows Privilege Escalation

Source: [winPEAS README.md file](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS).

### System Info 

* [ ] Obtain System information
* [ ] Search for kernel exploits using scripts.
* [ ] Use Google to search for kernel exploits
* [ ] Use searchsploit to search for kernel exploits
* [ ] Interesting info in env vars?
* [ ] Passwords in PowerShell history?
* [ ] Interesting info in Internet settings?
* [ ] Drives
* [ ] WSUS exploit?
* [ ] AlwaysInstallElevated?

### Logging/AV enumeration

* [ ] Check Audit and WEF
* [ ] Check LAPS
* [ ] Check if WDigest is active
* [ ] LSA Protection?
* [ ] Credentials Guard
* [ ] Cached Credentials?
* [ ] Check if any AV
* [ ] AppLocker Policy?
* [ ] UAC
* [ ] User Privileges
* [ ] Check current user privilege
* [ ] Are you member of any privileged group
* [ ] Check if you have any of these tokens enabled: SeImpersonatePrivilege, SeAssignPrimaryPrivilege, SeTcbPrivilege, SeBackupPrivilege, SeRestorePrivilege, SeCreateTokenPrivilege, SeLoadDriverPrivilege, SeTakeOwnershipPrivilege, SeDebugPrivilege?
* [ ] Users Sessions?
* [ ] Check users homes (access?)
* [ ] Check Password Policy
* [ ] What is inside the Clipboard?

### Network

* [ ] Check current network informatio
* [ ] Check hidden local services restricted to the outside

### Running Processes

* [ ] Processes binaries file and folders permission
* [ ] Memory Password mining
* [ ] Insecure GUI apps

### Services

* [ ] Can you modify any service
* [ ] Can you modify the binary that is executed by any service
* [ ] Can you modify the registry of any service
* [ ] Can you take advantage of any unquoted service binary path

### Applications

* [ ] Write permissions on installed applications
* [ ] Startup Applications
* [ ] Vulnerable Drivers

### DLL Hijacking

* [ ] Can you write in any folder inside PATH?
* [ ] Is there any known service binary that tries to load any non-existant DLL?
* [ ] Can you write in any binaries folder?

### Network

* [ ] Enumerate the network (shares, interfaces, routes, neighbours, ...)
* [ ] Take a special look at network services listening on localhost (127.0.0.1)

### Windows Credentials

* [ ] Winlogon.
* [ ] Windows Vault.
* [ ] Interesting DPAPI credentials.
* [ ] Passwords of saved Wifi networks.
* [ ] Interesting info in saved RDP Connections.
* [ ] Passwords in recently run commands.
* [ ] Remote Desktop Credentials Manager.
* [ ] AppCmd.exe exists.
* [ ] SCClient.exe.

### Files and Registry (Credentials)

* [ ] Putty: Creds.
* [ ] SSH keys in registry.
* [ ] Passwords in unattended files.
* [ ] Any SAM & SYSTEM.
* [ ] Cloud credentials.
* [ ] McAfee SiteList.xml.
* [ ] Cached GPP Password?
* [ ] Password in IIS Web config file.
* [ ] Interesting info in web logs.
* [ ] Do you want to ask for credentials
* [ ] Interesting files inside the Recycle Bin.
* [ ] Other registry containing credentials.
* [ ] Inside Browser data.
* [ ] Generic password search.
* [ ] Tools.

### Leaked Handlers

* [ ] Have you access to any handler of a process run by administrator?

### Pipe Client Impersonation

