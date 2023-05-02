---
title: dnscan - A DNS subdomain scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - scanning
  - domain
  - subdomain
  - reconnaissance
  - pentesting
---

# dnscan - A DNS subdomain scanner

dnscan is a python wordlist-based DNS subdomain scanner.

The script will first try to perform a zone transfer using each of the target domain's nameservers.

If this fails, it will lookup TXT and MX records for the domain, and then perform a recursive subdomain scan using the supplied wordlist.

## Installation

**Requirements**: dnscan requires Python 3, and the netaddr (version 0.7.19 or greater) and dnspython (version 2.0.0 or greater) libraries.

```bash
git clone https://github.com/rbsec/dnscan
cd dnscan
pip install -r requirements.txt
```

## Usage

```bash
dnscan.py (-d \<domain\> | -l \<list\>) [OPTIONS]
# Mandatory Arguments
#    -d  --domain                              Target domain; OR
#    -l  --list                                Newline separated file of domains to scan
```

## Optional Arguments

    -w --wordlist <wordlist>                  Wordlist of subdomains to use
    -t --threads <threadcount>                Threads (1 - 32), default 8
    -6 --ipv6                                 Scan for IPv6 records (AAAA)
    -z --zonetransfer                         Perform zone transfer and exit
    -r --recursive                            Recursively scan subdomains
       --recurse-wildcards                    Recursively scan wildcards (slow)

    -m --maxdepth                             Maximum levels to scan recursively
    -a --alterations                          Scan for alterations of subdomains (slow)
    -R --resolver <resolver>                  Use the specified resolver instead of the system default
    -L --resolver-list <file>                 Read list of resolvers from a file
    -T --tld                                  Scan for the domain in all TLDs
    -o --output <filename>                    Output to a text file
    -i --output-ips <filename>                Output discovered IP addresses to a text file
    -n --nocheck                              Don't check nameservers before scanning. Useful in airgapped networks
    -q --quick                                Only perform the zone transfer and subdomain scans. Suppresses most file output with -o
    -N --no-ip                                Don't print IP addresses in the output
    -v --verbose                              Verbose output
    -h --help                                 Display help text

Custom insertion points can be specified by adding `%%` in the domain name, such as:

```bash
dnscan.py -d dev-%%.example.org
```
