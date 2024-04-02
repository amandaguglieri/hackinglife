---
title: Testing for Reflected Cross Site Scripting - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-01
---



# Testing for Reflected Cross Site Scripting

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.1. Testing for Reflected Cross Site Scripting

	|ID|Link to Hackinglife|Link to OWASP|Description|
	|:---|:---|:---|:---|
	|7.1|[WSTG-INPV-01](WSTG-INPV-01.md)|[Testing for Reflected Cross Site Scripting](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting)|- Identify variables that are reflected in responses.  - Assess the input they accept and the encoding that gets applied on return (if any).|


Reflected Cross-site Scripting (XSS) occur when an attacker injects browser executable code within a single HTTP response. The injected attack is not stored within the application itself; it is non-persistent and only impacts users who open a maliciously crafted link or third-party web page. When a web application is vulnerable to this type of attack, it will pass unvalidated input sent through requests back to the client.

[XSS Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)

## Causes

This vulnerable PHP code in a welcome page may lead to an XSS attack:

```php
<?php $name = @$_GET['name']; ?>

Welcome <?=$name?>

```


## Attack techniques

Go to my [XSS cheat sheet](../webexploitation/cross-site-scripting-xss.md)