---
title: ping
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - scanning
  - reconnaissance
---

# Ping

ping works by sending one or more special ICMP packets (Type 8 - echo request) to a host. If the destination host replies with ICMP echo reply packets, then the host is alive.

```bash
ping www.example.com
ping 8.8.8.8
```

Ping sweeping tools automatically perform the same operation to every host in a subnet or IP range. 

