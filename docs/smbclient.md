---
title: smbclient - A tool for interacting with smb shares
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - smb
  - port 445
  - port 137
  - port 138
  - port 139
  - samba
  - tools
---

# smbclient - A tool for interacting with smb shares

See [Quick Cheat sheet for smbclient](#quick-cheat-sheet).

## smbclient installation 

```bash
sudo apt-get install smbclient
```


## smbclient configuration

Default settings are in `/etc/samba/smb.conf`.

```shell-session
 cat /etc/samba/smb.conf | grep -v "#\|\;" 
```


| **Setting**                    | **Description**                                                       |
| ------------------------------ | --------------------------------------------------------------------- |
| `[sharename]`                  | The name of the network share.                                        |
| `workgroup = WORKGROUP/DOMAIN` | Workgroup that will appear when clients query.                        |
| `path = /path/here/`           | The directory to which user is to be given access.                    |
| `server string = STRING`       | The string that will show up when a connection is initiated.          |
| `unix password sync = yes`     | Synchronize the UNIX password with the SMB password?                  |
| `usershare allow guests = yes` | Allow non-authenticated users to access defined shared?               |
| `map to guest = bad user`      | What to do when a user login request doesn't match a valid UNIX user? |
| `browseable = yes`             | Should this share be shown in the list of available shares?           |
| `guest ok = yes`               | Allow connecting to the service without using a password?             |
| `read only = yes`              | Allow users to read files only?                                       |
| `create mask = 0700`           | What permissions need to be set for newly created files?              |


[For pentesting notes on ports 137, 138, 139 and 445 with a smb service, see 137-138-139-445-smb](137-138-139-445-smb.md). 


## smbclient connection

See 
```bash
# [-L|--list=HOST] : Selecting the targeted host for the connection request.
smbclient -L -N //$ip
# -N: Suppresses the password prompt.
# -L: retrieve a list of available shares on the remote host
```

Smbclient will attempt to connect to the remote host and check if there is any authentication required. If there is, it will ask you for a user and a password for your local username. If we do not specify a specific username to smbclient when attempting to connect to the remote host, it will just use your local machine's username.If vulnerable and performing a Null Attack, we will hit Enter when prompted for a password.

After authenticating, we may obtain access to some typical shared folders, such as:

```
ADMIN$ - Administrative shares are hidden network shares created by the Windows NT family of operating systems that allow system administrators to have remote access to every disk volume on a network-connected system. These shares may not be permanently deleted but may be disabled.

C$ - Administrative share for the C:\ disk volume. This is where the operating system is hosted.

IPC$ - The inter-process communication share. Used for inter-process communication via named pipes and is not part of the file system.
WorkShares - Custom share. 
```

We will try to connect to each of the shares except for the IPC$ one, which is not valuable for us since it is not browsable as any regular directory would be and does not contain any files that we could use at this stage of our learning experience: 
```bash
# the use of / and \ might be different if you need to escape some characters
smbclient \\\\$ip\\ADMIN$
```

Important: Sometimes some jugling is needed:

```shell-session
smbclient -N -L \\$ip
smbclient -N -L \\\\$ip
smbclient -N -L /\/\$ip
```

If we have NT_STATUS_ACCESS_DENIED as output, we do not have the proper credentials to connect to this share. 


Connect to a Shared folders as Administrator:

```bash
smbclient -L 10.129.228.98 -U Administrator
```

Also we can use [rpcclient tool](rpcclient.md) for connecting to the shared folders.


## Basic commands in SMBclient



```smb-session
# Show available commands
help

# Download a file
get <file>

# See status
smbstatus

# Smbclient also allows us to execute local system commands using an exclamation mark at the beginning (`!<cmd>`) without interrupting the connection.
!cmd

!cat prep-prod.txt
```


## Quick cheat sheet 

```bash
# List shares on a machine using NULL Session
smbclient -L <target-IP>

# List shares on a machine using a valid username + password
smbclient -L \<target-IP\> -U username%password
 
# Connect to a valid share with username + password
smbclient //\<target\>/\<share$\> -U username%password
  
# List files on a specific share
smbclient //\<target\>/\<share$\> -c 'ls' password -U username
 
# List files on a specific share folder inside the share
smbclient //\<target\>/\<share$\> -c 'cd folder; ls' password -U username
 
# Download a file from a specific share folder
smbclient //\<target\>/\<share$\> -c 'cd folder;get desired_file_name' password -U username
  
# Copy a file to a specific share folder
smbclient //\<target\>/\<share$\> -c 'put /var/www/my_local_file.txt .\target_folder\target_file.txt' password -U username
 
# Create a folder in a specific share folder
smbclient //\<target\>/\<share$\> -c 'mkdir .\target_folder\new_folder' password -U username
 
# Rename a file in a specific share folder
smbclient //\<target\>/\<share$\> -c 'rename current_file.txt new_file.txt' password -U username
```