---
title: "5432 postgresql"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - postgresql
  - port 5432
---

# 5432 postgreSQL

[https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql](https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql).

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


## Description
In some cases, the default service that runs on TCP port 5432 is PostgreSQL, which is a database management system: creating, modifying, and updating databases, changing and adding data, and more. PostgreSQL can typically be interacted with using a command-line tool called psql.

```bash
psql
```


## Installation

### Linux

If the tool is not installed, then run:

```bash
sudo apt install postgresql-client-common
```

If your user is not in the sudoers file, we can do some workarounds about it. Some options arise here:

-uploading static binaries onto the target machine,
-port-forwarding, or tunneling, using SSH.

Using SSH and postgresql:

**1.** In the attacking machine:

```bash
ssh UserNameInTheAttackedMachine@IPOfTheAttackedMachine -L 1234:localhost:5432 
# We will listen for incoming connections on our local port 1234. When a client connects to our local port, the SSH client will forward the connection to the remote server on port 22. This allows the local client to access services on the remote server as if they were running on the local machine.
# We are forwarding traffic from any given local port, for instance 1234, to the port on which PostgreSQL is listening, namely 5432, on the remote server. We therefore specify port 1234 to the left of localhost, and 5432 to the right, indicating the target port.
```

**2.** In another terminal in the attacking machine:

```bash
sudo apt update && sudo apt install postgresql postgresql-client-common 
# this will install postgresql in case you don't have it.

psql -U christine -h localhost -p 1234
# Using our installation of psql, we can now interact with the PostgreSQL service running locally on the target machine:
# -U: to specify user.
# -h: to specify localhost. 
# -p 1234 as we are targeting the tunnel we created earlier with SSH, we need to specify which is the port the tunnel is listening on.
```


### Powershell

```
Install-Module PostgreSQLCmdlets

```




## Basics commands in postgresql

```bash
# List databases
# Short version: \l
\list

# Connect to a database
# Short version: \c NameOfDataBase
\connect NameOfDatabase

# List database tables (once you have selected a database)
\dt

# Dump content from a column
SELECT * FROM NameOfColumn;
# Watch out! Case sensitive
```



