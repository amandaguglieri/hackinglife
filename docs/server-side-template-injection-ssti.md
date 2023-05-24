---
title: Server-side Template Injection - SSTI
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---

# Server-side Template Injection (SSTI)

Source: [https://portswigger.net/research/server-side-template-injection](https://portswigger.net/research/server-side-template-injection)

Web applications frequently use template systems to embed dynamic content in web pages and emails. 

Example:

```
custom_email={{self}}
```

What we have here is essentially server-side code execution inside a sandbox. See for instance this entrudet performed on Burpsuite Repeater module with server-side template payloads:

![Example](img/nunchucks_1.png)

This vulnerability typically arises through developers intentionally letting users submit or edit templates. Template injection can also arise by accident, when user input is simply concatenated directly into a template. This may seem slightly counter-intuitive, but it is equivalent to SQL Injection vulnerabilities occurring in poorly written prepared statements. The 'Server-Side' qualifier is used to distinguish this from vulnerabilities in client-side templating libraries such as those provided by jQuery and KnockoutJS.


## Detection

To detect it, we need to invoke the template engine by embedding a statement (or payload).

Payloads

## Identify 

Payloads for SSTI  exploitation depend entirely on programming language and template engine in use. We need to extract that information. 


## Labs

[HackTheBox: Nunchunks](htb-nunchucks.md): Express server with a nunjucks template engine.


