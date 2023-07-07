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

the [Invoke-AESEncryption.ps1](https://www.powershellgallery.com/packages/DRTools/4.0.2.3/Content/Functions%5CInvoke-AESEncryption.ps1) PowerShell script

Import Module Invoke-AESEncryption.ps1

After the script has been transferred, it only needs to be imported as a module, as shown below.

```powershell-session
PS C:\htb> Import-Module .\Invoke-AESEncryption.ps1
```

After the script is imported, it can encrypt strings or files:

```powershell-session
# Encrypts the string "Secret Test" and outputs a Base64 encoded ciphertext
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Text "Secret Text" 

# Encrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin

# Encrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin.aes

# Decrypts the Base64 encoded string "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs=" and outputs plain text.
Invoke-AESEncryption -Mode Decrypt -Key "p@ssw0rd" -Text "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs="
```