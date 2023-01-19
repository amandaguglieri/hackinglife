---
title: moodlescan
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, web pentesting, cms
---


**my eval**: I'm not sure about how accurate it is. I was working on the [Goldeneye1 machine from vulnhub](vulnhub-goldeneye-1.md) and moodlescan identied the moodle version as 2.2.2 when in reality is 2.2.3.  


## Installation

Requirements: Install Python 3 and Install the package python3-pip

```bash
git clone https://github.com/inc0d3/moodlescan
cd moodlescan
pip install -r requirements.txt
```

## Basic commands


```bash

python moodlescan.py -u [URL]


#Options
#		-u [URL] 	: URL with the target, the moodle to scan
#		-a 		: Update the database of vulnerabilities to latest version
#		-r 		: Enable HTTP requests with random user-agent
#		-k 		: Ignore SSL Certificate
#		Proxy configuration
#
#		-p [URL]	: URL of proxy server (http)
#		-b [user]	: User for authenticate to proxy server
#		-c [password]	: Password for authenticate to proxt server
#		-d [protocol]  : Protocol of authentication: basic or ntlm

```


