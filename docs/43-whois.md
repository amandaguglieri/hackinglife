---
title: Port 43 - whois
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - port 111
  - rpc
  - NFS
  - Network File System
---

# Port 43 - whois

It is a TCP-based transaction-oriented query/response protocol listening on TCP port 43 by default. We can use it for querying databases containing domain names, IP addresses, or autonomous systems and provide information services to Internet users.

The [Internet Corporation of Assigned Names and Numbers](https://www.icann.org/get-started) (`ICANN`) requires that accredited registrars enter the holder's contact information, the domain's creation, and expiration dates, and other information in the Whois database immediately after registering a domain. In simple terms, the Whois database is a searchable list of all domains currently registered worldwide.

[Sysinternals WHOIS](https://docs.microsoft.com/en-gb/sysinternals/downloads/whois) for Windows or Linux [WHOIS](https://linux.die.net/man/1/whois) command-line utility are our preferred tools for gathering information. However, there are some online versions like [whois.domaintools.com](https://whois.domaintools.com) we can also use.

```bash
# Retrieve the registration details
whois $TARGET

# Reverse lookup
whois example.com -h $ipTarget
```

```powershell
# windows
whois.exe $TARGET
```