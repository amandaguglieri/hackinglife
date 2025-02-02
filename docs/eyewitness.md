---
title: EyeWitness
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# EyeWitness

EyeWitness is designed to take screenshots of websites provide some server header info, and identify default credentials if known. EyeWitness is designed to run on Kali Linux.

## Installation

Download from: [https://github.com/FortyNorthSecurity/EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness).

```
sudo apt install eyewitness
```



## Basic usage

First, create a file with the target domains, like for instance, listOfdomains.txt.

Then, run:

```
eyewitness --web -f listOfdomains.txt -d path/to/save/
```

After that you will get a report.html file with the request and a screenshot of those domains. You will also have the source index.html code and the libraries in use.

### Proxing the request via BurpSuite


```
eyewitness --web -f listOfdomains.txt -d path/to/save/ --proxy-ip 127.0.0.1 --proxy-port 8080
```

