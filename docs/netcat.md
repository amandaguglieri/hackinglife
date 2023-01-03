---
title: netcat
author: amandaguglieri
draft: false
TableOfContents: true
tag: http
---

Preinstalled in kali. Netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP.

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

```ash
nc -v <ip> <port>
```

