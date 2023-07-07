

Internet Control Message Protocol (ICMP) is a protocol used by devices to communicate with each other on the Internet for various purposes, including error reporting and status information. It sends requests and messages between device:

ICMP Requests: A request is a message sent by one device to another to request information or perform a specific action. 

- **Echo Request**: This message tests whether a device is reachable on the network. When a device sends an echo request, it expects to receive an echo reply message. For example, the tools `tracert` (Windows) or `traceroute` (Linux) always send ICMP echo requests.
- **Timestamp Request**: This message determines the time on a remote device.
- **Address Mask Request**: This message is used to request the subnet mask of a device.

ICMP Messages: A message in ICMP can be either a request or a reply. In addition to ping requests and responses, ICMP supports other types of messages, such as error messages, destination unreachable, and time exceeded messages. 

- **Echo reply**: This message is sent in response to an echo request message.
- **Destination unreachable**: This message is sent when a device cannot deliver a packet to its destination.
- **Redirect**: A router sends this message to inform a device that it should send its packets to a different router.
- **time exceeded**: This message is sent when a packet has taken too long to reach its destination.
- **Parameter problem**: This message is sent when there is a problem with a packet's header.
- **Source quench**: This message is sent when a device receives packets too quickly and cannot keep up. It is used to slow down the flow of packets.
