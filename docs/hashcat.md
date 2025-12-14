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

Official documentation: https://hashcat.net/wiki/doku.php?id=rule_based_attack


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

Where is the hashcat.potfile?

```
~/.local/share/hashcat/hashcat.potfile
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

```shell-session
ls /usr/share/hashcat/rules/
```

**One of the most used rules is `best64.rule`, which can often lead to good results.**

You can create rules by creating a file called custom.rule and using these commands: [https://hashcat.net/wiki/doku.php?id=rule_based_attack](https://hashcat.net/wiki/doku.php?id=rule_based_attack).

**1.** Let's have a look at an example of a custom.rule:

```
:
c
so0
c so0
sa@
c sa@
c sa@ so0
$!
$! c
$! so0
$! sa@
$! c so0
$! c sa@
$! so0 sa@
$! c so0 sa@
```

whereas, 

| **Function** | **Description**                                   |
| ------------ | ------------------------------------------------- |
| `:`          | Do nothing.                                       |
| `l`          | Lowercase all letters.                            |
| `u`          | Uppercase all letters.                            |
| `c`          | Capitalize the first letter and lowercase others. |
| `sXY`        | Replace all instances of X with Y.                |
| `$!`         | Add the exclamation character at the end.         |

**2.** Generate a mutate password list based on a custom.rule:

```bash
hashcat --force password.list -r custom.rule --stdout > mutated_password.list
```

Hashcat will apply the rules of `custom.rule` for each word in `password.list` and store the mutated version in our `mut_password.list` accordingly.

**3.** After that use the flag -r to be able to use the rule created:

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

- `1000` - Crack NTLM hash.
- `1100` - Crack DCC hash.
- `5500` - Crack Net-NTLMv1
- `5600` - Crack Net-NTLMv2
- `13100` - Crack Kerberoast(ed) hash.
- `27100` - Crack Net-NTLMv2 to an NTLM hash.



### Module 400:  phpass, WordPress (MD5),  Joomla (MD5)

The WordPress password hasher implements the [Portable PHP password hashing framework](http://www.openwall.com/phpass/), which is used in Content Management Systems like WordPress and Drupal. They used to use MD5 in the older versions, but thankfully, no more. You can generate hashes using this encryption scheme at

Crack with hashcat:

```shell-session
hashcat -m 400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```


### Module 500:  MD5 Hashes

```shell-session
hashcat -m 500 -a 0 md5-hashes.list /usr/share/wordlists/rockyou.txt
```

### Module 1000: NTLM hash

```bash
hashcat -m 1000 -a 0 hashes.txt /path/to/wordlist.txt`
#  `-m 1000`: Specifies that the hash type is NTLM.
#  `-a 0`: The attack mode (`0` is a dictionary attack).
# `hashes.txt`: The file containing your NTLM hash.
# `/path/to/wordlist.txt`: The path to your wordlist (for example,  /usr/share/wordlists/rockyou.txt`).
```


### Module 1800: unshadow file


```bash
hashcat -m 1800 -a 0 /tmp/unshadowed.hashes rockyou.txt -o /tmp/unshadowed.cracked
```


### Module 2100: mscache, Cached Domain Credentials

They can be obtained, for instance from mimikatz:

```
.\mimikatz.exe

privilege::debug
lsadump::cache
```

To crack mscache with hashcat, it should be in the following format:

```
$DCC2$10240#username#hash
```

```
hashcat -m2100 '$DCC2$10240#spot#3407de6ff2f044ab21711a394d85f3b8' /usr/share/wordlists/rockyou.txt --force --potfile-disable
```


### Module 5600: netNTLMv2

All saved Hashes are located in [Responder](responder.md)'s logs directory (/usr/share/responder/logs/). We can copy the hash to a file and attempt to crack it using the hashcat module 5600.

```shell-session
hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
```

### Module 7300: IPMI

For cracking hashes from [IPMI service](623-1900-intelligent-platform-management-interface-ipmi.md):
In the event of an HP iLO using a factory default password, we can use this Hashcat mask attack command 

```bash
hashcat -m 7300 ipmi.txt -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u
```


### Module 13100: kerberos RC4

```bash
hashcat -m 13100 rc4_to_crack /usr/share/wordlists/rockyou.txt 
```


### Module 19700: kerberos AES

```bash
hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt 
```

### Module 18200: kerberos asrep

```bash

hashcat -m 18200 asrep /usr/share/wordlists/rockyou.txt 
```


### Module 22100: bitlocker

```bash
hashcat -m 22100 backup.hash /usr/share/wordlists/rockyou.txt -o backup.cracked

cat backup.cracked 
```

