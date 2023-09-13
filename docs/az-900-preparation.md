---
title: AZ-900 Preparation
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - azure
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


## Azure accounts

To create and use Azure services, you need an Azure subscription. After you've created an Azure account, you're free to create additional subscriptions. After you've created an Azure subscription, you can start creating Azure resources within each subscription.

![Azure suscription](img/az-900_1.png)


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



## Architectural components

The core architectural components of Azure may be broken down into two main groupings: the physical infrastructure, and the management infrastructure.

### Physical infrastructure

The physical infrastructure for Azure starts with datacenters. Conceptually, the datacenters are the same as large corporate datacenters. They’re facilities with resources arranged in racks, with dedicated power, cooling, and networking infrastructure.  Individual datacenters aren’t directly accessible. Datacenters are grouped into Azure Regions or Azure Availability Zones

#### Azure Region

A region is a geographical area that contains at least one (but potentially multiple) datacenters that are networked together with a low-latency network.

Every Azure region is paired with another region within the same geography (ie. US, Europe, or Asia) at least 300 miles away in order to allow replication of resources across that geography. Replicating resources across region pairs helps reduce interruptions due to events like natural disasters, civil unrest, power outages, or physical network outages that affect both regions at once.

Some services or features are only available in certain regions. Others don't require to select an specific region. For instance: Azure Active Directory, Azure Traffic Manager, or Azure DNS.


![Azure Regions](img/azure-region.png)


#### Availability zones

Availability zones are physically separate datacenters within an Azure region. Each availability zone is made up of one or more datacenters equipped with independent power, cooling, and networking.

Availability zones are physically separate datacenters within an Azure region. Every availability zone includes one or more datacenters that features independent power, cooling, and networking. In essence, an availability zone is designed to be an isolation boundary, meaning if one zone goes down, the other continues working.  

Availability zones are designed primarily for VMs, managed disks, load balancers, and SQL databases.   It is important to remember that availability zones are connected through private high-speed fiber-optic networks. The image below shows what availability zones look like within a region: 

![Azure Regions](img/azure-availability-zone.png)

To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled regions. However, not all Azure Regions currently support availability zones.

Azure services that support availability zones fall into three categories:

- Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
- Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
- Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.


#### Region pairs

Each Azure region is paired with another region within the same geography at least 300 miles away. This is done to allow for the replication of resources across a geography and reduce the chance of unavailability. West US region is, for instance, paired with East US.

If an outage occurs:  one region is prioritized to make sure that at least one is restored as quickly as possible. It also does so to minimize downtime.  Data continues to reside within the same geography as its pair (except for Brazil South) for tax -and law- enforcement jurisdiction purposes.

> Most regions are paired in two directions, meaning they are the backup for the region that provides a backup for them (West US and East US back each other up). However, some regions, such as West India and Brazil South, are paired in only one direction. In a one-direction pairing, the Primary region does not provide backup for its secondary region. So, even though West India’s secondary region is South India, South India does not rely on West India. West India's secondary region is South India, but South India's secondary region is Central India. Brazil South is unique because it's paired with a region outside of its geography. Brazil South's secondary region is South Central US. The secondary region of South Central US isn't Brazil South.


**Sovereign regions**

>In addition to regular regions, Azure also has sovereign regions. Sovereign regions are instances of Azure that are isolated from the main instance of Azure. You may need to use a sovereign region for compliance or legal purposes. Azure sovereign regions include:
>	- US DoD Central, US Gov Virginia, US Gov Iowa and more: These regions are physical and logical network-isolated instances of Azure for U.S. government agencies and partners. These datacenters are operated by screened U.S. personnel and include additional compliance certifications.
>	- China East, China North, and more: These regions are available through a unique partnership between Microsoft and 21Vianet, whereby Microsoft doesn't directly maintain the datacenters.


### Management infrastructure
#### Azure Resources and Resource Groups 

A resource is the basic building block of Azure. Anything you create, provision, deploy, etc. is a resource. Virtual Machines (VMs), virtual networks, databases, cognitive services, etc. are all considered resources within Azure.

Resource groups are simply groupings of resources. When you create a resource, you’re required to place it into a resource group. While a resource group can contain many resources, a single resource can only be in one resource group at a time. Some resources may be moved between resource groups, but when you move a resource to a new group, it will no longer be associated with the former group. Additionally, resource groups can't be nested, meaning you can’t put resource group B inside of resource group A.

If you grant or deny access to a resource group, you’ve granted or denied access to all the resources within the resource group. When deleting a resource group, all resources included in it  will be deleted, so it makes sense to organized your resource groups by similar lifecycle, or by function.

Resource groups are also a scope for applying RBAC (Role Based Access Control) permissions.

#### Azure Subscription

An Azure subscription provides authenticated and authorized access to Azure products and services and allows organizations to provision cloud resources. Every Azure subscription links to an Azure account, which is an identity in Azure AD or in a directory that Azure AD trusts.  In Azure, subscriptions are a unit of management, billing, and scale.

An account can have multiple subscriptions, but it’s only required to have one. In a multi-subscription account, you can use the subscriptions to configure different billing models and apply different access-management policies. You can use Azure subscriptions to define boundaries around Azure products, services, and resources. There are two types of subscription boundaries that you can use:

- **Billing boundary**: This subscription type determines how an Azure account is billed for using Azure. You can create multiple subscriptions for different types of billing requirements. Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.
- **Access control boundary**: Azure applies access-management policies at the subscription level, and you can create separate subscriptions to reflect different organizational structures. An example is that within a business, you have different departments to which you apply distinct Azure subscription policies. This billing model allows you to manage and control access to the resources that users provision with specific subscriptions. 

An account can have one subscription or multiple subscriptions that have different billing models. You can also use subscription to apply different access-management policies when necessary. For example, you might choose to create additional subscriptions to separate:

- **Environments**: separate environments for development and testing, security, or to isolate data for compliance reasons. This design is particularly useful because resource access control occurs at the subscription level.
- **Organizational structures**:  you could limit one team to lower-cost resources, while allowing the IT department a full range. This design allows you to manage and control access to the resources that users provision within each subscription.
- **Billing**: For instance, you might want to create one subscription for your production workloads and another subscription for your development and testing workloads.


#### Management Groups in Azure 

To efficiently manage access, policies (like available regions), and compliance when you manage multiple Azure subscriptions, you can use Management Groups, because management groups provide scope that sits above subscriptions.  

When managing multiple subscriptions, you organize those subscriptions into containers called management groups, to  which you can then apply governance conditions. All subscriptions within a management group will, in turn, inherit the conditions you apply to the management group.  

All subscriptions within a single management group must trust the same Azure AD tenant.

The image below highlights how you can create a hierarchy for governance through the use of management groups: 

![Azure management group](img/azure-management-group.png)

Some examples of how you could use management groups might be:

- **Create a hierarchy that applies a policy**. 
- **Provide user access to multiple subscriptions**. 


Facts we need to know:

- Maximum of 10,000 management groups supported in a single directory.
- A management group tree can support up to six levels of depth (root and subscription level not included)
- Each management group and subscription can support only one parent.



## Azure Compute services and products

Azure compute is an on-demand computing service that organizations use to run cloud-based applications. It provides compute resources like disks, processors, memory, networking, and even operating systems. Azure supports many types of compute solutions, including Linux, Windows Server, SQL Server, Oracle, IBM, and SAP. Each Azure compute service offers different options depending on your requirements. The most common Azure compute services are:

- 1. Azure Virtual Machines 
	- VM Scale Sets 
	- VM Availability Sets
- 2. Azure Virtual Desktop 
- 3. Azure Container Instances 
- 4. Azure Functions (serverless computing)
- 5. Azure App Service 
- 6. Azure Virtual Networking
- 7. Azure Virtual Private Networks
- 8. Azure ExpressRoute
- 9. Azure DNS


### 1. Azure Virtual Machines

Virtual machines are virtual versions of physical computers that feature virtual processors, memory, storage, and networking resources. They host an operating system just like a physical computer, and you can install and run software on them just like a physical computer. 

VM provides IaaS and can be used in two ways:

- When you need total control over an operating system /environment, VMs are ideal when using in-house or customized software.

#### Virtual Machine Scale Sets 

Azure can also manage the grouping of VMs for you with features such as scale sets and availability sets. A virtual machine scale set allows you to deploy and manage a set of identical VMs that you can use to deploy solutions with true autoscale. As demand increases, VM instances can be added.

#### Virtual machine availability sets

Virtual machine availability sets are another tool to  ensure that VMs stagger updates and have varied power and network connectivity, preventing you from losing all your VMs with a single network or power failure.

Availability sets do this by grouping VMs in two ways: update domain and fault domain.

- **Update domain**: The update domain groups VMs that can be rebooted at the same time. 
- **Fault domain**: The fault domain groups your VMs by common power source and network switch. By default, an availability set will split your VMs across up to three fault domains. This helps protect against a physical power or networking failure by having VMs in different fault domains.

There’s no additional cost for configuring an availability set. You only pay for the VM instances you create.

When to use VMs: During testing and development, When running applications in the cloud, When extending your datacenter to the cloud, During disaster recovery.

### 2. Azure Virtual Desktop

Azure Virtual Desktop is a desktop and application virtualization service that runs on the cloud. It enables you to use a cloud-hosted version of Windows from any location. Azure Virtual Desktop provides centralized security management for users' desktops with Azure Active Directory (Azure AD). You can enable multifactor authentication to secure user sign-ins. You can also secure access to data by assigning granular role-based access controls (RBACs) to users.  With Azure Virtual Desktop, the data and apps are separated from the local hardware. The actual desktop and apps are running in the cloud, meaning the risk of confidential data being left on a personal device is reduced. Azure Virtual Desktop lets you use Windows 10 or Windows 11 Enterprise multi-session, the only Windows client-based operating system that enables multiple concurrent users on a single VM.

### 3. Azure Container Instances 

Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host.  Virtual machines appear to be an instance of an operating system that you can connect to and manage.

**VM vs Containers**

VM virtualizes the hardware emulating a computer. Containers virtualizes the Operating System. Unlike virtual machines, you don't manage the operating system for a container. Containers are a virtualization environment. If you need complete control, you use VM. On the other hands, Container priorizes portability and performance.

#### Azure Container Instances (ACI)

Azure Container Instances offer the fastest and simplest way to run a container in Azure; without having to manage any virtual machines or adopt any additional services. Azure Container Instances are a platform as a service (PaaS) offering. Azure Container Instances allow you to upload your containers and then the service will run the containers for you.

**Azure Container Instances ACI versus Azure Kubernetes service  AKS**

For many organizations, containers have become the preferred way to package, deploy, and manage cloud apps. 

- Azure Container Instances (ACI) is the easiest way to run a container in Azure, without the need for any VMs or other infrastructure.  You can use docker images.
- However, if you require full container orchestration, Microsoft  recommends Azure Kubernetes Service (AKS). 
#### Azure Container Apps

Azure Container Apps are similar in many ways to a container instance. They allow you to get up and running right away, they remove the container management piece, and they're a PaaS offering. Container Apps have extra benefits such as the ability to incorporate load balancing and scaling. These other functions allow you to be more elastic in your design.

#### Azure Kubernetes Service (AKS)

Azure Kubernetes Service (AKS) is a container orchestration service. An orchestration service manages the lifecycle of containers. When you're deploying a fleet of containers, AKS can make fleet management simpler and more efficient.

AKS simplifies the deployment of a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. Since it’s hosted, Azure handles the health monitoring and maintenance. The Kubernetes masters are managed by Azure, and you manage and maintain the agent nodes.  
 
It’s important to note that AKS itself is free. You pay only for the agent nodes within your clusters, not for the masters. 

You can deploy an AKS cluster using  Azure CLI, Azure Portal, Azure Powershell, and Template-driven deployment options  (ARM templates, bicep, terraform).

### 4. Azure Functions (serverless computing)

Functions are a serverless technology that are best used in cases where you're concerned only about the code running your service and not the underlying platform or infrastructure.

Azure Functions is an event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers. If you build an app using VMs or containers, those resources have to be “running” in order for your app to function. With Azure Functions, an event wakes the function, alleviating the need to keep resources provisioned when there are no events.

Benefits:
- No infraestructure management: as a business you don't have to focus on administrative tasks.
- Scalability.
- You only pay for what you use.

Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer, or message from another Azure service. Azure Functions runs your code when it's triggered and automatically deallocates resources when the function is finished. In this model, you're only charged for the CPU time used while your function runs. Functions can be either stateless or stateful. When they're stateless (the default), they behave as if they're restarted every time they respond to an event. When they're stateful (called Durable Functions), a context is passed through the function to track prior activity.

### 5. Azure App Service

App Service is a compute platform that you can use to quickly build, deploy, and scale enterprise grade web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice (it supports multiple languages, including .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python) without managing infrastructure (it also supports both Windows and Linux environments).

App service is a PaaS offering. It offers automatic scaling and high availability. It enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.

App Service handles most of the infrastructure decisions you deal with in hosting web-accessible apps:

- Deployment and management are integrated into the platform.
- Endpoints can be secured.
- Sites can be scaled quickly to handle high traffic loads.
- The built-in load balancing and traffic manager provide high availability.

#### Web apps

App Service includes full support for hosting web apps by using ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP, or Python. You can choose either Windows or Linux as the host operating system.

#### API apps (Azure Rest API)

Much like hosting a website, you can build REST-based web APIs by using your choice of language and framework. You get full Swagger support and the ability to package and publish your API in Azure Marketplace. The produced apps can be consumed from any HTTP- or HTTPS-based client.

#### WebJobs

You can use the WebJobs feature to run a program (.exe, Java, PHP, Python, or Node.js) or script (.cmd, .bat, PowerShell, or Bash) in the same context as a web app, API app, or mobile app. They can be scheduled or run by a trigger. WebJobs are often used to run background tasks as part of your application logic.

#### Mobile apps

Use the Mobile Apps feature of App Service to quickly build a back end for iOS and Android apps. With just a few actions in the Azure portal, you can store mobile app data in a cloud-based SQL database; authenticate customers against common social providers, such as MSA, Google, Twitter, and Facebook; send push notifications; execute custom back-end logic in C# or Node.js.

On the mobile app side, there's SDK support for native iOS and Android, Xamarin, and React native apps.

- Access, manage, monitor Azure accounts and resources.
- Monitor the health and status of Azure resources, check for alerts, diagnose and fix issues.
- Stop, start, restart a web app or virtual machine.  
- Run the Azure CLI or Azure PowerShell commands to manage Azure resources. 

#### Azure Advisor

Free services that helps you follow best practices. 

#### ARM templates 

ARM templates allow you to declaratively describe the resources you want to use, using JSON format. The template will then create those resources in parallel. For example, need 25 VMs, all 25 VMs will be created at the same time. 

### 6. Azure Virtual Networking

Azure virtual networks and virtual subnets enable Azure resources, such as VMs, web apps, and databases, to communicate with each other, with users on the internet, and with your on-premises client computers. 

Azure virtual networking supports both public and private endpoints to enable communication between external or internal resources with other internal resources.

- Public endpoints have a public IP address and can be accessed from anywhere in the world.
- Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network.

It provides the following key networking capabilities: 

**Isolation and segmentation**: Azure virtual network allows you to create multiple isolated virtual networks. For name resolution, you can use the name resolution service that's built into Azure. You also can configure the virtual network to use either an internal or an external DNS server.

**Internet communications**: You can enable incoming connections from the internet by assigning a public IP address to an Azure resource, or putting the resource behind a public load balancer.

**Communicate between Azure resources**: Enable Azure resources to communicate securely with each other. Virtual networks can connect not only VMs but other Azure resources. Service endpoints can connect to other Azure resource types.

**Communicate with on-premises resources**: Azure virtual networks enable you to link resources together in your on-premises environment and within your Azure subscription.
	- Point-to-site virtual private network connections are from a computer outside your organization back into your corporate network. In this case, the client computer initiates an encrypted VPN connection to connect to the Azure virtual network.
	- Site-to-site virtual private networks link your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network. In effect, the devices in Azure can appear as being on the local network. The connection is encrypted and works over the internet.
	- Azure ExpressRoute provides a dedicated private connectivity to Azure that doesn't travel over the internet. ExpressRoute is useful for environments where you need greater bandwidth and even higher levels of security.

**Route network traffic**: By default, Azure routes traffic between subnets on any connected virtual networks, on-premises networks, and the internet. Route tables allow you to define rules about how traffic should be directed. Border Gateway Protocol (BGP) works with Azure VPN gateways, Azure Route Server, or Azure ExpressRoute to propagate on-premises BGP routes to Azure virtual networks.

**Filter network traffic**: filter traffic between subnets.
- Network security groups are Azure resources that can contain multiple inbound and outbound security rules. You can define these rules to allow or block traffic, based on factors such as source and destination IP address, port, and protocol.
- Network virtual appliances are specialized VMs that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing wide area network (WAN) optimization.

**Connect virtual networks**:  You can link virtual networks together by using virtual network peering. Peering allows two virtual networks to connect directly to each other. Network traffic between peered networks is private, and travels on the Microsoft backbone network, never entering the public internet. Peering enables resources in each virtual network to communicate with each other. These virtual networks can be in separate regions, which allows you to create a global interconnected network through Azure.

User-defined routes (UDR) allow you to control the routing tables between subnets within a virtual network or between virtual networks. This allows for greater control over network traffic flow.


### 7. Azure Virtual Private Networks

A virtual private network (VPN) uses an encrypted tunnel within another network. VPNs are typically deployed to connect two or more trusted private networks to one another over an untrusted network (typically the public internet). Traffic is encrypted while traveling over the untrusted network to prevent eavesdropping or other attacks. VPNs can enable networks to safely and securely share sensitive information.

#### Azure VPN Gateway instances

Azure VPN Gateway instances are deployed in a dedicated subnet of the virtual network and enable the following connectivity:
- Connect on-premises datacenters to virtual networks through a site-to-site connection.
- Connect individual devices to virtual networks through a point-to-site connection.
- Connect virtual networks to other virtual networks through a network-to-network connection.

When setting up a VPN gateway, you must specify the type of VPN - either policy-based or route-based:

- **Policy-based VPN gateways** specify statically the IP address of packets that should be encrypted through each tunnel. This type of device evaluates every data packet against those sets of IP addresses to choose the tunnel where that packet is going to be sent through.
- In** Route-based gateways**, IPSec tunnels are modeled as a network interface or virtual tunnel interface. IP routing (either static routes or dynamic routing protocols) decides which one of these tunnel interfaces to use when sending each packet. Route-based VPNs are the preferred connection method for on-premises devices. They're more resilient to topology changes such as the creation of new subnets.

Use a route-based VPN gateway if you need any of the following types of connectivity:

- Connections between virtual networks
- Point-to-site connections
- Multisite connections
- Coexistence with an Azure ExpressRoute gateway


There are a few ways to maximize the resiliency of your VPN gateway:

**Active/standby**: By default, VPN gateways are deployed as two instances in an active/standby configuration, even if you only see one VPN gateway resource in Azure. When planned maintenance or unplanned disruption affects the active instance, the standby instance automatically assumes responsibility for connections without any user intervention.

**Active/active**: With the introduction of support for the BGP routing protocol, you can also deploy VPN gateways in an active/active configuration. In this configuration, you assign a unique public IP address to each instance. You then create separate tunnels from the on-premises device to each IP address. 

**ExpressRoute failover**: Another high-availability option is to configure a VPN gateway as a secure failover path for ExpressRoute connections. ExpressRoute circuits have resiliency built in. However, they aren't immune to physical problems that affect the cables delivering connectivity or outages that affect the complete ExpressRoute location. 

**Zone-redundant gateways**: In regions that support availability zones, VPN gateways and ExpressRoute gateways can be deployed in a zone-redundant configuration. This configuration brings resiliency, scalability, and higher availability to virtual network gateways.  These gateways require different gateway stock keeping units (SKUs) and use Standard public IP addresses instead of Basic public IP addresses.






### 8.  Azure ExpressRoute

Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider. This connection is called an ExpressRoute Circuit. These connection between Microsoft cloud services (such as Microsoft Azure and Microsoft 365) and the offices, datacenters, or other facilities would require its own ExpressRoute circuit.

ExpressRoute connections don't go over the public Internet. ExpressRoute is a private connection from your on-premises infrastructure to your Azure infrastructure. Even if you have an ExpressRoute connection, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests are still sent over the public internet.

- Connectivity to Microsoft cloud services across all regions in the geopolitical region.
- Global connectivity to Microsoft services across all regions with the ExpressRoute Global Reach.
- Dynamic routing between your network and Microsoft via Border Gateway Protocol (BGP).
- Built-in redundancy in every peering location for higher reliability.

ExpressRoute enables direct access to the following services in all regions:

- Microsoft Office 365
- Microsoft Dynamics 365
- Azure compute services, such as Azure Virtual Machines
- Azure cloud services, such as Azure Cosmos DB and Azure Storage

#### Features

**Global connectivity**: For example, say you had an office in Asia and a datacenter in Europe, both with ExpressRoute circuits connecting them to the Microsoft network. You could use ExpressRoute Global Reach to connect those two facilities, allowing them to communicate without transferring data over the public internet.

**Dynamic routing**: ExpressRoute uses the BGP. BGP is used to exchange routes between on-premises networks and resources running in Azure. This protocol enables dynamic routing between your on-premises network and services running in the Microsoft cloud.

**Built-in redundancy**: Each connectivity provider uses redundant devices to ensure that connections established with Microsoft are highly available. You can configure multiple circuits to complement this feature.

#### ExpressRoute connectivity models

ExpressRoute supports four models that you can use to connect your on-premises network to the Microsoft cloud:

**Co-location at a cloud exchange**: Your datacenter, office, or other facility is  physically co-located at a cloud exchange, such as an ISP. In this case, you can request a virtual cross-connect to the Microsoft cloud.

**Point-to-point Ethernet connection**: Point-to-point ethernet connection refers to using a point-to-point connection to connect your facility to the Microsoft cloud.

**Any-to-any networks**: With any-to-any connectivity, you can integrate your wide area network (WAN) with Azure by providing connections to your offices and datacenters. Azure integrates with your WAN connection to provide a connection like you would have between your datacenter and any branch offices.

**Directly from ExpressRoute sites**: You can connect directly into the Microsoft's global network at a peering location strategically distributed across the world. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale.









### 9. Azure DNS

Azure DNS is a hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure. By hosting your domains in Azure, you can manage your DNS records using the same credentials, APIs, tools, and billing as your other Azure services. Azure DNS can manage DNS records for your Azure services and provide DNS for your external resources as well. Applications that require automated DNS management can integrate with the service by using the REST API and SDKs.

Azure DNS is based on Azure Resource Manager, which provides features such as:

- Azure role-based access control (Azure RBAC) to control who has access to specific actions for your organization.
- Activity logs to monitor how a user in your organization modified a resource or to find an error when troubleshooting. 
- Resource locking to lock a subscription, resource group, or resource. Locking prevents other users in your organization from accidentally deleting or modifying critical resources.

Azure DNS also supports private DNS domains. This feature allows you to use your own custom domain names in your private virtual networks, rather than being stuck with the Azure-provided names.

Azure DNS also supports alias record sets. You can use an alias record set to refer to an Azure resource, such as an Azure public IP address, an Azure Traffic Manager profile, or an Azure Content Delivery Network (CDN) endpoint. 

You can't use Azure DNS to buy a domain name. For an annual fee, you can buy a domain name by using App Service domains or a third-party domain name registrar. Once purchased, your domains can be hosted in Azure DNS for record management.




## Azure Storage Services

A storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in this account is secure, highly available, durable, and massively scalable.  When you create your storage account, you’ll start by picking the storage account type. The type of account determines the storage services and redundancy options and has an impact on the use cases.


|**Type**|**Supported services**|**Redundancy Options**|**Usage**|
|---|---|---|---|
|Standard general-purpose v2|Blob Storage (including Data Lake Storage), Queue Storage, Table Storage, and Azure Files|LRS, GRS, RA-GRS, ZRS, GZRS, RA-GZRS|Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Azure Storage. If you want support for network file system (NFS) in Azure Files, use the premium file shares account type.|
|Premium block blobs|Blob Storage (including Data Lake Storage)|LRS, ZRS|Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency.|
|Premium file shares|Azure Files|LRS, ZRS|Premium storage account type for file shares only. Recommended for enterprise or high-performance scale applications. Use this account type if you want a storage account that supports both Server Message Block (SMB) and NFS file shares.|
|Premium page blobs|Page blobs only|LRS|Premium storage account type for page blobs only.|

Some acronyms here:

- Locally redundant storage (LRS)
- Geo-redundant storage (GRS)
- Read-access geo-redundant storage (RA-GRS)
- Zone-redundant storage (ZRS)
- Geo-zone-redundant storage (GZRS)
- Read-access geo-zone-redundant storage (RA-GZRS)

**Storage account endpoints**:

The following table shows the endpoint format for Azure Storage services.

|**Storage service**|**Endpoint**|
|---|---|
| Blob Storage | https://\<storage-account-name\>.blob.core.windows.net |
| Data Lake Storage Gen2 | https://\<storage-account-name\>.dfs.core.windows.net |
| Azure Files | https://\<storage-account-name\>.file.core.windows.net |
| Queue Storage | https://\<storage-account-name\>.queue.core.windows.net |
| Table Storage | https://\<storage-account-name\>.table.core.windows.net |


### Azure storage redundancy

Data in an Azure Storage account is always replicated three times in the primary region. Azure Storage offers two options for how your data is replicated in the primary region, locally redundant storage (LRS) and zone-redundant storage (ZRS).


#### Redundancy in the primary region

**Locally redundant storage (LRS)**

Locally redundant storage (LRS) replicates your data three times within a single data center in the primary region. LRS provides at least 11 nines of durability (99.999999999%) of objects over a given year. LRS is the lowest-cost redundancy option and offers the least durability compared to other options. LRS protects your data against server rack and drive failures. However, if a disaster such as fire or flooding occurs within the data center, all replicas of a storage account using LRS may be lost or unrecoverable. To mitigate this risk, Microsoft recommends using zone-redundant storage (ZRS), geo-redundant storage (GRS), or geo-zone-redundant storage (GZRS).

![LRS](img/az-900_2.png)


**Zone-redundant storage (ZRS)**

For Availability Zone-enabled Regions, zone-redundant storage (ZRS) replicates your Azure Storage data synchronously across three Azure availability zones in the primary region. ZRS offers durability for Azure Storage data objects of at least 12 nines (99.9999999999%) over a given year. With ZRS, your data is still accessible for both read and write operations even if a zone becomes unavailable. Microsoft recommends using ZRS in the primary region for scenarios that require high availability. ZRS is also recommended for restricting replication of data within a country or region to meet data governance requirements.

![ZRS](img/az-900_3.png)

#### Redundancy in the secondary region

For applications requiring high durability, you can choose to additionally copy the data in your storage account to a secondary region that is hundreds of miles away from the primary region. If the data in your storage account is copied to a secondary region, then your data is durable even in the event of a catastrophic failure that prevents the data in the primary region from being recovered. When you create a storage account, you select the primary region for the account. The paired secondary region is based on Azure Region Pairs, and can't be changed.

By default, data in the secondary region isn't available for read or write access unless there's a failover to the secondary region. If the primary region becomes unavailable, you can choose to fail over to the secondary region. After the failover has completed, the secondary region becomes the primary region, and you can again read and write data.

Because data is replicated to the secondary region asynchronously, a failure that affects the primary region may result in data loss if the primary region can't be recovered. The interval between the most recent writes to the primary region and the last write to the secondary region is known as the recovery point objective (RPO). The RPO indicates the point in time to which data can be recovered. Azure Storage typically has an RPO of less than 15 minutes, although there's currently no SLA on how long it takes to replicate data to the secondary region.

Azure Storage offers two options for copying your data to a secondary region: geo-redundant storage (GRS) and geo-zone-redundant storage (GZRS). GRS is similar to running LRS in two regions, and GZRS is similar to running ZRS in the primary region and LRS in the secondary region.

**Geo-redundant storage (GRS)**

GRS copies your data synchronously three times within a single physical location in the primary region using LRS. It then copies your data asynchronously to a single physical location in the secondary region (the region pair) using LRS. GRS offers durability for Azure Storage data objects of at least 16 nines (99.99999999999999%) over a given year.

![GRS](img/az-900_4.png)


**Geo-zone-redundant storage** (GZRS)

GZRS combines the high availability provided by redundancy across availability zones with protection from regional outages provided by geo-replication. Data in a GZRS storage account is copied across three Azure availability zones in the primary region (similar to ZRS) and is also replicated to a secondary geographic region, using LRS, for protection from regional disasters. Microsoft recommends using GZRS for applications requiring maximum consistency, durability, and availability, excellent performance, and resilience for disaster recovery. GZRS is designed to provide at least 16 nines (99.99999999999999%) of durability of objects over a given year.

![GZRS](img/az-900_5.png)


Read access to data in the secondary region (RA-GRS)
Geo-redundant storage (with GRS or GZRS) replicates your data to another physical location in the secondary region to protect against regional outages. However, that data is available to be read only if the customer or Microsoft initiates a failover from the primary to secondary region. However, if you enable read access to the secondary region, your data is always available, even when the primary region is running optimally. For read access to the secondary region, enable read-access geo-redundant storage (RA-GRS) or read-access geo-zone-redundant storage (RA-GZRS). Remember that the data in your secondary region may not be up-to-date due to RPO.


### Azure storage services

- 1. **Azure Blobs**: A massively scalable object store for text and binary data. Also includes support for big data analytics through Data Lake Storage Gen2.
- 2. **Azure Files**: Managed file shares for cloud or on-premises deployments.
- 3. **Azure Queues**: A messaging store for reliable messaging between application components.
- 4. **Azure Disks**: Block-level storage volumes for Azure VMs.
- 5. **Azure Tables:** NoSQL table option for structured, non-relational data.


#### Azure Blobs

To store massive amounts of data, such as text or binary data. Azure Blob storage is unstructured, meaning that there are no restrictions on the kinds of data it can hold. Blob storage is ideal for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.

Objects in blob storage can be accessed from anywhere in the world via HTTP or HTTPS. Users or client applications can access blobs via URLs, the Azure Storage REST API, Azure PowerShell, Azure CLI, or an Azure Storage client library.

Azure Storage offers different access tiers for your blob storage:

- **Hot access tier**: Optimized for storing data that is accessed frequently (for example, images for your website).
- **Cool access tier**: Optimized for data that is infrequently accessed and stored for at least 30 days (for example, invoices for your customers).
- **Cold access tier**: Optimized for storing data that is infrequently accessed and stored for at least 90 days.
- **Archive access tier**: Appropriate for data that is rarely accessed and stored for at least 180 days, with flexible latency requirements (for example, long-term backups).

Some considerations:

- Hot, cool, and cold access tiers can be set at the account level. The archive access tier isn't available at the account level.
- Hot, cool, cold, and archive tiers can be set at the blob level, during or after upload.
- Data in the cool and cold access tiers can tolerate slightly lower availability, but still requires high durability, retrieval latency, and throughput characteristics similar to hot data. For cool and cold data, a lower availability service-level agreement (SLA) and higher access costs compared to hot data are acceptable trade-offs for lower storage costs.
- Archive storage stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data.

#### Azure Files

Azure File storage offers fully managed file shares in the cloud that are accessible via the industry standard Server Message Block (SMB) or Network File System (NFS) protocols. Azure Files file shares can be mounted concurrently by cloud or on-premises deployments. SMB Azure file shares are accessible from Windows, Linux, and macOS clients. NFS Azure Files shares are accessible from Linux or macOS clients. 

PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the administration of Azure applications. You can create and manage Azure file shares using Azure portal and Azure Storage Explorer.

Applications running in Azure can access data in the share via file system I/O APIs.  In addition to System IO APIs, you can use Azure Storage Client Libraries or the Azure Storage REST API.

#### Azure Queues

Azure Queue storage is a service for storing large numbers of messages. Once stored, you can access the messages from anywhere in the world via authenticated calls using HTTP or HTTPS. A queue can contain as many messages as your storage account has room for (potentially millions). Each individual message can be up to 64 KB in size. Queues are commonly used to create a backlog of work to process asynchronously.

Queue storage can be combined with compute functions like Azure Functions to take an action when a message is received. F

#### Azure Disks

Azure Disk storage, or Azure managed disks, are block-level storage volumes managed by Azure for use with Azure VMs. Conceptually, they’re the same as a physical disk, but they’re virtualized – offering greater resiliency and availability than a physical disk. 

#### Azure Tables

Azure Table storage stores large amounts of structured data. Azure tables are a NoSQL datastore that accepts authenticated calls from inside and outside the Azure cloud. 



### Azure data migration options

Azure Migrate is a service that helps you migrate from an on-premises environment to the cloud:
- Unified migration platform: A single portal to start, run, and track your migration to Azure.
- Range of tools: Azure Migrate also integrates with other Azure services and tools, and with independent software vendor (ISV) offerings.
- Assessment and migration: In the Azure Migrate hub, you can assess and migrate your on-premises infrastructure to Azure.

Tools to help with migration:

#### **Azure Migrate: Discovery and assessment**

Discover and assess on-premises servers running on VMware, Hyper-V, and physical servers in preparation for migration to Azure.

####  **Azure Migrate: Server Migration**

Migrate VMware VMs, Hyper-V VMs, physical servers, other virtualized servers, and public cloud VMs to Azure.

#### Data Migration Assistant

Data Migration Assistant is a stand-alone tool to assess SQL Servers. It helps pinpoint potential problems blocking migration. It identifies unsupported features, new features that can benefit you after migration, and the right path for database migration.

#### Azure Database Migration Service

Migrate on-premises databases to Azure VMs running SQL Server, Azure SQL Database, or SQL Managed Instances.

#### Azure App Service migration assistant

Azure App Service migration assistant is a standalone tool to assess on-premises websites for migration to Azure App Service. Use Migration Assistant to migrate .NET and PHP web apps to Azure.

#### Azure Data Box

Azure Data Box is a physical migration service that helps transfer large amounts of data in a quick, inexpensive, and reliable way. The secure data transfer is accelerated by shipping you a proprietary Data Box storage device that has a maximum usable storage capacity of 80 terabytes. The Data Box is transported to and from your datacenter via a regional carrier. A rugged case protects and secures the Data Box from damage during transit. You can order the Data Box device via the Azure portal to import or export data from Azure. Data Box is ideally suited to transfer data sizes larger than 40 TBs in scenarios with no to limited network connectivity.

**Use cases for importing data**: 
	- Onetime migration - when a large amount of on-premises data is moved to Azure.
	- Moving a media library from offline tapes into Azure to create an online media library.
	- Migrating your VM farm, SQL server, and applications to Azure.
	- Moving historical data to Azure for in-depth analysis and reporting using HDInsight.
	- Initial bulk transfer - when an initial bulk transfer is done using Data Box (seed) followed by incremental transfers over the network.
	- Periodic uploads - when large amount of data is generated periodically and needs to be moved to Azure.

 **Use cases for exporting data:**
	- Disaster recovery - when a copy of the data from Azure is restored to an on-premises network.
	- Security requirements - when you need to be able to export data out of Azure due to government or security requirements.
	- Migrate back to on-premises or to another cloud service provider - when you want to move all the data back to on-premises, or to another cloud service provider, export data via Data Box to migrate the workloads.

#### AzCopy

In addition to large scale migration using services like Azure Migrate and Azure Data Box, Azure also has tools designed to help you move or interact with individual files or small file groups.

AzCopy is a command-line utility that you can use to copy blobs or files to or from your storage account. Synchronizing blobs or files with AzCopy is one-direction synchronization. When you synchronize, you designated the source and destination, and AzCopy will copy files or blobs in that direction. It doesn't synchronize bi-directionally based on timestamps or other metadata.

#### Azure Storage Explorer

In addition to large scale migration using services like Azure Migrate and Azure Data Box, Azure also has tools designed to help you move or interact with individual files or small file groups.

Azure Storage Explorer is a standalone app that provides a graphical interface to manage files and blobs in your Azure Storage Account. It works on Windows, macOS, and Linux operating systems and uses AzCopy on the backend to perform all of the file and blob management tasks.
#### Azure File Sync

In addition to large scale migration using services like Azure Migrate and Azure Data Box, Azure also has tools designed to help you move or interact with individual files or small file groups.

Azure File Sync is a tool that lets you centralize your file shares in Azure Files and keep the flexibility, performance, and compatibility of a Windows file server. 

With Azure File Sync, you can:

- Use any protocol that's available on Windows Server to access your data locally, including SMB, NFS, and FTPS.
- Have as many caches as you need across the world.
- Replace a failed local server by installing Azure File Sync on a new server in the same datacenter.
- Configure cloud tiering so the most frequently accessed files are replicated locally, while infrequently accessed files are kept in the cloud until requested.

## Azure identity, access, and security 


### Azure directory services

When you secure identities on-premises with Active Directory, Microsoft doesn't monitor sign-in attempts. When you connect Active Directory with Azure AD, Microsoft can help protect you by detecting suspicious sign-in attempts at no extra cost.

Azure AD provides services such as:
- **Authentication**: This includes verifying identity to access applications and resources. It also includes providing functionality such as self-service password reset, multifactor authentication, a custom list of banned passwords, and smart lockout services.
- **Single sign-on**: Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A single identity is tied to a user, which simplifies the security model. As users change roles or leave an organization, access modifications are tied to that identity, which greatly reduces the effort needed to change or disable accounts.
- **Application management**: You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user experience.
- **Device management**: Along with accounts for individual people, Azure AD supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also allows for device-based Conditional Access policies to restrict access attempts to only those coming from known devices, regardless of the requesting user account.

#### Azure AD Connect

If you had an on-premises environment running Active Directory and a cloud deployment using Azure AD, you would need to maintain two identity sets. However, you can connect Active Directory with Azure AD, enabling a consistent identity experience between cloud and on-premises.

One method of connecting Azure AD with your on-premises AD is using Azure AD Connect. Azure AD Connect synchronizes user identities between on-premises Active Directory and Azure AD. Azure AD Connect synchronizes changes between both identity systems, so you can use features like SSO, multifactor authentication, and self-service password reset under both systems.


#### Azure Active Directory Domain Services (Azure AD DS)

Azure Active Directory Domain Services (Azure AD DS) is a service that provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/NTLM authentication. Just like Azure AD lets you use directory services without having to maintain the infrastructure supporting it, with Azure AD DS, you get the benefit of domain services without the need to deploy, manage, and patch domain controllers (DCs) in the cloud.

Azure AD DS integrates with your existing Azure AD tenant. This integration lets users sign into services and applications connected to the managed domain using their existing credentials.

**How does Azure AD DS work?**  When you create an Azure AD DS managed domain, you define a unique namespace. This namespace is the domain name. Two Windows Server domain controllers are then deployed into your selected Azure region. This deployment of DCs is known as a replica set. You don't need to manage, configure, or update these DCs. The Azure platform handles the DCs as part of the managed domain, including backups and encryption at rest using Azure Disk Encryption.

A managed domain is configured to perform a one-way synchronization from Azure AD to Azure AD DS. You can create resources directly in the managed domain, but they aren't synchronized back to Azure AD.

## Key Azure Management Tools

There are several tools at your disposal to manage Azure resources and environments. They include the Azure Portal, Azure PowerShell, Azure CLI, the Azure Mobile App, and ARM templates. 

### Azure Portal

The Azure portal is a web-based user interface that you can use to access almost every feature of Azure. It can be used to visually understand and manage your Azure environment, while Azure PowerShell allows you to quickly perform one-off tasks and to script tasks as needed. Azure PowerShell is available for Windows, Linux, and Mac, and you can access it in a web browser via Azure Cloud Shell. 

Azure Portal does not offer a way to automate repetitive tasks.


### Azure CLI

The Azure CLI is a command-line interface.  A cross-platform command-line program (Windows, Linux and macOs) to connect to Azure and execute administrative commands. 

It’s an executable program that you can use to execute commands in Bash. You can use the Azure CLI to perform every possible management task in Azure. Like Azure PowerShell, the CLI allows you to run one-off commands or you can combine them into a script and execute them together.

Launch azure cli:

```powershell
# Launch Azure CLI interactive mode
az interactive
```

```azure cli
version
upgrade
exit
```

### Azure PowerShell

 Azure Powershell needs Windows Powershell run since Azure Powershell builds upon Windows Powershell with added features.

```ps
New-AzVm -ResourceGroupName "MyResourceGroup" -Name "MyVM01" -Image "UbuntLTS"
```


### Azure Cloud Shell

Browser-based scripting environment that is accessible from Azure Portal. It requires a storage account. It allows you to choose the shell experience that suits you best. 

During AZ-900 preparation at Microsoft Learn platform, an Azure Cloud Shell is provided. You can practice there the following commands:


```powershell
# Print current date
Get-date

# Print Azure version
az version

# Print Azure suscription
Get-AzureSuscription

# Launch Bash
bash

# you can use the letters az to start an Azure command in the BASH mode.
az upgrade

# Launch Azure CLI interactive mode
az interactive

# Create a VM with UbuntuLTS
az vm create --resourcegroup MyResourceGroup --name MyVM01 --image UbuntLTS --generate-ssh-keys

# Create a VM
az vm create --resource-group learn-857e3399-575d-4759-8de9-0c5a22e035e9 --name my-vm  --public-ip-sku Standard --image Ubuntu2204 --admin-username azureuser  --generate-ssh-keys

# Configure Nginx on your VM
az vm extension set  --resource-group learn-857e3399-575d-4759-8de9-0c5a22e035e9  --vm-name my-vm  --name customScript  --publisher Microsoft.Azure.Extensions  --version 2.1  --settings '{"fileUris":["https://raw.githubusercontent.com/MicrosoftDocs/mslearn-welcome-to-azure/master/configure-nginx.sh"]}'  --protected-settings '{"commandToExecute": "./configure-nginx.sh"}'

# Check running VMs
az vm list

# List IP addresses 
az vm list-ip-addresses

# Create a variable with public IP address: Run the following `az vm list-ip-addresses` command to get your VM's IP address and store the result as a Bash variable:
IPADDRESS="$(az vm list-ip-addresses --resource-group learn-51b45310-54be-47c3-8d62-8e53e9839083 --name my-vm --query "[].virtualMachine.network.publicIpAddresses[*].ipAddress" --output tsv)"

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