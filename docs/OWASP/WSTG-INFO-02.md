---
title: Fingerprint Web Server - OWASP Web Security Testing Guide 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - reconnaissance
  - WSTG-INFO-02
  - dorkings
---

# Fingerprint Web Server


!!! quote ""
	[OWASP Web Security Testing Guide 4.2](index.md) > 1. Information Gathering > 1.2. Fingerprint Web Server

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.2|[WSTG-INFO-02](WSTG-INFO-02.md)|[Fingerprint Web Server](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)|- Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.|


## Whois

```shell-session
 whois $TARGET
```


```cmd-session
whois.exe <TARGET>
```


### Banner grabbing

- [nmap](../nmap.md). 
	```
	# Grab banner of services in an IP
	nmap -sV --script=banner $ip
	
	# Grab banners of services in a range
	nmap -sV --script=banner $ip/24
	```
- [telnet](../23-telnet.md)
- [openssl](../openssl.md)
```bash
openssl s_client -connect target.site:443
HEAD / HTTP/1.0
```
- - sending malformed request (with SANTACLAUS method for instance):
	```
	GET / SANTACLAUS/1.1
	```

- Some targets obfuscate their servers by modifying headers, but, there is a default ordering in the headers response, so you can do some guessing from ordering too.



## Automatic scanning tools

[netcraft](../netcraft.md), [nikto](../nikto.md).


[Netcraft](https://www.netcraft.com) can offer us information about the servers without even interacting with them, and this is something valuable from a passive information gathering point of view. We can use the service by visiting `https://sitereport.netcraft.com` and entering the target domain. We need to pay special attention to the latest IPs used. Sometimes we can spot the actual IP address from the webserver before it was placed behind a load balancer, web application firewall, or IDS, allowing us to connect directly to it if the configuration.
