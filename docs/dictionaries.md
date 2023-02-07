---
title: Dictionaries or wordlists resources
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting
---

# Dictionaries

## Lists of my most used dictionaries

| Dictionary | Link | Description | Intended for |
| ---------- | ---- | ----------- | ------------ |
| Dotdotpwn | [https://github.com/wireghoul/dotdotpwn](https://github.com/wireghoul/dotdotpwn) | It's a very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc. | Traversal directory |
| Rockyou | /usr/shared/wordlists/rockyou.txt.gz | RockYou was a company that developed widgets for MySpace and implemented applications for various social networks and Facebook. Since 2014, it has engaged primarily in the purchases of rights to classic video games; it incorporates in-game ads and re-distributes the games.
| User agents | [Seclist](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/User-Agents) | Intended to bypass rate limiting (in an API) | User-agent headers |  



## Installing wordlists in your kali

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

## Dictionary generators

- [crunch](crunch.md).
- [cewl](cewl.md).
- [Common User Password Profiler: CUPP](cupp-common-user-password-profiler.md).


## More dictionaries

- [Dictionaries for cracking passwords: https://wiki.skullsecurity.org/index.php/Passwords](https://wiki.skullsecurity.org/index.php/Passwords).
- [Wordlist from wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist.

