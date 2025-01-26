---
title: Testing for Command Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-12
---
# Testing for command injection

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.12. Testing for Command Injection

	| ID   | Link to Hackinglife             | Link to OWASP                                                                                                                                                                                    | Description                                                                                                                                 |
	| :--- | :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
	| 7.12 | [WSTG-INPV-12](WSTG-INPV-12.md) | [Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection) | - Identify and assess the command injection points with special characters (i.e.: \| ; & $ > < ' !)  For example: ?doc=Doc1.pdf+\|+Dir c:\| |


Command injection vulnerabilities in the context of web application penetration testing occur when an attacker can manipulate the input fields of a web application in a way that allows them to execute arbitrary operating system commands on the underlying server. This type of vulnerability is a serious security risk because it can lead to unauthorized access, data theft, and full compromise of the web server.

[See my notes on Command injection](../webexploitation/command-injection.md)

