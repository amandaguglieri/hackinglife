
# Intro

Accessing the VMs:

```
# Ssh connections requires extra flags
ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" learner@192.168.50.52
```

The UserKnownHostsFile=/dev/null and StrictHostKeyChecking=no options have been added to prevent the known-hosts file on our local Kali machine from being corrupted. This means that every time we connect, it will be treated like a new connection. **In the real world, using either (or both) of these options would open us up to man-in-the-middle attacks.** 