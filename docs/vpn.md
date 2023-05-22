---
title: VPN notes
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - vpn
---

# VPN notes

There are two main types of remote access VPNs: client-based VPN and SSL VPN. SSL VPN uses the web browser as the VPN client.

Usage of a VPN service **does not** guarantee anonymity or privacy but is useful for bypassing certain network/firewall restrictions or when connected to a possible hostile network.

When connected to any penetration testing/hacking-focused lab, we should always consider the network to be "hostile." We should only connect from a virtual machine, disallow password authentication if SSH is enabled on our attacking VM, lockdown any web servers, and not leave sensitive information on our attack VM.  

**DO NOT use the same VM that we use to perform client assessments to play CTF in any platform 
**.

```bash
# Show us the networks accessible via the VPN.
 netstat -rn
  
```