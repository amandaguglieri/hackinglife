---
title: feroxbuster
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, web enumeration, tool, reconnaissance
---

feroxbuster is used to perform forced browsing. Forced browsing allows us to enumerate and access resources that are not referenced by the web application, but are still accessible by an attacker. 

Feroxbuster uses brute force combined with a wordlist to search for unlinked content in target directories.

## Installation

See the repo: [https://github.com/epi052/feroxbuster](https://github.com/epi052/feroxbuster).


```bash
sudo apt update && sudo apt install -y feroxbuster
```

## Dictionaries

path to dictionary: /etc/feroxbuster/ferox-config.toml


## Basic commands

```bash
# Include headers in the request
feroxbuster -u http://127.1 -H Accept:application/json "Authorization: Bearer {token}"

# Read urls from STDIN; pipe only resulting urls out to another tool
cat targets | feroxbuster --stdin --silent -s 200 301 302 --redirects -x js | fff -s 200 -o js-files

# Proxy traffic through Burp
feroxbuster -u http://127.1 --insecure --proxy http://127.0.0.1:8080

# Proxy traffic through a SOCKS proxy (including DNS lookups)
feroxbuster -u http://127.1 --proxy socks5h://127.0.0.1:9050

# Pass auth token via query parameter
feroxbuster -u http://127.1 --query token=0123456789ABCDEF
```
