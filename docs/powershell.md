---
title: Powershell
author: amandaguglieri
draft: false
TableOfContents: true
---

# Powershell

## Basic commands

```ps

# List contents
dir
Get-ChildItem -Force
# -Force: Display hidden files 


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
Copy-Item originFolder destinyPath -Recurse

# Get running processes filtered by name
get-process -name ccSvcHst

# Kill processes called ccSvcHst* // Notice here wild card *
taskkill /f /im ccSvcHst*

# Remove a file
rm nameofFile -Recurse
# -Recurse: Remove it recursively (in a folder)

# Display content of a file
cat nameofFile
Get-Content nameofFile

# Display one page of a file at a time
more nameofFile

# Display the first lines of a file
head nameofFile

# Open a file with an app
start nameofApp nameofFile

# Runs commands or expressions on the local computer.
$Command = "Get-Process"
Invoke-Expression $Command

# PS uses Invoke-Expression to evaluate the string. Otherwise the output of $Command would be the text "Get-Process". Invoke-Expression is similar to $($command) in linux.
# IEX is an alias

```

## Powershell wildcards

The four types of Wildcard:

> The * wildcard will match zero or more characters  
>   
> The ? wildcard will match a single character
> 
> [m-n] Match a range of characters from m to n, so [f-m]ake will match fake/jake/make
> 
> [abc] Match a set of characters a,b,c.., so [fm]ake will match fake/make



## Filters

Filters are a way to power up our queries in powershell.

Example: We can use the Filter parameter with the notlike operator to filter out all Microsoft software (which may be useful when enumerating a system for local privilege escalation vectors).

```ps
get-ciminstance win32_product -Filter "NOT Vendor like '%Microsoft%'" | fl
```


The Filter operator requires at least one operator:

| **Filter** | **Meaning** |
| ----- | --------- |
| -eq | Equal to | 
| -le | Less than or equal to |
| -ge | Greater than or equal to |
| -ne | Not equal to |
| -lt | Less than |
| -gt | Greater than |
| -approx || Approximately equal to |
| -bor | Bitwise OR |
| -band | Bitwise AND |
| -recursivematch | Recursive match |
| -like | Like |
| -notlike | Not like |
| -and | Boolean AND |
| -or | Boolean OR |
| -not | Boolean NOT |


### Filter Examples: AD Object Properties

The filter can be used with operators to compare, exclude, search for, etc., a variety of AD object properties. Filters can be wrapped in curly braces, single quotes, parentheses, or double-quotes. For example, the following simple search filter using `Get-ADUser` to find information about the user "Sally Jones" can be written as follows:

```ps
Get-ADUser Filter "name -eq 'sally jones'"
Get-ADUser -Filter {name -eq 'sally jones'}
Get-ADUser -Filter 'name -eq "sally jones"'
```

As seen above, the property value (here, `sally jones`) can be wrapped in single or double-quotes.

```ps
# The asterisk (`*`) can be used as a wildcard when performing queries. 
Get-ADUser -filter {-name -like "joe*"}
# it return all domain users whose name start with `joe` (joe, joel, etc.).
```

## Escaping characters

When using filters, certain characters must be escaped:

| **Character** | **Escaped As** | **Note** |
| ----------  | ------------ | ------ |
| “ | `” | Only needed if the data is enclosed in double-quotes.  |
| ‘ | \’ | Only needed if the data is enclosed in single quotes.  |
| NULL | \00 | Standard LDAP escape sequence.  |
| \ | \5c | Standard LDAP escape sequence.  |
| * | \2a | Escaped automatically, but only in -eq and -ne comparisons. Use -like and - notlike operators for wildcard comparison.  |
| ( | /28 | Escaped automatically.  |
| )  | /29 | Escaped automatically.   |
| / | /2f | Escaped automatically. |


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

# List installed software on a computer
get-ciminstance win32_product | fl


# Gets content from a web page on the internet.
Invoke-WebRequest https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1
# alias: `iwr`, `curl`, and `wget`

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


## Howtos

### How to delete shortcuts from Public Desktop

```ps
# Instead of "everyone" set the group that you prefer
$acl = Get-ACL “C:\Users\Public\Desktop”

$rule=new-object System.Security.AccessControl.FileSystemAccessRule (“everyone”,”FullControl”, “ContainerInherit,ObjectInherit”, “None”, “Allow”)

$acl.SetAccessRule($rule)

Set-ACL “C:\Users\Public\Desktop” $acl
```

### How to uninstall winzip from powershell line of command

```powershell
# Show all software installed:
Get-WmiObject -Class win32_product

# Find winzip object
Get-WmiObject -Class win32_product | where { $_.Name -like "*Winzip*"}

# Create a variable for  the object
$wzip = Get-WmiObject -Class win32_product | where { $_.Name -like "*Winzip*"}

# Uninstall it:
msiexec /x  $wzip.localpackage /passive

```

This will start un-installation of Winzip and will show only the Progress bar only {because we are using msiexex’s /passive switch”
