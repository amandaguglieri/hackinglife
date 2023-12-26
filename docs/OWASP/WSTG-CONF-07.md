---
title: Test HTTP Strict Transport Security - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - reconnaissance
  - WSTG-CONF-07
---



# Test HTTP Strict Transport Security

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 2. Configuration and Deploy Management Testing> 2.7. Test HTTP Strict Transport Security

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|2.7|[WSTG-CONF-07](WSTG-CONF-07.md)|[Test HTTP Strict Transport Security](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/02-Configuration_and_Deployment_Management_Testing/07-Test_HTTP_Strict_Transport_Security)|- Review the HSTS header and its validity. - Identify HSTS header on Web server through HTTP response header: curl -s -D- https://domain.com/ \| 


