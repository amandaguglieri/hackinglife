---
title: Testing for SSI Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-08
---
# Testing for SSI Injection

??? quote "OWASP"
		[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.8. Testing for SSI Injection

	|ID|Link to Hackinglife|Link to OWASP|Description|
	|:---|:---|:---|:---|
	|7.8|[WSTG-INPV-08](WSTG-INPV-08.md)|[Testing for SSI Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/08-Testing_for_SSI_Injection)|- Identify SSI injection points (Presense of .shtml extension) with these characters:  < ! # = / . " - > and [a-zA-Z0-9]  - Assess the severity of the injection.|


## Server-Side Includes (SSI) Injection

SSIs are directives present on Web applications used to feed an HTML page with dynamic contents. They are similar to CGIs, except that SSIs are used to execute some actions before the current page is loaded or while the page is being visualized. In order to do so, the web server analyzes SSI before supplying the page to the user.

SSI can lead to a [Remote Command Execution (RCE)](../webexploitation/remote-code-execution-rce.md), however most webservers have the exec directive disabled by default.