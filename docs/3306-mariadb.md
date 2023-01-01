---
title: "3306 mariadb"
draft: false
TableOfContents: true
---

## Description

**MySQL**: MySQL is an open-source relational database management system(RDBMS) based on Structured Query Language (SQL). It is developed and managed by oracle corporation and initially released on 23 may, 1995. It is widely being used in many small and large scale industrial applications and capable of handling a large volume of data. After the acquisition of MySQL by Oracle, some issues happened with the usage of the database and hence MariaDB was developed.

**MariaDB**: MariaDB is an open source relational database management system (RDBMS) that is a compatible drop-in replacement for the widely used MySQL database technology. It is developed by MariaDB Foundation and initially released on 29 October 2009. MariaDB has a significantly high number of new features, which makes it better in terms of performance and user-orientation than MySQL.



## Connect to database

```bash
# -h host/ip   
# -u user As default mariadb has a root user with no authentication
mariadb -h <host/IP> -u root
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

