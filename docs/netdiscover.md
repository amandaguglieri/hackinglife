---
title: netdiscover - A network enumeration tool based on ARP request  
author: amandaguglieri
draft: false
TableOfContents: true
tag: reconnaissance, pentesting
---

# netdiscover - A network enumeration tool based on ARP request

Netdiscover is another discovery tool, built in Kali Linux 2018.2. It performs reconnaissance and discovery on both wireless and switched networks using ARP requests.

What is cool about netdiscover? Being nmap a best suited tool for almost everything, netdiscover provides a way to find Internal IP addresses and MAC addresses. That is the difference: netdiscover works only in internal networks. 

## Installation

Sometimes, you may be given an outdated kali ova with no netdiscover tool installed. To install:

```bash
sudo apt-get install netdiscover
```

## Basic commands

```bash
# Get help
netdiscover -h

# Get all host in an interface and in a range
# -i: interface
# -r: range
netdiscover -i eth0 -r 192.168.5.42/24 
```


