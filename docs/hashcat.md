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



## Modules

One of the most difficult parts is setting the mode. See [https://hashcat.net/wiki/doku.php?id=example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes).

One common error is:

```
Approaching final keyspace - workload adjusted.           
Session..........: hashcat                                
Status...........: Exhausted

```


To fix this, you can use the flag '-w', which is used to set the workload profile. The -w 3 flag specifically sets the workload profile to "Insane."


## Rules

Located at:  `/usr/share/hashcat/rules/`.

You can create rules by creating a file called custom.rule and using these commands: [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack).

After that use the flag -r to be able to use the rule created:

```bash
hashcat -m 0 -a 0 -D2 example0.hash example.dict -r rules/custom.rule

S  
# By clicking s you can check at any time the status
```

Generate a mutate password list based on a custom.rule:

```bash
hashcat --force password.list -r custom.rule --stdout > mutated_password.list
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
?c = Capitalize the first letter and lowercase others
?sXY = Replace all instances of X with Y.
?b = 0x00 - 0xff
?$! 	Add the exclamation character at the end.
``` 

Hashcat will apply the rules of custom.rule for each word in password.list and store the mutated version in our mut_password.list accordingly. 

**Example of a mask attack**:

```bash
hashcat -m 0 -a 3 example0.hash ?l?l?l?l?L?l?l?la  
# first 8 letter will be lowercase and the ninth one will be from the all-character pool
```

Hashcat and John come with pre-built rule lists that we can use for our password generating and cracking purposes. One of the most used rules is best64.rule


## Cracking Password of Microsoft Word file

```
cd /root/Desktop/
/usr/share/john/office2john.py MS_Word_Document.docx > hash

cat hash

MS_Word_Document.docx:$office$*2013*100000*256*16*ff2563844faca58a12fc42c5036f9cf8*ffaf52db903dbcb6ac2db4bab6d343ab*c237403ec97e5f68b7be3324a8633c9ff95e0bb44b1efcf798c70271a54336a2

Remove the first part. Hash would be
$office$*2013*100000*256*16*ff2563844faca58a12fc42c5036f9cf8*ffaf52db903dbcb6ac2db4bab6d343ab*c237403ec97e5f68b7be3324a8633c9ff95e0bb44b1efcf798c70271a54336a2

hashcat -a 0 -m 9600 --status hash /root/Desktop/wordlists/1000000-password-seclists.txt --force
# -a 0: dictionary mode
# -m 9600: Set method to MS Office 2013
# --status : Enable automatic update of the status screen
```

## Resources

[Examples: cracking common hashes: https://infosecwriteups.com/cracking-hashes-with-hashcat-2b21c01c18ec](https://infosecwriteups.com/cracking-hashes-with-hashcat-2b21c01c18ec).



## Modules cheatsheet

https://hashcat.net/wiki/doku.php?id=example_hashes

### mode 7300: IPMI

For cracking hashes from [IPMI service](623-1900-intelligent-platform-management-interface-ipmi.md):
In the event of an HP iLO using a factory default password, we can use this Hashcat mask attack command 

```bash
hashcat -m 7300 ipmi.txt -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u
```


### Module 5600

All saved Hashes are located in [Responder](responder.md)'s logs directory (/usr/share/responder/logs/). We can copy the hash to a file and attempt to crack it using the hashcat module 5600.

```shell-session
hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
```

### Mode 1800: unshadow file


```bash
hashcat -m 1800 -a 0 /tmp/unshadowed.hashes rockyou.txt -o /tmp/unshadowed.cracked
```