---
title: CSRF attack - Cross-site Request Forgery
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, web app pentesting, HTTP headers
---

When it comes to web vulnerabilities, it is useful to have some links at hand:

Owasp vuln description: [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf).


## Using Burp to Test for Cross-Site Request Forgery (CSRF)

**Source**: [https://portswigger.net/support/using-burp-to-test-for-cross-site-request-forgery](https://portswigger.net/support/using-burp-to-test-for-cross-site-request-forgery).

Cross-site request forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which they are currently authenticated.

CSRF vulnerabilities may arise when applications rely solely on HTTP cookies to identify the user that has issued a particular request. Because browsers automatically add cookies to requests regardless of the request's origin, it may be possible for an attacker to create a malicious web site that forges a cross-domain request to the vulnerable application.

Burp has a quite awesome PoC so you can attach proofs to your security reports. Manual is They've released an article about it in [https://portswigger.net/burp/documentation/desktop/functions/generate-csrf-poc](https://portswigger.net/burp/documentation/desktop/functions/generate-csrf-poc).


## Tools and payloads 

- See updated chart: [Attacks and tools for web pentesting](index-attacks-tools-web-pentesting.md).



