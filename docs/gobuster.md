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

## Enumerate subdomains

From HackTheBox machine - Three:

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```

## Enumerate Virtual Hosts

There are a couple of things you need to prepare to brute force `Host` headers:

1. `Target Identification`: First, identify the target web server's IP address. This can be done through DNS lookups or other reconnaissance techniques.
2. `Wordlist Preparation`: Prepare a wordlist containing potential virtual host names. You can use a pre-compiled wordlist, such as SecLists, or create a custom one based on your target's industry, naming conventions, or other relevant information.


```shell-session
gobuster vhost -u http://$ip -w <wordlist_file> --append-domain
# The `-u` flag specifies the target URL
# The `-w` flag specifies the wordlist file 
# The `--append-domain` flag appends the base domain to each word in the wordlist. In newer versions of Gobuster, the --append-domain flag is required to append the base domain to each word in the wordlist when performing virtual host discovery. This flag ensures that Gobuster correctly constructs the full virtual hostnames, which is essential for the accurate enumeration of potential subdomains. In older versions of Gobuster, this functionality was handled differently, and the --append-domain flag was not necessary.
```

- Consider using the `-t` flag to increase the number of threads for faster scanning.
- The `-k` flag can ignore SSL/TLS certificate errors.
- You can use the `-o` flag to save the output to a file for later analysis.

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

