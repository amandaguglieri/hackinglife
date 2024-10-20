---
title:  PsExec - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - smb
---
# Impacket PsExec

The PSExec service then creates a [named pipe](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) that can send commands to the system.

## Installation 

Donwload from: [Impacket PsExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py) -

## Basic commands


```shell-session
# Get help 
impacket-psexec -h

# Connect to a remote machine with a local administrator account
impacket-psexec administrator:'<password>'@$ip
```