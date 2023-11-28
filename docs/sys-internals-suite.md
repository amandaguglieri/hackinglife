---
title: SysInternals Suite
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - thick applications
---

# SysInternals Suite

To download: [https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite).

 
## TPCView

Application that allows you to see incoming and outcoming network connections associated to their application.

In the course "Mastering Thick Application Pentesting" this is really helpfil to check the conections of the vulnerable applicaiton DVTA.


## Process Monitor

This tools helps us understand File System changes and what is being accessed in the file system.

## Strings

It's similar to the command "strings" in bash. It displays all the human readable strings in a binary.  Usage:

```ps
strings.exe <binaryFile>
```


## Sigcheck

Sigcheck is a command-line utility that shows file version number, timestamp information, and digital signature details, including certificate chains.

```powershell

.\sigcheck.exe -nobanner -s -e <folder/binaryFile>
# -s: Search recursively, useful for thick client apps with lot of folders and subfolders
# -e: Scan executable images only (regardless of their extension)
# -nobanner:	Do not display the startup banner and copyright message.
```


## PsExec

[PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) is a tool that lets us execute processes on other systems, complete with full interactivity for console applications, without having to install client software manually. It works because it has a Windows service image inside of its executable. It takes this service and deploys it to the admin$ share (by default) on the remote machine. It then uses the DCE/RPC interface over SMB to access the Windows Service Control Manager API. Next, it starts the PSExec service on the remote machine. The PSExec service then creates a [named pipe](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) that can send commands to the system.