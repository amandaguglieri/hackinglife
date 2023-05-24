---
title: Process capabilities - getcap
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
  - linux
---

# Process capabilities: getcap

Linux capabilities **provide a subset of the available root privileges** to a process. For the purpose of performing permission checks, traditional UNIX implementations distinguish two categories of processes: _privileged_ processes (whose effective user ID is 0, referred to as superuser or root), and _unprivileged_ processes (whose effective UID is nonzero). Privileged processes bypass all kernel permission checks, while unprivileged processes are subject to full permission checking based on the process's credentials (usually: effective UID, effective GID, and supplementary group list).

In Linux, files may be given specific capabilities. For example, if an executable needs to access (read) files that are only readable by root, it is possible to give that file this ‘permission’ without having it run with complete root privileges. This allows for a more secure system in general.

getcap and setcap are used to view and set capabilities, respectively. They usually belong to the libcap2-bin package on debian and debian-based distributions.


Scan all files in system and check capabilities:

```shell-session
getcap -r / 2>/dev/null
```

Check what every capability means in [https://linux.die.net/man/7/capabilities](https://linux.die.net/man/7/capabilities)

Knowing what capability is assigned to a proccess, try to make the best of it to escalate privileges. 

Example in [HackTheBox: nunchucks](htb-nunchucks.md) in which perl command has " cap_setuid+ep" capabilities, which means that at some point may run as sudo.


## Labs

[HackTheBox: nunchucks](htb-nunchucks.md)



## Resources

[Hacktricks](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities)

[https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/](https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/)
