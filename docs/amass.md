---
title: "Amass"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - dns enumeration
  - enumeration
  - tools
---

# Amass

In depth DNS Enumeration and network mapping.

## Install

```bash
apt install snapd
service snapd start
snap install amass
```

## Execute

```bash
snap run amass
```

## Some flags:

```
-active: Attempt zone transfer and certificate name grabs.
-bl: Blacklist of subdomain names that will not be investigated
-d: to specify a domain
-ip: Show ip addresses of cached subdomais.
–include-unresolvable: output DNS names that did not resolve.
-o file.txt: To output the result into a file
-w: path to a different wordlist file
```
