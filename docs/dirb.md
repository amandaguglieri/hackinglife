---
title: dirb
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, directory enumeration, tool, vulnerability
---


DIRB is a web content fingerprinting tool. It scans the server for directories using a dictionary file.

Scan the web server (http://192.168.1.224/) for directories using a dictionary file (/usr/share/wordlists/dirb/common.txt):

## Dictionaries 

See [wordlists](wordlists.md).

Path to default dictionary: /usr/share/dirb/wordlists/

## Basic commands

```bash
dirb <HOST> -w /path/to/dictionary.txt -o results.txt
# -w: to specify the path to the dictionary.
# -o: to print results to a file.
# -a: agent application. In case that the app checks out this header (use it with https://useragentstring.com/pages/useragentstring.php)
# -p: for indicating a proxy (for instance, Burp: dirb <target host or IP> -p http://127.0.0.1:8080)
# -c: it adds a cookie (dirb <target host or IP> -c “MYCOOKIE: ashdkjashdjkas”)
# -H: it adds a customized header (dirb <target host or IP> -H “MYHEADER: Mycontent”)
# -r: don’t search recursively in directories
# -z: it adds a millisecond delay to not cause excessive Flood.
# -S: silent mode. It doesn’t show tested words.
# -X: It allows us to specify extensions (dirb <target host or IP> -X “.php, .bak”). Appends each word with this extension
# -x:  It allows us to use a file with extensions (dirb <target host or IP> -x extensionfile.txt). Appends each word with the extensions specified in the file
# -o: to save the results in an output file
```
