---
title: CSRF attack - Cross-site Request Forgery
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - attack
  - HTTP headers
---

# CSRF attack - Cross-site Request Forgery

Cross-site request forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which they are currently authenticated.

CSRF vulnerabilities may arise when applications rely solely on HTTP cookies to identify the user that has issued a particular request. Because browsers automatically add cookies to requests regardless of the request's origin, it may be possible for an attacker to create a malicious web site that forges a cross-domain request to the vulnerable application.

When it comes to web vulnerabilities, it is useful to have some links at hand:

+ Owasp vuln description: [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf).
+ Using Burp to Test for Cross-Site Request Forgery (CSRF): [https://portswigger.net/support/using-burp-to-test-for-cross-site-request-forgery](https://portswigger.net/support/using-burp-to-test-for-cross-site-request-forgery).
+ PoC with Burp, official link: [https://portswigger.net/burp/documentation/desktop/functions/generate-csrf-poc](https://portswigger.net/burp/documentation/desktop/functions/generate-csrf-poc).

## Using Burp 

Burp has a quite awesome PoC so you can generate HTML (and javascript) code to replicate this attack.

1. Select a URL or HTTP request anywhere within Burp, and choose Generate CSRF PoC within Engagement tools in the context menu. 
![Step 1](img/csrf-1.png)


2. You have two buttons: one for editing the request manually (Regenerate button) the HTML based on the updated request; and tje ptjer to test the effectiveness of the generated PoC in Burp's browser (Test in browser button).

3. Open the crafted page from the same browser where the user has been logged in.

4. Observe the result, i.e. check if the web server executed the request.


## Related labs

+ [https://portswigger.net/web-security/all-labs#cross-site-request-forgery-csrf](https://portswigger.net/web-security/all-labs#cross-site-request-forgery-csrf)



## Tools and payloads 

- See updated chart: [Attacks and tools for web pentesting](web-exploitation.md).



