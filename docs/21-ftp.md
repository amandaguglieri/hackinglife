---
title: "21 ftp"
author: amandaguglieri
draft: false
TableOfContents: true
---

# 21 ftp

The File Transfer Protocol (FTP) is a standard communication protocol used to transfer computer files from a server to a client on a computer network. FTP is built on a client–server model architecture using separate control and data connections between the client and the server. FTP users may authenticate themselves with a clear-text sign-in protocol, generally in the form of a username and password. However, they can connect anonymously if the server is configured to allow it. For secure transmission that protects the username and password and encrypts the content, FTP is often secured with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP).

The Wiki article shows that it is considered non-standard for FTP to be used without the encryption layer provided by protocols such as SSL/TLS (FTPS) or SSH-tunneling (SFTP). FTP by itself does have the ability to require credentials before allowing access to the stored files. However, the deficiency here is that traffic containing said files can be intercepted with what is known as a Man-in-the-Middle Attack (MitM). The contents of the files can be read in plaintext (meaning unencrypted, human-readable form).

However, if the network administrators choose to wrap the connection with the SSL/TLS protocol or tunnel the FTP connection through SSH (as shown below) to add a layer of encryption that only the source and destination hosts can decrypt, this would successfully foil most Man-in-the-Middle attacks. Notice how port 21 has disappeared, as the FTP protocol gets moved under the SSH protocol on port 22, thus being tunneled through it and secured against any interception.

## Attacking a misconfigured FTP service:

You may need to install ftp service. Run:

```bash
sudo apt install ftp -y
```

Then to connect with ftp, run:

```bash
ftp <IP> 
```

The prompt will ask us for the username we want to log in with. Here is where the magic happens. A typical misconfiguration for running FTP services allows an anonymous account to access the service like any other authenticated user. The anonymous username can be input when the prompt appears, followed by any password whatsoever since the service will disregard the password for this specific account.
