---
title: Port 22 - Secure Shell (SSH)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web
  - pentesting
  - port
  - "22"
---
# Port 22 - Secure Shell (SSH)

Secure Shell (SSH) enables two computers to establish an encrypted and direct connection within a possibly insecure network on the standard port TCP 22. 

Implemented natively on all Linux distributions and MacOS, SSH can also be used on Windows, with an appropriate program. The well-known [OpenBSD SSH](https://www.openssh.com/) (`OpenSSH`) server on Linux distributions is an open-source fork of the original and commercial `SSH` server from SSH Communication Security.

There are two competing protocols: SSH-1 and SSH-2. SSH-2, also known as SSH version 2, is a more advanced protocol than SSH version 1 in encryption, speed, stability, and security. For example, SSH-1 is vulnerable to MITM attacks, whereas SSH-2 is not.

The SSH server runs on TCP port 22 by default, to which we can connect using an SSH client. This service uses three different cryptography operations/methods: symmetric encryption, asymmetric encryption, and hashing.

## Footprinting ssh

### ssh-audit

```bash
# Installation and execution
git clone https://github.com/jtesta/ssh-audit.git 

# Execute
cd ssh-audit
./ssh-audit.py $ip
```


### nmap

Brute force script: 

```bash
nmap $ip -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=/usr/share/nmap/nselib/data/passwords.lst
```

OpenSSH 7.6p1 Ubuntu ubuntu0.3 is well known for some vulnerabilities.

## Connect with ssh

```bash
ssh <user>@$ip

# connect with a ssh key
ssh -i id_rsa <user>@$ip
```



## Installing a ssh service

The sshd_config file, responsible for the OpenSSH server, has only a few of the settings configured by default. However, the default configuration includes X11 forwarding, which contained a command injection vulnerability in version 7.2p1 of OpenSSH in 2016. 

**Configuration file**: `/etc/ssh/sshd_config`.

Common misconfigurations:

|**Setting**|**Description**|
|---|---|
|`PasswordAuthentication yes`|Allows password-based authentication.|
|`PermitEmptyPasswords yes`|Allows the use of empty passwords.|
|`PermitRootLogin yes`|Allows to log in as the root user.|
|`Protocol 1`|Uses an outdated version of encryption.|
|`X11Forwarding yes`|Allows X11 forwarding for GUI applications.|
|`AllowTcpForwarding yes`|Allows forwarding of TCP ports.|
|`PermitTunnel`|Allows tunneling.|
|`DebianBanner yes`|Displays a specific banner when logging in.|

Some instructions and [hardening guides](https://www.ssh-audit.com/hardening_guides.html) can be used to harden our SSH servers.
