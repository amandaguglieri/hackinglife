
# Windows System Internals
## Notes on the book

Install the NTObjectManager module:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

Install-Module NTObjectManager -Scope CurrentUser -Force

# If the module is already installed, make sure you have the latest version
Update-Module NTObjectManager

# Some underlying installs that will take place:
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force


# Once installed, Load the module
Import-Module NTObjectManager
```

Check installation:

```powershell
New-NTSecurityDescriptor

Owner DACL ACE Count SACL ACE Count Integrity Level
----- -------------- -------------- ---------------
NONE  NONE           NONE           NONE
```

