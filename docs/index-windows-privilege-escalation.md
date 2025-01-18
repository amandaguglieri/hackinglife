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
	    - Creating a service with PsExec.
	- Kernel.
	- Password Mining:
		- [Cached SAM](active-directory-from-windows-privilege-escalation.md#attacking-sam).
		- [Cached LSASS](active-directory-from-windows-privilege-escalation.md#attacking-lsass).
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

- [CrackMapexec](crackmapexec.md).
- [mimikatz](mimikatz.md).


## Prominent Windows Exploits

| **Vulnerability** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MS08-067`        | MS08-067 was a critical patch pushed out to many different Windows revisions due to an SMB flaw. This flaw made it extremely easy to infiltrate a Windows host. It was so efficient that the Conficker worm was using it to infect every vulnerable host it came across. Even Stuxnet took advantage of this vulnerability.                                                                                                                                                                                      |
| `Eternal Blue`    | MS17-010 is an exploit leaked in the Shadow Brokers dump from the NSA. This exploit was most notably used in the WannaCry ransomware and NotPetya cyber attacks. This attack took advantage of a flaw in the SMB v1 protocol allowing for code execution. EternalBlue is believed to have infected upwards of 200,000 hosts just in 2017 and is still a common way to find access into a vulnerable Windows host.                                                                                                |
| `PrintNightmare`  | A remote code execution vulnerability in the Windows Print Spooler. With valid credentials for that host or a low privilege shell, you can install a printer, add a driver that runs for you, and grants you system-level access to the host. This vulnerability has been ravaging companies through 2021. 0xdf wrote an awesome post on it [here](https://0xdf.gitlab.io/2021/07/08/playing-with-printnightmare.html).                                                                                          |
| `BlueKeep`        | CVE 2019-0708 is a vulnerability in Microsoft's RDP protocol that allows for Remote Code Execution. This vulnerability took advantage of a miss-called channel to gain code execution, affecting every Windows revision from Windows 2000 to Server 2008 R2.                                                                                                                                                                                                                                                     |
| `Sigred`          | CVE 2020-1350 utilized a flaw in how DNS reads SIG resource records. It is a bit more complicated than the other exploits on this list, but if done correctly, it will give the attacker Domain Admin privileges since it will affect the domain's DNS server which is commonly the primary Domain Controller.                                                                                                                                                                                                   |
| `SeriousSam`      | CVE 2021-36924 exploits an issue with the way Windows handles permission on the `C:\Windows\system32\config` folder. Before fixing the issue, non-elevated users have access to the SAM database, among other files. This is not a huge issue since the files can't be accessed while in use by the pc, but this gets dangerous when looking at volume shadow copy backups. These same privilege mistakes exist on the backup files as well, allowing an attacker to read the SAM database, dumping credentials. |
| `Zerologon`       | CVE 2020-1472 is a critical vulnerability that exploits a cryptographic flaw in Microsoft’s Active Directory Netlogon Remote Protocol (MS-NRPC). It allows users to log on to servers using NT LAN Manager (NTLM) and even send account changes via the protocol. The attack can be a bit complex, but it is trivial to execute since an attacker would have to make around 256 guesses at a computer account password before finding what they need. This can happen in a matter of a few seconds.              |
