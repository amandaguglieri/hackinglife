---
title: Linux Enumeration Cheat sheet
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - linux
---
# Linux Enumeration Cheat sheet

## Enumeration scripts

!!! abstract "Enumeration scripts"
    
    - [Scan the Linux system with "linEnum"](linenum.md).
    - [Search for possible paths to escalate privileges with "linPEAS"](linpeas.md).
    - [Enumerate privileges with "Linux Privilege Checker" tool](linux-privilege-checker.md).
    - [Enumerate possible exploits with "Linux Exploit Suggester" tool](linux-exploit-suggester.md).
        

## System Information

### Operating System and Kernel

```bash
# Current user
whoami

# User ID and groups
id

# Hostname
hostname

# OS and kernel version
uname -a

# Kernel version details
cat /proc/version

# OS release information
lsb_release -a

# CPU details
lscpu

# Environmental variables
env

# Available login shells
cat /etc/shells
```

## User and Process Enumeration

### Users

```bash
# List home directories (users)
ls /home

# Users with login shell
grep "*sh$" /etc/passwd

# List groups
cat /etc/group

# List sudo group members
getent group sudo

# Last login of users
lastlog

# Logged-in users
who

# Active user sessions
w
```

### Processes

```bash
# Processes run by root
ps aux | grep root

# Processes run by other users
ps au

# Check Bash history
history
```

## SSH Enumeration

```bash
# Check SSH directory permissions
ls -l ~/.ssh

# List user’s sudo privileges
sudo -l
```

## Sensitive Files

### Hidden Files and Directories

```bash
# Hidden files
find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep htb-student

# Hidden directories
find / -type d -name ".*" -ls 2>/dev/null
```

### Temporary Folders

```bash
# Check temp directories
ls -l /tmp /var/tmp /dev/shm
```

### History and Password Files

```bash
# Bash history
history

# History files
find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null

# User list and possible password hashes
cat /etc/passwd

# Shadow file (if readable)
cat /etc/shadow
```

## File System and Storage

```bash
# List mounted file systems
df -h

# Mounted drives
cat /etc/fstab

# Printers attached to system
lpstat
```

## SETUID and Writable Files

```bash
# Check SETUID and SETGID permissions
find / -perm /4000 2>/dev/null

# Writable directories
find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null

# Writable files
find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null
```

## Networking

```bash
# Network interfaces
ifconfig

# IP information
ip -a

# Routing table
route

# Detailed routing table
netstat -rnv

# DNS configuration
cat /etc/resolv.conf

# Local host mappings
cat /etc/hosts

# ARP table
arp -a
```

## Cron Jobs

```bash
# Check scheduled cron jobs
ls -la /etc/cron.daily/
```

## System Calls and Debugging

```bash
# Trace system calls
strace ping -c1 10.129.112.20
```

## Services and Installed Packages

```bash
# Installed packages
apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g' | tee -a installed_pkgs.list

# Check sudo version
sudo -V

# List binaries
ls -l /bin /usr/bin/ /usr/sbin/
```

### Checking Installed Packages Against GTFOBins

```bash
# Install pup
sudo apt install pup -y

# Generate installed package list
dpkg --get-selections | awk '{print $1}' > installed_pkgs.list

# Compare installed packages against GTFOBins
[ -f installed_pkgs.list ] && curl -s https://gtfobins.github.io/ | pup 'a text{}' | grep -v ' ' | while read -r i; do grep -q "^$i$" installed_pkgs.list && echo "Check GTFO for: $i"; done || echo "Error: installed_pkgs.list not found"
```

## Running Services by User

```bash
# Services run by root
ps aux | grep root
```

## Configuration Files and Scripts

```bash
# Configuration files
find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null

# Scripts
find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"
```

### Checking for Credentials in Config Files

```bash
# Find config files
find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null

# Check for sensitive information
cat /var/www/html/config.php

# WordPress credentials
cat wp-config.php | grep 'DB_USER\|DB_PASSWORD'
```