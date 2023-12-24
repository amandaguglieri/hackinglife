---
title: Shodan
author: amandaguglieri
draft: false
TableOfContents: true
---

# shodan


Shodan can be used to find devices and systems permanently connected to the Internet like Internet of Things (IoT). It searches the Internet for open TCP/IP ports and filters the systems according to specific terms and criteria. For example, open HTTP or HTTPS ports and other server ports for FTP, SSH, SNMP, Telnet, RTSP, or SIP are searched. As a result, we can find devices and systems, such as surveillance cameras, servers, smart home systems, industrial controllers, traffic lights and traffic controllers, and various network components.

## Search parameters

```
country:
city:
geo:
hostname:
net:
os:
port:
before: / after:
```


## Example: shodan for enumeration

[Content from Pentesting notes](penetration-testing-process.md):

**[crt.sh](https://crt.sh/)**: it enables the verification of issued digital certificates for encrypted Internet connections. This is intended to enable the detection of false or maliciously issued certificates for a domain.

```bash
# Get all subdomais with that digital certificate
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq .

# Filter all by unique subdomain
curl -s https://crt.sh/\?q\=example.com\&output\=json | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | awk '{gsub(/\\n/,"\n");}1;' | sort -u

# With the list of unique subdomains, list all the Company hosted servers
for i in $(cat subdomainlist);do host $i | grep "has address" | grep example.com | cut -d" " -f4 >> ip-addresses.txt;done
```

**[Shodan](shodan.md)**:  Once we see which hosts can be investigated further, we can generate a list of IP addresses with a minor adjustment to the `cut` command and run them through `Shodan`.

```shell-session
for i in $(cat ip-addresses.txt);do shodan host $i;done
```

[Go to Pentesting notes to pursuit DNS enumeration](penetration-testing-process.md).