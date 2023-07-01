---
title: Web enumeration
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - enumeration
---

# Web enumeration

Along with all these tools and techniques it is always recommendable to review:

 - Source code
 - Some typical files such as robots.txt

## Web scanner

[See whatweb](whatweb.md).

```bash
# version of web servers, supporting frameworks, and applications
whatweb $ip
whatweb <hostname>

# Automate web application enumeration across a network.
whatweb --no-errors $ip/24
```


## Banner Grabbing / Web Server Headers

Curl:

```shell-session
curl -IL https://<TARGET>
# -I: --head (HTTP  FTP  FILE) Fetch the headers only!
# -L, --location: (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response  code),  this  option  will make  curl  redo the request on the new place. If used together with -i, --include or -I, --head, headers from all requested pages will be shown. 
```


## Hostname discovery

```shell-session
nmap --script smb-os-discovery $IP
```



## DNS enumeration

[Gobuster](gobuster.md):

```shell-session
gobuster dns -d <DOMAIN (without http)> -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```

[Dig](dig.md): 

```bash
# Get email of administrator of the domain
dig soa www.example.com
# The email will contain a (.) dot notation instead of @

# ENUMERATION
# List nameservers known for that domain
dig ns example.com @$ip
# -ns: other name servers are known in NS record
#  `@` character specifies the DNS server we want to query.

# View all available records
dig any example.com @$ip

# Display version. query a DNS server's version using a class CHAOS query and type TXT. However, this entry must exist on the DNS server.
dig CH TXT version.bind $ip
```

## Subdomain enumeration

[Gobuster](gobuster.md):

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u <exact target url>
# vhost : Uses VHOST for brute-forcing
# -w : Path to the wordlist
# -u : Specify the URL
```


[Wfuzz](wfuzz.md):

```shell-session
wfuzz -c --hc 404 -t 200 -u https://nunchucks.htb/ -w /usr/share/dirb/wordlists/common.txt -H "Host: FUZZ.nunchucks.htb" --hl 546
# -c: Color in output
# –hc 404: Hide 404 code responses
# -t 200: Concurrent Threads
# -u http://nunchucks.htb/: Target URL
# -w /usr/share/dirb/wordlists/common.txt: Wordlist 
# -H “Host: FUZZ.nunchucks.htb”: Header. Also with "FUZZ" we indicate the injection point for payloads
# –hl 546: Filter out responses with a specific number of lines. In this case, 546
```

Using [dnsenum](dnsenum.md).

Bash script, using Sec wordlist:

```shell-session
for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.example.com @$ip | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done
```

## Directory/File enumeration

[Cheat sheet with dirb](dirb.md).

[Gobuster](gobuster.md):

```bash
gobuster dir -u <exact target url> -w </path/dic.txt> -b 401 
# -b flag is to exclude from results an specific http response`
```

[Ffuf](ffuf.md):

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ

# Assuming that the default virtualhost response size is 4242 bytes, we can filter out all the responses of that size (`-fs 4242`)while fuzzing the Host - header:
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242
```


## Certificates

SSL/TLS certificates are another potentially valuable source of information if HTTPS is in use (for instance, in gathering information to prepare a phising attack).

For this we can use: 
- [sslyze](sslyze.md)
- [ssllabs by Qalys](https://www.ssllabs.com/ssltest/)

Also, you can use a script for nmap:

```bash
nmap --script ssl-enum-ciphers <HOSTNAME>
```



## Tools

- Enumeration of directories, as3 buckets, dns... : [Gobuster](gobuster.md)
- Fuzzing: [ffuf](ffuf.md), [Burpsuite](burpsuite.md), [Wfuzz](wfuzz.md), [feroxbuster](feroxbuster.md)
- Web scanner of web servers, supporting frameworks, and applications using the command-line: [whatweb].
- Taking screenshots and identify default credentials if known: [EyeWitness](eyewitness.md)
