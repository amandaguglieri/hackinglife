---
title: 3128 squid 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - port 3128
  - proxy
---

# 3128 Squid

**Squid** is a caching and forwarding HTTP web proxy. It has a wide variety of uses, including speeding up a web server by caching repeated requests, caching web, DNS and other computer network lookups for a group of people sharing network resources, and aiding security by filtering traffic.


Squid is a widely used open-source proxy server and web cache daemon. It primarily operates as a proxy server, which means it acts as an intermediary between client devices (such as computers or smartphones) and web servers, facilitating requests and responses between them. 

Squid is commonly deployed in network environments to improve performance, enhance security, and manage internet access. Squid can cache frequently requested web content locally. When a client requests a web page or object that Squid has cached, it serves the content from its cache instead of fetching it from the original web server.

Access Control: Squid provides robust access control mechanisms. Administrators can configure rules to control which clients are allowed to access specific websites or web services. 

Content Filtering: Squid can be used for content filtering and blocking access to specific websites or categories of websites (e.g., social media, adult content). This feature is often used by organizations to enforce acceptable use policies.

## Enumeration

```
# Proxify curl
curl -x -proxy http://$ip$:3128 http://$ip$ -H "User-Agent:Firefox"
```

