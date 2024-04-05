---
title: RFID 
author: amandaguglieri
---

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


# RFID

RFID Reader continuously sends Radio Waves. When the Tag is in the range it sends its feedback signals to the read.

Types of RFID Frequencies. There are Three Basic Types of RFID Frequencies:

- Low Frequency (LF) 125 kHz or 134 kHz Range 8-10 cm
- High Frequency (HF) 13.56 MHz Range approx. 1 m 
- Ultra High Frequency (UHF) 860-960 MHz Range 10 - 15 m

## Mifare Classic Cards

- Mifare Classic 1K
- Mifare Classic 4K
- Mifare Classic EV1


Each Mifare Tag has a 4Bytes UID whic is unique and not changeable.

Memory Organization:

- 1024 Bytes
- Sectors and Blocks: 
- 16 Sectors (0-15).
- 4 block in each Sector 
- 16 Bytes in each Block
- 2 Keys (A/B) in each Sector 
- Sector Trailer 
- Authentication is required


## Quick Overview of Arduino 

- Arduino is an open-source hardware 
- Single board with microcontroller (ATmega328P ) 
- Attach different modules and sensors
- Different versions of Arduino

Download Arduino IDE.