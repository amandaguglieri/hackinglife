---
title: openSSL - Cryptography and SSL/TLS Toolkit
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - openssl
---

# openSSL - Cryptography and SSL/TLS Toolkit

[openSSL Website](https://www.openssl.org/). 


## Basic usage

```bash
openssl s_client -connect target.site:443
HEAD / HTTP/1.0
```

- Create self signed certificates.
- Encrypt/Decrypt files
- Generate private/public keys.
- Encrypt/Decrypt files with public/private keys.

```bash
# Pwnbox - Create a Self-Signed Certificate
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

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