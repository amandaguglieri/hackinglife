---
title: Exams - Practice the AZ-500
TableOfContents: 
date: 2023-10-29T00:00:00Z
author: amandaguglieri
tags:
  - certification
  - cloud
  - azure
  - microsoft
  - az-500
---

# My 100 selected questions to warm up for the AZ-500 certificate

Cheatsheets: **[Azure-CLI](azure-cli.md)**  **|** **[Azure PowerShell](azure-powershell.md)**     |   Certification accomplished at: **October 30th,  2023**.

---

These questions form the hard core of my question bank. They originate from various sources, including Udemy, Microsoft's free practice assessments, and YouTube videos. Successfully completing these questions does not guarantee approval for the AZ-500 exam, but it does provide a good indicator of where you stand up.


??? abstract "Source for these practice tests"
	- [Free practice assessment from Microsoft](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-500/) 
	- [Udemy courses](https://www.udemy.com/courses/search/?src=ukw&q=az-500)  
	- [Video](https://yewtu.be/watch?v=Ct9CY0RGdf8) 

Go to my notes to get a taste of the contents:  [AZ-500: Notes to get through the Azure security engineer certificate](az-500-preparation.md).  

??? note "Summary: AZ-500 Microsoft Azure Security Engineer Certification"
	- [About the certificate](az-500-preparation.md)
	- [I. Manage Identity and Access](az-500-ad-1-identity-and-access.md)
	- [II. Platform protection](az-500-ad-2-platform-protection.md)
	- [III. Data and applications](az-500-ad-3-data-and-applications.md)
	- [IV. Security operations](az-500-ad-4-security-operations.md)
	- [AZ-500 and more: keep learning](az-500-keep-learning.md)

Cheatsheets: **[Azure-CLI](azure-cli.md)**  **|** **[Azure PowerShell](azure-powershell.md)**  

[100 questions you should pass for the AZ-500 certificate](az-500-exams.md)

---
#####  Question  1

**You have custom alert rules in Microsoft Sentinel. The rules exceed the query length limitations. You need to resolve the issue. Which function should you use for the rule? Select only one answer.**

- [ ] ADX functions
- [ ] Azure functions with a timer trigger
- [ ] stored procedures
- [ ] user-defined functions

??? tip "See response"
	You can use user-defined functions to overcome the query length limitation. Timer trigger runs in a scheduled manner (pull, not push). Using ADX functions to create Azure Data Explorer queries inside the Log Analytics query window is unsupported. Stored procedures are unsupported by Azure Data Explorer.

---
#####  Question  2 

**You have an Azure Kubernetes Service (AKS) cluster named AKS1. You are configuring network isolation for AKS1. You need to limit which IP addresses can access the Kubernetes control plane. What should you do? Select only one answer.**

- [ ] Configure API server authorized IP ranges.
- [ ] Configure Azure Front Door.
- [ ] Customize CoreDNS for AKS.
- [ ] Implement Open Service Mesh AKS add-on.

??? tip "See response" 	
	The "Open Service Mesh AKS add-on" is designed to enhance communication and control between services within an Azure Kubernetes Service (AKS) cluster, offering features like service discovery, load balancing, and observability. However, it is not directly related to the task of limiting IP addresses that can access the Kubernetes control plane. Configuring API server authorized IP ranges is the correct approach for controlling access to the control plane by specifying which IP addresses or IP ranges are allowed to interact with the Kubernetes API server. The Open Service Mesh AKS add-on addresses a different aspect of AKS management, focusing on service-to-service communication, making it less relevant for the specific task of network isolation and control of the Kubernetes control plane. Azure Front Door is a global service for routing and load balancing traffic. It is not designed for controlling access to the Kubernetes control plane. Front Door is used for directing and optimizing the delivery of web applications, and it doesn't offer the fine-grained control needed to limit access to the Kubernetes API server. CoreDNS is a DNS server used within Kubernetes clusters for service discovery. While CoreDNS can play a role in the internal DNS resolution within the cluster, it is not a tool for restricting access to the Kubernetes control plane. Customizing CoreDNS is generally related to DNS resolution configurations and would not address the task of limiting IP addresses that can access the control plane.
---
#####  Question 3

**Your company has an Azure subscription and an Amazon Web Services (AWS) account. You plan to deploy Kubernetes to AWS. You need to ensure that you can use Azure Monitor Container insights to monitor container workload performance. What should you deploy first? Select only one answer.**

- [ ] AKS Engine
- [ ] Azure Arc-enabled Kubernetes
- [ ] Azure Container Instances
- [ ] Azure Kubernetes Service (AKS)
- [ ] Azure Stack HCI

??? tip "See response" 	
	Azure Arc-enabled Kubernetes is the only configuration that includes Kubernetes and can be deployed to AWS.
---
#####  Question 4

**You have an Azure subscription that contains a virtual machine named VM1. VM1 is configured with just-in-time (JIT) VM access. You need to request access to VM1. Which PowerShell cmdlet should you run? Select only one answer.**

- [ ] `Add-AzNetworkSecurityRuleConfig`
- [ ] `Get-AzJitNetworkAccessPolicy`
- [ ] `Set-AzJitNetworkAccessPolicy`
- [ ] `Start-AzJitNetworkAccessPolicy`

??? tip "See response"
	The `start-AzJitNetworkAccesspolicy` PowerShell cmdlet is used to request access to a JIT-enabled virtual machine. `Set-AzJitNetworkAccessPolicy` is used to enable JIT on a virtual machine. `Get-AzJitNetworkAccessPolicy` and `Add-AzNetworkSecurityRuleConfig` are not used to start a request access. `Start-AzJitNetworkAccessPolicy` is used to initiate the JIT access request. When you run this cmdlet, you're essentially requesting access to a VM for a specific period, during which your access will be allowed through specific network security group (NSG) rules. These rules are temporarily modified to grant access only during the JIT access window you've requested. After the specified time window expires, the NSG rules revert to their previous state, thereby revoking the temporary access.
---
#####  Question 5

**You have an Azure subscription. You plan to use the `az aks create` command to deploy an Azure Kubernetes Service (AKS) cluster named AKS1 that has Azure AD integration. You need to ensure that local accounts cannot be used on AKS1. Which flag should you use with the command? Select only one answer.**

- [ ] `disable-local-accounts`
- [ ] `generate-ssh-keys`
- [ ] `kubelet-config`
- [ ] `windows-admin-username`

??? tip "See response"
	When deploying an AKS cluster, local accounts are enabled by default. Even when enabling RBAC or Azure AD integration, --admin access still exists essentially as a non-auditable backdoor option. To disable local accounts on an AKS cluster, you should use the `--disable-local-accounts` flag with the `az aks create` command. The remaining options do not remove local accounts.
---
#####  Question 6

**You need to enable encryption at rest by using customer-managed keys (CMKs). Which two services support CMKs? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] Azure Blob storage
- [ ] Azure Disk Storage
- [ ] Azure Files
- [ ] Azure NetApp Files
- [ ] Log Analytics workspace

??? tip "See response"
	 Azure Files and Azure Blob Storage
---
#####  Question   7

**You implement dynamic data masking for an Azure Synapse Analytics workspace. You need to provide only a user named User1 with the ability to see the data. What should you do? Select only one answer.**

- [ ] Create a Conditional Access policy for Azure SQL Database, and then grant access.
- [ ] Grant the UNMASK permission to User1.
- [ ] Use the `ALTER TABLE` statement to drop the masking function.
- [ ] Use the `ALTER TABLE` statement to edit the masking function.

??? tip "See response"
	 Granting the UNMASK permission to User1 removes the mask from User1 only. Creating a Conditional Access policy for Azure SQL Database, and then granting access is not enough for User1 to see the data, only to sign in. Using the `ALTER TABLE` statement to edit the masking function affects all users. Using the `ALTER TABLE` statement to drop the masking function removes the mask altogether.
---
#####  Question  8

**You need to provide public anonymous access to a file in an Azure Storage account. The solution must follow the principle of least privilege. Which two actions should you perform? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] For the container, set Public access level to **Blob**.
- [ ] For the container, set Public access level to **Container**.
- [ ] For the storage account, set Blob public access to **Disabled**.
- [ ] For the storage account, set Blob public access to **Enabled**.

??? tip "See response"
	Unless prevented by another setting, setting Public access level to **Blob** allows public access to the blob only. Setting Blob public access to **Enabled** is a prerequisite for setting the access level of container or blob. Setting Blob public access to **Disabled** prevents any public access and setting Public access level to **Container** also allows any current and future blobs in the container, which does not follow the principle of least privilege.
---
#####  Question  9

**You have an application that will securely share files hosted in Azure Blob storage to external users. The external users will not use Azure AD to authenticate. You plan to share more than 1,000 files. You need to restrict access to only a single IP address for each file. What should you do? Select only one answer.**

- [ ] Configure a storage account firewall.
- [ ] Generate a service SAS that include the signedIP field.
- [ ] Set the Allow public anonymous access to setting for the storage account.
- [ ] Set the Secure transfer required setting for the storage account.

??? tip "See response"
	 Using the Generate a service SAS that include the signedIP field allows a SAS to be generated by using an account key, and each SAS can be configured with an allowed IP address. **Configuring the storage account firewall does not allow for more than 200 IP address rules**. Setting the Allow public anonymous access to setting for the storage account does not prevent access by an IP address. Setting the Secure transfer required property for the storage account prevents HTTP access, but it does not limit where the access request originates from.
---
#####  Question 10

**You have an Azure virtual machine named VM1 the runs Windows Server 2022. A programmer is writing code to run on VM1. The code will use the system-assigned managed identity assigned to VM1 to access Azure resources. Which endpoint should the programmer use to request the authentication token required to access the Azure resources?**

- [ ] Azure AD v1.0.
- [ ] Azure AD v2.0.
- [ ] Azure Resources Manager.
- [ ] Azure Instance Metadata Service.

??? tip "See response"
	Azure Instance Metadata Service is a REST endpoint accessible to all IaaS virtual machines created via Azure Resource Manager (ARM). The endpoint is available at a well-known non-routable IP address (169.254.169.254) that can be accessed only from the virtual machines. The endpoint is used to request the authentication token required to gain access to the Azure resources. Azure AD v1.0 and Azure AD v2.0 endpoints are used to authenticate work and school accounts, not managed identities. The ARM endpoint is where the authentication token is sent by the code once it is obtained from the Azure Instance Metadata Service.
---
#####  Question  11

**You are managing permission scopes for an Azure AD app registration. What are three OpenID Connect scopes that you can use? Each correct answer presents a complete solution. **

- [ ] email
- [ ] openID
- [ ] phone
- [ ] offline_access

??? tip "See response"
	 The openID scope appears on the work account consent page as the Sign you in permission. The email scope gives the app access to a user's primary email address in the form of the email claim. The offline_access scope gives your app access to resources on behalf of a user for an extended time. On the consent page, this scope appears as the Maintain access to data you have given it access to permission.
---
#####  Question  12

**You have a resource group named RG1 that contains an Azure virtual machine named VM1. A user named User1 is assigned the Contributor role for RG1. You need to prevent User1 from modifying the properties of VM1. What should you do?**

- [ ] Add a deny assignment for `Microsoft.Compute/virtualMachines/*` in the VM1 scope. - 
- [ ] Apply a read-only lock to the RG1 scope. 
  
??? tip "See response"
	A read-only lock on a resource group that contains a virtual machine prevents all users from starting or restarting the virtual machine. The RBAC assignment is set at the resource group level and inherited by the resource. The assignment needs to be edited at the original scope (level). You cannot directly create your own deny assignments. Assigning User1 the Virtual Machine User Login role in the RG1 scope will still allow User1 to have access as a contributor to restart VM1. While you can create custom roles with specific permissions and assign those roles to users, Azure RBAC does not provide a direct mechanism for creating "deny" assignments, which would explicitly prevent users from performing specific actions. In other words, you can't explicitly deny a user or group certain permissions at the resource level using RBAC. To achieve fine-grained control over resource access, Azure generally focuses on granting permissions via role assignments and ensuring that users have only the necessary privileges for their tasks. If you want to restrict access, you typically grant a less permissive role or apply resource locks (such as a read-only lock, which prevents modifications) rather than creating deny assignments, which are not a standard part of Azure RBAC.
---
#####  Question  13

**You have an Azure subscription that contains an Azure AD tenant and an Azure web app named App1. A user named User1 needs permission to manage App1. The solution must follow the principle of least privilege. Which role should you assign to User1? **

- [ ] Cloud Application Administrator – Since App1 is an app in Azure, this role provides administrative permissions to App1 and follows the principle of least privilege.
- [ ]  Application Administrator – This role provides administrative permissions to App1 but also provides additional permissions to the app proxy for on-premises applications.
- [ ]  Cloud App Security Administrator – This role is specific to the Microsoft Defender for Cloud Apps solution.
- [ ]  Application Developer – This role allows the user to create registrations but not manage applications.

??? tip "See response"
	Correct: Cloud Application Administrator – Since App1 is an app in Azure, this role provides administrative permissions to App1 and follows the principle of least privilege. 
	Incorrect: Application Administrator – This role provides administrative permissions to App1 but also provides additional permissions to the app proxy for on-premises applications.
	Incorrect: Cloud App Security Administrator – This role is specific to the Microsoft Defender for Cloud Apps solution.
	Incorrect: Application Developer – This role allows the user to create registrations but not manage applications.
---
#####  Question  14 

**You have an Azure subscription that contains a virtual machine named VM1 and a storage account named storage1. You need to ensure that VM1 can access storage1 over the Azure backbone network.  What should you implement?**

- [ ] Service endpoints
- [ ] Private endpoints 
- [ ] A subnet 
- [ ] A VPN gateway 

??? tip "See response"
	Service endpoints route the traffic inside of Azure backbone, allowing access to the entire service, for example, all Microsoft SQL servers or the storage accounts of all customers. Private endpoints provide access to a specific instance.  A subnet does not allow isolation or route traffic to the Azure backbone. A VPN gateway does not allow traffic isolation to all resources.
---
#####  Question 15

**You have an Azure subscription that contains a virtual network named VNet1. VNet1 contains the following subnets:**

- Subnet1: Has a connected virtual machine
- Subnet2: Has a `Microsoft.Storage` service endpoint
- Subnet3: Has subnet delegation to the `Microsoft.Web/serverFarms` service
- Subnet: Has no additional configurations

**You need to deploy an Azure SQL managed instance named managed1 to VNet1. To which subnets can you connect managed1?**

- [ ] Subnet 2 and Subset 4
- [ ] Subnet2, Subnet3, and Subnet4 only
- [ ] Subnet 1, Subnet2, Subnet3, and Subnet4 
  
??? tip "See response"
	Azure SQL managed instances require a dedicated subnet without other resources or virtual machines connected to it. This is because managed instances have specific networking and isolation requirements, and sharing a subnet with other resources, like the virtual machine in Subnet1, could lead to conflicts in network configurations. Therefore, to deploy "managed1," you should select a subnet that doesn't have any other resources connected to it, such as Subnet2, Subnet3, or a new dedicated subnet within VNet1.You can deploy an SQL managed instance to a dedicated virtual network subnet that does not have any resource connected. The subnet can have a service endpoint or can be delegated for a different service. For this scenario, you can deploy managed1 to Subnet2, Subnet3, and Subnet4 only. You cannot deploy managed1 to Subnet1 because Subnet1 has a connected virtual machine.

#####  Question 16

**You host a web app on an Azure virtual machine. Users access the app through a public load balancer. You need to offload SSL traffic to the web app at the edge.  What should you do?**

- [ ] Configure Traffic Manager.
- [ ] Configure Azure Application Gateway.
- [ ] Configure Azure Front Door and switch access to the app via an internal load balancer.
- [ ] Configure Azure Firewall.

??? tip "See response"
	 Front Door allows for SSL offloading at the edge and can route traffic to an internal load balancer. Traffic Manager does not to perform SSL offloading. Neither Azure Firewall nor an Application Gateway can be deployed at the edge. **Azure Application Gateway**: While Azure Application Gateway is a Layer 7 load balancer that can provide SSL termination and load balancing for web applications, it is not positioned at the network edge like Azure Front Door. Application Gateway is typically used for routing traffic within a virtual network to backend services. It can offload SSL traffic, but it's more for managing traffic within the Azure infrastructure, and it does not provide the same level of global load balancing and edge routing capabilities as Azure Front Door.
---
#####  Question 17

**You have an Azure subscription that contains a virtual network named VNet1. You plan to deploy an Azure App Service web app named Web1. You need to be able to deploy Web1 to the subnet of VNet1. The solution must minimize costs. Which pricing plan should you use for Web1?**

- [ ] Basic
- [ ] Shared
- [ ] Isolated
- [ ] Premium

??? tip "See response"
	 Only the Isolated pricing plan (tier) can be deployed to a virtual network subnet. With other pricing plans, inbound traffic is always routed to the public IP address of the web app, while web app outbound traffic can reach the endpoints on a virtual network.
---
#####  Question  18

**You have a data connector for Microsoft Sentinel. You need to configure the connector to collect logs from Conditional Access in Azure AD. Which log should you connect to Microsoft Sentinel?**

- [ ] Sign-in logs
- [ ] Audit logs 
- [ ] Activity logs
- [ ] Provisioning logs

??? tip "See response"
	Sign-in logs include information about sign-ins and how resources are used by your users. Audit logs include information about changes applied to your tenant, such as user and group management or updates applied to your tenant’s resources. Activity logs include subscription-level events, not tenant-level activity. Provisioning logs include activities performed by the provisioning service, such as the creation of a group in ServiceNow or a user imported from Workday.
---
#####  Question 19

**You have an Azure Storage account. You plan to prevent the use of shared keys by using Azure Policy. Which two access methods will continue to work? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] SAS account SAS
- [ ] service SAS
- [ ] Storage Blob Data Reader role
- [ ] user delegation

??? tip "See response"
	user delegation and Storage Blob Data Reader role.
---
#####  Question 20

**You have an Azure SQL Database server. You enable Azure AD authentication for Azure SQL. You need to prevent other authentication methods from being used. Which command should you run? Select only one answer.**

- [ ] `az sql mi ad-admin create`
- [ ] `az sql mi ad-only-auth enable`
- [ ] `az sql server ad-admin create`
- [ ] `az sql server ad-only-auth enable`

??? tip "See response"
	 `az sql server ad-only-auth enable` enables authentication only through Azure AD. `az sql server ad-admin create` and `az sql mi ad-admin create` do not stop other authentication methods. `az sql mi ad-only-auth enable` enables Azure AD-only authentication for Azure SQL Managed Instance, not Microsoft SQL Server.
---
#####  Question 21

**You have an application that securely shares files hosted in Azure Blob storage to external users by using an account SAS.  One of the SAS tokens is compromised.  How should you stop the compromised SAS token from being used? Select only one answer.**

- [ ] Regenerate the storage account access keys.
- [ ] Set the Allow public anonymous access to setting for the storage account.
- [ ] Set the Secure transfer required property for the storage account.
- [ ] Switch to managed identities.
---
#####  Question 22

**You have an Azure AD tenant. Users have both Windows and non-Windows devices. All users have smart phones. You plan to implement Azure AD Multi-Factor Authentication (MFA). You need to ensure that Azure MFA is used to authenticate users to Azure resources. The solution must be implemented without any additional cost. Which three Azure MFA method should you implement? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] FIDO2 security keys
- [ ] OATH software tokens
- [ ] SMS verification
- [ ] the Microsoft Authenticator app
- [ ] voice call verification
- [ ] Windows Hello for Business

??? tip "See response"
	SMS verification, The Microsoft Authenticator app, and voice call verification.
---
#####  Question 23

**You are managing permission scopes for an Azure AD app registration. What are three OpenID Connect scopes that you can use? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] address
- [ ] email
- [ ] offline_access
- [ ] openID
- [ ] phone

??? tip "See response"
	email, openID, offline_access.
---
#####  Question 24

**You have an Azure subscription that contains a user named Admin1. You need to ensure that Admin1 can access the Regulatory compliance dashboard in Microsoft Defender for Cloud. The solution must follow the principle of least privilege. Which two roles should you assign to Admin1? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] Global Reader
- [ ] Resource Policy Contributor
- [ ] Security Admin
- [ ] Security Reader

??? tip "See response"
	To use the Regulatory compliance dashboard in Defender for Cloud, you must have sufficient permissions. At a minimum, you must be assigned the Resource Policy Contributor and Security Admin roles.
---
#####  Question 25

**Your company has a multi-cloud online environment. You plan to use Microsoft Defender for Cloud to protect all supported online environments. Which three environments support Defender for Cloud? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] Alibaba Cloud
- [ ] Amazon Web Services (AWS)
- [ ] Azure DevOps
- [ ] GitHub
- [ ] Oracle Cloud

??? tip "See response"
	Defender for Cloud protects workloads in Azure, AWS, GitHub, and Azure DevOps. Oracle Cloud and Alibaba Cloud are unsupported by Defender for Cloud.
---
#####  Question 26

**You have Azure SQL databases that contain credit card information. You need to identify and label columns that contain credit card numbers. Which Microsoft Defender for Cloud feature should you use? Select only one answer.**

- [ ] hash reputation analysis
- [ ] inventory filters
- [ ] SQL information protection
- [ ] SQL Servers on machines
---
#####  Question 27

**You configure Microsoft Sentinel to connect to different data sources. You are unable to configure a connector that uses an Azure Functions API connection. Which permissions should you change? Select only one answer.**

- [ ] read and write permissions for Azure Functions
- [ ] read and write permissions for the workspaces used by Microsoft Sentinel
- [ ] read permissions for Azure Functions
- [ ] read permissions for the workspaces used by Microsoft Sentinel

??? tip "See response"
	 You need to have read and write permissions to Azure Functions to configure a connector that uses an Azure Functions API connection. You were able to add other connectors, which proves that you have access to the workspace. Read permissions for the workspaces used by Microsoft Sentinel allow you to read data in Microsoft Sentinel. Read permissions to Azure Functions allows you to run functions, not create them.
---
#####  Question 28

**You are configuring retention for Azure activity logs in Azure Monitor logs. The retention period for the Azure Monitor logs is set to 30 days. You need to meet the following compliance requirements:**

- Store the Azure activity logs for 90 days.
- Encrypt the logs by using your own encryption keys.
- Use the most cost-efficient storage solution for the logs.

**What should you do? Select only one answer.**

- [ ] Configure a workspace retention policy.
- [ ] Configure diagnostic settings and send the logs to Azure Event Hubs Standard.
- [ ] Configure diagnostic settings and send the logs to Azure Storage.
- [ ] Leave the default settings as they are.

??? tip "See response"
	Configuring diagnostic settings and sending the logs to Azure Storage meets both the retention time and encryption requirements. Activity log data type is kept for 90 days by default, but the logs are stored by using Microsoft-managed keys. Configuring a workspace retention policy is not the most cost-efficient solution for this. Event Hubs is a real-time event stream engine and is not designed to be used instead of a database or as a permanent store for indefinitely held event streams.
---
#####  Question 29

**You need to implement a key management solution that supports importing keys generated in an on-premises environment. The solution must ensure that the keys stay within a single Azure region. What should you do? Select only one answer.**

- [ ] Apply the Keys should be the specified cryptographic type RSA or EC Azure policy.
- [ ] Disable the Allow trusted services option.
- [ ] Implement Azure Key Vault Firewall.
- [ ] Implement Azure Key Vault Managed HSM.

??? tip "See response"
	Key Vault Managed HSM supports importing keys generated in an on-premise HSM. Also, managed HSM does not store or process customer data outside the Azure region in which the customer deploys the HSM instance. On-premises-generated keys are still managed, after implementing Key Vault Firewall. Enforcing HSM-backed keys does not enforce them to be imported. Disabling the Allow trusted services option does not have a direct impact on key importing.
---
#####  Question 30

**You have an Azure subscription that contains the following resources:**

- A virtual machine named VM1 that has a network interface named NIC1
- A virtual network named VNet1 that has a subnet named Subnet1
- A public IP address named PubIP1
- A load balancer named LB1

**You create a network security group (NSG) named NSG1. To which two resources can you associate NSG1? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] LB1
- [ ] NIC1
- [ ] PubIP1
- [ ] Subnet1
- [ ] VM1
- [ ] VNet1

??? tip "See response"
	You can associate an NSG to a virtual network subnet and network interface only. You can associate zero or one NSGs to each virtual network subnet and network interface on a virtual machine. The same NSG can be associated to as many subnets and network interfaces as you choose.
---
#####  Question 31

**You have an Azure subscription that contains the following resources:**

- An web app named WebApp1 in the West US Azure region
- A virtual network named VNet1 in the West US 3 Azure region

**You need to integrate WebApp1 with VNet1. What should you implement first? Select only one answer**.

- [ ] a service endpoint
- [ ] a VPN gateway
- [ ] Azure Front door
- [ ] peering

??? tip "See response"
	 WebApp1 and VNet1 are in different regions and cannot use regional integration; you can use only gateway-required virtual network integration. To be able to implement this type of integration, you must first deploy a virtual network gateway in VNet1.
---
#####  Question 32

**You host a web app on an Azure virtual machine. Users access the app through a public load balancer. You need to offload SSL traffic to the web app at the edge. What should you do? Select only one answer.**

- [ ] Configure an Azure firewall and switch access to the app via an internal load balancer.
- [ ] Configure Azure Application Gateway.
- [ ] Configure Azure Front Door and switch access to the app via an internal load balancer.
- [ ] Configure Azure Traffic Manager with performance traffic routing.

??? tip "See response"
	 Front Door allows for SSL offloading at the edge and can route traffic to an internal load balancer. Traffic Manager does not to perform SSL offloading. Neither Azure Firewall nor an Application Gateway can be deployed at the edge.
---
#####  Question 33

**You have an Azure App Service web app named App1. You need to configure network controls for App1. App1 must only allow user access through Azure Front Door. Which two components should you implement? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] access restrictions based on service tag
- [ ] access restrictions based on the IP address of Azure Front Door
- [ ] application security groups
- [ ] header filters

??? tip "See response"
	 Traffic from Front Door to the app originates from a well-known set of IP ranges defined in the `AzureFrontDoor.Backend` service tag. This includes every Front Door. To ensure traffic only originates from your specific instance, you will need to further filter the incoming requests based on the unique HTTP header that Front Door sends.
---
#####  Question 34

**You have an Azure SQL database, an Azure key vault, and an Azure App Service web app. You plan to encrypt SQL data at rest by using Bring Your Own Key (BYOK). You need to create a managed identity to authenticate without storing any credentials in the code. The managed identity must share the lifecycle with the Azure resource it is used for. What should you implement?**

- [ ] a system-assigned managed identity for an Azure SQL logical server
- [ ] a system-assigned managed identity for an Azure web app
- [ ] a system-assigned managed identity for Azure Key Vault
- [ ] a user-assigned managed identity

??? tip "See response"
	 So, to clarify, it's not about setting the managed identity at the Azure SQL logical server level. The managed identity is associated with the Azure web app, and it is used to access the encryption keys in the Azure Key Vault, enabling the SQL data at rest encryption without storing credentials in your code. The correct answer aligns with this approach.
---
#####  Question 35

**You need to provide an administrator with the ability to manage custom RBAC roles. The solution must follow the principle of least privilege. Which role should you assign to the administrator?**

- [ ] Owner
- [ ] Contributor
- [ ] User Access Administrator 
- [ ] Privileged Role Administrator

??? tip "See response"
	User Access Administrator is the least privileged role that grants access to `Microsoft.Authorization/roleDefinition/write`. Assigning the Owner role does not follow the principle of least privilege. Contributor does not have access to `Microsoft.Authorization/roleDefinition/write`. Privileged Role Administrator grants access to manage role assignments in Azure AD, and all aspects of Azure AD Privileged Identity Management (PIM). This is not an RBAC role.
---
#####  Question 36

**You have a storage account that contains multiple containers, blobs, queues, and tables. You need to create a key to allow an application to access only data from a given table in the storage account. Which authentication method should you use for the application?**

- [ ] SAS
- [ ] service SAS
- [ ] User delegation
- [ ] Shared Allow access

??? tip "See response"
	 A SAS service is the only type of authentication that provides control at the table level. User delegation SAS is only available for Blob storage. SAS and shared allow access to the entire storage account.
---
#####  Question 37

**You have an Azure Storage account. You plan to prevent the use of shared keys by using Azure Policy. Which two access methods will continue to work? Each correct answer presents a complete solution.**

- [ ] Storage Blob Data Reader role
- [ ] service SAS
- [ ] user delegation
- [ ] account SAS

??? tip "See response"
	The Storage Blob Data Reader role uses Azure AD to authenticate. User delegation SAS is a method that uses Azure AD to generate a SAS. Both methods work whether the shared keys are allowed or prevented. Service SAS and account SAS use shared keys to generate.
---
#####  Question 38

**You enable Always Encrypted for an Azure SQL database. Which scenario is supported?**

- [ ] encrypting existing data

??? tip "See response"
	Encrypting existing data is supported. Always Encrypted uses the client driver to encrypt and decrypt data. This means that some actions that only occur on the server side will not work.
---
#####  Question 39

**You are evaluating the Azure Policy configurations to identify any required custom initiatives and policies. You need to run workloads in Azure that are compliant with the following regulations:**

- FedRAMP High
- PCI DSS 3.2.1
- GDPR
- ISO 27001:2013

**For which regulation should you create custom initiatives?**

- [ ] FedRAMP High
- [ ] PCI DSS 3.2.1
- [ ] GDPR
- [ ] ISO 27001:2013

??? tip "See response"
	To run workloads that are compliant with GDPR, custom initiatives should be to be created. GDPR compliance initiatives are not yet available in Azure. Azure has existing initiatives for ISO, PCI DSS 3.2.1, and FedRAMP High.
---
#####  Question 40

**You have a workload in Azure that uses multiple virtual machines and Azure functions to access data in a storage account.  You need to ensure that all access to the storage account is done by using a single identity. The solution must reduce the overhead of managing the identity. Which type of identity should you use? Select only one answer.**

- [ ] group
- [ ] system-assigned managed identity
- [ ] user
- [ ] user-assigned managed identity

??? tip "See response"
	A user assigned managed identity can be shared across Azure resources, and its password changes are handled by Azure. An user needs to manually handle password changes. You cannot use a group as a service principle. Multiple Azure resources cannot share system-assigned managed identities.
---
#####  Question 41

**You have a workload in Azure that uses a virtual machine named VM1. VM1 is in a resource group named RG1. You need to create and assign an identity to VM1 that will be used to access Azure resources. Other virtual machines must be able to use the same identity. Which PowerShell script should you run? Select only one answer.**

- [ ] `New-AzUserAssignedIdentity -ResourceGroupName RG1 -Name VMID $vm = Get-AzVM -ResourceGroupName RG1 -Name VM1 Update-AzVM -ResourceGroupName RG1 -VM $vm -IdentityType UserAssigned -IdentityID "/subscriptions/<SUBSCRIPTION ID>/resourcegroups/RG1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/VM1"`
- [ ] `New-AzUserAssignedIdentity -ResourceGroupName RG1 -Name VMID $vm = Get-AzVM -ResourceGroupName RG1 -Name VM1 Update-AzVM -ResourceGroupName RG1 -VM $vm -IdentityType UserAssigned -IdentityID "/subscriptions/<SUBSCRIPTION ID>/resourcegroups/RG1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/VMID"`
- [ ] `$vm = Get-AzVM -ResourceGroupName RG1 -Name VM1 Update-AzVM -ResourceGroupName RG1 -VM $vm -IdentityType SystemAssigned`
- [ ] `$vm = Get-AzVM -ResourceGroupName RG1 -Name VM1 Update-AzVM -ResourceGroupName RG1 -VM $vm -IdentityType SystemAssignedUserAssigned`

??? tip "See response"
	 `New-AzUserAssignedIdentity -ResourceGroupName RG1 -Name VMID $vm = Get-AzVM -ResourceGroupName RG1 -Name VM1 Update-AzVM -ResourceGroupName RG1 -VM $vm -IdentityType UserAssigned -IdentityID "/subscriptions/<SUBSCRIPTION ID>/resourcegroups/RG1/providers/Microsoft.ManagedIdentity/userAssignedIdentities/VMID"`
---
#####  Question  42

**You have an Azure subscription that contains an Azure Kubernetes Service (AKS) cluster named AKS1 and a user named User1. You need to ensure that User1 has access to AKS1 secrets. The solution must follow the principle of least privilege. Which role should you assign to User1? Select only one answer.**

- [ ] Azure Kubernetes Service RBAC Admin
- [ ] Azure Kubernetes Service RBAC Cluster Admin
- [ ] Azure Kubernetes Service RBAC Reader
- [ ] Azure Kubernetes Service RBAC Writer

??? tip "See response"
	Azure Kubernetes Service RBAC Writer has access to secrets. Azure Kubernetes Service RBAC Reader does not have access to secrets. Azure Kubernetes Service RBAC Cluster Admin and Azure Kubernetes Service RBAC Admin do not follow the principle of least privilege.
---
#####  Question  43

**You have an Azure subscription that contains an Azure container registry named CR1. You use Azure CLI to authenticate to the subscription. You need to authenticate to CR1 by using Azure CLI. Which command should you run? Select only one answer.**

- [ ] `az acr config`
- [ ] `az acr credential`
- [ ] `az acr login`
- [ ] `docker login`

??? tip "See response"
	The `az acr login` command is needed to authenticate to an Azure container registry from the Azure CLI. Docker login is used to sign in to a Docker repository. `az acr config` is used for configuring Azure Container Registry. `az acr credential` is used for managing login credentials for Azure Container Registry.
---
#####  Question 44

**You have an Azure AD tenant that syncs with the on-premises Active Directory Domain Service (AD DS) domain and uses Azure Active Directory Domain Services (Azure AD DS). You have an application that runs on user devices by using the credentials of the signed-in user The application accesses data in Azure Files by using REST calls. You need to configure authentication for the application in Azure Files by using the most secure authentication method. Which authentication method should you use? Select only one answer.**

- [ ] Azure AD
- [ ] SAS
- [ ] shared key
- [ ] on-premises Active Directory Domain Service (AD DS)

??? tip "See response"
	A SAS is the most secure way to access Azure Files by using REST calls. A shared key allows any user with the key to access data. Azure AD and Active Directory Domain Service (AD DS) are unsupported for REST calls.
---
#####  Question 45

**You have an Azure SQL Database server. You enable Azure AD authentication for Azure SQL. You need to prevent other authentication methods from being used. Which command should you run? Select only one answer.**

- [ ] `az sql mi ad-admin create`
- [ ] `az sql mi ad-only-auth enable`
- [ ] `az sql server ad-admin create`
- [ ] `az sql server ad-only-auth enable`

??? tip "See response"
	`az sql server ad-only-auth enable`
---
#####  Question 46

**You are configuring an Azure Policy in your environment. You need to ensure that any resources that are missing a tag named CostCenter inherit a value from a resource group. You create a custom policy that uses the following snippet. **

```
"policyRule": {
    "if": {
        "field": "tags['CostCenter']",
        "exists": "false"
    },
    "then": {
        "effect": "modify",
        "details": {
            "roleDefinitionIds": [
                "/providers/microsoft.authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c"
            ],
            "operations": [{
                "operation": "addOrReplace ",
                "field": "tags['CostCenter']",
                "value": "[resourcegroup().tags['CostCenter']]"
            }]
        }
    }
}
```

**Which policy mode should you use? Select only one answer.**

- [ ] `all`
- [ ] `Append`
- [ ] `DeployIfNotExists`
- [ ] `indexed`

??? tip "See response"
	Indexed.
---
#####  Question 47

**You set Periodic recurring scans to **ON** while implementing a Microsoft Defender for SQL vulnerability assessment. How often will the scan be triggered? Select only one answer.**

- [ ] at a recurrence that you configure
- [ ] once a day
- [ ] once a month
- [ ] once a week

??? tip "See response"
	Once a week.
---
#####  Question 48

**You are implementing Microsoft Defender for SQL vulnerability assessments. In which two locations can users view the results? Each correct answer presents a complete solution. Select all answers that apply.**

- [ ] an Azure Blob storage account
- [ ] an Azure Event Grid instance
- [ ] Microsoft Defender for Cloud
- [ ] Microsoft Teams

??? tip "See response"
	 Defender for Cloud is the default and mandatory location to view the results, while a Blob storage account is a mandatory destination and a prerequisite for enabling the scan. The Teams option is unavailable out of the box. A scan completion event is not sent to Event Grid.
---
##### Question 49 

**You are collecting Azure activity logs to Azure Monitor. The retention period for Azure Monitor logs is set to 30 days. To meet compliance requirements, you need to send a copy of the Azure activity logs to your SOC partner. What should you do? Select only one answer.**

- [ ] Configure a workspace retention policy.
- [ ] Configure diagnostic settings and send the logs to Azure Event Hubs.
- [ ] Configure diagnostic settings and send the logs to Azure Storage.
- [ ] Install the Microsoft Sentinel security information and event management (SIEM) connector.

---
#####  Question 50

**You are designing an Azure solution that stores encrypted data in Azure Storage. You need to ensure that the keys used to encrypt the data cannot be permanently deleted until 60 days after they are deleted. The solution must minimize costs. What should you do?  Select only one answer.**

- [ ] Store keys in an HSM-protected key vault that has soft delete and purge protection enabled.
- [ ] Store keys in an HSM-protected key vault that has soft delete enabled.
- [ ] Store keys in a software-protected key vault that has soft delete and purge protection enabled.
- [ ] Store keys in a software-protected key vault that has soft delete enabled and purge protection disabled.

??? tip "See response"
	Store keys in a software-protected key vault that has soft delete and purge protection enabled.
---
#####  Question 51
**You plan to provide connectivity between Azure and your company’s datacenter. You need to define how to establish the connection. The solution must meet the following requirements:**

- All traffic between the datacenter and Azure must be encrypted.
- Bandwidth must be between 10 and 100 Gbps.

**What should you use for the connection? Select only one answer.**

- [ ] Azure VPN Gateway
- [ ] ExpressRoute Direct
- [ ] ExpressRoute with a provider
- [ ] VPN Gateway with Azure Virtual WAN

??? tip "See response"
	ExpressRoute Direct
---
#####  Question  52

**You are operating in a cloud-only environment. Users have computers that run either Windows 10 or 11. The users are located across the globe. You need to secure access to a point-to-site (P2S) VPN by using multi-factor authentication (MFA). Which authentication method should you implement? Select only one answer.**

- [ ] Authenticate by using Active Directory Domain Services (AD DS).
- [ ] Authenticate by using native Azure AD authentication.
- [ ] Authenticate by using native Azure certificate-based authentication.
- [ ] Authenticate by using RADIUS.

---
#####  Question  53

**You have an Azure subscription that contains the following resources:**

- Two virtual networks
    - VNet1: Contains two subnets
    - VNet2: Contains three subnets
- Virtual machines: Connected to all the subnets on VNet1 and VNet2
- A storage account named storage1

**You need to identify the minimal number of service endpoints that are required to meet the following requirements:**

- Virtual machines that are connected to the subnets of VNet1 must be able to access storage1 over the Azure backbone.
- Virtual machines that are connected to the subnets of VNet2 must be able to access Azure AD over the Azure backbone.

**How many service endpoints should you recommend? Select only one answer. **

- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5

??? tip "See response"
	A service endpoint is configured for a specific server at the subnet level. Based on the requirements, you need to configure two service endpoints for `Microsoft.Storage` on VNet1 because VNet1 has two subnets and three service endpoints for `Microsoft.AzureActiveDirectory` on VNet2 because VNet2 has three subnets. The minimum number of service endpoints that you must configure is five.
---
##### Question 54

**You have an Azure subscription that contains a virtual network named VNet1. VNet1 contains the following subnets:**

- Subnet1: Has a connected virtual machine
- Subnet2: Has a `Microsoft.Storage` service endpoint
- Subnet3: Has subnet delegation to the `Microsoft.Web/serverFarms` service
- Subnet: Has no additional configurations

**You need to deploy an Azure SQL managed instance named managed1 to VNet1. To which subnets can you connect managed1? Select only one answer.**

- [ ] Subnet4 only
- [ ] Subnet3 and Subnet4 only
- [ ] Subnet2 and Subnet4 only
- [ ] Subnet2, Subnet3, and Subnet4 only
- [ ] Subnet1, Subnet2, Subnet3, and Subnet4

??? tip "See response"
	 You can deploy an SQL managed instance to a dedicated virtual network subnet that does not have any resource connected. The subnet can have a service endpoint or can be delegated for a different service. For this scenario, you can deploy managed1 to Subnet2, Subnet3, and Subnet4 only. You cannot deploy managed1 to Subnet1 because Subnet1 has a connected virtual machine.
---
##### Question 55

**You use Azure Blueprints to deploy resources to a resource group named RG1. After the deployment, you try to add a disk to a virtual machine created by using Blueprints, but you get an access denied error. You open **RG1** and check your access. You notice that you are listed as part of the Virtual Machine Contributor role for RG1, and there are no deny assignments or classic administrators in the resource group scope. Why are you unable to manage the virtual machine? Select only one answer.**

- [ ] Blueprints created a deny assignment for the virtual machine resource.
- [ ] Blueprints removed the user from the Classic Administrator role.
- [ ] You must be part of the Disk Pool Operator role.
- [ ] You must be part of the Virtual Machine Administrator Login role.

??? tip "See response"
	Blueprints must have created a deny assignment at the resource level. The Disk Pool Operator role allows users to provide permissions to the StoragePool resource provider, and the Virtual Machine Administrator Login role allows users to view the virtual machine in the portal and sign in as an administrator. You still have the Contributor role and should be able to manage a virtual machine unless a deny assignment is in place.
---
#####  Question 56

**You create an Azure policy by using the following snippet.**

```
"then": {
    "effect": "",
    "details": [{
        "field": "Microsoft.Storage/storageAccounts/networkAcls.ipRules",
        "value": [{
            "action": "Allow",
            "value": "134.5.0.0/21"
        }]
    }]
}
```

**You need to ensure that the policy is applied whenever a new storage account is created or updated. There is no managed identity assigned to the policy initiative. Which effect should you use? Select only one answer.**

- [ ] `Append`
- [ ] `Audit`
- [ ] `DeployIfNotExists`
- [ ] `Modify`

??? tip "See response"
	`Append` is used to add fields to existing properties. `Modify` is used to add, update, or remove properties, it does not ensure that a field has value. `DeployIfNotExists` is used to deploy resources. `Audit` is used to check for compliance.
---
##### Question 57

**You have an Azure subscription. You need to recommend a solution that uses crawling technology of Microsoft to discover and actively scan assets within an online infrastructure. The solution must also discover new connections over time. What should you include in the recommendation? Select only one answer.**

- [ ] a Microsoft Defender for Cloud custom initiative
- [ ] Microsoft Defender External Attack Surface Management (EASM)
- [ ] Microsoft Defender for Servers
- [ ] the Microsoft cloud security benchmark (MCSB)

??? tip "See response"
	 Defender EASM applies the crawling technology of Microsoft to discover assets that are related to your known online infrastructure and actively scans these assets to discover new connections over time. Attack Surface Insights are generated by applying vulnerability and infrastructure data to showcase the key areas of concern for your organization.
---
#####  Question 58 

**You have an Azure subscription and the following SQL deployments:**

- An Azure SQL database named DB1
- An Azure SQL Server named sqlserver1
- An instance of SQL Server on Azure Virtual Machines named VM1 that has Microsoft SQL Server 2022 installed
- An on-premises server named Server1 that has SQL Server 2019 installed

**Which deployments can be protected by using Microsoft Defender for Cloud? Select only one answer.**

- [ ] DB1 and sqlserver1 only
- [ ] DB1, sqlserver1, and VM1 only
- [ ] DB1, sqlserver1, VM1, and Server1
- [ ] sqlserver1 only
- [ ] sqlserver1 and VM1 only

??? tip "See response"
	Defender for Cloud includes Microsoft Defender for SQL. Defender for SQL can protect Azure SQL Database, Azure SQL Server, SQL Server on Azure Virtual Machines, and SQL servers installed on on-premises servers.
---
##### Question 59

**You are designing a solution that must meet FIPS 140-2 Level 3 compliance in Azure. Where should the solution maintain encryption keys? Select only one answer.**

- [ ] a managed HSM
- [ ] a software-protected Azure key vault
- [ ] an Azure SQL Manage Instance database
- [ ] an HSM-protected Azure key vault

??? tip "See response"
	 A managed HSM is level 3-compliant. An HSM-protected key vault is level 2-compliant. A software-protected key vault is level 1-complaint. SQL is not FIPS 104-2 level 3 compliant.
---
#####  Question 60

**You have an Azure tenant that contains a user named User1 and an Azure key vault named Vault1. Vault1 is configured to use Azure role-based access control (RBAC). You need to ensure that User1 can perform actions on keys in Vault1 but cannot manage permissions. The solution must follow the principle of least privilege. Which role should you assign to User1? Select only one answer.**

- [ ] Key Vault Crypto Officer
- [ ] Key Vault Crypto User
- [ ] Key Vault Reader
- [ ] Key Vault Secrets Officer
- [ ] Key Vault Secrets User

??? tip "See response"
	Correct: Key Vault Crypto Officer –– This role meets the requirements. 
	Incorrect: Key Vault Secrets Officer –– This role is for secrets, not keys.
	Incorrect: Key Vault Reader –– This role is only for read access, not performing actions.
	Incorrect: Key Vault Crypto User –– This role can manage permissions.
	Incorrect: Key Vault Secrets User –– This role is for secrets, not keys.
---
#####  Question 61

**You are implementing an Azure Kubernetes Service (AKS) cluster for a production workload. You need to ensure that the cluster meets the following requirements:**

- Provides the highest networking performance possible
- Manages ingress traffic by using Kubernetes tools

**What should you use? Select only one answer.**

- [ ] CNI networking with Azure load balancers
- [ ] CNI networking with ingress resources and controllers
- [ ] Kubenet networking with Azure load balancers
- [ ] Kubenet networking with ingress resources and controllers

??? tip "See response"
	CNI networking provides the best performance since it does not require IP forwarding and UDR, and ingress controllers can be managed from within Kuberbetes. Kubenet networking requires defined routes and IP forwarding, making the network slower. Azure load balancers cannot be managed by using Kubernetes tools.
---
#####  Question 62

**You have an Azure subscription that contains a virtual machine named VM1. VM1 is configured with just-in-time (JIT) VM access. You need to request access to VM1.  Which PowerShell cmdlet should you run? Select only one answer.**

- [ ] `Add-AzNetworkSecurityRuleConfig`
- [ ] `Get-AzJitNetworkAccessPolicy`
- [ ] `Set-AzJitNetworkAccessPolicy`
- [ ] `Start-AzJitNetworkAccessPolicy`

??? tip "See response"
	The `start-AzJitNetworkAccesspolicy` PowerShell cmdlet is used to request access to a JIT-enabled virtual machine. `Set-AzJitNetworkAccessPolicy` is used to enable JIT on a virtual machine. `Get-AzJitNetworkAccessPolicy` and `Add-AzNetworkSecurityRuleConfig` are not used to start a request access.
---
#####  Question 63

**You create a role by using the following JSON.**

```
{
  "Name": "Virtual Machine Operator",
  "Id": "88888888-8888-8888-8888-888888888888",
  "IsCustom": true,
  "Description": "Can monitor and restart virtual machines.",
  "Actions": [
    "Microsoft.Storage/*/read",
    "Microsoft.Network/*/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action",
    "Microsoft.Authorization/*/read",
    "Microsoft.ResourceHealth/availabilityStatuses/read",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.Insights/alertRules/*",
    "Microsoft.Insights/diagnosticSettings/*",
    "Microsoft.Support/*"
  ],
  "NotActions": [],
  "DataActions": [],
  "NotDataActions": [],
  "AssignableScopes": ["/subscriptions/*"]
}
```

**A user that is part of the new role reports that they are unable to restart a virtual machine by using a PowerShell script. What should you do to ensure that the user can restart the virtual machine?**

- [ ] Add `Microsoft.Compute/virtualMachines/login/action` to the list of `DataActions` in the custom role.
- [ ] Add `Microsoft.Compute/*/read` to the list of `Actions` in the role.

??? tip "See response"
	The role needs read access to virtual machines to restart them. The user does not need to authenticate again for the role to be in effect, and the user will not be able to access the virtual machine from the portal. Adding `Microsoft.Compute/virtualMachines/login/action` to the list of `DataActions` in the role allows the user to sign in as a user, but not to restart the virtual machine.
---
##### Question 64

**You have a Linux virtual machine in an on-premises datacenter that is used as a forwarder for Microsoft Sentinel by using CEF-formatted logs. The timestamp on events retrieved from the forwarder is the time the agent on the forwarder received the event, not the time the event occurred on the system it came from. You need to ensure that Microsoft Sentinel receives the time the event was generated. What should you do? Select only one answer.**

- [ ] Run `cef_gather_info.py` on CEF forwarder.
- [ ] Run `cef_gather_info.py` on each system that sends events to the forwarder.
- [ ] Run `TimeGenerated.py` on each system that sends events to the forwarder.
- [ ] Run `TimeGenerated.py` on the CEF forwarder.

??? tip "See response"
	Running `TimeGenerated.py` on the CEF forwarder changes the logging on the forwarder to the use the event time instead of the time the event was received by the agent on the forwarder. Running `TimeGenerated.py` on each system will not change the way events are logged on the forwarder. Running `cef_gather_info.py` gathers data, but it does not change the timestamp.
---
##### Question 65

**You configure a Linux virtual machine to send Syslog data to Microsoft Sentinel. You notice that events for the virtual machine are duplicated in Microsoft Sentinel. You need to ensure that the events are not duplicated.  Which two actions should you perform? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] Disable the synchronization of the Log Analytics agent with the Syslog configuration in Microsoft Sentinel.
- [ ] Disable the Syslog daemon from listening to network messages.
- [ ] Enable the Syslog daemon to listen to network messages.
- [ ] Remove the entry used to send CEF messages from the Syslog configuration file for the virtual machine.
- [ ] Stop the Syslog daemon on the virtual machine.

??? tip "See response"
	You must disable CEF messages on the virtual machine and prevent the setting to send CEF messages from being read. Stopping the Syslog daemon on the virtual machine will stop the virtual machine from sending both Syslog and CEF messages. Enabling the Syslog daemon to listen and disabling the Syslog daemon from listening to network messages does not handle the duplication of events.
---
#####  Question 66

**You are configuring automatic key rotation for an encryption key stored in Azure Key Vault. You need to implement an alert to be triggered five days before the keys are rotated. What should you use? Select only one answer.**

- [ ] an action group alert
- [ ] Application Insights
- [ ] Azure Event Grid
- [ ] Microsoft Defender for Key Vault

??? tip "See response"
	Using Event Grid triggers the `Microsoft.KeyVault.CertificateNearExpiry` event. Key Vault cannot be monitored by using Application Insights. Defender for Key Vault is used to alert for unusual and unplanned activities. Key Vault key expiration cannot be monitored by using action group alerts.
---
##### Question 67

**You have an Azure subscription that contains an Azure container registry named ACR1 and a user named User1. You need to ensure that User1 can administer images in ACR1. The solution must follow the principle of least privilege. Which two roles should you assign to User1? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] AcrDelete
- [ ] AcrImageSigner
- [ ] AcrPull
- [ ] AcrPush
- [ ] Contributor
- [ ] Reader

??? tip "See response"
	To administer images in ACR1, a user must be able to push and pull images to ACR1 and delete images from ACR1. The AcrPush and AcrDelete roles are required to push, pull, and delete images in ACR1. AcrPull only allows the Push image permission, not pull. Contributor can also perform these operations, however it also has many additional permissions, which means that it does not follow the principle of least privilege. Reader and AcrImageSigner do not have adequate permissions.
---
#####  Question 68

**You need to allow only Azure AD-authenticated principals to access an existing Azure SQL database. Which three actions should you perform? Each correct answer presents part of the solution. Select all answers that apply.**

- [ ] Add an Azure AD administrator.
- [ ] Assign your account the SQL Security Manager built-in role.
- [ ] Connect to the database by using Microsoft SQL Server Management Studio (SSMS).
- [ ] Connect to the database by using the Azure portal.
- [ ] Select **Support only Azure Active Directory authentication for this server**.

??? tip "See response"
	Adding an Azure AD administrator and assigning your account the SQL Security Manager built-in role are prerequisites for enabling Azure AD-only authentication. Selecting Support only Azure AD authentication for this server enforces the Azure SQL logical server to use Azure AD authentication. A connection to the data plane of the logical server is not needed.
---
#####  Question  69

**You manage Azure AD for a retail company. You need to ensure that employees using shared Android tablets can use passwordless authentication when accessing the Azure portal. Which authentication method should you use? Select only one answer.**

- [ ] the Microsoft Authenticator app
- [ ] security keys
- [ ] Windows Hello
- [ ] Windows Hello for Business

??? tip "See response"
	You can only use the Microsoft Authenticator app or one-time password login on shared devices. Windows Hello can only be used for Windows devices. You cannot use security keys on shared devices.
---
##### Question 70

**You need to configure passwordless authentication. The solution must follow the principle of least privilege. Which role should assign to complete the task? Select only one answer.**

- [ ] Authentication Administrator
- [ ] Authentication Policy Administrator
- [ ] Global Administrator
- [ ] Security Administrator

??? tip "See response"
	Configuring authentication methods requires Global Administrator privileges. Security administrators have permissions to manage other security-related features. Authentication policy administrators can configure the authentication methods policy, tenant-wide multi-factor authentication (MFA) settings, and password protection policy. Authentication administrators can set or reset any authentication methods, including passwords, for non-administrators and some roles.
---
##### Question 71 

You manage Azure AD. You disable the Users can register applications option in Azure AD. A user reports that they are unable to register an application. You need to ensure that that the user can register applications. The solution must follow the principle of least privilege. What should you do? Select only one answer.

- [ ] Assign the Application Developer role to the user.
- [ ] Assign the Authentication Administrator role to the user.
- [ ] Assign the Cloud App Security Administrator role to the user.
- [ ] Enable the Users can register applications option.

??? tip "See response"
	The Application Developer role has permissions to register an application even if the Users can register applications option is disabled. The Users can register applications option allows any user to register an application. The Authentication Administrator role and the Cloud App Security Administrator role do not follow the principle of least privilege.
---
##### Question 72

You have a virtual network that contains an Azure Kubernetes Service (AKS) workload and an internal load balancer. Multiple virtual networks are managed by multiple teams. You are unable to change any of the IP addresses. You need to ensure that clients from virtual networks in your Azure subscription can access the AKS cluster by using the internal load balancer. What should you do? Select only one answer.

- [ ] Create a private link endpoint on the virtual network and instruct users to access the cluster by using a private link endpoint on their virtual network.
- [ ] Create a private link service on the virtual network and instruct users to access the cluster by using a private link endpoint in their virtual networks.
- [ ] Create virtual network peering between the virtual networks to allow connectivity.
- [ ] Create VPN site-to-site (S2S) connections between the virtual networks to allow connectivity.

??? tip "See response"
	A private link service will allow access from outside the virtual network to an endpoint by using NAT. Since you do not control the IP addressing for other virtual networks, this ensures connectivity even if IP addresses overlap. Once a private link service is used in the load balancer, other users can create a private endpoint on virtual networks to access the load balancer.
---
##### Question 73

You have an Azure subscription that contains a virtual machine named VM1. VM1 runs a web app named App1. You need to protect App1 by implementing Web Application Firewall (WAF). What resource should you deploy? Select only one answer.

- [ ] Azure Application Gateway
- [ ] Azure Firewall
- [ ] Azure Front Door
- [ ] Azure Traffic Manager

??? tip "See response"
	WAF is a tier of Application Gateway. If you want to deploy WAF, you must deploy Application Gateway and select the WAF or WAF V2 tier.
---
##### Question 74

**You have an Azure AD tenant that uses the default setting. You need to prevent users from a domain named contoso.com from being invited to the tenant. What should you do? Select only one answer.**

- [ ] Deploy Azure AD Privileged Identity Management (PIM).
- [ ] Edit the Access review settings.
- [ ] Edit the Collaboration restrictions settings.
- [ ] Enable security defaults.

??? tip "See response"
	After you edit the Collaboration restrictions settings, if you try to invite a user from a blocked domain, you cannot. Security defaults and PIM do not affect guest invitation privileges. By default, the Allow invitations to be sent to any domain (most inclusive) setting is enabled. In this case, you can invite B2B users from any organization.
---
##### Question 75

Your company has an Azure Active Directory (Azure AD) tenant named whizlab.com. The company wants to deploy a service named “Getcloudskillsserver” that would run on a virtual machine running Windows Server 2016. The service needs to authenticate to the tenant and access Microsoft Graph to read the directory data. You need to delegate the minimum required permissions for the service. Which of the following steps would you perform in Azure? Choose 3 answers from the options below.

- [ ] Add an app registration.
- [ ] Grant Application Permissions.
- [ ] Add application permission.
- [ ]  Configure an Azure AD Application Proxy.
- [ ]  Add delegated permission.

??? tip "See response"
	Add an app registration.  (Correct)
	Grant Application Permissions. (Correct)
    Add application permission. (Correct)
    Configure an Azure AD Application Proxy. (Incorrect)
    Add delegated permission.  (Incorrect)
    First, you need to add an application registration. When it comes to the types of permissions, you have to use Application permissions for services. And then, finally, you grant the required permissions.
---
##### Question 76

In order to get diagnostics from an Azure virtual machine you own, what is the first step to doing that?

- [ ] A diagnostics agent needs to be installed on the VM
- [ ]  You need to create a storage account to store it
- [ ] You need to grant RBAC permissions to the user requesting diagnostics

??? tip "See response"
	You need to create a storage account to store it
---
##### Question 77

Being the network engineer at your company, you need to ensure that communications with Azure Storage pass through the Service Endpoint. How would you ensure it?

- [ ] By adding an Inbound rule to allow access to the storage
- [ ] By adding one Inbound rule and one Outbound rule
- [ ] By adding an Outbound rule to allow access to the storage
- [ ] You don't need to make a specific configuration or add any rule, it is automatically configured.

??? tip "See response"
	By adding an Outbound rule to allow access to the storage. Inbound/outbound network security group rules can be created to deny traffic from/to the Internet and allow traffic from/to AzureCloud or other available service tags of particular Azure services.
---
##### Question 78

**You need to recommend a solution for encrypting data at rest and in transit for your company's database. Which of the following would you recommend?**

- [ ] Azure storage encryption
- [ ] Transparent Data Encryption
- [ ] Always Encrypted
- [ ]  SSL certificates

??? tip "See response"
	 Always Encrypted.
---
##### Question 79

**A company wants to synchronize its on-premises Active Directory with its Azure AD tenant. They want to set up a solution that would minimize the need for additional hardware deployment. They also want to ensure that they can keep their current login restrictions. It includes logon hours for their current Active Directory users. Which authentication method should they implement?**

- [ ] Azure AD Connect and Pass-through authentication
- [ ] Federated identity using Azure Directory Federation Services
- [ ] Azure AD Connect and Password hash synchronization
- [ ] Azure AD Connect and Federated authentication
    
??? tip "See response"
	Azure AD Connect and Pass-through authentication. Since we need to minimize additional hardware deployments, we can use Azure AD Connect to synchronize Active Directory users with Azure AD. 
---
##### Question 80

**You must specify whether the following statement is TRUE or FALSE: You are an administrator at getcloudskills.com and responsible for managing user accounts on Azure Active Directory. In order to leverage Azure administrative units, do you need an Azure Active Directory Premium License for each Administrative Unit member?**

- [ ] True
- [ ] False

??? tip "See response"
	 False. To manage/use administrative units you need an Azure Active Directory premium license only for each Administrative Unit admin and you can use a free license for unit members.
---
##### Question 81

**A development team has published an application onto an Azure Web App service. They want to enable Azure AD authentication for the web application. They have to perform an application registration in Azure AD. Which of the following are required when you configure the App service for Azure AD authentication? Choose two answers from the options given below.**

- [ ] Client ID
- [ ] Logout URL
- [ ] Subscription ID
- [ ] Tenant ID

??? tip "See response"
	Client ID and Tenant ID
---
##### Question 82

**You decide to use Azure Front Door for defining, managing, and monitoring the global routing for your web traffic and optimizing end-user reliability and performance via quick global failover. From the below-given list, choose the features that is not supported by Azure Front Door.**

- [ ] Redirect HTTPS traffic to HTTP using URL redirect
- [ ] Web Application Firewall
- [ ] URL path-based routing

??? tip "See response"
	Redirect HTTPS traffic to HTTP using URL redirect
---
##### Question 83

If no rules other than the default NSG rules are in place, are VMs on SubnetA and SubnetB be able to connect to the Internet?

- [ ] Yes
- [ ] No
   
??? tip "See response"
	 Yes. The Outbound rules contain a Rule with the name “AllowInternetOutBound”. This would allow all Outbound traffic to the Internet.
---
##### Question 84

**Your company has a set of Azure SQL databases hosted on a logical server. They want to enable SQL auditing for the database. Which of the following can be used to store the audit logs? Choose 3 answers from the options given below.**

- [ ] Azure Log Analytics    
- [ ] Azure SQL database
- [ ] Azure Event Hubs
- [ ] Azure Storage accounts
- [ ] Azure SQL data warehouse

??? tip "See response"
	Azure Log Analytics, Azure Event Hubs and  Azure Storage accounts
---
##### Question 85

**Your organization is looking to increase its security posture. Which of the following would you implement to reduce the reliance on passwords and increase account security?**

- [ ] Entra ID B2C
- [ ] Multi-factor Authentication (MFA)    
- [ ] Passwordless Authentication
- [ ] Entra ID Directory Roles
   
??? tip "See response"
	Multi-factor Authentication (MFA) and  Passwordless Authentication.  Multi-factor Authentication (MFA) enhances security by requiring two or more verification methods. Passwordless authentication allows users to sign in without a password, instead using methods like the Microsoft Authenticator app. 
 ---
##### Question 86

**Which of the following is designed to ban certain passwords from being used, ensuring users avoid easily guessable and vulnerable passwords?**

- [ ] Entra ID Identity Protection
- [ ] Entra ID Password Protection
- [ ] Entra ID MFA
- [ ] Entra ID B2B

??? tip "See response"
	 Entra ID Password Protection. Entra ID Password Protection helps you establish comprehensive defense against weak passwords in your environment. It bans certain passwords and sets lockout settings to prevent malicious attempts. 
---
##### Question 87

**You're setting up an application to use Microsoft Entra ID for authentication. Which of the following are essential components you would need to create or configure in Microsoft Entra ID?**

- [ ] Application Registration
- [ ] OAuth token grant
- [ ] Azure Policy

??? tip "See response"
	Application Registration and  OAuth token grant. When you register an app with Microsoft Entra ID, you're creating an identity configuration for the app that allows it to integrate with the Entra ID identity service. A service principal is an identity created for use with applications, hosted services, and automated tools to access Azure resources. 
---
##### Question 88

**You need to restrict access to your Azure Storage account such that it can only be accessed from a specific subnet within your Azure Virtual Network. Which feature should you utilize?**

- [ ] Private Link services
- [ ] Virtual Network Service Endpoints
- [ ] Azure Functions
- [ ] Azure SQL Managed Instance

??? tip "See response"
	Virtual Network Service Endpoints. Virtual Network Service Endpoints extend your virtual network private address space and the identity of your VNet to the Azure services, over a direct connection. Endpoints allow you to secure your critical Azure service resources to only your virtual networks.
---
##### Question 89

**Which of the following Azure services offer built-in Distributed Denial of Service (DDoS) protection to secure your applications?**

- [ ] Azure Firewall
- [ ] Azure Application Gateway
- [ ] Azure DDoS Protection Standard
- [ ] Azure Front Door

??? tip "See response"
	 Azure Application Gateway, Azure DDoS Protection Standard and  Azure Front Door.  Azure Application Gateway offers DDoS protection as part of its WAF (Web Application Firewall) feature. c. Azure DDoS Protection Standard provides advanced DDoS mitigation capabilities. Azure Front Door provides both DDoS protection and Web Application Firewall for its global HTTP/HTTPS endpoints.
  ---
##### Question 90

**You have been assigned to enhance the security and compliance of your organization's Azure SQL Database. Which of the following measures can you adopt to encrypt data and audit database operations?**

- [ ] Transparent Database Encryption (TDE)
- [ ] Azure SQL Database Always Encrypted
- [ ] Azure Blob Soft Delete
- [ ]  Enable database auditing

??? tip "See response"
	 Transparent Database Encryption (TDE) and  Enable database auditing. Transparent Database Encryption (TDE) encrypts SQL Server, Azure SQL Database, and Azure Synapse Analytics data files. Database auditing tracks database events and writes them to an audit log in your Azure storage account. 
 ---
##### Question 91

**You need to centralize the management of security configurations for multiple Azure subscriptions. Which Azure service should you utilize to ensure consistent application of configurations?**

- [ ] Entra ID  
- [ ] Azure Key Vault
- [ ] Azure Blueprint
- [ ] Azure Landing Zone

??? tip "See response"
	 Azure Blueprint. Azure Blueprint enables organizations to define a repeatable set of Azure resources that adheres to specific requirements and standards. It allows consistent application of configurations across multiple subscriptions. 
---
##### Question 92

**You are an Azure security specialist who has been tasked with setting up and maintaining the security monitoring within the organization. Which of the following tasks can be accomplished with Microsoft Sentinel?**

- [ ] Monitor security events using Azure Monitor Logs
- [ ] Automate response to specific security threats
- [ ] Customize analytics rules to identify potential threats
- [ ] Deploy virtual machines in Azure
- [ ] Evaluate and manage generated alerts

??? tip "See response"
	Monitor security events using Azure Monitor Logs, Automate response to specific security threats, Customize analytics rules to identify potential threats and Evaluate and manage generated alerts. a. Microsoft Sentinel uses Azure Monitor Logs for security events, enabling users to monitor these events. b. Microsoft Sentinel offers automation features to respond to detected security threats. c. One of the features of Microsoft Sentinel is the ability to customize analytics rules, helping in the detection of potential threats. d. Deploying virtual machines is a task within Azure and isn't specifically a function of Microsoft Sentinel. e. Microsoft Sentinel generates alerts based on its analytics, and users can evaluate and manage these alerts within the platform.
---
##### Question 93

**You have a hybrid configuration of Azure Active Directory (Azure AD). You have an Azure HDInsight cluster on a virtual network. You plan to allow users to authenticate to the cluster by using their on-premises Active Directory credentials. You need to configure the environment to support the planned authentication. Solution: You deploy the On-premises data gateway to the on-premises network. Does this meet the goal?**

- [ ] Yes
- [ ] No

??? tip "See response"
	No.
---
##### Question 94

**Your company has an Azure subscription name Subscription1 that contains the users shown in the following table:**

| Name | Role |
| --- | --- |
| User1 | Global Administrator |
| User2 | Billing Administrator |
| User3 | Owner |
| User4 | Account Admin |

**The company is sold to a new owner. The company needs to transfer ownership of Suscription1. Which user can transfer the ownership and which tool should the user use? To answer, select the appropriate options in the answer area. NOTE: Each correct selection is worth one point.**

**Select user:**

- [ ] User1
- [ ] User2
- [ ] User3
- [ ] User4

**Select tool:**

- [ ] Azure Account Center
- [ ] Azure Cloud Shell
- [ ] Azure PowerShell
- [ ] Azure Security Center

??? tip "See response"
	User2. Azure Account Center.
---
##### Question 95

**Your company has an Azure subscription name Subscription1. Subscription1 is associated with the Azure Active Directory tenant that includes the users shown in the following table:**

| Name | Role |
| --- | --- |
| User1 | Global Administrator |
| User2 | Billing Administrator |
| User3 | Owner |
| User4 | Account Admin |

**The company is sold to a new owner. The company needs to transfer ownership of Suscription1. Which user can transfer the ownership and which tool should the user use? To answer, select the appropriate options in the answer area. NOTE: Each correct selection is worth one point.**

**Select user:**

- [ ] User1
- [ ] User2
- [ ] User3
- [ ] User4

**Select tool:**

- [ ] Azure Account Center
- [ ] Azure Cloud Shell
- [ ] Azure PowerShell
- [ ] Azure Security Center

??? tip "See response"
	User1. Azure Account Center.
---
##### Question 96

**The CIS Microsoft Azure Foundations Security Benchmark provides several recommended best practices related to identify and access management. Each of the following is a best practice except for this one?**

- [ ] Avoid unnecessary guest user accounts in Azure Active Directory.
- [ ] Enable Azure Multi-Factor Authentication (MFAA).
- [ ] Establish intervals for reviewing user authentication methods.
- [ ] Enable Self-Service Group Management.

??? tip "See response"
	Enable Self-Service Group Management.
---
##### Question 97

**You have an Azure Active Directory (Azure AD) tenant that contains the users shown in the following table.**

| Name | Member of a group | Multi-factor authentication (MFA) status | 
| --- | -------- | ------ |
| User1 | Group1, Group2 | Enabled |
| User2 | Group1 | Disabled |

**You create and enforce an Azure AD Identity Protection sign-in risk policy that has the following settings:**

- Assignments: Include Group 1, exclude Group2
- Conditions: Sign-in risk level: Low and above
- Access:  Allow access, Require multi-factor authentication.

**You need to identify what occurs when the users sign in to Azure AD. What should you identify for each user? To answer, select the apropriate options in the answer area. NOTE: Each correct selection is worth one point.**

**When User1 signs in from an anonymous IP address, the user will:**

- [ ] Be blocked.
- [ ] Be prompted for MFA.
- [ ] Sign in by using a username and password only.

**When User2 signs in from an unfamiliar location, the user will:**

- [ ] Be blocked.
- [ ] Be prompted for MFA.
- [ ] Sign in by using a username and password only.

??? tip "See response"
	User1 will  be prompted for MFA. User2 will be blocked
---
##### Question 98

You have an Azure subscription that contains the virtual machines shown in the following table

| Name | Location | Virtual network name |
| -- | -- | -- |
| VM1 | East US | VNet1 |
| VM2 | West US | VNet2 |
| VM3 | East US | VNet1 |
| VM4 | West US | VNet3 |

All the virtual networks are peered. You deploy Azure Bastion to VNet2. Which virtual machines can be protected by the bastion host?

- [ ] VM1, VM2, VM3, and VM4.
- [ ] VM1, VM2, and VM3 only.
- [ ] VM2 and VM4 only.
- [ ] VM2 only.

??? tip "See response"
	 VM1, VM2, VM3, and VM4.
---
##### Question 99

You have an Azure subscription that contains the Azure virtual machines shown in the following table

| Name | Operating System |
| -- | -- | 
| VM1 | Windows 10 |
| VM2 | Windows Server 2016 |
| VM3 | Windows Server 2019 |
| VM4 | Ubuntu Server 18.04 LTS |

You create an MDM Security Baseline profile named Profile1. You need to identify to which virtual machines Profile1 can be applied. Which virtual machines should you identify?

- [ ] VM1, VM2, VM3, and VM4.
- [ ] VM1, VM2, and VM3 only.
- [ ] VM1 and VM3 only.
- [ ] VM1 only.

??? tip "See response"
	 VM1 only.
---
#### Question 100

**You have an Azure subscription named Sub1. You create a virtual network that contains one subnet. On the subnet, you provision the virtual machines shown in the following table.**

| Name | Network Interface | Application security group assignment | IP address |
| -- | -- | -- | -- |
| VM1 | NIC1 | Appgroup12 | 10.0.0.10 |
| VM2 | NIC2 | Appgroup12 | 10.0.0.11 |
| VM3 | NIC3 | Appgroup3 | 10.0.0.100 |
| VM4 | NIC4 | Appgroup4 | 10.0.0.200 |

**Currently, you have not provisioned any network security group (NSGs). You need to implement network security to meet the following requirements:**

- Allow traffic to VM4 from VM3 only.
- Allow traffic from the Internet to VM1 and VM2.
- Minimize the number of NSGs and network security rules.

**How many NSGs and network security rules should you create? To answer, select the appropriate options in the answer area. NOTE: Each correct selection is worth one point.**

**NSGs:**

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**Network security rules: **

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

??? tip "See response"
	NSGs: 2. Network security rules: 3.

