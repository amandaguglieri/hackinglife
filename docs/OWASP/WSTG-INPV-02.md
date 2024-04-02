---
title: Testing for Stored Cross Site Scripting - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-02
---



# Testing for Stored Cross Site Scripting

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.2. Testing for Stored Cross Site Scripting

	|ID|Link to Hackinglife|Link to OWASP|Description|
	|:---|:---|:---|:---|
	|7.2|[WSTG-INPV-02](WSTG-INPV-02.md)|[Testing for Stored Cross Site Scripting](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting)|- Identify stored input that is reflected on the client-side.  - Assess the input they accept and the encoding that gets applied on return (if any).|



Stored cross-site scripting is a vulnerability where an attacker is able to inject Javascript code into a web application’s database or source code via an input that is not sanitized. For example, if an attacker is able to inject a malicious XSS payload in to a webpage on a website without proper sanitization, the XSS payload injected in to the webpage will be  executed by the browser of anyone that visits that webpage.


## Causes

This vulnerable PHP code in a welcome page may lead to a stored XSS attack:

```php
<?php 
$file  = 'newcomers.log';
if(@$_GET['name']){
	$current = file_get_contents($file);
	$current .= $_GET['name']."\n";
	//store the newcomer
	file_put_contents($file, $current);
}
//If admin show newcomers
if(@$_GET['admin']==1)
	echo file_get_contents($file);
?>

Welcome <?=$name?>
```


## Attack techniques

Go to my [XSS cheat sheet](../webexploitation/cross-site-scripting-xss.md)