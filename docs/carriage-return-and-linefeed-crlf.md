---
title: Carriage Return and Linefeed - CRLF Attack
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, webpentesting
---

**Source**: [Owasp description: https://owasp.org/www-community/vulnerabilities/CRLF_Injection](https://owasp.org/www-community/vulnerabilities/CRLF_Injection).

## Description

A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL. CRLF is the acronym used to refer to Carriage Return (\r) Line Feed (\n). As one might notice from the symbols in the brackets, “Carriage Return” refers to the end of a line, and “Line Feed” refers to the new line.

The term CRLF refers to Carriage Return (ASCII 13, \r) Line Feed (ASCII 10, \n). They’re used to note the termination of a line, however, dealt with differently in today’s popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. In the HTTP protocol, the CR-LF sequence is always used to terminate a line.


## Tools and payloads 

- See updated chart: [Attacks and tools for web pentesting](index-attacks-tools-web-pentesting.md).

