


# ldapsearch

LDAP anonymous binds allow unauthenticated attackers to retrieve information from the domain, such as a complete listing of users, groups, computers, user account attributes, and the domain password policy.


For example, `ldapsearch` is a command-line utility used to search for information stored in a directory using the LDAP protocol. It is commonly used to query and retrieve data from an LDAP directory service.


```bash
ib2
-H ldap://ldap.example.com:389 -D "cn=admin,dc=example,dc=com" -w secret123 -b "ou=people,dc=example,dc=com" "(mail=john.doe@example.com)"

```

This command can be broken down as follows:

- Connect to the server `ldap.example.com` on port `389`.
- Bind (authenticate) as `cn=admin,dc=example,dc=com` with password `secret123`.
- Search under the base DN `ou=people,dc=example,dc=com`.
- Use the filter `(mail=john.doe@example.com)` to find entries that have this email address.

The server would process the request and send back a response, which might look something like this:

```ldap
dn: uid=jdoe,ou=people,dc=example,dc=com
objectClass: inetOrgPerson
objectClass: organizationalPerson
objectClass: person
objectClass: top
cn: John Doe
sn: Doe
uid: jdoe
mail: john.doe@example.com
```

This response includes the entry's `distinguished name (DN)` that matches the search criteria and its attributes and values.


#### Basic use in Domain context

```shell-session
ldapsearch -h $ip -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "

ldapsearch -x -H ldap://$ip -b "DC=CASCADE,DC=LOCAL" "(objectClass=user)" | grep sAMAccountName: | cut -f2 -d" "

```

Other tools related to ldap: `windapsearch.py`, `ldapsearch`, `ad-ldapdomaindump.py`.

Example from the hutch.offsec machine:

```bash
ldapsearch -v -x -D fmcsorley@hutch.offsec -w CrabSharkJellyfish192 -b "DC=hutch,DC=offsec" "(ms-MCS-AdmPwd=*)" ms-MCS-AdmPwd -H LDAP://192.168.116.122 
```


```bash
# # ldapsearch -x -H ldap://$ip -D '<DOMAIN>\<username>' -w '<password>' -b "CN=Users,DC=<1_SUBDOMAIN>,DC=<TLD>"

ldapsearch -x -H ldap://support.htb -D 'support\ldap' -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -b "CN=Users,DC=support,DC=htb"
```
