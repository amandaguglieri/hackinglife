---
title: msSQL - Microsoft SQL Server
author: amandaguglieri
draft: false
TableOfContents: true
tag: database,Cheat sheet
---

# msSQL - Microsoft SQL Server

Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network. [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_SQL_Server).


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
