

## Windows


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

Normal compilation

```bash

```


```bash
gcc -static -O2 50808.c  -o write_anything
```