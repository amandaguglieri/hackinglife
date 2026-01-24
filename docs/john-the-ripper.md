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

### Example 1

There is a Python script called [`ssh2john.py`](ssh2john.md) for SSH keys, which generates the corresponding hashes for encrypted SSH keys, which we can then store in files. It's preinstalled in Kali linux:

```shell-session
ssh2john.py SSH.private > ssh.hash
```

Now we can crack the hash with [john the ripper](john-the-ripper.md):

```shell-session
john --wordlist=rockyou.txt ssh.hash
```

Also have a look at [hashcat](hashcat.md) for AES 128/256 and rsa.

### Example 2


Pass the key to a key.hash format:

```
/usr/share/john/ssh2john.py id_rsa > ssh.hash
cat ssh.hash
```

Output:

```text
id_rsa:$sshng$6$16$7059e78a8d3764ea1e883fcdf592feb7$1894$6f70656e7373682d6b65792d7631000000000a6165733235362d6374720000000662637279707400000018000000107059e78a8d3764ea1e883fcdf592feb7000000100000000100000197000000077373682d727361000000030100010000018100efae6dfe87157683772695bba9daf5f40bff961ed5d329a2706a68fa2b704b0718c1464e60d07cc7d39b546f9a89642a36b0536276cfbb06f3b9349f3d7fdfb54d2c21f0a42f87374c7750971ba305931e11a5a9f6ee014a1cee399a5f58fe9e49f31bef98b3aee67c0259b057d5df23936aac7b5e34753dc5c04d4d29c63d49eb02b7d3320e78d391fa80de248d76f10bc1cffd9b27c14b17555b0213ffb4ba83b255e85dc9c9529a3d9952f780e9e11a8ede456968109253e46434cc88f3e3beb7e0b4e6e05ff625628a0057f1cf06316437e6d272d8b285cc6e2832c715ddfc7edfe82a5fc7a61b1b07666003f711cfb5707747eb2389a28b212491cf8e1acb183dd3dd2a0f6f2667f14feb1f10da2c7d1d85a871b573826dc4db2e20d51be5cf55bdcf1384455aca7e3cd274fcb12b1b3a87e2e804e07e4c904ba2220fccb0a8ff829944a51f1ca7c4097256496f89174160ed831f2c4f21e411252f8fb9112deba4c3089ba2983b49d703e7f6bfbbc2b3626964dccd2e51349ec8e4949f0000058018795357c0b4addcc14f32a4c3e90627de0a9cd99324dd0c09daa1aee656a529ec384f6c92eae832807254104104279316076d781e86bf747b37e43ba8606bc1b851c2d0e97d866f48d800e40e741a7c26096b08a7dc2ea5f3b2c891d565d8b6de13c2caa1604d1f44c0bd2bdae221835ec6f7ae3477b179bb8be7ac2a54347eebc2af15636f99fc8b4c454f3c7bf2af9a35acc852d40b5156cb1cd1d30422ba1b766ad4eaec5a0b92e8978c67dc8671d448289a1f39aa156b308b6985bd92bc261eebe10d8537f68bc7645a76242d25c86bf3284de3c803a460b7851c317fdf683bfa52b51f67fccfd14bc34f7e2d9c3a4241204cd183dd34e97f135ccb1e2dab85a864a61cb4618934fa89abd356a0511e7514762e214685d54e42b51abb2a9c94ee037a71da0a42722ad9eb432ab1bf985f5a01d0afa74b370e8d8c85f4d7fdc6bcaad833f508542b3bf3c4a589c8bd5e0ad93b07c7a7c29b5a7b3c41ebb79cb750b15e6331d10d43ee16b3e7258291dcb4297d34cca6e24ba494a21465152112baba1ced9039f6c288395497cca41954dbb3858e13548768998419a9c1fe5089ba18e44b65e72efd40c3394111d2798219063d685f8d5f89cac8f0955bb244019238615ebf438d1adf88c80481aa62a8a9e6c19f4ac4931ab33d0b33d999fb69a8bd725c9feb0110a67d152edbb3435a4cac029c4876b2da87a27070a39cef510706986871649241a7a9731a3a732fa0cbbf468a9da9af4670432d269d1aa334882a0e49d0c5a52f6bae655bcea2b9d39ac30e1f0c30707dd957d98c4a5f757a3ba6667761ccc736ed9b3a2d7f91c784f61a25d8ed70d6e91a7518f2fb379b0bb39cf7881a60498a9b96690d1a45d29d74d54004fc10b9f6b777ac812fb7ee4f9a74f540134870f2865d90dbde765349e0b696b56b31f8a90033029bfb6a5cc927dc3629d867a95bcf95698f4cfcebbccda7e75f1e016500c7738d38ab0a0074ee3e8b29986b2fac8251fa26db3248cff96afd5e32112da221be9aaba7ac9e8d9547cd90bb1e8b1e3594d87c96b4cff829a2d1f850f222a9b7b4bd845e4a43911f7577611536a60824fe4db5ded1e180f350cb978f5fc729c35d1b9221cb0c236178c79e90897d96a0e470406e9dc6fd93c567e89f7a6e5d037e8dcff0746a3a47f5ca41cfa8f4e028edc531695a4d165749bd57413d893c31164d304a4ec68ac15c6502b74d16b34e41a66611f2e61d0cd00e67a18e496ad8a11cf12ac1b6bed55e26112b2c9ec7ef4962c0e01e8d472b9387759b2ba2fab1ef865a6971d6f9e49c119bc4390e68ef0dd877419e9a7f2c5332656de9f3186e6f1e97ab4a0f91872ada83050d9db3e312c795890b417293bb9a151e34e05d9f4334e6794e91704e71763f2bdc0e21bf0f5dacbcd77914f6de4c70884e67f2461010bee568cf77ce32c32f5533d6d8a3e790e10f593e6bb778b027a1ed7698d1df545411b66c2027809f005e6ae036ec83e7c337a3c2eddaf967e195b464e18d6807123ed94aaf28431f7b2c62310acaf3893dc9b0d6b21e6baa6683302b8b3a311d658564525f395f882fd4d57e2232dc706c12b3354801c8a9886f1b52b17b11677d1c86d6cc037a51d7da28c8204e6e9978482a4fa816a3aeea492adc388d8f2b2f906a955e019dc178c4be6a6c06fdbbfb0084ca68ce786db4c2e9b00b4a4f842ae73c29c5581dbd1ffcbe0e4fddac5179465974e665c3ba2a4fdf1ef5aebb271f385c5a267cb5686fe1539296ea53b292cc70a04b048c99b91640d5b0f93df0817cef28d2ea1d04df2e09dab65d8660745b8248bb9c6b13de2d36f054db2897b33a194e10f0a492f3eaae1c7b73759594e3f1a5808f941e882d19f3beec856c7db925b515c76f648ab256f6f21fe61cce53bbf393c867ef8c8adf4e93cfd23dfb89408462fb60e97b910a69740ee952743d679017a32cfeadfb412288b183df308632$16$486

```


```bash
hashcat -h | grep -i "ssh"
```


Output:

```text
   6700 | AIX {ssha1}                                                | Operating System
   6400 | AIX {ssha256}                                              | Operating System
   6500 | AIX {ssha512}                                              | Operating System
   1411 | SSHA-256(Base64), LDAP {SSHA256}                           | FTP, HTTP, SMTP, LDAP Server
   1711 | SSHA-512(Base64), LDAP {SSHA512}                           | FTP, HTTP, SMTP, LDAP Server
    111 | nsldaps, SSHA-1(Base64), Netscape LDAP SSHA                | FTP, HTTP, SMTP, LDAP Server
  10300 | SAP CODVN H (PWDSALTEDHASH) iSSHA-1                        | Enterprise Application Software (EAS)
  22911 | RSA/DSA/EC/OpenSSH Private Keys ($0$)                      | Private Key
  22921 | RSA/DSA/EC/OpenSSH Private Keys ($6$)                      | Private Key
  22931 | RSA/DSA/EC/OpenSSH Private Keys ($1, $3$)                  | Private Key
  22941 | RSA/DSA/EC/OpenSSH Private Keys ($4$)                      | Private Key
  22951 | RSA/DSA/EC/OpenSSH Private Keys ($5$)                      | Private Key
```

`$6$` signifies [_SHA-512_](https://en.wikipedia.org/wiki/SHA-2).

and then, crack it:

```bash
hashcat -m 22921 ssh.hash /usr/share/wordlists/rockyou.txt --force
```

But it returns:

```
Hashfile 'ssh.hash' on line 1 ($sshng...cfeadfb412288b183df308632$16$486): Token length exception

```

So we will use [johntheripper]().

Create a rule that matches the requested rules, like ssh.rule containing:

```txt
[List.Rules:sshRules]
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#
```

Create a list of passwords indicated by user david, like ssh.passwords, containing:

```text
Window
rickc137
dave
superdave
megadave
umbrella
```

For using a rule: To be able to use a rule in John, we need to add a name for the rules and append them to the **/etc/john/john.conf** configuration file. For this demonstration, we'll name the rule **sshRules** with a "List.Rules" rule naming syntax (as shown in Listing 34). We'll use **sudo** and **sh -c** to append the contents of our rule file into **/etc/john/john.conf**.

```
cat ssh.rule
[List.Rules:sshRules]
c $1 $3 $7 $!
c $1 $3 $7 $@
c $1 $3 $7 $#

kali@kali:~/passwordattacks$ sudo sh -c 'cat /home/kali/passwordattacks/ssh.rule >> /etc/john/john.conf'
```

And now:

```bash
john --wordlist=ssh.passwords --rules=sshRules ssh.hash
```


## Cracking PDFs protected file

```bash
pdf2john.py PDF.pdf > pdf.hash
john --wordlist=rockyou.txt pdf.hash
```
