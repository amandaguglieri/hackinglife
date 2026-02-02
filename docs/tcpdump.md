---
title: tcpdump - A command-line packet analyzer
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - reconnaissance
---

# tcpdump - A command-line packet analyzer
 
It dumps  all tcp connections from a .pcap file. Also tcpdump  prints out a description of the contents of packets on a network interface that match the Boolean
       expression


## Installation

https://www.tcpdump.org/

## Usage

```bash
tcpdump -nntttAr <nameOfFile.pcap> 

# Exit after receiving count packets.
-c count

# Save the packet data to a file for later analysis
-w 

# Read  from  a saved  packet  file
-r

# Print out all captured packages in ASCII
-A
```