---
title: apktool
author: amandaguglieri
draft: false
TableOfContents: true
tag: mobile pentesting
---


## Installation

Go to your tool folder and download the tool:

```bash
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.6.0.jar
```

Have the device from genymotion already running on Host-Only mode + NAT.

Have your kali on Host-Only mode + NAT.

Run:

```bash
adb connect <the device Host-Only IP>:5555

#Making sure that genymotion is not using a proxy:
adb shell-settings put global http_proxy :0

# Installing the app
adb install nameOfApp
```

To decompile and see source code:

```bash
java-jar apktool_2.6.0.jar d -s nameOfApp
# d: decompile
# -s: source.
```

When decompiled, a folder is created. If you go into the folder you will see the file classes.dex, which contains the source code. To see it:

```bash
jadx-gui
```


