---
title: rpcclient - A tool for interacting with smb shares
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - smb
  - port 445
  - port 137
  - port 138
  - port 139
  - samba
  - tools
---
# rpcclient - A tool for interacting with smb shares


This is a tool to perform MS-RPC functions.

The [Remote Procedure Call](https://www.geeksforgeeks.org/remote-procedure-call-rpc-in-operating-system/) (`RPC`) is a central tool to realize operational and work-sharing structures in networks and client-server architectures.

**Remote Procedure Call (RPC)** is a powerful technique for constructing **distributed, client-server based applications**. It is based on extending the conventional local procedure calling so that the **called procedure need not exist in the same address space as the calling procedure**. The two processes may be on the same system, or they may be on different systems with a network connecting them.

## Basic usage

```shell-session
# SMB NULL Session with rpcclient
rpcclient -U "" -N $ip

# Connect to a remote shared folder (same as smbclient in this regard)
rpcclient -U "" 10.129.14.128
rpcclient -U'%' 10.10.110.17

# Server information
srvinfo

# Enumerate all domains that are deployed in the network 
enumdomains

# Provides domain, server, and user information of deployed domains.
querydominfo

# Enumerates all available shares.
netshareenumall

# Provides information about a specific share.
netsharegetinfo <share>

# Get Domain Password Information
getdompwinfo

# Enumerates all domain users.
enumdomusers

# Provides information about a specific user.
queryuser <RID>
	# An example:
	# rpcclient $> queryuser 0x3e8

# Provides information about a specific group.
querygroup <ID>

# Enumerating Privileges
enumprivs

# Enumerating SID from LSA
lsaenumsid
```

### Brute forcing user enumeration with rpcclient

```shell-session
for i in $(seq 500 1100);do rpcclient -N -U "" $ip -c "queryuser 0x$(printf '%x\n' $i)" | grep "User Name\|user_rid\|group_rid" && echo "";done
```