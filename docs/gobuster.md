---
title: gobuster
author: amandaguglieri
draft: false
TableOfContents: true
---

# gobuster

Great tool to brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). Also, dictionaries are not API-specific. But here are some commands for Gobuster:

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 401 
# -b flag is to exclude from results an specific http response`
```

## Example

```bash
gobuster dir -u https://friendzone.red/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x txt,php -t 20 -k

# dir to search for directories
# -t number of concurrent threads
# -k to avoid error message about certificate: nvalid certificate: x509: certificate has expired or is not yet valid
# -x to indicate an extension for the file
# -w to indicate a dictionary or wordlist



# -l Display the length of the response
# -s Show an especific status code
# -r Follow redirect

```
