---
title: "Amass"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - dns enumeration
  - enumeration
  - tools
---

# Amass

In depth DNS Enumeration and network mapping.

## Install

```bash
apt install snapd
service snapd start
snap install amass
```


 
Before diving into using Amass, we should make the most of it by adding API keys to it. 

**1.** First, we can see which data sources are available for Amass (paid and free) by running:

```bash
amass enum -list 
```

**2.** Next, we will need to create a config file to add our API keys to.

```bash
sudo curl https://raw.githubusercontent.com/OWASP/Amass/master/examples/config.ini >~/.config/amass/config.ini
```

**3.**  Now, see the file ~/.config/amass/config.ini and register in as many services as you can. Once you have obtained your API ID and Secret, edit the config.ini file and add the credentials to the file.

```bash
sudo nano ~/.config/amass/config.ini
```

**4.** Now, edit the file to add the sources. It is recommended to add:

+ censys.io: guesswork out of understanding and protecting your organization’s digital footprint.
+ https://asnlookup.com: Quickly lookup updated information about specific Autonomous System Number (ASN), Organization, CIDR, or registered IP addresses (IPv4 and IPv6) among other relevant data. We also offer a free and paid API access!
+ https://otx.alienvault.com:  Quickly identify if your endpoints have been compromised in major cyber attacks using OTX Endpoint Security and many other.
+ https://bigdatacloud.com
+ https://cloudflare.com
+ https://www.digicert.com/tls-ssl/certcentral-tls-ssl-manager: 
+ https://fullhunt.io
+ https://github.com
+ https://ipdata.co
+ https://leakix.net
+ as many more as you can.

**5.** When ready, we can run amass:



## Basic usage


```bash
amass enum -active -d crapi.apisec.ai  
```

Some flags:

```
-active: Attempt zone transfer and certificate name grabs.
-bl: Blacklist of subdomain names that will not be investigated
-d: to specify a domain
-ip: Show ip addresses of cached subdomais.
–include-unresolvable: output DNS names that did not resolve.
-o file.txt: To output the result into a file
-w: path to a different wordlist file
```



Also, to be more precise:

```bash
amass enum -active -d <target> | grep api
# amass enum -active -d microsoft.com | grep api
```

Amass has several useful command-line options. Use the intel command to collect SSL certificates, search reverse Whois records, and find ASN IDs associated with your target. Start by providing the command with target IP addresses

```bash
amass intel -addr [target IP addresses]
```

If this scan is successful, it will provide you with domain names. These domains can then be passed to intel with the whois option to perform a reverse Whois lookup:

```bash
amass intel -d [target domain] –whois
```

This could give you a ton of results. Focus on the interesting results that relate to your target organization. Once you have a list of interesting domains, upgrade to the enum subcommand to begin enumerating subdomains. If you specify the -passive option, Amass will refrain from directly interacting with your target:

```bash
amass enum -passive -d [target domain]
```

The active enum scan will perform much of the same scan as the passive one, but it will add domain name resolution, attempt DNS zone transfers, and grab SSL certificate information:

```bash
amass enum -active -d [target domain]
```

To up your game, add the -brute option to brute-force subdomains, -w to specify the API_superlist wordlist, and then the -dir option to send the output to the directory of your choice:

```bash
amass enum -active -brute -w /usr/share/wordlists/API_superlist -d [target domain] -dir [directory name]  
```

