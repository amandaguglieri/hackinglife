---
title: Footprinting Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
---
# Footprinting Windows

Nmap script

```
# To determine the OS
 sudo nmap -v -O $ip

# To see banners of existing open ports
sudo nmap -v $ip --script banner.nse
```

TTL technique
**`Time To Live` (TTL) counter** when utilizing ICMP to determine if the host is up. 

```
ping $ip
```

A typical response from a Windows host will either be 32 or 128. We can utilize this value since most hosts will never be more than 20 hops away from your point of origin, so there is little chance of the TTL counter dropping into the acceptable values of another OS type. More at [https://subinsb.com/default-device-ttl-values/](https://subinsb.com/default-device-ttl-values/).


## Payloads

Payloads types:

- [DLLs](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library) A Dynamic Linking Library (DLL) is a library file used in Microsoft operating systems to provide shared code and data that can be used by many different programs at once.
- [Batch](https://commandwindows.com/batch.htm) Batch files are text-based DOS scripts utilized by system administrators to complete multiple tasks through the command-line interpreter. These files end with an extension of `.bat`.
- [VBS](https://www.guru99.com/introduction-to-vbscript.html) VBScript is a lightweight scripting language based on Microsoft's Visual Basic. It is typically used as a client-side scripting language in webservers to enable dynamic web pages.
- [MSI](https://docs.microsoft.com/en-us/windows/win32/msi/windows-installer-file-extensions) `.MSI` files serve as an installation database for the Windows Installer.
- [Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) Powershell is both a shell environment and scripting language. It serves as Microsoft's modern shell environment in their operating systems.


Payload tools:

| **Resource**                                   | **Description**                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [MSFVenom & Metasploit-Framework](msfvenom.md) | [Source](https://github.com/rapid7/metasploit-framework) MSF is an extremely versatile tool for any pentester's toolkit. It serves as a way to enumerate hosts, generate payloads, utilize public and custom exploits, and perform post-exploitation actions once on the host. Think of it as a swiss-army knife. |
| `Payloads All The Things`                      | [Source](https://github.com/swisskyrepo/PayloadsAllTheThings) Here, you can find many different resources and cheat sheets for payload generation and general methodology.                                                                                                                                        |
| `Mythic C2 Framework`                          | [Source](https://github.com/its-a-feature/Mythic) The Mythic C2 framework is an alternative option to Metasploit as a Command and Control Framework and toolbox for unique payload generation.                                                                                                                    |
| [Nishang](nishang.md)                          | [Source](https://github.com/samratashok/nishang) Nishang is a framework collection of Offensive PowerShell implants and scripts. It includes many utilities that can be useful to any pentester.                                                                                                                  |
| [Darkarmour](darkarmour.md)                    | [Source](https://github.com/bats3c/darkarmour) Darkarmour is a tool to generate and utilize obfuscated binaries for use against Windows hosts.                                                                                                                                                                    |


Payload transfers:

- [Impacket](impacket.md): [Impacket](https://github.com/SecureAuthCorp/impacket) is a toolset built-in Python that provides us a way to interact with network protocols directly. Some of the most exciting tools we care about in Impacket deal with `psexec`, `smbclient`, `wmi`, Kerberos, and the ability to stand up an SMB server.
- [Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Download%20and%20Execute.md): is a great resource to find quick oneliners to help transfer files across hosts expediently.
- `SMB`: SMB can provide an easy to exploit route to transfer files between hosts. This can be especially useful when the victim hosts are domain joined and utilize shares to host data. We, as attackers, can use these SMB file shares along with C$ and admin$ to host and transfer our payloads and even exfiltrate data over the links.
- `Remote execution via MSF`: Built into many of the exploit modules in Metasploit is a function that will build, stage, and execute the payloads automatically.
- `Other Protocols`: When looking at a host, protocols such as FTP, TFTP, HTTP/S, and more can provide you with a way to upload files to the host. Enumerate and pay attention to the functions that are open and available for use.


## cmd or powershell

CMD shell is the original MS-DOS shell built into Windows. It was made for basic interaction and I.T. operations on a host. Some simple automation could be achieved with batch files, but that was all. Powershell came along with a purpose to expand the capabilities of cmd. PowerShell understands the native MS-DOS commands utilized in CMD and a whole new set of commands based in .NET.

New self-sufficient modules can also be implemented into PowerShell with cmdlets. CMD prompt deals with text input and output while Powershell utilizes .NET objects for all input and output.

Another important consideration is that CMD does not keep a record of the commands used during the session whereas, PowerShell does. So in the context of being stealthy, executing commands with cmd will leave less of a trace on the host.

Another important consideration is that CMD does not keep a record of the commands used during the session whereas, PowerShell does. So in the context of being stealthy, executing commands with cmd will leave less of a trace on the host.

If you land on a Windows XP or older host ( yes, it's still possible..) PowerShell is not present, so your only option will be cmd. PowerShell did not come to fruition until Windows 7.

Use `CMD` when:

- You are on an older host that may not include PowerShell.
- When you only require simple interactions/access to the host.
- When you plan to use simple batch files, net commands, or MS-DOS native tools.
- When you believe that execution policies may affect your ability to run scripts or other actions on the host.

Use `PowerShell` when:

- You are planning to utilize cmdlets or other custom-built scripts.
- When you wish to interact with .NET objects instead of text output.
- When being stealthy is of lesser concern.
- If you are planning to interact with cloud-based services and hosts.
- If your scripts set and use Aliases.