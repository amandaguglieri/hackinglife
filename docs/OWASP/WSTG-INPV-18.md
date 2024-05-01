---
title: Testing for Server-side Template Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-18
---
# Testing for Server-side Template Injection

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.18. Testing for Server-side Template Injection

    |ID|Link to Hackinglife|Link to OWASP|Description|
    |:---|:---|:---|:---|
    |7.18|[WSTG-INPV-18](WSTG-INPV-18.md)|[Testing for Server-side Template Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server-side_Template_Injection)|- Detect template injection vulnerability points. - Identify the templating engine.  - Build the exploit.|

[Server-side Template Injection in HackingLife](../webexploitation/server-side-template-injection-ssti.md)

Web applications commonly use server-side templating technologies (Jinja2, Twig, FreeMaker, etc.) to generate dynamic HTML responses. Server-side Template Injection vulnerabilities (SSTI) occur when user input is embedded in a template in an unsafe manner and results in remote code execution on the server. Any features that support advanced user-supplied markup may be vulnerable to SSTI.

## See my notes

- [Server Side Template Injections](../webexploitation/server-side-template-injection-ssti.md): What is it. How this attack works. Attack classification. Types of databases. Payloads. Dictionaries.