---
title: RFID
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - RFID
---

# RFID 

RFID Reader continuously sends Radio Waves. When the Tag is in the range it sends its feedback signals to the read.

Types of RFID Frequencies. There are Three Basic Types of RFID Frequencies:

- Low Frequency (LF) 125 kHz or 134 kHz Range 8-10 cm
- High Frequency (HF) 13.56 MHz Range approx. 1 m 
- Ultra High Frequency (UHF) 860-960 MHz Range 10 - 15 m



## Quick Overview of Arduino 

- Arduino is an open-source hardware 
- Single board with microcontroller (ATmega328P ) 
- Attach different modules and sensors
- Different versions of Arduino

Download Arduino IDE.




## Requirements

RFID Cards we need.
- Mifare classic cards (1K, 4K, EV1): UID is not changeable.
- Magic cards: In magic cards, UID is changeable.


For programming Mifare we will use

- ACR122u
- MFRC522 with STMB
- USB to TTL
- STM8 & STM32 USB 
- Jumper wires (female to female)

More tools require: 

- Arduino UNO
- RC522 Module
- OLED 4 Pin
- Breadboard
- Jumper wires
- Buzzer


