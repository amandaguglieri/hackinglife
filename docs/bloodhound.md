---
title: BloodHound
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
  - enumeration
  - reconnaissance
  - tools
---


# BloodHound

(C# and PowerShell Collectors)


## Installation

BloodHound is a single page Javascript web application, built on top of [Linkurious](http://linkurio.us/), compiled with [Electron](http://electron.atom.io/), with a [Neo4j](https://neo4j.com/) database fed by a C# data collector.

Download github repo from: [https://github.com/BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound).

Sharphound is the official data collector for BloodHound.

```bash
sudo apt-get install bloodhound
```

Initialize the console:

```bash
sudo neo4j console 
```

Open the browser at the indicated address: http://localhost:7474/

The first time it will ask you for default user and password:  neo4j:neo4j.

After loging into the application you will be prompted to change default password.


## Basic usage

**1.** Get SharpHound collector working in the victim's machine:

```ps
# Same as with powerview
powershell -ep bypass

# Launch Sharphound
..\Downloads\SharpHound.ps1

# Generate a zip file
Invoke-BloodHound -CollectionMethod All -Domain CONTROLER.local -ZipFileName loot.zip
```

**2.** [Transfer](data-transfer-and-backdoors.md) loot.zip file to you attacker machine

**3.** Import loot.zip into Bloodhoud.

```bash
# Launch Bloodhound interface.
bloodhound
# enter user:password already set before for the neo4j console.
```

Click on "Upload data". Upload the file.

