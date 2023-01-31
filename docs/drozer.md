---
title: drozer - A security testing framework for Android
author: amandaguglieri
draft: false
TableOfContents: true
tag: mobile pentesting
---

# drozer - A security testing framework for Android

drozer (formerly Mercury) is the leading security testing framework for Android.

drozer allows you to search for security vulnerabilities in apps and devices by assuming the role of an app and interacting with the Dalvik VM, other apps' IPC endpoints and the underlying OS.

drozer provides tools to help you use, share and understand public Android exploits. It helps you to deploy a drozer Agent to a device through exploitation or social engineering.

## Installation

Instructions from: https://github.com/WithSecureLabs/drozer

Also, you can download it from: https://github.com/FSecureLABS/drozer/releases/download/2.3.4/drozer-agent-2.3.4.apk

```bash
adb install drozer-agent-2.3.4.apk
pip install twisted
```

**Prerequisites**: JDK 1.6, python2.7, Android SDK, adb, java 1.6.

Note: Java 1.6 is mandatory since Android bytecode is only compliant to version 1.6 and no higher.

1. Install genymotion and get a device, for instance a samsung galaxy S6, running in the virtualbox.
2. Go to drozer app ant turn on servers. You will get a message on the app saying that port 31415 is now on.
3. From the terminal, we redirect the port with:
```bash
adb connect IPDevice:PORT
adb forward tcp:31415 tcp:31415
```
4. No we connect to drozer console:
```bash
drozer console connect
```

For this to work, we need to have: 

+ device set on Host-Only + Nat mode.
+ Kali set on Host-Only + Nat mode.

Also, connections need to be running on the same interfaces (eth**n**).


## Basic commands

These commands run on a drozer terminal:

```drozer
# Display the apps installed on the device.
run app.package.list

# Display only the apps with identifier lala
run app.package.list -f lala

# Log debug information
log.d

# Log system information
log.i

# Log error information
log.e

```

### Basic commands on packages

```
# Display available commands.
run + TAB

# Show the manifest of a given app.
run app.package.manifest nameOfApp

# Show generic information about the app
run app.package.info -a nameOfApp

# Display surface, a resume of activities, component providers, services, exported activities and if it is debugable.
run app.package.attacksurface nameOfApp
```

### Basic commands on activities

```
# Show generic information about the activities
run app.activity.info -a nameOfApp

# Display an activity on a device
run app.activity.start --component nameOfApp nameOfApp.nameOfActivity
```

### Basic commands on providers


```
# Display existing providers.
run app.provider.info -a nameOfApp

# Display the location of providers. It uses content:// protocol
run app.providers.finduri nameOfApp

# Display the database information of the provider.
run app.provider.query uriOfProvider
```

### Basic commands on scanners


```
# To see all tests and scans you can run with drozer on your app.
run scanner. +TAB

# Test the app to see if it is vulnerable to an injection.
run scanner.provider.injection -a nameOfApp

# Check out if the App is vulnerable to a traversal attack
run scanner.provider.traversal -a nameOfApp
```

