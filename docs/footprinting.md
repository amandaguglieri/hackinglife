---
title: 01. Information Gathering   /  Footprinting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - footprinting
  - CPTS
---

# 01. Information Gathering   /  Footprinting

## Methodology

| **Layer** | **Description** | **Information Categories** |
| --- | --- | --- |
| 1. Internet Presence | Identification of internet presence and externally accessible infrastructure.|Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures |
| 2. Gateway | Identify the possible security measures to protect the company's external and internal infrastructure.|Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare|
| 3. Accessible Services | Identify accessible interfaces and services that are hosted externally or internally.|Service Type, Functionality, Configuration, Port, Version, Interface|
| 4. Processes | Identify the internal processes, sources, and destinations associated with the services.|PID, Processed Data, Tasks, Source, Destination|
| 5. Privileges | Identification of the internal permissions and privileges to the accessible services.|Groups, Users, Permissions, Restrictions, Environment|
| 6. OS Setup | Identification of the internal components and systems setup.|OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files|


## OWASP reference


|ID|WSTG-ID|Test Name|Objectives|Tools|
|:---|:---|:---|:---|:---|
|1.1|WSTG-INFO-01|[Conduct Search Engine Discovery Reconnaissance for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/01-Conduct_Search_Engine_Discovery_Reconnaissance_for_Information_Leakage)|- Identify what sensitive design and configuration information of the application, system, or organization is exposed directly (on the organization's website) or indirectly (via third-party services).|Google Hacking  <br>Shodan  <br>Recon-ng|
|1.2|WSTG-INFO-02|[Fingerprint Web Server](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)|- Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.|Wappalyzer  <br>Nikto|
|1.3|WSTG-INFO-03|[Review Webserver Metafiles for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage)|- Identify hidden or obfuscated paths and functionality through the analysis of metadata files (robots.txt, <META> tag, sitemap.xml)  <br>- Extract and map other information that could lead to a better understanding of the systems at hand.|Browser  <br>Curl  <br>Burpsuite/ZAP|
|1.4|WSTG-INFO-04|[Enumerate Applications on Webserver](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/04-Enumerate_Applications_on_Webserver)|- Enumerate the applications within the scope that exist on a web server.  <br>- Find applications hosted in the webserver (Virtual hosts/Subdomain), non-standard ports, DNS zone transfers|dnsrecon  <br>Nmap|
|1.5|WSTG-INFO-05|[Review Webpage Content for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Webpage_Content_for_Information_Leakage)|- Review webpage comments, metadata, and redirect bodies to find any information leakage.  <br>- Gather JavaScript files and review the JS code to better understand the application and to find any information leakage.  <br>- Identify if source map files or other front-end debug files exist.|Browser  <br>Curl  <br>Burpsuite/ZAP|
|1.6|WSTG-INFO-06|[Identify Application Entry Points](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/06-Identify_Application_Entry_Points)|- Identify possible entry and injection points through request and response analysis which covers hidden fields, parameters, methods HTTP header analysis|OWASP ASD  <br>Burpsuite/ZAP|
|1.7|WSTG-INFO-07|[Map Execution Paths Through Application](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/07-Map_Execution_Paths_Through_Application)|- Map the target application and understand the principal workflows.  <br>- Use HTTP(s) Proxy Spider/Crawler feature aligned with application walkthrough|Burpsuite/ZAP|
|1.8|WSTG-INFO-08|[Fingerprint Web Application Framework](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/08-Fingerprint_Web_Application_Framework)|- Fingerprint the components being used by the web applications.  <br>- Find the type of web application framework/CMS from HTTP headers, Cookies, Source code, Specific files and folders, Error message.|Whatweb  <br>Wappalyzer  <br>CMSMap|
|1.9|WSTG-INFO-09|[Fingerprint Web Application](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/09-Fingerprint_Web_Application)|N/A, This content has been merged into: WSTG-INFO-08|NA|
|1.10|WSTG-INFO-10|[Map Application Architecture](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/10-Map_Application_Architecture)|- Understand the architecture of the application and the technologies in use.  <br>- Identify application architecture whether on Application and Network components:  <br>Applicaton: Web server, CMS, PaaS, Serverless, Microservices, Static storage, Third party services/APIs  <br>Network and Security: Reverse proxy, IPS, WAF|WAFW00F  <br>Nmap|
