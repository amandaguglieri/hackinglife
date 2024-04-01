---
title: Testing for SQL Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-05
---



# Testing for SQL Injection

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.5. Testing for SQL Injection

| ID  | Link to Hackinglife             | Link to OWASP                                                                                                                                                                            | Description                                                                                                                       |
| :-- | :------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| 7.5 | [WSTG-INPV-05](WSTG-INPV-05.md) | [Testing for SQL Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection) | - Identify SQL injection points.  - Assess the severity of the injection and the level of access that can be achieved through it. |

SQL injection testing checks if it is possible to inject data into an application/site so that it executes a user-controlled SQL query in the database. Testers find a SQL injection vulnerability if the application uses user input to create SQL queries without proper input validation. 

## See my notes

- [SQL injection](../webexploitation/sql-injection.md): What is it. How this attack works. Attack classification. Types of databases. Payloads. Dictionaries.
- [NoSQL injection](../webexploitation/nosql-injection.md): What is it. Typical payloads.
- [Manual attack](../sqli-manual-attack.md).

