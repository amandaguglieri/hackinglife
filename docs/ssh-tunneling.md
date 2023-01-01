---
title: ssh tunneling
author: amandaguglieri
TableOfContents: true
draft:false
---

### Local port forwarding 

In this example we will use this tunneling as a way to access locally to a remote postgresql service: 

1. In the attacking machine:

```bash
ssh UserNameInTheAttackedMachine@IPOfTheAttackedMachine -L 1234:localhost:5432 
# We will listen for incoming connections on our local port 1234. When a client connects to our local port, the SSH client will forward the connection to the remote server on port 22. This allows the local client to access services on the remote server as if they were running on the local machine.
# We are forwarding traffic from any given local port, for instance 1234, to the port on which PostgreSQL is listening, namely 5432, on the remote server. We therefore specify port 1234 to the left of localhost, and 5432 to the right, indicating the target port.
```

2. In another terminal in the attacking machine:

```bash
sudo apt update && sudo apt install postgresql postgresql-client-common 
# this will install postgresql in case you don't have it.

psql -U christine -h localhost -p 1234
# Using our installation of psql, we can now interact with the PostgreSQL service running locally on the target machine:
# -U: to specify user.
# -h: to specify localhost. 
# -p 1234 as we are targeting the tunnel we created earlier with SSH, we need to specify which is the port the tunnel is listening on.
```

### Dynamic Port Forwarding
Unlike local port forwarding and remote port forwarding, which use a specific local and remote port (earlier we used 1234 and 5432, for instance), dynamic port forwarding uses a single local port and dynamically
assigns remote ports for each connection.

To use dynamic port forwarding with SSH, you can use the ssh command with the -D option, followed by the local port, the remote host and port, and the remote SSH server. For example, the following command will forward traffic from the local port 1234 to the remote server on port 5432, where the PostgreSQL server is running:

```bash
ssh UserNameInTheAttackedMachine@IPOfAttackedMachine -D 1234 
# -f send the command to the shell's background right before executing it remotely
# -N tells SSH not to execute any commands remotely.
```

As you can see, this time around we speciify a single local port to which we will direct all the traffic needing forwarding. 

If we now try running the same psql command as before, we will get an error. That is because this time around we did not specify a target port for our traffic to be directed to, meaning psql is just sending traffic into the established local socket on port 1234, but never reaches the To make use of dynamic port forwarding, a tool such as proxychains is especially useful. 

In summary and as the name implies, proxychains can be used to tunnel a connection through multiple proxies; a use case for this could be increasing anonymity, as the origin of a connection would be significantl more difficult to trace. 

In our case, we would only tunnel through one such "proxy"; the target machine. The tool is pre-installed on most pentesting distributions (such as ParrotOS and Kali Linux ) and is highly customisable, featuring an array of strategies for tunneling, which can be tampered with in itis configuration file /etc/proxychains4.conf.

The minimal changes that we have to make to the file for proxychains to work in our current use case is to:

1. Ensure that strict_chain is not commented out; ( dynamic_chain and random_chain should be commented out)
2. At the very bottom of the file, under [ProxyList], we specify the socks5 (or socks4 ) host and port that we used for our tunnel

In our case, it would look something like this, as our tunnel is listening at localhost:1234.
PostgreSQL service on the target machine.

```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4 127.0.0.1 9050
socks5 127.0.0.1 1234
```

Having configured proxychains correctly, we can now connect to the PostgreSQL service on the target, as if we were on the target machine ourselves! This is done by prefixing whatever command we want to run with proxychains:

```bash
proxychains psql -U NameOfUserOfAttackedMachine -h localhost -p 5432
```


