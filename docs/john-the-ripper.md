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

John the Ripper (JTR or john) is one of those tools that can be used for several things: you can crack a hash and you can crack a file.

## Installation

Download from: [https://www.openwall.com/john/](https://www.openwall.com/john/).

--list=formats  // gives you a list of the formats

## Crack a hash

### Hash: Single Crack Mode attack

```bash
john --format=sha256 hashes_to_crack.txt
# --format=sha256: specifies that the hash format is SHA-256
# hashes_to_crack.txt:  is the file name containing the hashes to be cracked 
```

John will output the cracked passwords to the console and the file "john.pot" (~/.john/john.pot) to the current user's home directory. 

Furthermore, it will continue cracking the remaining hashes in the background, and we can check the progress by running:

```bash
john --show 
```

Cheat sheet:

|**Hash Format**|**Example Command**|**Description**|
|---|---|---|
|afs|`john --format=afs hashes_to_crack.txt`|AFS (Andrew File System) password hashes|
|bfegg|`john --format=bfegg hashes_to_crack.txt`|bfegg hashes used in Eggdrop IRC bots|
|bf|`john --format=bf hashes_to_crack.txt`|Blowfish-based crypt(3) hashes|
|bsdi|`john --format=bsdi hashes_to_crack.txt`|BSDi crypt(3) hashes|
|crypt(3)|`john --format=crypt hashes_to_crack.txt`|Traditional Unix crypt(3) hashes|
|des|`john --format=des hashes_to_crack.txt`|Traditional DES-based crypt(3) hashes|
|dmd5|`john --format=dmd5 hashes_to_crack.txt`|DMD5 (Dragonfly BSD MD5) password hashes|
|dominosec|`john --format=dominosec hashes_to_crack.txt`|IBM Lotus Domino 6/7 password hashes|
|EPiServer SID hashes|`john --format=episerver hashes_to_crack.txt`|EPiServer SID (Security Identifier) password hashes|
|hdaa|`john --format=hdaa hashes_to_crack.txt`|hdaa password hashes used in Openwall GNU/Linux|
|hmac-md5|`john --format=hmac-md5 hashes_to_crack.txt`|hmac-md5 password hashes|
|hmailserver|`john --format=hmailserver hashes_to_crack.txt`|hmailserver password hashes|
|ipb2|`john --format=ipb2 hashes_to_crack.txt`|Invision Power Board 2 password hashes|
|krb4|`john --format=krb4 hashes_to_crack.txt`|Kerberos 4 password hashes|
|krb5|`john --format=krb5 hashes_to_crack.txt`|Kerberos 5 password hashes|
|LM|`john --format=LM hashes_to_crack.txt`|LM (Lan Manager) password hashes|
|lotus5|`john --format=lotus5 hashes_to_crack.txt`|Lotus Notes/Domino 5 password hashes|
|md4-gen|`john --format=md4-gen hashes_to_crack.txt`|Generic MD4 password hashes|
|md5|`john --format=md5 hashes_to_crack.txt`|MD5 password hashes|
|md5-gen|`john --format=md5-gen hashes_to_crack.txt`|Generic MD5 password hashes|
|mscash|`john --format=mscash hashes_to_crack.txt`|MS Cache password hashes|
|mscash2|`john --format=mscash2 hashes_to_crack.txt`|MS Cache v2 password hashes|
|mschapv2|`john --format=mschapv2 hashes_to_crack.txt`|MS CHAP v2 password hashes|
|mskrb5|`john --format=mskrb5 hashes_to_crack.txt`|MS Kerberos 5 password hashes|
|mssql05|`john --format=mssql05 hashes_to_crack.txt`|MS SQL 2005 password hashes|
|mssql|`john --format=mssql hashes_to_crack.txt`|MS SQL password hashes|
|mysql-fast|`john --format=mysql-fast hashes_to_crack.txt`|MySQL fast password hashes|
|mysql|`john --format=mysql hashes_to_crack.txt`|MySQL password hashes|
|mysql-sha1|`john --format=mysql-sha1 hashes_to_crack.txt`|MySQL SHA1 password hashes|
|NETLM|`john --format=netlm hashes_to_crack.txt`|NETLM (NT LAN Manager) password hashes|
|NETLMv2|`john --format=netlmv2 hashes_to_crack.txt`|NETLMv2 (NT LAN Manager version 2) password hashes|
|NETNTLM|`john --format=netntlm hashes_to_crack.txt`|NETNTLM (NT LAN Manager) password hashes|
|NETNTLMv2|`john --format=netntlmv2 hashes_to_crack.txt`|NETNTLMv2 (NT LAN Manager version 2) password hashes|
|NEThalfLM|`john --format=nethalflm hashes_to_crack.txt`|NEThalfLM (NT LAN Manager) password hashes|
|md5ns|`john --format=md5ns hashes_to_crack.txt`|md5ns (MD5 namespace) password hashes|
|nsldap|`john --format=nsldap hashes_to_crack.txt`|nsldap (OpenLDAP SHA) password hashes|
|ssha|`john --format=ssha hashes_to_crack.txt`|ssha (Salted SHA) password hashes|
|NT|`john --format=nt hashes_to_crack.txt`|NT (Windows NT) password hashes|
|openssha|`john --format=openssha hashes_to_crack.txt`|OPENSSH private key password hashes|
|oracle11|`john --format=oracle11 hashes_to_crack.txt`|Oracle 11 password hashes|
|oracle|`john --format=oracle hashes_to_crack.txt`|Oracle password hashes|
|pdf|`john --format=pdf hashes_to_crack.txt`|PDF (Portable Document Format) password hashes|
|phpass-md5|`john --format=phpass-md5 hashes_to_crack.txt`|PHPass-MD5 (Portable PHP password hashing framework) password hashes|
|phps|`john --format=phps hashes_to_crack.txt`|PHPS password hashes|
|pix-md5|`john --format=pix-md5 hashes_to_crack.txt`|Cisco PIX MD5 password hashes|
|po|`john --format=po hashes_to_crack.txt`|Po (Sybase SQL Anywhere) password hashes|
|rar|`john --format=rar hashes_to_crack.txt`|RAR (WinRAR) password hashes|
|raw-md4|`john --format=raw-md4 hashes_to_crack.txt`|Raw MD4 password hashes|
|raw-md5|`john --format=raw-md5 hashes_to_crack.txt`|Raw MD5 password hashes|
|raw-md5-unicode|`john --format=raw-md5-unicode hashes_to_crack.txt`|Raw MD5 Unicode password hashes|
|raw-sha1|`john --format=raw-sha1 hashes_to_crack.txt`|Raw SHA1 password hashes|
|raw-sha224|`john --format=raw-sha224 hashes_to_crack.txt`|Raw SHA224 password hashes|
|raw-sha256|`john --format=raw-sha256 hashes_to_crack.txt`|Raw SHA256 password hashes|
|raw-sha384|`john --format=raw-sha384 hashes_to_crack.txt`|Raw SHA384 password hashes|
|raw-sha512|`john --format=raw-sha512 hashes_to_crack.txt`|Raw SHA512 password hashes|
|salted-sha|`john --format=salted-sha hashes_to_crack.txt`|Salted SHA password hashes|
|sapb|`john --format=sapb hashes_to_crack.txt`|SAP CODVN B (BCODE) password hashes|
|sapg|`john --format=sapg hashes_to_crack.txt`|SAP CODVN G (PASSCODE) password hashes|
|sha1-gen|`john --format=sha1-gen hashes_to_crack.txt`|Generic SHA1 password hashes|
|skey|`john --format=skey hashes_to_crack.txt`|S/Key (One-time password) hashes|
|ssh|`john --format=ssh hashes_to_crack.txt`|SSH (Secure Shell) password hashes|
|sybasease|`john --format=sybasease hashes_to_crack.txt`|Sybase ASE password hashes|
|xsha|`john --format=xsha hashes_to_crack.txt`|xsha (Extended SHA) password hashes|
|zip|`john --format=zip hashes_to_crack.txt`|ZIP (WinZip) password hashes|


###  Hash: Wordlist mode attack

```bash
john --wordlist=<wordlist_file> --rules <hash_file>
```

Multiple wordlists can be specified by separating them with a comma.

John will output the cracked passwords to the console and the file "john.pot" (~/.john/john.pot) to the current user's home directory. 

Furthermore, it will continue cracking the remaining hashes in the background, and we can check the progress by running:

```bash
john --show 
```


### Hash: Incremental mode attack

Incremental Mode is an advanced John mode used to crack passwords using a character set. It is a hybrid attack, which means it will attempt to match the password by trying all possible combinations of characters from the character set. This mode is the most effective yet most time-consuming of all the John modes.

```bash
john --incremental <hash_file>
```

Additionally, it is important to note that the default character set is limited to a-zA-Z0-9. Therefore, if we attempt to crack complex passwords with special characters, we need to use a custom character set.


## Crack a file

For cracking files you have the following tools:

| **Tool**                | **Description**                               |
| ----------------------- | --------------------------------------------- |
| `pdf2john`              | Converts PDF documents for John               |
| `ssh2john`              | Converts SSH private keys for John            |
| `mscash2john`           | Converts MS Cash hashes for John              |
| `keychain2john`         | Converts OS X keychain files for John         |
| `rar2john`              | Converts RAR archives for John                |
| `pfx2john`              | Converts PKCS#12 files for John               |
| `truecrypt_volume2john` | Converts TrueCrypt volumes for John           |
| `keepass2john`          | Converts KeePass databases for John           |
| `vncpcap2john`          | Converts VNC PCAP files for John              |
| `putty2john`            | Converts PuTTY private keys for John          |
| `zip2john`              | Converts ZIP archives for John                |
| `hccap2john`            | Converts WPA/WPA2 handshake captures for John |
| `office2john`           | Converts MS Office documents for John         |
| `wpa2john`              | Converts WPA/WPA2 handshakes for John         |

If you need addional ones, run:

```bash
locate *2john*
```

### Basic usage

```bash
# Syntax. Three steps:
# 1. Extract hash from file
<tool> <file_to_crack> > file.hash
# 2. Crack the hash
john file.hash
# 3. Another way to crack the hash
john --wordlist=<wordlist.txt> file.hash 

# Example with a pdf:
# 1. Extract hash from file
pdf2john server_doc.pdf > server_doc.hash
# 2. Crack the hash
john server_doc.hash
# 3. Another way to crack the hash
john --wordlist=<wordlist.txt> server_doc.hash 
```


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

List compressed files:

```shell-session
curl -s https://fileinfo.com/filetypes/compressed | html2text | awk '{print tolower($1)}' | grep "\." | tee -a compressed_ext.txt
```

```bash
zip2john nameoffile.zip > zip.hashes
cat zip.hashes
john zip.hashes
```

## Cracking a ssh private key

There is a Python script called [`ssh2john.py`](ssh2john.md) for SSH keys, which generates the corresponding hashes for encrypted SSH keys, which we can then store in files. It's preinstalled in Kali linux:

```shell-session
ssh2john.py SSH.private > ssh.hash
```

Now we can crack the hash with [john the ripper](john-the-ripper.md):

```shell-session
john --wordlist=rockyou.txt ssh.hash
```

Also have a look at [hashcat](hashcat.md) for AES 128/256 and rsa.



## Cracking PDFs protected file

```bash
pdf2john.py PDF.pdf > pdf.hash
john --wordlist=rockyou.txt pdf.hash
```
