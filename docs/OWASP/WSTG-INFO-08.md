---
title: Fingerprint Web Application Framework - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-08
---

# Fingerprint Web Application Framework

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 1. Information Gathering > 1.8. Fingerprint Web Application Framework

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.8|[WSTG-INFO-08](WSTG-INFO-08.md)|[Fingerprint Web Application Framework](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/08-Fingerprint_Web_Application_Framework)|- Fingerprint the components being used by the web applications.  - Find the type of web application framework/CMS from HTTP headers, Cookies, Source code, Specific files and folders, Error message.|


## HTTP headers

- Note the response header `X-Powered-By`, or `X-Generator` as well.
- Identify framework specific cookies. For instance, the cookie `CAKEPHP` for php.


## HTML source code

- Framework is often include in the `META` tag.
- Revise header and footer sections carefully: general markers and specific markers.
- See typical file and folders structure. An example would be wp-includes folder for a wordpress installation, or a CHANGELOG file for a Drupal one.
- Check out file extensions, as sometimes they reveals the underlying framework.
- Revise error messages. They commonly reveals framework.

See [WSTG-INFO-07](WSTG-INFO-07.md) for a reference to [HTTRack](../httrack.md) for mirrowing the code and [EyeWitness](../eyewitness.md). These utilities replicated the source code of the target domain.


## Tools


**1. HTTP headers**:

X-Powered-By and cookies: 
- .NET: `ASPSESSIONID<RANDOM>=<COOKIE_VALUE>`
- PHP: `PHPSESSID=<COOKIE_VALUE>`
- JAVA: `JSESSION=<COOKIE_VALUE>`

**2. [whatweb](../whatweb.md)**.

```bash
whatweb -a3 https://www.example.com -v
# -a3: aggression level 3
# -v: verbose mode
```

**3. Wappalyzer**: [https://www.wappalyzer.com](https://www.wappalyzer.com).

**4. [wafw00f](../wafw00f.md)**:

```shell-session
wafw00f -v https://www.example.com

# -a: check all possible WAFs in place instead of stopping scanning at the first match.
# -i: read targets from an input file 
# -p proxy the requests 
```

**5.**  [Aquatone](../aquatone.md)

```bash
cat example_of_list.txt | aquatone -out ./aquatone -screenshot-timeout 1000
```


**6**. Addons for browsers: 

- [BuiltWith](https://addons.mozilla.org/es/firefox/addon/builtwith/): BuiltWith® covers 93,551+ internet technologies which include analytics, advertising, hosting, CMS and many more.


**7.** [Curl](../curl.md):

```bash
curl -IL https://<TARGET>
# -I: --head (HTTP  FTP  FILE) Fetch the headers only!
# -L, --location: (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response  code),  this  option  will make  curl  redo the request on the new place. If used together with -i, --include or -I, --head, headers from all requested pages will be shown. 
```

**8**. [nmap](../nmap.md):

```shell-session
sudo nmap -v $ip --script banner.nse
```


