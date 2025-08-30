---
title: nslookup
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---


# nslookup

With `Nslookup`, we can search for domain name servers on the Internet and ask them for information about hosts and domains.

```bash
# Query `A` records by submitting a domain name: default behaviour
nslookup $TARGET

# We can use the `-query` parameter to search specific resource records
# Querying: A Records for a Subdomain
nslookup -query=A example.com

# Querying: PTR Records for an IP Address
nslookup -query=PTR 31.13.92.36

# Querying: ANY Existing Records
nslookup -query=ANY example.com

# Querying: TXT Records
nslookup -query=TXT example.com

# Querying: MX Records
nslookup -query=MX example.com

#  Specify a nameserver if needed by adding `@<nameserver/IP>` to the command


# Query `A` records by submitting a domain name: default behaviour
nslookup -type=txt example.com $ip

```


References:  
- nslookup (https://linux.die.net/man/1/nslookup)  