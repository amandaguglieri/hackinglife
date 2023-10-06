---
title: Azure Powershell
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - azure
  - powershell
---

# Azure Powershell

See all available releases for powershell: [https://github.com/PowerShell/PowerShell/releases](https://github.com/PowerShell/PowerShell/releases).

Azure powershell documentation: [https://learn.microsoft.com/en-us/powershell/azure/?view=azps-10.3.0](https://learn.microsoft.com/en-us/powershell/azure/?view=azps-10.3.0)

**Az** is the formal name for the Azure PowerShell module containing cmdlets to work with Azure features. It contains hundreds of cmdlets that let you control nearly every aspect of every Azure resource. You can work with the following features, and more: Resource groups, Storage, VMs, Azure AD, Containers, Machine learning.

## Installation

```powershell
# Get version of the installed AZ module
Get-InstalledModule -Name Az -AllVersions | Select-Object -Property Name, Version

# To install a new AZ Module, run as Administrator
Install-Module -Name Az -AllowClobber -Repository PSGallery -Force

# To update a new AZ Module, run as Administrator
Update-Module -Name Az -AllowClobber -Repository PSGallery
```

You can have several versions of Powershell Azure installed.

### 
Installation on Linux


The Az PowerShell module is available from a global repository called the PowerShell Gallery. You can install the module onto your local machine through the Install-Module cmdlet.

In a terminal, run the following command to launch PowerShell.

```bash
#  launch PowerShell
pwsh
```

Run the following command at the PowerShell prompt to install Azure PowerShell.

```powershell
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
```

Update a PowerShell module

```powershell
Update-Module -Name Az
```

## Basic commands

For an account to work, you need a subscription. Additionally, you will need to create several resources: a resource group, an storage account and a file share.

```powershell
# First, connect to your Azure account
Connect-AzAccount

# List your subscriptions 
Get-AzSubscription

# Set a variable name for your subscription context and set context in Azure
$context = Get-AzSubscription -SubscriptionId <ID>
# Set context 
Set-AzContext $context
```

### Resource Groups

```
# List existing Resource Groups
Get-AzResourceGroup

# Get a list of existing resource group with a table format
Get-AzResourceGroup | Format-Table

# Create a new Resource group. Two things needed: a name and a location. Create variables for those:
$location = (Get-AzResourceGroup -Name resource-group_test1).Location
$rgName = "myresourcegroup"
New-AzResourceGroup -Name $rgName -Location $location

# A way to assign a variable to location if you want to replicate an existing location from another resource group 
$location = (Get-AzResourceGroup -Name $rgName).Location


# Delete resource groups
Remove-AzResourceGroup -Name "ContosoRG01"

```

### Resources

```powershell
# List resources
Get-AzResource

# List resources witha table format 
Get-AzResource | Format-Table

# Filter resources by resourcegroups
Get-AzResource -ResourceGroupName ExerciseResources

```


### VMs

```
# List VMs in your subscription
Get-AzVm -Status


# Create a new VM
New-AzVm -ResourceGroupName learn-c6274d0c-2c2a-404d-a592-6d5cc97d594a -Name "testvm-eus-01" -Credential (Get-Credential) -Location "eastus" -Image Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest -OpenPorts 22 -PublicIpAddressName "testvm-eus-01"

# Save your VM in a variable and update it
$vm = (Get-AzVM -Name "testvm-eus-01" -ResourceGroupName learn-c6274d0c-2c2a-404d-a592-6d5cc97d594a)

# Dump info about your new VM
$vm

# reach into complex objects through a dot (.) notation. 
$vm.HardwareProfile
$vm.StorageProfile.OsDisk

#  pass the VM object into other cmdlets. For example, running the following command shows you all available sizes for your VM:
$vm | Get-AzVMSize

# get your public IP address:
Get-AzPublicIpAddress -ResourceGroupName learn-c6274d0c-2c2a-404d-a592-6d5cc97d594a -Name "testvm-eus-01"

# With the IP address, you can connect to the VM with SSH. For example, if you used the username `bob`, and the IP address is `205.22.16.5`, running this command would connect to the Linux machine:
ssh bob@205.22.16.5

$vm.HardwareProfile.vmSize = "Standard_DS3_v2"
Update-AzVM -ResourceGroupName $ResourceGroupName  -VM $vm

# Shut VM down
Stop-AzVM -Name $vm.Name -ResourceGroupName $vm.ResourceGroupName

# When the VM has stopped, delete the VM by running the Remove-AzVM
Remove-AzVM -Name $vm.Name -ResourceGroupName $vm.ResourceGroupName

# Run this command to list all the resources in your resource group:
Get-AzResource -ResourceGroupName $vm.ResourceGroupName | Format-Table
```


```
# Results:
Microsoft.Compute/disks
Microsoft.Network/networkInterfaces
Microsoft.Network/networkSecurityGroups
Microsoft.Network/publicIPAddresses
Microsoft.Network/virtualNetworks
```

The `Remove-AzVM` command _just deletes the VM_. It doesn't clean up any of the other resources.

To clean them:

```
# Deleting the network interface
$vm | Remove-AzNetworkInterface –Force

# Deleting the managed OS disk
Get-AzDisk -ResourceGroupName $vm.ResourceGroupName -DiskName $vm.StorageProfile.OSDisk.Name | Remove-AzDisk -Force

# Delete the virtual network
Get-AzVirtualNetwork -ResourceGroupName $vm.ResourceGroupName | Remove-AzVirtualNetwork -Force

# Delete the network security group
Get-AzNetworkSecurityGroup -ResourceGroupName $vm.ResourceGroupName | Remove-AzNetworkSecurityGroup -Force

# Delete the Public IP
Get-AzPublicIpAddress -ResourceGroupName $vm.ResourceGroupName | Remove-AzPublicIpAddress -Force

```




### Storage accounts


```
# List VMs
Get-AzStorageAccount

```

### File Disk

```
# List all File shares
Get-AzDisk

# Create a new configuration for your File Disk
$myDiskConfig = New-AzDiskConfig -Location $location -CreateOption Empty -DiskSizeGB 32 -Sku Standard_LRS

# Create the file disk. First assign a variable for the disk name
$myDiskName = "myDiskname"
New-AzDisk -ResourceGroupName $myresourcegroup -DiskName $myDiskName -Disk $myDiskConfig

# Increase size of an existing Az Disk
New-AzDiskUpdateConfig -DiskSize 64 | Update-AzDisk -ResourceGroup $rgName -DiskName $myDiskName

# Get current SKU of a given Az Disk
(Get-AzDisk -ResourceGroupName rg-test2 -Name myDiskName).Sku  

# Update an Standard_LRS SKU to a premium one 
New-AzDiskUpdateConfig -Sku Premium_LRS | Update-AzDisk -ResourceGroupName $rgName -DiskName $myDiskName

```



### WebApps

```
# List webapps and provide name and location
Get-AzWebapp | Select-Object Name, Location

```


## Scripting

### Windows PowerShell Integrated Scripting Environment (ISE)


![Sample](img/az-104_2.png)

Once you've written the script, execute it from the PowerShell command line by passing the name of the file preceded by a dot and a backslash:

```powershell
.\myscript.ps1
```

Variables can hold objects. For example, the following definition sets the **adminCredential** variable to the object returned by the **Get-Credential** cmdlet.

```powershell
$adminCredential = Get-Credential
```

To obtain the value stored in a variable, use the `$` prefix and its name, as in the following:

```powershell
$loc = "East US"
New-AzResourceGroup -Name "MyResourceGroup" -Location $loc
```

To achieve a for loop:

```powershell
For ($i = 1; $i -lt 3; $i++)
{
    $i
}
```

The comparison operators are written `-lt` for "less than," `-le` for "less than or equal," `-eq` for "equal," `-ne` for "not equal".


When you execute a script, you can pass arguments on the command line. You can provide names for each parameter to help the script extract the values. For example:


```powershell
.\setupEnvironment.ps1 -size 5 -location "East US"
```

Inside the script, you'll capture the values into variables. In this example, the parameters are matched by name:


```powershell
param([string]$location, [int]$size)
```

You can omit the names from the command line. For example:

```powershell
.\setupEnvironment.ps1 5 "East US"
```

Inside the script, you'll rely on position for matching when the parameters are unnamed:

```powershell
param([int]$size, [string]$location)
```

We could take these parameters as input and use a loop to create a set of VMs from the given parameters. We'll try that next.


This is an example of a script for creating VMs

```powershell
param([string]$resourceGroup)

$adminCredential = Get-Credential -Message "Enter a username and password for the VM administrator."

For ($i = 1; $i -le 3; $i++)
{
    $vmName = "ConferenceDemo" + $i
    Write-Host "Creating VM: " $vmName
    New-AzVm -ResourceGroupName $resourceGroup -Name $vmName -Credential $adminCredential -Image Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest
}
```

To run this script:

```powershell
./ConferenceDailyReset.ps1 learn-c6274d0c-2c2a-404d-a592-6d5cc97d594a
```

