---
title: Testing for Insecure Direct Object References - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-ATHZ-04
---



# Testing for Insecure Direct Object References

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 5. Authorization Testing > 5.4. Testing for Insecure Direct Object References

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|5.4|[WSTG-ATHZ-04](WSTG-ATHZ-04.md)|[Testing for Insecure Direct Object References](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References)|- Identify points where object references may occur.  - Assess the access control measures and if they're vulnerable to IDOR. For example: Force changing parameter value (?invoice=123 -> ?invoice=456)|
