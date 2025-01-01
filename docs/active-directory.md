---
title: Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
---
# Active Directory

!!! quote "Related resources"
	- [Powershell](powershell.md) 
	- [cmd](cmd.md)
	- [LDAP](ldap.md)


!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)



## Reconnaissance: External Recon and Enumeration Principles

| **Resource**                     | **Examples**                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ASN / IP registrars`            | [IANA](https://www.iana.org/), [arin](https://www.arin.net/) for searching the Americas, [RIPE](https://www.ripe.net/) for searching in Europe, [BGP Toolkit](https://bgp.he.net/)                                                                                                                                                                                                                                                       |
| `Domain Registrars & DNS`        | [Domaintools](https://www.domaintools.com/), [PTRArchive](http://ptrarchive.com/), [ICANN](https://lookup.icann.org/lookup), manual DNS record requests against the domain in question or against well known DNS servers, such as `8.8.8.8`. [viewdns.info](https://viewdns.info/)                                                                                                                                                       |
| `Social Media`                   | Searching Linkedin, Twitter, Facebook, your region's major social media sites, news articles, and any relevant info you can find about the organization.                                                                                                                                                                                                                                                                                 |
| `Public-Facing Company Websites` | Often, the public website for a corporation will have relevant info embedded. News articles, embedded documents, and the "About Us" and "Contact Us" pages can also be gold mines.                                                                                                                                                                                                                                                       |
| `Cloud & Dev Storage Spaces`     | [GitHub](https://github.com/), [AWS S3 buckets & Azure Blog storage containers](https://grayhatwarfare.com/), [Google searches using "Dorks"](https://www.exploit-db.com/google-hacking-database)                                                                                                                                                                                                                                        |
| `Breach Data Sources`            | [HaveIBeenPwned](https://haveibeenpwned.com/) to determine if any corporate email accounts appear in public breach data, [Dehashed](https://www.dehashed.com/) to search for corporate emails with cleartext passwords or hashes we can try to crack offline. We can then try these passwords against any exposed login portals (Citrix, RDS, OWA, 0365, VPN, VMware Horizon, custom applications, etc.) that may use AD authentication. |

## Set up

 This is one common way that a client might select for us to perform an internal penetration test. A list of the types of setups a client may choose for testing includes:

- A penetration testing distro (typically Linux) as a virtual machine in their internal infrastructure that calls back to a jump host we control over VPN, and we can SSH into.
- A physical device plugged into an ethernet port that calls back to us over VPN, and we can SSH into.
- A physical presence at their office with our laptop plugged into an ethernet port.
- A Linux VM in either Azure or AWS with access to the internal network that we can SSH into using public key authentication and our public IP address whitelisted.
- VPN access into their internal network (a bit limiting because we will not be able to perform certain attacks such as LLMNR/NBT-NS Poisoning).
- From a corporate laptop connected to the client's VPN.
- On a managed workstation (typically Windows), physically sitting in their office with limited or no internet access or ability to pull in tools. They may also elect this option but give you full internet access, local admin, and put endpoint protection into monitor mode so you can pull in tools at will.
- On a VDI (virtual desktop) accessed using Citrix or the like, with one of the configurations described for the managed workstation typically accessible over VPN either remotely or from a corporate laptop.


## Tools

|Tool|Description|
|---|---|
|[PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)/[SharpView](https://github.com/dmchell/SharpView)|A PowerShell tool and a .NET port of the same used to gain situational awareness in AD. These tools can be used as replacements for various Windows `net*` commands and more. PowerView and SharpView can help us gather much of the data that BloodHound does, but it requires more work to make meaningful relationships among all of the data points. These tools are great for checking what additional access we may have with a new set of credentials, targeting specific users or computers, or finding some "quick wins" such as users that can be attacked via Kerberoasting or ASREPRoasting.|
|[BloodHound](https://github.com/BloodHoundAD/BloodHound)|Used to visually map out AD relationships and help plan attack paths that may otherwise go unnoticed. Uses the [SharpHound](https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors) PowerShell or C# ingestor to gather data to later be imported into the BloodHound JavaScript (Electron) application with a [Neo4j](https://neo4j.com/) database for graphical analysis of the AD environment.|
|[SharpHound](https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors)|The C# data collector to gather information from Active Directory about varying AD objects such as users, groups, computers, ACLs, GPOs, user and computer attributes, user sessions, and more. The tool produces JSON files which can then be ingested into the BloodHound GUI tool for analysis.|
|[BloodHound.py](https://github.com/fox-it/BloodHound.py)|A Python-based BloodHound ingestor based on the [Impacket toolkit](https://github.com/CoreSecurity/impacket/). It supports most BloodHound collection methods and can be run from a non-domain joined attack host. The output can be ingested into the BloodHound GUI for analysis.|
|[Kerbrute](https://github.com/ropnop/kerbrute)|A tool written in Go that uses Kerberos Pre-Authentication to enumerate Active Directory accounts, perform password spraying, and brute-forcing.|
|[Impacket toolkit](https://github.com/SecureAuthCorp/impacket)|A collection of tools written in Python for interacting with network protocols. The suite of tools contains various scripts for enumerating and attacking Active Directory.|
|[Responder](https://github.com/lgandx/Responder)|Responder is a purpose-built tool to poison LLMNR, NBT-NS, and MDNS, with many different functions.|
|[Inveigh.ps1](https://github.com/Kevin-Robertson/Inveigh/blob/master/Inveigh.ps1)|Similar to Responder, a PowerShell tool for performing various network spoofing and poisoning attacks.|
|[C# Inveigh (InveighZero)](https://github.com/Kevin-Robertson/Inveigh/tree/master/Inveigh)|The C# version of Inveigh with a semi-interactive console for interacting with captured data such as username and password hashes.|
|[rpcinfo](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rpcinfo)|The rpcinfo utility is used to query the status of an RPC program or enumerate the list of available RPC services on a remote host. The "-p" option is used to specify the target host. For example the command "rpcinfo -p 10.0.0.1" will return a list of all the RPC services available on the remote host, along with their program number, version number, and protocol. Note that this command must be run with sufficient privileges.|
|[rpcclient](https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html)|A part of the Samba suite on Linux distributions that can be used to perform a variety of Active Directory enumeration tasks via the remote RPC service.|
|[CrackMapExec (CME)](https://github.com/byt3bl33d3r/CrackMapExec)|CME is an enumeration, attack, and post-exploitation toolkit which can help us greatly in enumeration and performing attacks with the data we gather. CME attempts to "live off the land" and abuse built-in AD features and protocols like SMB, WMI, WinRM, and MSSQL.|
|[Rubeus](https://github.com/GhostPack/Rubeus)|Rubeus is a C# tool built for Kerberos Abuse.|
|[GetUserSPNs.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py)|Another Impacket module geared towards finding Service Principal names tied to normal users.|
|[Hashcat](https://hashcat.net/hashcat/)|A great hash cracking and password recovery tool.|
|[enum4linux](https://github.com/CiscoCXSecurity/enum4linux)|A tool for enumerating information from Windows and Samba systems.|
|[enum4linux-ng](https://github.com/cddmp/enum4linux-ng)|A rework of the original Enum4linux tool that works a bit differently.|
|[ldapsearch](https://linux.die.net/man/1/ldapsearch)|Built-in interface for interacting with the LDAP protocol.|
|[windapsearch](https://github.com/ropnop/windapsearch)|A Python script used to enumerate AD users, groups, and computers using LDAP queries. Useful for automating custom LDAP queries.|
|[DomainPasswordSpray.ps1](https://github.com/dafthack/DomainPasswordSpray)|DomainPasswordSpray is a tool written in PowerShell to perform a password spray attack against users of a domain.|
|[LAPSToolkit](https://github.com/leoloobeek/LAPSToolkit)|The toolkit includes functions written in PowerShell that leverage PowerView to audit and attack Active Directory environments that have deployed Microsoft's Local Administrator Password Solution (LAPS).|
|[smbmap](https://github.com/ShawnDEvans/smbmap)|SMB share enumeration across a domain.|
|[psexec.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py)|Part of the Impacket toolkit, it provides us with Psexec-like functionality in the form of a semi-interactive shell.|
|[wmiexec.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/wmiexec.py)|Part of the Impacket toolkit, it provides the capability of command execution over WMI.|
|[Snaffler](https://github.com/SnaffCon/Snaffler)|Useful for finding information (such as credentials) in Active Directory on computers with accessible file shares.|
|[smbserver.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py)|Simple SMB server execution for interaction with Windows hosts. Easy way to transfer files within a network.|
|[setspn.exe](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731241(v=ws.11))|Adds, reads, modifies and deletes the Service Principal Names (SPN) directory property for an Active Directory service account.|
|[Mimikatz](https://github.com/ParrotSec/mimikatz)|Performs many functions. Notably, pass-the-hash attacks, extracting plaintext passwords, and Kerberos ticket extraction from memory on a host.|
|[secretsdump.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py)|Remotely dump SAM and LSA secrets from a host.|
|[evil-winrm](https://github.com/Hackplayers/evil-winrm)|Provides us with an interactive shell on a host over the WinRM protocol.|
|[mssqlclient.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/mssqlclient.py)|Part of the Impacket toolkit, it provides the ability to interact with MSSQL databases.|
|[noPac.py](https://github.com/Ridter/noPac)|Exploit combo using CVE-2021-42278 and CVE-2021-42287 to impersonate DA from standard domain user.|
|[rpcdump.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/rpcdump.py)|Part of the Impacket toolset, RPC endpoint mapper.|
|[CVE-2021-1675.py](https://github.com/cube0x0/CVE-2021-1675/blob/main/CVE-2021-1675.py)|Printnightmare PoC in python.|
|[ntlmrelayx.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ntlmrelayx.py)|Part of the Impacket toolset, it performs SMB relay attacks.|
|[PetitPotam.py](https://github.com/topotam/PetitPotam)|PoC tool for CVE-2021-36942 to coerce Windows hosts to authenticate to other machines via MS-EFSRPC EfsRpcOpenFileRaw or other functions.|
|[gettgtpkinit.py](https://github.com/dirkjanm/PKINITtools/blob/master/gettgtpkinit.py)|Tool for manipulating certificates and TGTs.|
|[getnthash.py](https://github.com/dirkjanm/PKINITtools/blob/master/getnthash.py)|This tool will use an existing TGT to request a PAC for the current user using U2U.|
|[adidnsdump](https://github.com/dirkjanm/adidnsdump)|A tool for enumerating and dumping DNS records from a domain. Similar to performing a DNS Zone transfer.|
|[gpp-decrypt](https://github.com/t0thkr1s/gpp-decrypt)|Extracts usernames and passwords from Group Policy preferences files.|
|[GetNPUsers.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetNPUsers.py)|Part of the Impacket toolkit. Used to perform the ASREPRoasting attack to list and obtain AS-REP hashes for users with the 'Do not require Kerberos preauthentication' set. These hashes are then fed into a tool such as Hashcat for attempts at offline password cracking.|
|[lookupsid.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/lookupsid.py)|SID bruteforcing tool.|
|[ticketer.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ticketer.py)|A tool for creation and customization of TGT/TGS tickets. It can be used for Golden Ticket creation, child to parent trust attacks, etc.|
|[raiseChild.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/raiseChild.py)|Part of the Impacket toolkit, It is a tool for automated child to parent domain privilege escalation.|
|[Active Directory Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/adexplorer)|Active Directory Explorer (AD Explorer) is an AD viewer and editor. It can be used to navigate an AD database and view object properties and attributes. It can also be used to save a snapshot of an AD database for offline analysis. When an AD snapshot is loaded, it can be explored as a live version of the database. It can also be used to compare two AD database snapshots to see changes in objects, attributes, and security permissions.|
|[PingCastle](https://www.pingcastle.com/documentation/)|Used for auditing the security level of an AD environment based on a risk assessment and maturity framework (based on [CMMI](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration) adapted to AD security).|
|[Group3r](https://github.com/Group3r/Group3r)|Group3r is useful for auditing and finding security misconfigurations in AD Group Policy Objects (GPO).|
|[ADRecon](https://github.com/adrecon/ADRecon)|A tool used to extract various data from a target AD environment. The data can be output in Microsoft Excel format with summary views and analysis to assist with analysis and paint a picture of the environment's overall security state.|


## Domain Trust Overview

A trust creates a link between the authentication systems of two domains and may allow either one-way or two-way (bidirectional) communication. 

Types of trusts:

- `Parent-child`: Two or more domains within the same forest. The child domain has a two-way transitive trust with the parent domain, meaning that users in the child domain `corp.inlanefreight.local` could authenticate into the parent domain `inlanefreight.local`, and vice-versa.
- `Cross-link`: A trust between child domains to speed up authentication.
- `External`: A non-transitive trust between two separate domains in separate forests which are not already joined by a forest trust. This type of trust utilizes [SID filtering](https://www.serverbrain.org/active-directory-2008/sid-history-and-sid-filtering.html) or filters out authentication requests (by SID) not from the trusted domain.
- `Tree-root`: A two-way transitive trust between a forest root domain and a new tree root domain. They are created by design when you set up a new tree root domain within a forest.
- `Forest`: A transitive trust between two forest root domains.
- [ESAE](https://docs.microsoft.com/en-us/security/compass/esae-retirement): A bastion forest used to manage Active Directory.


Trusts can be transitive or non-transitive:

- A `transitive` trust means that trust is extended to objects that the child domain trusts:
	- Shared, 1 to many.
	- The trust is shared with anyone in the forest. 
	- Forest, tree-root, parent-child, and cross-link trusts are transitive.
- In a non-transitive trust, the child domain itself is the only one trusted:
	- Direct trust.
	- Not extended to the next level child domains.
	- Typical for external or custom trust setup.


Trusts can be set up in two directions: one-way or two-way (bidirectional):

- - `One-way trust`: Users in a `trusted` domain can access resources in a trusting domain, not vice-versa.
- `Bidirectional trust`: Users from both trusting domains can access resources in the other domain. 
