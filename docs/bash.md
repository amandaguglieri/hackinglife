---
title: bash - Bourne Again Shell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - bash
---

# Bash  - Bourne Again Shell

## File descriptors and redirections
 
```bash
# <<: # This is known as a "here document" or "here-strings" operator. It allows you to input multiple lines of text into a command or a file. Example:
cat << EOF > stream.txt
```

**1.**  `cat`: It is a command used to display the contents of a file.
    
**2.**  `<<`: This is known as a "here document" or "here-strings" operator. It allows you to input multiple lines of text into a command or a file.
    
**3.**  `EOF`: It stands for "End of File" and serves as a delimiter to mark the end of the input. You can choose any other unique string instead of "EOF" as long as it is consistent with the opening and closing delimiter.
    
**4.**  `>`: This is a redirection operator used to redirect the output of a command to a file. In this case, it will create a new file named `stream.txt` or overwrite its contents if it already exists.
    
**5.**  `stream.txt`: It is the name of the file where the input text will be written.


## Shortcuts

+Delete last word CTRL-W
+Fill out the next word that appears in gray: CTRL ->

## Commands

### df

Displays the amount of space available on the file system containing each file name argument.

```bash
df -H
# -H: Print sizes in powers of 1000
# -h: Print sizes in powers of 1024. Humanly readable.
```


### grep

```shell-session
grep -rn /mnt/Finance/ -ie cred
# `grep`: The command used to search text using patterns.
#  `-r`: Recursive search, meaning it will search through all files and subdirectories in `/mnt/Finance/`.
#  `-n`: Displays the line number where the pattern is found within the files.
#  `/mnt/Finance/`: The directory path where the search is performed.
#  `-i`: Makes the search case-insensitive, so it will match "cred", "CRED", "Cred", etc.
#  `-e cred`: Specifies the search pattern `"cred"`. It will search for any occurrence of the string "cred" in the files.
```

### host

host is a simple utility for performing DNS lookups. It is normally used to convert names to IP addresses and vice versa. When no arguments or options are given, host prints a short summary of its command-line arguments and options.

```shell-session
# General syntax
host <name> <server> 

# <name> is the domain name that is to be looked up. It can also be a dotted-decimal IPv4 address or a colon-delimited IPv6 address, in which case host by default performs  a  reverse  lookup  for  that  address.   
# <server>  is  an optional argument which is either the name or IP address of the name server that host should query instead of the server or servers listed in /etc/resolv.conf.
```

Example:

```shell-session
host example.com 8.8.8.8
```

### lsblk 

```bash
# Lists block devices.
lsblk
```

### lsusb

```bash
# Lists USB devices
lsusb
```


### lsof


```bash
# Lists opened files.
lsof
```

### lspci

```bash
# Lists PCI devices.
lspci
```

### lsb_release

Print distribution-specific information

```bash
# Display version, id, description, release and codename of the distro
lsb_release -a 
```


### mount

We need to install `cifs-utils` to connect to an SMB share folder. 

**CIFS** (Common Internet File System) is a protocol used for network file sharing. CIFS is an implementation of the SMB (Server Message Block) protocol, commonly used for sharing files and printers between Windows machines and Linux systems.

To install it:

```
sudo apt install cifs-utils
```

Now mount the file structure:

```shell-session
sudo mkdir /mnt/Finance
sudo mount -t cifs -o username=plaintext,password=Password123,domain=. //$ip/Finance /mnt/Finance
# 
# `mount -t cifs`: Specifies that you are mounting a CIFS (or SMB) file system.
```

As an alternative, we can use a credential file.

```shell-session
mount -t cifs //$ip/Finance /mnt/Finance -o credentials=/path/credentialfile
```

whereas `credentialfile` has to be structured like this:

```txt
username=plaintext
password=Password123
domain=.
```

Once a shared folder is mounted, you can use common Linux tools such as `find` or `grep` to interact with the file structure. 
### netstat

Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships. By default, netstat displays a list of open sockets.  If you don't specify any address families, then the active sockets of all configured address families will be printed.


```bash
netstat -tnlp
# -p: Show  the  PID  and name of the program to which each socket belongs. 
# -l: Show only listening sockets.

# Show networks accessible via VP
netstat -rn
# -r: Display the kernel routing tables. Replacement for netstat -r is "ip route".
# -n: Show numerical addresses instead of trying to determine symbolic host, port or user names.
```
 


### sed 

sed looks for patterns we have defined in the form of regular expressions (regex) and replaces them with another pattern that we have also defined. Let us stick to the last results and say we want to replace the word "bin" with "HTB."

The "s" flag at the beginning stands for the substitute command. Then we specify the pattern we want to replace. After the slash (`/`), we enter the pattern we want to use as a replacement in the third position. Finally, we use the "g" flag, which stands for replacing all matches.

```bash
cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'
```


### ss
Sockets statistic. It can be used to check which ports are listening locally on a given machine.

```bash
ss -ltn
#-l: Display only listening sockets.
#-t: Display TCP sockets.
#-n: Do not try to resolve service name.
```

How many services are listening on the target system on all interfaces? (Not on localhost and IPv4 only):

```bash
ss -l -4 | grep -v "127\.0\.0" | grep "LISTEN" | wc -l
#   **-l**: show only listening services
#   **-4**: show only ipv4
#   **-grep -v "127.0.0"**: exclude all localhost results
#   **-grep "LISTEN"**: better filtering only listening services
#   **wc -l**: count results
```

### uname

```bash
# Print out the kernel release to search for potential kernel exploits quickly.
uname -r


```shell-session
## Flags
 -a, --all
              print all information, in the following order, except omit -p and -i if unknown:
       -s, --kernel-name
              print the kernel name
       -n, --nodename
              print the network node hostname
       -r, --kernel-release
              print the kernel release
       -v, --kernel-version
              print the kernel version
       -m, --machine
              print the machine hardware name
       -p, --processor
              print the processor type (non-portable)
       -i, --hardware-platform
              print the hardware platform (non-portable)
       -o, --operating-system

```


### xrandr

Xrandr is used to set the size, orientation and/or reflection of the outputs for a screen. It can also set the screen size.

```
# See commands and usage
man xrandr

# List current settings
xrandr

# Also, for listing current settings
xrandr --current
```

Listing current settings helps you out to see the name of the outputs of your screens.

In my case:

```shell-session
# Place laptop to the left of DP-2 (27'')
xrandr --output eDP-1  --left-of DP-2

# Place 34'' to the right of DP-2 (27'')
xrandr --output HDMI-1 --right-of DP-2

# Rotate 27''
xrandr --output DP-2  --rotate left 
```

```
xrandr --output  eDP-1 --brightness 0.5
# ranges from 0 to 1
```
