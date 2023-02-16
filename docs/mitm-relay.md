---
title: mitm_relay Suite
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - thick applications
---

# mitm_relay

Hackish way to intercept and modify non-HTTP protocols through Burp & others with support for SSL and STARTTLS interception

This script is a very simple, quick and easy way to MiTM any arbitrary protocol through existing traffic interception software such as Burp Proxy or [Proxenet](https://github.com/hugsy/proxenet). It can be particularly useful for thick clients security assessments. It saves you from the pain of having to configure specific setup to intercept exotic protocols, or protocols that can't be easily intercepted. TCP and UDP are supported.

It's "hackish" in the way that it was specifically designed to use interception and modification capabilities of existing proxies, but for arbitrary protocols. In order to achieve that, each client request and server response is wrapped into the body of a HTTP POST request, and sent to a local dummy "echo-back" web server via the proxy. Therefore, the HTTP responses or headers that you will see in your intercepting proxy are meaningless and can be disregarded. Yet the dummy web server is necessary in order for the interception tool to get the data back and feed it back to the tool.

-   The requests from client to server will appear as a request to a URL containing "CLIENT_REQUEST"
-   The responses from server to client will appear as a request to a URL containing "SERVER_RESPONSE"

This way, it is completely asynchronous. Meaning that if the server sends responses in successive packets it won't be a problem.

To intercept only server responses, configure your interception rules like so:

[![Intercept responses](https://camo.githubusercontent.com/b97b925d0f7c9a84eebac05c0d52584284eab12f8d296e2903d18a65dbd90c6a/68747470733a2f2f692e696d6775722e636f6d2f744f6d504e77472e706e67)](https://camo.githubusercontent.com/b97b925d0f7c9a84eebac05c0d52584284eab12f8d296e2903d18a65dbd90c6a/68747470733a2f2f692e696d6775722e636f6d2f744f6d504e77472e706e67)

"Match and Replace" rules can be used. However, using other Burp features such as repeater, intruder or scanner is pointless. That would only target the dummy webserver used to echo the data back.

The normal request traffic flow during typical usage would be as below:

[![Traffic flow](https://camo.githubusercontent.com/f74f1455e9651c49e47a31e3113ce6c25b72115e43cecfd00fec699ea7c62a10/68747470733a2f2f692e696d6775722e636f6d2f6d6e7676536b342e706e67)](https://camo.githubusercontent.com/f74f1455e9651c49e47a31e3113ce6c25b72115e43cecfd00fec699ea7c62a10/68747470733a2f2f692e696d6775722e636f6d2f6d6e7676536b342e706e67)



## Installation

Download from [GitHub - jrmdev/mitm_relay: Hackish way to intercept and modify non-HTTP protocols through Burp & others.](https://github.com/jrmdev/mitm_relay)

## Requirements

**1.** mitm_relay requires python 3. Also to make sure that it doesn't have a conflict with pip module, we can use version 3.7.6. Download from: https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe and install it. Once installed, restart the system.

**2.** Also, we can run in some problems like not having some modules installed, To get them installed, we would need to download getpip.py from https://github.com/amandaguglieri/python/blob/main/getpip.py 

After installing pip, to install a module, run:

```
python -m pip install <nameofmodule>
```



