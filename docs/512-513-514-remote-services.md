---
title: Ports 512, 513, 514 - Remote Execution (REXEC) services
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - r-services
---
# Ports 512, 513, 514 - Remote services


R-services span across the ports 512, 513, and 514 and are only accessible through a suite of programs known as r-commands. R-Services are a suite of services hosted to enable remote access or issue commands between Unix hosts over TCP/IP.

r-services were the de facto standard for remote access between Unix operating systems until they were replaced by the Secure Shell (SSH) protocols and commands due to inherent security flaws built into them. They are most commonly used by commercial operating systems such as Solaris, HP-UX, and AIX. While less common nowadays, we do run into them from time to time.

The [R-commands](https://en.wikipedia.org/wiki/Berkeley_r-commands) suite consists of the following programs:

- rcp (`remote copy`)
- rexec (`remote execution`)
- rlogin (`remote login`)
- rsh (`remote shell`)
- rstat
- ruptime
- rwho (`remote who`).

These are the most frequently abused commands:

| **Command** | **Service Daemon** | **Port** | **Transport Protocol** | **Description**                                                                                                                                                                                                                                                            |
| ----------- | ------------------ | -------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rcp`       | `rshd`             | 514      | TCP                    | Copy a file or directory bidirectionally from the local system to the remote system (or vice versa) or from one remote system to another. It works like the `cp` command on Linux but provides `no warning to the user for overwriting existing files on a system`.        |
| `rsh`       | `rshd`             | 514      | TCP                    | Opens a shell on a remote machine without a login procedure. Relies upon the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files for validation.                                                                                                                 |
| `rexec`     | `rexecd`           | 512      | TCP                    | Enables a user to run shell commands on a remote machine. Requires authentication through the use of a `username` and `password` through an unencrypted network socket. Authentication is overridden by the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files. |
| `rlogin`    | `rlogind`          | 513      | TCP                    | Enables a user to log in to a remote host over the network. It works similarly to `telnet` but can only connect to Unix-like hosts. Authentication is overridden by the trusted entries in the `/etc/hosts.equiv` and `.rhosts` files.                                     |

The /etc/hosts.equiv file contains a list of trusted hosts and it is used to grant access to other systems on the network.

## Footprinting r-services

```bash
sudo nmap -sV -p 512,513,514 $ip
```

## Accessing the service

```bash
# Login 
rlogin $ip -l <username>

# list all interactive sessions on the local network by sending requests to the UDP port 513
rwho

#  detailed account of all logged-in users over the network, including information such as the username, hostname of the accessed machine, TTY that the user is logged in to, the date and time the user logged in, the amount of time since the user typed on the keyboard, and the remote host they logged in from (if applicable).
rusers -al $ip
```


## Bypass  authentication via `/etc/hosts.equiv` and `.rhosts` files 

The `hosts.equiv` file is recognized as the global configuration regarding all users on a system, whereas `.rhosts` provides a per-user configuration.

Even though, these r-services utilize [Pluggable Authentication Modules (PAM)](https://web.mit.edu/rhel-doc/5/RHEL-5-manual/Deployment_Guide-en-US/ch-pam.html) for user authentication onto a remote system by default, they also bypass this authentication through the use of the `/etc/hosts.equiv` and `.rhosts` files on the system.

If any misconfiguration exists on those files, we could get access to those services.

```shell-session
# Example of a misconfiguration in rhosts file:

htb-student     10.0.17.5
+               10.0.17.10
+               +

# The file follows the specific syntax of `<username> <ip address>` or `<username> <hostname>` pairs. Additionally, the `+` modifier can be used within these files as a wildcard to specify anything. In this example, the `+` modifier allows any external user to access r-commands from the `htb-student` user account via the host with the IP address `10.0.17.10`.
```
