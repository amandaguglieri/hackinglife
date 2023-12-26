---
title: Testing for Privilege Escalation - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-ATHZ-03
---



# Testing for Privilege Escalation

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 5. Authorization Testing > 5.3. Testing for Privilege Escalation

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|5.3|[WSTG-ATHZ-03](WSTG-ATHZ-03.md)|[Testing for Privilege Escalation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation)|- Identify injection points related to role/privilege manipulation. For example: Change some param groupid=2 to groupid=1  - Verify that it is not possible for a user to modify their privileges or roles inside the application  - Fuzz or otherwise attempt to bypass security measures.|
