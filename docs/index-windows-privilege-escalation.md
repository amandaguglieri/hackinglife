---
title: Index for Windows Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
  - windows
---

# Index for Windows Privilege Escalation

??? note "Guides to have at hand"
    - [HackTricks](https://book.hacktricks.xyz/).  Written by the creator of WinPEAS and LinPEAS.
    - [Vulnhub PrivEsc Cheatsheet](https://github.com/Ignitetechnologies/Privilege-Escalation).
    - [s0cm0nkey's Security Reference Guide](https://s0cm0nkey.gitbook.io/s0cm0nkeys-security-reference-guide/).


This is a nice summary related to Local Privilege Escalation by [@s4gi_](https://twitter.com/s4gi_/status/866501430374301696/photo/1):

![local-privilege-escalation.jpg](img/local-privilege-escalation.jpg)


## Enumeration scripts

!!! abstract "Enumeration scripts"
	
    - [Windows Privilege Escalation Awesome Scripts: winPEAS tool](winpeas.md).
    - [Seatbelt](seatbelt.md).
    - [JAWS](jaws.md).


## Privilege escalation techniques  

!!! abstract "Techniques"

    - Services:
	    - DLL Hacking.
	    - Uniqued Path.
	    - Named Pipes.
	    - Registry.
	    - [Windows binaries: LOLBAS](windows-binaries.md).
	    - bin Path.
	    - [Abusing a service with PowerUp.ps1](powerup.md)
	- Kernel.
	- Password Mining:
		- [Cached SAM](attacking-sam.md).
		- [Cached LSASS](attacking-lsass.md).
		- [Pass The Hash](pass-the-hash.md).
		- Configuration files: unattend.xml, SiteList.xml, web.config, vnc.ini.
		- Logs.
		- [Credentials in recently accessed files/executed commands](windows-privilege-escalation-history.md)
		- Memory: mimiktenz, Process Dump (minidump).
		- .rdp Files.
		- Registry: HKCU\Software\USERNAME\PuTTY\Sessions, AutoLogon, VNC.
	- Registry: 
		- Autorun.
		- AlwaysInstallElevated
	- Scheduled Tasks: 
		- Binary Overwrite.
		- Missing binary.
	- Hot Potato.
	- Startup Applications

## Privilege escalation tools

- [CrackMapexex](crackmapexec.md).
- [mimikatz](mimikatz.md).
- 