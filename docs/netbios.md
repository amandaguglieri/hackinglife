---
title: NetBIOS - Network Basic Input Output System
author: amandaguglieri
draft: false
TableOfContents: true
tag: #windows 
---

# NetBIOS - Network Basic Input Output System


NetBIOS stands for Network Basic Input Output System. Basically, servers and clients use NetBIOS when viewing network shares on the local area network.

NetBIOS supplies hostname, NetBIOS name, Domain, Network shares when querying a computer. When a MS Windows machine browses a network , it uses NetBIOS:

- datagrams to list the shares amd the machines (port 138 / UDP)
- names to find wrous (port 137 / UDP)
- sessions to transmit data to and from a windows share (port 139 / TCP )

## Create a network share in a Windows based environment: 

1. Turn on the File and Printer Sharing service.
2. Choose directories to share


```
UNC paths (Universal Naming Convention paths) \\Servername\ShareName\file.nat

\\ComputerName\C$

\\ComputerName\admin$

\\ComputerName\ipc$      //inter process communication
```

