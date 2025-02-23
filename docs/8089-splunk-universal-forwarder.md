---
title: 8089 - Splunk Universal Forwarder
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - mongodb
  - port
  - "8089"
---
# 8089 - Splunk Universal Forwarder

!!! tip "Source of this note"
	- [https://airman604.medium.com/splunk-universal-forwarder-hijacking-5899c3e0e6b2](https://airman604.medium.com/splunk-universal-forwarder-hijacking-5899c3e0e6b2)
	- [HTB module](https://academy.hackthebox.com/module/67/section/926)

Splunk Universal Forwarder includes a management service that is listening on TCP port 8089 and is used for managing the forwarder. By default it accepts remote connections, but doesn’t allow remote connections with default credentials (`admin/changeme`). The exploit described below can be used in the following ways:

- Local privilege escalation to the user that the forwarder is running under, if the default password is not changed.
- Remote command execution (with the privileges that the forwarder is running under) **if** the default password has been changed and is known to the attacker.


## How Does It Work

1. Connect to the Splunk Universal Forwarder management port, authenticate with provided or default credentials, and configure the forwarder to use the attacker controlled machine as the deployment server.
2. The forwarder then connects to the attacker machine and requests deployment applications.
3. The exploit responds to the request with a fake application containing a script input instructing the forwarder to run the script.
4. After a delay, the exploit connects again to the forwarder management port and reverts the deployment server configuration.


## The Exploit

The code can be found here: [https://github.com/airman604/splunk_whisperer](https://github.com/airman604/splunk_whisperer)

Exploit parameters (review and change within the .py script):

RHOST — target machine, 127.0.0.1 for local privilege escalation. Default Splunk credentials are only accepted for local connections.

RPORT — management port of the Splunk Universal Forwarder, 8089 by default.

LHOST — attacker’s IP where the for

LPORT — port number to run the fake deployment server on.

SPLUNK_USER/SPLUNK_PASSWORD — credentials to authenticate to the forwarder.

SCRIPT — path to the script to be sent to the forwarder for execution.