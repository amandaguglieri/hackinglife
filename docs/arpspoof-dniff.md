---
title: arpspoof from dniff
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows 
  - tools
---

# arpspoof from dniff

dniff is a collection of tools for network auditing and penetration testing. It includes arpspoof, a utility designed to intercept traffic on a switched LAN.

Before running, enable Linux Kernel IP Forwarding (this transforms Linux box into a router).

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

And then, run arpspoof:

```
arpspoof -i <interface> -t <target IP> -r <host IP>
# interface: NIC you want to use (like eth0 for your local LAN, or tap0 for Hera Lab)
# target IP: one of the victim address
# host IP: the other victim address.
```

After that, run Wireshark to intercept the traffic.

- **SMB traffic**. When capturing smb traffic in wireshark, go to: FILE>Export Objects>SMB/SMB2. There you have all files uploaded or downloaded from a server during a SMB capture session.
- **Telnet traffic**: Telnet sends characters one by one, that's why you don't see the username/password straight away. But with "Follow TCP Stream", wireshark will put all data together and you will be able to see the username/password. Just rightclick on a packet of the telnet session and choose: "Follow TCP Stream".
