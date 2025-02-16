---
title: Index for Linux Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
---
# Index for Linux Privilege Escalation

??? note "Guides to have at hand"
    - [HackTricks](https://book.hacktricks.xyz/).  Written by the creator of WinPEAS and LinPEAS.
    - [Vulnhub PrivEsc Cheatsheet](https://github.com/Ignitetechnologies/Privilege-Escalation).
    - [s0cm0nkey's Security Reference Guide](https://s0cm0nkey.gitbook.io/s0cm0nkeys-security-reference-guide/).


This is a nice summary related to Local Privilege Escalation by [@s4gi_](https://twitter.com/s4gi_/status/866501430374301696/photo/1):

![local-privilege-escalation.jpg](img/local-privilege-escalation.jpg)

## Basic enumeration

See [Linux Enumeration Cheat sheet](linux-enumeration.md)

## Enumeration scripts

!!! abstract "Enumeration scripts"
    
    - [Scan the Linux system with "linEnum"](linenum.md).
    - [Search for possible paths to escalate privileges with "linPEAS"](linpeas.md).
    - [Enumerate privileges with "Linux Privilege Checker" tool](linux-privilege-checker.md).
    - [Enumerate possible exploits with "Linux Exploit Suggester" tool](linux-exploit-suggester.md).
        

## Privilege escalation techniques  

!!! abstract "Techniques"
	
    - [Cron jobs: path, wildcards, file overwrite](cron-jobs.md).
    - Daemons. 
	- [Dirty cow](dirty-cow.md).
	- File Permissions: 
		- [Configuration files](linux-enumeration.md).
		- Startup scripts.
		- [Process capabilities: getcap](process-capabilities-getcap.md)
		- [Suid binaries](suid-binaries.md): shared object injection, symlink, environmental variables.
		- [Lxd privileges escalation](lxd.md).
		- [Pentesting docker](cloud/containers/pentesting-docker.md)
		- [Pentesting kubernetes](pentesting-kubernetes.md)
	- [Hijacking Tmux Sessions](hijacking-tmux-sessions.md)
	- [Kernel vulnerability exploitation](kernel-vulnerability-exploitation.md).
	- [Logrotate](logrotate.md)
	- [NFS](2049-nfs-network-file-system.md).
	- Password Mining: logs, memory, history, configuration files.
	- [Path Abuse](linux-path-abuse.md)
	- [Shared libraries: LD_PRELOAD / LD_LIBRARY_PATH.](shared-libraries-ldpreload-ldlibrarypath.md)
	- Sudo: 
		- [Escaping restricted shells](linux-escaping-restricted-shells.md).
		- [Sudo Rights Abuse](sudo-rights-abuse.md)
		- Others.
	- [ssh keys](ssh-keys.md).
	- Vulnerable services:
		- [Screen 4.5.0](screen-4.5.0.md)
	- [Wildcard Abuse](linux-wildcard-abuse.md)


