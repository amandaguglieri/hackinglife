---
title: SubBrute
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - dns
  - enumeration
  - tools
---
# SubBrute

SubBrute is a community driven project with the goal of creating the fastest, and most accurate subdomain enumeration tool. Some of the magic behind SubBrute is that it uses open resolvers as a kind of proxy to circumvent DNS rate-limiting ([https://www.us-cert.gov/ncas/alerts/TA13-088A](https://www.us-cert.gov/ncas/alerts/TA13-088A)). This design also provides a layer of anonymity, as **SubBrute does not send traffic directly to the target's name servers.**

This tool allows us to use self-defined resolvers and perform pure DNS brute-forcing attacks during internal penetration tests on hosts that do not have Internet access.

## Installation

```shell-session
git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1
cd subbrute
```


## Basic commands

```shell-session
echo "ns1.inlanefreight.com" > ./resolvers.txt

./subbrute inlanefreight.com -s ./names.txt -r ./resolvers.txt
```