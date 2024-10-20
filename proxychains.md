---
title: proxychains
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - proxy
  - tools
---
# proxychains

ProxyChains is a UNIX program, that hooks network-related libc functions in dynamically linked programs via a preloaded DLL and redirects the connections through SOCKS4a/5 or HTTP proxies. [Documentation](https://github.com/haad/proxychains).

## Basic usage

```
# Checks installation
which proxychains

# Configuration file
/etc/proxychains4.conf

# To use `proxychains`, we first have to edit `/etc/proxychains.conf`, comment out the final line and add the following line at the end of it:
#socks4         127.0.0.1 9050
http 127.0.0.1 8080

# Enable quiet_mode by uncommenting and removing # 
```

After this we can prepend `proxychains`to any command. The traffic of that command should be routed through proxychains. For example:

```
proxychains curl http://example.com
```

This request will be addressed to Burpsuite tool.