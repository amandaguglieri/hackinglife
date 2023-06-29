---
title: 1521 - Oracle Transparent Network Substrate (TNS)  
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - oracle tns
  - port 1521
  - port 162
---

# 1521 - Oracle Transparent Network Substrate (TNS)

The Oracle Transparent Network Substrate (TNS) server is a communication protocol that facilitates communication between Oracle databases and applications over networks.  TNS supports various networking protocols between Oracle databases and client applications, such as IPX/SPX and TCP/IP protocol stacks. As a result, it has become a preferred solution for managing large, complex databases in the healthcare, finance, and retail industries. 

Addittionaly, it supports IPv6 and SSL/TLS encryption, which make it suitable for Name resolution, Connection management, Load balancing, Security.

Oracle TNS is often used with other Oracle services like Oracle DBSNMP, Oracle Databases, Oracle Application Server, Oracle Enterprise Manager, Oracle Fusion Middleware, web servers, and many more:

- Oracle Enterprise Manager: tool for start, stop, or restart an instance, adjust its memory allocation or other configuration parameters, and monitor its performance.

## Footprinting Oracle TNS

Let's now use nmap to scan the default Oracle TNS listener port:

```shell-session
sudo nmap -p1521 -sV <IP> --open
```

### Enumerating SIDs

In Oracle relational databases, also known as **Oracle RDBMS**, there are System Identifiers (`SID`).

>**System Identifiers (SID)** are a unique name that identifies a particular database instance. It can have multiple instances, each with its own System ID. An instance is a set of processes and memory structures that interact to manage the database's data. 
>
>The client uses this SID to identify which database instance it wants to connect to. If there is not a SID in the request, then, the default value defined in the `tnsnames.ora` file is used.


```shell-session
sudo nmap -p1521 -sV <IP> --open --script oracle-sid-brute
```


### More enumeration with ODAT

We can use the `odat.py`  from [ODAT](odat.md) tool to retrieve database names, versions, running processes, user accounts, vulnerabilities, misconfigurations,...

```shell-session
/odat.py all -s <IP>
```

Addittionaly, if you have sysdba admin rights, you might  upload a web shell to the target ([more in odat](odat.md))  

## Connect to Oracle database: sqlplus

If we manage to get some credentials we can connect to the Oracle TNS service with [sqlplus](sqlplus.md).

```shell-session
sqlplus <username>/<password>@<IP>/XE;
```

In case of this error message ( sqlplus: error while loading shared libraries: libsqlplus.so: cannot open shared object file: No such file or directory), there might be an issue with libraries. Possible solution:

```shell-session
sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig
```

The System Database Admin  in an Oracle RDBMS is **sysdba**. If an user has more privileges that they should have we can try to exploit it as sysdba.

```shell-session
sqlplus <user>/<password>@<IP>/XE as sysdba
```

## Upload a web shell

If we have sysdba admin rights, we might  upload a web shell to the target. This requires the server to run a web server, and we need to know the exact location of the root directory for the webserver.

```bash
# 1. Create a non suspicious web shell 
echo "Oracle File Upload Test" > testing.txt

# 2. Upload  the shell to linux (/var/www/html) or windows (C:\\inetpub\\wwwroot):
./odat.py utlfile -s <IP> -d XE -U <user> -P <password> --sysdba --putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt

## 3. Test if the file upload approach worked with curl, or visit via browser.
curl -X GET http://<IP>/testing.txt
```


## Oracle basic commands

```shell-session
# List all available tables in the current database
select table_name from all_tables;

# Show the privileges of the current user
select * from user_role_privs;

# If we have sysdba admin rights, we might:
	## 1. enumerate all databases
select * from user_role_privs;

	## 2. extract Password Hashes
select name, password from sys.user$;

	## 3. upload a web shell to the target. This requires the server to run a web server, and we need to know the exact location of the root directory for the webserver.
	## 1. Creating a non suspicious web shell 
echo "Oracle File Upload Test" > testing.txt
	## 2. Uploading the shell to linux (/var/www/html) or windows (C:\\inetpub\\wwwroot):
./odat.py utlfile -s <IP> -d XE -U <user> -P <password> --sysdba --putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt
```



## How does Oracle TNS work

### Technical components

**The listener**:  

By default, the listener listens for incoming connections on the TCP/1521 port. However, this default port can be changed during installation or later in the configuration file. The TNS listener is configured to support various network protocols, including TCP/IP, UDP, IPX/SPX, and AppleTalk. The listener can also support multiple network interfaces and listen on specific IP addresses or all available network interfaces. By default, Oracle TNS can be remotely managed in Oracle 8i/9i but not in Oracle 10g/11g. 


Additionally, the listener will use Oracle Net Services to encrypt the communication between the client and the server. 


**Configuration files for Oracle TNS**

The configuration files for Oracle TNS are called `tnsnames.ora` and `listener.ora` and are typically located in the `ORACLE_HOME/network/admin` directory. The client-side Oracle Net Services software uses the `tnsnames.ora` file to resolve service names to network addresses, while the listener process uses the `listener.ora` file to determine the services it should listen to and the behavior of the listener.

*tnsnames.ora*

> Each database or service has a unique entry in the [tnsnames.ora](https://docs.oracle.com/cd/E11882_01/network.112/e10835/tnsnames.htm#NETRF007) file, containing the necessary information for clients to connect to the service. The entry consists of a name for the service, the network location of the service, and the database or service name that clients should use when connecting to the service.

```txt
Code: txt
>ORCL =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)(HOST = 10.129.11.102)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVER = DEDICATED)
      (SERVICE_NAME = orcl)
    )
  )
```

*listener.ora*

>The `listener.ora` file is a server-side configuration file that defines the listener process's properties and parameters, which is responsible for receiving incoming client requests and forwarding them to the appropriate Oracle database instance.

```txt
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (SID_NAME = PDB1)
      (ORACLE_HOME = C:\oracle\product\19.0.0\dbhome_1)
      (GLOBAL_DBNAME = PDB1)
      (SID_DIRECTORY_LIST =
        (SID_DIRECTORY =
          (DIRECTORY_TYPE = TNS_ADMIN)
          (DIRECTORY = C:\oracle\product\19.0.0\dbhome_1\network\admin)
        )
      )
    )
  )

LISTENER =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = TCP)(HOST = orcl.inlanefreight.htb)(PORT = 1521))
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
    )
  )

ADR_BASE_LISTENER = C:\oracle
```


### Default passwords

+ Oracle 9 has a default password, CHANGE_ON_INSTALL.
- Oracle 10 has no default password set.
- The Oracle DBSNMP service also uses a default password, `dbsnmp`.

### PL/SQL Exclusion List

Oracle databases can be protected by using so-called PL/SQL Exclusion List (`PlsqlExclusionList`). It is a user-created text file that needs to be placed in the `$ORACLE_HOME/sqldeveloper` directory, and it contains the names of PL/SQL packages or types that should be excluded from execution. Once the PL/SQL Exclusion List file is created, it can be loaded into the database instance. It serves as a blacklist that cannot be accessed through the Oracle Application Server.

|**Setting**|**Description**|
|---|---|
|`DESCRIPTION`|A descriptor that provides a name for the database and its connection type.|
|`ADDRESS`|The network address of the database, which includes the hostname and port number.|
|`PROTOCOL`|The network protocol used for communication with the server|
|`PORT`|The port number used for communication with the server|
|`CONNECT_DATA`|Specifies the attributes of the connection, such as the service name or SID, protocol, and database instance identifier.|
|`INSTANCE_NAME`|The name of the database instance the client wants to connect.|
|`SERVICE_NAME`|The name of the service that the client wants to connect to.|
|`SERVER`|The type of server used for the database connection, such as dedicated or shared.|
|`USER`|The username used to authenticate with the database server.|
|`PASSWORD`|The password used to authenticate with the database server.|
|`SECURITY`|The type of security for the connection.|
|`VALIDATE_CERT`|Whether to validate the certificate using SSL/TLS.|
|`SSL_VERSION`|The version of SSL/TLS to use for the connection.|
|`CONNECT_TIMEOUT`|The time limit in seconds for the client to establish a connection to the database.|
|`RECEIVE_TIMEOUT`|The time limit in seconds for the client to receive a response from the database.|
|`SEND_TIMEOUT`|The time limit in seconds for the client to send a request to the database.|
|`SQLNET.EXPIRE_TIME`|The time limit in seconds for the client to detect a connection has failed.|
|`TRACE_LEVEL`|The level of tracing for the database connection.|
|`TRACE_DIRECTORY`|The directory where the trace files are stored.|
|`TRACE_FILE_NAME`|The name of the trace file.|
|`LOG_FILE`|The file where the log information is stored.|

