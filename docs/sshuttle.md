

# sshuttle Cheat Sheet

`sshuttle` is a "VPN over SSH" tool that transparently routes traffic to remote networks via an SSH tunnel.

Important: `sshuttle` routes **TCP traffic only**, not raw IP packets. This is key as, for instance, we will find issues with running nmap.

## Installation

In my case, in my virtualenv tooling:

```
pyenv activate tooling
pip install sshuttle
```

## Basic Usage

```bash
sshuttle -r user@pivot-host subnet
```

**Example:**

```bash
sshuttle -r root@10.129.242.211 172.16.8.0/16
```

This routes all traffic to `172.16.8.0/16` through the pivot.


### Using an SSH Key

```bash
sshuttle -r root@10.129.242.211 \
  --ssh-cmd "ssh -i ~/.ssh/dmz01_key" \
  172.16.8.0/16
```


### Custom SSH Port

```bash
sshuttle -r root@10.129.242.211 \
  --ssh-cmd "ssh -i ~/.ssh/dmz01_key -p 2222" \
  172.16.8.0/16
```


### Verbose Output for Debugging

```bash
sshuttle -v -r root@10.129.242.211 172.16.8.0/16
```


### Multiple Subnets

```bash
sshuttle -r root@10.129.242.211 \
  172.16.8.0/16 10.0.0.0/8
```


## ✅  Troubleshooting nmap
Most `nmap` scan types use raw packets (not TCP). When you run a typical `nmap` scan like:

```
nmap -sS 172.16.8.20
```

It uses a **SYN scan**, which sends **raw TCP SYN packets** directly via raw sockets or `libpcap`. These:

- **Bypass** the system's TCP stack
- **Do not go through `sshuttle`**, which routes only normal TCP connections
    

So `nmap`'s probes never reach the target.


**How to make `nmap` work with `sshuttle`**

Force `nmap` to use **normal TCP connections** that `sshuttle` can route:

```
nmap -sT 172.16.8.20 -Pn
```



##  sshuttle vs Ligolo-ng

| Feature                                 | `sshuttle`                      | Ligolo-ng                                                    |
| --------------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| **Transport**                           | SSH                             | Custom agent + TLS tunnel                                    |
| **Setup complexity**                    | Simple, native to Python        | Slightly more complex (requires deploying an agent on pivot) |
| **Raw traffic support**                 | ❌ Only TCP                      | ✅ Supports TCP & ICMP (if using TUN mode)                    |
| **ICMP support**                        | ❌ No                            | ✅ Yes (with TUN mode)                                        |
| **Tool footprint**                      | Minimal                         | Requires deploying binary on the pivot                       |
| **Stealth**                             | Medium (uses SSH)               | High (can use mutual TLS, encryption, and obfuscation)       |
| **Cross-platform support**              | Linux/macOS                     | Linux/Windows (agent runs on both)                           |
| **Socks proxy mode**                    | ✅ via `ssh -D` or system routes | ✅ Built-in SOCKS support                                     |
| **Packet injection (e.g., `nmap -sS`)** | ❌ (must use `-sT`)              | ✅ (when using TUN mode)                                      |
