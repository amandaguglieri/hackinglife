---
title: iptables - Linux packet filtering and NAT framework  
author: amandaguglieri  
draft: false  
TableOfContents: true  
tags:
- firewall
- packetfiltering
- linux
- postexploitation
---

# iptables - Linux packet filtering and NAT framework

??? abstract "Sources of these notes"  
- `man iptables`, `man iptables-extensions`  
- Netfilter / iptables official documentation  
- Various Linux firewall hardening guides

> **Note**: Modern Linux systems often use `nftables` underneath, but `iptables` is still widely present and commonly encountered in CTFs, HTB, and real infra.

---

## Description

`iptables` is the user-space tool to configure the Linux kernel’s **Netfilter** firewall. It allows:

- Packet filtering (firewall)
- NAT (SNAT, DNAT, MASQUERADE)
- Packet mangling (change TOS, TTL, mark packets)
- Logging and rate limiting
    

Conceptually, packets traverse **tables**, which contain **chains**, which contain **rules**. Each rule matches packets and jumps to a **target** (`ACCEPT`, `DROP`, `REJECT`, `LOG`, `DNAT`, `SNAT`, `MASQUERADE`, etc.).

```shell-session
sudo iptables [-t table] COMMAND CHAIN [matches] -j TARGET
```

---

## Tables and Chains

### Tables

|Table|Purpose|Common chains|
|---|---|---|
|filter|Default; firewall rules|INPUT, OUTPUT, FORWARD|
|nat|Network Address Translation|PREROUTING, POSTROUTING, OUTPUT|
|mangle|Packet mangling (TTL, marks, QoS)|PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING|
|raw|Exempt packets from conntrack|PREROUTING, OUTPUT|
|security|SELinux-related rules|INPUT, OUTPUT, FORWARD|

### Built-in chains (filter table)

- **INPUT** – Packets _to_ the local machine
- **OUTPUT** – Packets _from_ the local machine
- **FORWARD** – Packets _through_ the machine (routing)
    

---

## Quick reference

### List rules

```bash
# All filter rules, numeric output, verbose
sudo iptables -L -n -v

# With rule numbers (very useful to delete)
sudo iptables -L -n --line-numbers

# NAT and mangle tables
sudo iptables -t nat -L -n -v
sudo iptables -t mangle -L -n -v

# Canonical representation (good for diffing)
sudo iptables -S           # filter
sudo iptables -t nat -S
```

### Flush / reset

```bash
# Flush all rules in filter table
sudo iptables -F

# Flush specific chain
sudo iptables -F INPUT

# Flush other tables
sudo iptables -t nat -F
sudo iptables -t mangle -F

# Reset default policies to ACCEPT (dangerous but useful in labs)
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
```

### Default policies

```bash
# Basic "default deny inbound, allow outbound" policy
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT
```

### Add / insert / delete rules

```bash
# Append rule
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Insert as first rule
sudo iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT

# Delete by full rule
sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT

# Delete by line number (from -L --line-numbers)
sudo iptables -D INPUT 3
```

---

## Basic firewall template (host firewall)

Typical “sane” host-based firewall:

```bash
# Reset
sudo iptables -F
sudo iptables -X

# Default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow loopback
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# Allow established/related traffic
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT

# Optional: allow ICMP (ping)
sudo iptables -A INPUT -p icmp -j ACCEPT
```

---

## Cheat Sheet

### Targeting hosts and ports

```bash
# Allow SSH from everywhere
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow SSH only from a specific IP
sudo iptables -A INPUT -p tcp --dport 22 -s 10.0.0.5 -j ACCEPT

# Drop traffic from a specific IP
sudo iptables -A INPUT -s 10.0.0.5 -j DROP

# Allow HTTP/HTTPS
sudo iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT

# Allow a specific subnet
sudo iptables -A INPUT -s 10.0.0.0/24 -j ACCEPT

# Block a specific port (e.g., SMB)
sudo iptables -A INPUT -p tcp --dport 445 -j DROP
```

### Connection tracking / states

```bash
# Allow established and related incoming traffic (almost always needed)
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop invalid packets
sudo iptables -A INPUT -m state --state INVALID -j DROP
```

### Rate limiting and brute-force protection

```bash
# Limit new SSH connections to 3 per minute
sudo iptables -A INPUT -p tcp --dport 22 \
  -m state --state NEW \
  -m limit --limit 3/min --limit-burst 5 \
  -j ACCEPT

# Basic example using 'recent' to block repeated SSH attempts
sudo iptables -A INPUT -p tcp --dport 22 \
  -m state --state NEW \
  -m recent --set --name SSH

sudo iptables -A INPUT -p tcp --dport 22 \
  -m state --state NEW \
  -m recent --update --seconds 60 --hitcount 5 --name SSH \
  -j DROP
```

### Logging

```bash
# Log then drop everything else at the end of INPUT
sudo iptables -A INPUT -m limit --limit 5/min \
  -j LOG --log-prefix "IPTABLES DROP: " --log-level 4

sudo iptables -A INPUT -j DROP
```

Logs usually appear in `/var/log/syslog`, `/var/log/messages`, or `journalctl` depending on distro.

---

## NAT and port forwarding

### Enable IPv4 forwarding

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Persistent (Debian/Ubuntu)
# /etc/sysctl.conf:
# net.ipv4.ip_forward = 1
# sudo sysctl -p
```

### Source NAT (SNAT / MASQUERADE)

Use this when the box is a gateway and you want internal hosts to reach the Internet.

```bash
# Typical lab: internal network on eth1, external on eth0
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

For static public IP:

```bash
sudo iptables -t nat -A POSTROUTING -o eth0 \
  -j SNAT --to-source 203.0.113.10
```

### Destination NAT (DNAT / port forwarding)

Forward traffic from external interface to an internal host:

```bash
# Forward incoming TCP/80 on eth0 to 192.168.1.10:8080
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 \
  -j DNAT --to-destination 192.168.1.10:8080

# Allow forwarding of the forwarded packets
sudo iptables -A FORWARD -p tcp -d 192.168.1.10 --dport 8080 -j ACCEPT
```

---

## Mangle table and packet marking

```bash
# Mark incoming HTTP packets
sudo iptables -t mangle -A PREROUTING -p tcp --dport 80 \
  -j MARK --set-mark 1

# Example routing based on mark (outside of iptables):
# ip rule add fwmark 1 table special
# ip route add default via 10.0.0.1 table special
```

You may also adjust TOS/TTL (less common in CTFs, more in traffic engineering).

---

## iptables in pentesting / post-exploitation

Quick things you might need on a compromised box:

```bash
# 1. See what firewall rules are blocking you
sudo iptables -L -n -v
sudo iptables -t nat -L -n -v

# 2. Open a port for a reverse shell listener
sudo iptables -A INPUT -p tcp --dport 4444 -j ACCEPT

# 3. Temporarily disable the firewall (very noisy, but useful in labs)
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# 4. Stealthier: allow yourself in without destroying existing policy
sudo iptables -I INPUT 1 -p tcp --dport 22 -s YOUR.IP.HERE -j ACCEPT
```

---

## Saving and restoring rules

### Using iptables-save / iptables-restore

```bash
# Save current rules to a file
sudo iptables-save > /root/iptables.rules

# Restore from a file
sudo iptables-restore < /root/iptables.rules
```

### Debian / Ubuntu style persistence

```bash
# Install helpers
sudo apt install iptables-persistent

# Save rules
sudo netfilter-persistent save
# or manually:
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

### RHEL / CentOS / older systems

```bash
sudo service iptables save
# or
sudo /etc/init.d/iptables save
```

(Exact commands depend on distro and whether `firewalld` is in use.)

---

## Debugging and troubleshooting

```bash
# Show counters for each rule
sudo iptables -L -n -v

# Reset counters (to see which rule hits afterwards)
sudo iptables -Z

# Show numeric output (no DNS lookups, faster, clearer)
sudo iptables -L -n

# Check for connection tracking behavior
sudo iptables -t raw -L -n -v
```

Useful pattern while debugging:

1. `iptables -L -n -v --line-numbers`
    
2. Generate some traffic (curl, ping, nc, etc.)
    
3. Run the command again and see which rule’s counters increased.
    

---

## IPv6: ip6tables

For IPv6, rules are maintained separately with `ip6tables`:

```bash
sudo ip6tables -L -n -v
sudo ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
```

On many modern distros, `nftables` may handle both IPv4 and IPv6 with a unified config, but in CTFs you will often still see `iptables` / `ip6tables`.

---