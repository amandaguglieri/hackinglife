


# weevely

Weevely is **a stealth PHP web shell that simulate telnet-like connection**. It is an essential tool for web application post exploitation, and can be used as stealth backdoor or as a web shell to manage legit web accounts, even free hosted ones.

```bash
# Run terminal to the target
 weevely <URL> <password> [cmd]

# Generate backdoor agent
weevely generate <password> <path/to/save/your/phpBackdoorNamefile.php>

# Load session file
weevely session <path>
```

Upload weevely PHP agent to a target web server to get remote shell access to it. It has more than 30 modules to assist administrative tasks, maintain access, provide situational awareness, elevate privileges, and spread into the target network.

Read the [Install](https://github.com/epinna/weevely3/wiki/Install) page to install weevely and its dependencies.

Read the [Getting Started](https://github.com/epinna/weevely3/wiki/Getting-Started) page to generate an agent and connect to it.

Browse the [Wiki](https://github.com/epinna/weevely3/wiki) to read examples and use cases.