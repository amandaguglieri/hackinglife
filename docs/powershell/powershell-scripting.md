---
title: PowerShell scripting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - powershell
  - scripting
---

# PowerShell scripting

Fundamentals for writing and reading PowerShell scripts. For a command reference (not scripting), see the [PowerShell cheat sheet](../powershell.md).

## Execution policy

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Run a script that would otherwise be blocked
powershell -ExecutionPolicy Bypass -File script.ps1
```

See [Execution Policy bypasses](../execution-policy-bypasses.md) for offensive angles.

## Variables and types

```powershell
$name = "offsec"
Write-Output $name

[int]$port = 443
[string]$target = "10.10.10.10"

# Everything is an object - inspect its type
$name.GetType()
```

## Quoting and string interpolation

```powershell
$user = "amanda"

Write-Output "hello, $user"        # double quotes interpolate variables
Write-Output 'hello, $user'        # single quotes are literal

# Expression interpolation
Write-Output "2 + 2 = $(2 + 2)"
```

## Arrays and hashtables

```powershell
$hosts = @("10.10.10.1", "10.10.10.2", "10.10.10.3")

$hosts[0]              # first element
$hosts.Count           # length

foreach ($h in $hosts) {
    Write-Output $h
}

# Hashtables
$creds = @{ user = "admin"; pass = "P@ssw0rd" }
$creds["user"]
$creds.pass
```

## Conditionals

```powershell
if (Test-Path "C:\Windows\System32\config\SAM") {
    Write-Output "file exists"
} elseif (Test-Path "C:\Windows") {
    Write-Output "directory exists instead"
} else {
    Write-Output "not found"
}

# Comparison operators: -eq -ne -lt -le -gt -ge
# String operators: -like -notlike (wildcards), -match -notmatch (regex)
# Logical: -and -or -not

if ($env:USERNAME -eq "admin") {
    Write-Output "welcome, admin"
}
```

## Loops

```powershell
# foreach
foreach ($i in 1..5) {
    Write-Output $i
}

# for
for ($i = 0; $i -lt 5; $i++) {
    Write-Output $i
}

# while
$count = 0
while ($count -lt 5) {
    Write-Output $count
    $count++
}

# reading a file line by line
Get-Content targets.txt | ForEach-Object {
    Write-Output $_
}
```

## Functions

```powershell
function Greet {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Name
    )
    Write-Output "hello, $Name"
    return 0
}

Greet -Name "amanda"

# Capturing output
$result = Greet -Name "amanda"
```

## Parameter parsing for scripts

```powershell
# script.ps1
param(
    [string]$Target,
    [int]$Port = 443,
    [switch]$Verbose
)

Write-Output "target=$Target port=$Port verbose=$Verbose"

# Usage: .\script.ps1 -Target 10.10.10.10 -Port 8080 -Verbose
```

## Error handling

```powershell
try {
    Get-Item "C:\doesnotexist" -ErrorAction Stop
} catch {
    Write-Output "error: $($_.Exception.Message)"
} finally {
    Write-Output "cleanup runs regardless"
}

# Suppress errors inline
Get-Item "C:\doesnotexist" -ErrorAction SilentlyContinue

# Stop on any error in the script
$ErrorActionPreference = "Stop"
```

## Output and redirection

```powershell
"data" | Out-File output.txt          # write to file
"data" | Out-File -Append output.txt  # append to file
Get-Process | Out-Null                # discard output

# Redirect streams (PowerShell uses numbered streams, not just stdout/stderr)
command 2> err.txt   # error stream
command *> all.txt   # all streams
```

## Debugging scripts

```powershell
Set-PSDebug -Trace 1     # trace execution
powershell -File script.ps1 -Verbose

# Syntax check without running
[System.Management.Automation.PSParser]::Tokenize((Get-Content script.ps1 -Raw), [ref]$null)
```
