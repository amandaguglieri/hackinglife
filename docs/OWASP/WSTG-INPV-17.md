---
title: Testing for Host Header Injection - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - WSTG-INPV-17
---

# Testing for Host Header Injection

!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 7. Data Validation Testing > 7.17. Testing for Host Header Injection

|ID|Link to Hackinglife|Link to OWASP|Description|
|:---|:---|:---|:---|
|7.17|[WSTG-INPV-17](WSTG-INPV-17.md)|[Testing for Host Header Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection)|- Assess if the Host header is being parsed dynamically in the application.  - Bypass security controls that rely on the header.|


The goal:

- Assess if the Host header is being parsed dynamically in the application.
- Bypass security controls that rely on the header.

Source: [https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html)

## Supply an arbitrary Host header

Some intercepting proxies derive the target IP address from the Host header directly, which makes this kind of testing all but impossible; any changes you made to the header would just cause the request to be sent to a completely different IP address. However, Burp Suite accurately maintains the separation between the Host header and the target IP address. 

In Burpsuite, set the target to www.example.com. Then, send your request with modified Host header:


```
GET / HTTP/1.1
Host: www.attacker.com
```

The front-end server or load balancer that received your request may simply not know where to forward it, resulting in an "Invalid Host header" error of some kind. This is especially likely if your target is accessed via a CDN.



## Inject host override headers

### X-Forwarded Host Header Bypass


```
GET / HTTP/1.1
Host: www.example.com
X-Forwarded-Host: www.attacker.com
```

Potentially producing client-side output such as:

```
<link src="http://www.attacker.com/link" />
```

### More headers bypassing

Although `X-Forwarded-Host` is the de facto standard for this behavior, you may come across other headers that serve a similar purpose, including:

- `X-Host`
- `X-Forwarded-Server`
- `X-HTTP-Host-Override`
- `Forwarded`

In Burp Suite, you can use thec's "Guess headers" function to automatically probe for supported headers using its extensive built-in wordlist.



## Injecting multiple Host headers

```
GET / HTTP/1.1
Host: www.example.com
Host: www.attacker.com
```

##  HTTP_HOST vs. SERVER_NAME Routing 

By supplying an absolute URL.

```
POST https://example.com/passwordreset HTTP/1.1
Host: www.evil.com
```

## Port-based attack 

Webservers allow a port to be specified in the Host header, but ignore it for the purpose of deciding which virtual host to pass the request to. This is simple to exploit using the ever-useful http://username:password@domain.com syntax:

```
POST /user/passwrordeset HTTP/1.1
Host: example.com:@attacker.net
```

This may result in a suspicious password reset link. By clicking it, the victim's browser will  send the key to attacker.net before creating the suspicious URL popup.

## Persistent XSS via Host header injection

```
GET /index.html HTTP/1.1
Host: cow\"onerror='alert(1)'rel='stylesheet'" http://example.com/ | fgrep cow\
```

The response should show a poisoned `<link>` element:

```
<link href="http://cow"onerror='alert(1)'rel='stylesheet'/" rel="canonical"/>
```


## Add line wrapping

The website may block requests with multiple Host headers, but you may be able to bypass this validation by indenting one of them like this. Some servers will interpret the indented header as a wrapped line and, therefore, treat it as part of the preceding header's value. Other servers will ignore the indented header altogether.

```
GET /example HTTP/1.1 
    Host: attacker.com 
Host: example.com
```


## Exploitation

[https://portswigger.net/web-security/host-header/exploiting](https://portswigger.net/web-security/host-header/exploiting)