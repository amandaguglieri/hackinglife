---
title: Dictionaries or wordlists resources
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - dictionary
  - tools
---

# Dictionaries

## Lists of my most used dictionaries

| Dictionary                      | Link                                                                                                       | Description                                                                                                                                                                                                                                                                       | Intended for                        |     |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --- |
| Dotdotpwn                       | [https://github.com/wireghoul/dotdotpwn](https://github.com/wireghoul/dotdotpwn)                           | It's a very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc.                                                                                                  | Traversal directory                 |     |
| Payload all the things          | [https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | many different resources and cheat sheets for payload generation and general methodology.                                                                                                                                                                                         |                                     |     |
| Rockyou                         | /usr/shared/wordlists/rockyou.txt.gz                                                                       | RockYou was a company that developed widgets for MySpace and implemented applications for various social networks and Facebook. Since 2014, it has engaged primarily in the purchases of rights to classic video games; it incorporates in-game ads and re-distributes the games. |                                     |     |
| User agents                     | [Seclist](https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/User-Agents)                      | Intended to bypass rate limiting (in an API)                                                                                                                                                                                                                                      | User-agent headers                  |     |
| Windows Files                   | [My dictionaty repo](https://github.com/amandaguglieri/dictionaries/blob/main/windows/file_inclusion)      | To read interesting files from windows machines                                                                                                                                                                                                                                   | Intended for information disclosure |     |
| Default Credential Cheat sheets | [https://github.com/ihebski/DefaultCreds-cheat-sheet](https://github.com/ihebski/DefaultCreds-cheat-sheet) | Install and run `"python3.11 creds search <service>"`                                                                                                                                                                                                                             |                                     |     |
| Insidetruest                    | [Statistically Likelly Usernames](https://github.com/insidetrust/statistically-likely-usernames)           | This resource contains wordlists for creating statistically likely usernames for use in username-enumeration, simulated password-attacks and other security testing tasks.                                                                                                        |                                     |     |


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

## Installing seclist

```shell-session

git clone https://github.com/danielmiessler/SecLists

sudo apt install seclists -y

```

## Dictionary generators

- [crunch](crunch.md).
- [cewl](cewl.md).
- [Common User Password Profiler: CUPP](cupp-common-user-password-profiler.md).
- Username Anarchy.


## More dictionaries

- [Dictionaries for cracking passwords: https://wiki.skullsecurity.org/index.php/Passwords](https://wiki.skullsecurity.org/index.php/Passwords).
- [Wordlist from wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist.

## Default credentials

Install app "Cred" from: [https://github.com/ihebski/DefaultCreds-cheat-sheet](https://github.com/ihebski/DefaultCreds-cheat-sheet)

```bash
pip3 install defaultcreds-cheat-sheet

python3.11 creds search tomcat
```
