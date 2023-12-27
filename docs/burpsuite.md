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

