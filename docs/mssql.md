---
title: msSQL - Microsoft SQL Server
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - cheat sheet
---

# MSSQL - Microsoft SQL Server

Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network. [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_SQL_Server).

[By default, MSSQL uses ports `TCP/1433` and `UDP/1434`](1433-mssql.md).  However, when MSSQL operates in a "hidden" mode, it uses the `TCP/2433` port.
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

## Authentication Mechanisms

MSSQL supports two authentication modes, which means that users can be created in Windows or the SQL Server:

- Windows authentication mode: This is the default, often referred to as integrated security because the SQL Server security model is tightly integrated with Windows/Active Directory. Specific Windows user and group accounts are trusted to log in to SQL Server. Windows users who have already been authenticated do not have to present additional credentials.
- Mixed mode: Mixed mode supports authentication by Windows/Active Directory accounts and SQL Server. Username and password pairs are maintained within SQL Server.

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


## Interact with MSSQL

### From Linux

[sqsh](sqsh.md)


```shell-session
 sqsh -S $IP -U username -P Password123 -h
 # -h: disable headers and footers for a cleaner look.

# When using Windows Authentication, we need to specify the domain name or the hostname of the target machine. If we don't specify a domain or hostname, it will assume SQL Authentication.
sqsh -S $ip -U .\\<username> -P 'MyPassword!' -h
# For windows authentication we can use  SERVERNAME\\accountname or .\\accountname
```

### From Windows

[sqlcmd](https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility) 

The `sqlcmd` utility lets you enter Transact-SQL statements, system procedures, and script files through a variety of available modes:

- At the command prompt.
- In Query Editor in SQLCMD mode.
- In a Windows script file.
- In an operating system (Cmd.exe) job step of a SQL Server Agent job.

> Careful. In some environments the command GO needs to be in lowercase.

```cmd-session
sqlcmd -S $IP -U username -P Password123


# We need to use GO after our query to execute the SQL syntax. 
# List databases
SELECT name FROM master.dbo.sysdatabases
go

# Use a database
USE dbName
go

# Show tables
SELECT table_name FROM dbName.INFORMATION_SCHEMA.TABLES
go

# Select all Data from Table "users"
SELECT * FROM users
go

```


### GUI Application

 [mssql-cli](https://github.com/dbcli/mssql-cli), [mssqlclient.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/mssqlclient.py), [dbeaver](https://github.com/dbeaver/dbeaver) 

####  SQL Server Management Studio or SSMS 

Only in windows. Download, install, and connect to database.

#### dbeaver

dbeaver is a multi-platform database tool for Linux, macOS, and Windows that supports connecting to multiple database engines such as MSSQL, MySQL, PostgreSQL, among others, making it easy for us, as an attacker, to interact with common database servers.

#### mssqlclient.py

Alternatively, we can use the tool from Impacket with the name `mssqlclient.py`.

```shell-session
mssqlclient.py -p 1433 <username>@$ip 
```


## Basic commands

```
# Get Microsoft SQL server version
select @@version;

# Get usernames
select user_name()
go 

# Get databases
SELECT name FROM master.dbo.sysdatabases
go

# Get current database
SELECT DB_NAME()
go

# Get a list of users in the domain
SELECT name FROM master..syslogins
go

# Get a list of users that are sysadmins
SELECT name FROM master..syslogins WHERE sysadmin = 1
go

# And to make sure: 
SELECT is_srvrolemember(‘sysadmin’)
go
# If your user is admin, it will return 1.

# Read Local Files in MSSQL
SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
```

Also, you might be interested in executing a cmd shell using [xp_cmdshell by reconfiguring sp_configure](1433-mssql.md).



