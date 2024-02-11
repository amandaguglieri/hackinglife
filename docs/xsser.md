---
title: XSSer -  An automated web pentesting framework tool to detect and exploit XSS vulnerabilities
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# XSSer - An automated web pentesting framework tool to detect and exploit XSS vulnerabilities

A Cross Site Scripter (or XSSer) is an automatic framework to detect, exploit and report XSS vulnerabilities in web-based applications. It contains several options to try to bypass certain filters, and various special techniques of code injection. XSSer has pre-installed ( `> 1300 XSS` ) attacking vectors and can bypass-exploit code on several browsers/WAFs.

## Installation

```bash
sudo apt install xsser
```


## Usage 

Capture with BurpSuite a POST request and fuzz it with XSSER:

```
xsser --url "http://demo.ine.local/index.php?page=dns-lookup.php" -p "target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS" --auto
# --url: to introduce the target
# -p: Payload (it's the body of the POST request captured with Burpsuite). Use the characters 'XSS' to indicate where you want to inject the payloads that xsser is going to fuzz.
#--auto: Inject a list of vectors provided by XSSer.
# In the results you will have a confirmation about that parameter being injectable, and an example of payload. Use it for launching the Final Payload (-Fp).

xsser --url "http://demo.ine.local/index.php?page=dns-lookup.php" -p "target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS" --Fp "<script>alert(1)</script>"
```

With this, the encoded XSS payload is generated. Now, in Burp Suite, replace the POST parameters with the final attack payload and forward the request.

Launch the XSSer interface:

```
xsser --gtk
```

