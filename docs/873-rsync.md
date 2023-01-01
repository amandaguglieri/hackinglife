---
title: "873 rsync"
draft: false
TableOfContents: true
---

## Description

rsync is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification timesand sizes of files.[3] It is commonly found on Unix-like operating systems. The rsync algorithm is a type of delta encoding, and is used for minimizing network usage. Zlib may be used for additional data compression,[3] and SSH or stunnel can be used for security.

## Connect to the service

```bash
rsync rsync://IP
```

## Basic rsync commands

### Copy a file the server to your machine

General syntax:

```
rsync [OPTION] ... [USER@]HOST::SRC [DEST]
```

Example

```bash
rsync rsync://IP/folder/sourcefile.txt destinationfile.txt    
```

