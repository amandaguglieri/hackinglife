---
title: eJPT
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting 
---

# eJPT


## Subdomain enumeration

| Tool + Cheat sheet | What it does |
| ---- | ----------- |
| [Google dorks](google-dorks.md) | Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. |
| [Sublist3r](sublist3r.md) | Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS.   |
| [crt.sh](ctr.md) | It collects information about SSL certificates. If you visit a domain and it contains a certificate you can extract other subdomain by using the View Certificate functionality. |
| [dnscan](dnscan.md) | Python wordlist-based DNS subdomain scanner. |
| [amass](amass.md) | In depth DNS Enumeration and network mapping.  |



## Footprinting & Scanning

| Tool + Cheat sheet | What it does |
| ---- | ----------- |
| [ping](ping.md) | ping works by sending one or more special ICMP packets (Type 8 - echo request) to a host. If the destination host replies with ICMP echo reply packets, then the host is alive. |
| [fping](fping.md) | Linux tool which is an improved version of the ping utility. |
| [nmap](nmap.md) | Network Mapper is an open source tool for network exploration and security auditing. Free and open-source scanner created by Gordon Lyon. Nmap is used to discover hosts and services on a computer network by sending packages and analyzing the responses.|
| [p0f](p0f) | P0f is a tool that utilizes an array of sophisticated, purely passive traffic fingerprinting mechanisms to identify the players behind any incidental TCP/IP communications (often as little as a single normal SYN) without interfering in any way. |
| [masscan](masscan.md) |  Masscan was designed to deal with large networks and to scan thousands of Ip addresses at once. It’s faster than nmap but probably less accurate. |


## Enumeration tools 

|  Tool + Cheat sheet | URL | 
| ------------------ | --- |
| [dirb](dirb.md) | DIRB is a **web content** fingerprinting tool. It scans the web server for directories using a dictionary file | 
| [feroxbuster](feroxbuster.md) | FEROXBUSTER is a **web content** fingerprintinf tool that uses brute force combined with a wordlist to search for unlinked content in target directories. |
| [httprint](httprint.md) | HTTPRINT is a **web server** fingerprinting tool. It identifies web servers and detects web enabled devices which do not have a server banner string, such as wireless access points, routers, switches, cable modems, etc. | 
| [wpscan](wpscan.md) | WPSCAN is a **wordpress** security scanner. | 

## Dictionaries

[List of dictionaries](dictionaries.md).


| Tool + Cheat sheet | What it does |
| ------------------ | ------------ |
| [crunch](crunch.md) | Generate combinations of words and manglings to be used later off as attacking dictionaries. |
| 


## Vulnerability assessment: scanners

| Available scanners + Cheat sheet | URL | 
| ------------------ | --- |
| [Nessus](nessus.md) | [https://www.tenable.com/downloads/nessus](https://www.tenable.com/downloads/nessus) |  
| OpenVAS | [https://www.openvas.org/](https://www.openvas.org/) | 
| Nexpose | [https://www.rapid7.com/products/nexpose/](https://www.rapid7.com/products/nexpose/) | 
| GFOLAnGuard | [https://www.gfi.com/products-and-solutions/network-security-solutions/gfi-languard](https://www.gfi.com/products-and-solutions/network-security-solutions/gfi-languard) |



## Tools for exploitation

| Tool + Cheat sheet | What it does |
| ------------------ | ------------ |
| [netcat](netcat.md) | netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP. |
| [openSSL](openssl.md) | OpenSSL is a software library for applications that provide secure communications over computer networks against eavesdropping or need to identify the party at the other end. It is widely used by Internet servers, including the majority of HTTPS websites. |


## Web pentesting

| Vulnerability / Technique | What it does |
| ------------------ | ------------ |
| [Backdoors with netcat](netcat.md#backdoors-with-netcat) |   |
| [Buffer Overflow attacks](buffer-overflow.md) |   |
| [Remote Code Execution](remote-code-execution-rce.md) |   |
| [XSS attack - Cross-site Scripting attack](cross-site-scripting-xss.md) | **Cross-Site Scripting** attacks or **XSS** attacks enable attackers to inject client-side scripts into web pages. This is done through an URL than the attacker sends. Crafted in the URL, this js payload is injected. | 
| [SQL injection](sql-injection.md) | SQL stands for Structure Query Language. SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. |



### Password cracker


| Tool + Cheat sheet | What it does |
| ------------------ | ------------ |
| [ophcrack](ophcrack.md) | Ophcrack is a free Windows password cracker based on rainbow tables. It is a efficient implementation of rainbow tables. It comes with a Graphical User Interface and runs on multiple platforms. |
| [hashcat](hashcat.md) | Hashcat is a password recovery tool. It had a proprietary code base until 2015, but was then released as open source software. Versions are available for Linux, OS X, and Windows. [wikipedia](https://en.wikipedia.org/wiki/Hashcat). |
| [John the Ripper](john-the-ripper.md) | John the Ripper is one of those tools that can be used for several things: hash cracker and dictionary attack. | 
| [hydra](hydra.md) | Hydra can attack nearly 50 services including: Cisco auth, FTP, HTTP, IMAP, RDP, SMB, SSH, Telnet... It uses modules for each protocol. |


### Dictionary attacks

| Tool + Cheat sheet | What it does |
| ------------------ | ------------ |
| [John the Ripper](john-the-ripper.md) | John the Ripper is one of those tools that can be used for several things: hash cracker and dictionary attack. |
| [hydra](hydra.md) | Hydra can attack nearly 50 services including: Cisco auth, FTP, HTTP, IMAP, RDP, SMB, SSH, Telnet... It uses modules for each protocol. |


