---
title: Burpsuite
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - proxy
  - burpsuite
  - tools
---

# Burpsuite

Burp Suite is a Man-in-the-middle (MITM) proxy loaded with valuable tools to help pentesters.

Related issues:

[Setting up Postman with BurpSuite](proxies.md)

Burp Suite has two editions:

- **Community Edition** - Provides you with everything you need to get started and is designed for students or professionals looking to learn more about AppSec. Features include:
		■ HTTP(s) Proxy.
		■ Modules - Repeater, Decoder, Sequencer & Comparer.
		■ Lite version of the Intruder module (Performance Throttling).
- **Professional Edition** - Faster, more reliable offering designed for penetration testers and security professionals. Features include everything in the community edition plus:
		■ Project files.
		■ No performance throttling.
		■ Intruder - Fully featured module.
		■ Custom PortSwigger payloads.
		■ Automatic scanner and crawler.


Accessing older releases: [https://portswigger.net/burp/releases/archive](https://portswigger.net/burp/releases/archive).



## Runtime environments

### Jython: python environment

Download from: https://www.jython.org/download.html


###  JRuby: ruby environment

Download from:  https://www.jruby.org/download


## Removing the captive portal from captured traffic

A [captive portal](https://en.wikipedia.org/wiki/Captive_portal) is a web page that serves as a sort of gateway page when attempting to browse the Internet. It is often displayed when accepting a user agreement or authenticating through a browser to a Wi-Fi network.

To ignore this, simply enter about:config in the address bar. Firefox will present a warning, but we can proceed by clicking I accept the risk!.

Finally, search for "network.captive-portal-service.enabled" and double-click it to change the value to "false". This will prevent these messages from appearing in the proxy history.


## Extensions that make your life better

### Autorize 

Autorize is an extension aimed at helping the penetration tester to detect authorization vulnerabilities, one of the more time-consuming tasks in a web application penetration test.

It is sufficient to give to the extension the cookies of a low privileged user and navigate the website with a high privileged user. The extension automatically repeats every request with the session of the low privileged user and detects authorization vulnerabilities.

It is also possible to repeat every request without any cookies in order to detect authentication vulnerabilities in addition to authorization ones.

The plugin works without any configuration, but is also highly customizable, allowing configuration of the granularity of the authorization enforcement conditions and also which requests the plugin must test and which not. It is possible to save the state of the plugin and to export a report of the authorization tests in HTML or in CSV.

The reported enforcement statuses are the following:

1.  Bypassed! - Red color
2.  Enforced! - Green color
3.  Is enforced??? (please configure enforcement detector) - Yellow color

### Param Miner

In Burp Suite, you can use the Param Miner extension's "Guess headers" function to automatically probe for supported headers using its extensive built-in wordlist.


### Turbo intruder

### CMS Scanner

### WAF Detect

### Bypass WAF

### Waf Cookie Fetcher

### PDF Viewer

### Wayback machine

### Software Vulnerability Scanner

### PHP Object Injection Slinger

[https://github.com/portswigger/poi-slinger](https://github.com/portswigger/poi-slinger)

This is an extension for Burp Suite Professional, designed to help you scan for PHP Object Injection vulnerabilities on popular PHP Frameworks and some of their dependencies. It will send a serialized PHP Object to the web application designed to force the web server to perform a DNS lookup to a Burp Collaborator Callback Host.

The payloads for this extension are all from the excellent Ambionics project PHPGGC. PHPGGC is a library of PHP unserialize() payloads along with a tool to generate them, from command line or programmatically. You will need it for further exploiting any vulnerabilities found by this extension.

You should combine your testing with the PHP Object Injection Check extension from Securify so you can identify other possible PHP Object Injection issues that this extension does not pick up.

To use the extension, on the Proxy/Target/Intruder/Repeater Tab, right click on the desired HTTP Request and click Send To POI Slinger. This will also highlight the HTTP Request and set the comment Sent to POI Slinger You can watch the debug messages on the extension's output pane under Extender->Extensions->PHP Object Injection Slinger.

### JWT Editor

[https://github.com/portswigger/jwt-editor](https://github.com/portswigger/jwt-editor)

JWT Editor is a Burp Suite extension for editing, signing, verifying, encrypting and decrypting JSON Web Tokens (JWTs).

It provides automatic detection and in-line editing of JWTs within HTTP requests/responses and web socket messages, signing and encrypting of tokens and automation of several well-known attacks against JWT implementations.

It was written originally by Fraser Winterborn, formerly of BlackBerry Security Research Group. The original source code can be found [here](https://github.com/blackberry/jwt-editor).

For further information, check out the repository [here](https://github.com/PortSwigger/jwt-editor).

### Java Deserialization Scanner

[https://github.com/portswigger/java-deserialization-scanner](https://github.com/portswigger/java-deserialization-scanner)

This extension gives Burp Suite the ability to find Java deserialization vulnerabilities.

It adds checks to both the active and passive scanner and can also be used in an "Intruder like" manual mode, with a dedicated tab.

The extension allows the user to _discover and exploit_ Java Deserialization Vulnerabilities with different encodings (Raw, Base64, Ascii Hex, GZIP, Base64 GZIP) when the following libraries are loaded in the target JVM:

- Apache Commons Collections 3 (up to 3.2.1), with five different chains
- Apache Commons Collections 4 (up to 4.4.0), with two different chains
- Spring (up to 4.2.2)
- Java 6 and Java 7 (up to Jdk7u21) without any weak library
- Hibernate 5
- JSON
- Rome
- Java 8 (up to Jdk8u20) without any weak library
- Apache Commons BeanUtils
- Javassist/Weld
- JBoss Interceptors
- Mozilla Rhino (two different chains)
- Vaadin

Furthermore, URLSNDS payload has been introduced to actively detect Java deserialization on the backend without any vulnerable library. This check does the same job as the CPU attack vector already present in the "Manual testing" section but can be safely added to the Burp Suite Active Scanner engine, while the CPU payload should be use with caution.

After that a Java deserialization vulnerability has been found, a dedicated exploitation tab offers a comfortable interface to exploit deserialization vulnerabilities using frohoff ysoserial [https://github.com/frohoff/ysoserial](https://github.com/frohoff/ysoserial)

Mini walkthrough: [https://techblog.mediaservice.net/2017/05/reliable-discovery-and-exploitation-of-java-deserialization-vulnerabilities/](https://techblog.mediaservice.net/2017/05/reliable-discovery-and-exploitation-of-java-deserialization-vulnerabilities/)