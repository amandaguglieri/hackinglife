---
title: "Nmap"
draft: false
TableOfContents: true
---

## Description
Network Mapper is an open source tool for network exploration and security auditing. Free and open-source scanner created by Gordon Lyon. Nmap is used to discover hosts and services on a computer network by sending packages and analyzing the responses.
Another discovery feature is that of operating system detection. These features are extensible by scripts that provide more advanced service detection.

## Cheat Sheet

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

nmap -sL 10.0.2.1  // lists targets to scan
nmap -sC -sV -p-10.0.2.1  // Full scanner
nmap -sU -sV  10.0.2.1 //UDP quick
nmap -sA 10.0.2.1 // called ACK scan. Returns if the port is filtered or not. Useful to determine if there is a firewall.
nmap -sW 10.0.2.1 // It sends a ACK packet. In the response we pay attention to the windows size of the TCP header. If the windows size is different from zero, the port is open. If it is zero, then port is either closed or filtered.
```

To redirect results to a file > targetfile.txt


Search an script in nmap:

```bash
locate -r nse$|grep <term>
# if this doesn’t work, update the db with:
sudo updatedb
```

Attacking a ssh connection:

```bash
nmap 192.153.213.3 -p 22 --script ssh-brute --script-args userdb=users.txt,passdb=/usr/share/nmap/nselib/data/passwords.lst
```

To get services in a range

```bash
nmap -sV --script=banner 192.217.70.0/24
```

