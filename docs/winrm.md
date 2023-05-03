---
title: WinRM - Windows Remote Management
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
---

# WinRM - Windows Remote Management

How is WinRM different from Remote Desktop (RDP)? WinRM is a protocol for remote management, while Remote Desktop (RDP) is a protocol for remote desktop access. WinRM allows for remote execution of management commands, while RDP provides a graphical interface for remote desktop access.

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM listener.

We'll connect to the WinRM service on the target and try to get a session. Because PowerShell isn't installed on Linux by default, we'll use a tool called [Evil-WinRM](evil-winrm.md)  which is made for this kind of scenario.

