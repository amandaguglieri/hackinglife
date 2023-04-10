---
title: noip 
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, python
---

# noip

When coding a reverse shell you don't need to hardcode the IP address of the attacker machine. Instead, you can use a Dynamic DNS server such as https://www.noip.com/. To inform this server of our attacker IP public address we will install a linux dynamic client on our kali (an agent that will do the trick).


##  Install Dynamic Update Client on Linux

As root user:

```bash
cd /usr/local/src/
wget http://www.noip.com/client/linux/noip-duc-linux.tar.gz
tar xf noip-duc-linux.tar.gz
cd noip-2.1.9-1/
make install
```