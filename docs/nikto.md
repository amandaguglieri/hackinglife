---
title: nikto
author: amandaguglieri
draft: false
TableOfContents: true
---

# nikto

You will get some results related to headers such as, for example:

+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type

Run:

```bash
nikto -h http://localhost:8888
```
