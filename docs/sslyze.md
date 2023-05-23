---
title: sslyze - A tool for scanning certificates
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
---


# sslyze - A tool for scanning certificates

Analyze the SSL/TLS configuration of a server by connecting to it, in order to ensure that it uses strong encryption settings (certificate, cipher suites, elliptic curves, etc.), and that it is not vulnerable to known TLS attacks (Heartbleed, ROBOT, OpenSSL CCS injection, etc.).

## Installation

Preinstalled in kali.

Download it from: [https://github.com/nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze).


## Basic usage

```shell-session
sslyze --certinfo <DOMAIN>
```

In order not to have false positive regarding hostname validation, use the domain (not IP).
