---
title: File Encryption: windows and linux  
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - file encryption
  - windows
  - linux
---


# File Encryption 

## Windows

### Invoke-AESEncryption.ps1 PowerShell script

[Invoke-AESEncryption.ps1](https://www.powershellgallery.com/packages/DRTools/4.0.2.3/Content/Functions%5CInvoke-AESEncryption.ps1) PowerShell script

After the script has been transferred, it only needs to be imported as a module, as shown below.

```powershell-session
PS C:\htb> Import-Module .\Invoke-AESEncryption.ps1
```


This command creates an encrypted file with the same name as the encrypted file but with the extension "`.aes`."
Cheat sheet for encrypting and decrypting files:

```powershell
############
# ENCRYPTION
############
# Encrypts the string "Secret Test" and outputs a Base64 encoded ciphertext
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Text "Secret Text" 

# Encrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin

# Decrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin.aes
```

```powershell
############
# DECRYPTION
############
# Decrypts the Base64 encoded string "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs=" and outputs plain text.
Invoke-AESEncryption -Mode Decrypt -Key "p@ssw0rd" -Text "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs="
```

## Linux

[See openssl](openssl.md)

```bash
# Encrypt a file
openssl enc -aes-256-cbc -iter 100000 -pbkdf2 -in sourceFile.txt -out outputFile.txt.enc
# -iter 100000: Optional. Override the default iterations counts with this option.
# -pbkdf2: Optional. Use the Password-Based Key Derivation Function 2 algorithm.

# Decrypt a file
openssl enc -d -aes-256-cbc -iter 100000 -pbkdf2 -in encryptedFile.enc -out outputFile.txt

# Generate private key
openssl genrsa -aes256 -out private.pem 2048

# Generate public key
openssl rsa -in private.pem -outform PEM -pubout -out public.pem

# Encrypt a file with public key
openssl rsautl -encrypt -inkey public.pem -pubin -in file.txt -out file.enc
# -pubin: Specify the entry parameter

# Decrypt a dile with private key
openssl rsautl -decrypt -inkey private.pem -in file.enc -out file.txt
```