---
title: fierce - DNS scanner that helps locate non-contiguous IP space and hostnames
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---

# fierce - DNS scanner that helps locate non-contiguous IP space and hostnames

Fierce is a semi-lightweight scanner that helps locate non-contiguous IP space and hostnames against specified domains.  It's  really  meant  as  a pre-cursor to nmap, OpenVAS, nikto, etc, since all of those require that you already know what IP space you are looking for.  This does not perform exploitation and does not scan the whole internet indiscriminately. It is  meant  specifically to  locate likely targets both inside and outside a corporate network.  Because it uses DNS primarily you will often find mis-configured networks that leak internal address space. That's especially useful in targeted malware. Originally  written  by  RSnake along with others at http://ha.ckers.org/. 

```
# Perform a dns transfer using a wordlist againts domain.com
fierce -dns domain.com 

# Brute force subdomains with a seclist
fierce --domain domain.com --subdomain-file fierce-hostlist.txt
```

