---
title: NFC - Setting up proxmark3 RDV4.01
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - NFC pentesting
---

# Installing proxmark3 RDV4.01 in Kali

## Preparing Linux

In my case, I will create a Virtual environment:

```shell
mkvirtualenv nfc
```


An system upgrade was carried out prior to following these instructions.

Update the packages list

```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get auto-remove -y
```


Install the requirements

```shell
sudo apt-get install --no-install-recommends git ca-certificates build-essential pkg-config libreadline-dev gcc-arm-none-eabi libnewlib-dev qtbase5-dev libbz2-dev liblz4-dev libbluetooth-dev libpython3-dev libssl-dev libgd-dev
```


Clone the repository:

```
git clone https://github.com/RfidResearchGroup/proxmark3.git
```

**Check ModemManager**. Make sure ModemManager will not interfere, otherwise it could brick your Proxmark3! Modem Manager must be discarded. 

>ModemManager is pre-installed on many different Linux distributions, very probably yours as well. It's intended to prepare and configure the mobile broadband (2G/3G/4G) devices, whether they are built-in or dongles. Some are serial, so when the Proxmark3 is plugged and a `/dev/ttyACM0` appears, ModemManager attempts to talk to it to see if it's a modem replying to AT commands. Now imagine what happens when you're flashing your Proxmark3 and ModemManager suddenly starts sending bytes to it at the same time... Yes it makes the flashing failing. And if it happens while you're flashing the bootloader, it will require a JTAG device to unbrick the Proxmark3. ModemManager is a threat for the Proxmark3, but also for many other embedded devices, such as some Arduino platforms.

```
# Solution 1: remove ModemManager
sudo apt remove modemmanager

# Solution 2: disable ModemManager
sudo systemctl stop ModemManager
sudo systemctl disable ModemManager
```

[Troubleshooting  issues with ModemManager](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/ModemManager-Must-Be-Discarded.md#if-youre-a-linux-user)


Connect your device using the USB cable and check that the proxmark is being picked up by your computer:

```shell
sudo dmesg | grep -i usb
```

It should show up as a CDC device:

```
usb 3-3: Product: proxmark3
usb 3-3: Manufacturer: proxmark.org
usb 3-3: SerialNumber: iceman
cdc_acm 3-3:1.0: ttyACM0: USB ACM device
```

And a new `/dev/ttyACM0` should have appeared:

```
ls -la /dev | grep ttyACM0    
```


Get permissions to use /dev/ttyACM0. Add current user to the proper groups to get permission to use `/dev/ttyACM0`. This step can be done from the Iceman Proxmark3 repo with:

```shell
make accessrights
```

Then, you need to logout and login in again for your new group membership to be fully effective.

To test you have the proper read & write rights, plug the Proxmark3 and execute:

```shell
[ -r /dev/ttyACM0 ] && [ -w /dev/ttyACM0 ] && echo ok
```

It must return ok. Otherwise this means you've got a permission problem to fix.


## Compilation instructions for RDV4

The repo defaults for compiling a firmware and client suitable for Proxmark3 RDV4.

Get the latest commits:

```
cd proxmark3
git pull
```

Clean and compile everything:

```
make clean && make -j
```

if you got an error, go to the [troubleshooting guide](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Troubleshooting.md). 


Install, but be carefull, if you do

```shell
sudo make install
```

Then the required files will be installed on your system, by default in `/usr/local/bin` and `/usr/local/share/proxmark3`. Maintainers can read [this doc](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Development/Maintainers.md) to learn how to modify installation paths via `DESTDIR` and `PREFIX` Makefile variables.

The commands given in the documentation assume you did the installation step. If you didn't, you've to adjust the commands paths and files paths accordingly, e.g. calling `./pm3` or `client/proxmark3` instead of just `pm3` or `proxmark3`.

In most cases, you can run the following script which try to auto-detect the port to use, on several OS:

```shell
pm3-flash-all
```

if not working: [go to troubleshooting](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Use_of_Proxmark/0_Compilation-Instructions.md)

Run the client:  In most cases, you can run the script `pm3` which try to auto-detect the port to use, on several OS.

```shell
./pm3
```

For the other cases, specify the port by yourself. For example, for a Proxmark3 connected via USB under Linux. Here, for example, for a Proxmark3 connected via USB under Linux (adjust the port for your OS):

```shell
proxmark3 /dev/ttyACM0
```

or from the local repo

```shell
client/proxmark3 /dev/ttyACM0
```

If all went well you should get some information about the firmware and memory usage as well as the prompt, something like this.

```shell
[=] Session log /home/iceman/.proxmark3/logs/log_20230208.txt
[+] loaded from JSON file /home/iceman/.proxmark3/preferences.json
[=] Using UART port /dev/ttyS3
[=] Communicating with PM3 over USB-CDC


  8888888b.  888b     d888  .d8888b.
  888   Y88b 8888b   d8888 d88P  Y88b
  888    888 88888b.d88888      .d88P
  888   d88P 888Y88888P888     8888"
  8888888P"  888 Y888P 888      "Y8b.
  888        888  Y8P  888 888    888
  888        888   "   888 Y88b  d88P
  888        888       888  "Y8888P"    [ ☕ ]


 [ Proxmark3 RFID instrument ]

    MCU....... AT91SAM7S512 Rev A
    Memory.... 512 Kb ( 66% used )

    Client.... Iceman/master/v4.16191 2023-02-08 22:54:30
    Bootrom... Iceman/master/v4.16191 2023-02-08 22:54:26
    OS........ Iceman/master/v4.16191 2023-02-08 22:54:27
    Target.... RDV4
 
[usb] pm3 -->
```

This `[usb] pm3 -->`  is the Proxmark3 interactive prompt.


## Configuration and Verification

Verify the status of your installation with:

```
script run init_rdv4
```

To make sure you got the latest sim module firmware:

```
hw status
```

If you get a message such as:

```
[#] Smart card module (ISO 7816)
[#]   version................. vX.XX ( Outdated )
```

Then, the version is obsolete and you will need to update it. The following command upgrades your device sim module firmware. Don't not turn off your device during the execution of this command!! Even its a quite fast command you should be warned. You may brick it if you interrupt it.

```
smart upgrade -f /usr/local/share/proxmark3/firmware/sim014.bin

# or if from local repo
smart upgrade -f sim014.bin
```


You get the following output if the execution was successful:

```
[=] --------------------------------------------------------------------
[!] ⚠️  WARNING - sim module firmware upgrade
[!] ⚠️  A dangerous command, do wrong and you could brick the sim module
[=] --------------------------------------------------------------------

[=] firmware file       sim014.bin
[=] Checking integrity  sim014.sha512.txt
[+] loaded 3658 bytes from binary file sim014.bin
[+] loaded 158 bytes from binary file sim014.sha512.txt
[=] Don't turn off your PM3!
[+] Sim module firmware uploading to PM3...
 🕑 3658 bytes sent
[+] Sim module firmware updating...
[#] FW 0000
[#] FW 0080
[#] FW 0100
[#] FW 0180
[#] FW 0200
[#] FW 0280
[#] FW 0300
[#] FW 0380
[#] FW 0400
[#] FW 0480
[#] FW 0500
[#] FW 0580
[#] FW 0600
[#] FW 0680
[#] FW 0700
[#] FW 0780
[#] FW 0800
[#] FW 0880
[#] FW 0900
[#] FW 0980
[#] FW 0A00
[#] FW 0A80
[#] FW 0B00
[#] FW 0B80
[#] FW 0C00
[#] FW 0C80
[#] FW 0D00
[#] FW 0D80
[#] FW 0E00
[+] Sim module firmware upgrade successful    
```

Run hw status command to verify that the upgrade went well.

```
hw status
```

