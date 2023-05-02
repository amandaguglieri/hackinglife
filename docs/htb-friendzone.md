---
title: Walkthrough - Friendzone - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Walkthrough - Friendzone, a Hack The Box machine


```bash
nmap -sC -sV $IP -Pn
```

```
└─$ nmap -sC -sV $IP -Pn          
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-18 18:23 EDT
Stats: 0:00:14 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 14.29% done; ETC: 18:23 (0:00:00 remaining)
Stats: 0:00:14 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 28.57% done; ETC: 18:23 (0:00:00 remaining)
Stats: 0:00:20 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 28.57% done; ETC: 18:23 (0:00:15 remaining)
Nmap scan report for 10.129.228.87
Host is up (0.045s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a96824bc971f1e54a58045e74cd9aaa0 (RSA)
|   256 e5440146ee7abb7ce91acb14999e2b8e (ECDSA)
|_  256 004e1a4f33e8a0de86a6e42a5f84612b (ED25519)
53/tcp  open  domain      ISC BIND 9.11.3-1ubuntu1.2 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.11.3-1ubuntu1.2-Ubuntu
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Friend Zone Escape software
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.29
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO
| Not valid before: 2018-10-05T21:02:30
|_Not valid after:  2018-11-04T21:02:30
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.29 (Ubuntu)
| tls-alpn: 
|_  http/1.1
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Hosts: FRIENDZONE, 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2023-04-18T22:23:28
|_  start_date: N/A
|_clock-skew: mean: -59m59s, deviation: 1h43m54s, median: 0s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: friendzone
|   NetBIOS computer name: FRIENDZONE\x00
|   Domain name: \x00
|   FQDN: friendzone
|_  System time: 2023-04-19T01:23:29+03:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: FRIENDZONE, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.34 seconds
```

**Interesting here**: port 53 open. On port 443 you can read:

| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO

We have here domain name friendzone.red. Also visiting the ip in the browser there is an info email with domain friendzoneportal.red.

Enumerating shares in samba:

```bash
smbclient -L 10.129.228.87
smbmap -H 10.129.228.87
```
An alternative is using [enum4linux.md](enum4linux.md).

Checking out each shared folder:

```bash
smbclient \\\\10.129.228.87\\Files
smbclient \\\\10.129.228.87\\print$
smbclient \\\\10.129.228.87\\general
smbclient \\\\10.129.228.87\\Developement
smbclient \\\\10.129.228.87\\IPC$
```

From shared folder general and samba terminal we can download the file creds.txt

```smb
dir
mget *
```




## Transferring DNS zone


Some HackTheBox machines exploits [DNS zone transfer](dig.md):

In the example of Friendzone machine, accessible web page on port 80 provides an email in which a different domain is appreciated. Also port 53 is open, which is an indicator of some possible DNS zone transfer.

In friendzone, we will transfer our zone to all zones spotted in different scanners:

```bash
# friendzone.red was spotted in the nmap scan. Transferring 10.129.228.87 zone to friendzone.red
dig axfr friendzone.red @10.129.228.87

# Also friendzoneportal.red was spotted in the email that appeared on http://10.129.228.87. Transferring 10.129.228.87 zone to friendzoneportal.red:
dig axfr friendzoneportal.red @10.129.228.87
```

Add those subdomains to your /etc/hosts

Visit https://administrator1.friendzone.red and a login panel is displayed. Use credentials found in samba shared folder. After login into the application a message is displayed: "Login Done ! visit /dashboard.php".


![Friendzone dashboard](img/htb-friendzone1.png)

