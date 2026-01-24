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

Benchmarking with hashcat:

```bash
hashcat -b
```

Here, hashcat does not crack real hashes. It runs synthetic hashing workloads and measures hashes per second (H/s) for different algorithms. Basically, it shows how well your CPU or GPU performs.


What hash is it:  [_hash-identifier_](https://www.kali.org/tools/hash-identifier/) or [_hashid_](https://www.kali.org/tools/hashid/)

```

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
| `$l`         | Add the letter `l` at the end                     |

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


Show mutated words: Now, we can use **hashcat** with our wordlist mutation, providing the rule file with **-r**, and **--stdout**, which starts Hashcat in debugging mode. In this mode, Hashcat will not attempt to crack any hashes, but merely display the mutated passwords.


```bash
# Remove words starting with number 1 from the list:
cp /usr/share/wordlists/rockyou.txt > demo.txt
sed -i '/^1/d' demo.txt

# Append the number 1 at the end 
echo \$1 > demo.rule

# Apply the demo.rule to the list demo.txt and print it as output
hashcat -r demo.rule --stdout demo.txt
```

Example:

```
kali@kali:~/passwordattacks$ cat demo1.rule     
$1 c
       
kali@kali:~/passwordattacks$ hashcat -r demo1.rule --stdout demo.txt
Password1
Iloveyou1
Princess1
Rockyou1
Abc1231

kali@kali:~/passwordattacks$ cat demo2.rule   
$1
c

kali@kali:~/passwordattacks$ hashcat -r demo2.rule --stdout demo.txt
password1
Password
iloveyou1
Iloveyou
princess1
Princess
...
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

Find the module:

```bash
hashcat --help | grep -i "KeePass"
```

Output:

```text
13400 | KeePass 1 (AES/Twofish) and KeePass 2 (AES)                | Password Manager
29700 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) - keyfile only mode | Password Manager

```


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

```
$krb5tgs$23$ → RC4-HMAC
```

```bash
hashcat -m 13100 rc4_to_crack /usr/share/wordlists/rockyou.txt 
```



### Module 13400: keepass

Find keepass files:

```powershell
Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue
```

```bash
keepass2john Database.kdbx
```

Output:

```
Database:$keepass$*2*60000*0*682a0e535986c0ab7f02ef294ddfdf869d39bf9e29e17a2d521eb0cdcbd744c0*3d7849d98a8eae59f70b27b1eba401db19dbbae8c095b8be52ef08ffd05a747a*c56d10e5ace50d5924d4b6a9781af20a*947c768ced6729f3741485b9f6ee0737ad70e11933ebdb727c627fe5bc66491a*55de9df220b1d816eb6bad76da248c383a8fde3dbfb2d77e3bb50a25b5ef6133
```

Save as keepass_hash the following:

```text
$keepass$*2*60000*0*682a0e535986c0ab7f02ef294ddfdf869d39bf9e29e17a2d521eb0cdcbd744c0*3d7849d98a8eae59f70b27b1eba401db19dbbae8c095b8be52ef08ffd05a747a*c56d10e5ace50d5924d4b6a9781af20a*947c768ced6729f3741485b9f6ee0737ad70e11933ebdb727c627fe5bc66491a*55de9df220b1d816eb6bad76da248c383a8fde3dbfb2d77e3bb50a25b5ef6133
```

Crack:

```bash
hashcat -m 13400 keepass_hash /usr/share/wordlists/rockyou.txt

```

Output: welcome1

Also: the rule /usr/share/hashcat/rules/rockyou-30000.rule is really helpful sometimes:

```bash
hashcat -m 13400 keepass_hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule 
```


### Module 19600: kerberos AES etype 17


```
$krb5tgs$17$ → AES128-CTS-HMAC-SHA1
```


```bash
hashcat -m 19700 aes_to_crack /usr/share/wordlists/rockyou.txt 
```


### Module 19700: kerberos AES etype 18


```
$krb5tgs$18$ → AES256-CTS-HMAC-SHA1-96
```


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


### Module 22911: SSH crack a id_rsa key 

Pass the key to a key.hash format:

```
/usr/share/john/ssh2john.py id_ana2 > key.hash
```

and then, crack it:

```bash
hashcat -m 22911 key.hash /usr/share/wordlists/rockyou.txt --force
```

If the private key is not rsa, but ecdsa-sha2-* keys or ed25519 keys, use john:

```
/usr/share/john/ssh2john.py id_ana2 > id.hash

john id.hash --wordlist=/usr/share/wordlists/rockyou.txt
```


### Module 22921: SSH crack a id_rsa key 

Pass the key to a key.hash format:

```
/usr/share/john/ssh2john.py id_ana2 > ssh.hash
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

So we will use [johntheripper](john-the-ripper.md).







## Calculating times

To calculate the keyspace needed for cracking a password, we count two things:

- Length of the password.
- Number of different characters we are using.

Then, with a-z and A-Z in a English alphabet we would have 52 different characters:

```
echo -n "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" | wc -c
```

Output:

```text
52
```


For a password of 8 characters, that gives us a keyspace of....

```
python3 -c (print (52**8))
```

Output:

```text
53459728531456
```


**How long then it will take us to  crack a  MD5 hash of a password 8 character long with the lower-case and upper-case of the english alphabet?**

First we benchmark the crack speed with:

```
hashcat -b
```

We will see a long output, but pay attention only to the required one, MD5:

```text
-------------------
* Hash-Mode 0 (MD5)
-------------------

Speed.#1.........:  1519.2 MH/s (5.45ms) @ Accel:1024 Loops:1024 Thr:1 Vec:16

...
```

Now, by knowing that 1 MH/s equals 1,000,000 hashes per second, we can again use Python to calculate CPU and GPU cracking times.

```
# Number of different characters
└─$ echo -n "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" | wc -c 
52
                                                                                    
# Calculate keyspace: number of differen character * password length
└─$ python3 -c (print (52**8))                                                    
53459728531456
                                                                                    
# Calculate time needed by dividing keyspace by MH/s. You will obtain seconds
└─$ python3 -c "print (53459728531456 / 1519200000)"                
35189.39476794102
                                                                                    
# And in minutes
└─$ python3 -c "print (35189.39476794102 / 60)"                                     
586.489912799017
```
