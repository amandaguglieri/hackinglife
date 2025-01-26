---
title: CPTS labs - 06 File Transfers
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 06 File Transfers



## [File Transfers](https://academy.hackthebox.com/module/details/24)

### Windows File Transfer methods

**Download the file flag.txt from the web root using wget from the Pwnbox. Submit the contents of the file as your answer.**

```bash
curl http://$ip:80/flag.txt
```

Results:  b1a4ca918282fcd96004565521944a3b

RDP to 10.129.201.55 (ACADEMY-MISC-MS02) with user "htb-student" and password "HTB_@cademy_stdnt!".
**Upload the attached file named upload_win.zip to the target using the method of your choice. Once uploaded, unzip the archive, and run "hasher upload_win.txt" from the command line. Submit the generated hash as your answer.**

```
# First download the file to your kali. Second, run a server, for instance this PHP server
sudo php -S 0.0.0.0:80

# Launch a RDP connection
xfreerdp /cert:ignore /u:$user /p:$pass /v:$ip

# In the windows machine, open Powershell and retrieve the file:
(New-Object Net.WebClient).DownloadFile('http://$ip/upload_win.zip','C:\Users\htb-student\Desktop\upload_win.zip')

# Unzip it in the Desktop. Open cmd and run:
hasher C:\Users\htb-student\Desktop\upload_win\upload_win.txt
```

Results:  f458303ea783c224c6b4e7ef7f17eb9d


### Linux File Transfer methods

**Download the file flag.txt from the web root using Python from the Pwnbox. Submit the contents of the file as your answer.**

```
wget -O flag.txt http://$ip/flag.txt
```

Results:  5d21cf3da9c0ccb94f709e2559f3ea50

**SSH to 10.129.206.169 (ACADEMY-MISC-NIX04) with user "htb-student" and password "HTB_@cademy_stdnt!". Upload the attached file named upload_nix.zip to the target using the method of your choice. Once uploaded, SSH to the box, extract the file, and run "hasher `<extracted file>`" from the command line. Submit the generated hash as your answer.**

```
scp upload_nix.zip htb-student@$ip:/tmp
# Enter the htb-student password

# Unzip file
python3 -m zipfile -e  upload_nix.zip .
# Or
 gunzip -S .zip upload_nix.zip

# hash it
hasher upload_nix.txt
```

Results:  159cfe5c65054bbadb2761cfa359c8b0


