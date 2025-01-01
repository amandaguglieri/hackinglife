---
title: Interesting Windows Computer & Active Directory Well-Known Security Identifiers - SIDs
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
---
# Interesting Windows Computer & Active Directory Well-Known Security Identifiers (SIDs)
Source: [https://adsecurity.org/?p=1001](https://adsecurity.org/?p=1001)

##### The [Microsoft Knowledge Base article KB243330 lists the well-known security identifiers in Windows operating systems](http://support.microsoft.com/KB/243330) 

Listed here are the more interesting ones from the article as well as some additional ones.

#### **Local Computer SIDs  
**

> SID: S-1-5-2  
> Name: Network  
> Description: A group that includes all users that have logged on through a network connection. Membership is controlled by the operating system.
> 
> SID: S-1-5-6  
> Name: Service  
> Description: A group that includes all security principals that have logged on as a service. Membership is controlled by the operating system.
> 
> SID: S-1-5-9  
> Name: Enterprise Domain Controllers  
> Description: A group that includes all domain controllers in a forest that uses an Active Directory directory service. Membership is controlled by the operating system.
> 
> SID: S-1-5-11  
> Name: Authenticated Users  
> Description: A group that includes all users whose identities were authenticated when they logged on. Membership is controlled by the operating system.
> 
> SID: S-1-5-18  
> Name: Local System  
> Description: A service account that is used by the operating system.
> 
> SID: S-1-5-19  
> Name: NT Authority  
> Description: Local Service
> 
> SID: S-1-5-20  
> Name: NT Authority  
> Description: Network Service

#### **New Local Computer SIDs in Windows 8.1, Windows 2012 R2, and earlier operating systems ([with KB2871997](https://adsecurity.org/?p=559 "Microsoft KB2871997: Back-Porting Windows 8.1/Win2012R2 Enhanced Security & Pass The Hash Mitigation to Windows 7, Windows 8, & Windows 2008R2")):**

> LOCAL_ACCOUNT (S-1-5-113) – any local account  
> LOCAL_ACCOUNT_AND_MEMBER_OF_ADMINISTRATORS_GROUP (S-1-5-114)

#### **Active Directory Domain SIDs’

**

> SID: S-1-5-21<DOMAIN>-500  
> Name: Administrator  
> Description: A user account for the system administrator. By default, it is the only user account that is given full control over the system.
> 
> SID: S-1-5-21<DOMAIN>-501  
> Name: Guest  
> Description: A user account for people who do not have individual accounts. This user account does not require a password. By default, the Guest account is disabled.
> 
> SID: S-1-5-21<DOMAIN>-502  
> Name: KRBTGT  
> Description: A service account that is used by the Key Distribution Center (KDC) service.
> 
> SID: S-1-5-21<DOMAIN>-512  
> Name: Domain Admins  
> Description: A global group whose members are authorized to administer the domain. By default, the Domain Admins group is a member of the Administrators group on all computers that have joined a domain, including the domain controllers. Domain Admins is the default owner of any object that is created by any member of the group.
> 
> SID: S-1-5-21<DOMAIN>-513  
> Name: Domain Users  
> Description: A global group that, by default, includes all user accounts in a domain. When you create a user account in a domain, it is added to this group by default.
> 
> SID: S-1-5-21<DOMAIN>-514  
> Name: Domain Guests  
> Description: A global group that, by default, has only one member, the domain’s built-in Guest account.
> 
> SID: S-1-5-21<DOMAIN>-515  
> Name: Domain Computers  
> Description: A global group that includes all clients and servers that have joined the domain.
> 
> SID: S-1-5-21<DOMAIN>-516  
> Name: Domain Controllers  
> Description: A global group that includes all domain controllers in the domain. New domain controllers are added to this group by default.
> 
> SID: S-1-5- 21<DOMAIN>-498  
> Name: Enterprise Read-only Domain Controllers  
> Description: A Universal group. Members of this group are Read-Only Domain Controllers in the enterprise  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5- 21<DOMAIN>-521  
> Name: Read-only Domain Controllers  
> Description: A Global group. Members of this group are Read-Only Domain Controllers in the domain  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-21<DOMAIN>-517  
> Name: Cert Publishers  
> Description: A global group that includes all computers that are running an enterprise certification authority. Cert Publishers are authorized to publish certificates for User objects in Active Directory.
> 
> SID: S-1-5-21<ROOTDOMAIN>-518  
> Name: Schema Admins  
> Description: A universal group in a native-mode domain; a global group in a mixed-mode domain. The group is authorized to make schema changes in Active Directory. By default, the only member of the group is the Administrator account for the forest root domain.
> 
> SID: S-1-5-21<ROOTDOMAIN>-519  
> Name: Enterprise Admins  
> Description: A universal group in a native-mode domain; a global group in a mixed-mode domain. The group is authorized to make forest-wide changes in Active Directory, such as adding child domains. By default, the only member of the group is the Administrator account for the forest root domain.
> 
> SID: S-1-5-21<DOMAIN>-520  
> Name: Group Policy Creator Owners  
> Description: A global group that is authorized to create new Group Policy objects in Active Directory. By default, the only member of the group is Administrator.
> 
> SID: S-1-5-32-544  
> Name: Administrators  
> Description: A built-in group. After the initial installation of the operating system, the only member of the group is the Administrator account. When a computer joins a domain, the Domain Admins group is added to the Administrators group. When a server becomes a domain controller, the Enterprise Admins group also is added to the Administrators group.
> 
> SID: S-1-5-32-545  
> Name: Users  
> Description: A built-in group. After the initial installation of the operating system, the only member is the Authenticated Users group. When a computer joins a domain, the Domain Users group is added to the Users group on the computer.
> 
> SID: S-1-5-32-546  
> Name: Guests  
> Description: A built-in group. By default, the only member is the Guest account. The Guests group allows occasional or one-time users to log on with limited privileges to a computer’s built-in Guest account.
> 
> SID: S-1-5-32-548  
> Name: Account Operators  
> Description: A built-in group that exists only on domain controllers. By default, the group has no members. By default, Account Operators have permission to create, modify, and delete accounts for users, groups, and computers in all containers and organizational units of Active Directory except the Builtin container and the Domain Controllers OU. Account Operators do not have permission to modify the Administrators and Domain Admins groups, nor do they have permission to modify the accounts for members of those groups.
> 
> SID: S-1-5-32-549  
> Name: Server Operators  
> Description: A built-in group that exists only on domain controllers. By default, the group has no members. Server Operators can log on to a server interactively; create and delete network shares; start and stop services; back up and restore files; format the hard disk of the computer; and shut down the computer.
> 
> SID: S-1-5-32-550  
> Name: Print Operators  
> Description: A built-in group that exists only on domain controllers. By default, the only member is the Domain Users group. Print Operators can manage printers and document queues.
> 
> SID: S-1-5-32-551  
> Name: Backup Operators  
> Description: A built-in group. By default, the group has no members. Backup Operators can back up and restore all files on a computer, regardless of the permissions that protect those files. Backup Operators also can log on to the computer and shut it down.
> 
> SID: S-1-5-32-552  
> Name: Replicators  
> Description: A built-in group that is used by the File Replication service on domain controllers. By default, the group has no members. Do not add users to this group
> 
> SID: S-1-5-32-557  
> Name: BUILTIN\Incoming Forest Trust Builders  
> Description: An alias. Members of this group can create incoming, one-way trusts to this forest.
> 
> SID: S-1-5-32-569  
> Name: BUILTIN\Cryptographic Operators  
> Description: A Builtin Local group. Members are authorized to perform cryptographic operations.  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-21<DOMAIN>-571  
> Name: Allowed RODC Password Replication Group  
> Description: A Domain Local group. Members in this group can have their passwords replicated to all read-only domain controllers in the domain.  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-21<DOMAIN>-572  
> Name: Denied RODC Password Replication Group  
> Description: A Domain Local group. Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-32-573  
> Name: BUILTIN\Event Log Readers  
> Description: A Builtin Local group. Members of this group can read event logs from local machine.  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-32-574  
> Name: BUILTIN\Certificate Service DCOM Access  
> Description: A Builtin Local group. Members of this group are allowed to connect to Certification Authorities in the enterprise.  
> _New with Windows Server 2008 Active Directory schema (or newer)_
> 
> SID: S-1-5-21-<DOMAIN>–522  
> Name: Cloneable Domain Controllers  
> Description: A Global group. Members of this group that are domain controllers may be cloned.  
> _New with Windows Server 2012 Active Directory schema (or newer)_
> 
> SID: S-1-5-32-578  
> Name: BUILTIN\Hyper-V Administrators  
> Description: A Builtin Local group. Members of this group have complete and unrestricted access to all features of Hyper-V.  
> _New with Windows Server 2012 Active Directory schema (or newer)_
> 
> SID: S-1-5-32-579  
> Name: BUILTIN\Access Control Assistance Operators  
> Description: A Builtin Local group. Members of this group can remotely query authorization attributes and permissions for resources on this computer.  
> _New with Windows Server 2012 Active Directory schema (or newer)_
> 
> SID: S-1-5-32-580  
> Name: BUILTIN\Remote Management Users  
> Description: A Builtin Local group. Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.  
> _New with Windows Server 2012 Active Directory schema (or newer)_
> 
> SID: S-1-5-64-10  
> Name: NTLM Authentication  
> Description: A SID that is used when the NTLM authentication package authenticated the client
> 
> SID: S-1-5-64-14  
> Name: SChannel Authentication  
> Description: A SID that is used when the SChannel authentication package authenticated the client.
> 
> SID: S-1-5-64-21  
> Name: Digest Authentication  
> Description: A SID that is used when the Digest authentication package authenticated the client.
> 
> SID: S-1-5-80  
> Name: NT Service  
> Description: An NT Service account prefix
> 
> SID: S-1-5-80-0  
> NT SERVICES\ALL SERVICES  
> Name: All Services  
> Description: A group that includes all service processes that are configured on the system. Membership is controlled by the operating system.