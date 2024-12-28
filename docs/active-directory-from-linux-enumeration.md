---
title: Enumerating Active Directory from Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# Enumerating Active Directory from Linux

[Index of Active Directory](active-directory.md)

!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)



## 1.Hosts

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


## 2. Users

### Kerbrute

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

### rpcclient

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


### enum4linux

[enum4linux](enum4linux.md) 

```
# Enumerate users
enum4linux -U $ip  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"

```


### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

#### ldapsearch

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "

```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.

####  windapsearch

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


## 3. Password policy

The password policy can also be obtained remotely with:

### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Obtain the password policy
crackmapexec smb $ip -u <username> -p <password> --pass-pol
```


### rpcclient

[rpcclient](rpcclient.md) and the  SMB NULL session technique:

```shell-session
rpcclient -U "" -N $ip

rpcclient $> querydominfo
```


### enum4linux

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

### Net

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


### ldap 

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "*" | grep -m 1 -B 10 pwdHistoryLength
```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.



## 4. Shares

### crackmapexec

[CrackMapExec](crackmapexec.md):

```shell-session
# Enumerate shares
crackmapexec smb $ip -u <username> -p <password> --shares

# The module spider_plus will dig through each readable share on the host and list all readable files. 
sudo crackmapexec smb  $ip --local-auth -u <username> -p <password> -d <DOMAIN> -M spider_plus --share 'NameOfShare'
# CME writes the results to a JSON file located at /tmp/cme_spider_plus/<ip of host>

```


### SMBMap

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

### rpcclient

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

