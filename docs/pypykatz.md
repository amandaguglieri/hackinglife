---
title: pypykatz
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - dump hashes
  - passwords
---
# pypykatz

Mimikatz implementation in pure Python.  Runs on all OS's which support python>=3.6

## Installation

Download from github repo: [https://github.com/skelsec/pypykatz](https://github.com/skelsec/pypykatz).

## Basic usage 

```bash
pypykatz lsa minidump /home/path/lsass.dmp 
```

From results, and as an example, we will have this snip:

```
sid S-1-5-21-4019466498-1700476312-3544718034-1001
luid 1354633
	== MSV ==
		Username: bob
		Domain: DESKTOP-33E7O54
		LM: NA
		NT: 64f12cddaa88057e06a81b54e73b949b
		SHA1: cba4e545b7ec918129725154b29f055e4cd5aea8
		DPAPI: NA
```

`MSV` is an authentication package in Windows that LSA calls on to validate logon attempts against the SAM database. Pypykatz extracted the SID, Username, Domain, and even the NT & SHA1 password hashes associated with the bob user account's logon session stored in LSASS process memory.

But also, these others:

- `WDIGEST` is an older authentication protocol enabled by default in `Windows XP` - `Windows 8` and `Windows Server 2003` - `Windows Server 2012`. LSASS caches credentials used by WDIGEST in clear-text.
- `Kerberos` is a network authentication protocol used by Active Directory in Windows Domain environments. Domain user accounts are granted tickets upon authentication with Active Directory. LSASS `caches passwords`, `ekeys`, `tickets`, and `pins` associated with Kerberos. It is possible to extract these from LSASS process memory and use them to access other systems joined to the same domain.
- `DPAPI`: The Data Protection Application Programming Interface or DPAPI is a set of APIs in Windows operating systems used to encrypt and decrypt DPAPI data blobs on a per-user basis for Windows OS features and various third-party applications. Here are just a few examples of applications that use DPAPI and what they use it for:

| Applications | Use of DPAPI |
| --- | --- |
| `Internet Explorer` | Password form auto-completion data (username and password for saved sites). |
| `Google Chrome` | Password form auto-completion data (username and password for saved sites). |
| `Outlook` | Passwords for email accounts. |
| `Remote Desktop Connection` | Saved credentials for connections to remote machines. |
| `Credential Manager` | Saved credentials for accessing shared resources, joining Wireless networks, VPNs and more.|

Mimikatz and Pypykatz can extract the DPAPI `masterkey` for the logged-on user whose data is present in LSASS process memory. This masterkey can then be used to decrypt the secrets associated with each of the applications using DPAPI and result in the capturing of credentials for various accounts.