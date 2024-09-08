---
title: Port 135 - Windows Management Instrumentation (`WMI`)
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - tools
  - port 135
  - wmi
---
# Port 135 - Windows Management Instrumentation (`WMI`)

Windows Management Instrumentation (`WMI`) is Microsoft's implementation and also an extension of the Common Information Model (`CIM`), core functionality of the standardized Web-Based Enterprise Management (`WBEM`) for the Windows platform. WMI allows read and write access to almost all settings on Windows systems. Understandably, this makes it the most critical interface in the Windows environment for the administration and remote maintenance of Windows computers, regardless of whether they are PCs or servers. WMI is typically accessed via PowerShell, VBScript, or the Windows Management Instrumentation Console (`WMIC`). WMI is not a single program but consists of several programs and various databases, also known as repositories.

## Footprinting the service

The initialization of the WMI communication always takes place on TCP port 135, and after the successful establishment of the connection, the communication is moved to a random port. For example, the program wmiexec.py from the Impacket toolkit can be used for this.

```bash
/usr/share/doc/python3-impacket/examples/wmiexec.py <username>:<"password">@$ip <hostname>
```


## Source

HackTheBox Academy