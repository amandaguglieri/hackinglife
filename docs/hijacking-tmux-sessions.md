---
title: Hijacking Tmux Sessions
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - privilege
  - escalation
  - linux
  - tmux
---
# Hijacking Tmux Sessions

Terminal multiplexers such as [tmux](https://en.wikipedia.org/wiki/Tmux) can be used to allow multiple terminal sessions to be accessed within a single console session.

For many reasons, a user may leave a `tmux` process running as a privileged user, such as root set up with weak permissions, and can be hijacked. This may be done with the following commands to create a new shared session and modify the ownership.

---

## **🛠️ Step-by-Step Breakdown of the Attack**

The first two steps are not the attack, but the conditions that posibilitates the attack.

### **1️⃣ `tmux` is Started as Root with a Shared Socket**

```
tmux -S /shareds new -s debugsess`
```

- This command **creates a new tmux session named `debugsess`**.
- The `-S /shareds` option **sets up a custom Unix domain socket at `/shareds`** instead of the default `/tmp/tmux-<uid>/`.
- Since the user running the command is **root**, the session runs with **root privileges**.

---

### **2️⃣ Changing Ownership of the tmux Socket File**

```
chown root:devs /shareds
```

- This changes the ownership of the **tmux socket (`/shareds`)** to:
    - **User:** `root`
    - **Group:** `devs`
- The **group `devs` now has access to attach to the session.**

---

### **3️⃣ Attacker Checks for Running `tmux` Sessions**

```
ps aux | grep tmux
```

- This command lists all running processes that contain "tmux."
- The attacker sees:

```
root      4806  0.0  0.1  29416  3204 ?        Ss   06:27   0:00 tmux -S /shareds new -s debugsess`
```

- **Key takeaways:**
    - The `tmux` session is **running as root**.
    - The socket file is located at **`/shareds`**.

---

### **4️⃣ Checking Permissions on the tmux Socket**

```
ls -la /shareds
``` 

- Output:

```
srw-rw---- 1 root devs 0 Sep  1 06:27 /shareds`
```

- **Breakdown of permissions (`srw-rw----`)**:
    - `s` → **Socket file**.
    - `rw- rw- ---` → **Owner (`root`) and group (`devs`) can read/write to it**.
    - `---` → **Other users cannot access it**.

🔴 **Dangerous Misconfiguration!**

- Any user in the `devs` group can **attach to this session**.
- Since **the session is running as root**, **attaching grants full root access**.

---

### **5️⃣ Attacker Confirms Group Membership**

```
id
```

- Output:

```
uid=1000(htb) gid=1000(htb) groups=1000(htb),1011(devs)
```
 
- The attacker (`htb`) is **part of the `devs` group**, meaning they have access to the `/shareds` socket.

---

### **6️⃣ Attacker Hijacks the Root `tmux` Session**

```
tmux -S /shareds
```

- The attacker **attaches to the existing root session**.

Once inside, they run:

```
id
```

- Output:

```
uid=0(root) gid=0(root) groups=0(root)`
```

✅ **The attacker now has a full root shell!** 🎉



---

## Summary

- **Flaw:** Root starts a **shared tmux session** with weak permissions (`root:devs`).
- **Attack:** Attacker, part of `devs`, attaches to the session and **gets a root shell**.
- **Fix:** **Restrict access to the tmux socket file** (`chmod 600 /shareds`) and **avoid assigning sensitive groups**.