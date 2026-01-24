


# adPEAS

Repo: [https://github.com/61106960/adPEAS](https://github.com/61106960/adPEAS)

adPEAS is a Powershell tool to automate Active Directory enumeration. In fact, adPEAS is like a wrapper for different other cool projects like PowerView, PoshADCS, BloodHound stuff and some own written lines of code.

As said, adPEAS is a wrapper for other tools. They are almost all written in pure Powershell but some of them are included as C# code in a compressed binary blob.

adPEAS-Light is a version without Bloodhound and it is more likely that it will not be blocked by an AV solution.

## Install

```bash
git clone https://github.com/61106960/adPEAS.git
```

Now we have adPEAS.ps1


## Basic usage

First you have to load adPEAS in Powershell...

```
Import-Module .\adPEAS.ps1
```

or

```
. .\adPEAS.ps1
```

or

```
gc -raw .\adPEAS.ps1 | iex
```

or

```
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/61106960/adPEAS/main/adPEAS.ps1')
```

Start adPEAS with all enumeration modules and enumerate the domain the logged-on user and computer is connected to.

```
Invoke-adPEAS
```

Start adPEAS with all enumeration modules and enumerate the domain 'contoso.com'. In addition it writes all output without any ANSI color codes to a file.

```
Invoke-adPEAS -Domain 'contoso.com' -Outputfile 'C:\temp\adPEAS_outputfile' -NoColor
```

Start adPEAS with all enumeration modules, enumerate the domain 'contoso.com' and use the domain controller 'dc1.contoso.com' for almost all enumeration requests.

```
Invoke-adPEAS -Domain 'contoso.com' -Server 'dc1.contoso.com'
```

Start adPEAS with all enumeration modules, enumerate the domain 'contoso.com' and use the passed PSCredential object during enumeration.

```
$SecPassword = ConvertTo-SecureString 'Passw0rd1!' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('contoso\johndoe', $SecPassword)
Invoke-adPEAS -Domain 'contoso.com' -Cred $Cred
```

Start adPEAS with all enumeration modules, enumerate the domain 'contoso.com' by using the domain controller 'dc1.contoso.com' and use the username 'contoso\johndoe' with password 'Passw0rd1!' during enumeration. If, due to DNS issues Active Directory detection fails, the switch -Force forces adPEAS to ignore those issues and try to get still as much information as possible.

```
Invoke-adPEAS -Domain 'contoso.com' -Server 'dc1.contoso.com' -Username 'contoso\johndoe' -Password 'Passw0rd1!' -Force
```