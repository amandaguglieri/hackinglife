---
title: Scheduled Tasks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
---

# Scheduled Tasks

#### Enumerating Scheduled Tasks

We can use the [schtasks](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks) command to enumerate scheduled tasks on the system.

```cmd
schtasks /query /fo LIST /v
```

With powershell:

```powershell
Get-ScheduledTask | select TaskName,State
```

If we want to grab clear credentials stored in scheduled tasks:

```powershell
Get-ScheduledTask | ForEach-Object { Get-ScheduledTaskInfo -TaskName $_.TaskName } | Select-String -Pattern "password|user"
```

We cannot list out scheduled tasks created by other users (such as admins) because they are stored in C:\Windows\System32\Tasks, which standard users do not have read access to.

We (though rarely) may encounter a scheduled task that runs as an administrator configured with weak file/folder permissions for any number of reasons.

#### Checking Permissions on C:\Scripts Directory

Made-up scenario: we notice a writeable `C:\Scripts` directory that we overlooked in our initial enumeration.

```cmd-session
 .\accesschk64.exe /accepteula -s -d C:\Scripts\
```

Output:

```
Accesschk v6.13 - Reports effective permissions for securable objects
Copyright ⌐ 2006-2020 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Scripts
  RW BUILTIN\Users
  RW NT AUTHORITY\SYSTEM
  RW BUILTIN\Administrators
 ```

We notice various scripts in this directory, such as `db-backup.ps1`, `mailbox-backup.ps1`, etc., which are also all writeable by the `BUILTIN\USERS` group. At this point, we can append a snippet of code to one of these files with the assumption that at least one of these runs on a daily, if not more frequent, basis. We write a command to send a beacon back to our C2 infrastructure and carry on with testing. The next morning when we log on, we notice a single beacon as `NT AUTHORITY\SYSTEM` on the DB01 host. We can now safely assume that one of the backup scripts ran overnight and ran our appended code in the process.