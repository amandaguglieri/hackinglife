---
title: nmap - A network exploration and security auditing tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanning
  - active recon
  - passiverecon
---

# nmap - A network exploration and security auditing tool

## Description

Network Mapper is an open source tool for network exploration and security auditing. Free and open-source scanner created by Gordon Lyon. Nmap is used to discover hosts and services on a computer network by sending packages and analyzing the responses. Another discovery feature is that of operating system detection. These features are extensible by scripts that provide more advanced service detection.

```
# commonly used
nmap -sT -Pn --unprivileged --script banner targetIP

# enumerate ciphers supported by the application server
nmap -sT -p 443 -Pn -unprivilegeds --script ssl-enum-ciphers targetIP

# sync-scan the top 10,000 most well-known ports
nmap -sS $IP --top-ports 10000
```


## Cheat Sheet

By default, Nmap will conduct a TCP scan unless specifically requested to perform a UDP scan.

```bash
nmap 10.0.2.1
nmap 10.0.2.1/24
nmap 10.0.2.1-254
nmap 10.0.*.*
nmap 10.0.2.1,3,17
nmap 10.0.2,4.1,3,17
nmap domain.com
nmap 10.0.2.1 -p 3389
nmap 10.0.2.1 -p 80,3389
nmap 10.0.2.1 -p 50-90
nmap 10.0.2.1 -p U:53, T:80

# It forces port enumeration and it's not limited to 1000 ports
nmap 10.0.2.1 -p-     

# It doesn’t do a port scan after host discovery amd it only prints out the available hosts that responded to the host discovery probes. Also called ping scan or ping sweep. More reliable that pinging the broadcast address because hosts do not reply to broadcast queries).
nmap -sn 10.0.2.1

# This option skips the host discovery stage altogether
nmap  -Pn  10.0.2.1  

# To skip host discovery and port scan, while still allowing NMAP Scripting Engine to run, we use -Pn -sn combined.
nmap -Pn -sn 10.0.2.1

# OS detection
nmap -O 10.0.2.1 

# Limit OS detection to promising targets
nmap -O 10.0.2.1 -osscan-limit

# Guess OS more aggressively
nmap -O 10.0.2.1 -osscan-guess

# Version detection
nmap -sV 10.0.2.1 

# Intensity level goes from 0 to 9
nmap -sV 10.0.2.1 –version-intensity 8  

tcpwrapped means that the TCP handshake was completed, 
but the remote host closed the connection without receiving any data. 
This means that something is blocking connectivity with the target host. 

# OS detection + version detection + script scanning + traceroute
nmap -A 10.0.2.1

# Half-open scanning. SYN + SYN ACK + RST
# A well-configured IDS will still detect the scan
nmap -sS 10.0.2.1

# TCP connect scan: SYN + SYN ACK + ACK + DATA (banner) +RST
# This scan gets recorded in the application logs on the target systems
nmap -sT 10.0.2.1 

# Scan a list of hosts. One per line in the file
nmap -sn -iL 10.0.2.1 hosttoscanlist.txt 

# List targets to scan
nmap -sL 10.0.2.1  

# Full scanner
nmap -sC -sV -p- 10.0.2.1  
# The script scan `-sC` flag causes `Nmap` to report the server headers `http-server-header` page and the page title `http-title` for any web page hosted on the webserver.


# UDP quick
nmap -sU -sV  10.0.2.1 

# Called ACK scan. Returns if the port is filtered or not. Useful to determine if there is a firewall.
nmap -sA 10.0.2.1 

# It sends a ACK packet. In the response we pay attention to the windows size of the TCP header. If the windows size is different from zero, the port is open. If it is zero, then port is either closed or filtered. 
nmap -sW 10.0.2.1 
```

To redirect results to a file > targetfile.txt


## Search and run a script in nmap

```bash
locate -r nse$|grep <term>
# if this doesn’t work, update the db with:
sudo updatedb


# Also:
locate scripts/<nameOfservice>
```

Run a script:

```bash
nmap --script <script name> -p<port> <host>

# For instance, a script to grab a banner
nmap -sV --script=banner <target>
```




## Attacking a ssh connection:

```bash
nmap 192.153.213.3 -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=/usr/share/nmap/nselib/data/passwords.lst
```

## To get services in a range

```bash
nmap -sV --script=banner 192.217.70.0/24
```


## Nmap for smb enumeration

```bash
# 1. Search for existing script for smb enumeration
locate -r nse$|grep <term>

# 2. Select smb-enum-shares and run it
nmap -script=smb-enum-shares <target IP>

# 3. Retrieve users
nmap -script=smb-enum-users <target IP>

# 4. Retrieve groups with passwords and user
nmap -script=smb-brute <target IP>

# Interact with the SMB service to extract the reported operating system version
nmap --script smb-os-discovery.nse -p445 <target IP>
```


## Nmap for detecting a WAF

```bash
nmap -p 80 -script http-waf-detect <TARGET> 
```


## Introducing delays

```bash
# While connecting to the service, we noticed that the connection took longer than usual (about 15 seconds). There are some services whose connection speed, or response time, can be configured. Now that we know that an FTP server is running on this port, we can deduce the origin of our "failed" scan. We could confirm this again by specifying the minimum `probe round trip time` (`--min-rtt-timeout`) in Nmap to 15 or 20 seconds and rerunning the scan.
nmap $IP --min-rtt-timeout 15
```