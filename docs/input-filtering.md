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

## Solutions for implementing input filtering

WAFs. An well known open source solution is ModSecurity. WAFs use rules to indicate what a filter must block or allow. These rules use Regular Expressions (RE or RegEx).

[See notes on regex](regex.md).

The best solution for protecting a webapp is whitelisting. But blacklisting methods are commonly found in deployments. Blacklisting includes a collection of well-known attacks. There are WAF bypasses.

## WAF bypasses

```
################
# XSS: alert('xss') and alert(1)
################
prompt('xss')
prompt(8)
confirm('xss')
confirm(8)
alert(/xss/.source)
window[/alert/.source](8)

################
# XSS: alert(document.cookie)
################
with(document)alert(cookie)
alert(document['cookie'])
alert(document[/cookie/.source])
alert(document[(/coo/.source+/kie/.source])

################
# XSS: <img src=x onerror=alert(1);>
################
<svg/onload=alert(1)>
<video src=x onerror=alert(1);>
<audio src=x onerror=alert(1);>


################
# XSS: javascript:alert(document.cookie)
################
data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4=
```


```
################
# Blind SQL injection: 'or 1=1
################
' or 6=6
' or 0x47=0x47
or char(32)=''
or 6 is not null

################
# Blind SQL injection: 'or 1=1
################

UNION ALL SELECT
```


```
################
#  Directory Traversals: /etc/passwd
################
/too/../etc/far/../passwd
/etc//passwd
/etc/ignore/../passwd
/etc/passwd.......
```

```
################
#  Webshells: c99.php, r57.php, shell.aspx, cmd.jsp, CmdAsp.asp
################
augh.php
```

### Fingerprinting a WAF 

Tools: [wafw00f](wafw00f.md) and [nmap](nmap.md) script:

```bash
nmap -p 80 -script http-waf-detect $ip 
nmap -p 80 -script http-waf-fingerprint $ip 
```


**Detecting a WAF manually**

**1.** *Cookies*: Via cookie values.

| WAF              | Cookie value                                                     |
| ---------------- | ---------------------------------------------------------------- |
| Citrix netscaler | ns_af, citrix_ns_id, NSC_                                        |
| F5 BIG-IP ASM    | TS followed by a string with the regex:<br>`^TS[a-zA-Z0-9]{3,6}` |
| Barracuda        | barra_counter_session, BNi__BARRACUDA_LB_COOKIE                  |

**2.** *Server cloaking*: WAFs can rewrite Server header to deceive attackers.

**3.** *Response codes*: WAFs can also modify the HTTP response codes if the request is hostile.

**4.** WAFs can be displayed in response bodies, like for instance mod_security, AQTRONIX WebKnight, dotDefender.

**5.** *Drop Action*: WAFs can close the connections in the case they detect a malicious request.


## Client-side filters

### Firefox

Browser addons such as [NoScript](https://addons.mozilla.org/en-US/firefox/addon/noscript/) is a whitelist-based security tool that basically disables all the executable web content (javascript, java, flash, silverlight...) and lets the user choose which sites are "trusted". Nice feature: anti-XSS protection.


### Internet explorer

Internet Explorer, XSS Filter, which modifies reflected values in the following way:

```
# This payload
<svg/onload=alert(1)>
# is transformed to
<svg/#nload=alert(1)>
```

XSS Filter is enabled by default in the Internet but websites that want to opt-out of this protection can use the following response header:

```
X-XSS-Protection:0
```

Later on the Internet Explorer team introduced a new directive in the X-XSS-Protection header:

```
X-XSS-Protection:1; mode=block
```

With this directive, if a potential XSS attack is detected, the browser, rather than attempting to sanitize the page, will render a simple #. This directive has been implemented in other browsers.

### Chrome

Chrome has XSS Auditor. XSS Auditor is between the HTML Parser and the JS engine.

![XSS auditor](img/xss-auditor.png)

The filter analyzes both the inbound requests and the outbound. If executable code is found within the response, then it stops the script and generates a console alert.