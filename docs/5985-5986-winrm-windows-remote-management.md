---
title: Port 5985, 5986 - Windows Remote Management (WinRM)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - port
  - "5985"
  - port
  - "5986"
  - winrm
---
# Port 5985, 5986 - Windows Remote Management (WinRM)

How is WinRM different from [Remote Desktop (RDP)](3389-rdp.md)? WinRM is a protocol for remote management, while Remote Desktop (RDP) is a protocol for remote desktop access. WinRM allows for remote execution of management commands, while RDP provides a graphical interface for remote desktop access.

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM listener.

WinRM is a network protocol based on XML web services using the [Simple Object Access Protocol](https://docs.microsoft.com/en-us/windows/win32/winrm/windows-remote-management-glossary) (`SOAP`) used for remote management of Windows systems. It takes care of the communication between [Web-Based Enterprise Management](https://en.wikipedia.org/wiki/Web-Based_Enterprise_Management) (`WBEM`) and the [Windows Management Instrumentation](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) (`WMI`), which can call the [Distributed Component Object Model](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/4a893f3d-bd29-48cd-9f43-d9777a4415b0) (`DCOM`). WinRM uses the Simple Object Access Protocol (`SOAP`) to establish connections to remote hosts and their applications. However, for security reasons, WinRM must be activated and configured manually in Windows 10. WinRM uses the TCP ports `5985` (`HTTP`) and `5986` (`HTTPS`).

Another component that fits WinRM for administration is Windows Remote Shell (`WinRS`), which lets us execute arbitrary commands on the remote system. The program is even included on Windows 7 by default.


## Footprinting winrm

As we already know, WinRM uses TCP ports 5985 (HTTP) and 5986 (HTTPS) by default, which we can scan using Nmap:

```bash
nmap -sV -sC $ip -p5985,5986 --disable-arp-ping -n
```

## Connect to a machine

### From Linux

[See evil-winrm](evil-winrm.md).

We'll connect to the WinRM service on the target and try to get a session. Because PowerShell isn't installed on Linux by default, we'll use a tool called [Evil-WinRM](evil-winrm.md)  which is made for this kind of scenario.

```bash
evil-winrm -i $ip -u <username> -p <password>
```

### From Windows 

For windows, we can use The [Test-WsMan](https://docs.microsoft.com/en-us/powershell/module/microsoft.wsman.management/test-wsman?view=powershell-7.2) cmdlet.

Also we can access  with Powershell and the [Enter-PSSession](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.2) cmdlet:

```powershell
# Create a SecureString object_
$password = ConvertTo-SecureString "$passwordOfUser" -AsPlainText -Force
$cred = new-object System.Management.Automation.PSCredential ("$domain\$userSamAccountName", $password)

# Access the host
Enter-PSSession -ComputerName $hostName -Credential $cred

#####
# Example:
# $password = ConvertTo-SecureString "Klmcargo2" -AsPlainText -Force
# $cred = new-object System.Management.Automation.PSCredential ("INLANEFREIGHT\forend", $password)
# Enter-PSSession -ComputerName ACADEMY-EA-MS01 -Credential $cred
```

