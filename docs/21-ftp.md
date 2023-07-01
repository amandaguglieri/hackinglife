---
title: 21 ftp
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - ftp
  - port 21
  - port 20
  - tftp
  - vsFTPd
---

# 21 ftp

The File Transfer Protocol (FTP) is a standard communication protocol used to transfer computer files from a server to a client on a computer network. FTP is built on a client–server model architecture using separate control and data connections between the client and the server. The FTP runs within the application layer of the TCP/IP protocol stack. Thus, it is on the same layer as `HTTP` or `POP`.

FTP users may authenticate themselves with a clear-text sign-in protocol, generally in the form of a username and password. However, they can connect anonymously if the server is configured to allow it. For secure transmission that protects the username and password and encrypts the content, FTP is often secured with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP).

However, if the network administrators choose to wrap the connection with the SSL/TLS protocol or tunnel the FTP connection through SSH to add a layer of encryption that only the source and destination hosts can decrypt, this would successfully foil most Man-in-the-Middle attacks.


## How it works

### The connection

**1.** First, the client and server establish a control channel through `TCP port 21`. The client sends commands to the server, and the server returns status codes. 

**2.** Then both communication participants can establish the data channel via `TCP port 20`. This channel is used exclusively for data transmission, and the protocol watches for errors during this process.

### Active and passive FTP

A distinction is made between `active` and `passive` FTP. In the active variant, the client establishes the connection as described via TCP port 21 and thus informs the server via which client-side port the server can transmit its responses. However, if a firewall protects the client, the server cannot reply because all external connections are blocked. For this purpose, the `passive mode` has been developed. Here, the server announces a port through which the client can establish the data channel. Since the client initiates the connection in this method, the firewall does not block the transfer.

## Installation

You may need to install ftp service. Run:

```bash
sudo apt install ftp -y
```

Then to connect with ftp, run:

```bash
ftp $ip 
```

The prompt will ask us for the username we want to log in with. Here is where the magic happens. A typical misconfiguration for running FTP services allows an anonymous account to access the service like any other authenticated user. The anonymous username can be input when the prompt appears, followed by any password whatsoever since the service will disregard the password for this specific account.

## Basic usage

```
# Connect with ftp
ftp $ip

# If anonymous login is allowed, enter anonymous as user and press Enter when prompted for password

# Give you a list of available commands
help

# List directories and files
ls

# List recursively. Not always available, only in some configurations
ls -R

# Change to a directory
cd <folder>

# Download a file to your localhost
get <nameofFileInOrigin> <nameOfFileInLocalhost>

# Upload a file from your localhost
put <yourfile>

# Exit connection
quit
```

More posibilities with wget:

```
# Download all available files at once
wget -m --no-passive ftp://anonymous:anonymous@$ip

```

## Footprinting with nmap


```shell-session
# Locate all ftp scripts related
find / -type f -name ftp* 2>/dev/null | grep scripts

# Run a general scanner for version, mode aggresive and perform default scripts
sudo nmap -sV -p21 -sC -A $ip
# ftp-anon NSE script checks whether the FTP server allows anonymous access.
# ftp-syst, for example, executes the `STAT` command, which displays information about the FTP server status.
```

[See more about nmap for scanning, running scripts and footprinting](nmap.md) 


## Other FTP services

### TFTP

Trivial File Transfer Protocol (`TFTP`) is simpler than FTP and performs file transfers between client and server processes.

- It does not provide user authentication and other valuable features supported by FTP.
- It uses  UDP.
- It does not require the user's authentication

Because of the lack of security, TFTP, unlike FTP, may only be used in local and protected networks.

#### Basic usage

```
# Sets the remote host, and optionally the port, for file transfers.
connect

# Transfers a file or set of files from the remote host to the local host.
get

# Transfers a file or set of files from the local host onto the remote host
put

# Exits tftp
quit

# Shows the current status of tftp, including the current transfer mode (ascii or binary), connection status, time-out value, and so on
status

# Turns verbose mode, which displays additional information during file transfer, on or off.
verbose 

# Unlike the FTP client, TFTP does not have directory listing functionality.
```


### vsFTPd

One of the most used FTP servers on Linux-based distributions is [vsFTPd](https://security.appspot.com/vsftpd.html). 


#### Installation

```shell-session
sudo apt install vsftpd 
```


#### Configuration file

The default configuration of vsFTPd can be found in `/etc/vsftpd.conf`.


|**Setting**|**Description**|
|---|---|
|`listen=NO`|Run from inetd or as a standalone daemon?|
|`listen_ipv6=YES`|Listen on IPv6 ?|
|`anonymous_enable=NO`|Enable Anonymous access?|
|`local_enable=YES`|Allow local users to login?|
|`dirmessage_enable=YES`|Display active directory messages when users go into certain directories?|
|`use_localtime=YES`|Use local time?|
|`xferlog_enable=YES`|Activate logging of uploads/downloads?|
|`connect_from_port_20=YES`|Connect from port 20?|
|`secure_chroot_dir=/var/run/vsftpd/empty`|Name of an empty directory|
|`pam_service_name=vsftpd`|This string is the name of the PAM service vsftpd will use.|
|`rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem`|The last three options specify the location of the RSA certificate to use for SSL encrypted connections.|
|`rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key`||
|`ssl_enable=NO`||

In addition, there is a file called `/etc/ftpusers` that we also need to pay attention to, as this file is used to deny certain users access to the FTP service. 

