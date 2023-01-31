---
title: HTTP Authentication Schemes
author: amandaguglieri
draft: false
TableOfContents: true
tag: authentication, windows, basic, digest, NTLM, negotiate
---

# HTTP Authentication Schemes

This resource is pretty awesome: [https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/understanding-http-authentication](https://learn.microsoft.com/en-us/dotnet/framework/wcf/feature-details/understanding-http-authentication).

I'll be (CTRL-c-CTRL-v)ing what I think it's important.

## Understanding HTTP Authentication

Authentication is the process of identifying whether a client is eligible to access a resource. The HTTP protocol supports authentication as a means of negotiating access to a secure resource.

The initial request from a client is typically an anonymous request, not containing any authentication information. HTTP server applications can deny the anonymous request while indicating that authentication is required. The server application sends WWW-Authentication headers to indicate the supported authentication schemes. 

## HTTP Authentication Schemes



| Authentication Scheme | Description |
| --------------------- | ----------- |
| Anonymous | An anonymous request does not contain any authentication information. This is equivalent to granting everyone access to the resource. |
| Basic | Basic authentication sends a Base64-encoded string that contains a user name and password for the client. Base64 is not a form of encryption and should be considered the same as sending the user name and password in clear text. If a resource needs to be protected, strongly consider using an authentication scheme other than basic authentication. |
| Digest | Digest authentication is a challenge-response scheme that is intended to replace Basic authentication. The server sends a string of random data called a nonce to the client as a challenge. The client responds with a hash that includes the user name, password, and nonce, among additional information. The complexity this exchange introduces and the data hashing make it more difficult to steal and reuse the user's credentials with this authentication scheme. Digest authentication requires the use of Windows domain accounts. The digest realm is the Windows domain name. Therefore, you cannot use a server running on an operating system that does not support Windows domains, such as Windows XP Home Edition, with Digest authentication. Conversely, when the client runs on an operating system that does not support Windows domains, a domain account must be explicitly specified during the authentication. | 
| NTLM | NT LAN Manager (NTLM) authentication is a challenge-response scheme that is a securer variation of Digest authentication. NTLM uses Windows credentials to transform the challenge data instead of the unencoded user name and password. NTLM authentication requires multiple exchanges between the client and server. The server and any intervening proxies must support persistent connections to successfully complete the authentication. |
| Negotiate | Negotiate authentication automatically selects between the Kerberos protocol and NTLM authentication, depending on availability. The Kerberos protocol is used if it is available; otherwise, NTLM is tried. Kerberos authentication significantly improves upon NTLM. Kerberos authentication is both faster than NTLM and allows the use of mutual authentication and delegation of credentials to remote machines. |
| Windows Live ID | The underlying Windows HTTP service includes authentication using federated protocols. However, the standard HTTP transports in WCF do not support the use of federated authentication schemes, such as Microsoft Windows Live ID. Support for this feature is currently available through the use of message security. | 

