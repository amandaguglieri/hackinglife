---
title: M365 CLI 
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - Microsoft 365
  - pentesting
---

# M365 CLI
  

## Installation

Source: [https://pnp.github.io/cli-microsoft365/cmd/docs/ ](https://pnp.github.io/cli-microsoft365/cmd/docs/ )
  
  
Install m365 cli from: https://github.com/pnp/cli-microsoft365  

Login into Microsoft:  

```bash
m365 login  
```
  

You will be prompted to open a browser with this url https://microsoft.com/devicelogin  Enter the code that prompt message indicates and login as m365 user.  


## Ennumeration techniques  

Get information about the default Power Apps environment.  

```bash
m365 pa environment get  
```
 

List Microsoft Power Apps environments in the current tenant 

```bash
m365 pa environment list 
```
 
List all available apps for that user  

```bash
m365 pa app list  
```
  
List all apps in an environment as Admin  

```bash
m365 pa app list --environmentName 00000000-0000-0000-0000-000000000000 --asAdmin  
```  

Remove an app  

```bash
m365 pa app remove --name 00000000-0000-0000-0000-000000000000  
```
 
Removes the specified Power App without confirmation  

```bash
m365 pa app remove --name 00000000-0000-0000-0000-000000000000 --force  
``` 
 
Removes the specified Power App you don't own  

```bash
m365 pa app remove --name 00000000-0000-0000-0000-000000000000 --environmentName Default- 00000000-0000-0000-0000-000000000000 --asAdmin  
``` 
 
 Add an owner without removing the old one  

```bash
m365 pa app owner set --environmentName 00000000-0000-0000-0000-000000000000 --appName 00000000-0000-0000-0000-000000000000 --userId 00000000-0000-0000-0000-000000000000 --roleForOldAppOwner CanEdit  
```

Export an app

```bash
m365 pa app export --environmentName 00000000-0000-0000-0000-000000000000 --name 00000000-0000-0000-0000-000000000000 --packageDisplayName "PowerApp" --packageDescription "Power App Description" --packageSourceEnvironment "Pentesting" --path ~/Documents
```
