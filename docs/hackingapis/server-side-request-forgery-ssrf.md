---
title: SSRF attack - Server-side Request Forgery
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - api
---

# SSRF attack - Server side Request Forgery 

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-reconnaissance.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
    - [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](docs/hackingapis/mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)

This vulnerability allows an attacker to supply URLs that expose private data, scan the target's internal network, or compromise the target through remote code execution.

## Identify endpoints

Read your collection throughfully and search for requests that:

-   Include full URLs in the POST body or parameters
-   Include URL paths (or partial URLs) in the POST body or parameters
-   Headers that include URLs like Referer
-   Allows for user input that may result in a server retrieving resources


## SSRF types

### In-Band SSRF

A URL is specified as an attack. The request is sent and the content of your supplied URL is displayed back to you in a response.

A possible endpoint:

```
{
	"inventory":"http://store.com/api/v3/inventory/item/12345"
}
```

SSRF code:

```
{
	"inventory":"http://maliciousserver.com"
}
```


### Blind  SSRF

It's similar to In-Band attack. In this case, the response is returned and we do not have any indication that the server is vulnerable:

```
HTTP/1.1 200 OK  
headers...  
{}
```

But, there is a way to test it. Burp Suite Pro has a great tool called Burp Suite Collaborator. Collaborator can be leveraged to set up a web server that will provide us with the details of any requests that are made to our random URL.


## Tools to test Blind SSRF

Free:

- https://webhook.site
- [http://pingb.in/](http://pingb.in/) 
- [https://requestbin.com/](https://requestbin.com/) 
- [https://canarytokens.org/](https://canarytokens.org/)

Paid:

- Burp Collaborator. 