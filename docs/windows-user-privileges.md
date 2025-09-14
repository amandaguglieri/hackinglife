---
title: Windows User Privileges
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege
  - escalation
  - windows
---
# Windows User Privileges

## What are my privileges?

```powershell
whoami /priv
```

Some rights are only available to administrative users and can only be listed/leveraged when running an elevated cmd or PowerShell session. 

When a privilege is listed for our account in the `Disabled` state, it means that our account has the specific privilege assigned. Still, it cannot be used in an access token to perform the associated actions until it is enabled.

### PrivescCheck script for quick checks

⚠️ The script **IS NO LONGER** available in the repository, check out the [latest release](https://github.com/itm4n/PrivescCheck/releases/latest/) instead.

Download the script here: [PrivescCheck.ps1](https://github.com/itm4n/PrivescCheck/releases/latest/download/PrivescCheck.ps1)

Run:

```powershell
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```


### Enable a privilege: alternative #1

Windows does not provide a built-in command or PowerShell cmdlet to enable privileges, so we need some scripting to help us out.

See [PoshPrivilege: Scripts/Enable-Privilege.ps1](https://www.powershellgallery.com/packages/PoshPrivilege/0.3.0.0/Content/Scripts%5CEnable-Privilege.ps1): 

```powershell
Function Enable-Privilege {  
    <#  
        .SYNOPSIS  
            Enables specific privilege or privileges on the current process.  
  
        .DESCRIPTION  
            Enables specific privilege or privileges on the current process.  
          
        .PARAMETER Privilege  
            Specific privilege/s to enable on the current process  
          
        .NOTES  
            Name: Enable-Privilege  
            Author: Boe Prox  
            Version History:  
                1.0 - Initial Version  
  
        .EXAMPLE  
        Enable-Privilege -Privilege SeBackupPrivilege  
  
        Description  
        -----------  
        Enables the SeBackupPrivilege on the existing process  
  
        .EXAMPLE  
        Enable-Privilege -Privilege SeBackupPrivilege, SeRestorePrivilege, SeTakeOwnershipPrivilege  
  
        Description  
        -----------  
        Enables the SeBackupPrivilege, SeRestorePrivilege and SeTakeOwnershipPrivilege on the existing process  
          
    #>  
    [cmdletbinding(  
        SupportsShouldProcess = $True  
    )]  
    Param (  
        [parameter(Mandatory = $True)]  
        [Privileges[]]$Privilege  
    )      
    If ($PSCmdlet.ShouldProcess("Process ID: $PID", "Enable Privilege(s): $($Privilege -join ', ')")) {  
        #region Constants  
        $SE_PRIVILEGE_ENABLED = 0x00000002  
        $SE_PRIVILEGE_DISABLED = 0x00000000  
        $TOKEN_QUERY = 0x00000008  
        $TOKEN_ADJUST_PRIVILEGES = 0x00000020  
        #endregion Constants  
  
        $TokenPriv = New-Object TokPriv1Luid  
        $HandleToken = [intptr]::Zero  
        $TokenPriv.Count = 1  
        $TokenPriv.Attr = $SE_PRIVILEGE_ENABLED  
      
        #Open the process token  
        $Return = [PoshPrivilege]::OpenProcessToken(  
            [PoshPrivilege]::GetCurrentProcess(),  
            ($TOKEN_QUERY -BOR $TOKEN_ADJUST_PRIVILEGES),   
            [ref]$HandleToken  
        )      
        If (-NOT $Return) {  
            Write-Warning "Unable to open process token! Aborting!"  
            Break  
        }  
        ForEach ($Priv in $Privilege) {  
            $PrivValue = $Null  
            $TokenPriv.Luid = 0  
            #Lookup privilege value  
            $Return = [PoshPrivilege]::LookupPrivilegeValue($Null, $Priv, [ref]$PrivValue)               
            If ($Return) {  
                $TokenPriv.Luid = $PrivValue  
                #Adjust the process privilege value  
                $return = [PoshPrivilege]::AdjustTokenPrivileges(  
                    $HandleToken,   
                    $False,   
                    [ref]$TokenPriv,   
                    [System.Runtime.InteropServices.Marshal]::SizeOf($TokenPriv),   
                    [IntPtr]::Zero,   
                    [IntPtr]::Zero  
                )  
                If (-NOT $Return) {  
                    Write-Warning "Unable to enable privilege <$priv>! "  
                }  
            }  
        }  
    }  
}
```

### Enable a privilege: alternative #2

Another script for enabling privileges from: [https://www.leeholmes.com/adjusting-token-privileges-in-powershell/](https://www.leeholmes.com/adjusting-token-privileges-in-powershell/)

```powershell
param(    ## The privilege to adjust. This set is taken from
    ## http://msdn.microsoft.com/en-us/library/bb530716(VS.85).aspx

    [ValidateSet(
        "SeAssignPrimaryTokenPrivilege", "SeAuditPrivilege", "SeBackupPrivilege",
        "SeChangeNotifyPrivilege", "SeCreateGlobalPrivilege", "SeCreatePagefilePrivilege",
        "SeCreatePermanentPrivilege", "SeCreateSymbolicLinkPrivilege", "SeCreateTokenPrivilege",
        "SeDebugPrivilege", "SeEnableDelegationPrivilege", "SeImpersonatePrivilege", "SeIncreaseBasePriorityPrivilege",
        "SeIncreaseQuotaPrivilege", "SeIncreaseWorkingSetPrivilege", "SeLoadDriverPrivilege",
        "SeLockMemoryPrivilege", "SeMachineAccountPrivilege", "SeManageVolumePrivilege",
        "SeProfileSingleProcessPrivilege", "SeRelabelPrivilege", "SeRemoteShutdownPrivilege",
        "SeRestorePrivilege", "SeSecurityPrivilege", "SeShutdownPrivilege", "SeSyncAgentPrivilege",
        "SeSystemEnvironmentPrivilege", "SeSystemProfilePrivilege", "SeSystemtimePrivilege",
        "SeTakeOwnershipPrivilege", "SeTcbPrivilege", "SeTimeZonePrivilege", "SeTrustedCredManAccessPrivilege",
        "SeUndockPrivilege", "SeUnsolicitedInputPrivilege")]
    $Privilege,

    ## The process on which to adjust the privilege. Defaults to the current process.
    $ProcessId = $pid,

    ## Switch to disable the privilege, rather than enable it.
    [Switch] $Disable
)

## Taken from P/Invoke.NET with minor adjustments.
$definition = @'
using System;

using System.Runtime.InteropServices;
public class AdjPriv
{
    [DllImport("advapi32.dll", ExactSpelling = true, SetLastError = true)]
    internal static extern bool AdjustTokenPrivileges(IntPtr htok, bool disall,
        ref TokPriv1Luid newst, int len, IntPtr prev, IntPtr relen);

    [DllImport("advapi32.dll", ExactSpelling = true, SetLastError = true)]
    internal static extern bool OpenProcessToken(IntPtr h, int acc, ref IntPtr phtok);

    [DllImport("advapi32.dll", SetLastError = true)]
    internal static extern bool LookupPrivilegeValue(string host, string name, ref long pluid);

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    internal struct TokPriv1Luid
    {
        public int Count;
        public long Luid;
        public int Attr;
    }

    internal const int SE_PRIVILEGE_ENABLED = 0x00000002;
    internal const int SE_PRIVILEGE_DISABLED = 0x00000000;
    internal const int TOKEN_QUERY = 0x00000008;
    internal const int TOKEN_ADJUST_PRIVILEGES = 0x00000020;

    public static bool EnablePrivilege(long processHandle, string privilege, bool disable)
    {
        bool retVal;
        TokPriv1Luid tp;
        IntPtr hproc = new IntPtr(processHandle);
        IntPtr htok = IntPtr.Zero;
        retVal = OpenProcessToken(hproc, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, ref htok);
        tp.Count = 1;
        tp.Luid = 0;

        if(disable)
        {
            tp.Attr = SE_PRIVILEGE_DISABLED;
        }
        else
        {
            tp.Attr = SE_PRIVILEGE_ENABLED;
        }

        retVal = LookupPrivilegeValue(null, privilege, ref tp.Luid);
        retVal = AdjustTokenPrivileges(htok, false, ref tp, 0, IntPtr.Zero, IntPtr.Zero);
        return retVal;
    }
}
'@

$processHandle = (Get-Process -id $ProcessId).Handle
$type = Add-Type $definition -PassThru
$type[0]::EnablePrivilege($processHandle, $Privilege, $Disable)
```


## 🤷 SeImpersonate and SeAssignPrimaryToken

In Windows, every process has a token that has information about the account that is running it. These tokens are not considered secure resources, as they are just locations within memory.

 To utilize the token, the `SeImpersonate` privilege is needed.  It is only given to administrative accounts.

We will often run into this privilege after gaining remote code execution via an application that runs in the context of a service account. 
 
**List our privileges**

```
whoami /priv
```

If the command `whoami /priv` confirms that [SeImpersonatePrivilege](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/seimpersonateprivilege-secreateglobalprivilege) is listed, we may  use it to impersonate a privileged account such as `NT AUTHORITY\SYSTEM`.

For that there are several tools such as [JuicyPotato](https://github.com/ohpe/juicy-potato), [PrintSpoofer](https://github.com/itm4n/PrintSpoofer), or [RoguePotato](https://github.com/antonioCoco/RoguePotato) to escalate to `SYSTEM` level privileges, depending on the target host.

[See more on seimpersonateprivilege](seimpersonateprivilege.md)


## 🗒️ SeDebugPrivilege

This privilege can be used to capture sensitive information from system memory, or access/modify kernel and application structures. A user might be assigned the SeDebugPrivilege without belonging to the administrators group.

[See more on SeDebugPrivilege](sedebugprivilege.md).


## 🖨️ SeLoadDriverPrivilege

[Print Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#print-operators) is another highly privileged group, which grants its members the `SeLoadDriverPrivilege`, rights to manage, create, share, and delete printers connected to a Domain Controller, as well as the ability to log on locally to a Domain Controller and shut it down.

!!! tip "Note"
	Note: Since Windows 10 Version 1803, the "SeLoadDriverPrivilege" is not exploitable, as it is no longer possible to include references to registry keys under "HKEY_CURRENT_USER".


[See more on SeLoadDriverPrivilege](seloaddriverprivilege.md).


## 🔊 SeManageVolume

[See more on SeManageVolume](semanagevolumeprivilege.md).

 

## 🅾️ SeTakeOwnershipPrivilege

[SeTakeOwnershipPrivilege](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/take-ownership-of-files-or-other-objects) grants a user the ability to take ownership of any "securable object," meaning Active Directory objects, NTFS files/folders, printers, registry keys, services, and processes. This privilege assigns [WRITE_OWNER](https://docs.microsoft.com/en-us/windows/win32/secauthz/standard-access-rights) rights over an object, meaning the user can change the owner within the object's security descriptor.

[See more on SeTakeOwnershipPrivilege](setakeownershipprivilege.md).


## 🔊 SeRestorePrivilege

[See more on SeRestorePrivilege](serestoreprivilege.md).



## Compilations

Example with the [https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges](https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges) where I have cloned the awesome work of https://github.com/3gstudent.

Compile `EnableSeLoadDriverPrivilege.exe` . I've set up Visual Studio 2022 in a Windows Virtual Machine. 

```
# Go to https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges and access to the .cpp files. In the case of EnableSeLoadDriverPrivilege.cpp, download it


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



## Windows Authorization Process

**Windows Authorization Process in a nugshell:**  the process started when a user attempts to access a securable object such as a folder on a file share. During this process, the user's access token (including their user SID, SIDs for any groups they are members of, privilege list, and other access information) is compared against [Access Control Entries (ACEs)](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-entries) within the object's [security descriptor](https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptors) (which contains security information about a securable object such as access rights (discussed below) granted to users or groups). Once this comparison is complete, a decision is made to either grant or deny access. This entire process happens almost instantaneously whenever a user tries to access a resource on a Windows host. As part of our enumeration and privilege escalation activities, we attempt to use and abuse access rights and leverage or insert ourselves into this authorization process to further our access towards our goal.

![](img/privileges.png)


### Rights and Privileges in Windows

| **Group**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default Administrators      | Domain Admins and Enterprise Admins are "super" groups.                                                                                                                                                                                                                                                                                                                                            |
| Server Operators            | Members can modify services, access SMB shares, and backup files.                                                                                                                                                                                                                                                                                                                                  |
| Backup Operators            | Members are allowed to log onto DCs locally and should be considered Domain Admins. They can make shadow copies of the SAM/NTDS database, read the registry remotely, and access the file system on the DC via SMB. This group is sometimes added to the local Backup Operators group on non-DCs.                                                                                                  |
| Print Operators             | Members can log on to DCs locally and "trick" Windows into loading a malicious driver.                                                                                                                                                                                                                                                                                                             |
| Hyper-V Administrators      | If there are virtual DCs, any virtualization admins, such as members of Hyper-V Administrators, should be considered Domain Admins.                                                                                                                                                                                                                                                                |
| Account Operators           | Members can modify non-protected accounts and groups in the domain.                                                                                                                                                                                                                                                                                                                                |
| Remote Desktop Users        | Members are not given any useful permissions by default but are often granted additional rights such as `Allow Login Through Remote Desktop Services` and can move laterally using the RDP protocol.                                                                                                                                                                                               |
| Remote Management Users     | Members can log on to DCs with PSRemoting (This group is sometimes added to the local remote management group on non-DCs).                                                                                                                                                                                                                                                                         |
| Group Policy Creator Owners | Members can create new GPOs but would need to be delegated additional permissions to link GPOs to a container such as a domain or OU.                                                                                                                                                                                                                                                              |
| Schema Admins               | Members can modify the Active Directory schema structure and backdoor any to-be-created Group/GPO by adding a compromised account to the default object ACL.                                                                                                                                                                                                                                       |
| DNS Admins                  | Members can load a DLL on a DC, but do not have the necessary permissions to restart the DNS server. They can load a malicious DLL and wait for a reboot as a persistence mechanism. Loading a DLL will often result in the service crashing. A more reliable way to exploit this group is to [create a W](https://web.archive.org/web/20231115070425/https://cube0x0.github.io/Pocing-Beyond-DA/) |

Depending on group membership, and other factors such as privileges assigned via domain and local Group Policy, users can have various rights assigned to their account. 

| Setting [Constant](https://docs.microsoft.com/en-us/windows/win32/secauthz/privilege-constants) | Setting Name                                                                                                                                                                              | Standard Assignment                                     | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SeNetworkLogonRight                                                                             | [Access this computer from the network](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/access-this-computer-from-the-network)               | Administrators, Authenticated Users                     | Determines which users can connect to the device from the network. This is required by network protocols such as SMB, NetBIOS, CIFS, and COM+.                                                                                                                                                                                                             |
| SeRemoteInteractiveLogonRight                                                                   | [Allow log on through Remote Desktop Services](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services) | Administrators, Remote Desktop Users                    | This policy setting determines which users or groups can access the login screen of a remote device through a Remote Desktop Services connection. A user can establish a Remote Desktop Services connection to a particular server but not be able to log on to the console of that same server.                                                           |
| SeBackupPrivilege                                                                               | [Back up files and directories](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/back-up-files-and-directories)                               | Administrators                                          | This user right determines which users can bypass file and directory, registry, and other persistent object permissions for the purposes of backing up the system.                                                                                                                                                                                         |
| SeSecurityPrivilege                                                                             | [Manage auditing and security log](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/manage-auditing-and-security-log)                         | Administrators                                          | This policy setting determines which users can specify object access audit options for individual resources such as files, Active Directory objects, and registry keys. These objects specify their system access control lists (SACL). A user assigned this user right can also view and clear the Security log in Event Viewer.                          |
| SeTakeOwnershipPrivilege                                                                        | [Take ownership of files or other objects](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/take-ownership-of-files-or-other-objects)         | Administrators                                          | This policy setting determines which users can take ownership of any securable object in the device, including Active Directory objects, NTFS files and folders, printers, registry keys, services, processes, and threads.                                                                                                                                |
| SeDebugPrivilege                                                                                | [Debug programs](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/debug-programs)                                                             | Administrators                                          | This policy setting determines which users can attach to or open any process, even a process they do not own. Developers who are debugging their applications do not need this user right. Developers who are debugging new system components need this user right. This user right provides access to sensitive and critical operating system components. |
| SeImpersonatePrivilege                                                                          | [Impersonate a client after authentication](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/impersonate-a-client-after-authentication)       | Administrators, Local Service, Network Service, Service | This policy setting determines which programs are allowed to impersonate a user or another specified account and act on behalf of the user.                                                                                                                                                                                                                |
| SeLoadDriverPrivilege                                                                           | [Load and unload device drivers](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/load-and-unload-device-drivers)                             | Administrators                                          | This policy setting determines which users can dynamically load and unload device drivers. This user right is not required if a signed driver for the new hardware already exists in the driver.cab file on the device. Device drivers run as highly privileged code.                                                                                      |
| SeRestorePrivilege                                                                              | [Restore files and directories](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/restore-files-and-directories)                               | Administrators                                          | This security setting determines which users can bypass file, directory, registry, and other persistent object permissions when they restore backed up files and directories. It determines which users can set valid security principals as the owner of an object.                                                                                       |


### Detection

By logging event [4672: Special privileges assigned to new logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4672) which will generate an event if certain sensitive privileges are assigned to a new logon session. This can be fine-tuned in many ways, such as by monitoring privileges that should _never_ be assigned or those that should only ever be assigned to specific accounts.

### Other resources

- [Windows Privilege Abuse: Auditing, Detection, and Defense](https://blog.palantir.com/windows-privilege-abuse-auditing-detection-and-defense-3078a403d74e)


