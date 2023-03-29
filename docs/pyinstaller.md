---
title: pyinstaller 
author: amandaguglieri
draft: false
TableOfContents: true
tag: pentesting, python
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
