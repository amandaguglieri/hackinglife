---
title: nxc
author: amandaguglieri  
draft: false  
TableOfContents: true  
tags:
- factive directory
---


# Nxc



Generate the krb5.conf file:

```bash
netexec smb frizzdc.frizz.htb -u f.frizzle -p 'Jenni_Luvs_Magic23' -k --generate-krb5-file krb5.conf

```

Example from [HackTheBox machine The Frizz](htb-thefrizz.md)


## Installation

```bash
# Install within you pyenv environment, in my case tooling
pyenv activate tooling
pip install git+https://github.com/Pennyw0rth/NetExec.git    

# Once installed, remember to remove cache locations for commands
hash -r

# and now it's ready to be used within your env
```

## Basic commands

**Why using an env version of the netExec???** I've notice that some features of the preinstalled version of netExec in kali don't work properly. For instance, creating a TGT the tag --generate-tgt is not recognized.

```bash
####
# Generate TGT
netexec smb ip -u user -p password --generate-tgt /path

export KRB5CCNAME=/path

# use TGT
netexec smb ip -u user -k --use-kcache


######
# Generate krb5.conf file
netexec smb ip -u user -p password --generate-krb5-file /path
export KRB5_CONFIG=/path


### 
# Execute commands
netexec smb ip -d corp.com -u user -p password  -x "type c:\Users\Administrator\Desktop\flag.txt"
 
#### 
# List the shares
netexec smb ip -d corp.com -u user -p password  --shares 
 
 







```