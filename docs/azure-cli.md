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

All commands: [https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest).

It’s an executable program that you can use to execute commands in Bash. You can use the Azure CLI to perform every possible management task in Azure. Like Azure PowerShell, the CLI allows you to run one-off commands or you can combine them into a script and execute them together.

Azure CLI is a command-line program to connect to Azure and execute administrative commands on Azure resources. It runs on Linux, macOS, and Windows, and allows administrators and developers to execute their commands through a terminal, command-line prompt, or script instead of a web browser.

## Installation

- Linux: apt-get on Ubuntu, yum on Red Hat, and zypper on OpenSUSE
- Mac: Homebrew.

1. Modify your sources list so that the Microsoft repository is registered and the package manager can locate the Azure CLI package:

```bash
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
sudo tee /etc/apt/sources.list.d/azure-cli.list
```

2. Import the encryption key for the Microsoft Ubuntu repository. This allows the package manager to verify that the Azure CLI package you install comes from Microsoft.

```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
```

3. Install the Azure CLI:

```bash
sudo apt-get install apt-transport-https
sudo apt-get update && sudo apt-get install azure-cli
```

## Basic usage

Run Azure-CLI

```
# Running Azure-CLI from Cloud Shell
bash

# Running Azure-CLI from Linux
az
```

Basic commands to warm up:

```
# See installed version
az --version

# you can use the letters az to start an Azure command 
az upgrade

# Launch Azure CLI interactive mode
az interactive

# Getting help. If you want to find commands that might help you manage a storage blob, you can use the find command:
az find blob

# If you already know the name of the command you want, the `--help` argument
az storage blob --help
```


Commands in the CLI are structured in _groups_ and _subgroups_. Each group represents a service provided by Azure, and the subgroups divide commands for these services into logical groupings. For example, the `storage` group contains subgroups including **account**, **blob**, and **queue**.

Because you're working with a local install of the Azure CLI, you'll need to authenticate before you can execute Azure commands by using the Azure CLI **login** command.

```bash
az login
```

The Azure CLI will typically launch your default browser to open the Azure sign-in page. After successfully signing in, you'll be connected to your Azure subscription.

### Output formatting

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

# List all your resource groups in a table:
az group list --output table

# Return in json all my resources in my resource group:
az group list --query "[?name == '$RESOURCE_GROUP']"


# Retrieve properties from an existing and known resource group
az group show --name myresourcegroup

# From a specific resource group (provided, for instance, its name), query a value. Querying location:
az group show --name <name> --query location --out table

# Querying id
az group show --name <name> --query id --out table

# Create a Resource group
az group create --name <name> --location <location>
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

### App Service plan

Create variables:

```bash
export RESOURCE_GROUP=learn-fbc52a1a-b4e0-491b-ab1e-a2e3d6eff778 
export AZURE_REGION=eastus 
export AZURE_APP_PLAN=popupappplan-$RANDOM 
export AZURE_WEB_APP=popupwebapp-$RANDOM
```


Create an App Service plan to run your app. 

```bash
az appservice plan create --name $AZURE_APP_PLAN --resource-group $RESOURCE_GROUP --location $AZURE_REGION --sku FREE
```

Verify that the service plan was created successfully by listing all your plans in a table:

```bash
az appservice plan list --output table
```


### Web app

Create variables:

```bash
export RESOURCE_GROUP=learn-fbc52a1a-b4e0-491b-ab1e-a2e3d6eff778 
export AZURE_REGION=eastus 
export AZURE_APP_PLAN=popupappplan-$RANDOM 
export AZURE_WEB_APP=popupwebapp-$RANDOM
```

Create a Web App

```bash
# Create web app
az webapp create --name $AZURE_WEB_APP --resource-group $RESOURCE_GROUP --plan $AZURE_APP_PLAN
```

List existing ones:

```bash
az webapp list --output table
```

Return HTTP address of my web app:

```bash
site="http://$AZURE_WEB_APP.azurewebsites.net"
echo $site
```

Getting the default html for the sample web app:

```bash
curl $AZURE_WEB_APP.azurewebsites.net
```


### Deploy code from Github

Create variables:

```bash
export RESOURCE_GROUP=learn-fbc52a1a-b4e0-491b-ab1e-a2e3d6eff778 
export AZURE_REGION=eastus 
export AZURE_APP_PLAN=popupappplan-$RANDOM 
export AZURE_WEB_APP=popupwebapp-$RANDOM
```

The goal is to deploy code from a GitHub repository to the web app.

```bash
az webapp deployment source config --name $AZURE_WEB_APP --resource-group $RESOURCE_GROUP --repo-url "https://github.com/Azure-Samples/php-docs-hello-world" --branch master --manual-integration
```

Once it's deployed, hit your site again with a browser or CURL:

```bash
curl $AZURE_WEB_APP.azurewebsites.net
```


### Deploy an ARM template

Prerequisites:

```bash
# First, sign in to Azure by using the Azure CLI 
az login

# define your resource group. 
	# 1. You can obtain available location values from: 
az account list-locations
	# 2. You can configure the default location using 
az configure --defaults location=<location>
	# 3. If non existentm create it
	az group create --name {name of your resource group} --location "{location}"
```

Now, you are set. Deploy your ARM template:

```bash
templateFile="{provide-the-path-to-the-template-file}"
az deployment group create --name blanktemplate --resource-group myResourceGroup --template-file $templateFile
```

Use linked templates to deploy complex solutions. You can break a template into many templates and deploy these templates through a main template. When you deploy the main template, it triggers the linked template's deployment. You can store and secure the linked template by using a SAS token.


#### AKS


Azure Container Registry
```bash
# Authenticate to an Azure Container Registry
az acr login --name <acrName>
# This will log me to the acr with the token that was generated when authenticating my session firstly.

```

```bash
# Get the resource ID of your AKS cluster
AKS_CLUSTER=$(az aks show --resource-group myResourceGroup --name myAKSCluster --query id -o tsv)

# Get the account credentials for the logged in user
ACCOUNT_UPN=$(az account show --query user.name -o tsv)
ACCOUNT_ID=$(az ad user show --id $ACCOUNT_UPN --query objectId -o tsv)

# Assign the 'Cluster Admin' role to the user
az role assignment create --assignee $ACCOUNT_ID --scope $AKS_CLUSTER --role "Azure Kubernetes Service Cluster Admin Role"

```

```bash
# You create an application named App1 in an Azure tenant. You need to host the application as a multitenant application for any users in Azure, while restricting non-Azure accounts. You need to allow administrators in other Azure tenants to add the application to their gallery.
az ad app create –display-name app1--sign-in-audience AzureADMultipleOrgs

```




