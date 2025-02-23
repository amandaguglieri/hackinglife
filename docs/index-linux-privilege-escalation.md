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

	
	- [Configuration files](linux-enumeration.md)
	- [Crack sensitive files](crack-sensitive-files.md)
    - [Cron jobs: path, wildcards, file overwrite](cron-jobs.md)
	- [Dirty cow](dirty-cow.md)
	- [Dirty Pipe](dirty-pipe.md)
	- [Escaping restricted shells](linux-escaping-restricted-shells.md)
	- [Escaping docker: Pentesting docker](cloud/containers/pentesting-docker.md)
	- [Escaping kubernetes](pentesting-kubernetes.md)
	- [Hijacking Tmux Sessions](hijacking-tmux-sessions.md)
	- [Kernel vulnerability exploitation](kernel-vulnerability-exploitation.md)
	- [Lxd privileges escalation](lxd.md)
	- [Logrotate](logrotate.md)
	- [Netfilter](netfilter.md)
	- [NFS](2049-nfs-network-file-system.md)
	- Password Mining: logs, memory, history, configuration files
	- [Path Abuse](linux-path-abuse.md)
	- [Polkit](polkit.md)
	- [Process capabilities: getcap](process-capabilities-getcap.md)
	- [Python Library Hickjacking](python-library-hijacking.md)
	- [Shared libraries: LD_PRELOAD / LD_LIBRARY_PATH.](shared-libraries-ldpreload-ldlibrarypath.md)
	- [Shared object hijacking](shared-object-hijacking.md)
	- [ssh keys](ssh-keys.md)
	- [Sudo Rights Abuse](sudo-rights-abuse.md)
	- [Suid binaries](suid-binaries.md): shared object injection, symlink, environmental variables
	- Vulnerable services:
		- [Screen 4.5.0](screen-4.5.0.md)
	- [Wildcard Abuse](linux-wildcard-abuse.md)



## Linux hardening


### **1. Updates and Patching**


- Keep your system up to date to mitigate known privilege escalation vulnerabilities.
- **Ubuntu/Debian**: Use `unattended-upgrades` for automated updates.

  ```sh
  sudo apt install unattended-upgrades
  sudo dpkg-reconfigure unattended-upgrades
  ```

- **Red Hat-based systems**: Use `yum-cron` for automatic updates.

  ```sh
  sudo yum install yum-cron
  sudo systemctl enable --now yum-cron
  ```


### **2. Configuration Management**


#### **File and Directory Security**

- Audit writable files and SUID binaries:

  ```sh
  find / -perm -4000 2>/dev/null
  find / -writable -type f 2>/dev/null
  ```

- Remove unnecessary SUID binaries:

  ```sh
  chmod u-s /path/to/binary
  ```


#### **Cron Jobs and Sudo Security**

- Ensure absolute paths are used in cron jobs and sudo commands.
- Review cron job permissions:

  ```sh
  ls -l /etc/cron* /var/spool/cron/
  ```


#### **Credential Management**

- Do not store plaintext passwords in world-readable files.
- Clean up home directories and bash history:

  ```sh
  cat /dev/null > ~/.bash_history && history -c
  ```


#### **Library Security**

- Prevent low-privileged users from modifying custom libraries.
- Audit shared library usage:

  ```sh
  ldd /path/to/binary
  ```


#### **Remove Unnecessary Packages and Services**

- Disable unused services:

  ```sh
  systemctl disable --now <service>
  ```

- Remove unnecessary packages:

  ```sh
  sudo apt purge <package>
  sudo yum remove <package>
  ```


#### **SELinux/AppArmor**

- Enable SELinux for additional security:

  ```sh
  setenforce 1
  ```

- Check AppArmor status:

  ```sh
  aa-status
  ```


### **3. User Management**


#### **Limit User Accounts and Privileges**


- Check active users:

  ```sh
  cat /etc/passwd
  ```

- Check sudo privileges:

  ```sh
  sudo -l
  ```

- Restrict sudo access based on least privilege:

  ```sh
  visudo
  ```


#### **Password Policies**

- Enforce password history using `/etc/security/opasswd`:

  ```sh
  sudo vi /etc/pam.d/common-password
  password required pam_unix.so remember=5 sha512
  ```

- Enforce password expiration:

  ```sh
  chage -M 90 -W 7 username
  ```


#### **Monitoring and Automation**

- Use tools like **Puppet**, **SaltStack**, **Zabbix**, and **Nagios** for automation.
- Enable remote alerts for security events.


### **4. Audit and Security Baselines**

- Perform regular security audits using industry standards like **DISA STIGs**, **ISO27001**, **PCI-DSS**, and **HIPAA**.
- Supplement with penetration testing and vulnerability scans.


#### **Lynis Security Auditing Tool**

- Install and run **Lynis**:

  ```sh
  git clone https://github.com/CISOfy/lynis
  cd lynis
  ./lynis audit system
  ```


#### **Example Output Warnings**

```sh
! Found one or more cronjob files with incorrect file permissions (SCHD-7704)
! systemd-timesyncd never successfully synchronized time (TIME-3185)
```


### **Lynis Hardening Suggestions**

- Set a **GRUB boot loader password**:

  ```sh
  grub-mkpasswd-pbkdf2
  ```

- Disable core dumps:

  ```sh
  echo '* hard core 0' >> /etc/security/limits.conf
  ```

- Run `pwck` to check password file integrity:

  ```sh
  pwck
  ```
