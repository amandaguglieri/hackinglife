---
title: adidnsdump - A tool for enumerating DNS records in Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
---

# adidnsdump - A tool for enumerating DNS records in Active Directory

By default any user in Active Directory can enumerate all DNS records in the Domain or Forest DNS zones, similar to a zone transfer. This tool enables enumeration and exporting of all DNS records in the zone for recon purposes of internal networks.

## Installation

The tool requires `impacket` and `dnspython` to function. While the tool works with both Python 2 and 3, Python 3 support requires you to install [impacket from GitHub](https://github.com/CoreSecurity/impacket).

```bash
git clone https://github.com/dirkjanm/adidnsdump
cd adidnsdump
pip install .
```

## Basic commands

Installation adds the `adidnsdump` command to your `PATH`. For help, try `adidnsdump -h`. The tool can be used both directly from the network and via an implant using proxychains. If using proxychains, make sure to specify the `--dns-tcp` option.

```bash
adidnsdump -u $domain\\$user ldap://$DomainControllerIP
# Example:
# adidnsdump -u inlanefreight\\forend ldap://172.16.5.5 
```