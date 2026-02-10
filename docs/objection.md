---
title: Objection
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mobile pentesting
---

# Objection

What it does? It makes a regular ADB tion.

Note: be careful when it comes to Objection + Frida.

## Installation

```bash
pip3 install objection
```

## Usage

What it does? It makes a regular ADB connection ant start the frida server in the device. If you are using a rooted device it is needed to select the application that you want to test inside the --gadget option.

In the metromadrid app, this would be:

```
objection --gedget es.metromadrid.metroandroid explore
```

## Basic commands

```bash
# Launch objection
objection -n <NameOfPackage> 

# Some interesting information (like passwords, paths...) could be found inside the environment.
env

file download <remotepath> [<localpath>]
file upload <localpath> [<remotepath>]
import <localpath frida-script>

# Disable SSL pinning on android devices
android sslpinningdisable

# There are predefined scripts that can be run. See in repor /master/agent /src/android/*
android NameofScript
# example: andoird keystore detal -- json
# example: memory dump all > memory_dump /// then we may run strings on the generated file.

```

