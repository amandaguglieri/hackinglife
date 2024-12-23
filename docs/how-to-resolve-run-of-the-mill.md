---
title: How to resolve run of the mill...
author: amandaguglieri
TableOfContents: true
draft: false
tags:
  - dns
  - ping
  - connection
  - problems
---
# How to resolve run-of-the-mill 

## ... connection problems

```bash
# Check connection
ping 8.8.8.8

# Check domain resolver
ping google.com

# If pinging 8.8.8.8 works but pinging google.com doesn't, check dns file resolver
	# Add a new line: 
	# nameserver 8.8.8.8
sudo nano /etc/resolv.conf

# Check wired connections
sudo service networking
```

### Prevent /etc/resolv.conf from updating

By default, NetworkManager  dynamically updates the `/etc/resolv.conf` file with the DNS settings from active NetworkManager connection profiles. However, you can disable this behavior and manually configure DNS settings in `/etc/resolv.conf`. Steps:

**1.**  As the root user, create the `/etc/NetworkManager/conf.d/90-dns-none.conf` file with the following content by using a text editor:

```
[main]
dns=none
```

**2.**  Reload the NetworkManager service:

```
systemctl reload NetworkManager
```    

 After you reload the service, NetworkManager no longer updates the `/etc/resolv.conf` file. However, the last contents of the file are preserved.
   
**3.**  Optionally, remove the "Generated by NetworkManager" comment from /etc/resolv.conf to avoid confusion.


**Verification**

**1.**  Edit the /etc/resolv.conf file and manually update the configuration.

**2.**  Reload the NetworkManager service:
   
```
systemctl reload NetworkManager
````   

**3.**  Display the /etc/resolv.conf file:

```
cat /etc/resolv.conf
```

 If you successfully disabled DNS processing, NetworkManager did not override the manually configured settings.


## ...issues with screen monitors

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



## ... issues with monitor recognized but not displayed

Weird key sequence:

Ctrl-Alt-F3, Ctrl-Alt-F7
