---
title: nikto
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - reconnaissance
  - WSTG-INFO-02
---

# nikto

You will get some results related to headers such as, for example:

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type

Run:

```bash
nikto -h domain.com -o nikto.html -Format html


nikto -h http://domain.com/index.php?page=target-page.php -Tuning 5 -Display V
# -Display V : turn verbose mode on
# -Tuning 5 : Level 5 is considered aggressive, covering a wide range of tests but may also increase the likelihood of false positives. 
```

