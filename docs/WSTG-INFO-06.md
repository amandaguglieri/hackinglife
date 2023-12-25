---
title: Identify Application Entry Points - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-06
---

# Identify Application Entry Points


|ID|Link to Hackinglife|Link to OWASP|Objectives|Tools|
|:---|:---|:---|:---|:---|
|1.6|WSTG-INFO-06|[Identify Application Entry Points](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/06-Identify_Application_Entry_Points)|- Identify possible entry and injection points through request and response analysis which covers hidden fields, parameters, methods HTTP header analysis|OWASP ASD, Burpsuite/ZAP|



### Some enumeration techniques for HTTP verbs

With [netcat](netcat.md)
```bash
# Send a OPTIONS message with netcat
nc victim.target 80
OPTIONS / HTTP/1.0

```



### Kiterunner

[kiterunner Cheat sheet](../kiterunner.md).

Kiterunner is an excellent tool that was developed and released by Assetnote. Kiterunner is currently the best tool available for discovering API endpoints and resources. While directory brute force tools like Gobuster/Dirbuster/ work to discover URL paths, it typically relies on standard HTTP GET requests. Kiterunner will not only use all HTTP request methods common with APIs (GET, POST, PUT, and DELETE) but also mimic common API path structures. In other words, instead of requesting GET /api/v1/user/create, Kiterunner will try POST /api/v1/user/create, mimicking a more realistic request.

**1.** First, download the dictionaries from the [project](https://github.com/assetnote/kiterunner). In my case I downloaded it to /usr/share/wordlists/kiterunner/:

+ https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-large.json.tar.gz
+ https://wordlists-cdn.assetnote.io/rawdata/kiterunner/routes-small.json.tar.gz
+ https://wordlists-cdn.assetnote.io/data/kiterunner/routes-large.kite.tar.gz
+ https://wordlists-cdn.assetnote.io/data/kiterunner/routes-small.kite.tar.gz

**2.** Run a quick scan of your target’s URL or IP address like this:

```bash
kr scan HTTP://127.0.0.1 -w ~/api/wordlists/data/kiterunner/routes-large.kite  
```

But. Note that we conducted this scan without any authorization headers, which the target API likely requires.

To use a dictionary (and not a kite file): 

```bash
kr brute <target> -w ~/api/wordlists/data/automated/nameofwordlist.txt
```

If you have many targets, you can save a list of line-separated targets as a text file and use that file as the target.

One of the coolest Kiterunner features is the ability to replay requests. Thus, not only will you have an interesting result to investigate, you will also be able to dissect exactly why that request is interesting. In order to replay a request, copy the entire line of content into Kiterunner, paste it using the kb replay option, and include the wordlist you used:

```bash
kr kb replay "GET     414 [    183,    7,   8]://192.168.50.35:8888/api/privatisations/count 0cf6841b1e7ac8badc6e237ab300a90ca873d571" -w ~/api/wordlists/data/kiterunner/routes-large.kite
```

Running this will replay the request and provide you with the HTTP response.

To run Kiterunner providing an authorization token as it could be "x-access-token", we can take the full authorization token and add it to your Kiterunner scan with the -H option:

```bash
kr scan http://IP -w /path/to/dict.txt -H 'x-access-token: eyJhGcwisdfdsfdfsdfsdfsdfdsfdsfddfdf.eyfakefakefakefaketokenfakeken._wcoooooo_kkkkkk_kkkk'
```

