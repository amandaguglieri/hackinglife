---
title: Responder.py - A SMB server to listen to NTLM hashes 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - cheat sheet
  - python
  - windows
  - active directory
  - ldap
  - server
---
# Responder.py - A SMB server to listen to NTLM hashes 

Mitre ATT&CK lists this technique as [ID: T1557.001](https://attack.mitre.org/techniques/T1557/001), `Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay`.

Responder is a LLMNR, NBT-NS and MDNS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. 

Responder can do many different kinds of attacks. For instance we may set up a malicious SMB server. When the target machine attempts to perform the NTLM authentication to that server, Responder sends a challenge back for the server to encrypt with the user's password. When the server responds, Responder will use the challenge and the encrypted response to generate the NetNTLMv2. While we can't reverse the NetNTLMv2, we can try many different common passwords to see if any generate the same challenge-response, and if we find one, we know that is the password. We can use [John The Ripper](john-the-ripper.md).

```
# Protocols that can be attacked with responder
- LLMNR
- DNS
- MDNS
- NBNS
- DHCP
- ICMP
- HTTP
- HTTPS
- SMB
- LDAP
- WebDAV
- Proxy Auth
- MSSQL
- DCE-RPC
- FTP, POP3, IMAP, and SMTP auth
```

## Installation


```bash
git clone https://github.com/lgandx/Responder.git
cd Responder 
sudo pip install -r requirements.txt
```


## Basic usage

```bash
./Responder.py -I [interface] -w -d
# -I: Set interface 
# -w: Start the WPAD rogue proxy server. Default value is False
# -d: Enable answers for DHCP broadcast requests. This option will inject a WPAD server in the DHCP response. Default: False

# In the HTB machine responder:
./Responder.py -I tun0 -w -d
```

All saved Hashes are located in Responder's logs directory (`/usr/share/responder/logs/`). We can copy the hash to a file and attempt to crack it using the [hashcat](hashcat.md) module 5600.

>**Note:** If you notice multiples hashes for one account this is because NTLMv2 utilizes both a client-side and server-side challenge that is randomized for each interaction. This makes it so the resulting hashes that are sent are salted with a randomized string of numbers. This is why the hashes don't match but still represent the same password.


**Responder in Analyzing mode:**

The `-A` flag puts us into analyze mode, allowing us to see NBT-NS, BROWSER, and LLMNR requests in the environment without poisoning any responses. 

```bash
sudo responder -I ens224 -A -wf
# sudo privileges or root to make sure that all ports needed are available on our attack host for it to function best.
# -w: The use of the -w flag utilizes the built-in WPAD proxy server. This can be highly effective, especially in large organizations, because it will capture all HTTP requests by any users that launch Internet Explorer if the browser has Auto-detect settings enabled.
# -f: attempts to fingerprint the remote host operating system and version.
```

With this configuration shown above, Responder will listen and answer any requests it sees on the wire. If you are successful and manage to capture a hash, Responder will print it out on screen and write it to a log file per host located in the `/usr/share/responder/logs` directory.

Hashes are also stored in a SQLite database that can be configured in the `Responder.conf` config file, typically located in `/usr/share/responder` unless we clone the Responder repo directly from GitHub.

## Practical example 

[HackTheBox machine: Responder](htb-responder.md).

