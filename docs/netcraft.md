---
title: netcraft
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
---

# netcraft


[Netcraft](https://www.netcraft.com) can offer us information about the servers without even interacting with them, and this is something valuable from a passive information gathering point of view. We can use the service by visiting `https://sitereport.netcraft.com` and entering the target domain. We need to pay special attention to the latest IPs used. 

Sometimes we can spot the actual IP address from the webserver before it was placed behind a load balancer, web application firewall, or IDS, allowing us to connect directly to it if the configuration.

See [Information Gathering phase in a Security assessment](information-gathering.md).



