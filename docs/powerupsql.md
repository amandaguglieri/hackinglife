---
title: PowerUpSQL
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active
  - directory
  - tools
---
# PowerUpSQL

PowerUpSQL includes functions that support SQL Server discovery, weak configuration auditing, privilege escalation on scale, and post exploitation actions such as OS command execution. It is intended to be used during internal penetration tests and red team engagements. However, PowerUpSQL also includes many functions that can be used by administrators to quickly inventory the SQL Servers in their ADS domain and perform common threat hunting tasks related to SQL Server.

## Installation

Github repo: [https://github.com/NetSPI/PowerUpSQL](https://github.com/NetSPI/PowerUpSQL).

## Basic commands

Cheat sheets: [https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet)

Authenticate against the remote SQL server host and run custom queries or operating system commands.

```powershell
Get-SQLQuery -Verbose -Instance "$ipHost,$port" -username "$domain\$userSamAccountName" -password "$password" -query 'Select @@version'

# Example:
# Get-SQLQuery -Verbose -Instance "172.16.5.150,1433" -username "inlanefreight\damundsen" -password "SQL1234!" -query 'Select @@version'
```
 


