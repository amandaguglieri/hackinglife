---
title: Port 5985, 5986 - WinRM - Windows Remote Management
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
---

# Port 5985, 5986 - WinRM - Windows Remote Management

How is WinRM different from [Remote Desktop (RDP)](3389-rdp.md)? WinRM is a protocol for remote management, while Remote Desktop (RDP) is a protocol for remote desktop access. WinRM allows for remote execution of management commands, while RDP provides a graphical interface for remote desktop access.

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM listener.

WinRM uses the Simple Object Access Protocol (`SOAP`) to establish connections to remote hosts and their applications. Therefore, WinRM must be explicitly enabled and configured starting with Windows 10. WinRM relies on `TCP` ports `5985` and `5986` for communication, with the last port `5986 using HTTPS`.

Another component that fits WinRM for administration is Windows Remote Shell (`WinRS`), which lets us execute arbitrary commands on the remote system. The program is even included on Windows 7 by default.


## Footprinting winrm

As we already know, WinRM uses TCP ports 5985 (HTTP) and 5986 (HTTPS) by default, which we can scan using Nmap:

```bash
nmap -sV -sC $ip -p5985,5986 --disable-arp-ping -n
```


We'll connect to the WinRM service on the target and try to get a session. Because PowerShell isn't installed on Linux by default, we'll use a tool called [Evil-WinRM](evil-winrm.md)  which is made for this kind of scenario.

```bash
evil-winrm -i $ip -u <username> -p <password>
```


For windows, we can use The [Test-WsMan](https://docs.microsoft.com/en-us/powershell/module/microsoft.wsman.management/test-wsman?view=powershell-7.2) cmdlet.

