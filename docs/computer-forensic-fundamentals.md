---
title: File systems 
author: amandaguglieri
draft: false
TableOfContents: true
---

## MBR

The Master Boot Record (MBR) is **the information in the first sector of a hard disk or a removable drive**. It identifies how and where the system's operating system (OS) is located in order to be booted (loaded) into the computer's main storage or random access memory (RAM).

##  File systems

| Windows / floppy disls /USB sticks | FAT12, FAT 16/32, NTFS | 
| Linux most common | ext, Apple/MAC, HFS |
| CDs  most commons | ISO 9660, ISO 13490 | 
| DVDs most common | UDF, Joliet | 


## USB sticks

Get serial number and manufacture information (useful in linking to an OS later).

First time USB device connected to system (registry key): 

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR
```

Last time USB device connected to system (registry key): 

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceClass
```


## FTK imager - A tool for forensic analysis

**What is it?** A tool that quickly assess electronic evidence by obtaining forensic images of computer data, without making changes to the original evidence.

