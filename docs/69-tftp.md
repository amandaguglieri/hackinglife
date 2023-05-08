---
title: 69 - tftp 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# 69 - ftpt

Trivial File Transfer Protocol (TFTP) uses UDP port 69 and requires no authentication—clients read from, and write to servers using the datagram format outlined in RFC 1350. Due to deficiencies within the protocol (namely lack of authentication and no transport security), it is uncommon to find servers on the public Internet. Within large internal networks, however, TFTP is used to serve configuration files and ROM images to VoIP handsets and other devices.

You can spot the open port after running a UDP scan. But also, when reading /etc/passwd, you might find service/user tftp. 

Trivial File Transfer Protocol (TFTP) is a simple protocol that provides basic file transfer function with no user authentication. TFTP is intended for applications that do not need the sophisticated interactions that File Transfer Protocol (FTP) provides. 

UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. It is implemented in the transport layer of the OSI Model, known as a fast but not reliable protocol, unlike TCP, which is reliable, but slower then UDP. Just like how TCP contains open ports for protocols such as HTTP, FTP, SSH and etcetera, the same way UDP has ports for protocols that work for UDP.

## Enumeration

```bash
nmap -n -Pn -sU -p69 -sV --script tftp-enum <IP>
```

## Exploitation

You can use Metasploit or Python to check if you can download/upload files:

Module: `auxiliary/admin/tftp/tftp_transfer_util`


Also you can exploit manually. Install tftp client:

```bash
# Installing a tftp server
sudo apt-get install tftpd-hpa

# Installing a tftp client
sudo apt install tftp
```

For available commands: 

```bash
man tftp
```

Upload your [pentesmonkey shell](pentesmonkey.md) with:

```bash
put pentesmonkey.php
```

Where does it get uploaded? Depends. But The default configuration file for tftpd-hpa is /etc/default/tftpd-hpa. The directory is configured there under the parameter `TFTP_DIRECTORY=`
With that information, you can access the directory and from there launch your reverse shell. 


## Related labs

[HackTheBox machine: included](htb-included.md).
