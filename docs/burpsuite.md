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

