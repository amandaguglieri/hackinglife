---
title:  SMBExec - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
---

# Impacket SMBExec

[Impacket SMBExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py) - A similar approach to PsExec without using [RemComSvc](https://github.com/kavika13/RemCom). The technique is described here. This implementation goes one step further, instantiating a local SMB server to receive the output of the commands. This is useful when the target machine does NOT have a writeable share available.

## Installation 

Donwload from: [Impacket PsExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py) -

## Basic commands


```shell-session
# Get help 
impacket-smbexec -h

# Connect to a remote machine with a local administrator account
impacket-smbexec administrator:'<password>'@$ip
```