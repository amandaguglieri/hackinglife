---
title: sublist3r - A subdomain enumerating tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - scanning
  - subdomains
  - reconnaissance
  - pentesting
---

# sublist3r - A subdomain enumerating tool

Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu and Ask. Sublist3r also enumerates subdomains using Netcraft, Virustotal, ThreatCrowd, DNSdumpster and ReverseDNS. Easily blocked by Google.


## Installation

```bash
git clone https://github.com/aboul3la/Sublist3r
cd sublist3r
sudo pip install -r requirements.txt
```

## Usage

From sublist3r directory:

```bash
python3 sublist3r.py -d example.com -o file.txt
# -d: Specify the domain.
# -o file.txt: It prints the results to a file
# -b: Enable the subbrute  bruteforce module. This built-in module relies on the names.txt wordlist. To find it, use: locate names.txt (you can edit it).
```


