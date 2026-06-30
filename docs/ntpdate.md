

## Troubleshooting  Clock skew too great for OSCP+

```
# With VPN closed, syncronize to google time:
sudo ntpdate time.google.com

# And after that, connect to the VPN
```


## Troubleshooting  88 not reachable from attacking machine HTB

First we use  ligolo to redirect the internal service 88.

Our kali attacking machine has netowork interface 10.10.15.140.

Out target machine is at 10.128.18.220. 

We gain a foothold at the target and notice an internal website running at 127.0.0.1:88. 

When trying to generate a ticket with impacket, the request gets frozen.  We need to establish a tunnel and a reverse connection to redirect the 127.0.0.1 traffic to our kali and be able this way to open our browser and browse that internal site.

In our kali:

```bash
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
sudo ip route add 240.0.0.1/32 dev ligolo
```

Then we launch the proxy and the agent as usual. 

```
./proxy -selfcert
./ligolo-ng-proxy-linux_amd64 -selfcert 
```

The key piece here is:

```
sudo ip route add 240.0.0.1/32 dev ligolo
```

All we have to do now is run again the command to get the ticket:

```
getTGT.py -dc-ip 240.0.0.1 EIGHTEEN.HTB/adam.scott:'iloveyou1'
```

Then another error we may need to troubleshout is:

```
└─$ getTGT.py -dc-ip 240.0.0.1 EIGHTEEN.HTB/adam.scott:'iloveyou1'
Impacket v0.14.0.dev0+20251209.143744.82a5a8f0 - Copyright Fortra, LLC and its affiliated companies 

Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)

```

To bypass it we will update the clock in our machine to syncronize it with the target DC:

First get the time of the server:

```
└─$ getTGT.py -debug -dc-ip 240.0.0.1 EIGHTEEN.HTB/adam.scott:'iloveyou1'
Impacket v0.14.0.dev0+20251209.143744.82a5a8f0 - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /home/kali/.pyenv/versions/tooling/lib/python3.11/site-packages/impacket
[+] Trying to connect to KDC at 240.0.0.1:88
[+] Trying to connect to KDC at 240.0.0.1:88
[+] Server time (UTC): 2026-04-02 01:34:07
Traceback (most recent call last):

```

Use it: [+] Server time (UTC): 2026-04-02 01:34:07

```
sudo timedatectl set-timezone UTC

sudo date -s "2026-04-02 01:34:07"
```

and now:

```
─$ getTGT.py -dc-ip 240.0.0.1 EIGHTEEN.HTB/adam.scott:'iloveyou1'       
Impacket v0.14.0.dev0+20251209.143744.82a5a8f0 - Copyright Fortra, LLC and its affiliated companies 

[*] Saving ticket in adam.scott.ccache

```


Perfect