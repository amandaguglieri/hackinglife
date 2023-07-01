---
title: snmpwalk - SNMP scanner
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - enumeration
  - snmp
  - port 161
  - tools
---

# snmpwalk - SNMP scanner

[See SNMP for details about the protocol](161-162-snmp.md).

Snmpwalk is used to query the OIDs with their information. It retrieves a subtree of management values using SNMP GETNEXT requests.

## Installation

```shell-session
sudo apt-get install snmp
```

## Basic usage

```shell-session
snmpwalk -v2c -c public $ip
```

```shell-session
snmpwalk -v 2c -c public $ip 1.3.6.1.2.1.1.5.0
```

```shell-session
snmpwalk -v 2c -c private $ip
```

 If we do not know the community string, we can use [onesixtyone](onesixtyone.md) and SecLists wordlists to identify these community strings.