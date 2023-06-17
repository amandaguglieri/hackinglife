---
title: 873 rsync
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - rsync
  - port 873
---

# 873 rsync

## Description

rsync is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification timesand sizes of files. It is commonly found on Unix-like operating systems. The rsync algorithm is a type of delta encoding, and is used for minimizing network usage. Zlib may be used for additional data compression, and SSH or stunnel can be used for security.

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

