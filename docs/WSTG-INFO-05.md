
---
title: Review Webpage content for Information Leakage - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-05
---

# Review Webpage content for Information Leakage

|ID|Link to Hackinglife|Link to OWASP|Objectives|Tools|
|:---|:---|:---|:---|:---|
|1.5|WSTG-INFO-05|[Review Webpage Content for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage)|- Review webpage comments, metadata, and redirect bodies to find any information leakage.  - Gather JavaScript files and review the JS code to better understand the application and to find any information leakage.  <br>- Identify if source map files or other front-end debug files exist.|Browser, Curl, Burpsuite/ZAP|


Sensitive information can include (but not limited to): Private API keys, internal IP addresses, debugging information, sensitive routes, or even credentials. 

## Review HTTP comments

```
<!--
```

## Review `META`tags

They do not provide a vector attack directly, but allows an attacker to profile an application:

```
<META name="Author" content="John Smith">
```


## Review javascript comments


````
```
````

And

```
/*
```

And the `<script>` tag.


## Review Source map files

By adding .map extension to .js files.
