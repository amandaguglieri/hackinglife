---
title: ELF Executable Examination
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - binary
  - forensics
---

# ELF Executable Examination

The `octopus_checker` binary (for example) is found on a remote machine during the testing. Running the application locally reveals that it connects to database instances in order to verify that they are available.

```shell-session
./octopus_checker 
```

Output:

```shell-session
Program had started..
Attempting Connection 
Connecting ... 

The driver reported the following diagnostics whilst running SQLDriverConnect

01000:1:0:[unixODBC][Driver Manager]Can't open lib 'ODBC Driver 17 for SQL Server' : file not found
connected
```

We can analyze this binary using tools like [PEDA](https://github.com/longld/peda) (Python Exploit Development Assistance for GDB)

## PEDA  (Python Exploit Development Assistance for GDB)

Install [PEDA](https://github.com/longld/peda) (Python Exploit Development Assistance for GDB):

```
git clone https://github.com/longld/peda.git
```

PEDA uses the standard GNU Debugger (GDB) command line, which is used for debugging C and C++ programs.

GDB is a command line tool that lets you step through the code, set breakpoints, and examine and change variables. Running the following command we can execute the binary through it.

```
gdb ./octopus_checker
```

Output:

```shell-session
GNU gdb (Debian 9.2-1) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./octopus_checker...
(No debugging symbols found in ./octopus_checker)
```

Once the binary is loaded, we set the disassembly-flavor to define the display style of the code, and we proceed with disassembling the main function of the program.

```assembly
gdb-peda$ set disassembly-flavor intel
gdb-peda$ disas main
```

Output:

```assembly
Dump of assembler code for function main:
   0x0000555555555456 <+0>:	endbr64 
   0x000055555555545a <+4>:	push   rbp
   0x000055555555545b <+5>:	mov    rbp,rsp
 
 <SNIP>
 
   0x0000555555555625 <+463>:	call   0x5555555551a0 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>
   0x000055555555562a <+468>:	mov    rdx,rax
   0x000055555555562d <+471>:	mov    rax,QWORD PTR [rip+0x299c]        # 0x555555557fd0
   0x0000555555555634 <+478>:	mov    rsi,rax
   0x0000555555555637 <+481>:	mov    rdi,rdx
   0x000055555555563a <+484>:	call   0x5555555551c0 <_ZNSolsEPFRSoS_E@plt>
   0x000055555555563f <+489>:	mov    rbx,QWORD PTR [rbp-0x4a8]
   0x0000555555555646 <+496>:	lea    rax,[rbp-0x4b7]

 <SNIP>
```

Let's say we are interested in the instruction that aparently does the SQL connection:

```assembly
   0x00005555555555ff <+425>:	mov    esi,0x0
   0x0000555555555604 <+430>:	mov    rdi,rax
   0x0000555555555607 <+433>:	call   0x5555555551b0 <SQLDriverConnect@plt>
   0x000055555555560c <+438>:	add    rsp,0x10
   0x0000555555555610 <+442>:	mov    WORD PTR [rbp-0x4b4],ax
```

Or in the HTB exercise it was:

```
   0x0000000000001607 <+433>:	call   0x11b0 <SQLDriverConnect@plt>
```

which (different from the first option) is a **PLT-relative offset**, **not** an absolute virtual memory address like in the first case. This is important when setting a breaking point.

Setting a breaking point in the first case (with the absolute memory location):

```assembly
gdb-peda$ b *0x5555555551b0
```

But for the option 2 we can set the breakpoint on the _function name_, not the address:

```assembly
gdb-peda$ break SQLDriverConnect
```

Now we run it:

```assembly
gdb-peda$ run
```

And the code will stop there in the breakpoint:

```assembly
Starting program: /home/htb-student/octopus_checker 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Program had started..
Attempting Connection 
[----------------------------------registers-----------------------------------]
RAX: 0x55555556c4f0 --> 0x4b5a ('ZK')
RBX: 0x5555555557d0 (<__libc_csu_init>:	endbr64)
RCX: 0xfffffffd 
RDX: 0x7fffffffdf10 ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost, 1401;UID=SA;PWD=N0tS3cr3t!;")
RSI: 0x0 
RDI: 0x55555556c4f0 --> 0x4b5a ('ZK')
RBP: 0x7fffffffe390 --> 0x0 
RSP: 0x7fffffffdeb8 --> 0x55555555560c (<main+438>:	add    rsp,0x10)
RIP: 0x7ffff7d61c20 (<SQLDriverConnect>:	push   r15)
R8 : 0x7fffffffdf70 --> 0x7ffff7d3fec0 --> 0x7ffff7d3f008 --> 0x7ffff7c15c90 (<_ZN10__cxxabiv117__class_type_infoD2Ev>:	endbr64)
R9 : 0x400 
R10: 0xfffffffffffff8ff 
R11: 0x246 
R12: 0x555555555240 (<_start>:	endbr64)
R13: 0x7fffffffe480 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x213 (CARRY parity ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x7ffff7d61c15 <__handle_attr_extensions_cs+149>:	pop    rbp
   0x7ffff7d61c16 <__handle_attr_extensions_cs+150>:	ret    
   0x7ffff7d61c17:	nop    WORD PTR [rax+rax*1+0x0]
=> 0x7ffff7d61c20 <SQLDriverConnect>:	push   r15
   0x7ffff7d61c22 <SQLDriverConnect+2>:	push   r14
   0x7ffff7d61c24 <SQLDriverConnect+4>:	mov    r14d,ecx
   0x7ffff7d61c27 <SQLDriverConnect+7>:	push   r13
   0x7ffff7d61c29 <SQLDriverConnect+9>:	mov    r13,r8
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdeb8 --> 0x55555555560c (<main+438>:	add    rsp,0x10)
0008| 0x7fffffffdec0 --> 0x7fffffffdeda --> 0xb3b0000000000000 
0016| 0x7fffffffdec8 --> 0x0 
0024| 0x7fffffffded0 --> 0x1 
0032| 0x7fffffffded8 --> 0x0 
0040| 0x7fffffffdee0 --> 0x55555556b3b0 --> 0x4b59 ('YK')
0048| 0x7fffffffdee8 --> 0x55555556c4f0 --> 0x4b5a ('ZK')
0056| 0x7fffffffdef0 --> 0x7fffffffe290 --> 0x7ffff7d4cf74 --> 0x2 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, SQLDriverConnect (hdbc=0x55555556c4f0, hwnd=0x0, 
    conn_str_in=0x7fffffffdf10 "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost, 1401;UID=SA;PWD=N0tS3cr3t!;", len_conn_str_in=0xfffd, conn_str_out=0x7fffffffdf70 "\300\376\323\367\377\177", conn_str_out_max=0x400, 
    ptr_conn_str_out=0x7fffffffdeda, driver_completion=0x0) at SQLDriverConnect.c:686
686	SQLDriverConnect.c: No such file or directory.
```


## DLL File Examination

A DLL file is a `Dynamically Linked Library` and it contains code that is called from other programs while they are running. The `MultimasterAPI.dll` binary is found on a remote machine during the enumeration process. Examination of the file reveals that this is a .Net assembly.

