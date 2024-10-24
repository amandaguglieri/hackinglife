---
title: Walkthrough - Greenhorn - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - pluck-cms
  - rce
  - file-upload
---
# Walkthrough - Greenhorn - A HackTheBox machine

Enumerate open services:

```bash
nmap -sC -sV $ip -Pn
```

Port 22, 80 3000.  Also, banner greenhorn.htb is displayed

- Port 80 has the service HTTP generator Pluck 4.7.18, well-known for a RCE vulnerability.
- Port 3000 contains a Gitea hosting all the source code of the web service on port 80.
- Port 8000 contains a PHP cli server 5.5

Read  `pass.php` file in the `/data/settings/` path. It's a hashed 512 password.

Searching for it you will obtain that password is iloveyou1. 

Enter it in http://greenhorn.htb/login.php and you will access to the admin panel. 

Exploitation of the CMS is done with this POC: https://github.com/Rai2en/CVE-2023-50564_Pluck-v4.7.18_PoC

With that you will get access to the www-data user. Go to home folder. There is an user named junior. 

```
su junior
```

Password is the same as the CMS. Now you can print user.txt

Escalating provileges involves the use of the tool [depix](depix.md) for extracting root password from the pdf file saved at `/home/junior/Using OpenVAS.pd`. 


