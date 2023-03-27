---
title: PESecurity - A powershell script to check windows binaries compilations
author: amandaguglieri
draft: false
TableOfContents: true
---

# PESecurity - A powershell script to check windows binaries compilations

PESecurity is a powershell script that checks if a Windows binary (EXE/DLL) has been compiled with ASLR, DEP, SafeSEH, StrongNaming, Authenticode, Control Flow Guard, and HighEntropyVA.

## Installation

Download from:  [https://github.com/NetSPI/PESecurity]( https://github.com/NetSPI/PESecurity
).

## Usage 


```
# To execute Get-PESecurity, first import the module
Import-Module .\Get-PESecurity.psm1

# Check a single file
Get-PESecurity -file C:\Windows\System32\kernel32.dll

# Check a directory for DLLs & EXEs
Get-PESecurity -directory C:\Windows\System32\

# Check a directory for DLLs & EXEs recrusively
Get-PESecurity -directory C:\Windows\System32\ -recursive

# Export results as a CSV
Get-PESecurity -directory C:\Windows\System32\ -recursive | Export-CSV file.csv

# Show results in a table
Get-PESecurity -directory C:\Windows\System32\ -recursive | Format-Table

# Show results in a table and sort by a column
Get-PESecurity -directory C:\Windows\System32\ -recursive | Format-Table | sort ASLR
```

