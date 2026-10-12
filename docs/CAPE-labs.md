

# Active Directory LDAP

Find the user in the DNSAdmins group (first.last).

```
Get-ADGroup -Identity "DNSAdmins" -Properties *
```

Hazel.Lamb

How many users are in the Help Desk group?

```
Get-ADGroup -Identity "Help Desk" -Properties *
```

3

What OU is the Help Desk group managed by?

```
Get-ADGroup -Identity "Help Desk" -Properties *
```

Microsof Exchange Security Groups