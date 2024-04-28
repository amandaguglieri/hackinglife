---
title: Android Debug Bridge - ADB 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mobile pentesting 
---

# Android Debug Bridge - ADB

ADB or Android Debug Bridge is a command-line tool developed to facilitate communication between a computer and a connected emulator or Android device. ADB works with the aid of three components called Client, Daemon, and Server.

- **Client**: It’s is very computer on which you use a command-line terminal to issue an ADB command. which sends commands.
- **Daemon**: Or, ADBD is a background process that runs on both connected devices. It’s responsible for running commands on a connected emulator or Android device.
- **Server**: It runs in the background and works as a bridge between the Client and the Daemon and manages the communication. which manages communication between the client and the daemon.


## Basic commands


```bash
# Activate remote shell command console on the connected Android smartphone or tablet.
adb shell

# List Android devices connected to your computer
adb devices
# -l: to list devices by model or product number

# Connect to device
adb connect

# List Android devices connected and emulators in your computer
show devices

# Remove a package
pm uninstall --user 0 com.package.name

# Remove a package but leave app data 
pm uninstall -k --user 0 com.package.name
# -k: Keep the app data and cache after package removal

# Reinstall an uninstalled system app
cmd package install-existing com.package.name
```

## Howtos

- [Remove bloatware from android device](remove-bloatware.md).
