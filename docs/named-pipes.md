---
title: 25672 - Erlang Port
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - privilege
  - escalation
  - windows
---
# Named Pipes


Pipes are used for communication between two applications or processes using shared memory. There are two types of pipes, [named pipes](https://docs.microsoft.com/en-us/windows/win32/ipc/named-pipes) and anonymous pipes. An example of a named pipe is `\\.\PipeName\\ExampleNamedPipeServer`.

Windows systems use a client-server implementation for pipe communication. In this type of implementation, the process that creates a named pipe is the server, and the process communicating with the named pipe is the client.

Named pipes can communicate using `half-duplex`, or a one-way channel with the client only being able to write data to the server, or `duplex`, which is a two-way communication channel that allows the client to write data over the pipe, and the server to respond back with data over that pipe.

We can use the tool [PipeList](https://docs.microsoft.com/en-us/sysinternals/downloads/pipelist) from the Sysinternals Suite to enumerate instances of named pipes.

Pipes are essentially files stored in memory that get cleared out after being read.

```cmd
# Listing Named Pipes with Pipelist from cmd
pipelist.exe /accepteula

```

Additionally, we can use PowerShell to list named pipes using gci (Get-ChildItem).

```powershell-session
gci \\.\pipe\
```


After obtaining a listing of named pipes, we can use [Accesschk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk) to enumerate the permissions assigned to a specific named pipe by reviewing the Discretionary Access List (DACL)), which shows us who has the permissions to modify, write, read, or execute a resource.

```
# Reviewing LSASS Named Pipe Permissions
.\accesschk.exe /accepteula \\.\Pipe\lsass -v

# Reviewing all named pipes
.\accesschk.exe /accepteula \pipe\.
```

## Attack example

Let's walk through an example of taking advantage of an exposed named pipe to escalate privileges. 

Using accesschk we can search for all named pipes that allow write access:

```
.\accesschk.exe -w \pipe\* -v
```

Note in the output if there is any named pipe that allows `READ` and `WRITE` access to the `Everyone` group, meaning all authenticated users. For instance, let's say `WindscribeService` does.

Check `WindscribeService` Named Pipe Permissions:

```powershell
.\accesschk.exe -accepteula -w \pipe\WindscribeService -v
```

Output:

```powershell
Accesschk v6.13 - Reports effective permissions for securable objects
Copyright ⌐ 2006-2020 Mark Russinovich
Sysinternals - www.sysinternals.com

\\.\Pipe\WindscribeService
  Medium Mandatory Level (Default) [No-Write-Up]
  RW Everyone
        FILE_ALL_ACCESS
```

From here, we could leverage these lax permissions to escalate privileges on the host to SYSTEM.

Check if the service is running as SYSTEM:

```
wmic service where name="WindscribeService" get name, startname
```

If `StartName` is `LocalSystem`, we have a potential privilege escalation vector.


Craft a Malicious Named Pipe Server
