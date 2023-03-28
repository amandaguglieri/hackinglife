

```bash
# Check connection
ping 8.8.8.8

# Check domain resolver
ping google.com

# If pinging 8.8.8.8 works but pinging google.com doesn't, check dns file resolver
	# Add a new line: 
	# nameserver 8.8.8.8
sudo nano /etc/resolv.conf

# Check wired connections
sudo service networking
```