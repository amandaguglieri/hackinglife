---
title: msSQL - Microsoft SQL Server
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - cheat sheet
---

# msSQL - Microsoft SQL Server

Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network. [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_SQL_Server).

## MSSQL Databases

MSSQL has default system databases that can help us understand the structure of all the databases that may be hosted on a target server.

|Default System Database|Description|
|---|---|
|`master`|Tracks all system information for an SQL server instance|
|`model`|Template database that acts as a structure for every new database created. Any setting changed in the model database will be reflected in any new database created after changes to the model database|
|`msdb`|The SQL Server Agent uses this database to schedule jobs & alerts|
|`tempdb`|Stores temporary objects|
|`resource`|Read-only database containing system objects included with SQL server|

Table source: [System Databases Microsoft Doc](https://docs.microsoft.com/en-us/sql/relational-databases/databases/system-databases?view=sql-server-ver15) and HTB Academy



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

Also, you might be interested in executing a cmd shell using [xp_cmdshell by reconfiguring sp_configure](1433-mssql.md).


##  MSSQL Clients

- [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) (`SSMS`) comes as a feature that can be installed with the MSSQL install package or can be downloaded & installed separately
- [mssql-cli](https://docs.microsoft.com/en-us/sql/tools/mssql-cli?view=sql-server-ver15)
- [SQL Server PowerShell](https://docs.microsoft.com/en-us/sql/powershell/sql-server-powershell?view=sql-server-ver15)|
- [HediSQL](https://www.heidisql.com)
- [SQLPro](https://www.macsqlclient.com)
- [Impacket's mssqlclient.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/mssqlclient.py) To locate it:

```shell-session
locate mssqlclient
```


Of the MSSQL clients listed above, pentesters may find Impacket's mssqlclient.py to be the most useful due to SecureAuthCorp's Impacket project being present on many pentesting distributions at install.


## Database configuration

When an admin initially installs and configures MSSQL to be network accessible, the SQL service will likely run as `NT SERVICE\MSSQLSERVER`. Connecting from the client-side is possible through Windows Authentication, and by default, encryption is not enforced when attempting to connect.

Authentication being set to `Windows Authentication` means that the underlying Windows OS will process the login request and use either the local SAM database or the domain controller (hosting Active Directory) before allowing connectivity to the database management system.

Misconfigurations to look at:

- MSSQL clients not using encryption to connect to the MSSQL server.    
- The use of self-signed certificates when encryption is being used. It is possible to spoof self-signed certificates   
- The use of [named pipes](https://docs.microsoft.com/en-us/sql/tools/configuration-manager/named-pipes-properties?view=sql-server-ver15)
- Weak & default `sa` credentials. Admins may forget to disable this account
