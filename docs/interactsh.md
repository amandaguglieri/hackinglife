---
title: Interactsh - An alternative to BurpSuite Collaborator
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - proxy
  - servers
  - burpsuite
  - tools
---


# Interactsh - An alternative to BurpSuite Collaborator

**Interactsh** is an open-source tool for detecting out-of-band interactions. It is a tool designed to detect vulnerabilities that cause external interactions.

Website version: [https://app.interactsh.com/](https://app.interactsh.com)
## Installation

Download from: [https://github.com/projectdiscovery/interactsh/](https://github.com/projectdiscovery/interactsh/)

```bash
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
```

## Basic Usage

```bash
interactsh-client   
```

Cry for help:

```bash
interactsh-client  -h
```

Interactsh server runs multiple services and captures all the incoming requests. To host an instance of **interactsh-server**, you are required to setup:

1. Domain name with custom **host names** and **nameservers**.
2. Basic droplet running 24/7 in the background.

### Burpsuite integrated

[interactsh-collaborator](https://github.com/wdahlenburg/interactsh-collaborator) is Burp Suite extension developed and maintained by [@wdahlenb](https://twitter.com/wdahlenb)

