---
title: pyinstaller 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - python
---

# Pyinstaller

PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! – and puts them with your script **in a single folder, or optionally in a single executable file**.


## Installation

```bash
pip install pyinstaller
```

## Usage

```bash
pyinstaller /path/to/yourscript.py
```

But the real power of pyinstaller is when it comes to onefile script generation. Additionally, pyinstaller provides a flag to avoid consoles from opening.


```bash
pyinstaller --onefile --windowed /path/to/yourscript.py
```

IF the antivirus (signature based) is able to catch the EXE even before opening it, then you need to change the packaging method as that would change the signature of the exported EXE. 

Pyinstaller uses UPX to compress the size of the EXE output. So it's worth to try with


```bash
pyinstaller --onefile --windowed /path/to/yourscript.py --noupx   

# --noupx: Do not use UPX
```

Or even other software to export into EXE.

IF the antivirus (heuristic based) did catch your exe after opening it, then you need to change the structure or the order of your source code:

- Add some random delay.
- Add some random operations like create a text file, append random text and then delete the file.
- Change the order of doing things.
- Offload some operations/commands to subprocess.

Tips:

Never blindly rely on Anti-Virus Sandbox Vmware to test an EXE.