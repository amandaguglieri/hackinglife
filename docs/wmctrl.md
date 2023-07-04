

```bash
sudo apt-get install wmctrl
```



```bash
#!/bin/bash
wmctrl -s 0
/bin/bash
firefox https://enterprise.hackthebox.com/login &
obsidian &
Google Chrome &
riseup-vpn --start-vpn on 
sleep 5
wmctrl -r /bin/bash -t 0
wmctrl -r firefox -t 1
wmctrl -r obsidian -t 2
wmctrl -r riseup-vpn -t 3
wmctrl -s 0
```
