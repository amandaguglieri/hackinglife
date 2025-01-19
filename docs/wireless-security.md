---
title: Wireless security
author: amandaguglieri
draft: false
TableOfContents: true
---
# Wireless security


## Basic concepts

| Name | Explanation |
| --- | --- |
|`MAC address`|A unique identifier for the device's wireless adapter.|
|`SSID`|The network name, also known as the `Service Set Identifier` of the WiFi network.|
|`Supported data rates`|A list of the data rates the device can communicate.|
|`Supported channels`|A list of the `channels` (frequencies) on which the device can communicate.|
|`Supported security protocols`|A list of the security protocols that the device is capable of using, such as `WPA2`/`WPA3`.|



Wired Equivalent Privacy: WEP

Wi-Fi Protected Access: WPA


## WEP Challenge-Response Handshake

|**Step**|**Who**|**Description**|
|---|---|---|
|1|`Client`|Sends an association request packet to the WAP, requesting access.|
|2|`WAP`|Responds with an association response packet to the client, which includes a challenge string.|
|3|`Client`|Calculates a response to the challenge string and a shared secret key and sends it back to the WAP.|
|4|`WAP`|Calculates the expected response to the challenge with the same shared secret key and sends an authentication response packet to the client.|

Nevertheless, some packets can get lost, so the so-called CRC checksum has been integrated. Cyclic Redundancy Check (CRC) is an error-detection mechanism used in the WEP protocol to protect against data corruption in wireless communications. 

## Encryption Protocols

We can use various encryption algorithms to protect the confidentiality of data transmitted over wireless networks. The most common encryption algorithms in WiFi networks are [Wired Equivalent Privacy](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) (`WEP`), [WiFi Protected Access 2](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access#WPA2) (`WPA2`), and [WiFi Protected Access 3](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access#WPA3) (`WPA3`).


### Wired Equivalent Privacy: WEP

Very week with 63-bit and 128-bit encryption keys.

WEP uses the RC4 cipher encryption algorithm, which makes it vulnerable to attacks.

Passwords can be crack in minutes.

Superseded by WPA in 2003


### Wi-Fi Protected Access: WPA

Developed by Wi-Fi Alliance

Massive security improvement over WEP with 256-bit encryption keys.

Superseded by WPA2 in 2006.