---
title: User/Computer Description Field
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - windows
---
# Mount VHDX/VMDK

Why do we care about a virtual hard drive (especially Windows)? If we can locate a backup of a live machine, we can access the `C:\Windows\System32\Config` directory and pull down the `SAM`, `SECURITY` and `SYSTEM` registry hives. We can then use a tool such as secretsdump to extract the password hashes for local users.

```bash
secretsdump.py -sam SAM -security SECURITY -system SYSTEM LOCAL
```

When it comes to virtual hard drives there are three specific file types of interest are `.vhd`, `.vhdx`, and `.vmdk` files. These are `Virtual Hard Disk`, `Virtual Hard Disk v2` (both used by Hyper-V), and `Virtual Machine Disk` (used by VMware). 

We will use a tool such as [Snaffler](https://github.com/SnaffCon/Snaffler) to crawl network share drives for interesting file extensions such as `.kdbx`, `.vmdk`, `.vdhx`, `.ppk`, etc.

If we encounter any of these three files, we have options to mount them on either our local Linux or Windows attack boxes.

## Linux

#### Mount VMDK on Linux

```shell-session
guestmount -a SQL01-disk1.vmdk -i --ro /mnt/vmdk
```


#### Mount VHD/VHDX on Linux

```shell-session
guestmount --add WEBSRV10.vhdx  --ro /mnt/vhdx/ -m /dev/sda1
```

## Windows

### vhd and vhdx files

In Windows, we can right-click on the file and choose `Mount`, or use the `Disk Management` utility to mount a `.vhd` or `.vhdx` file.

 If preferred, we can use the [Mount-VHD](https://docs.microsoft.com/en-us/powershell/module/hyper-v/mount-vhd?view=windowsserver2019-ps) PowerShell cmdlet.

```powershell
Mount-VHD -Path c:\test\testvhdx.vhdx
```


### vmdk files
For a `.vmdk` file, we can right-click and choose `Map Virtual Disk` from the menu. Next, we will be prompted to select a drive letter. If all goes to plan, we can browse the target operating system's files and directories.

If this fails, we can use VMWare Workstation `File --> Map Virtual Disks` to map the disk onto our base system.
We could also add the `.vmdk` file onto our attack VM as an additional virtual hard drive, then access it as a lettered drive. We can even use `7-Zip` to extract data from a .`vmdk` file.

This [guide](https://www.nakivo.com/blog/extract-content-vmdk-files-step-step-guide/) illustrates many methods for gaining access to the files on a `.vmdk` file.


