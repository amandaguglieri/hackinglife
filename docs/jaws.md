---
title: JAWS - Just Another Windows (Enum) Script 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows pentesting
  - enumeration
---

# JAWS - Just Another Windows (Enum) Script



## Installation

Github repo: [https://github.com/411Hall/JAWS](https://github.com/411Hall/JAWS).

## Basis usage

**Run from within CMD shell and write out to file.**

```cmd
CMD C:\temp> powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1 -OutputFilename JAWS-Enum.txt
```

**Run from within CMD shell and write out to screen.**

```cmd
CMD C:\temp> powershell.exe -ExecutionPolicy Bypass -File .\jaws-enum.ps1
```

**Run from within PS Shell and write out to file.**

```powershell
PS C:\temp> .\jaws-enum.ps1 -OutputFileName Jaws-Enum.txt
```