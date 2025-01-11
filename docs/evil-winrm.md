---
title: evil-winrm 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - active directory
  - windows remote management
---
# Evil-WinRm

Evil-WinRM connects to a target using the Windows Remote Management service combined with the PowerShell Remoting Protocol to establish a PowerShell session with the target.

By default, installed on kali. [See winrm](5985-5986-winrm-windows-remote-management.md).


## Basic usage

Example from [HTB machine: Responder](htb-responder.md).

```bash
evil-winrm -i $ip -u <username -p <password>

evil-winrm -i <ip> -u Administrator -H "<passwordhash>"
# -H: Hash

# Open a menu
menu

# There are some options there like
[+] Bypass-4MSI
[+] services
[+] upload
[+] download
[+] menu
[+] exit

# To use them, just run it on the terminal
```




