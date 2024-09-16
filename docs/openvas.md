---
title: OpenVAS
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanner
  - vulnerability assessment
---

# OpenVAS

[OpenVAS](https://www.openvas.org/) by Greenbone Networks is a publicly available open-source vulnerability scanner. OpenVAS can perform network scans, including authenticated and unauthenticated testing.

Scans may take 1-2 hours to finish.


## Installation

```shell-session
# Updating packages
sudo apt-get update && apt-get -y full-upgrade

# Install the tool
sudo apt-get install gvm && openvas

# Initiate setup process
sudo gvm-setup

# Check installation
sudo gvm-check-setup

# Start OpenVAS
sudo gvm-start
```

Openvas stands for Open Vulnerability Assessment Scanner. It's based on assets (not on scans). These assets may be hosts, operating systems, TLS certificates... Scans are called here `Tasks`.


## Basic usage

```bash
# Start OpenVAS
sudo gvm-start
```


Go to `https://$ip:8080`

[Documentation](https://docs.greenbone.net/GSM-Manual/gos-6/en/scanning.html).

- `Base`: This scan configuration is meant to enumerate information about the host's status and operating system information.    
- `Discovery`: Enumerate host's services, hardware, accessible ports, and software being used on the system.
- `Host Discovery`: Whether the host is alive and determines what devices are `active` on the network.  _OpenVAS leverages ping to identify if the host is alive._
- `System Discovery`: Enumerates the target host further than the 'Discovery Scan' and attempts to identify the operating system and hardware associated with the host.
- `Full and fast`: This configuration is recommended by OpenVAS as the safest option and leverages intelligence to use the best NVT checks for the host(s) based on the accessible ports.

There are various export formats for reporting purposes, including XML, CSV, PDF, ITG, and TXT. If you choose to export your report out as an XML, you can leverage various XML parsers to view the data in an easier to read format.

## Reporting

[See openVAS Reporting](openvasreporting.md).
