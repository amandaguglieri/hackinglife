---
title: MariaDB
author: amandaguglieri
draft: false
TableOfContents: true
tag: database,"relational database",SQL
---

# MariaDB

MariaDB is an open source relational database management system (RDBMS) that is a compatible drop-in replacement for the widely used MySQL database technology. It is developed by MariaDB Foundation and initially released on 29 October 2009. MariaDB has a significantly high number of new features, which makes it better in terms of performance and user-orientation than MySQL.

## Basic commands

```mariadb
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

## Connect to database: mariadb

```bash
# -h host/ip   
# -u user As default mariadb has a root user with no authentication
mariadb -h <host/IP> -u root
```

