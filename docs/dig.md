---
title: dig axfr
author: amandaguglieri
TableOfContents: true
draft: false
---

# dig 


## Footprinting DNS with dig

```bash
# Querying: A Records for a Subdomain
 dig a www.example @$ip
 # here, $ip refers to ip of DNS server

# Get email of administrator of the domain
dig soa www.example.com
# The email will contain a (.) dot notation instead of @

# ENUMERATION
# List nameservers known for that domain
dig ns example.com @$ip
# -ns: other name servers are known in NS record
#  `@` character specifies the DNS server we want to query.
# here, $ip refers to ip of DNS server

# View all available records
dig any example.com @$ip
 # here, $ip refers to ip of DNS server. The more recent RFC8482 specified that `ANY` DNS requests be abolished. Therefore, we may not receive a response to our `ANY` request from the DNS server.

# Display version. query a DNS server's version using a class CHAOS query and type TXT. However, this entry must exist on the DNS server.
dig CH TXT version.bind $ip

# Querying: PTR Records for an IP Address
dig -x $ip @1.1.1.1

# Querying: TXT Records
dig txt example.com @$ip

# Querying: MX Records
dig mx example.com @1.1.1.1
```


## dig axfr

dig is a DNS lookup utility but combined with "axfr" is used to do DNS zone transfer. This procedure is abbreviated `Asynchronous Full Transfer Zone` (`AXFR`), which is the protocol used during a DNS zone transfer. 

Basically, in a DNS query a client provide a human-readable hostname and the DNS server responses with an IP address. 

### What is a DNS zone? 

DNS servers host zones. One example of a DNS zone might be example.com and all its subdomains. However secondzone.example.com can also be a separated zone. 

A zone file is a text file that describes a DNS zone with the BIND file format. In other words it is a point of delegation in the DNS tree. The BIND file format is the industry-preferred zone file format and is now well established in DNS server software. A zone file describes a zone completely. 

### Why Is DNS Zone Transfer Needed

DNS is a critical service. If a DNS server for a zone is not working and cached information has expired, the domain is inaccessible to all services (web, mail, and more). Therefore, each zone should have at least two DNS servers. For more critical zones, there may be even more.

However, a zone may be large and may require frequent changes. If you manually edit zone data on each server separately, it takes a lot of time and there is a a lot of potential for a mistake. This is why DNS zone transfer is needed.

You can use different mechanisms for DNS zone transfer but the simplest one is AXFR (technically speaking, AXFR refers to the protocol used during a DNS zone transfer). It is a client-initiated request. Therefore, you can edit information on the primary DNS server and then use AXFR from the secondary DNS server to download the entire zone.

Synchronization between the servers involved is realized by zone transfer. Using a secret key `rndc-key`, which we have seen initially in the default configuration, the servers make sure that they communicate with their own master or slave. A DNS server that serves as a direct source for synchronizing a zone file is called a master. A DNS server that obtains zone data from a master is called a slave. A primary is always a master, while a secondary can be both a slave and a master. For some `Top-Level Domains` (`TLDs`), making zone files for the `Second Level Domains` accessible on at least two servers is mandatory.

Initiating an AXFR zone-transfer request from a secondary server is as simple as using the following dig commands, where zonetransfer.me is the domain that we want to initiate a zone transfer for. First, we will need to get the list of DNS servers for the domain.


```shell-session
dig axfr example.htb @$ip
```

If the administrator used a subnet for the `allow-transfer` option for testing purposes or as a workaround solution or set it to `any`, everyone would query the entire zone file at the DNS server.

## HTB machines

Some HackTheBox machines exploits DNS zone transfer:

In the example of [Friendzone machine](htb-friendzone.md), accessible web page on port 80 provides an email in which a different domain is appreciated. Also port 53 is open, which is an indicator of some possible DNS zone transfer.

In friendzone, we will transfer our zone to all zones spotted in different scanners:

```bash
# friendzone.red was spotted in the nmap scan. Transferring 10.129.228.87 zone to friendzone.red
dig axfr friendzone.red @10.129.228.87

# Also friendzoneportal.red was spotted in the email that appeared on http://10.129.228.87. Transferring 10.129.228.87 zone to friendzoneportal.red:
dig axfr friendzoneportal.red @10.129.228.87
```


