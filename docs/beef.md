---
title: BeEF - The browser exploitation framework project
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - phishing
  - tools
---

# BeEF - The browser exploitation framework project

**BeEF** is short for **The Browser Exploitation Framework**. It is a penetration testing tool that focuses on the web browser.


## Installation

Repository: [https://github.com/beefproject/beef](https://github.com/beefproject/beef)


```bash
git clone https://github.com/beefproject/beef`
```


## Usage

Basically it allows you to create a hook in the persistent or storage script injection. BeEF provides a pannel to see the connections to your hook. If eventually admin connect to the website, you may gain permission to the server.


## Basic commands

```
Social engineering 
Open webcams 
Alert messages
Run javascript
Get screenshots of what the person has on their screen
Redirect Browser
Create Fake authentication dialog box (facebooks...)
.......

```


## Attacks 

### Tunneling proxy

See [XSS attacks](webexploitation/cross-site-scripting-xss.md).

An alternative to stealing protected cookies is to use the victim browser as a proxy. The Tunneling Proxy in BeEF exploits the XSS flaw and uses the victim browser to perform requests as the victim user to the web application. Basically, it tunnels requests through the hooked browser. By doing so, there is no way for the web application to distinguish between requests coming from legitimate user and requests forged by an atacker. 
BeEF allows you to bypass other web developer protection techniques such as using multiple validations (User-agent, custom headers,...)

### Event logger

The event logger allows us to capture keystrokes, acting as a keylogger.