---
title: Input Filtering
author: amandaguglieri
draft: false
TableOfContents: true
---
# Input filtering

Input Filtering involves validating and sanitizing data received by the web application from users or external sources. Input filtering helps prevent security vulnerabilities such as SQL injection, cross-site scripting (XSS), and command injection. Some common techniques for input filtering include data validation, input validation, and input sanitization:

- Data Validation: Data validation checks whether the incoming data conforms to expected formats and constraints. Example: an email field.
- Input Validation: Input validation goes a step further by not only checking data formats but also assessing data for potential security threats. It detects and rejects input that could be used for attacks, such as SQL injection payloads or malicious scripts.
- Input Sanitization: Input sanitization involves cleaning or escaping input data to remove or neutralize potentially dangerous characters or content.


## Input filtering techniques

- Content Security Policy (CSP): CSP is a security feature that controls which sources of content are allowed to be loaded by a web page. It helps prevent XSS attacks by specifying which domains are permitted sources for scripts, styles, images, and other resources.
- Cross-Site Request Forgery (CSRF) Protection: Filtering mechanisms can be used to implement CSRF protection, ensuring that incoming requests have valid anti-CSRF tokens to prevent attackers from tricking users into performing actions they didn't intend.
- Web Application Firewalls (WAFs): WAFs are security appliances or services that filter incoming HTTP requests to a web application. They use predefined rules and heuristics to detect and block malicious traffic. 
- Regular Expression Filtering: Regular expressions (regex) can be used to filter and validate data against complex patterns. However, improper regex usage can introduce security  vulnerabilities, so careful crafting and testing of regex patterns are necessary.

## Evasion techniques

Web application defense mechanisms are proactive tools and techniques designed to protect and defend web applications against various security threats and vulnerabilities.

Evasion in web application security testing refers to the practice of using various techniques and methods to bypass or  circumvent security mechanisms and controls put in place to protect a web application. 

### Bypass what!

- Authentication: Authentication mechanisms verify the identity of users and ensure that they have the appropriate permissions to access specific resources within the application. Common authentication methods include username and password, multi-factor authentication (MFA), and biometrics.
- Authorization: Authorization mechanisms determine what actions and resources users are allowed to access within the application once they have been authenticated. This includes defining roles, permissions, and access controls.
- Input Validation/Filtering: Input validation is the process of verifying and sanitizing data received from users or external sources to prevent malicious input that could lead to vulnerabilities like SQL injection, cross-site scripting (XSS), or command injection.
- Session Management: Session management mechanisms are responsible for creating, managing, and securing user  sessions. They include measures like session timeouts, secure session tokens, and protection against session fixation attacks.
- Cross-Site Request Forgery (CSRF) Protection: CSRF protection mechanisms prevent attackers from tricking users into making unauthorized requests to the application on their behalf. Tokens and anti-CSRF measures are often used for this purpose.
- Security Headers: HTTP security headers like Content  Security Policy (CSP), X-Content-Type-Options, and X-Frame-Options are used to control how web browsers should handle various aspects of web page security and rendering.
- Rate Limiting: Rate limiting mechanisms restrict the number of requests a user or IP address can make to the application within a specific time frame. This helps prevent brute force attacks and DDoS attempts.
- Web Application Firewalls (WAFs): WAFs are security  appliances or software solutions that sit between the web application and the client to monitor and filter incoming traffic. They can detect and block common web application attacks, such as SQL injection, cross-site scripting (XSS), and application-layer DDoS attacks. 
- Intrusion Detection Systems (IDS) and Intrusion Prevention Systems  (IPS): IDS and IPS solutions inspect network and application traffic for signs of suspicious or malicious activity. IDS detects and alerts on potential threats, while IPS can take proactive measures to block or prevent malicious traffic.
- Proxies: In the context of web applications, proxies refer to intermediary servers that facilitate communication between a user's browser and the web server hosting the application. These proxies can serve various purposes, ranging from enhancing security and privacy to optimizing performance and managing network traffic.


### Bypass how!

- Bypassing Web Application Firewalls (WAFs)/Proxy Rules: WAFs and proxies are designed to filter out malicious requests and prevent attacks like SQL injection or cross-site scripting (XSS). Evasion techniques may involve encoding, obfuscation, or fragmentation of malicious payloads to bypass the WAF's detection rules.
- Evading Intrusion Detection Systems (IDS): IDS systems monitor network traffic for signs of malicious activity. Evasion techniques can be used to hide or modify the payload of an attack so that it goes undetected by the IDS.

