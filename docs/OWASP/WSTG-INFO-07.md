---
title: Map Execution Paths through applications - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-07
---

# Map Execution Paths through applications

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 1. Information Gathering > 1.7. Map Execution Paths through applications

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.7|[WSTG-INFO-07](WSTG-INFO-07.md)|[Map Execution Paths Through Application](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/07-Map_Execution_Paths_Through_Application)|- Map the target application and understand the principal workflows.  - Use HTTP(s) Proxy Spider/Crawler feature aligned with application walkthrough|

Map  the target application and understand the principal workflows (paths, data flow and race conditions.)

You may use authomatic spidering tools such as Zed Attack Proxy (ZAP).


## Spidering

### HTTRack

[HTTRack tutorial](../httrack.md)

Create a folder for replicating in it your target.

```
mkdir targetsite
httrack domain.com  targetsite/
```

Interactive mode:

```
httrack
```

### EyeWitness

[EyeWitness tutorial](../eyewitness.md)

First, create a file with the target domains, like for instance, listOfdomains.txt.

Then, run:

```
eyewitness --web -f listOfdomains.txt -d path/to/save/
```

After that you will get a report.html file with the request and a screenshot of those domains.

```
# Proxing the request via BurpSuite
eyewitness --web -f listOfdomains.txt -d path/to/save/ --proxy-ip 127.0.0.1 --proxy-port 8080
```


## Directory/File enumeration

### nmap

```
nmap -sV -p80 --script=http-enum <target>
```

### dirb

[Cheat sheet with dirb](../dirb.md).

```
dirb http://domain.com /usr/share/metasploit-framework/data/wordlists/directory.txt
```

### gobuster

[Gobuster](../gobuster.md):

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 403,4.4 -x .php,.txt -r 
# -b: exclude from results an specific http response`
# -r: follow redirects
# -x: add to the path provided by dictionary these extensions
```


### Ffuf

[Ffuf](../ffuf.md):

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ

# Assuming that the default virtualhost response size is 4242 bytes, we can filter out all the responses of that size (`-fs 4242`)while fuzzing the Host - header:
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242

# Enumerating directories and folders:
ffuf -recursion -recursion-depth 1 -u http://$ip/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-small-directories-lowercase.txt
# -recursion: activates the recursive scan
# -recursion-depth 1: specifies the maximum depth to scan

# fuzz a combination of folder names, with a wordlist of possible files and a dictionary of extensions
ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://$ip/FOLDERS/WORDLISTEXTENSIONS
```


### Wfuzz

[Wfuzz](../wfuzz.md)

### feroxbuster

[feroxbuster](../feroxbuster.md)
