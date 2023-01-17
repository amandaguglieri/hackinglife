---
title: Dictionaries or wordlists resources
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting
---

## Lists of my most used dictionaries

- rockyou.txt: /usr/shared/wordlists/rockyou.txt.gz



## Installing wordlist in your kali

```bash
# This package contains the rockyou.txt wordlist and has an installation size of 134 MB.
sudo apt install wordlists
```

You will be adding:

```
/usr/share/wordlists
|-- amass -> /usr/share/amass/wordlists
|-- brutespray -> /usr/share/brutespray/wordlist
|-- dirb -> /usr/share/dirb/wordlists
|-- dirbuster -> /usr/share/dirbuster/wordlists
|-- dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
|-- fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
|-- fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
|-- john.lst -> /usr/share/john/password.lst
|-- legion -> /usr/share/legion/wordlists
|-- metasploit -> /usr/share/metasploit-framework/data/wordlists
|-- nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
|-- rockyou.txt.gz
|-- seclists -> /usr/share/seclists
|-- sqlmap.txt -> /usr/share/sqlmap/data/txt/wordlist.txt
|-- wfuzz -> /usr/share/wfuzz/wordlist
`-- wifite.txt -> /usr/share/dict/wordlist-probable.txt
```

