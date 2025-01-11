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