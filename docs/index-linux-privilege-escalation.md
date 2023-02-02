---
title: Index for Linux Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
---

# Index for Linux Privilege Escalation

??? note "Guides to have at hand"
    - [HackTricks](https://book.hacktricks.xyz/).  Written by the creator of WinPEAS and LinPEAS.
    - [Vulnhub PrivEsc Cheatsheet](https://github.com/Ignitetechnologies/Privilege-Escalation).
    - [s0cm0nkey's Security Reference Guide](https://s0cm0nkey.gitbook.io/s0cm0nkeys-security-reference-guide/).


This is a nice summary related to Local Privilege Escalation by [@s4gi_](https://twitter.com/s4gi_/status/866501430374301696/photo/1):

![local-privilege-escalation.jpg](img/local-privilege-escalation.jpg)


!!! abstract "Techniques"

    - Cron: path, wildcards, file overwrite.
    - Daemons. 
	- [Dirty cow](dirty-cow.md).
	- File Permissions: 
		- Configuration files.
		- Startup scripts.
		- [Suid binaries](suid-binaries.md): shared object injection, symlink, environmental variables.
	- Kernel.
	- LD_PRELOAD / LD_LIBRARY_PATH.
	- NFS.
	- Password Mining: logs, memory, history, configuration files.
	- Sudo: shell escape sequences, abuse intended functionality.


!!! abstract "Resources and tools"

    - [Enumerate privileges with "Linux Privilege Checker" tool](linux-privilege-checker.md).
    - [Enumerate possible exploits with "Linux Exploit Suggester" tool](linux-exploit-suggester.md).
        

