---
title: CPTS labs - 04 Information Gathering
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 04 Information Gathering
## [Information Gathering - Web Edition](https://academy.hackthebox.com/module/details/144)


### WHOIS

#### Utilizing WHOIS

**Perform a WHOIS lookup against the paypal.com domain. What is the registrar Internet Assigned Numbers Authority (IANA) ID number?**

```
whoid paypal.com
```

Results: 292

**What is the admin email contact for the tesla.com domain (also in-scope for the Tesla bug bounty program)?**

```
whoid tesla.com
```

Results: admin@dnstinations.com



### DNS & Subdomains

#### Digging DNS


**Which IP address maps to inlanefreight.com?**

```
dig +short inlanefreight.com
```

Results: 134.209.24.248



**Which domain is returned when querying the PTR record for 134.209.24.248?**

```
dig -x 134.209.24.248 @1.1.1.1
```

Results:  inlanefreight.com

What is the full domain returned when you query the mail records for facebook.com?

```
dig MX facebook.com
```

Results: smtpin.vvv.facebook.com
#### Subdomain BruteForcing

**Using the known subdomains for inlanefreight.com (www, ns1, ns2, ns3, blog, support, customer), find any missing subdomains by brute-forcing possible domain names. Prov**ide your answer with the complete subdomain, e.g., www.inlanefreight.com.

```
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -r
```

Results: my.inlanefreight.com

#### DNS Zone Transfers

**After performing a zone transfer for the domain inlanefreight.htb on the target system, how many DNS records are retrieved from the target system's name server? Provide your answer as an integer, e.g, 123.**

```
dig axfr inlanefreight.htb @$ip 
```

```
# Response
; <<>> DiG 9.19.21-1-Debian <<>> axfr inlanefreight.htb @10.129.72.193
;; global options: +cmd
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.
admin.inlanefreight.htb. 604800	IN	A	10.10.34.2
ftp.admin.inlanefreight.htb. 604800 IN	A	10.10.34.2
careers.inlanefreight.htb. 604800 IN	A	10.10.34.50
dc1.inlanefreight.htb.	604800	IN	A	10.10.34.16
dc2.inlanefreight.htb.	604800	IN	A	10.10.34.11
internal.inlanefreight.htb. 604800 IN	A	127.0.0.1
admin.internal.inlanefreight.htb. 604800 IN A	10.10.1.11
wsus.internal.inlanefreight.htb. 604800	IN A	10.10.1.240
ir.inlanefreight.htb.	604800	IN	A	10.10.45.5
dev.ir.inlanefreight.htb. 604800 IN	A	10.10.45.6
ns.inlanefreight.htb.	604800	IN	A	127.0.0.1
resources.inlanefreight.htb. 604800 IN	A	10.10.34.100
securemessaging.inlanefreight.htb. 604800 IN A	10.10.34.52
test1.inlanefreight.htb. 604800	IN	A	10.10.34.101
us.inlanefreight.htb.	604800	IN	A	10.10.200.5
cluster14.us.inlanefreight.htb.	604800 IN A	10.10.200.14
messagecenter.us.inlanefreight.htb. 604800 IN A	10.10.200.10
ww02.inlanefreight.htb.	604800	IN	A	10.10.34.112
www1.inlanefreight.htb.	604800	IN	A	10.10.34.111
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 540 msec
;; SERVER: 10.129.72.193#53(10.129.72.193) (TCP)
;; WHEN: Tue Sep 10 15:25:16 EDT 2024
;; XFR size: 22 records (messages 1, bytes 594)
```


Results: 22

**Within the zone record transferred above, find the ip address for ftp.admin.inlanefreight.htb. Respond only with the IP address, eg 127.0.0.1**

Results:  10.10.34.2

**Within the same zone record, identify the largest IP address allocated within the 10.10.200 IP range. Respond with the full IP address, eg 10.10.200.1**

Results:  10.10.200.14

#### Virtual Hosts

**Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "web"? Answer using the full domain, e.g. "x.inlanefreight.htb"**

Important, the --append-domain part

```
gobuster vhost -u http://$domain:$port/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain
```

Results: web17611.inlanefreight.htb

**Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "vm"? Answer using the full domain, e.g. "x.inlanefreight.htb"**

Results: vm5.inlanefreight.htb

**Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "br"? Answer using the full domain, e.g. "x.inlanefreight.htb"**

Results: browser.inlanefreight.htb


**Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "a"? Answer using the full domain, e.g. "x.inlanefreight.htb"**

Results: admin.inlanefreight.htb


**Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "su"? Answer using the full domain, e.g. "x.inlanefreight.htb"**

Results: support.inlanefreight.htb

### Fingerprinting

#### Fingerprinting

**Determine the Apache version running on app.inlanefreight.local on the target system. (Format: 0.0.0)**

```
sudo echo $ip app.inlanefreight.local >> /etc/hosts
curl -I app.inlanefreight.local
```

Results: 2.4.41B



**Which CMS is used on app.inlanefreight.local on the target system? Respond with the name only, e.g., WordPress.**

```
whatweb http://app.inlanefreight.local
```

Results: Joomla


**On which operating system is the dev.inlanefreight.local webserver running in the target system? Respond with the name only, e.g., Debian.**

Results: Ubuntu 

### Crawling

#### Creepy crawlies

**After spidering inlanefreight.com, identify the location where future reports will be stored. Respond with the full domain, e.g., files.inlanefreight.com.**

```
python3 ReconSpider.py https://inlanefreight.com
```

Results: inlanefreight-comp133.s3.amazonaws.htb

### Web Archives


**How many Pen Testing Labs did HackTheBox have on the 8th August 2018? Answer with an integer, eg 1234.**

Go to https://web.archive.org/web/20180808080705/https://www.hackthebox.eu/

Results: 74

**How many members did HackTheBox have on the 10th June 2017? Answer with an integer, eg 1234.**

Go to https://web.archive.org/web/20180808080705/https://www.hackthebox.eu/

Results: 3054

**Going back to March 2002, what website did the facebook.com domain redirect too? Answer with the full domain, eg http://www.facebook.com/**

Go to https://web.archive.org/web/20020601000000*/www.facebook.com

Results:  http://site.aboutface.com/

**According to the paypal.com website in October 1999, what could you use to "beam money to anyone"? Answer with the product name, eg My Device, remove the ™ from your answer.**

Go to https://web.archive.org/web/19991013140707/http://paypal.com/

Results: Palm 0rganizer

**Going back to November 1998 on google.com, what address hosted the non-alpha "Google Search Engine Prototype" of Google? Answer with the full address, eg http://google.com**

Go to https://web.archive.org/web/19981111184551/http://google.com/

Results: http://google.stanford.edu/


**Going back to March 2000 on www.iana.org, when exacty was the site last updated? Answer with the date in the footer, eg 11-March-99**

Go to https://web.archive.org/web/20000303211237/http://www.iana.org/

Results: 17-December-99


**According to the wikipedia.com snapshot taken in March 2001, how many pages did they have over? Answer with the number they state without any commas, eg 2000 not 2,000**

Go to https://web.archive.org/web/20010331173908/http://www.wikipedia.com/

Results: 3000


### Skills Assessment

**What is the IANA ID of the registrar of the inlanefreight.com domain?**

```
whois inlanefreight.com
```

Results: 468


**What http server software is powering the inlanefreight.htb site on the target system? Respond with the name of the software, not the version, e.g., Apache.**

```
curl -I $ip:$port
```

Results: nginx


**What is the API key in the hidden admin directory that you have discovered on the target system?**

```
# 1. Add $ip inlanefreight.htb to /etc/hosts

# 2. Create variable $port

# 3. Do a vhost scan. For instance
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt:FUZZ -u http://inlanefreight.htb:$port -H "HOST:FUZZ.inlanefreight.htb" -fs 120

# 4. Add the discovered VHOST to /etc/hosts

# 5. Enumerate the site 
dirb http://web1337.inlanefreight.htb:$port

# 6. There is a robots.txt file in the results, with a hiden admin panel. Trying to access directly the panel returns a 404. However we could try to fuzz it deeper:
ffuf -recursion -recursion-depth 1 -u http://web1337.inlanefreight.htb:53178/admin_h1dd3n/FUZZ -w /usr/share/seclists//Discovery/Web-Content/common.txt

# 7. There is one result: index.html. Go to http://web1337.inlanefreight.htb:$port/admin_h1dd3n/index.html to retrieve the flag.


```

Results:  e963d863ee0e82ba7080fbf558ca0d3f

 **After crawling the inlanefreight.htb domain on the target system, what is the email address you have found? Respond with the full email, e.g., mail@inlanefreight.htb.**

```
# 1. Following the previous question, additional vhost discovery could be done:
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt:FUZZ -u http://inlanefreight.htb:$port -H "HOST:FUZZ.web1337.inlanefreight.htb" -fs 120
# Add the second discovered VHOST (`dev`) to /etc/host, and visit the site http://dev.web1337.inlanefreight.htb/index.html. Notice that there is a next button, that takes you to a http://dev.web1337.inlanefreight.htb/index-123.html. Set-up an intruder attack with Numbered payload

```

![pay](img/payload_00.png)

![pay](img/payload_02.png)

Results:   1337testing@inlanefreight.htb


**What is the API key the inlanefreight.htb developers will be changing too?**


![pay](img/payload_01.png)

Results: ba988b835be4aa97d068941dc852ff33


