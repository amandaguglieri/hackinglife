---
title: Tools for pentesting thick client applications 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - thick client applications
  - thick client applications pentesting
  - tools
---

# Tools for pentesting thick client applications

!!! abstract "General index of the course"
    - [Introduction](../thick-applications/index.md).
    - [Tools for pentesting thick client applications](tools-for-thick-apps.md).
    - [Basic lab setup](tca-basic-lab-setup.md).
    - [First challenge: enabling a button](tca-first-challenge.md).
    - [Information gathering phase](tca-information-gathering-phase.md).
    - [Traffic analysis](tca-traffic-analysis.md).
    - [Attacking thick clients applications](tca-attacking-thick-clients-applications.md).
    - [Reversing and patching thick clients applications](tca-reversing-and-patching.md).    
    - [Common vulnerabilities](tca-common-vulnerabilities.md).
    - [Attack example](tca-attack-example.md)

## Decompilation tools

+ C++ decompilation: [https://ghidra-sre.org](https://ghidra-sre.org "https://ghidra-sre.org/")
+ C# decompilation: [dnspy](../dnspy.md).
+ JetBrains [dotPeek](../dotpeek.md).

- [Ghidra](https://www.ghidra-sre.org/)
- [IDA](https://hex-rays.com/ida-pro/)
- [OllyDbg](http://www.ollydbg.de/)
- [Radare2](https://www.radare.org/r/index.html)
- [dnSpy](https://github.com/dnSpy/dnSpy)
- [x64dbg](https://x64dbg.com/)
- [JADX](https://github.com/skylot/jadx)
- [Frida](https://frida.re/)


## Read app metadata

+  [CFF explorer](../cff-explorer.md). Open the app with CFF  Explorer to see which language and tool was used for its creation.


+ [Detect It Easy](https://github.com/horsicq/Detect-It-Easy)
+ [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
+ [Strings](https://learn.microsoft.com/en-us/sysinternals/downloads/strings)

## Sniff connections 

- TCP View from [sysInternalsSuite](../sys-internals-suite.md).
- Wireshark.
- [tcpdump](https://www.tcpdump.org/)
- Burpsuite


## Traffic monitoring

- wireshark, it's ok if we just want to monitor. 
- [Echo mirage](../echo-mirage.md), very old and not maintained.
- [mitm_relay](../mitm-relay.md) + [BurpSuite](../burpsuite.md).


## Static analysis

### Spot hard coded credentials

+ Strings from  [sysInternalsSuite](../sys-internals-suite.md). It's similar to the command "strings" in bash. It displays all the human readable strings in a binary.
+ [dnspy](../dnspy.md) can be used to spot functions containing hard coded credentials (for connections,...).


### Log analysis

When debug mode is on, you can run:

```bash
thick-app-name.exe > path/to/logs.txt
```
Open the file with the logs of the application and, if you are lucky and debug mode is still on, you will be able to see some stuff such as SQL queries, decrypted database passwords, users, temp location of the ftp file...
 
## Dynamic analysis

### Changes in the file system

+ ProcessMonitor tool from [sysInternalsSuite](../sys-internals-suite.md) to see changes in the file system. For instance, you can analyze the access to interesting files in the application directory in real time.

### Spot sensitive data in Registry entries 

+ ProcessMonitor tool from [sysInternalsSuite](../sys-internals-suite.md) to spot changes in the Registry Entries.  
- [regshot](../regshot.md) allows you to compare two snapshots of registry entries (before opening the application and during executing the application).

### Check the memory

[Process Hacker tool](../thick-applications/tca-attacking-thick-clients-applications.md/#3-database-connection-strings-in-memory) During a  a connection to database the code  that does it may be in clear text or encrypted. If encrypted, it's still possible to find it in memory. Process Hacker tool dumps the memory of the process so we might find the clear text connection string  in memory.

### Scan the application

[Visual Code grepper](tca-common-vulnerabilities.md#automated-source-code-scanning).


## Attacks

A quick list:

- Improper Error Handling.
- Hardcoded sensitive data.
- DLL Hijacking.
- Buffer Overflow.
- SQL Injection.
- Insecure Storage.
- Session Management.

### DLL Hickjacking

[Step by step](tca-attacking-thick-clients-applications.md#how-is-dll-hijacking-perform). 

**1.** Locate interesting DLL files with ProcessMonitor (or ProcMon).

**2**. Craft  malicious DLL  with msfvenom from attacker machine.

**3.** Serve it to the victime machine using an apache server.

**4.** Placing the file in the same directory from where is going to be called.

**5.** Run the app.


###  Reversing .NET applications

- [dnspy](../dnspy.md): c# code + IL code + patching the application
- [dotPeek](../dotpeek.md) (from JetBrains)
- [ILspy / Reflexil](tca-reversing-and-patching.md#using-ilspy-reflexil-to-patch-applications)
- [ILASM (IL Assembler)](tca-reversing-and-patching.md#using-ilasm-and-ldasm-to-patch-applications) (comes with .NET Framework).
- [ILDASM (IL Disassembler)](tca-reversing-and-patching.md#using-ilasm-and-ldasm-to-patch-applications) (comes with Visual Studio).

[How to do it?](tca-reversing-and-patching.md)


### Input sanitization: SQL injections

Manually



### Application Signing

Sigcheck, from SysInternals Suite ([more](tca-common-vulnerabilities.md#application-signing)).

### Compiler protection

[Binscope](tca-common-vulnerabilities.md#compiler-protection).

[PESecurity](../pesecurity.md)  is a powershell script that checks if a Windows binary (EXE/DLL) has been compiled with ASLR, DEP, SafeSEH, StrongNaming, Authenticode, Control Flow Guard, and HighEntropyVA.





Also, check these other tools and resources:

- [WinSpy](../winspy.md).
- [Window Detective](https://windowdetective.sourceforge.net/index.html)
- [netspi.com](https://www.netspi.com/blog/technical/thick-application-penetration-testing/introduction-to-hacking-thick-clients-part-2-the-network/?_gl=1*2wn9s0*_ga*MTQ0NjMzNTMxNi4xNjc1Mjc0ODU3*_ga_BVEZXBBWG7*MTY3NTI3NzMyMS4yLjAuMTY3NTI3NzMzOS40Mi4wLjA).
