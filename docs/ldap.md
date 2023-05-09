---
title: LDAP 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
---

# LDAP

Lightweight Directory Access Protocol (LDAP) is an integral part of Active Directory (AD). The **Lightweight Directory Access Protocol** (**LDAP**) is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network.  A common use of LDAP is to provide a central place to store usernames and passwords. This allows many different applications and services to connect to the LDAP server to validate users.

The latest LDAP specification is Version 3, which is published as [RFC 4511](https://tools.ietf.org/html/rfc4511). **AD** stores user account information and security information such as passwords and facilitates sharing this information with other devices on the network. **LDAP** is the language that applications use to communicate with other servers that also provide directory services. In other words, LDAP is a way that systems in the network environment can "speak" to AD.

The relationship between AD and LDAP can be compared to Apache and HTTP. The same way Apache is a web server that uses the HTTP protocol, Active Directory is a directory server that uses the LDAP protocol. While uncommon, you may come across organizations while performing an assessment that does not have AD but does have LDAP, meaning that they most likely use another type of LDAP server such as OpenLDAP.



- TCP and UDP port 389.
- It's a binary protocol and by default not encrypted.
- Has been updated to include encryptions addons, as Transport Layer Security (TLS)/SSL and can be tunnelled through SSH

The hierarchy (tree) of information stored via LDAP is known as the Directory Information Tree (DIT). That structure is defined in a schema.


## AD LDAP Authentication

LDAP is set up to authenticate credentials against AD using a "BIND" operation to set the authentication state for an LDAP session. There are two types of LDAP authentication.

**1.**  **Simple Authentication:** This includes anonymous authentication, unauthenticated authentication, and username/password authentication. Simple authentication means that a username and password create a BIND request to authenticate to the LDAP server.
    
**2.**  **SASL Authentication:** The Simple Authentication and Security Layer (SASL) framework uses other authentication services, such as Kerberos, to bind to the LDAP server and then uses this authentication service (Kerberos in this example) to authenticate to LDAP. The LDAP server uses the LDAP protocol to send an LDAP message to the authorization service which initiates a series of challenge/response messages resulting in either successful or unsuccessful authentication. SASL can provide further security due to the separation of authentication methods from application protocols. 

LDAP authentication messages are sent in cleartext by default so anyone can sniff out LDAP messages on the internal network. It is recommended to use TLS encryption or similar to safeguard this information in transit.