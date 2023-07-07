---
title: Port 389 - LDAP 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - active directory
  - ldap
  - windows
  - port 389
---

# Port 389 - LDAP

>Application protocol for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network. 

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


## LDAP queries: LDAPFilter

By combining the  "Get-ADObject" cmdlet  with the "LDAPFilter" parameter in powershell we can perform some ldap queries via powershell. 

```ps
Get-ADObject -LDAPFilter <FILTER> | select cn
```

Some useful  LDAPFilters:

| Search for | LDAP query | 
| ------------ | ---------- |
| Find All Workstations |  ' (objectCategory=computer)' |
| Find All DomainControllers | '(&(objectCategory=Computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))' |

| Search for | LDAP query | 
| ------------ | ---------- |
| Find All Users | ' (&(objectCategory=person)(objectClass=user))' |
| Filnd All Contacts | '(objectClass=contact)' |
| Find All Users and Contacts | '(objectClass=user)' |
| List Disabled Users |  '(userAccountControl:1.2.840.113556.1.4.803:=2)' | 


| Search for | LDAP query | 
| ------------ | ---------- |
| Find All Groups | '(objectClass=group)' |
| Find direct members of a Security Group | '(memberOf=CN=Admin,OU=Security,DC=DOM,DC=NT)' |



More:

- [LDAP Queries related to AD computers](https://ldapwiki.com/wiki/Wiki.jsp?page=Active%20Directory%20Computer%20Related%20LDAP%20Query)
- [LDAP queries related to AD users](https://ldapwiki.com/wiki/Wiki.jsp?page=Active%20Directory%20User%20Related%20Searches).
- [LDAP queries related to AD groups](https://ldapwiki.com/wiki/Wiki.jsp?page=Active%20Directory%20Group%20Related%20Searches).


## LDAP queries: Search Filters

The LDAPFilter parameter with the same cmdlets lets us use LDAP search filters when searching for information. 

Operators: 

- & -> and
- | -> or
- ! -> not


**AND** Operation:

-   One criteria: `(& (..C1..) (..C2..))`
-   More than two criteria: `(& (..C1..) (..C2..) (..C3..))`

**OR** Operation:

-   One criteria: `(| (..C1..) (..C2..))`
-   More than two criteria: `(| (..C1..) (..C2..) (..C3..))`


### Filters

| **Criteria** | **Rule** | **Example** |
| ------- | ---- | --------- |
| Equal to | (attribute=123) | (&(objectclass=user)(displayName=Smith) |
| Not equal to | (!(attribute=123)) | !objectClass=group) |
| Present | (attribute=*) |  (department=*) |
| Not present | (!(attribute=*)) | (!homeDirectory=*) |
| Greater than | (attribute>=123) | (maxStorage=100000) |
| Less than | (attribute<=123) | (maxStorage<=100000) |
| Approximate match | (attribute~=123) | (sAMAccountName~=Jason) | 
| Wildcards | (attribute=*A) | (givenName=*Sam) |

