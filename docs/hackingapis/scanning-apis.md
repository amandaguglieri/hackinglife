---
title: Scanning APIs
author: amandaguglieri
draft: false
TableOfContents: true
---

# Scanning APIs

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-authentication-attacks.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
    - [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)

Once you have discovered an API and used it as it was intended, you can proceed to perform a baseline vulnerability scan. Most of these scans return false-negative results (because they are web-oriented)  but they are helpful in structuring next steps.

Basic scans you can run:

## nikto

You will get some results related to headers such as:

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type

Run:

```bash
nikto -h http://localhost:8888
```

## OWASP zap

To launch it, run:

```bash
zaproxy
```

You can do several things:

+ Run an automatic attack.
+ Import your spec.yml file and run an automatic attack.
+ Run a manual attack. 

The manual explore option will allow you to perform authenticated scanning. Set the URL to your target, make sure the HUD is enabled, and choose "Launch Browser". 


### How to run a manual attack

Select "Continue to your target". On the right-hand side of the HUD, you can set the Attack Mode to On. This will begin scanning and performing authenticated testing of the target. Now you  perform all the actions (sign up a new user, log  in into the account, modify you avatar, post a comment...).

After that, OWASP Zap allows you to narrow the results to your target. How? In the Sites module, right click on your site and select "Include in context". After that, click on the icon shaped as a "target" to filter out sites by context. 

With the results, start your analysis and remove false-negative vulnerabilities.
 


