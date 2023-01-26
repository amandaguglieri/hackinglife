---
title: Virtualbox and Extension Pack
author: amandaguglieri
draft: false
TableOfContents: true
tag: windows, bypass techniques
---

# VirtualBox and Extension Pack

How to install the Extension Pack manually, bypassing possible policies existing in a Windows DC.

1. The .vbox-extpack file that can be downloaded. Actually, it is just a .tar.gz archive so its contents can be unpacked. 

2. Place these contents in subdirectory ExtensionPacks of the VirtualBox installation directory, tipically C:\Program Files\Oracle\VirtualBox

3. That's it. Run Virtualbox and click on Install extension in the corresponding section. Installation now will be successful. 
