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

## Detect injection points

Have an extensive template expression payloads. Common examples:

```
a{{7*7}}
a{{bar}}b
```

```
$ curl -g 'http://www.target.com/page?name={{7*7}}'
Hello 49!
```

## Identify the templating engine

After detecting template injection, the next step is to identify the template engine in use.

!!! quote "Burpsuite article"
	[https://portswigger.net/research/server-side-template-injection#Identify](https://portswigger.net/research/server-side-template-injection#Identify)

Green and red arrows represent 'success' and 'failure' responses respectively. In some cases, a single payload can have multiple distinct success responses - for example, the probe {{7*'7'}} would result in 49 in Twig, 7777777 in Jinja2, and neither if no template language is in use.

![SSTI](../img/ssti_01.png)

## Exploitation

!!! quote "Burpsuite article"
	[https://portswigger.net/research/server-side-template-injection#exploit](https://portswigger.net/research/server-side-template-injection#exploit)


## Tools

- [Tplmap](https://github.com/epinna/tplmap)
- [Backslash Powered Scanner Burp Suite extension](https://github.com/PortSwigger/backslash-powered-scanner)
- [Template expression test strings/payloads list](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)


## Related lab

[HackTheBox: Nunchunks](../htb-nunchucks.md): Express server with a nunjucks template engine.

