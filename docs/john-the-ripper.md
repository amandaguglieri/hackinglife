---
title: John the Ripper - A hash cracker and dictionary attack tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - brute force
  - dictionary attack
  - enumeration
---

# John the Ripper - A hash cracker and dictionary attack tool

John the Ripper is one of those tools that can be used for several things: hash cracker and dictionary attack.

## Installation

Download from: [https://www.openwall.com/john/](https://www.openwall.com/john/).

--list=formats  // gives you a list of the formats

## Basic commands

### Brute forcing /etc/passwd and /etc/shadow

**First**, save /etc/passwd and john /etc/shadow from the victim machine to the attacker machine.

**Second**, use unshadow to put users and passwords in the same file:

```bash
unshadow passwd shadow > crackme
# passwd: file saved with /etc/passwd content.
# shadow: file saved with /etc/shadow content.
```

**Third**, run johtheripper. You can use a list of users or specific ones brute force:

```bash
john -incremental -users:<userList> <fileToCrack>

# To display the passwords recovered:
john --show crackme

# Default path to cracked password: /root/.john/john.pot

# Dictionary attack
john -wordlist=<file> -users=victim1,victim2 -rules <filetocrack>
# -rules parameter adds som mangling to the wordlist
```

## Cracking Password of Microsoft Word file

```
cd /root/Desktop/
/usr/share/john/office2john.py MS_Word_Document.docx > hash
cat hash
john --wordlist=/root/Desktop/wordlists/1000000-password-seclists.txt hash
```

## Cracking password of a zip file

```bash
zip2john nameoffile.zip > zip.hashes
cat zip.hashes
john zip.hashes
```


