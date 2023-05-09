---
title: NT Authority System
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
---

# NT Authority System

The [LocalSystem account](https://docs.microsoft.com/en-us/windows/win32/services/localsystem-account) `NT AUTHORITY\SYSTEM` is a built-in account in Windows operating systems, used by the service control manager. It has the highest level of access in the OS (and can be made even more powerful with Trusted Installer privileges). This account has more privileges than a local administrator account and is used to run most Windows services. It is also very common for third-party services to run in the context of this account by default. The SYSTEM account has thist privileges: 

SE_ASSIGNPRIMARYTOKEN_NAME, SE_AUDIT_NAME, SE_BACKUP_NAME, SE_CHANGE_NOTIFY_NAME, SE_CREATE_GLOBAL_NAME, SE_CREATE_PAGEFILE_NAME, SE_CREATE_PERMANENT_NAME, SE_CREATE_TOKEN_NAME, SE_DEBUG_NAME, SE_IMPERSONATE_NAME, SE_INC_BASE_PRIORITY_NAME, SE_INCREASE_QUOTA_NAME, SE_LOAD_DRIVER_NAME, SE_LOCK_MEMORY_NAME, SE_MANAGE_VOLUME_NAME, SE_PROF_SINGLE_PROCESS_NAME, SE_RESTORE_NAME, SE_SECURITY_NAME, SE_SHUTDOWN_NAME, SE_SYSTEM_ENVIRONMENT_NAME, SE_SYSTEMTIME_NAME, 
SE_TAKE_OWNERSHIP_NAME, SE_TCB_NAME, SE_UNDOCK_NAME 

The SYSTEM account on a domain-joined host can enumerate Active Directory by impersonating the computer account, which is essentially a special user account. If you land on a domain-joined host with SYSTEM privileges during an assessment and cannot find any useful credentials in memory or other data on the machine, there are still many things you can do. Having SYSTEM-level access within a domain environment is nearly equivalent to having a domain user account. The only real limitation is not being able to perform cross-trust Kerberos attacks such as Kerberoasting.


There are several ways to gain SYSTEM-level access on a host, including but not limited to:

-   Remote Windows exploits such as EternalBlue or BlueKeep.
-   Abusing a service running in the context of the SYSTEM account.
-   Abusing SeImpersonate privileges using [RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG) against older Windows systems, [Juicy Potato](https://github.com/ohpe/juicy-potato), or [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) if targeting [Windows 10/Windows Server 2019](https://itm4n.github.io/printspoofer-abusing-impersonate-privileges/).
-   Local privilege escalation flaws in Windows operating systems such as the [Windows 10 Task Scheduler 0day](https://blog.0patch.com/2019/06/another-task-scheduler-0day-another.html).
-   PsExec with the `-s` flag