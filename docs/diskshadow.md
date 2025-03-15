
# Diskshadow

Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS). By default, Diskshadow uses an interactive command interpreter similar to that of Diskraid or Diskpart. [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow)

See an use example in [Abusing Windows Group privileges](windows-group-privileges.md).

|Command|Description|
|---|---|
|[set command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set)|Sets the context, options, verbose mode, and metadata file for creating shadow copies.|
|[load metadata command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/load-metadata)|Loads a metadata .cab file prior to importing a transportable shadow copy or loads the writer metadata in the case of a restore.|
|[writer command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/writer)|verifies that a writer or component is included or excludes a writer or component from the backup or restore procedure.|
|[add command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/add)|Adds volumes to the set of volumes that are to be shadow copied, or adds aliases to the alias environment.|
|[create command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/create)|Starts the shadow copy creation process, using the current context and option settings.|
|[exec command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/exec)|Executes a file on the local computer.|
|[begin backup command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/begin-backup)|Starts a full backup session.|
|[end backup command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/end-backup)|Ends a full backup session and issues a **backupcomplete** event with the appropriate writer state, if needed.|
|[begin restore command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/begin-restore)|Starts a restore session and issues a **prerestore** event to involved writers.|
|[end restore command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/end-restore)|Ends a restore session and issues a **postrestore** event to involved writers.|
|[reset command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reset)|Resets Diskshadow to the default state.|
|[list command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/list)|Lists writers, shadow copies, or currently registered shadow copy providers that are on the system.|
|[delete shadows command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/delete-shadows)|Deletes shadow copies.|
|[import command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/import)|Imports a transportable shadow copy from a loaded metadata file into the system.|
|[mask command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mask)|Removes hardware shadow copies that were imported by using the **import** command.|
|[expose command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/expose)|Exposes a persistent shadow copy as a drive letter, share, or mount point.|
|[unexpose command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/unexpose)|Unexposes a shadow copy that was exposed by using the **expose** command.|
|[break command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/break_2)|Disassociates a shadow copy volume from VSS.|
|[revert command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/revert)|Reverts a volume back to a specified shadow copy.|
|[exit command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/exit)|Exits the command interpreter or script.|


