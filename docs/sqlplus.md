---
title: sqlplus - To connect and manage the Oracle RDBMS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - oracle tns
  - port 1521
  - tools
---

# sqlplus - To connect and manage the Oracle RDBMS

SQL Plus is a command-line tool that provides access to the Oracle RDBMS. SQLPlus enables you to:

- Enter SQL*Plus commands to configure the SQL*Plus environment.
- Startup and shutdown an Oracle database.
- Connect to an Oracle database.
- Enter and execute SQL commands and PL/SQL blocks.
- Format and print query results.

## Connect to Oracle database

If we manage to get some credentials we can connect to the Oracle TNS service with [sqlplus](sqlplus.md).

```shell-session
sqlplus <username>/<password>@<IP>/XE;
```

In case of this error message ( sqlplus: error while loading shared libraries: libsqlplus.so: cannot open shared object file: No such file or directory), there might be an issue with libraries. Possible solution:

```shell-session
sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig
```

## Basic commands

[All commands from Oracle's documentation](https://docs.oracle.com/cd/E11882_01/server.112/e41085/sqlqraa001.htm#SQLQR985).

```shell-session
# List all available tables in the current database
select table_name from all_tables;

# Show the privileges of the current user
select * from user_role_privs;


```