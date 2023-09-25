---
title: AZ-104 Microsoft Azure Administrator certificate
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - azure
  - az-104
  - course
  - certification
---

# AZ-104 Microsoft Azure Administrator certificate

!!! abstract "Sources of this notes:"
    - [The Microsoft e-learn platform](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/).
    - Udemy course:  [Prove your AZ-104 Microsoft Azure Administrator skills to the world. Updated.](https://eylearning.udemy.com/course/70533-azure/).


## Configure Azure resources with tools 


### Azure Cloud Shell

- Is temporary and requires a new or existing Azure Files share to be mounted.
- Offers an integrated graphical text editor based on the open-source Monaco Editor.
- Authenticates automatically for instant access to your resources.
- Runs on a temporary host provided on a per-session, per-user basis.
- Times out after 20 minutes without interactive activity.
- Requires a resource group, storage account, and Azure File share.
- Uses the same Azure file share for both Bash and PowerShell.
- Is assigned to one machine per user account.
- Persists $HOME using a 5-GB image held in your file share.
- Permissions are set as a regular Linux user in Bash.


### Azure PowerShell

Azure PowerShell is a module that you add to Windows PowerShell or PowerShell Core to enable you to connect to your Azure subscription and manage resources. Azure PowerShell requires PowerShell to function. PowerShell provides services such as the shell window and command parsing. Azure PowerShell adds the Azure-specific commands.



[See cheat sheet for Azure Powershell](azure-powershell.md). 