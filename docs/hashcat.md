---
title: Hashcat - A password recovery tool
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - enumeration
  - cracking tool
---

# Hashcat - A password recovery tool

**Hashcat** is a password recovery tool. It had a proprietary code base until 2015, but was then released as open source software. Versions are available for Linux, OS X, and Windows. Wikipedia

## Installation

Download from: [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/).

## Basic commands

```bash
# Get help 
hashcat -help 

# To crack a hash with a dictionary
hashcat -m 0 -a 0 -D2 example0.hash example.dict
# -m:  to specify the module of the algorithm we’ll be running. Then -m 0 specifies an MD5 type of hash
# -a: type of attack. Then -a 0 is a dictionary attack
# Results are stored in file hashcat.potfile
```

## Modules cheatsheet

https://hashcat.net/wiki/doku.php?id=example_hashes


## Rules

You can create rules by creating a file called custom.rule and using these commands: [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack).

After that use the flag -r to be able to use the rule created:

```bash
hashcat -m 0 -a 0 -D2 example0.hash example.dict -r rules/custom.rule

S  
# By clicking s you can check at any time the status
```


## Mask attacks 

These are the possible masks that you can use:

```
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?h = 0123456789abcdef
?H = 0123456789ABCDEF
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
?a = ?l?u?d?s
?b = 0x00 - 0xff
``` 

**Example of a mask attack**:

```bash
hashcat -m 0 -a 3 example0.hash ?l?l?l?l?L?l?l?la  
# first 8 letter will be lowercase and the ninth one will be from the all-character pool
```

## Cracking Password of Microsoft Word file

```
cd /root/Desktop/
/usr/share/john/office2john.py MS_Word_Document.docx > hash
cat hash
MS_Word_Document.docx:$office$*2013*100000*256*16*ff2563844faca58a12fc42c5036f9cf8*ffaf52db903dbcb6ac2db4bab6d343ab*c237403ec97e5f68b7be3324a8633c9ff95e0bb44b1efcf798c70271a54336a2

Remove the first part. Hash woul be
$office$*2013*100000*256*16*ff2563844faca58a12fc42c5036f9cf8*ffaf52db903dbcb6ac2db4bab6d343ab*c237403ec97e5f68b7be3324a8633c9ff95e0bb44b1efcf798c70271a54336a2

hashcat -a 0 -m 9600 --status hash /root/Desktop/wordlists/1000000-password-seclists.txt --force
# -a 0: dictionary mode
# -m 9600: Set method to MS Office 2013
# --status : Enable automatic update of the status screen
```

