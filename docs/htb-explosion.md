---
title: Explosion - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---


# Explosion - A HackTheBox machine


```bash
nmap -sC -sV $ip -Pn
```

``PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2023-04-27T10:42:37+00:00
|_ssl-date: 2023-04-27T10:42:45+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=Explosion
| Issuer: commonName=Explosion
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-04-26T10:27:02
| Not valid after:  2023-10-26T10:27:02
| MD5:   2446e544fced2077f37238e35735b16e
| SHA-1: cace39c8a8b0ae2a4bf509705cc78f084b9aec0b
| -----BEGIN CERTIFICATE-----
| MIIC1jCCAb6gAwIBAgIQadtbfAUkgr5BZjE2eNbcBzANBgkqhkiG9w0BAQsFADAU
| MRIwEAYDVQQDEwlFeHBsb3Npb24wHhcNMjMwNDI2MTAyNzAyWhcNMjMxMDI2MTAy
| NzAyWjAUMRIwEAYDVQQDEwlFeHBsb3Npb24wggEiMA0GCSqGSIb3DQEBAQUAA4IB
| DwAwggEKAoIBAQDSS2eXLWZRkoPS26o641YgH94ZMh9lCyaz2qMPhHsbjNGwZSTC
| WY+Pm8nAROk5HTTq0CYHWyKZN7I2dONAG42I6pRWdpV3k5NwTj3wCR7BB1WqL5mB
| CTN7LxfEzngrdU1tPI6FdSkI12I+2h+ckz+2lUaY58+3ENNGe06U82jE8RrEmnFd
| 0Is0UvA3D3ec2Mzr1Ji8LRko3/rMhggn9T5n75Kh0PstZoRdN+XVjcKfazIfhkZb
| Wz0/BXcB5fwfSGOWaKcHIL26IviI8DbgS46d4Ydw0tGWE+8BHt3jizillCueg03v
| TYj4W6d9nqDB1/QmUz9w1tqviUZM7qPCK6qxAgMBAAGjJDAiMBMGA1UdJQQMMAoG
| CCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsFAAOCAQEANyNIxLXD
| ftgW+zs+5JGz2WbeLauLLWE3+LJNfMxGWZr9BJAaF4VX0V/dXP3MXLywhqsz+V56
| mam2jNi44nu4ov+1FgqPKsRdUEb8uOocWEAUE28L48Eh0M09JjVg639REwzqohPV
| KyqdnHhPkCNH3Js8nJCZkAl6EgWJMWLenD0htNTkJHjtHSR0D3Dyc08WsMPmyOtX
| m+4Oi8RS7qrHYG0nCvQmJpvNO9eiqYfVVzP5Q06K45hZ/xlVTVePhJFxdVGcc7CH
| qEILmRdzuvKaRpAD6QocoUm8I3wogOTTV4DcsNOnNSLoFj/TI8i5FV791lZDEzcL
| bWFK5GD+11kCOw==
|_-----END CERTIFICATE-----
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-04-27T10:42:40
|_  start_date: N/A
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 37798/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 6858/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 35582/udp): CLEAN (Timeout)
|   Check 4 (port 50597/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
```

After going through all open ports, running this nmap script on 3389 gives us interesting results:

```bash
nmap -Pn -sV -p3389 --script rdp-* $ip
```

Resolution of machine in [port 3389 tricks](3389-rdp.md).



