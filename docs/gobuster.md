---
title: gobuster
author: amandaguglieri
draft: false
TableOfContents: true
---

# gobuster

Great tool to brute force directory discovery but it's not recursive (you need to specify a directory to perform a deeper scanner). 

## Installation

Repository: [https://github.com/OJ/gobuster](https://github.com/OJ/gobuster)

Also, dictionaries are not API-specific. But here are some commands for Gobuster:


```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 403,4.4 -x .php,.txt -r 
# -b: exclude from results an specific http response`
# -r: follow redirects
# -x: add to the path provided by dictionary these extensions
```

## Enumerate subdomains:

From HackTheBox machine - Three:

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```


## Examples from real life

```bash
gobuster dir -u https://friendzone.red/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x txt,php -t 20 -k

# dir to search for directories
# -t number of concurrent threads
# -k to avoid error message about certificate: invalid certificate: x509: certificate has expired or is not yet valid
# -x to indicate an extension for the file
# -w to indicate a dictionary or wordlist



# -l Display the length of the response
# -s Show an especific status code
# -r Follow redirect

```

