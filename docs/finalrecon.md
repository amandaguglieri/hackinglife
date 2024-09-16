---
title: Final recon - a recon tool with modules
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - enumeration
  - snmp
  - port
  - "161"
  - tools
---
# Final recon


A Python-based reconnaissance tool offering a range of modules for different tasks like SSL certificate checking, Whois information gathering, header analysis, and crawling. Its modular structure enables easy customisation for specific needs.

## Installation

```shell-session
git clone https://github.com/thewhiteh4t/FinalRecon.git
cd FinalRecon
pip3 install -r requirements.txt
chmod +x /finalrecon.py
```

## Basic commands

| Option         | Argument | Description                                         |
| -------------- | -------- | --------------------------------------------------- |
| `-h`, `--help` |          | Show the help message and exit.                     |
| `--url`        | URL      | Specify the target URL.                             |
| `--headers`    |          | Retrieve header information for the target URL.     |
| `--sslinfo`    |          | Get SSL certificate information for the target URL. |
| `--whois`      |          | Perform a Whois lookup for the target domain.       |
| `--crawl`      |          | Crawl the target website.                           |
| `--dns`        |          | Perform DNS enumeration on the target domain.       |
| `--sub`        |          | Enumerate subdomains for the target domain.         |
| `--dir`        |          | Search for directories on the target website.       |
| `--wayback`    |          | Retrieve Wayback URLs for the target.               |
| `--ps`         |          | Perform a fast port scan on the target.             |
| `--full`       |          | Perform a full reconnaissance scan on the target.   |

```shell-session
./finalrecon.py --headers --whois --url http://domain.com
```