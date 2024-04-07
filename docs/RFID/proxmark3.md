---
title: Proxmark3 RDV4.01
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - NFC
  - pentesting
---
#  Using Proxmark3 RDV4.01 

Installation: [Installing proxmark3 RDV4.01 in Kali](proxmark3-rdv4.01-setting-up.md)

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


Read and write:

```
# Read sector 1 with key FFFFFFFFFFFF
hf mf rdsc -s 1 -k FFFFFFFFFFFF

# Read block 13 with key FFFFFFFFFFFF
hf mf rdbl --blk 13 -k FFFFFFFFFFFF

# Write block 8 with key a FFFFFFFFFFFF 
hf mf wrbl --blk 8 -a -k FFFFFFFFFFFF -d FFFFFFFFFFFF7F078800FFFFFFFFFFFF
```



Getting keys

```
# Check all sectors, all keys, 1K, and write to file
hf mf chk --1k --dump             

# Check for default keys:
hf mf chk --1k -f mfc_default_keys

# Check dictionary against block 0, key A
hf mf chk -a --tblk 0 -f mfc_default_keys.dic       

# Run autopwn, to extract all keys and backup a MIFARE Classic tag
hf mf autopwn


hf mf nested --1k --blk 0 -a -k FFFFFFFFFFFF --dump

# Dump MIFARE Classic card contents:
hf mf dump
hf mf dump --1k -k hf-mf-A29558E4-key.bin -f hf-mf-A29558E4-dump.bin


# Write to MIFARE Classic block:
hf mf wrbl --blk 0 -k FFFFFFFFFFFF -d d3a2859f6b880400c801002000000016


# Bruteforce MIFARE Classic card numbers from 11223344 to 11223346:
script run hf_mf_uidbruteforce -s 0x11223344 -e 0x11223346 -t 1000 -x mfc

```




## Next steps
- [https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/cheatsheet.md](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/cheatsheet.md)
- [https://github.com/Proxmark/proxmark3/wiki/Generic-ISO14443-Ops](https://github.com/Proxmark/proxmark3/wiki/Generic-ISO14443-Ops)
- [https://github.com/RfidResearchGroup/proxmark3/wiki/More-cheat-sheets](https://github.com/RfidResearchGroup/proxmark3/wiki/More-cheat-sheets)

