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

# Create a new Resource group. Two things needed: a name and a location. Create variables for those:
$location = (Get-AzResourceGroup -Name resource-group_test1).Location
$rgName = "myresourcegroup"
New-AzResourceGroup -Name $rgName -Location $location

# A way to assign a variable to location if you want to replicate an existing location from another resource group 
$location = (Get-AzResourceGroup -Name $rgName).Location
```

### VMs

```
# List VMs
Get-AzVm


# Create a new VM
New-AzVm -ResourceGroupName $rgName -Name "MyVM01" -Image "UbuntLTS"
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

