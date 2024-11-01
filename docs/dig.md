---
title: dig axfr
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---
# dig 

The `dig` command (`Domain Information Groper`) is a versatile and powerful utility for querying DNS servers and retrieving various types of DNS records. Its flexibility and detailed and customizable output make it a go-to choice. 

References:  [https://linux.die.net/man/1/dig](https://linux.die.net/man/1/dig)

See also [# Port 53 - Domain Name Server (DNS)](53-dns.md).

## Footprinting DNS with dig

```bash
# Querying: A Records for a Subdomain. Retrieves the IPv4 address (A record) associated with the domain. 
dig A www.example @$ip
 # here, $ip refers to ip of DNS server

# Retrieves the IPv6 address (AAAA record) associated with the domain.
dig AAAA www.example @$ip

# Retrieves the start of authority (SOA) record for the domain. Get email of administrator of the domain
dig SOA www.example.com
# The email will contain a (.) dot notation instead of @

# ENUMERATION
# List nameservers known for that domain. Identifies the authoritative name servers for the domain.
dig NS example.com @$ip
# -ns: other name servers are known in NS record
#  `@` character specifies the DNS server we want to query.
# here, $ip refers to ip of DNS server

# View all available records
dig ANY example.com @$ip
 # here, $ip refers to ip of DNS server. The more recent RFC8482 specified that `ANY` DNS requests be abolished. Therefore, we may not receive a response to our `ANY` request from the DNS server.

# Display version. query a DNS server's version using a class CHAOS query and type TXT. However, this entry must exist on the DNS server.
dig CH TXT version.bind $ip



# Querying: TXT Records. Retrieves any TXT records associated with the domain.
dig txt example.com @$ip

# Querying: MX Records. Finds the mail servers (MX records) responsible for the domain.
dig MX example.com @1.1.1.1

# Specifies a specific name server to query; in this case 1.1.1.1
dig @1.1.1.1 domain.com

# Querying: PTR Records for an IP Address
dig -x $ip @1.1.1.1

# Performs a reverse lookup on the IP address 192.168.1.1 to find the associated host name. You may need to specify a name server. You can also facilitate a range:
dig -x 192.168 @1.1.1.1

# Shows the full path of DNS resolution.
dig +trace domain.com

# Provides a short, concise answer to the query.
dig +short domain.com

# Displays only the answer section of the query output.
dig +noall +answer domain.com

```


### Interpretation of the output

The output can be broken down into four key sections:

- Header
- Question Section
- Answer Section
- Footer

An `opt pseudosection` can sometimes exist in a `dig` query. This is due to Extension Mechanisms for DNS (`EDNS`), which allows for additional features such as larger message sizes and DNS Security Extensions (`DNSSEC`) support.

```
######
# 1. Header
######

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16449`: 
# This line indicates the type of query (`QUERY`), the successful status (`NOERROR`), and a unique identifier (`16449`) for this specific query.

;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0`:
# This describes the flags in the DNS header:
# - `qr`: Query Response flag - indicates this is a response.
# - `rd`: Recursion Desired flag - means recursion was requested.
# - `ad`: Authentic Data flag - means the resolver considers the data authentic.
# The remaining numbers indicate the number of entries in each section of the DNS response: 1 question, 1 answer, 0 authority records, and 0 additional records.

;; WARNING: recursion requested but not available
# This indicates that recursion was requested, but the server does not support it.
     
######
# 2. Question Section
######
    
;google.com. IN A
# This line specifies the question: "What is the IPv4 address (A record) for `google.com`?"

######
# 3. Answer Section
######
    
google.com. 0 IN A 142.251.47.142
# This is the answer to the query. It indicates that the IP address associated with `google.com` is `142.251.47.142`. The '`0`' represents the `TTL` (time-to-live), indicating how long the result can be cached before being refreshed.

######
# 4. Footer
######
    
;; Query time: 0 msec`
# This shows the time it took for the query to be processed and the response to be received (0 milliseconds).
     
;; SERVER: 172.23.176.1#53(172.23.176.1) (UDP)
# This identifies the DNS server that provided the answer and the protocol used (UDP).

;; WHEN: Thu Jun 13 10:45:58 SAST 2024
# This is the timestamp of when the query was made.

;; MSG SIZE rcvd: 54
# This indicates the size of the DNS message received (54 bytes).
```


## dig axfr

dig is a DNS lookup utility but combined with "axfr" is used to do DNS zone transfer. This procedure is abbreviated `Asynchronous Full Transfer Zone` (`AXFR`), which is the protocol used during a DNS zone transfer. 

Basically, in a DNS query a client provide a human-readable hostname and the DNS server responses with an IP address. 

Quick syntax for zone transfers:

```
# This command instructs `dig` to request a full zone transfer (`axfr`) from the DNS server responsible for `actualtarget.com`. If the server is misconfigured and allows the transfer, you'll receive a complete list of DNS records for the domain, including all subdomains.
dig axfr actualtarget.com @nameserver 

# You can also solicitate the transfer of reverse DNS query
 dig axfr -x 192.168  @ip
```


### What is a DNS zone? 

DNS servers host zones. One example of a DNS zone might be example.com and all its subdomains. However secondzone.example.com can also be a separated zone. 

A zone file is a text file that describes a DNS zone with the BIND file format. In other words it is a point of delegation in the DNS tree. The BIND file format is the industry-preferred zone file format and is now well established in DNS server software. A zone file describes a zone completely. 

### Why Is DNS Zone Transfer Needed

!!! tip "Attack vector"
	Unless a DNS server is configured correctly (limiting which IPs can perform a DNS zone transfer), anyone can ask a DNS server for a copy of its zone information since DNS zone transfers do not require any authentication. In addition, the DNS service usually runs on a UDP port; however, when performing DNS zone transfer, it uses a TCP port for reliable data transmission.


DNS is a critical service. If a DNS server for a zone is not working and cached information has expired, the domain is inaccessible to all services (web, mail, and more). Therefore, each zone should have at least two DNS servers. For more critical zones, there may be even more.

However, a zone may be large and may require frequent changes. If you manually edit zone data on each server separately, it takes a lot of time and there is a a lot of potential for a mistake. This is why DNS zone transfer is needed.


You can use different mechanisms for DNS zone transfer but the simplest one is AXFR (technically speaking, AXFR refers to the protocol used during a DNS zone transfer). It is a client-initiated request. Therefore, you can edit information on the primary DNS server and then use AXFR from the secondary DNS server to download the entire zone.  

Synchronization between the servers involved is realized by zone transfer. Using a secret key `rndc-key`, which we have seen initially in the default configuration, the servers make sure that they communicate with their own master or slave. A DNS server that serves as a direct source for synchronizing a zone file is called a master. A DNS server that obtains zone data from a master is called a slave. A primary is always a master, while a secondary can be both a slave and a master. For some `Top-Level Domains` (`TLDs`), making zone files for the `Second Level Domains` accessible on at least two servers is mandatory.

Initiating an AXFR zone-transfer request from a secondary server is as simple as using the following dig commands, where zonetransfer.me is the domain that we want to initiate a zone transfer for. First, we will need to get the list of DNS servers for the domain.


```shell-session
dig axfr example.htb @$ip
```

If the administrator used a subnet for the `allow-transfer` option for testing purposes or as a workaround solution or set it to `any`, everyone would query the entire zone file at the DNS server.

> If misconfigured and left unsecured, this functionality can be abused by attackers to copy the zone file from the primary DNS server to another DNS server. A DNS Zone transfer can provide penetration testers with a holistic view of an organization's network layout. Furthermore, in certain cases, internal network addresses may be found on an organization's DNS servers.
> 

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


