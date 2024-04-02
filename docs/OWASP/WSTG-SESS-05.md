---
title: Testing for Cross Site Request Forgery - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-SESS-05
---
# Testing for Cross Site Request Forgery

??? quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 6. Session Management Testing > 6.5. Testing for Cross Site Request Forgery

	| ID  | Link to Hackinglife             | Link to OWASP                                                                                                                                                                                                        | Description                                                                                                                                                                           |
	| :-- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
	| 6.5 | [WSTG-SESS-05](WSTG-SESS-05.md) | [Testing for Cross Site Request Forgery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/05-Testing_for_Cross_Site_Request_Forgery) | - Determine whether it is possible to initiate requests on a user's behalf that are not initiated by the user.  - Conduct URL analysis, Direct access to functions without any token. |

Cross Site Request Forgery (CSRF) is a type of web security vulnerability that occurs when an attacker tricks a user into performing actions on a web application without their knowledge or consent. A successful CSRF exploit can compromise end user data and operation when it targets a normal user. If the targeted end user is the administrator account, a CSRF attack can compromise the entire web application.

## See my notes

- [CSRF attack - Cross Site Request Forgery](../webexploitation/cross-site-request-forgery-csrf.md)
