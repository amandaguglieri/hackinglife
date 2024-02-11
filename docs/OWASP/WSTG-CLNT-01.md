---
title: Testing for DOM-Based Cross Site Scripting - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-CLNT-01
---



# Testing for DOM-Based Cross Site Scripting

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 11. Client Side Testing > 11.1. Testing for DOM-Based Cross Site Scripting

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|11.1|[WSTG-CLNT-01](WSTG-CLNT-01.md)|[Testing for DOM-Based Cross Site Scripting](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting)|- Identify DOM sinks.  - Build payloads that pertain to every sink type. |



The key in exploiting this XSS flaw is that the client-side script code can access the browser's DOM, thus all the information available in it. Examples of this information are the URL, history, cookies, local storage,...  Technically there are two keywords: sources and sinks. Let's use the following vulnerable code:

## Causes

This vulnerable code in a welcome page may lead to a DOM XSS attack:
http://example.com/#w!Giuseppe

```html
<h1 id='welcome'></h1>
<script>
	var w = "Welcome";
	var name = document.location.hash.search(/#W!1)+3,
				document.location.hash.length
				);
	document.getElementById('Welcome').innerHTML = w + name;
</script>
```


>location.hash is the source of the untrusted input.
>.innerHTML is the sink where the input is used.


To deliver a DOM-based XSS attack, you need to place data into a source so that it is propagated to a sink and causes execution of arbitrary JavaScript.
The most common source for DOM XSS is the URL, which is typically accessed with the `window.location` object.

What is a sink? A sink is a potentially dangerous JavaScript function or DOM object that can cause undesirable effects if attacker-controlled data is passed to it. For example, the `eval()` function is a sink because it processes the argument that is passed to it as JavaScript. An example of an HTML sink is `document.body.innerHTML` because it potentially allows an attacker to inject malicious HTML and execute arbitrary JavaScript.

Summing up: you should avoid allowing data from any untrusted source to be dynamically written to the HTML document.


Which sinks can lead to DOM-XSS vulnerabilities:

- document.write()
- document.writeln() 
- document.replace()
- document.domain 
- element.innerHTML 
- element.outerHTML 
- element.insertAdjacentHTML 
- element.onevent

This project, [DOMXSS wiki](https://code.google.com/archive/p/domxsswiki/) aims to identify sources and sinks methods exposed by public, widely used javascript frameworks.



## Attack techniques

Go to my [XSS cheat sheet](../webexploitation/cross-site-scripting-xss.md)