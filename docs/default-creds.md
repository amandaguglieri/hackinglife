


# Default Credentials Cheat Sheet

## Installation

```bash
git clone https://github.com/ihebski/DefaultCreds-cheat-sheet.git 
cd DefaultCreds-cheat-sheet 
pip3 install defaultcreds-cheat-sheet           
```


## Basic commands

```bash
 creds search mysql  
```

Returns:

```
+---------------------+-------------------+----------+
| Product             |      username     | password |
+---------------------+-------------------+----------+
| mysql               | admin@example.com |  admin   |
| mysql               |        root       | <blank>  |
| mysql (ssh)         |        root       |   root   |
| mysql               |      superdba     |  admin   |
| scrutinizer (mysql) |    scrutremote    |  admin   |
+---------------------+-------------------+----------+
```