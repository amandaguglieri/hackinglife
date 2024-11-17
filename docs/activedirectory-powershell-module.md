---
title: The ActiveDirectory PowerShell module
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
  - enumeration
  - reconnaissance
  - tools
---
# The ActiveDirectory PowerShell module 

The Active Directory module for Windows PowerShell is a PowerShell module that consolidates a group of cmdlets. You can use these cmdlets to manage your Active Directory domains, Active Directory Lightweight Directory Services (AD LDS) configuration sets, and Active Directory Database Mounting Tool instances in a single, self-contained package.


## Installation 

Download from [The ActiveDirectory PowerShell module github repository](https://github.com/samratashok/ADModule ) 

This module is Microsoft signed and works even in PowerShell Constrained Language Mode (CLM). 

```ps
Import-Module .\ADModule-master\Microsoft.ActiveDirectory.Management.dll 

Import-Module .\ADModule-master\ActiveDirectory\ActiveDirectory.psd1 
```

Also, you can copy the DLL from the github repo to your machine and use it to enumerate Active Directory without installing RSAT and without having administrative privileges.

```ps
Import-Module C:\ADModule\Microsoft.ActiveDirectory.Management.dll -Verbose
```


## Basic commands

```ps
# Get ACL for a folder (or a file)
Get-ACL “C:\Users\Public\Desktop”

# Search for AD elements. [See more in ldap queries](ldap.md)
Get-ADObject -LDAPFilter <thespecificfilter>

# Count occurrences in a query, like the one above.
(Get-ADObject -LDAPFilter <thespecificfilter>
).count
```


### Get-ADUser 

[More on https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps).  

```ps
# This command gets all users in the container OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM.
Get-ADUser -Filter * -SearchBase "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"

# This command gets all users that have a name that ends with SvcAccount:
Get-ADUser -Filter 'Name -like "*SvcAccount"' | Format-Table Name,SamAccountName -A

# This command gets all of the properties of the user with the SAM account name ChewDavid:
Get-ADUser -Identity ChewDavid -Properties *

# This command gets the user with the name ChewDavid in the Active Directory Lightweight Directory Services (AD LDS) instance:
Get-ADUser -Filter "Name -eq 'ChewDavid'" -SearchBase "DC=AppNC" -Properties "mail" -Server lds.Fabrikam.com:50000

# This command gets all enabled user accounts in Active Directory using an LDAP filter:
Get-ADUser -LDAPFilter '(!userAccountControl:1.2.840.113556.1.4.803:=2)'

# search for all administrative users with the `DoesNotRequirePreAuth` attribute set, meaning that they can be ASREPRoasted:
Get-ADUser -Filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}

# Find all administrative users with the SPN "servicePrincipalName" attribute set, meaning that they can likely be subject to a Kerberoasting attack
Get-ADUser -Filter "adminCount -eq '1'" -Properties * | where servicePrincipalName -ne $null | select SamAccountName,MemberOf,ServicePrincipalName | fl

```

### Get-ADComputer

```ps
# Search domain computers for interesting hostnames. SQL servers are a particularly juicy target on internal assessments. The below command searches all hosts in the domain using `Get-ADComputer`, filtering on the `DNSHostName` property that contains the word `SQL`
Get-ADComputer  -Filter "DNSHostName -like 'SQL*'"
```


### Get-ADGroup

```ps
# Search for administrative groups by filtering on the `adminCount` attribute. If set to `1`, it's protected by AdminSDHolder and known as protected groups. `AdminSDHolder` is owned by the Domain Admins group. It has the privileges to change the permissions of objects in Active Directory. 
Get-ADGroup -Filter "adminCount -eq 1" | select Name
```


### Get-ADObject
