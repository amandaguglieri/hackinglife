---
title: "Crack  sensitive files: Linux"
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - cracking
  - tool
---
# Crack  sensitive files: Linux

## Hunting for Encoded Files

```shell-session
for ext in $(echo ".xls .xls* .xltx .csv .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done
```


## Crack ssh key with ssh2john.py

```shell-session
grep -rnw "PRIVATE KEY" /* 2>/dev/null | grep ":1"
```

Most SSH keys we will find nowadays are encrypted. We can recognize this by the header of the SSH key because this shows the encryption method in use.

```shell-session
cat /home/cry0l1t3/.ssh/SSH.private

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2109D25CC91F8DBFCEB0F7589066B2CC

8Uboy0afrTahejVGmB7kgvxkqJLOczb1I0/hEzPU1leCqhCKBlxYldM2s65jhflD
4/OH4ENhU7qpJ62KlrnZhFX8UwYBmebNDvG12oE7i21hB/9UqZmmHktjD3+OYTsD
...SNIP...
```

encrypted SSH keys are protected with a passphrase that must be entered before use. However, many are often careless in the password selection and its complexity because SSH is considered a secure protocol, and many do not know that even lightweight [AES-128-CBC](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) can be cracked.


There is a Python script called [`ssh2john.py`](ssh2john.md) for SSH keys, which generates the corresponding hashes for encrypted SSH keys, which we can then store in files. It's preinstalled in Kali linux:

```shell-session
ssh2john.py SSH.private > ssh.hash
```

Now we can crack the hash with [johntheripper](john-the-ripper.md):

```shell-session
john --wordlist=rockyou.txt ssh.hash
```


## Crack password of Microsoft Word file

The `office2john` script is preinstalled in kali linux:

```
office2john MS_Word_Document.docx > hash
office2john 'Important Document.docx' > /home/lala/CPTS/hash
cat hash
john --wordlist=/root/Desktop/wordlists/1000000-password-seclists.txt hash
```


## Cracking PDFs protected file

```bash
pdf2john.py PDF.pdf > pdf.hash
john --wordlist=rockyou.txt pdf.hash
```

## Cracking password of a zip file

List compressed files:

```shell-session
curl -s https://fileinfo.com/filetypes/compressed | html2text | awk '{print tolower($1)}' | grep "\." | tee -a compressed_ext.txt
```

```bash
zip2john nameoffile.zip > zip.hashes
cat zip.hashes
john --wordlist=rockyou.txt zip.hashes
```


## Cracking OpenSSL Encrypted Archives

`openssl` can be used to encrypt the `gzip` format.

Checking file format and encryption:

```shell-session
file filename.gzip 

# Output:
# filename.gzip: openssl enc'd data with salted password
```

Extract files with `openssl` in a `for loop`:

```shell-session
for i in $(cat rockyou.txt);do openssl enc -aes-256-cbc -d -in GZIP.gzip -k $i 2>/dev/null| tar xz;done
```

Once the for-loop has finished, we can look in the current folder again to check if the cracking of the archive was successful.

## Cracking BitLocker Encrypted Drives

[BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-device-encryption-overview-windows-10) is an encryption program for entire partitions and external drives. Microsoft developed it for the Windows operating system. It has been available since Windows Vista and uses the `AES` encryption algorithm with 128-bit or 256-bit length.

The recovery key is a 48-digit string of numbers generated during BitLocker setup that also can be brute-forced.

We can use a script called `bitlocker2john` to extract the hash we need to crack:


```shell-session
bitlocker2john -i Backup.vhd > backup.hashes
grep "bitlocker\$0" backup.hashes > backup.hash
```

Using hashcat:

```shell-session
hashcat -m 22100 backup.hash /usr/share/wordlists/rockyou.txt -o backup.cracked


cat backup.cracked 
```

Once we have cracked the password, we will be able to open the encrypted drives. The easiest way to mount a BitLocker encrypted virtual drive is to transfer it to a Windows system and mount it.

To do this, we only have to double-click on the virtual drive. Since it is password protected, Windows will show us an error. After mounting, we can again double-click BitLocker to prompt us for the password.

