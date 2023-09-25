---
title: Azure-CLI
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - azure
  - bash
  - azure-cli
---

# Azure-CLI

The Azure CLI is a command-line interface.  A cross-platform command-line program (Windows, Linux and macOs) to connect to Azure and execute administrative commands. 

It’s an executable program that you can use to execute commands in Bash. You can use the Azure CLI to perform every possible management task in Azure. Like Azure PowerShell, the CLI allows you to run one-off commands or you can combine them into a script and execute them together.

Azure CLI is a command-line program to connect to Azure and execute administrative commands on Azure resources. It runs on Linux, macOS, and Windows, and allows administrators and developers to execute their commands through a terminal, command-line prompt, or script instead of a web browser.


## Basic usage

```
# Launch Bash from Azure Cloud Shell
bash

# you can use the letters az to start an Azure command 
az upgrade

# Launch Azure CLI interactive mode
az interactive
```

### Help

```
# Getting help. If you want to find commands that might help you manage a storage blob, you can use the find command:
az find blob

# If you already know the name of the command you want, the `--help` argument
az storage blob --help
```


### Output

```
# Results in a json format by default
az group list

# Results in a line format
az group list --out tsv

# Results in a table
az group list --out table
```


### Resource groups

```
# List resource groups
az group list
# remember you can format output

# Retrieve properties from an existing and known resource group
az group show --name myresourcegroup

# From a specific resource group (provided, for instance, its name), query a value. Querying location:
az group show --name rg-test2 --query location --out table

# Querying id
az group show --name rg-test2 --query id --out table

# Create a Resource group
az group create --name mynewresource --location westeurope
```


### Disk

```
# List disks
az disk list

# Retrieve the properties of an existing Disk
az disk show --name myDiskname --resource-group rg-test2

# Retrieve the properties of an existing Disk, and output it in a table
az disk show --name myDiskname --resource-group rg-test2 --out table


# Create a new disk
az disk create --resource-group $myResourceGroup --name $mynewDisk --sku "Standard_LRD" --size-gb 32

# Increase the size of a disk
az disk update --resource-group $myResourceGroup --name $myDiskName --size-gb 64

# Change standard SKU to premium
az disk update --resource-group $myResourceGroup --name $myDiskName --sku "Premium_LRS"

# Verify size of a disk by querying size
az disk show --resource-group $myResourceGroup --name $myDiskName --query diskSizeGb --out table
```


### VMs

```
# Check running VMs
az vm list

# List IP addresses 
az vm list-ip-addres ses

# Create a VM with UbuntuLTS
az vm create --resourcegroup MyResourceGroup --name MyVM01 --image UbuntLTS --generate-ssh-keys

# Create a VM
az vm create --resource-group learn-857e3399-575d-4759-8de9-0c5a22e035e9 --name my-vm  --public-ip-sku Standard --image Ubuntu2204 --admin-username azureuser  --generate-ssh-keys

# Restart existing VM
az vm restart -g MyResourceGroup -n MyVm

# Configure Nginx on your VM
az vm extension set  --resource-group learn-857e3399-575d-4759-8de9-0c5a22e035e9  --vm-name my-vm  --name customScript  --publisher Microsoft.Azure.Extensions  --version 2.1  --settings '{"fileUris":["https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"]}'  --protected-settings '{"commandToExecute": "./configure-nginx.sh"}'

# Create a variable with public IP address: Run the following `az vm list-ip-addresses` command to get your VM's IP address and store the result as a Bash variable:
IPADDRESS="$(az vm list-ip-addresses --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --name my-vm --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" --output tsv)"
```

### NSG (Network Security Groups)

```
# Run the following `az network nsg list` command to list the network security groups that are associated with your VM:
az network nsg list --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --query '[].name' --output tsv

# You see this:
# my-vmNSG 
# Every VM on Azure is associated with at least one network security group. In this case, Azure created an NSG for you called _my-vmNSG_.
# Run the following `az network nsg rule list` command to list the rules associated with the NSG named _my-vmNSG_:
az network nsg rule list --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --nsg-name my-vmNSG

# Run the `az network nsg rule list` command a second time. This time, use the `--query` argument to retrieve only the name, priority, affected ports, and access (**Allow** or **Deny**) for each rule. The `--output` argument formats the output as a table so that it's easy to read.
az network nsg rule list --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --nsg-name my-vmNSG --query '[].{Name:name, Priority:priority, Port:destinationPortRange, Access:access}' --output table
# You see this:
# Name              Priority    Port    Access
# -----------------  ----------  ------  --------
# default-allow-ssh  1000        22      Allow

# By default, a Linux VM's NSG allows network access only on port 22. This enables administrators to access the system. You need to also allow inbound connections on port 80, which allows access over HTTP.
# Run the following `az network nsg rule create` command to create a rule called _allow-http_ that allows inbound access on port 80:
az network nsg rule create --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --nsg-name my-vmNSG --name allow-http --protocol tcp --priority 100 --destination-port-range 80 --access Allow
```


Script:
```
# The script under https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh

#!/bin/bash

# Update apt cache.
sudo apt-get update

# Install Nginx.
sudo apt-get install -y nginx

# Set the home page.
echo "<html><body><h2>Welcome to Azure! My name is $(hostname).</h2></body></html>" | sudo tee -a /var/www/html/index.html
```
