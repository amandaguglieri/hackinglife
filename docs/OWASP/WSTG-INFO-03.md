---
title: Review Webserver Metafiles for Information Leakage - OWASP Web Security Testing Guide
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web
  - pentesting
  - reconnaissance
  - WSTG-INFO-03
---
# Review Webserver Metafiles for Information Leakage

!!! quote "OWASP"
	[OWASP Web Security Testing Guide 4.2](index.md) > 1. Information Gathering > 1.3. Review Webserver Metafiles for Information Leakage

|ID|Link to Hackinglife|Link to OWASP|Objectives|
|:---|:---|:---|:---|
|1.3|[WSTG-INFO-03](WSTG-INFO-03.md)|[Review Webserver Metafiles for Information Leakage](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage)|- Identify hidden or obfuscated paths and functionality through the analysis of metadata files (robots.txt, `<META>` tag, sitemap.xml) - Extract and map other information that could lead to a better understanding of the systems at hand.|

## Searching for well-known files

- robots.txt
- sitemap.xml
- security.txt (proposed standard which allows websites to define security policies and contact details.)
- human.txt (initiative for knowing the people behind a website.)

## Examining META tags

`<META>` tags are located within the `HEAD`section of each HTML document. 

**Robots directive** can also be specified through the use of a specific `META`tag.

```
<META NAME="ROBOTS" ...>
```

If no `META` tag is present, then the default is `INDEX, FOLLOW`. 

Other revealing `META` tags. 

## The .well-known/ directory

The `.well-known` standard, defined in [RFC 8615](https://datatracker.ietf.org/doc/html/rfc8615), serves as a standardized directory within a website's root domain. This designated location, typically accessible via the `/.well-known/` path on a web server, centralizes a website's critical metadata, including configuration files and information related to its services, protocols, and security mechanisms.

Some of the files are these: [https://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml](https://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml).

| URI Suffix                     | Description                                                                                           | Status      | Reference                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------- |
| `security.txt`                 | Contains contact information for security researchers to report vulnerabilities.                      | Permanent   | RFC 9116                                                                                |
| `/.well-known/change-password` | Provides a standard URL for directing users to a password change page.                                | Provisional | https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri |
| `openid-configuration`         | Defines configuration details for OpenID Connect, an identity layer on top of the OAuth 2.0 protocol. | Permanent   | http://openid.net/specs/openid-connect-discovery-1_0.html                               |
| `assetlinks.json`              | Used for verifying ownership of digital assets (e.g., apps) associated with a domain.                 | Permanent   | https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md     |
| `mta-sts.txt`                  | Specifies the policy for SMTP MTA Strict Transport Security (MTA-STS) to enhance email security.      | Permanent   | RFC 8461                                                                                |