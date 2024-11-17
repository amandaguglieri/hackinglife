---
title: cmd
author: amandaguglieri
draft: false
TableOfContents: true
---
# cmd

```cmd-session

# Run a utility as another user
runas /netonly /user:htb.local\jackie.may powershell

# The command net use connects a computer to or disconnects a computer from a shared resource or displays information about computer connections.
net use n: \\192.168.220.129\Finance

# Connect/ Disconnect a share with user and password
net use n: \\192.168.220.129\Finance /user:plaintext Password123

# Count how many files the shared folder and its subdirectories contain.
dir n: /a-d /s /b | find /c ":\"
# dir   ->  List
# n:	-> Directory or drive to search
/a-d	-> /a is the attribute and -d means not directories
/s	    -> Displays files in a specified directory and all subdirectories
/b      ->	Uses bare format (no heading information or summary)

# Search for specific names in files, like cred, secret, pass
dir n:\*cred* /s /b
dir n:\*secret* /s /b

#  search for a specific word within a text file
findstr /s /i cred n:\*.*

```