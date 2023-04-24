---
title: "bash"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
---

# Bash

## Shortcuts


+Delete last word CTRL-W
+Fill out the next word that appears in gray: CTRL ->

## Commands


### lsb_release

Print distribution-specific information

```bash
# Display version, id, description, release and codename of the distro
lsb_release -a 
```
 


### ss
Sockets statistic. It can be used to check which ports are listening locally on a given machine.

```bash
ss -ltn
#-l: Display only listening sockets.
#-t: Display TCP sockets.
#-n: Do not try to resolve service name.
```

### netstat

Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

```bash
netstat -tnlp
```
