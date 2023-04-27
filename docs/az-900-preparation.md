---
title: AZ-900 Preparation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
---



# AZ-900 Preparation

The REAL AZ-900 exam includes multiple choice questions, true/false questions, and even fill-in-the-blank questions.

These notes come from the course [AZ-900 Bootcamp: Microsoft Azure Fundamentals](https://www.udemy.com/course/az-900-azure-exam-prep-understanding-cloud-concepts/), created by [Thomas Mitchell](https://www.udemy.com/course/az-900-azure-exam-prep-understanding-cloud-concepts/#instructor-1) and [labITout Learning](https://www.udemy.com/course/az-900-azure-exam-prep-understanding-cloud-concepts/#instructor-2)

## Labs 

[Labitpro](https://labitpro.com/microsoft-azure-labs/).

### Deploy a file share in Microsoft Azure

In this Azure simulation, you will be guided through the process of creating an Azure file share, setting a quota on the new file share, create a folder within the file share, and viewing the share connection information.

[Lab Details](https://labitpro.com/deploy-a-file-share-in-azure/)

### Deploy a virtual network in Microsoft Azure

In this step-by-step Azure simulation, you will be guided through the creation of a virtual network called MyNewVnet. You will configure a vNet address space, two subnets, and address ranges for each new subnet.

[Lab Details](https://labitpro.com/deploy-a-virtual-network-in-microsoft-azure/)

### Provision a resource group in Azure

A resource group is a container that holds related resources for an Azure solution. In this Azure simulation, you will be guided through the process of creating a new resource group in Azure, using the Azure Portal. 

[Lab Details](https://labitpro.com/provision-a-resource-group-in-azure/)

### Deploy and configure an Azure Virtual Machine

In this Azure simulation, you will be guided through the process of provisioning a new Windows virtual machine via the Azure Portal. During the creation of the VM, you will also create and attach a data disk.

[Lab Details](https://labitpro.com/deploy-and-configure-an-azure-virtual-machine/)

### Deploy and configure an Azure Storage Account

In this Azure simulation, you will be guided through the process of provisioning a new General Purpose V2 storage account via the Azure Portal. You will configure the storage account to use Locally Redundant Storage.

[Lab Details](https://labitpro.com/deploy-and-configure-an-azure-storage-account/)

### Deploy and configure a network security group

In this Azure simulation, you will be guided through the process of provisioning a new Network Security Group in Microsoft Azure, using the Azure Portal. Rule creation is covered in the NSG Rules lab simulation.

[Lab Details](https://labitpro.com/deploy-and-configure-an-nsg-in-azure/)

### Deploy and configure Azure Bastion

In this guided, step-by-step Azure simulation, you will will create a Bastion subnet in an existing virtual network, deploy the Bastion Host, and then use the bastion host to connect to an existing virtual machine.

[Lab Details](https://labitpro.com/deploy-and-configure-azure-bastion/)

### Configure devices in Azure Active Directory

In this step-by-step, hands-on Azure lab simulation, you will be guided through the process of allowing a specific Azure Active Directory user to join devices to your fictional organization’s Azure

## More labs

Are you the curious type? If so, feel free to take advantage of these additional labIT PRO hands-on labs:

-   [Add a Custom Domain to Azure AD](https://www.labitpro.com/wp-content/Udemy/AZ900/AddCustomDomaintoAzureAD)
 -   [Create Users and Groups in Azure AD](https://www.labitpro.com/wp-content/Udemy/AZ900/CreateUsersandGroupsinAzureAD)
-   [Configure Self-Service Password Reset in Azure AD](https://www.labitpro.com/wp-content/Udemy/AZ900/ConfigureSSPRinAzureAD)
-   [Create and Configure an Azure Storage Account](https://www.labitpro.com/wp-content/Udemy/AZ900/CreateStorageAccount)
-   [Manage Azure Storage Account Access Keys](https://www.labitpro.com/wp-content/Udemy/AZ900/ManageAccessKeys)
-   [Create an Azure File Share](https://www.labitpro.com/wp-content/Udemy/AZ900/CreateAnAzureFileShare)
-   [Create and Attach a VM Data Disk](https://www.labitpro.com/wp-content/Udemy/AZ900/CreateAndAttachDataDisk)
-   [Resize an Azure Virtual Machine](https://www.labitpro.com/wp-content/Udemy/AZ900/ResizeAzureVM)
-   [Create a VM Scale Set in Azure](https://www.labitpro.com/wp-content/Udemy/AZ900/CreateVMScaleSetInAzure)
-   [Configure vNet Peering](https://www.labitpro.com/wp-content/Udemy/AZ900/ConfigurevNetPeeringinAzure)
-   [Create and Configure an Azure Recovery Services Vault](https://www.labitpro.com/wp-content/Udemy/AZ900/AzureRecoveryServicesVault)
-   [Managing Users and Groups in Azure AD](https://www.labitpro.com/wp-content/Udemy/AZ900/ManageUsersAndGroupsinAzureAD)


## Resources

- Practice with a [mock exam](https://www.tomteachesit.com/az-900-mock-exam/).
- [AZ-900 crossword puzzle](https://www.tomteachesit.com/az-900-crossword-puzzle-fun/)
- [Flashcards](https://www.tomteachesit.com/az-900-flashcards/)


## Basic Cloud Computing concepts


### Shared responsability model 


![Shared responsability model](img/cloud-models.png)

Very often, IaaS, PaaS and SaaS are referred as Cloud computing stack because esencially they are built on top one from another. 

### Cloud models

#### Public cloud 

In a public cloud deployment, services are offered over the public internet. These services are available to customers who wish to purchase them. The cloud resources, like servers and storage, are owned and operated by the cloud service provider. 


#### Private cloud 

In a private cloud, compute resources are accessed exclusively by users from a single business or organization. You can host a private cloud physically in your own on-prem datacenter, or it can be hosted by a third-party cloud service provider. 


#### Hybrid cloud 

A hybrid cloud is a complex computing environment. It combines a public cloud and a private cloud by allowing data and applications to be shared between them. This type of cloud deployment is often utilized by large organizations.


### Consumption-Based Model

The consumption-based model refers to the way in which organizations only pay for the resources they use. The consumption-based model offers the following benefits: 

• No upfront costs 
• No need to purchase or manage infrastructure 
• Customer pays for resources only when they are needed 
• Customer can stop paying for resources that are no longer needed


### Benefits of Cloud Computing

Cloud computing offers several key advantages over a physical environment: 

• High availability: Cloud-based apps can provide a continuous user experience with virtually no downtime. 
• Scalability: Apps in the cloud can scale vertically and horizontally. When scaling vertically, compute capacity is added by adding RAM or CPUs to a virtual machine. When scaling horizontally, compute capacity is increased by adding instances of resources, such as adding VMs to a configuration. 
• Elasticity: Allows you to configure apps to autoscale so they always have the resources they need. 
• Agility: Deploy and configure cloud-based resources quickly as requirements change. 
• Geo-distribution: Deploy apps to regional datacenters so that customers always have the best performance in their specific region. 
• Disaster recovery: Cloud-based backup services, data replication, and geo-distribution allow you to deploy apps and know that their data is safe in the event of disaster. 


### Capital Expenses vs. Operating Expenses 

Organizations have to think about two different types of expenses: 

• Capital Expenditure (CapEx): The spending of money up-front on physical infrastructure. These expenses are deducted over time. 
• Operational Expenditure (OpEx): The spending of money on services or products now and being billed for them now. These expenses are deducted in the same year they are incurred. Most cloud services are considered OpEx.


### The Cloud Computing stack


![Shared responsability model](img/cloud-models-02.png)


#### Infrastructure-as-a-Service (IaaS)

Migrating to IaaS helps reduce the need for maintenance of on-prem data centers and allows organizations to save money on hardware costs. IaaS solutions allow organizations to scale their IT resources up and down with demand, while also allowing them to quickly provision new applications and increase the reliability of their underlying infrastructure.

**1.** One common business scenario and use case for IaaS is **Lift-and-Shift Migration**:
- migrate app and workloads to the cloud
- Increase scale and perfomance
- Enhance security
- Reduce the cost without refactoring the application

**2.** Another common use case is **Storage, backup, and recovery**:
- Avoid capital outlay for storage and complexity of storage management
- IaaS is useful for handling unpredictable demand and steadily growing storage needs
- Simplify planning/management of backup/recovery

**3.** **Web apps**
IaaS provides all the infraestructure needed to support web apps: storage, web and application servers, networking resources. Quickly deployable, easily scale infraestructure up and down.

**4.** **High-performance computer**


#### Platform-as-a-Service (PaaS)

Basically, PaaS is a complete development and deployment environment in the cloud. Includes: servers, storage, networking, middleware, development tools, BI services, database management systems, and more. PaaS supports the complete web application lifecycle.  Yo manage the applications and services and the service provider manages everything else.

Platform-as-a-Service is a complete development and deployment environment in the cloud. It can be used to deploy simple cloud-based apps and complex cloud-enabled enterprise applications. When leveraging PaaS, you purchase the resources you need from your cloud service provider on a pay-as-yougo basis. The resource you purchase are accessed over a secure Internet connection.

PaaS resources include the same resources included in IaaS (servers, storage, and networking) PLUS things like middleware, development tools, business intelligence services, and database management systems.

It’s important to remember that PaaS is designed to support the complete web application lifecycle. It allows organizations to avoid the expense buying and managing software licenses, underlying infrastructure and middleware, container orchestrators, and development tools. 

Ultimately, when leveraging PaaS offerings, you manage the applications and services, while the cloud service provider manages everything else.

**1.**  One common business scenario and use case for PaaS is **Development framework**. A framework that developers can use to develop or customize cloud based applications and that Azure provides.

**2.** **Analytics and BI**: tools provided as a service with PaaS.


#### Software-as-a-Service (SaaS)

Software-as-a-Service allows users to connect to cloud-based apps over the Internet. Microsoft Office 365 is a good example of SaaS in action. Gmail would be another good example. SaaS provides a complete software solution that’s purchased on a pay-as-you-go basis from a cloud service provider. It’s essentially the rental of an app, that users can then connect to over the Internet, via a web browser. The underlying infrastructure, middleware, app software, and app data for a SaaS solution are all hosted in the provider’s data center, which means the service provider is responsible for managing the hardware and software. SaaS allows organizations to get up and running quickly, with minimal upfront cost.


## Core Architectural components

### Availability Sets 

They protect resources against rack failures within a datacenter.

### Azure Region

A region is a geographical area that contains at least one (but potentially multiple) datacenters that are networked together with a low-latency network.

Every Azure region is paired with another region within the same geography (ie. US, Europe, or Asia) at least 300 miles away in order to allow replication of resources across that geography. Replicating resources across region pairs helps reduce interruptions due to events like natural disasters, civil unrest, power outages, or physical network outages that affect both regions at once.

Some services or features are only available in certain regions. Others don't require to select an specific region. For instance: Azure Active Directory, Azure Traffic Manager, or Azure DNS.


![Azure Regions](img/azure-region.png)

There are some special regions that exist, maybe, for compliance reasons (or others). Examples: 
- US DoD Central, US Gov Virginia, and US Gov Iowa are some physical and logical network-isolated instances of Azure for US government agencies and partners. 
- China East, China North: Available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly.

### Availability zones

They are created by using one or more datacenters. There are a minimum of three zones within a single region to recover from a massive outage.

Availability zones are physically separate datacenters within an Azure region. Every availability zone 
includes one or more datacenters that features independent power, cooling, and networking. In 
essence, an availability zone is designed to be an isolation boundary, meaning if one zone goes down, 
the other continues working.  

Availability zones are designed primarily for VMs, managed disks, load balancers, and SQL databases.  

![Azure Regions](img/azure-availability-zone.png)


It is important to remember that availability zones are connected through private high-speed fiber-optic 
networks. The image below shows what availability zones look like within a region: 

### Region pairs

Each Azure region is paired with another region within the same geography at least 300 miles away. This is done to allow for the replication of resources across a geography and reduce the chance of unavailability. West US region is, for instance, paired with East US.

If an outage occurs:  one region is prioritized to make sure that at least one is restored as quickly as possible. It also does so to minimize downtime.  Data resides within the same geography as its pair.


### Azure Resources and Resource Groups 

Before deploying an Azure resource, you need to create at least a resource group to deploy the resource into. The relationship of resources with resource groups is highlighted below: 

• **Resource**: A resource is a manageable item in Azure. Virtual machines, storage accounts, web apps, and virtual networks are examples of resources. 
• **Resource Group**: A resource group is a container that holds all related resources that you want to manage as a group.  Resources within a resource group are typically managed as a group.  Resource groups can be nested. 

All resources must be in a resource group, and a single resource can only be a member of a single resource group.  What you can do is moving resources from one group to another.

When deleting a resource group, all resources included in it  will be deleted, so it makes sense to organized your resource groups by similar lifecycle, or by function.

Resource groups are also a scope for applying RBAC (Role Based Access Control) permissions.


### Azure Subscription

An Azure subscription provides authenticated and authorized access to Azure products and services and allows organizations to provision cloud resources. Every Azure subscription links to an Azure account, which is an identity in Azure AD or in a directory that Azure AD trusts. 

Azure subscriptions can be used to define boundaries around Azure products, services, and resources:  

• Billing boundary: Azure subscription determines how an Azure account is billed for using Azure. 
• Access control boundary: Azure subscription creates separate subscriptions to reflect different organizational structures.  

An account can have one subscription or multiple subscriptions that have different billing models. You can also use subscription to apply different access-management policies when necessary. 


### Management Groups in Azure 

To efficiently manage access, policies (like available regions), and compliance when you manage multiple Azure subscriptions, you can use Management Groups, because management groups provide scope that sits above subscriptions.  

When managing multiple subscriptions, you organize those subscriptions into containers called management groups, to  which you can then apply governance conditions. All subscriptions within a management group will, in turn, inherit the conditions you apply to the management group.  

All subscriptions within a single management group must trust the same Azure AD tenant.

The image below highlights how you can create a hierarchy for governance through the use of management groups: 

![Azure management group](img/azure-management-group.png)

Maximum of 10,000 management groups supported in a single directory.

A management group tree can support up to six levels of depth (root and subscription level not included)



## Core Azure Compute services and products

Azure compute is an on-demand computing service that organizations use to run cloud-based applications. It provides compute resources like disks, processors, memory, networking, and even operating systems. Azure supports many types of compute solutions, including Linux, Windows Server, SQL Server, Oracle, IBM, and SAP. Each Azure compute service offers different options depending on your requirements. The most common Azure compute services are:

- Azure Virtual Machines 
- VM Scale Sets 14 
- Azure Container Instances 
- Azure App Service 
- Azure Functions (serverless computing)


### Azure Virtual Machines

Virtual machines are virtual versions of physical computers that feature virtual processors, memory, storage, and networking resources. They host an operating system just like a physical computer, and you can install and run software on them just like a physical computer. 

VM provides IaaS and can be used in two ways:

- When you need total control over an operating system /environment, VMs are ideal when using in-house or customized software.


### Virtual Machine Scale Sets 

A virtual machine scale set allows you to deploy and manage a set of identical VMs that you can use to deploy solutions with true autoscale. As demand increases, VM instances can be added.


### Containers and Kubernetes 

Container Instances and Azure Kubernetes Service are both Azure compute resources that organizations can use to deploy and manage containers. Unlike VMs, which are full virtualized servers, containers are lightweight, virtualized application environments. 


### App Service Azure

App Service is a compute platform that you can use to quickly build, deploy, and scale enterprise grade web, mobile, and API apps running on any platform.  App service is a PaaS offering. 


### Functions 

Functions are a serverless technology that are best used in cases where you're concerned only about the code running your service and not the underlying platform or infrastructure.


## Azure Container Instances ACI versus Azure Kubernetes service  AKS

For many organizations, containers have become the preferred way to package, deploy, and manage cloud apps. 

- Azure Container Instances (ACI) is the easiest way to run a container in Azure, without the need for any VMs or other infrastructure.  You can use docker images.
- However, if you require full container orchestration, Microsoft  recommends Azure Kubernetes Service (AKS). 

### Azure Kubernetes Service (AKS)

AKS simplifies the deployment of a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. Since it’s hosted, Azure handles the health monitoring and maintenance. The Kubernetes masters are managed by Azure, and you manage and maintain the agent nodes.  
 
It’s important to note that AKS itself is free. You pay only for the agent nodes within your clusters, not for the masters. 

You can deploy an AKS cluster using  Azure CLI, Azure Portal, Azure Powershell, and Template-driven deployment options  (ARM templates, bicep, terraform).


## Key Azure Management Tools

There are several tools at your disposal to manage Azure resources and environments. They include the 
Azure Portal, Azure PowerShell, Azure CLI, the Azure Mobile App, and ARM templates. 


### Azure Portal

The Azure portal is a web-based user interface that you can use to access almost every feature of Azure. It can be used to visually understand and manage your Azure environment, while Azure PowerShell allows you to quickly perform one-off tasks and to script tasks as needed. Azure PowerShell is available for Windows, Linux, and Mac, and you can access it in a web browser via Azure Cloud Shell. 

Azure Portal does not offer a way to automate repetitive tasks.


### Azure CLI

The Azure CLI is a command-line interface.  A cross-platform command-line program (Windows, Linux and macOs) to connect to Azure and execute administrative commands. It can be  run on
It’s an executable program that you can use to execute commands in Bash. You can use the Azure CLI to perform every possible management task in Azure. Like Azure PowerShell, the CLI allows you to run one-off commands or you can combine them into a script and execute them together.

```ps
az vm create --resourcegroup MyResourceGroup --name MyVM01 --image UbuntLTS --generate-ssh-keys
```


### Azure PowerShell

 Azure Powershell needs Windows Powershell run since Azure Powershell builds upon Windows Powershell with added features.

```ps
New-AzVm -ResourceGroupName "MyResourceGroup" -Name "MyVM01" -Image "UbuntLTS"
```


### Azure Cloud Shell

Browser-based scripting environment that is accessible from Azure Portal. It requires a storage account. It allows you to choose the shell experience that suits you best.

### Azure mobile app

The Azure mobile app is available for iOS and Android devices. It allows you to access Azure resources when you're away from a computer. 

- Access, manage, monitor Azure accounts and resources.
- Monitor the health and status of Azure resources, check for alerts, diagnose and fix issues.
- Stop, start, restart a web app or virtual machine.  
- Run the Azure CLI or Azure PowerShell commands to manage Azure resources. 


### Azure REST APIs

Service endpoints that support sets of HTTP operations. CRUD access to services.


### Azure Advisor

Free services that helps you follow best practices. 

### ARM templates 

ARM templates allow you to declaratively describe the resources you want to use, using JSON format. The template will then create those resources in parallel. For example, need 25 VMs, all 25 VMs will be created at the same time. 









## Flashcard questions

**What is Cloud computing?**

The delivery of computing services, such as servers, storage, databases, and networking, over the Internet to provide faster innovation, flexible resources, and economies of scale.


**How does cloud computing lower operating costs?**

By only paying for the cloud services used, rather than the capital expense of buying hardware and setting up on-site datacenters.


**Why do organizations move to the cloud?**

For cost savings, improved speed and scalability, increased productivity, better performance, reliability, and improved security.


**What is the advantage of cloud computing's self-service and on-demand nature?**

It allows for vast amounts of computing resources to be provisioned quickly, giving businesses a lot of flexibility and taking the pressure off capacity planning.


**What does "elastically scaling" mean in cloud computing?**

Delivering the right amount of IT resources, such as computing power and storage, at the right time and from the right location.


**How does cloud computing improve productivity?**

By removing the need for time-consuming IT management tasks, allowing IT teams to focus on more important business goals.


**How does cloud computing improve performance?**

By running on a worldwide network of secure datacenters that are regularly upgraded to the latest generation of efficient computing hardware, reducing network latency and offering greater economies of scale.


**How does cloud computing improve reliability?**

By making data backup, disaster recovery, and business continuity easier and less expensive through data mirroring at multiple redundant sites on the cloud provider's network.


**How does cloud computing improve security?**

By offering a broad set of policies, technologies, and controls that strengthen the overall security posture, protecting data, apps, and infrastructure from potential threats.
  

**What is the main advantage of using cloud computing?**

Cost savings, improved speed and scalability, increased productivity, better performance, reliability, and improved security.


**What is the biggest difference between cloud computing and traditional IT resources?**

Traditional IT resources required buying hardware and software, setting up and running on-site datacenters, and paying for electricity and IT experts. Cloud computing eliminates these expenses and provides flexible and on-demand resources.


**What are the benefits of cloud computing services?**

Faster innovation, flexible resources, and economies of scale.


**What is the advantage of cloud computing over traditional on-site datacenters?**

Cloud computing eliminates the need for hardware setup, software patching, and other time-consuming IT management tasks, allowing IT teams to focus on more important business goals.


**What is the advantage of cloud computing over a single corporate datacenter?**

Reduced network latency for applications and greater economies of scale.


**What is the main advantage of data backup, disaster recovery, and business continuity in cloud computing?**

It is easier and less expensive.


**What is the main advantage of security in cloud computing?**

Cloud providers offer a broad set of policies, technologies, and controls that strengthen the overall security posture.


**What is the shared responsibility model in cloud computing?**

The shared responsibility model in cloud computing refers to the division of responsibilities between the cloud provider and the customer in terms of security tasks and workloads.


**What are the different types of cloud deployment?**

The different types of cloud deployment are Software as a Service (SaaS), Platform as a Service (PaaS), Infrastructure as a Service (IaaS), and on-premises datacenter.


**In which type of deployment do customers retain the most responsibilities?**

In an on-premises datacenter, customers retain the most responsibilities, as they own the entire stack.


**What responsibilities are always retained by the customer, regardless of the type of deployment?**

The responsibilities retained by the customer regardless of the type of deployment are data, endpoints, account, and access management.


**In a SaaS deployment, which party is responsible for protecting the security of the data?**

In a SaaS deployment, the customer is responsible for protecting the security of the data.


**In a PaaS deployment, who is responsible for managing and maintaining the underlying infrastructure?**

In a PaaS deployment, the cloud provider is responsible for managing and maintaining the underlying infrastructure.


**In an IaaS deployment, who is responsible for managing and maintaining the operating systems and middleware?**

In an IaaS deployment, the customer is responsible for managing and maintaining the operating systems and middleware.


**What are the three broad categories of cloud computing services?**

Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS)


**What are the benefits of migrating your organization's infrastructure to an IaaS solution?**

Migrating to IaaS helps reduce maintenance of on-premises data centers, save money on hardware costs, and gain real-time business insights. It also gives you the flexibility to scale IT resources up and down with demand and quickly provision new applications.


**Is lift-and-shift migration a common business scenario for using IaaS?**

Yes. Lift-and-shift migration is a common business scenario for using IaaS. It is the fastest and least expensive method of migrating an application or workload to the cloud.


**What is PaaS and how does it differ from IaaS?**

Platform as a service (PaaS) is a complete development and deployment environment in the cloud, with resources that enable you to deliver everything from simple cloud-based apps to sophisticated, cloud-enabled enterprise applications. PaaS includes infrastructure such as servers, storage, and networking, but also middleware, development tools, business intelligence services, and more. IaaS only includes infrastructure resources.


**How does PaaS differ from SaaS?**

PaaS provides a complete development and deployment environment in the cloud, including infrastructure, middleware, development tools, and more. SaaS is a type of cloud service where users access software applications over the internet, without the need for installation or maintenance.


** How does SaaS work?**

With SaaS, users connect to the software over the Internet, usually with a web browser. The service provider manages the hardware and software, and with the appropriate service agreement, will ensure the availability and the security of the app and your data.


**What are some common examples of SaaS?**

Common examples of SaaS are email, calendaring, and office tools (such as Microsoft Office 365).


**What are the components of SaaS?**

The components of SaaS include hosted applications/apps, development tools, database management, business analytics, operating systems, servers and storage, networking firewalls/security, and data center physical plant/building.


** What are the benefits of using SaaS for an organization?**

SaaS provides a complete software solution that you purchase on a pay-as-you-go basis from a cloud service provider. It allows your organization to get quickly up and running with an app at minimal upfront cost.

  
**What is a region in Azure?**

A region in Azure is a geographical area on the planet that contains at least one but potentially multiple datacenters that are nearby and networked together with a low-latency network.


**Why are regions important in Azure?**

Regions are important in Azure because they provide flexibility to bring applications closer to users no matter where they are, global regions provide better scalability and redundancy, and they preserve data residency for services.


**What are some examples of special Azure regions?**

Examples of special Azure regions include US DoD Central, US Gov Virginia, US Gov Iowa, China East, and China North.


**What are availability zones in Azure?**

Availability zones in Azure are created by using one or more datacenters, and there is a minimum of three zones available within a single region.


**What are region pairs in Azure?**

Each Azure region is paired with another region within the same geography (such as US, Europe, or Asia) at least 300 miles away. This allows for the replication of resources across a geography and helps reduce the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect both regions at once.


**What are the advantages of region pairs in Azure?**

Region pairs in Azure include automatic geo-redundant storage and prioritization of one region out of every pair in the event of an extensive Azure outage. Planned Azure updates are rolled out to paired regions one region at a time to minimize downtime and risk of application outage.


**What is the purpose of region pairs in Azure?**

The purpose of region pairs in Azure is to provide reliable services and data redundancy by replicating resources across a geography and reducing the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect both regions at once.


**What happens if a region in a region pair is affected by a natural disaster in Azure?**

If a region in a region pair is affected by a natural disaster in Azure, services will automatically failover to the other region in its region pair.


**How does Azure provide a high guarantee of availability?**

Azure provides a high guarantee of availability by having a broadly distributed set of datacenters, creating region pairs that are directly connected and far enough apart to be isolated from regional disasters, and offering automatic geo-redundant storage and failover capabilities.


**What is the difference between regions, geographies, and availability zones in Azure?**

In Azure, regions are geographical areas on the planet that contain at least one but potentially multiple datacenters that are nearby and networked together with a low-latency network. Geographies refer to the larger geographical area that a region is located in, such as US, Europe, or Asia. Availability zones are created by using one or more datacenters and there is a minimum of three zones within a single region.


**What is an availability zone?**

Availability zones are physically separate datacenters within an Azure region that are equipped with independent power, cooling, and networking, and are connected through high-speed, private fiber-optic networks.


**What is the purpose of availability zones?**

The purpose of availability zones is to provide high availability for mission-critical applications by creating duplicate hardware environments, in case one goes down.


**How are availability zones connected?**

Availability zones are connected through high-speed, private fiber-optic networks.


**What types of Azure services support availability zones?**

VMs, managed disks, load balancers, and SQL databases support availability zones.


**What are zonal services?**

Zonal services are resources that are pinned to a specific zone, such as VMs, managed disks, and IP addresses.


**What are zone-redundant services?**

Zone-redundant services are services that the platform replicates automatically across zones, such as zone-redundant storage and SQL Database.


**What are non-regional services?**

Non-regional services are services that are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.


**What is a resource in Azure?**

A manageable item that's available through Azure. Virtual machines (VMs), storage accounts, web apps, databases, and virtual networks are examples of resources.


**What is a resource group in Azure?**

A container that holds related resources for an Azure solution. The resource group includes resources that you want to manage as a group.


**What is the purpose of a resource group in Azure?**

The purpose of a resource group is to help manage and organize Azure resources by placing resources of similar usage, type, or location in a resource group.


**Can a resource belong to multiple resource groups in Azure?**

No, a resource can only be a member of a single resource group.


**Can resource groups be nested in Azure?**

No, resource groups can't be nested.


**What happens when a resource group is deleted in Azure?**

When a resource group is deleted, all resources contained within it are also deleted.


**How can resource groups be used for authorization in Azure?**

Resource groups are also a scope for applying role-based access control (RBAC) permissions. By applying RBAC permissions to a resource group, you can ease administration and limit access to allow only what's needed.


**What is the relationship between resources and resource groups in Azure?**

All resources must be in a resource group, and a resource can only be a member of a single resource group.


**What is an Azure subscription?**

An Azure subscription is a logical unit of Azure services that links to an Azure account, which is an identity in Azure Active Directory (Azure AD) or in a directory that Azure AD trusts. It provides authenticated and authorized access to Azure products and services and allows you to provision resources.


**What are the two types of subscription boundaries in Azure?**

The two types of subscription boundaries in Azure are Billing boundary and Access control boundary.


**What happens when you delete a subscription in Azure?**

When you delete a subscription in Azure, all resources contained within it are also deleted.


**What is the purpose of creating a billing profile in Azure?**

The purpose of creating a billing profile in Azure is to have its own monthly invoice and payment method.


**How can you manage costs in Azure?**

You can manage costs in Azure by creating multiple subscriptions for different types of billing requirements, and Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.


**What is the purpose of resource access control in Azure?**

The purpose of resource access control in Azure is to manage and control access to the resources that users provision within each subscription.


**What is the purpose of an Azure management group?**
Azure management groups provide a level of scope above subscriptions for efficiently managing access, policies, and compliance for those subscriptions.


**How do management groups affect subscriptions?**

All subscriptions within a management group automatically inherit the conditions applied to the management group.


**Can all subscriptions within a single management group trust different Azure AD tenants?**

No, all subscriptions within a single management group must trust the same Azure AD tenant.


**How can management groups be used for governance?**

You can apply policies to a management group that limit the regions available for VM creation, for example, which would be applied to all management groups, subscriptions, and resources under that management group.


**How can management groups be used to provide user access to multiple subscriptions?**

By moving multiple subscriptions under that management group, you can create one role-based access control (RBAC) assignment on the management group, which will inherit that access to all the subscriptions.


**How many management groups can be supported in a single directory?**

10,000 management groups can be supported in a single directory.


**How many levels of depth can a management group tree support?**

A management group tree can support up to six levels of depth, not including the root level or the subscription level.


**Can each management group and subscription have multiple parents?**

No, each management group and subscription can support only one parent.


**Is each management group and subscription within a single hierarchy in each directory?**

Yes, all subscriptions and management groups are within a single hierarchy in each directory.