---
title: ffuf - A fast web fuzzer written in Go
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# ffuf - A fast web fuzzer written in Go

## Installation

Download from: [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf)


## Basic commands

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ

####### Matchers options #######
# -mc: Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403,405)
# -ml: Match amount of lines in response
# -mr: Match regexp
# -ms: Match HTTP response size
# -mw: Match amount of words in response

####### Filters options #######
# -fc: Filter HTTP status codes from response. Comma separated list of codes and ranges
# -fl: Filter by amount of lines in response. Comma separated list of line counts and ranges
# -fr: Filter regexp
# -fs: Filter HTTP response size. Comma separated list of sizes and ranges
# -fw: Filter by amount of words in response. Comma separated list of word counts and ranges

# Virtual Host enumeration
# use a vhost dictionary file
cp /usr/share/wordlists/secLists/Discovery/DNS/namelist.txt ./vhosts

ffuf -w ./vhosts -u http://$ip -H "HOST: FUZZ.example.com" -fs 612
ffuf -w /path/to/vhost/wordlist -u https://$ip -H "Host: FUZZ" -fs 612
# `-w`: Path to our wordlist
# `-u`: URL we want to fuzz
# `-H "HOST: FUZZ.example.com"`: This is the `HOST` Header, and the word `FUZZ` will be used as the fuzzing point.
# `-fs 612`: Filter responses with a size of 612, default response size in this case.


# Enumerating directories and folders:
ffuf -recursion -recursion-depth 1 -u http://$ip/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-directories-lowercase.txt
# -recursion: activates the recursive scan
# -recursion-depth 1: specifies the maximum depth to scan

# fuzz a combination of folder names, with a wordlist of possible files and a dictionary of extensions
ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://$ip/FOLDERS/WORDLISTEXTENSIONS

```



By pressing ENTER during ffuf execution, the process is paused and user is dropped to a shell-like interactive mode: in this mode, filters can be reconfigured, queue managed and the current state saved to disk.
