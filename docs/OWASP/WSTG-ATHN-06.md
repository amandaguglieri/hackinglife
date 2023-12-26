---
title: Testing for Browser Cache Weaknesses - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-ATHN-06
---



# Testing for Browser Cache Weaknesses

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 4. Authentication Testing > 4.6. Testing for Browser Cache Weaknesses

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|4.6|[WSTG-ATHN-06](WSTG-ATHN-06.md)|[Testing for Browser Cache Weaknesses](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses)|- Review if the application stores sensitive information on the client-side.  - Review if access can occur without authorization.  - Check browser history issue by clicking "Back" button after logging out.  - Check browser cache issue from HTTP response headers (Cache-Control: nocache)|



