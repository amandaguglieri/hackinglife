---
title: Nessus
author: amandaguglieri
draft: false
TableOfContents: true
tag: reconnaissance,scanner,vulnerabilityassessment
---

# Nessus

Nessus has a client and a server. We use the client to configure the scans and the server to actually perform the scanning processes and report back the result to the client.

## Installation

Download .deb from: https://www.tenable.com/downloads/nessus

```bash
sudo dpkg -i Nessus-10.3.0-debian9_amdb64.deb
service nessusd start
```

Now you can go to https://localhost:8834

Once installed, register in the website to generate an API key.





