---
title: Map Application architecture - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-10
---

# Map Application architecture


!!! quote ""
	[OWASP Web Security Testing Guide 4.2](web-security-testing-guide.md) > 1. Information Gathering > 1.10. Map Application architecture

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.10|[WSTG-INFO-10](WSTG-INFO-10.md)|[Map Application Architecture](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/10-Map_Application_Architecture)|- Understand the architecture of the application and the technologies in use. - Identify application architecture whether on Application and Network components:  <br>Applicaton: Web server, CMS, PaaS, Serverless, Microservices, Static storage, Third party services/APIs , Network and Security: Reverse proxy, IPS, WAF|


- In a blind testing, start with the assumption that there is a simple setup (a single server.)
- Then, question if there is a firewall protecting the web server.
- Is it a stateful firewall or is it an access list filter on a router?  Is it bypasseable?
- See response headers and try to identify a typical firewall response header.
- Reverse proxies might be in use, and configured as Intrusion Prevention System.
- Application- level firewall might be in use. 
- Proxy-caches can be in use.
- Is there a Load Balancer in place? F5 BIG-IP load balancers introduces some prefixed  cookies.
- Some application web servers include values in the response or rewrite URLS  automatically to do session tracking.