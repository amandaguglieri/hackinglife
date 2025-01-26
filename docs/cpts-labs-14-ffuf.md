---
title: CPTS labs - 14 Attacking Web Applications with Ffuf
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---

# CPTS labs - 14 Attacking Web Applications with Ffuf

## [Attacking Web Applications with Ffuf](https://academy.hackthebox.com/module/details/54)

### Basic Fuzzing

#### Directory fuzzing

**In addition to the directory we found above, there is another directory that can be found. What is it?**

``` shell-session 
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt  -u http://$ip:$port/FUZZ
```

Results: forum

#### Page fuzzing


**Try to use what you learned in this section to fuzz the '/blog' directory and find all pages. One of them should contain a flag. What is the flag?.**

``` shell-session 
# Find the extension in use
ffuf -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://$ip:$port/blog/indexFUZZ

# As it is php, we will fuzz now possible existent files.php 
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://$ip:$port/blog/FUZZ.php

# We obtain http://$ip:$port/blog/home.php
```

Results: HTB{bru73_f0r_c0mm0n_p455w0rd5}

#### Recursive fuzzing
**Try to repeat what you learned so far to find more files/directories. One of them should give you a flag. What is the content of the flag?.**

``` shell-session 
ffuf  -recursion -recursion-depth 1 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ  -u http://$ip:$port/FUZZ -e .php 

### We obtain http://$ip:$port/forum/flag.php and the flag is there. 
```

Results: HTB{fuzz1n6_7h3_w3b!}


### Domain Fuzzing
#### Subdomain fuzzing 
**Try running a sub-domain fuzzing test on 'inlanefreight.com' to find a customer sub-domain portal. What is the full domain of it?.**

``` shell-session 
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://FUZZ.inlanefreight.com/
```

Results: customer.inlanefreight.com

#### Filtering results
**Try running a VHost fuzzing scan on 'academy.htb', and see what other VHosts you get. What other VHosts did you get?.**

``` shell-session 
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:$port -H 'Host: FUZZ.academy.htb' -fs 986
```

Results: test.academy.htb

### Parameter fuzzing

#### Parameter fuzzing - GET
**Using what you learned in this section, run a parameter fuzzing scan on this page. what is the parameter accepted by this webpage?.**

``` shell-session 
# We enumerate:
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:$por/admin/admin.php?FUZZ=key -fs 798

# And we obtain user. We enter http://admin.academy.htb:30721/admin/admin.php?user=key and obtain the message, You don't have access to read the flag. We enter http://admin.academy.htb:30721/admin/admin.php?user=admin and obtain the message "This method is deprecated"

ffuf -w  /usr/share/wordlists/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:$port/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx

```

Results: user

#### Value  fuzzing
**Try to create the 'ids.txt' wordlist, identify the accepted value with a fuzzing scan, and then use it in a 'POST' request with 'curl' to collect the flag. What is the content of the flag?.**

``` shell-session 
# First create a list of 1000 id values, from 1 to 1000
for i in $(seq 1 1000); do echo $i >> ids.txt; done
# Now, fuzz
ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:$port/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
# it will return the payload 73. Now with curl:
curl http://admin.academy.htb:$port/admin/admin.php -X POST -d 'id=73' -H 'Content-Type: application/x-www-form-urlencoded' 
```

Results: HTB{p4r4m373r_fuzz1n6_15_k3y!}


### Skills assessment - Web fuzzing

**Run a sub-domain/vhost fuzzing scan on '*.academy.htb' for the IP shown above. What are all the sub-domains you can identify? (Only write the sub-domain name).**

``` shell-session 
ffuf -w  /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:$port/ -H 'Host: FUZZ.academy.htb' -fs 985
```

Results: test archive faculty

**Before you run your page fuzzing scan, you should first run an extension fuzzing scan. What are the different extensions accepted by the domains?.**

``` shell-session 
ffuf -w  /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://academy.htb:$port/indexFUZZ -H 'Host:test.academy.htb'
ffuf -w  /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://academy.htb:$port/indexFUZZ -H 'Host:archive.academy.htb'
ffuf -w  /usr/share/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://academy.htb:$port/indexFUZZ -H 'Host:faculty.academy.htb'
```

Results: php phps php7

** One of the pages you will identify should say 'You don't have access!'. What is the full page URL?.**

``` shell-session 
ffuf -w  /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ  -u http://faculty.academy.htb:$port/FUZZ  -recursion -recursion-depth 1 -e .php,.php7,.phps -fc 403

```

Results:  http://faculty.academy.htb:PORT/courses/linux-security.php7

** In the page from the previous question, you should be able to find multiple parameters that are accepted by the page. What are they?.**

``` shell-session 
# First, we fuzz parameters:
ffuf -w  /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ  -u http://faculty.academy.htb:$port/courses/linux-security.php7?FUZZ=1   -fs 774

# We obtain user. We enter http://faculty.academy.htb:$port/courses/linux-security.php7?user=admin in the browsers. When accessing, we read the message "This method is no longer used." printed on the screen. So we try to FUZZ the value of the user parameter with the POST method
ffuf -w  /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ  -u "http://faculty.academy.htb:$port/courses/linux-security.php7"  -X POST -d "FUZZ=key" -H 'Content-Type: application/x-www-form-urlencoded'  -fs 774 

```

Results:  user, username


**Try fuzzing the parameters you identified for working values. One of them should return a flag. What is the content of the flag?.**

``` shell-session 
ffuf -w  /usr/share/seclists/Usernames/Names/names.txt:FUZZ  -u "http://faculty.academy.htb:$port/courses/linux-security.php7"  -X POST -d "username=FUZZ" -H 'Content-Type: application/x-www-form-urlencoded'  -fs 781

# This returns 'harry'. Now we curl that url
curl  "http://faculty.academy.htb:$port/courses/linux-security.php7"  -X POST -d "username=harry"  
```

Results:  HTB{w3b_fuzz1n6_m4573r}

