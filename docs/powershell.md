---
title: "Powershell"
author: amandaguglieri
draft: false
TableOfContents: true
---


## Basic commands

```ps

# List contents
dir
Get-ChilItem

# Print working directory
pwd
Get-Location

# Change directory
cd
cd ..			// it gets you up one level
cd ..\brotherdirectory	// go to a brother directory
cd ~\Desktop		// go to logged user's Desktop

# Creates folder
mkdir nameOfFolder
New-Item -ItemType Directory nameOfDirectory

# Display all commands saved in a file
history
Get-history

# Browse the command history
CTRL-R

# Clear screen
clear
Clear-Host

# Copy item
cp nameOfSource nameOfDestiny
Copy-Item nameOfSource nameOfDestiny

# Copy a folder and its content
cp originFolder destinyPath -Recurse
Copy-Iten originFolder destinyPath -Recurse

# Get running processes filtered by name
get-process -name ccSvcHst

# Kill processes called ccSvcHst* // Notice here wild card *
taskkill /f /im ccSvcHst*

```


## Disk Management

```powershell
# Show disks
Get-Disk

# Show disks in a more humanly mode
Get-disk | FT -AutoSize

# Show partitions from a disk
Get-Partition -DiskNumber 1

# Create partition
New-Partition -DiskNumber 1 -Size 50GB -AssignDriveLetter

# Show volume
Get-volume -DriveLetter e

# Format Disk and assign file system
Format-volume -DriveLetter E -FileSystem NTFS

# Delete Partition 
Remove-Partition -DriveLetter E
```

### Disk Management with diskpart

Diskpart is a command interpreter that helps you manage your computer's drivers. **How it works?** Before using diskpart commands, you usually have to list and select the object you want to operate on.


```powershell
# To enter in diskpart command interpreter
diskpart

# Enumerate disk
list disk

# Select disk
select disk 0

# Enumerate volumes
list volume

# Select volume
select volume 1

# Enumerate partitions
list partition

# Select partition
select partition 2

# Extend a volume (once you have it selected)
extend size=2048

# Shring a volume (once you have it selected)
shrink desired=2048
```

## Basic commands for reconnaissance

```ps
# Display Powershell relevant Powershell version information
echo $PSVersion

# Check current execution policy. If the answer is
# - "Restricted": Ps scripts cannot run.
# - "RemoteSigned": Downloaded scripts will require the script to be signed by a trusted publisher.
Get-Execution-Policy

# Bypass execution policy
powershell -ep bypass

#You can tell if PowerShell is running with administrator privileges (a.k.a “elevated” rights) with the following snippet:
[Security.Principal.WindowsIdentity]::GetCurrent().Groups -contains 'S-1-5-32-544'
# [Security.Principal.WindowsIdentity]::GetCurrent() - Retrieves the WindowsIdentity for the currently running user.
# (...).groups - Access the groups property of the identity to find out what user groups the identity is a member of.
# -contains "S-1-5-32-544" returns true if groups contains the Well Known SID of the Administrators group (the identity will only contain it if “run as administrator” was used) and otherwise false.


# List which processes are elevated:
Get-Process | Add-Member -Name Elevated -MemberType ScriptProperty -Value {if ($this.Name -in @('Idle','System')) {$null} else {-not $this.Path -and -not $this.Handle} } -PassThru | Format-Table Name,Elevated
```
