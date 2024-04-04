---
title: NFC - Proxmark3 RDV4.01 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - NFC pentesting
---
#  NFC - Using Proxmark3 RDV4.01 

## Basic commands

```
# The prompt will have this appearance
[usb] pm3 --> 

# Display help and commands
help

# Close the client
quit
```


To get an overview of the available commands for LF RFID and HF RFID:

```
[usb] pm3 --> lf
[usb] pm3 --> hf
```

To search quickly for known LF or HF tags:

```
[usb] pm3 --> lf search
[usb] pm3 --> hf search
```

To get info on a ISO14443-A tag:

```
[usb] pm3 --> hf 14a info
```


## Next steps
- [https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/cheatsheet.md](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/cheatsheet.md)
- [https://github.com/Proxmark/proxmark3/wiki/Generic-ISO14443-Ops](https://github.com/Proxmark/proxmark3/wiki/Generic-ISO14443-Ops)
- [https://github.com/RfidResearchGroup/proxmark3/wiki/More-cheat-sheets](https://github.com/RfidResearchGroup/proxmark3/wiki/More-cheat-sheets)

