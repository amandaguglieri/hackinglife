---
title: Remote Server Administration Tools (RSAT)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
---

# Remote Server Administration Tools (RSAT)

The Remote Server Administration Tools (RSAT) have been part of Windows since the days of Windows 2000. RSAT allows systems administrators to remotely manage Windows Server roles and features from a workstation running Windows 10, Windows 8.1, Windows 7, or Windows Vista. RSAT can only be installed on Professional or Enterprise editions of Windows. 

- [Script to install RSAT on Windows 10 1809, 1903, and 1909](https://gist.github.com/dually8/558fcfa9156f59504ab36615dfc4856a).
- [Other versions of Windows and more documentation](https://learn.microsoft.com/en-US/troubleshoot/windows-server/system-management-components/remote-server-administration-tools).

```ps
# Check if RSAT tools are installed
Get-WindowsCapability -Name RSAT* -Online \| Select-Object -Property Name, State

# Install all RSAT tools
Get-WindowsCapability -Name RSAT* -Online \| Add-WindowsCapability –Online

# Install a specific RSAT tool, for instance Rsat.ActiveDirectory.DS-LDS.Tools 
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0  –Online
```

Once installed, all of the tools will be available under: Control Panel> All Control Panel Items >Administrative Tools.
