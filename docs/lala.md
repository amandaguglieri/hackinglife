
## Test 5

#### Question 1: True or False: Unlike RBAC, Azure Policy is a default-allow-and-explicit-deny system.

- No
- Yes (Correct)
 
A few key differences between Azure Policy and RBAC exist. RBAC focuses on user actions at different scopes. You might be added to the contributor role for a resource group, allowing you to make changes to that resource group. Azure Policy focuses on resource properties during deployment and for already-existing resources. Azure Policy controls properties such as the types or locations of resources. Unlike RBAC, Azure Policy is a default-allow-and-explicit-deny system.

RBAC and Polices in Azure play a vital role in a governance strategy. While different, they both work together to ensure organizational business rules are followed be ensuring proper access and resource creation guidelines are met.

 

![](https://docs.microsoft.com/en-ca/learn/wwl-azure/enterprise-governance/media/az500-role-based-versus-policies-ee3f9164.png)

#### Question 2: Which tier of Azure Files allows you to enable Azure File Sync?

- Both Premium and Standard (Correct)
- Standard
- None of the above
- Premium

Azure File Sync supports both Premium and Standard tiers of Azure Files, which means you can enable Azure File Sync on either tier depending on your performance and cost requirements. Premium tier offers higher performance with lower latency, but at a higher cost compared to the Standard tier. However, it is not the only tier supported for Azure File Sync. Standard tier provides cost-effective storage but with lower performance compared to the Premium tier.

#### Question 3: Your company is looking for a tool that can help with the following:  1) Upload, download and manage Azure Storage blobs, files, queues and tables, as well as Azure Data Lake Storage entities. 2) Configure storage permissions and access controls, tiers and rules. Which of the following is the right choice?

- Azure AzCopy
- Azure Blueprint
- Azure Data Box Gateway
- Azure Policy
- Azure VM Scale Sets
- Azure Storage Explorer (Correct)
- ARM Templates 

#### Question 4: Which of the following are free?

- Data transfer within the same region (Correct)
- Data transfer from one region to another
- Data Ingress (Correct)
- Data transfer within same Availability Zone (Correct)

#### Question 5: What is the key benefit of Azure Arc-enabled Kubernetes clusters?

- They provide additional storage options for Azure VMs, reducing the chances of failures.
- They limit your deployments to Azure regions only, savings costs.
- They enable you to manage and configure Kubernetes clusters across multiple environments (Correct)
- They eliminate the need for container orchestration using Kubernetes.

#### Question 6: Which of the following Azure Migrate features can be used to discover and assess physical servers?

- Dependency visualization
- Agent-less discovery
- Agent-based discovery (Correct)
- Hyper-V discovery

The keyword here is 'physical' servers. The correct answer is 'Agent-Based Discovery'. Agent-based discovery is the correct choice for discovering and assessing physical servers. This method requires the installation of agents on the physical servers, which then collect and report data back to Azure Migrate for assessment.

Other Options -

- Dependency visualization is a feature within Azure Migrate that helps you understand the dependencies between servers, applications, and services. It doesn't directly discover or assess physical servers.
- Hyper-V discovery is used to discover and assess virtual machines running on Hyper-V hosts. It is not designed for discovering and assessing physical servers.
- Agentless discovery is a method used by Azure Migrate to discover and assess virtual machines in virtualized environments, such as VMware or Hyper-V, without the need for installing agents on the source virtual machines. It is not intended for discovering and assessing physical servers.

#### Question 7:  Yes or No: Availability zones are implemented in all Azure regions.

- Yes
- No (Correct)

#### Question 8: What is a key advantage of using Infrastructure as Code (IaC) in cloud deployments?

- It eliminates the need for network monitoring. (Incorrect)
- It reduces the need for data backups.
- It enables version control and automated provisioning. (Correct)
- It increases physical hardware utilization.

Infrastructure as Code (IaC) is a key DevOps practice that involves the management of infrastructure, such as networks, compute services, databases, storages, and connection topology, in a descriptive model. IaC allows teams to develop and release changes faster and with greater confidence. Also, Infrastructure as Code (IaC) allows you to store your infrastructure configuration as code in version control systems. This enables tracking changes over time, collaborating with team members, and automating the provisioning and management of resources.

#### Question 9: Yes or No: Azure Synapse Analytics is an analytics service that brings together data integration, enterprise data warehousing and big data analytics

- No
- Yes (Correct)

Azure Synapse Analytics was previously called Azure SQL Data Warehouse! Azure Synapse Analytics is a limitless analytics service that brings together data integration, enterprise data warehousing and big data analytics. It gives you the freedom to query data on your terms, using either serverless or dedicated resources at scale. Azure Synapse brings these worlds together with a unified experience to ingest, explore, prepare, manage and serve data for immediate BI and machine-learning needs.

#### Question 10: Which of the following can you use to estimate the cost savings you can get by migrating your workloads to Azure?

- Azure TCO Calculator (Correct)
- Azure Cost Management
- Azure Pricing Calculator
- Azure Advisor

#### Question 11: Since your company has shifted to a fully-remote working model, they are looking to provide employees with the best virtualized experience while saving costs by using existing eligible Windows licences. They also want to enable Bring your own device (BYOD) to access their desktop and applications over the Internet. Which of the following would you suggest?

- Azure Virtual Desktop (Correct)
- Azure Kubernetes
- Azure Arc
- Azure ExpressRoute
- Azure FileSync
- Azure Virtual Machines

#### Question 12:  Which of the following is designed for enterprise big data analytics and includes a hierarchical namespace to Blob storage?

- Azure Blob Storage
- Azure Data Lake Storage Gen2 (Correct)
- Azure Files
- Azure Data Box Gateway
- Azure Stack Edge

Azure Data Lake Storage Gen2 is a set of capabilities dedicated to big data analytics, built on [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction). Data Lake Storage Gen2 converges the capabilities of [Azure Data Lake Storage Gen1](https://docs.microsoft.com/en-us/azure/data-lake-store/) with Azure Blob Storage.

#### Question 13: Which Azure service can Azure Firewall integrate with to provide threat intelligence and advanced security analytics?

- Azure Monitor
- Azure Active Directory
- Azure Security Center
- Azure Sentinel (Correct)

#### Question 14: You own a streaming-service website and notice extremely high spikes in traffic whenever a new movie is launched on your platform. However, during the rest of the month you experience moderate traffic. Which of the following benefits does having your website hosted on Azure provide you given this scenario?

- Elasticity (Correct)
- High Latency
- Load Balancing
- Auto-Rollovers
- Fault Tolerance

 
Elasticity in this case is the ability to provide additional compute resource when needed and reduce the compute resource when not needed to reduce costs. 
Autoscaling is an example of elasticity. Here you don't need to provision lot of resources in advance. You will incur costs by allocating more resources only when demand increases!

#### Question 15: If your workload can tolerate interruptions and its execution time is flexible, which of the following pricing plans would be BEST suited to save costs?

- Spot Pricing (Correct)
- Reserved Instances
- Pay-as-you-go
- Dedicated Hosts

#### Question 16: What is the primary purpose of Azure Arc?

- To enable AI-powered analytics for Azure resources.
- To manage and monitor on-premises and multi-cloud environments from a single Azure portal. (Correct)
- To facilitate communication between Azure regions.
- To provide virtual machine hosting services in Azure.

Azure Arc allows organizations to manage and monitor not only Azure resources but also on-premises and multi-cloud environments using the Azure portal. It extends Azure management capabilities to a broader range of resources and locations.

#### Question 17: __________________ provide organizations with the ability to manage the compliance of Azure resources across multiple subscriptions.

- Azure Management Groups (Incorrect)
- Azure Resource Groups
- Azure Subscriptions
- Azure Policy (Correct)
- Azure Conditional Access and MFA

#### Question 18: Which tool should you use to perform a lift-and-shift migration of your on-premises virtual machines to Azure?

- Azure Migrate 
- Server Migration (Correct)
- Azure Database Migration Service
- Azure Site Recovery
- Azure Data Factory

The correct answer is Azure Migrate - Server Migration.  Azure Migrate - Server Migration is the right tool for performing a lift-and-shift migration of your on-premises virtual machines to Azure. It supports various virtualization platforms like VMware, Hyper-V, and physical servers. The tool simplifies the migration process, automates tasks, and ensures minimal downtime during migration.

#### Question 19: Which of the following best describes the relationship between Azure AD and RBAC?

- Azure AD and RBAC are two separate identity and access management solutions.
- Azure AD is a prerequisite for RBAC, and RBAC relies on Azure AD for user authentication. (Incorrect)
- Azure AD and RBAC are both built into the Azure portal and are used interchangeably.
- Azure AD and RBAC provide complementary functionality for managing access to Azure resources. (Correct)

The correct option is : Azure AD and RBAC provide complementary functionality for managing access to Azure resources.

#### Question 20: A startup is looking to deploy a tool that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. Which of the following would you recommend?

- A Resource Group
- A Hub
- A Router
- A Firewall (Correct)
- A Gateway
- A Filter

A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. You can create firewall rules that specify ranges of IP addresses. Only clients granted IP addresses from within those ranges are allowed to access the destination server. Firewall rules can also include specific network protocol and port information. What's Azure Firewall? [Azure Firewall](https://azure.microsoft.com/services/azure-firewall) is a managed, cloud-based network security service that helps protect resources in your Azure virtual networks. A virtual network is similar to a traditional network that you'd operate in your own datacenter. It's a fundamental building block for your private network that enables virtual machines and other compute resources to securely communicate with each other, the internet, and on-premises networks.

#### Question 21: An Insurance company is planning to migrate sensitive client records to Azure. They are concerned about the security of their data during the transfer process. They have decided to use Azure Data Box for this migration. Which of the following security features can they rely on to ensure their data remains secure during the transfer process?

- Data-at-rest encryption (Correct)
- Multi-factor authentication (Incorrect)
- Tamper-resistant storage (Correct)
- Firewall protection

Azure Data Box offers several security features to protect data during the transfer process, including data-at-rest encryption and tamper-resistant storage. Data-at-rest encryption ensures that data is encrypted while it is being stored on the Data Box device. Tamper-resistant storage is designed to help protect against unauthorized access or tampering during the transit.

#### Question 22: Which of the following Azure AD features allows users to use their existing corporate credentials to sign in to cloud-based applications?

- Azure AD Connect
- Azure AD B2C (Correct)
- Azure AD Domain Services
- Azure AD B2B (Incorrect)

The correct option is - Azure AD B2C. It allows users to use their existing corporate credentials, social accounts, or local accounts to sign in to cloud-based applications.
Azure AD B2B, enables collaboration between users in different organizations by allowing external users to access resources in a partner organization's Azure AD.

#### Question 23: Your __________________ is your organization's ability to protect from and respond to security threats.

- security posture (Correct)
- security standard
- security response
- security blueprint

Your _security posture_ is your organization's ability to protect from and respond to security threats. The common principles used to define a security posture are confidentiality, integrity, and availability, known collectively as CIA.

#### Question 25: Which Azure service allows you to provide a self-service sign-up experience for customers accessing your application?

- Azure Active Directory Domain Services
- Azure Multi-Factor Authentication
- Azure B2B Collaboration
- Azure Active Directory B2C (Correct)

Azure Active Directory B2C (Business-to-Customer) is designed to handle customer identities and provides a self-service sign-up experience. It enables organizations to customize and control how customers sign up, sign in, and manage their profiles when accessing applications.

#### Question 26: What is the primary benefit of using private endpoints for connecting to Azure services?

- Faster network performance compared to public endpoints.
- Improved security by bypassing the public internet. (Correct)
- Reduced cost for outbound data transfer.
- Compatibility with legacy protocols.

One of the primary benefits of using private endpoints is improved security. By utilizing private endpoints, you can establish a direct connection to Azure services from within your virtual network, bypassing the public internet. This helps in reducing the exposure of your resources to potential security risks associated with public internet traffic.

#### Question 27: Which of the following are like a physical disk in an on-premises server but, virtualized?

- Azure SQL Databases
- Azure Virtual Machines
- Azure Tapes
- Azure Blobs
- Azure Managed Disks (Correct)

 Azure managed disks are block-level storage volumes that are managed by Azure and used with Azure Virtual Machines. Managed disks are like a physical disk in an on-premises server but, virtualized. With managed disks, all you have to do is specify the disk size, the disk type, and provision the disk. Once you provision the disk, Azure handles the rest.

#### Question 28: A large organization plans to migrate all their On-Prem Virtual Machines to an Azure pay-as-you-go subscription. Which of the following expenditure models would this migration follow?

- Capital
- Elastic 
- Operational (Correct)
- Scalable

#### Question 29: If you want to keep tabs on Azure itself, especially the services and regions you depend on, you should to choose __________________.

- Azure Advisor
- Azure Service Health (Correct)
- Azure Arc
- Azure Monitor

 
If you want to keep tabs on Azure itself, especially the services and regions you depend on, you want to choose Azure Service Health. You can view the current status of the Azure services you rely on, upcoming planned outages, and services that will be sunset. You can set up alerts that help you stay on top of incidents and upcoming downtime without having to visit the dashboard regularly.

#### Question 30: The Azure Data Box family provides a range of physical devices and a virtual device to help customers with their offline and online data transfer needs, respectively called Data Box, Data Box Disk, Data Box Heavy, and Data Box ________.

- Corner
- Ultra
- Node
- Edge (Correct)

The correct answer is "Edge". The full list of Azure Data Box devices is: Data Box, Data Box Disk, Data Box Heavy, Data Box Edge. 

#### Question 31: Which of the following can be leveraged for transferring data to the cloud such as cloud archival, disaster recovery, or if there is a need to process your data at cloud scale?

- Azure File Sync
- Azure Data Lake Storage Gen2 (Incorrect)
- Azure CosmosDB
- Azure Sentinel
- Azure Data Box Gateway (Correct)
- Azure Arc

 
Azure Data Box Gateway is a storage solution that enables you to seamlessly send data to Azure. This article provides you an overview of the Azure Data Box Gateway solution, benefits, key capabilities, and the scenarios where you can deploy this device. Data Box Gateway is a virtual device based on a virtual machine provisioned in your virtualized environment or hypervisor. The virtual device resides in your premises and you write data to it using the NFS and SMB protocols. The device then transfers your data to Azure block blob, page blob, or Azure Files.

Use cases:  Data Box Gateway can be leveraged for transferring data to the cloud such as cloud archival, disaster recovery, or if there is a need to process your data at cloud scale. Here are the various scenarios where Data Box Gateway can be used for data transfer.

- Cloud archival - Copy hundreds of TBs of data to Azure storage using Data Box Gateway in a secure and efficient manner. The data can be ingested one time or an ongoing basis for archival scenarios.

- Continuous data ingestion - Continuously ingest data into the device to copy to the cloud, regardless of the data size. As the data is written to the gateway device, the device uploads the data to Azure Storage.

- Initial bulk transfer followed by incremental transfer - Use Data Box for the bulk transfer in an offline mode (initial seed) and Data Box Gateway for incremental transfers (ongoing feed) over the network.

#### Question 32: How does Microsoft Purview contribute to data collaboration within an organization?

- It offers a cloud-based file sharing and storage solution.
- It provides tools to discover and share trusted data sources across teams. (Correct)
- It facilitates secure communication between on-premises servers and Azure services.
- It enables real-time communication between virtual machines.

Microsoft Purview provides a unified data governance solution to help manage and govern your on-premises, multicloud, and software as a service (SaaS) data. Microsoft Purview enables data collaboration by providing tools for discovering and sharing trusted data sources across different teams and departments. It helps improve data accessibility and collaboration while maintaining governance and security.

#### Question 33: You can link virtual networks together by using virtual network __________________._

- cloning
- connectivity
- seeding
- peering (Correct)

#### Question 34: Upon creating a new Virtual Machine in Azure, will you be billed separately for its local disk storage?

- No 
- Yes
 
All new virtual machines have an operating system disk and a local disk (or “resource disk”). Azure doesn't charge for local disk storage. The operating system disk is charged at the standard rate for disks. [See all virtual machine configurations](https://docs.microsoft.com/en-gb/azure/cloud-services/cloud-services-sizes-specs).

#### Question 35: Correct

How does Azure Arc enable governance across hybrid environments?

- By enforcing limitations on network connectivity both on-premises and in a multi-cloud environment. 
- By extending Azure Policy and Blueprints to on-premises and multi-cloud environments.(Correct)
- By providing exclusive access to on-premises resources and extra security through NSGs.
- By restricting all management operations to Azure regions only.

#### Question 36: Your organization has decided to migrate a large amount of on-premises data to Azure Blob Storage. Due to bandwidth limitations and a strict migration timeline, you are considering using Azure Data Box to expedite the process. Which of the following factors should you take into account when choosing the appropriate Data Box device for your migration?

- The type of data you are transferring
- Your available network bandwidth
- Your organization's budget for the migration
- The total amount of data you need to transfer(Correct)

The correct answer is : The total amount of data you need to transfer.

#### Question 37: Yes or No: A company can extend a private cloud by adding its own physical servers to the public cloud.

- No (Correct)
- Yes

You cannot add physical servers to the public cloud. You can only deploy virtual servers in the public cloud. You can extend a private cloud by deploying virtual servers in a public cloud. This would create a hybrid cloud.

#### Question 38: Which cloud benefit allows you to rapidly deploy applications or systems across multiple regions or locations?

- Elasticity
- Geographic distribution (Correct)
- Scalability
- Fault tolerance

One of the major benefits of cloud computing is the ability to quickly and easily deploy applications or systems across multiple regions or locations. This is often referred to as geographic distribution, and it allows organizations to better serve customers in different regions by providing faster response times and reduced latency.

#### Question 39: Yes or No:

When you apply a lock at a parent scope, all resources within that scope inherit the same lock. Even resources you add later inherit the same parent lock. The most unrestrictive lock in the inheritance takes precedence.

- No

(Correct)

- Yes

 

As an administrator, you can lock an Azure subscription, resource group, or resource to protect them from accidental user deletions and modifications. The lock overrides any user permissions.

 

When you apply a lock at a parent scope, all resources within that scope inherit the same lock. Even resources you add later inherit the same parent lock. The most restrictive lock in the inheritance takes precedence.

If you have a Delete lock on a resource and attempt to delete its resource group, the feature blocks the whole delete operation. Even if the resource group or other resources in the resource group are unlocked, the deletion doesn't happen. You never have a partial deletion.

 

When you [cancel an Azure subscription](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/cancel-azure-subscription#what-happens-after-subscription-cancellation):

 

- A resource lock doesn't block the subscription cancellation.

- Azure preserves your resources by deactivating them instead of immediately deleting them.

- Azure only deletes your resources permanently after a waiting period.

 

Reference: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources?tabs=json)

#### Question 40: Incorrect

True or False: Private endpoints provide secure access to Azure resources over the public internet.

- True

(Incorrect)

- False

(Correct)

This statement is false. Private endpoints provide secure access to Azure resources, but they do so without using the public internet. Private endpoints allow resources to be accessed privately through the Azure backbone network, enhancing security by avoiding exposure to the public internet.

 

Reference: [https://learn.microsoft.com/en-us/azure/private-link/private-link-overview](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)

#### Question 41: Correct

What is the key advantage of using ARM templates for resource deployment?

- They provide direct access to Azure data centers and are hence faster.

- They eliminate the need for Azure subscriptions.

- They ensure consistent and repeatable resource deployments.

(Correct)

- They allow you to deploy resources manually.

ARM templates enable consistent and repeatable deployments by defining the desired state of resources in a declarative manner. This reduces manual errors and ensures a predictable environment.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

#### Question 42: Correct

You have to run business critical workloads using Azure Virtual Machines, SQL Databases, Data Explorer, and Blob Storage for the next 3 years. Which of the following would provide the MOST cost savings?

- By Purchasing Reservations

(Correct)

- By using Resources judiciously

- Stopping the Virtual Machines every night

- Using a Pay-As-You-Go subscription

 

Azure Reservations help you save money by committing to one-year or three-year plans for multiple products. Committing allows you to get a discount on the resources you use. Reservations can significantly reduce your resource costs by up to 72% from pay-as-you-go prices. Reservations provide a billing discount and don't affect the runtime state of your resources. After you purchase a reservation, the discount automatically applies to matching resources.

You can pay for a reservation up front or monthly. The total cost of up-front and monthly reservations is the same and you don't pay any extra fees when you choose to pay monthly. Monthly payment is available for Azure reservations, not third-party products.

 

Why buy a reservation?

 

If you have consistent resource usage that supports reservations, buying a reservation gives you the option to reduce your costs. For example, when you continuously run instances of a service without a reservation, you're charged at pay-as-you-go rates. When you buy a reservation, you immediately get the reservation discount. The resources are no longer charged at the pay-as-you-go rates.

 

Reference: [https://docs.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations](https://docs.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)

#### Question 43: Correct

Which of the following can you use to track resource usage and manage costs across all of your clouds with a single, unified view?

- Azure Pricing Calculator

- Azure Trust Center

- Azure Cost Management + Billing

(Correct)

- Azure Monitor

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-26_04-31-51-626a8cf434f0e0495b3dbe6ba2405417.png)

The following depicts the single unified view to track resource usage as well as manage costs.

![](https://img-c.udemycdn.com/redactor/raw/2020-05-26_04-32-17-a0f99d1280011d741e8b2b48eccda230.png)

 

Reference : [https://azure.microsoft.com/en-gb/services/cost-management/#overview](https://azure.microsoft.com/en-gb/services/cost-management/#overview)

#### Question 44: Correct

Which of the following does not affect a storage account billing?

- Redundancy

- Account  Type

- Region

- Data Ingress within the same AZ

(Correct)

- Data Egress outside a region

- Access Tier

 

An Azure storage account contains all of your Azure Storage data objects, including blobs, file shares, queues, tables, and disks. The storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in your storage account is durable and highly available, secure, and massively scalable.

 

Azure Storage bills based on your storage account usage. All objects in a storage account are billed together as a group. Storage costs are calculated according to the following factors:

 

- Region refers to the geographical region in which your account is based.

- Account type refers to the type of storage account you're using.

- Access tier refers to the data usage pattern you’ve specified for your general-purpose v2 or Blob Storage account.

- Capacity refers to how much of your storage account allotment you're using to store data.

- Redundancy determines how many copies of your data are maintained at one time, and in what locations.

- Transactions refer to all read and write operations to Azure Storage.

- Data egress refers to any data transferred out of an Azure region. When the data in your storage account is accessed by an application that isn’t running in the same region, you're charged for data egress. For information about using resource groups to group your data and services in the same region to limit egress charges, see [What is an Azure resource group?](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group).

The [Azure Storage pricing page](https://azure.microsoft.com/pricing/details/storage) provides detailed pricing information based on account type, storage capacity, replication, and transactions. The [Data Transfers pricing details](https://azure.microsoft.com/pricing/details/data-transfers) provides detailed pricing information for data egress. You can use the [Azure Storage pricing calculator](https://azure.microsoft.com/pricing/calculator/?scenario=data-management) to help estimate your costs.

 

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview)

#### Question 45: Correct

True or False:

 

The Basic service tier is automatically enabled for free as part of your Azure subscription.

- Yes

(Correct)

- No

This is True, the basic Tier is activated and provided as part of your Azure Subscription!

#### Question 46: Correct

Which of the following is the most flexible category of cloud services?

- Platform as a Service (PaaS)

- Infrastructure as a Service (IaaS)

(Correct)

- Software as a Service (SaaS)

 

IaaS is the most flexible category of cloud services. It aims to give you complete control over the hardware that runs your application. Instead of buying hardware, with IaaS, you rent it.

 

![](https://docs.microsoft.com/en-ca/learn/azure-fundamentals/fundamental-azure-concepts/media/iaas-paas-saas-575a09e9.png)

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/fundamental-azure-concepts/categories-of-cloud-services](https://docs.microsoft.com/en-ca/learn/modules/fundamental-azure-concepts/categories-of-cloud-services)

#### Question 47: Correct

Your company wants to copy blobs or files to or from a storage account and is looking for a command-line utility to accomplish this. Which of the following is the right choice?

- Azure FileSync

- Azure AzCopy

(Correct)

- Azure PowerShell

- Azure Storage Explorer

- Azure Bash

 

AzCopy is a command-line utility that you can use to copy blobs or files to or from a storage account.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

#### Question 48: Correct

A company wants to deploy a set of Azure Virtual Machines and wants to understand their pricing. Which 2 of the following affect Virtual Machine (VM) costs in Azure?

- The Data Center the VM resides in

- The Region the Virtual Machine is located in

(Correct)

- The Resource group the VM belongs to

- The Scale Set the VM belongs to

- The Virtual Network the VM belongs to

- The Size of the Virtual Machine (VM)

(Correct)

- The branding of the VM

From the Azure Pricing Calculator, we can see that:

 

![](https://img-c.udemycdn.com/redactor/raw/2020-08-12_18-11-00-3787eae036b4ef3246a3d001d23aade3.png)

 

Region and Instance size affects Virtual Machine costs!

 

Reference: [https://azure.microsoft.com/en-us/pricing/calculator/](https://azure.microsoft.com/en-us/pricing/calculator/)

#### Question 49: Correct

A startup has deployed a set of Virtual Machines which are critical for their day-to-day operations. They need to ensure their availability even if a single data center goes down. An intern has suggested that deploying the virtual machines to two or more scale sets will solve the problem.

 

Is this suggestion correct?

- No

(Correct)

- Yes

This answer does not specify that the scale set will be configured across multiple data centers so this solution does not meet the goal. For this #### Question, deploying the VMs to multiple data centers / availability zones would make more sense.

 

 

Azure virtual machine scale sets let you create and manage a group of load balanced VMs. The number of VM instances can automatically increase or decrease in response to demand or a defined schedule. Scale sets provide high availability to your applications, and allow you to centrally manage, configure, and update many VMs.

 

Virtual machines in a scale set can be deployed across multiple update domains and fault domains to maximize availability and resilience to outages due to data center outages, and planned or unplanned maintenance events.

 

Reference: [https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/availability)

#### Question 50: Correct

Your Cloud Security team is looking to block any access from untrusted sources, such as access from unknown or unexpected locations. Which of the following can they use?

- Policies

- Conditional Access

(Correct)

- Blueprints

- Resource Locks

- Multifactor Authentication

 

Conditional Access is a tool that Azure Active Directory uses to allow (or deny) access to resources based on identity signals. These signals include who the user is, where the user is, and what device the user is requesting access from.

 

Conditional Access is useful when you need to:

 

- Require multifactor authentication to access an application.

You can configure whether all users require multifactor authentication or only certain users, such as administrators.

You can also configure whether multifactor authentication applies to access from all networks or only untrusted networks.

- Require access to services only through approved client applications.

For example, you might want to allow users to access Office 365 services from a mobile device as long as they use approved client apps, like the Outlook mobile app.

- Require users to access your application only from managed devices.

A managed device is a device that meets your standards for security and compliance.

- Block access from untrusted sources, such as access from unknown or unexpected locations.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/secure-access-azure-identity-services/4-what-are-mfa-conditional-access](https://docs.microsoft.com/en-ca/learn/modules/secure-access-azure-identity-services/4-what-are-mfa-conditional-access)

#### Question 51: Correct

Which of the following Azure plans should you choose for Trial and non-production environments?

- Standard

- Developer

(Correct)

- Professional Direct

- Premier

From the official documentation:

 

![](https://img-c.udemycdn.com/redactor/raw/2020-08-12_17-44-56-c7f65aa3d2609bbfa57930ff769d87ff.png)

 

Reference: [https://azure.microsoft.com/en-in/pricing/#product-pricing](https://azure.microsoft.com/en-in/pricing/#product-pricing)

#### Question 52: Correct

Data that is stored in the Archive access tier of an Azure Storage account ________________.

- must be recovered before the data can be accessed

- can only be read by using Azure Instant Access

- must be rehydrated before the data can be accessed

(Correct)

- must be requested from Azure by calling the helpline.

 

Azure storage offers different access tiers: hot, cool and archive.

 

The archive access tier has the lowest storage cost. But it has higher data retrieval costs compared to the hot and cool tiers. Data in the archive tier can take several hours to retrieve.

 

While a blob is in archive storage, the blob data is offline and can't be read, overwritten, or modified. To read or download a blob in archive, you must first rehydrate it to an online tier.

 

Example usage scenarios for the archive access tier include: Long-term backup, secondary backup, and archival datasets

 

Original (raw) data that must be preserved, even after it has been processed into final usable form.

 

Compliance and archival data that needs to be stored for a long time and is hardly ever accessed.

 

References: [https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-storage-tiers?tabs=azure-portal#archive-access-tier](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-storage-tiers?tabs=azure-portal#archive-access-tier)

#### Question 53: Correct

When a company thinks of migrating to the public cloud (like Azure), which of the following expense gets reduced?

- Primary Expense

- Operational Expense

- Capital Expense

(Correct)

- Secondary Expense

Migrating to the public cloud saves a lot of Capex upfront and one of the biggest advantages is the ability to Pay as you go!

#### Question 54: Incorrect

Which of the following is not a valid way to connect your on-premise data center to Azure?

- Site-to-site virtual private networks

- Azure ExpressRoute

- Point-to-site virtual private networks

(Incorrect)

- Network virtual appliances

(Correct)

 

Azure virtual networks enable you to filter traffic between subnets by using the following approaches:

 

- Network security groups A network security group is an Azure resource that can contain multiple inbound and outbound security rules. You can define these rules to allow or block traffic, based on factors such as source and destination IP address, port, and protocol.

- Network virtual appliances A network virtual appliance is a specialized VM that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing wide area network (WAN) optimization.

 

Azure virtual networks enable you to link resources together in your on-premises environment and within your Azure subscription. In effect, you can create a network that spans both your local and cloud environments. There are three mechanisms for you to achieve this connectivity:

 

- Point-to-site virtual private networks The typical approach to a virtual private network (VPN) connection is from a computer outside your organization, back into your corporate network. In this case, the client computer initiates an encrypted VPN connection to connect that computer to the Azure virtual network.

- Site-to-site virtual private networks A site-to-site VPN links your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network. In effect, the devices in Azure can appear as being on the local network. The connection is encrypted and works over the internet.

- Azure ExpressRoute For environments where you need greater bandwidth and even higher levels of security, Azure ExpressRoute is the best approach. ExpressRoute provides a dedicated private connectivity to Azure that doesn't travel over the internet.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-networking-fundamentals/azure-virtual-network-fundamentals](https://docs.microsoft.com/en-ca/learn/modules/azure-networking-fundamentals/azure-virtual-network-fundamentals)

#### Question 55: Correct

Which cloud benefit ensures that a system or application can continue to operate without disruption in the event of a failure?

- Elasticity

- Fault tolerance

(Correct)

- High availability

- Scalability

The correct answer is Fault tolerance.

 

Fault tolerance refers to the ability of a system or application to continue operating without disruption in the event of a failure. This is achieved through redundancy and failover mechanisms that ensure that if one component fails, another component takes over seamlessly, without any downtime or interruption of service.

 

Scalability refers to the ability to increase or decrease resources as needed to meet changing demands, while elasticity refers to the ability to dynamically provision and de-provision resources based on demand.

 

High availability refers to the ability of a system or application to remain operational and accessible for a high percentage of time, typically measured as a percentage of uptime over a given period.

 

Reference: [https://azure.microsoft.com/en-us/overview/what-is-cloud-computing/](https://azure.microsoft.com/en-us/overview/what-is-cloud-computing/)

#### Question 56: Correct

You have a workload in Blob Storage that processes large datasets that need to be stored in a cost-effective way, while additional data is being gathered for processing. Which of the following Access Tiers would make the most sense?

- Archive

- Hot

- Luke Warm

- Efficient

- Cool

(Correct)

The keyword here is 'cost-effective'.

 

 

When your data is stored in an online access tier (either Hot or Cool), users can access it immediately. The Hot tier is the best choice for data that is in active use, while the Cool tier is ideal for data that is accessed less frequently, but that still must be available for reading and writing.

 

Example usage scenarios for the Hot tier include:

 

- Data that's in active use or is expected to be read from and written to frequently.

- Data that's staged for processing and eventual migration to the Cool access tier.

Usage scenarios for the Cool access tier include:

 

- Short-term data backup and disaster recovery.

- Older data sets that aren't used frequently, but are expected to be available for immediate access.

- Large data sets that need to be stored in a cost-effective way while additional data is being gathered for processing.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview](https://docs.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)

#### Question 57: Correct

Yes or No:

 

All data that is copied to an Azure storage account is backed up automatically to another Azure data center.

- No

(Correct)

- Yes

Automatically is the key word in this #### Question that most people miss.

 

Data is not backed up automatically to another Azure Data Center, although it can be backed up depending on the replication option configured for the account. Locally Redundant Storage (LRS) is the default which maintains three copies of the data in the data center.

Geo-redundant storage (GRS) has cross-regional replication to protect against regional outages. Data is replicated synchronously three times in the primary region, then replicated asynchronously to the secondary region.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview)

#### Question 58: Correct

Which of the following can you use to calculate your estimated hourly or monthly costs for using Azure?

- Azure Pricing Calculator

(Correct)

- Azure Cost Management

- Azure Advisor

- Azure Billing

- Azure TCO Calculator

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-26_05-16-39-89fde434af3953cf9064a89becb1e3e7.png)

 

Disclaimer : Prices are estimates and are not intended as actual price quotes. Actual prices may vary depending on the date of purchase, currency of payment and type of agreement that you enter into with Microsoft. Contact a Microsoft sales representative for additional information on pricing.

 

Reference : [https://azure.microsoft.com/en-gb/pricing/calculator/](https://azure.microsoft.com/en-gb/pricing/#product-pricing)

#### Question 59: Correct

What is the benefit of utilizing Microsoft Purview for regulatory compliance?

- It automatically generates reports for financial audits.

- It provides a compliance score for Azure subscriptions.

- It integrates with external cloud providers for data storage.

- It helps classify and manage data to meet regulatory requirements.

(Correct)

Microsoft Purview helps organizations classify and manage data according to regulatory requirements. It allows data to be categorized based on sensitivity, helping organizations comply with data protection regulations and policies.

 

Reference: [https://azure.microsoft.com/en-ca/products/purview](https://azure.microsoft.com/en-ca/products/purview)

#### Question 60: Correct

Your company plans to migrate all on-premises data to Azure.

 

However, before this, the legal department has asked you to fetch all information such as Audit and Compliance Reports to identify whether Azure complies with the company's regional requirements.

 

Which of the following can help with this?

- The Knowledge Center

- Azure Marketplace

- The Trust Center

(Correct)

- The Azure portal

You can use the Trust Center to check the Audit and Compliance requirements (compliance manager).

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-02_21-22-16-e66a385704cb045b3ac7303d2d2ec46f.png)![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-02_21-22-16-804efb741cb5f44fc3c7fe50cb2462e7.png)![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-02_21-22-16-89334a2972258af649786b8c98364def.png)![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-02_21-22-16-5776ae538ee8518ebd7e26061cf19e08.png)![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-02_21-22-16-235e4df244eb2314c2f1a1939c8bc1ce.png)

Reference: [https://servicetrust.microsoft.com/](https://servicetrust.microsoft.com/)

#### Question 61: Correct

What does Microsoft Purview offer to assist organizations with data lineage and impact analysis?

- Built-in ETL (Extract, Transform, Load) capabilities for data integration.

- Integrated machine learning models for predictive analytics.

- Tools for visualizing data flow and understanding its origins and dependencies.

(Correct)

- Real-time data replication between Azure regions.

Microsoft Purview provides a unified data governance solution to help manage and govern your on-premises, multicloud, and software as a service (SaaS) data. Microsoft Purview provides tools for visualizing data lineage, allowing organizations to track the flow of data, understand its origins, and analyze its dependencies. This helps in performing impact analysis and ensuring data quality.

 

Reference: [https://azure.microsoft.com/en-ca/products/purview](https://azure.microsoft.com/en-ca/products/purview)

#### Question 62: Correct

What is an ARM template used for?

- To declare the desired state of Azure resources and their dependencies.

(Correct)

- To provide user authentication for Azure services.

- To configure Azure Active Directory settings.

- To define the schema for Azure Storage.

An ARM template is a JSON file that defines the desired state of Azure resources, including their configuration, dependencies, and relationships. It allows you to automate resource provisioning.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

#### Question 63: Correct

_________________ enables large-scale parallel and high-performance computing (HPC) batch jobs with the ability to scale to tens, hundreds, or thousands of VMs.

- Azure Batch

(Correct)

- Azure Kubernetes

- Azure Virtual Machines

- Azure Parallel

- Azure Container Instances

 

Azure Batch enables large-scale parallel and high-performance computing (HPC) batch jobs with the ability to scale to tens, hundreds, or thousands of VMs.

 

When you're ready to run a job, Batch does the following:

 

- Starts a pool of compute VMs for you.

- Installs applications and staging data.

- Runs jobs with as many tasks as you have.

- Identifies failures.

- Requeues work.

- Scales down the pool as work completes.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-virtual-machines](https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-virtual-machines)

#### Question 64: Correct

True or False: Azure Data Box can be used to transfer data from Azure to on-premises data centers or other cloud providers.

- True

(Correct)

- False

Yes, Azure Data Box can be used to transfer data from Azure to other cloud providers. This can be useful when customers need to move data between different cloud providers or from on-premises data centers to cloud providers other than Azure.

 

Reference: [https://learn.microsoft.com/en-us/azure/databox/data-box-overview#use-cases](https://learn.microsoft.com/en-us/azure/databox/data-box-overview#use-cases)

#### Question 65: Correct

Select the valid options to pay for Azure? ( Choose 3 )

- Microsoft Representative

(Correct)

- Microsoft Stores

- Azure Partner

(Correct)

- Any 3rd Party Vendor

- Azure Website

(Correct)

- Xbox Website

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-26_05-19-59-ebb5a052ef4317b848dbfc8a491ca0ff.png)

 

Reference : [https://azure.microsoft.com/en-gb/pricing/#product-pricing](https://azure.microsoft.com/en-gb/pricing/#product-pricing)

#### Question 66: Incorrect

______________ enables centralizing your organization's file shares in Azure Files, while keeping the flexibility, performance, and compatibility of a Windows file server.

- Azure Data Box Gateway

- Azure Arc

- Azure File Manager

(Incorrect)

- Azure File Sync

(Correct)

- Azure Resource Manager

 

Azure File Sync enables centralizing your organization's file shares in Azure Files, while keeping the flexibility, performance, and compatibility of a Windows file server. While some users may opt to keep a full copy of their data locally, Azure File Sync additionally has the ability to transform Windows Server into a quick cache of your Azure file share. You can use any protocol that's available on Windows Server to access your data locally, including SMB, NFS, and FTPS. You can have as many caches as you need across the world.

 

Azure file shares can be used in two ways: by directly mounting these serverless Azure file shares (SMB) or by caching Azure file shares on-premises using Azure File Sync. Which deployment option you choose changes the aspects you need to consider as you plan for your deployment.

 

- Direct mount of an Azure file share: Since Azure Files provides SMB access, you can mount Azure file shares on-premises or in the cloud using the standard SMB client available in Windows, macOS, and Linux. Because Azure file shares are serverless, deploying for production scenarios does not require managing a file server or NAS device. This means you don't have to apply software patches or swap out physical disks.

- Cache Azure file share on-premises with Azure File Sync: Azure File Sync enables you to centralize your organization's file shares in Azure Files, while keeping the flexibility, performance, and compatibility of an on-premises file server. Azure File Sync transforms an on-premises (or cloud) Windows Server into a quick cache of your Azure file share.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction](https://docs.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction)

[https://docs.microsoft.com/en-us/azure/storage/file-sync/file-sync-planning](https://docs.microsoft.com/en-us/azure/storage/file-sync/file-sync-planning)

#### Question 67: Correct

Which of the following is a private connection from your on-premises infrastructure to your Azure infrastructure wherein the data does not travel through the internet?

- Azure ExpressRoute

(Correct)

- Azure DNS

- Azure Arc

- Azure VPN Gateway

 

With ExpressRoute, your data doesn't travel over the public internet, so it's not exposed to the potential risks associated with internet communications. ExpressRoute is a private connection from your on-premises infrastructure to your Azure infrastructure. However, even if you have an ExpressRoute connection, DNS queries, certificate revocation list checking, and Azure Content Delivery Network requests are still sent over the public internet.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-networking-fundamentals/express-route-fundamentals](https://docs.microsoft.com/en-ca/learn/modules/azure-networking-fundamentals/express-route-fundamentals)

#### Question 68: Incorrect

__________________ are often used to create solutions by using a microservice architecture. This architecture is where you break solutions into smaller, independent pieces.

- Functions

- Modules

(Incorrect)

- Containers

(Correct)

- Kubernetes

 

Containers are often used to create solutions by using a _microservice architecture_. This architecture is where you break solutions into smaller, independent pieces. For example, you might split a website into a container hosting your front end, another hosting your back end, and a third for storage. This split allows you to separate portions of your app into logical sections that can be maintained, scaled, or updated independently.

 

Imagine your website back-end has reached capacity but the front end and storage aren't being stressed. You could:

 

- Scale the back end separately to improve performance.

- Decide to use a different storage service.

- Replace the storage container without affecting the rest of the application.

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-container-services](https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-container-services)

#### Question 69: Correct

You are migrating an application with multiple interconnected servers to Azure. To ensure minimal downtime and a smooth migration, which Azure Migrate features should you utilize?

- Azure Migrate - Database Assessment and Azure Migrate - Database Migration

- Azure Migrate - Server Assessment and Azure Migrate - Server Migration

(Correct)

- Azure Migrate - App Service and Azure Migrate - Web App Migration

- Azure Migrate - Data Box and Azure Migrate - Data Factory

The correct answer is : Azure Migrate - Server Assessment and Azure Migrate - Server Migration.

 

Azure Migrate - Server Assessment helps you to evaluate the migration readiness of your on-premises servers, identify any potential issues, and provide recommendations. Azure Migrate - Server Migration is designed to migrate your on-premises virtual machines or physical servers to Azure with minimal downtime. These two features work together to ensure a smooth migration of interconnected servers, as they address both the pre-migration assessment and the actual migration process.

 

Other options:

 

- Azure Migrate - App Service and Azure Migrate Web App Migration  - These are geared towards migrating web applications to Azure App Service and not for migrating interconnected servers.

- Azure Migrate - Database Assessment and Azure Migrate Database Migration - These focus on the assessment and migration of on-premises databases to Azure. They are not intended for migrating interconnected servers.

- Azure Migrate - Data Box and Azure Migrate Data Factory - These are used for transferring large amounts of data to Azure and for data integration, respectively. They do not address the migration of interconnected servers.

Reference: [https://docs.microsoft.com/en-us/azure/migrate/migrate-overview](https://docs.microsoft.com/en-us/azure/migrate/migrate-overview)

#### Question 70: Correct

True or False:

 

There is no programmatic access to the Blob, Queue, Table, and File services in Azure, though you can access VMs using API calls.

- True

- False

(Correct)

 

The REST APIs for the Microsoft Azure storage services offer programmatic access to the Blob, Queue, Table, and File services in Azure or in the development environment via the storage emulator.

All storage services are accessible via REST APIs. Storage services may be accessed from within a service running in Azure, or directly over the Internet from any application that can send an HTTP/HTTPS request and receive an HTTP/HTTPS response.

 

Important:

 

The Azure storage services support both HTTP and HTTPS; however, using HTTPS is highly recommended.

 

Storage Account

All access to storage services takes place through the storage account. The storage account is the highest level of the namespace for accessing each of the fundamental services. It is also the basis for authorization.

The REST APIs for storage services expose the storage account as a resource.

 

Reference: [https://docs.microsoft.com/en-us/rest/api/storageservices/](https://docs.microsoft.com/en-us/rest/api/storageservices/)

#### Question 71: Correct

Which of the following scenarios would be best suited for using Azure Active Directory (AAD) rather than Role-Based Access Control (RBAC)?

- Managing user identities for a cloud-based application.

(Correct)

- Limiting access to specific resource groups within an Azure subscription.

- Managing access to a specific Azure resource for a group of users.

- Providing role-based access control to an Azure Virtual Machine.

The correct answer is : Managing user identities for a cloud-based application.

 

Azure Active Directory (AAD) is a cloud-based identity and access management service that is used to manage user identities and their access to various cloud-based applications and services, including those hosted in Azure. AAD provides a centralized location for managing user accounts, passwords, and access to applications.

In contrast, Role-Based Access Control (RBAC) is used to manage access control for specific Azure resources, including virtual machines, storage accounts, and other Azure services. RBAC provides a way to assign permissions to specific roles rather than individual users, making it easier to manage access control in large environments.

 

Other options -

 

- Managing access to a specific Azure resource for a group of users : This describes a scenario that would be best suited for using RBAC.

 

- Providing role-based access control to an Azure Virtual Machine : This also describes a scenario that would be best suited for using RBAC, as RBAC is used to provide role-based access control to Azure Virtual Machines.

 

- Limiting access to specific resource groups within an Azure subscription: This also describes a scenario that would be best suited for using RBAC, as it involves limiting access to specific resource groups within an Azure subscription.

 

 

Therefore, the correct answer is Managing user identities for a cloud-based application, as Azure Active Directory is best suited for managing user identities for cloud-based applications, whereas RBAC is best suited for managing access control to specific Azure resources.

 

Reference: [https://docs.microsoft.com/en-us/azure/role-based-access-control/overview#understanding-azure-rbac-vs-azure-ad-roles](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview#understanding-azure-rbac-vs-azure-ad-roles)

 

#### Question 72: Correct

You have deployed a new Azure SQL Database in a VNet and want to restrict the ports, as well as allow or deny communication based on the connection state of the flow record.

 

What should you use?

- An Azure DNS Record

- An Azure Active Directory (Azure AD) role

- An Azure Policy

- An Azure Blueprint

- An Azure ExpressRoute

- An Azure Network Security Group (NSG)

(Correct)

Restricting Internet access to your VMs in Azure can be achieved by making use of Azure Network Security Groups.

 

 

We can use an Azure network security group to filter network traffic to and from Azure resources in an Azure virtual network. A network security group contains [security rules](https://docs.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#security-rules) that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources. For each rule, you can specify source and destination, port, and protocol.

 

Reference: [https://docs.microsoft.com/en-us/azure/virtual-network/security-overview](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)

#### Question 73: Correct

Yes or No:

 

To utilize a hybrid cloud model, you must deploy resources to the public cloud while having some resources on-prem.

- Yes

(Correct)

- No

A hybrid cloud is a combination of a private cloud and public cloud. Therefore, to create a hybrid cloud, you must deploy resources to a public cloud.

 

Reference: [https://azure.microsoft.com/en-gb/overview/what-are-private-public-hybrid-clouds/](https://azure.microsoft.com/en-gb/overview/what-are-private-public-hybrid-clouds/)

#### Question 74: Correct

Which of the following would be ideal to store flexible datasets like user data for web applications, address books, device information, or other types of metadata your service requires?

- Azure Queue Storage

- Azure Data Lake Storage Gen1

- Azure SQL Database

- Azure Data Lake Storage Gen2

- Azure File Sync

- Azure Table Storage

(Correct)

 

Azure Table storage is a service that stores non-relational structured data (also known as structured NoSQL data) in the cloud, providing a key/attribute store with a schemaless design. Because Table storage is schemaless, it's easy to adapt your data as the needs of your application evolve. Access to Table storage data is fast and cost-effective for many types of applications, and is typically lower in cost than traditional SQL for similar volumes of data.

You can use Table storage to store flexible datasets like user data for web applications, address books, device information, or other types of metadata your service requires. You can store any number of entities in a table, and a storage account may contain any number of tables, up to the capacity limit of the storage account.

 

Table storage contains the following components:

 

![](https://docs.microsoft.com/en-us/azure/includes/media/storage-table-concepts-include/table1.png)

 

Note: The Cosmos DB Table API offers higher performance and availability, global distribution, and automatic secondary indexes. It is also available in a consumption-based [serverless](https://docs.microsoft.com/en-us/azure/cosmos-db/serverless)mode. There are some [feature differences](https://docs.microsoft.com/en-us/azure/cosmos-db/table/introduction) between Table API in Azure Cosmos DB and Azure table storage. For more information, see [Azure Cosmos DB Table API](https://docs.microsoft.com/en-us/azure/cosmos-db/table-introduction)

 

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/tables/table-storage-overview](https://docs.microsoft.com/en-us/azure/storage/tables/table-storage-overview)

#### Question 75: Correct

You have multiple offices with file servers that need to access and share the same files. Which Azure service would be the most suitable to achieve this while minimizing latency and maintaining a central copy of the data?

- Azure Storage Service Encryption

- Azure Blob Storage

- Azure Data Lake Storage

- Azure File Sync

(Correct)

The correct answer is Azure File Sync. It is the most suitable service for this scenario as it allows you to synchronize files between on-premises file servers and Azure Files. This enables multiple offices with file servers to access and share the same files while minimizing latency by using a local cache. Additionally, it maintains a central copy of the data in Azure Files, which can be accessed and managed centrally.

 

Other options -

 

- Azure Blob Storage is primarily designed for storing unstructured data such as images, videos, and documents. It is not optimized for file sharing and synchronization between multiple offices.

- Azure Storage Service Encryption is a security feature that provides encryption for data stored in Azure Storage, but it does not address file sharing and synchronization between multiple offices.

- Azure Data Lake Storage is designed for big data analytics workloads and is not optimized for file sharing and synchronization between multiple offices.

Reference: [https://docs.microsoft.com/en-us/azure/storage/files/storage-sync-files-planning](https://docs.microsoft.com/en-us/azure/storage/files/storage-sync-files-planning)

#### Question 76: Correct

Which of the following is the correct hierarchy for the Azure levels of scope?

- Subscription --> Resource Group --> Management Group

- Management Group --> Resource Group -->  Subscription

- Resource Group --> Management Group --> Subscription

- Subscription --> Management Group --> Resource Group

- Management Group --> Subscription --> Resource Group

(Correct)

 

Azure provides four levels of scope: management groups, subscriptions, resource groups, and resources. The following image shows an example of these layers. Though not labeled as such, the blue cubes are resources.

 

![](https://docs.microsoft.com/en-ca/learn/wwl-azure/enterprise-governance/media/az500-hierarchy-f8eb3da1.png)

 

You apply management settings at any of these levels of scope. The level you select determines how widely the setting is applied. Lower levels inherit settings from higher levels. For example, when you apply a policy to the subscription, the policy is applied to all resource groups and resources in your subscription. When you apply a policy on the resource group, that policy is applied to the resource group and all its resources. However, another resource group doesn't have that policy assignment.

You can deploy templates to management groups, subscriptions, or resource groups.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/enterprise-governance/4-azure-hierarchy](https://docs.microsoft.com/en-ca/learn/modules/enterprise-governance/4-azure-hierarchy)

#### Question 77: Incorrect

Azure Locks can be set at the ______ level to prevent users from modifying or deleting a resource group or its resources.

- Management Group

(Incorrect)

- Tenant

- Resource

- Subscription

(Correct)

Azure Locks can be set at the subscription level to prevent users from modifying or deleting a resource group or its resources. When an Azure Lock is applied to a resource or resource group, it prevents all users and roles from making any changes to the resource or deleting it.

 

Other Options:

 

- Resource is incorrect because locks can be applied to resources, but it is not the highest level at which a lock can be set. Setting a lock at the resource level would only apply to that specific resource, whereas setting a lock at the subscription level would apply to all resources within the subscription.

- Management Group is incorrect because although locks can be applied at the management group level, this is not the highest level at which a lock can be set. Setting a lock at the management group level would apply to all resources within that management group, but if a resource group is not within that management group, it would not be affected by the lock.

- Tenant is incorrect because locks cannot be set at the tenant level. The highest level at which locks can be set is the subscription level.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

#### Question 78: Correct

Which of the following is a key benefit of using Role-Based Access Control (RBAC) in Azure?

- RBAC allows you to manage user identities and access to cloud resources.

- RBAC allows you to assign permissions to specific roles rather than individual users.

(Correct)

- RBAC provides a centralized directory for managing user accounts and access to resources.

- RBAC provides authentication and authorization services for Azure resources.

The correct option is : RBAC allows you to assign permissions to specific roles rather than individual users.

 

Other options -

 

- RBAC allows you to manage user identities and access to cloud resources: This is incorrect because while RBAC is used for managing access to cloud resources, it specifically provides granular access control by allowing you to assign permissions to specific roles rather than individual users. Manage user identities are the keywords here.

- RBAC provides authentication and authorization services for Azure resources : This is incorrect because RBAC provides authorization services, but not authentication services. Authentication is provided by Azure AD!

- RBAC provides a centralized directory for managing user accounts and access to resources : This is incorrect because while RBAC does provide a centralized management interface for managing access to Azure resources, it specifically allows you to assign permissions to roles rather than manage user accounts. Again, managing user accounts is the keyword here.

 

Reference: [https://learn.microsoft.com/en-us/azure/role-based-access-control/overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

#### Question 79: Correct

Your company is building a mission critical application and wants asynchronous message management for communication between application components, whether they are running in the cloud, on the desktop, on-premises, or on mobile devices. They also expect sudden bursts of requests and are looking to prevent servers from being overwhelmed.

 

Which of the following is the right choice?

- Azure Files

- Azure Queue Storage

(Correct)

- Azure Table Storage

- Azure FileSync

- Azure Data Box Gateway

- Azure Async Manager

 

You can use Azure Queue Storage to build flexible applications and separate functions for better durability across large workloads. When you design applications for scale, application components can be decoupled, so that they can scale independently. Queue storage gives you asynchronous message queueing for communication between application components, whether they are running in the cloud, on the desktop, on-premises, or on mobile devices

 

You can also use Queue Storage to rightsize your service deployment. Applications absorb unexpected traffic bursts, which prevents servers from being overwhelmed by a sudden flood of requests. Monitor queue length to add elasticity to your application, and deploy or hibernate additional worker nodes based on customer demand

 

Reference: [https://azure.microsoft.com/en-ca/services/storage/queues/#features](https://azure.microsoft.com/en-ca/services/storage/queues/#features)

#### Question 80: Correct

What is a key security feature of Azure Data Box devices that ensures data is unreadable if intercepted during the shipping process?

- Data-at-rest encryption

(Correct)

- Firewall protection

- Data transfer over HTTPS

- Multi-factor authentication

The correct answer is : Data-at-rest encryption. This is a key security feature of Azure Data Box devices that ensures data is unreadable if intercepted during the shipping process. Data-at-rest encryption ensures that data is encrypted when it is stored on the device, making it impossible for anyone to access the data without the encryption key. This is an important security measure that protects against data theft or loss during the shipping process.

 

Other options:

 

- Firewall protection: This is incorrect because it refers to a network security measure that protects against unauthorized access to a network, but it is not directly related to the security of data during the shipping process.

- Multi-factor authentication: This is also incorrect because it is a security measure that verifies a user's identity using multiple methods, such as a password and a fingerprint or a security token. This is not directly related to the security of data during the shipping process.

- Data transfer over HTTPS: This is incorrect because it refers to a network protocol that encrypts data during transmission between a web server and a client, but it does not protect data during the shipping process.

 

Reference: [https://docs.microsoft.com/en-us/azure/databox/data-box-security](https://docs.microsoft.com/en-us/azure/databox/data-box-security)

#### Question 81: Correct

True or False: Business-to-Customer (B2C) scenarios in Azure AD are primarily focused on internal employee collaboration.

- True

- False

(Correct)

This statement is false. Business-to-Customer (B2C) scenarios in Azure AD are focused on managing customer identities and providing a tailored sign-up and sign-in experience for external customers using your applications.

 

From the official documentation: Azure AD B2C is a Customer Identity and Access Management (CIAM) solution that lets you build user journeys for consumer- and customer-facing apps. If you're a business or individual developer creating customer-facing apps, you can scale to millions of consumers, customers, or citizens by using Azure AD B2C. Developers can use Azure AD B2C as the full-featured CIAM system for their applications.

With Azure AD B2C, customers can sign in with an identity they've already established (like Facebook or Gmail). You can completely customize and control how customers sign up, sign in, and manage their profiles when using your applications.

 

Reference: [https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview)

#### Question 82: Correct

You can use _________________ to create private connections between Azure datacenters and infrastructure on your premises or in a colocation environment.

- Azure DNS

- Azure ExpressRoute

(Correct)

- Azure Firewall

- Azure Network Security Groups

 

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-03_20-18-37-a9d64e3ced9177952bce3ce6d9c2d798.png)

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-03_20-19-02-f4a66b825fda7d158b38479f478b3a9f.png)

 

Reference: [https://azure.microsoft.com/en-us/services/expressroute/#partners](https://azure.microsoft.com/en-us/services/expressroute/#partners)

#### Question 83: Incorrect

What is the key benefit of using Azure AD B2C for managing customer identities?

- Ability to enforce security policies on internal applications.

- Centralized management of employee identities and access.

- Customizable user experiences for sign-up and sign-in processes.

(Correct)

- Integration with on-premises Active Directory.

(Incorrect)

Azure AD B2C allows you to provide custom user experiences during sign-up and sign-in processes for your applications. This enhances customer engagement and satisfaction by delivering a branded and consistent identity experience.

 

Reference: [https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview)

#### Question 84: Correct

By default, only the ________ can delete or modify an Azure Lock.

- Contributor

- User

- Owner

(Correct)

- Reader

By default, only the owner of an Azure subscription or resource group can delete or modify an Azure Lock. The owner role is the most privileged built-in role in Azure, allowing full access to all resources and management operations within a subscription or resource group.

 

Contributors can perform actions on resources but are not allowed to modify or delete locks. Readers can only view the resources but cannot perform any actions on them. Users is not a built-in role in Azure and therefore is not a valid option.

 

Imp. Note - While Azure Locks can prevent accidental or malicious deletion or modification of resources, they do not prevent users with the appropriate permissions from creating new resources or modifying existing ones.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources)

#### Question 85: Incorrect

Which of the following is not a valid authentication method for Azure AD?

- Certificates  - Passwords

- None of the above

(Correct)

- Biometric authentication

(Incorrect)

The correct answer is - None of the above.

 

Azure AD supports multiple authentication methods for user sign-in, including passwords, certificates, and biometric authentication. Passwords are the most commonly used authentication method and are supported by all Azure AD editions. Certificates can be used for machine authentication and require a client certificate to be installed on the device. Biometric authentication uses unique physical characteristics, such as fingerprints or facial recognition, to authenticate users.

 

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-authentication-methods](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-authentication-methods)

Reference: [https://learn.microsoft.com/en-us/azure/azure-arc/overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

## Test 6 

#### Question 1: Correct

Which type of code/language is commonly used in Infrastructure as Code (IaC) to define and manage resources?

- YAML 

(Correct)

- SQL

- JavaScript

- HTML

YAML (Yet Another Markup Language) is a common choice for writing code to define and manage infrastructure in IaC. It provides a human-readable format for specifying configurations and settings for various resources.

 

Reference: [https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code](https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/infrastructure-as-code)

#### Question 2: Correct

A new startup needs to control its cloud environment so that it complies with several industry standards, but it's not sure where to start. They have existing business requirements, and understand how these requirements relate to their on-premises workloads. These requirements also must be met by any workloads they run in the cloud.

 

Which of the following can help them in this case?

- The Azure Blueprint for Cloud

- The Cloud Adoption Framework for Azure

(Correct)

- The Proven Roadmap for Azure

- Microsoft Defender for Cloud

 

The [Cloud Adoption Framework for Azure](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/) provides you with proven guidance to help with your cloud adoption journey. The Cloud Adoption Framework helps you create and implement the business and technology strategies needed to succeed in the cloud.

 

Cloud Adoption Framework consists of tools, documentation, and proven practices. The Cloud Adoption Framework includes these stages:

 

1. Define your strategy.

2. Make a plan.

3. Ready your organization.

4. Adopt the cloud.

5. Govern and manage your cloud environments.

Reference: [https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/9-accelerate-cloud-adoption-framework](https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/9-accelerate-cloud-adoption-framework)

#### Question 3: Incorrect

Which Azure service allows you to control the DNS settings for private endpoints in your virtual network?

- Azure DNS Zone

- Azure Private DNS 

(Correct)

- Azure Traffic Manager 

- Azure DNS

(Incorrect)

Azure Private DNS is the service that allows you to manage and control the DNS settings for private endpoints in your virtual network. It enables you to map the private endpoint's hostname to its private IP address within the virtual network, ensuring proper resolution.

#### Question 4: Correct

Yes or No:

 

Each Azure subscription can contain multiple account administrators.

- Yes

- No

(Correct)

It is possible to assign multiple administrators to a particular subscription, however there is ONLY 1

account administrator.

 

 

To manage access to Azure resources, you must have the appropriate administrator role. Azure has an authorization system called [Azure role-based access control (Azure RBAC)](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) with several built-in roles you can choose from. You can assign these roles at different scopes, such as management group, subscription, or resource group. By default, the person who creates a new Azure subscription can assign other users administrative access to a subscription (account Admin).

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-04_01-13-55-688855e01b128a07f9cfbda945eeca21.png)![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-04_01-13-55-36312f10ea0a68aafdf03552c5140f19.png)

 

Reference: [https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/add-change-subscription-administrator)

 

#### Question 5: Incorrect

An Azure service is said to be available to all Azure customers when it is in ______________`.`

- general availability

(Incorrect)

- fixed preview

- private preview

- public preview

(Correct)

 

Public preview means that the service is available to everyone with an Azure subscription but the normal SLAs don't apply. This is different from general availability when the service is available to all Azure customers with SLA backed guarantees!

 

Example -

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-04_03-58-59-af7f6d90764acd7a6d81fbf6b3fd689a.png)

Reference: [https://azure.microsoft.com/en-ca/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-ca/support/legal/preview-supplemental-terms/)

#### Question 6: Correct

________________ is Microsoft's cloud-based SIEM system. It uses intelligent security analytics and threat analysis.

- Microsoft Defender for Cloud

- Azure Key Vault

- Azure Arc

- Azure Sentinel

(Correct)

 

Security management on a large scale can benefit from a dedicated security information and event management (SIEM) system. A SIEM system aggregates security data from many different sources (as long as those sources support an open-standard logging format). It also provides capabilities for threat detection and response.

 

[Azure Sentinel](https://azure.microsoft.com/services/azure-sentinel/) is Microsoft's cloud-based SIEM system. It uses intelligent security analytics and threat analysis.

 

Azure Sentinel enables you to:

 

- Collect cloud data at scale Collect data across all users, devices, applications, and infrastructure, both on-premises and from multiple clouds.

- Detect previously undetected threats Minimize false positives by using Microsoft's comprehensive analytics and threat intelligence.

- Investigate threats with artificial intelligence Examine suspicious activities at scale, tapping into years of cybersecurity experience from Microsoft.

- Respond to incidents rapidly Use built-in orchestration and automation of common tasks.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/protect-against-security-threats-azure/3-detect-respond-threats-sentinel](https://docs.microsoft.com/en-ca/learn/modules/protect-against-security-threats-azure/3-detect-respond-threats-sentinel)

#### Question 7: Correct

Which feature of Azure AD External Identities enables customers to sign up, sign in, and manage their own profiles using social accounts?

- Azure Multi-Factor Authentication

- Azure Active Directory B2C

(Correct)

- Azure Active Directory Domain Services

- Azure B2B Collaboration

Azure Active Directory B2C is designed to handle customer identities and enables them to sign up, sign in, and manage their profiles using social accounts or other identity providers, enhancing their experience with your applications.

 

Reference: [https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview)

#### Question 8: Incorrect

Which of the following can an application retrieve security tokens from? Choose the Best possible answer.

- An Azure SQL Database

- An Azure Key Vault

(Incorrect)

- Azure Active Directory (Azure AD)

(Correct)

- A Certificate Store

Please note that the #### Question asks us "To retrieve security tokens". You might be thinking about Azure Key Vaults here.

 

A service such as Azure Key Vault can keep security token, however to access/retrieve something from the Key Vault , we need to be authenticated to retrieve them. To authenticate, we can use "managed identity" that gives Azure services an automatically managed identity in Azure AD. So the answer is Azure AD.

Remember that Azure AD provides access tokens. Azure Key vault is used to securely store passwords, secrets, certificates and tokens.

 

Reference: [https://docs.microsoft.com/en-us/azure/key-vault/general/basic-concepts](https://docs.microsoft.com/en-us/azure/key-vault/general/basic-concepts)

#### Question 9: Correct

Yes or No:

 

Azure Pay-As-You-Go pricing is an example of Capex.

- No

(Correct)

- Yes

 

One of the major changes that you will face when you move from on-premises cloud to the public cloud is the switch from capital expenditure (buying hardware) to operational expenditure (paying for service as you use it).

 

Reference: [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/fiscal-outcomes](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/fiscal-outcomes)

#### Question 10: Correct

How does Azure AD B2B Collaboration benefit organizations when collaborating with external partners?

- It grants full administrator access to external partners.

- It enables external partners to manage Azure subscriptions.

- It provides controlled access to specified resources while maintaining security.

(Correct)

- It integrates external partners into the organization's on-premises network.

Azure AD B2B Collaboration enables organizations to securely collaborate with external partners by granting them controlled access to specific resources. This allows external partners to work on shared projects without compromising security.

 

Reference: [https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview)

#### Question 11: Correct

Which of the following would you recommend for these given requirements?

 

1) Create thousands of identical virtual machines in minutes

2) Deploy across availability zones to protect against datacenter failures

- Azure Kubernetes

- Azure Container Instance

- Azure Virtual Machine Scale Sets

(Correct)

- Azure Blueprints

- Azure Resource Groups

- Azure Virtual Machines

According to the official website : 

 

Azure Virtual Machine Scale Sets is Automated virtual machine scaling that helps you cost-effectively simplify the deployment, management, and availability of your applications.

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_19-14-04-834b00b4057d776755eb60c62160df93.png)

 

Reference : [https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/](https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/)

#### Question 12: Correct

Which of the following scenarios are suitable for using Data Box to import data to Azure?

- Moving a media library from offline tapes to Azure

(Correct)

- Incremental backups of Azure virtual machines

- One-time migration of a large amount of on-premises data

(Correct)

- Configuring real-time data synchronization between Azure and on-premises servers

The correct options are : 

 

One-time migration of a large amount of on-premises data: Azure Data Box is an ideal solution for importing large volumes of data to Azure when network connectivity is limited or insufficient. It is suitable for one-time migration scenarios where you need to move a large amount of data from on-premises to Azure.

 

Moving a media library from offline tapes to Azure: Data Box can be used to move media libraries from offline tapes to Azure, creating an online media library. It provides a secure and efficient way to transfer large amounts of media files to Azure storage services.

 

Other options -

 

Configuring real-time data synchronization between Azure and on-premises servers: Data Box is designed for offline data transfers and is not meant for real-time data synchronization between Azure and on-premises servers. For real-time data synchronization, you might consider Azure File Sync or other data synchronization services.

 

Incremental backups of Azure virtual machines: Data Box is used for transferring data to or from Azure, not specifically for incremental backups of Azure virtual machines. To perform incremental backups of Azure VMs, you can use Azure Backup service, which is designed for that purpose.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options)

#### Question 13: Correct

In a scenario where you need to manage access, policies, and compliance for multiple subscriptions, which Azure service would you use?

- Azure management groups

(Correct)

- Azure Active Directory

- Azure resource groups

- Azure subscriptions

Azure management groups is the correct answer.

 

In a scenario where you need to manage access, policies, and compliance for multiple subscriptions, you would use Azure management groups. Management groups provide a level of scope above subscriptions, allowing you to organize subscriptions into containers and apply governance conditions to the management groups. All subscriptions within a management group automatically inherit the conditions applied to the management group.

 

Other options -

 

- Azure Active Directory: While Azure AD is used for identity and access management, it does not directly manage policies and compliance for multiple subscriptions.

- Azure subscriptions: Subscriptions are a unit of management, billing, and scale in Azure, but they do not provide a higher level of scope for managing multiple subscriptions.

- Azure resource groups: Resource groups are used to organize resources within a subscription, but they do not provide a higher level of scope for managing multiple subscriptions.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)

#### Question 14: Correct

_____________ make it easier to identify groups that generate the biggest Azure costs, which can help you adjust your spending accordingly.

- Tags

(Correct)

- Policies

- Blueprints

- Mangement Groups

 

Tags help you manage costs associated with the different groups of Azure products and resources. You can apply tags to groups of Azure resources to organize billing data.

For example, if you run several VMs for different teams, you can use tags to categorize costs by department, such as Human Resources, Marketing, or Finance; or by environment, such as Test or Production.

Tags make it easier to identify groups that generate the biggest Azure costs, which can help you adjust your spending accordingly.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/6-manage-minimize-total-cost](https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/6-manage-minimize-total-cost)

#### Question 15: Correct

An Azure Web App that queries an on-prem Oracle SQL Database is an example of a ____________________ cloud architecture.

- multi-vendor

- public

- hybrid

(Correct)

- private

Since you are using both Azure, as well as on-prem resources ( A combination of both ) -> This is an example of a hybrid cloud!

 

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-03_20-40-37-bbbeae1d4e6e6fa044a55d13ff640aba.png)

Reference: [https://azure.microsoft.com/en-in/overview/what-is-hybrid-cloud-computing/](https://azure.microsoft.com/en-in/overview/what-is-hybrid-cloud-computing/)

#### Question 16: Correct

Yes or No:

 

Purchasing your own infrastructure and deploying it in your own data center is an example of CapEx.

- No

- Yes

(Correct)

Deploying your own datacenter is definitely an example of CapEx. This is because you need to purchase all the infrastructure upfront before you can use it.

 

References: [https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold](https://docs.microsoft.com/en-us/azure/architecture/cloud-adoption/appendix/azure-scaffold)

#### Question 17: Correct

True or False: Data stored in an Azure Storage account is automatically copied twice.

- False

(Correct)

- True

This is False.

 

Azure Storage offers multiple redundancy options, including locally redundant storage (LRS), zone-redundant storage (ZRS), geo-redundant storage (GRS), and read-access geo-redundant storage (RA-GRS).

LRS and ZRS provide redundancy within a datacenter or within a single zone, respectively, and create three copies of the data. GRS and RA-GRS provide additional redundancy across multiple datacenters or regions, respectively, and create six copies of the data (three copies in the primary region and three copies in the secondary region).

However, none of these redundancy options provide only two copies of the data by default.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy](https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy)

#### Question 18: Correct

Yes or No:

 

Azure Reserved VM Instances are an example of Opex.

- Yes

- No

(Correct)

A reserved instance is where you pay upfront for the use of a virtual machine for a period of time (1 or 3 years). This can save you money as you receive a discount on the cost of a VM if you pay upfront for a reserved instance.

 

However, as this is an upfront payment, it will be classed as CapEx, not OpEx.

 

Simple way to remember : Upfront payment = Capex, Pay as you go = Opex!

#### Question 19: Correct

Your organization needs to move all its data back to on-premises due to new government regulations. Which Azure service should you use to export data from Azure for this migration?

- Azure Data Factory

- AzCopy

- Azure Data Box

(Correct)

- Azure Site Recovery

The correct option is Azure Data Box. Azure Data Box is designed for transferring large amounts of data to and from Azure. In this scenario, where the organization needs to move all its data back to on-premises due to government regulations, Data Box is the most suitable choice. It provides a secure and efficient way to transfer large volumes of data without relying on limited or slow network connections.

 

Wrong options:

 

- Azure Data Factory - Azure Data Factory is a cloud-based data integration service that allows you to create, schedule, and manage data workflows. While it can be used to move and transform data, it's not the best option for large-scale data export to on-premises, especially with limited network connectivity.

- Azure Site Recovery - Azure Site Recovery is a disaster recovery service that helps protect and recover on-premises and Azure-based virtual machines. It is not designed for exporting large amounts of data from Azure to on-premises environments.

- AzCopy - AzCopy is a command-line utility for copying data to and from Azure Storage. While it can be used for data transfers, it relies on network connectivity, which may not be suitable for transferring large amounts of data back to on-premises locations.

 

Reference: [https://docs.microsoft.com/en-us/azure/databox/data-box-overview](https://docs.microsoft.com/en-us/azure/databox/data-box-overview)

#### Question 20: Correct

How does Microsoft Purview contribute to data security and compliance?

- It encrypts data at rest and in transit.

- It enforces strict role-based access control for virtual machines.

- It helps classify and protect sensitive data and ensures compliance policies are followed.

(Correct)

- It provides real-time monitoring of network traffic.

Microsoft Purview provides a unified data governance solution to help manage and govern your on-premises, multicloud, and software as a service (SaaS) data. Microsoft Purview helps organizations classify and label data, apply data protection policies, and manage access controls. This ensures that sensitive data is properly protected and that compliance with data regulations is maintained, contributing to data security and compliance efforts.

 

Reference: [https://azure.microsoft.com/en-ca/products/purview](https://azure.microsoft.com/en-ca/products/purview)

#### Question 21: Correct

What are the two types of subscription boundaries that you can use in Azure?

- Billing boundary

(Correct)

- Access control boundary

(Correct)

- Geographical boundary

- Organizational boundary

In Azure, you can use two types of subscription boundaries:

 

1. Billing boundary: This subscription type determines how an Azure account is billed for using Azure. You can create multiple subscriptions for different types of billing requirements. Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.

2. Access control boundary: Azure applies access-management policies at the subscription level, and you can create separate subscriptions to reflect different organizational structures. An example is that within a business, you have different departments to which you apply distinct Azure subscription policies. This billing model allows you to manage and control access to the resources that users provision with specific subscriptions.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)

#### Question 22: Correct

Your legal team is requesting for documentation pertaining to Microsoft's implementation of controls and processes, namely - Audit Reports, Compliance scores, Pen-Test and Security assessments, and Industry compliance.

 

Where can you obtain this information?

- Microsoft Privacy Statement

- Azure Support Docs

- Azure Advisor

- Azure Resources

- Service Trust Portal

(Correct)

 

The Microsoft Service Trust Portal contains details about Microsoft's implementation of controls and processes that protect our cloud services.

 

![](https://img-c.udemycdn.com/redactor/raw/practice_test_#### Question_explanation/2022-07-23_17-53-34-bf82542743976ce17ee8a6455fced3b5.png)

 

![](https://img-c.udemycdn.com/redactor/raw/practice_test_#### Question_explanation/2022-07-23_17-53-35-3159e0827fb41a2197637a3505a4ceaf.png)

 

Reference: [https://servicetrust.microsoft.com](https://servicetrust.microsoft.com/)

#### Question 23: Correct

Which of the following would you use to deploy and manage containerised applications to provide an integrated continuous integration and continuous delivery (CI/CD) experience and enterprise-grade security and governance.

- Azure Container Instances

- Azure Functions

- Azure Batch

- Azure Kubernetes

(Correct)

 

You can deploy and manage containerised applications more easily with a fully managed Kubernetes service. Azure Kubernetes Service (AKS) offers serverless Kubernetes, an integrated continuous integration and continuous delivery (CI/CD) experience and enterprise-grade security and governance. You can also unite your development and operations teams on a single platform to rapidly build, deliver and scale applications with confidence.

 

![](https://img-c.udemycdn.com/redactor/raw/2020-08-12_18-22-01-3dfec47e0b7037b451c46bd551f3688c.png)

 

Reference: [https://azure.microsoft.com/en-in/services/kubernetes-service/#features](https://azure.microsoft.com/en-in/services/kubernetes-service/#features)

#### Question 24: Incorrect

Which of the following is a way that Azure AD Identity Protection helps to protect against identity-based attacks?

- By requiring all users to use multi-factor authentication

(Incorrect)

- By enforcing strong passwords for all users

- By automatically blocking all sign-in attempts from high-risk IP addresses

- By monitoring users' device health and security posture

(Correct)

Azure AD Identity Protection uses various signals, including device health and security posture, to detect identity-based attacks and suspicious activities. By monitoring these factors, it can assess the risk level of a user's sign-in attempt or activity and take appropriate action, such as requiring additional authentication or blocking access.

Note that Azure AD Identity Protection is not a replacement for strong passwords, multi-factor authentication, or other security measures. Instead, it is an additional layer of security that helps to protect against identity-based attacks.

- By enforcing strong passwords for all users: This is incorrect because enforcing strong passwords is not a specific feature of Azure AD Identity Protection, but rather a general best practice for secure password management.

- By automatically blocking all sign-in attempts from high-risk IP addresses: This is incorrect because Azure AD Identity Protection does not automatically block sign-in attempts based on IP address, but instead uses a risk-based approach to evaluate sign-in attempts and assess the level of risk.

- By requiring all users to use multi-factor authentication: This is incorrect because although Azure AD Identity Protection supports multi-factor authentication, it is not the only method used to protect against identity-based attacks.

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview)

#### Question 25: Correct

A Senior Security Engineer in your company has enforced MFA for all users. How does MFA enhance security?

- It requires a Social Insurance Number and a Password

- It requires a Password and a code through the Microsoft Authenticator App

(Correct)

- It uses two passwords

- It requires password complexity

 

Multi-factor authentication is a process where a user is prompted during the sign-in process for an additional form of identification, such as to enter a code on their cellphone or to provide a fingerprint scan.

If you only use a password to authenticate a user, it leaves an insecure vector for attack. If the password is weak or has been exposed elsewhere, is it really the user signing in with the username and password, or is it an attacker? When you require a second form of authentication, security is increased as this additional factor isn't something that's easy for an attacker to obtain or duplicate.

![](https://docs.microsoft.com/en-us/azure/active-directory/authentication/media/concept-mfa-howitworks/methods.png)

 

Azure AD Multi-Factor Authentication works by requiring two or more of the following authentication methods:

 

1) Something you know, typically a password.

2) Something you have, such as a trusted device that is not easily duplicated, like a phone or hardware key.

3) Something you are - biometrics like a fingerprint or face scan.

 

Users can register themselves for both self-service password reset and Azure AD Multi-Factor Authentication in one step to simplify the on-boarding experience. Administrators can define what forms of secondary authentication can be used. Azure AD Multi-Factor Authentication can also be required when users perform a self-service password reset to further secure that process.

 

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 26: Correct

As part of its modernization strategy, your company has decided to move all its operations to the Azure cloud. It is looking for an advanced modernization, and optimization service for Azure with a wide range of tools for assessment.

 

Which of the following would you recommend?

- Azure Advisor

- Azure Cloud Adopter

- Azure Migrate

(Correct)

- Azure Data Box

 

Azure Migrate provides a simplified migration, modernization, and optimization service for Azure. All pre-migration steps such as discovery, assessments, and right-sizing of on-premises resources are included for infrastructure, data, and applications. Azure Migrate’s extensible framework allows for integration of third-party tools, thus expanding the scope of supported use-cases. It provides the following:

 

- Unified migration platform: A single portal to start, run, and track your migration to Azure.

- Range of tools: A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and Azure Migrate: Server Migration. Azure Migrate also integrates with other Azure services and tools, and with independent software vendor (ISV) offerings.

 

Reference: [https://docs.microsoft.com/en-us/azure/migrate/migrate-services-overview](https://docs.microsoft.com/en-us/azure/migrate/migrate-services-overview)

#### Question 27: Correct

Which of the following is a factor that Azure AD Identity Protection uses to assess the risk level of a user's sign-in attempt or activity?

- The user's physical location

- The user's job title

- The user's email address

- The user's device health and security posture.

(Correct)

The correct answer is - The user's device health and security posture is one of the factors that Azure AD Identity Protection uses to assess the risk level of a user's sign-in attempt or activity. Azure AD Identity Protection uses machine learning algorithms and various risk factors, such as device health and security posture, to identify potential risks and take appropriate action to protect the user's identity and the organization's resources.

 

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview)

#### Question 28: Correct

You want to set up separate environments for development and testing, and security in Azure. What would you create to achieve this?

- Additional resource groups

- Additional Azure accounts

- Additional management groups

- Additional subscriptions

(Correct)

Creating additional subscriptions is a suitable approach for setting up separate environments for development and testing, and security in Azure. By having separate subscriptions for different environments, you can manage and control access to the resources provisioned within each subscription, and it helps you track costs and apply different access-management policies more effectively.

 

Other options:

 

Additional resource groups: While resource groups help organize resources within a subscription, they don't provide the level of separation needed for different environments with distinct access-management policies and billing tracking. Resource groups are more suitable for organizing resources that have the same lifecycle and need the same access control settings.

 

Additional management groups: Management groups are used to organize subscriptions and apply governance conditions to them. Creating additional management groups would not directly create separate environments for development, testing, and security. They are more suited for organizing multiple subscriptions and applying consistent policies across them.

 

Additional Azure accounts: Azure accounts are associated with Azure Active Directory (Azure AD) identities and used for billing purposes. Creating additional Azure accounts doesn't directly create separate environments. It is the subscriptions within the accounts that determine the environments and access controls.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)

#### Question 29: Incorrect

True or False:

 

You can create multiple billing reports per subscription. This is handy when you have multiple departments and need to do a chargeback of cloud costs.

- False

(Correct)

- True

(Incorrect)

 

You can create one billing report per subscription. If you have multiple departments and need to do a "chargeback" of cloud costs, one possible solution is to organize subscriptions by department or by project.

 

Resource tags can also help.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/10-create-subscription-governance-strategy](https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/10-create-subscription-governance-strategy)

#### Question 30: Correct

Which of the following is NOT an Azure Subscription type?

- Free Trial

- Pay As You Go

- Pay For a Year

(Correct)

- Member offers

 

You probably know that an Azure _subscription_ provides you with access to Azure resources such as virtual machines (VMs), storage, and databases. The types of resources you use affect your monthly bill.

Azure offers both free and paid subscription options to fit your needs and requirements. They are:

 

- Free trial

A free trial subscription provides you with 12 months of popular free services, a credit to explore any Azure service for 30 days, and more than 25 services that are always free. Your Azure services are disabled when the trial ends or when your credit expires for paid products, unless you upgrade to a paid subscription.

- Pay-as-you-go

A pay-as-you-go subscription lets you pay for what you use by attaching a credit or debit card to your account. Organizations can apply for volume discounts and prepaid invoicing.

- Member offers

Your existing membership to certain Microsoft products and services might provide you with credits for your Azure account, and reduced rates on Azure services. For example, member offers are available to Visual Studio subscribers, Microsoft Partner Network members, Microsoft for Startups members, and Microsoft Imagine members.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/4-purchase-azure-services](https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/4-purchase-azure-services)

#### Question 31: Correct

To begin using Azure Storage, you first create an Azure ________________ to store your data objects.

- Resource Group

- DNS

- Storage Section

- Storage Account

(Correct)

 

[Azure Storage](https://azure.microsoft.com/product-categories/storage) is a service that you can use to store files, messages, tables, and other types of information. Clients such as websites, mobile apps, desktop applications, and many other types of custom solutions can read data from and write data to Azure Storage. Azure Storage is also used by infrastructure as a service virtual machines, and platform as a service cloud services.

 

To begin using Azure Storage, you first create an Azure Storage account to store your data objects. You can create an Azure Storage account by using the Azure portal, PowerShell, or the Azure CLI. Your storage account will contain all of your Azure Storage data objects, such as blobs, files, and disks.

 

![](https://docs.microsoft.com/en-ca/learn/azure-fundamentals/azure-storage-fundamentals/media/account-container-blob-4da0ac47.png)

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-storage-accounts](https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-storage-accounts)

#### Question 32: Correct

How does Microsoft Purview enhance data governance across multi-cloud environments?

- By offering a unified solution to manage and govern data across various cloud and on-premises sources.

(Correct)

- By offering virtual machine management capabilities.

- By enabling cross-platform application deployment.

- By providing a cloud-native development environment.

Microsoft Purview provides a unified solution for managing and governing data across various sources, including multi-cloud and on-premises environments. It helps organizations maintain consistent data governance practices and policies regardless of where the data resides.

 

Reference: [https://azure.microsoft.com/en-ca/products/purview](https://azure.microsoft.com/en-ca/products/purview)

#### Question 33: Correct

What is the primary role of Azure Arc-enabled data services?

- To optimize network connectivity between Azure regions.

- To provide cloud-based virtual machines for data processing.

- To extend Azure data services to on-premises and multi-cloud environments.

(Correct)

- To manage and monitor data services exclusively within Azure regions.

Azure Arc-enabled data services extend Azure data services to on-premises and multi-cloud environments, enabling consistent data management and integration across different locations.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-arc/overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

#### Question 34: Incorrect

Which of the following is an event driven, compute-on-demand service , with capabilities to implement code triggered by events occurring in Azure or third party service as well as on-premises systems?

- Azure Policies

- Azure Functions

(Correct)

- Azure Kubernetes

- Azure Machine Learning Studio

- Azure Serverless

(Incorrect)

- Azure CosmosDB

 

Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.

You focus on the pieces of code that matter most to you, and Azure Functions handles the rest.

 

Reference: [https://azure.microsoft.com/en-in/blog/introducing-azure-functions/](https://azure.microsoft.com/en-in/blog/introducing-azure-functions/)

#### Question 35: Correct

Which of the following is an excellent choice if you want to run multiple instances of an application on a single host machine?

- Containers

(Correct)

- Functions

- Blueprints

- Scale Sets

 

While virtual machines are an excellent way to reduce costs versus the investments that are necessary for physical hardware, they're still limited to a single operating system per virtual machine. If you want to run multiple instances of an application on a single host machine, containers are an excellent choice.

 

What are containers?

 

Containers are a virtualization environment. Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host. Unlike virtual machines, you don't manage the operating system for a container. Virtual machines appear to be an instance of an operating system that you can connect to and manage, but containers are lightweight and designed to be created, scaled out, and stopped dynamically. While it's possible to create and deploy virtual machines as application demand increases, containers are designed to allow you to respond to changes on demand. With containers, you can quickly restart in case of a crash or hardware interruption. One of the most popular container engines is Docker, which is supported by Azure.

 

Containers are managed through a container orchestrator, which can start, stop, and scale out application instances as needed. There are two ways to manage both Docker and Microsoft-based containers in Azure: Azure Container Instances and Azure Kubernetes Service (AKS).

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-container-services](https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-container-services)

#### Question 36: Correct

What benefit does Infrastructure as Code (IaC) provide for disaster recovery scenarios?

- It enables version control for application code.

- It ensures consistent infrastructure configuration replication.

(Correct)

- It accelerates the download speed of cloud resources.

- It automates the creation of virtual machines.

From the official documentation:

 

Infrastructure as Code (IaC) is a key DevOps practice that involves the management of infrastructure, such as networks, compute services, databases, storages, and connection topology, in a descriptive model. IaC allows teams to develop and release changes faster and with greater confidence. Benefits of IaC include:

 

- Increased confidence in deployments

- Ability to manage multiple environments

- Improved understanding of the state of infrastructure

 

With IaC, you can create infrastructure configurations as code. This enables consistent replication of infrastructure settings, reducing the risk of configuration errors during disaster recovery scenarios.

 

Reference: [https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/infrastructure-as-code](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/considerations/infrastructure-as-code)

#### Question 37: Incorrect

Which of the following categories does Azure Kubernetes service belong to?

- Database as a service (DaaS)

- Software as a service (SaaS)

- Infrastructure as a service (IaaS)

(Correct)

- Platform as a service (PaaS)

(Incorrect)

Remember that Virtual Machines, Containers and Kubernetes are considered Compute Services, and fall under IaaS!

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_19-21-30-6506fcdb4760bf70c958ec8d013d7aaf.png)

 

Azure Kubernetes Service (AKS) offers serverless Kubernetes, an integrated continuous integration and continuous delivery (CI/CD) experience, and enterprise-grade security and governance. Unite your development and operations teams on a single platform to rapidly build, deliver, and scale applications with confidence.

 

Reference: [https://azure.microsoft.com/en-us/services/kubernetes-service/](https://azure.microsoft.com/en-us/services/kubernetes-service/)

#### Question 38: Incorrect

Your boss wants to ensure that your teams virtual machines are automatically patched and updated. Which Azure Virtual Machines feature should you use to achieve this?

- Azure Virtual Machine Extensions
- Azure Virtual Machine Configuration Management
- Azure Update Management (Correct)
- Azure Virtual Machine Scale Sets (Incorrect)

A tough  Question for sure. Azure Update Management is the correct answer, and it is a service that provides a solution for automatically patching and updating virtual machines in Azure. It enables you to schedule and track updates across your entire Azure environment, including virtual machines, hybrid machines, and servers. You can also assess the compliance of your virtual machines against security baselines and audits.

#### Question 39: Correct

____________________ notifies you about Azure service incidents and planned maintenance so you can take action to mitigate downtime.

- Azure Service Health

(Correct)

- Azure Monitor

- Azure Active Directory

- Azure Trust Center

 

Azure Service Health provides personalised alerts and guidance for Azure service issues.

 

Azure Service Health notifies you about Azure service incidents and planned maintenance so you can take action to mitigate downtime. You can also configure customisable cloud alerts and use your personalised dashboard to analyse health issues, monitor the impact to your cloud resources, get guidance and support, and share details and updates.

 

IMPORTANT!

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-03_20-06-54-98569b93c4d534c3dd4be09c47fa0bbf.png)

 

![](https://img-c.udemycdn.com/redactor/raw/test_#### Question_description/2021-04-03_20-06-54-71c0abdee7c86b8e4512591ab15db569.png)

 

Reference: [https://azure.microsoft.com/en-ca/features/service-health/](https://azure.microsoft.com/en-ca/features/service-health/)

#### Question 40: Correct

Which of the following options would meet these requirements?

 

1) SDKs for popular languages, APIs for SQL, MongoDB, Cassandra and more

2) Guaranteed speed at any scale with instant and limitless elasticity, fast reads, and multi-region writes anywhere in the world

3) The ability to work with NoSQL data

- Azure Files

- Azure Queues

- Azure Table Storage

- Azure Cosmos DB

(Correct)

According to the offical documentation : 

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_18-52-05-ef189a13fc080ddafb5e0c48556dc24c.png)![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_18-52-41-20bb5275342e3278d12b7fcc13976832.png)

Reference : [https://azure.microsoft.com/en-us/services/cosmos-db/#featured](https://azure.microsoft.com/en-us/services/cosmos-db/#featured)

#### Question 41: Correct

What is the recommended minimum data size for using Data Box to transfer data in scenarios with limited network connectivity?

- 40 TB

(Correct)

- 100 TB

- 10 TB

- 20 TB

Data Box is an Azure service designed for offline data transfer when dealing with large data sizes and limited or no network connectivity. The recommendation for using Data Box is for data sizes larger than 40 TB. This is because, at such large data sizes, transferring data over the network can be slow, unreliable, or costly due to bandwidth limitations.

In scenarios with limited network connectivity, using Data Box helps avoid the challenges of slow data transfer speeds, potential data corruption, and high costs associated with transferring massive amounts of data over the network. By opting for Data Box, you ensure a secure, efficient, and cost-effective solution for moving large volumes of data to or from Azure.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/6-identify-azure-data-migration-options)

#### Question 42: Incorrect

Yes or No:

 

You can enforce Azure AD Multi-Factor Authentication for all users via the Microsoft Authenticator app, phone call, or SMS code.

- Yes

(Incorrect)

- No

(Correct)

 

Azure AD Multi-Factor Authentication is a Microsoft service that provides multifactor authentication capabilities. Azure AD Multi-Factor Authentication enables users to choose an additional form of authentication during sign-in, such as a phone call or mobile app notification.

 

The Azure Active Directory free edition enables Azure AD Multi-Factor Authentication for administrators with the global admin level of access, via the Microsoft Authenticator app, phone call, or SMS code. You can also enforce Azure AD Multi-Factor Authentication for all users via the Microsoft Authenticator app only, by enabling security _defaults_ in your Azure AD tenant.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/secure-access-azure-identity-services/4-what-are-mfa-conditional-access](https://docs.microsoft.com/en-ca/learn/modules/secure-access-azure-identity-services/4-what-are-mfa-conditional-access)

#### Question 43: Correct

You are a cloud administrator responsible for managing a large Azure environment with multiple subscriptions. You want to enforce a company-wide requirement that requires all virtual machines to be encrypted using Azure Disk Encryption. Which Azure service should you use to enforce this?

- Azure Security Center

- Azure Policy

(Correct)

- Azure Resource Manager

- Azure Active Directory

The correct answer is Azure Policy.

 

Azure Policy can be used to enforce company-wide policies across multiple Azure subscriptions, including policies related to Azure Disk Encryption. By creating a policy definition that requires all virtual machines to have Azure Disk Encryption enabled, you can ensure that this policy is applied consistently across your entire Azure environment.

 

Other options -

 

- Azure Security Center: This is a service that helps customers protect their Azure and on-premises resources from threats, but it is not designed specifically for enforcing policies related to Azure Disk Encryption.

- Azure Active Directory: This is a cloud-based identity and access management service, and while it can be used to manage access to Azure resources, it is not designed to enforce policies related to Azure Disk Encryption.

- Azure Resource Manager: This is a service that allows customers to manage resources in their Azure subscription, but it is not designed to enforce policies related to Azure Disk Encryption.

- multiple subscriptions.

 

Reference: [https://docs.microsoft.com/en-us/azure/governance/policy/overview](https://docs.microsoft.com/en-us/azure/governance/policy/overview)

#### Question 44: Correct

You plan to deploy an SQL database to Azure. One of the major requirements is resource isolation, i.e this database should not be accessible to other your other resources on Azure.

 

Which of the following can help with this?

- Deploy the SQL Database to a different Virtual Network

(Correct)

- Use an Azure ExpressRoute circuit

- Setup custom rules in Azure Blueprints

- Setup custom rules in Azure Policies

Deploy the SQL Database to a different Virtual Network explains network segmentation. You can deploy the SQL database to a new Virtual Network and filter any traffic using a Network Security Group on top of it.

 

 

Azure Virtual Network (VNet) is the fundamental building block for your private network in Azure. VNet enables many types of Azure resources, such as Azure Virtual Machines (VM), to securely communicate with each other, the internet, and on-premises networks. VNet is similar to a traditional network that you'd operate in your own data center, but brings with it additional benefits of Azure's infrastructure such as scale, availability, and `isolation.`

 

Communicate between Azure resources

 

You'll want to enable Azure resources to communicate securely with each other. You can do that in one of two ways:

- Virtual networks Virtual networks can connect not only VMs but other Azure resources, such as the App Service Environment for Power Apps, Azure Kubernetes Service, and Azure virtual machine scale sets.

- Service endpoints You can use service endpoints to connect to other Azure resource types, such as Azure SQL databases and storage accounts. This approach enables you to link multiple Azure resources to virtual networks to improve security and provide optimal routing between resources.

 

Filter network traffic

 

Azure virtual networks enable you to filter traffic between subnets by using the following approaches:

 

- Network security groups A network security group is an Azure resource that can contain multiple inbound and outbound security rules. You can define these rules to allow or block traffic, based on factors such as source and destination IP address, port, and protocol.

- Network virtual appliances A network virtual appliance is a specialized VM that can be compared to a hardened network appliance. A network virtual appliance carries out a particular network function, such as running a firewall or performing wide area network (WAN) optimization.

 

Reference: [https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)

#### Question 45: Incorrect

Which of the following is not a cost saving solution?

- Using Azure Hybrid Benefit to repurpose software licenses on Azure

- Deleting unused resources

- Using Azure Reservations to prepay

- Choosing low-cost locations and regions

(Incorrect)

- Using spending limits to restrict your spending

- Shutting down Virtual Machines at night

(Correct)

- Resize underutilized virtual machines

Shutting down Virtual Machines at night is not a cost saving solution.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/6-manage-minimize-total-cost](https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/6-manage-minimize-total-cost)

#### Question 46: Correct

In the context of Azure AD B2C, what is a "policy"?

- An encryption key used to secure customer data.

- A predefined set of access permissions for internal employees.

- A secure authentication method using multi-factor authentication.

- A customized set of rules and behaviors for customer identity interactions.

(Correct)

In Azure AD B2C, a policy is a collection of predefined rules and behaviors that define how customers interact with your applications. It helps you customize the user journey, authentication methods, and user flows during sign-up, sign-in, and profile management.

 

Reference: [https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview](https://learn.microsoft.com/en-us/azure/active-directory/external-identities/external-identities-overview)

#### Question 47: Correct

Which of the following is an example of an Azure Application Platform?

- Azure App service

(Correct)

- Azure Firewall

- Azure Cache for Redis

- Azure DNS

- Azure Load Balancer

 

Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. You can develop in your favorite language, be it .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. Applications run and scale with ease on both Windows and Linux-based environments. For Linux-based environments, see [App Service on Linux](https://docs.microsoft.com/en-us/azure/app-service/containers/app-service-linux-intro).

 

![](https://img-c.udemycdn.com/redactor/raw/2020-07-16_18-56-28-19bd4481cbe43457c7797bdf352bd8d7.png)

 

Using Azure App Service, it is also possible to scale apps on an enterprise grade platform:

 

![](https://img-c.udemycdn.com/redactor/raw/2020-07-16_18-58-07-217cdb788c6380ba5bf6f867218e934a.png)

 

 

Reference : [https://docs.microsoft.com/en-us/azure/app-service/overview](https://docs.microsoft.com/en-us/azure/app-service/overview)

#### Question 48: Incorrect

Which of the following statements regarding Azure subscriptions are correct? 

- Azure subscription cannot have a trust relationship with an Azure Active Directory (AD) instance

- Billing is applied to each subscription separately

(Correct)

- Subscription is dependent on a region

(Correct)

- Multiple subscriptions cannot be created within an Azure account

- Trial subscription can be converted to paid

(Correct)

Billing is applied to each subscription separately - Yes! It is one of the many reasons why people use separate subscriptions.

 

Trial subscription can be converted to paid - Of course. When you sign up for an Azure free account, you get $200 credit. In the first 30 days, any services you use beyond their free amounts will be deducted from that $200 credit. When you’ve used up your $200 credit or 30 days have passed (whichever happens first), you’ll need to upgrade by moving to [pay-as-you-go pricing](https://azure.microsoft.com/en-us/offers/ms-azr-0003p/). That way, you can keep getting free amounts of services and purchase services beyond their free amounts as needed. The cost of those services is charged to the payment method you provide.

 

Subscription is dependent on a region - Yes, when you create a subscription in Azure, you need to specify a certain region for that Subscription. Hence, this choice is valid as well.

 

All other options are invalid and don't stand true.

 

References:

 

[https://techcommunity.microsoft.com/t5/azure/understanding-azure-account-subscription-and-directory/m-p/34800](https://techcommunity.microsoft.com/t5/azure/understanding-azure-account-subscription-and-directory/m-p/34800)

[https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-subscriptions-associated-directory)

[https://azure.microsoft.com/en-us/free/free-account-faq/](https://azure.microsoft.com/en-us/free/free-account-faq/)

#### Question 49: Incorrect

When you form a cloud center of excellence team or a cloud custodian team, that team can use Azure _______________ to scale their governance practices throughout the organization.

- Compliance

(Incorrect)

- Resource Groups

- Blueprints

(Correct)

- Subscriptions

 

When you form a cloud center of excellence team or a cloud custodian team, that team can use Azure Blueprints to scale their governance practices throughout the organization.

Implementing a blueprint in Azure Blueprints involves these three steps:

 

1. Create an Azure blueprint.

2. Assign the blueprint.

3. Track the blueprint assignments.

With Azure Blueprints, the relationship between the blueprint definition (what should be deployed) and the blueprint assignment (what was deployed) is preserved. In other words, Azure creates a record that associates a resource with the blueprint that defines it. This connection helps you track and audit your deployments.

Blueprints are also versioned. Versioning enables you to track and comment on changes to your blueprint.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/8-govern-subscriptions-azure-blueprints](https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/8-govern-subscriptions-azure-blueprints)

#### Question 50: Correct

_____________ helps you estimate the cost savings of operating your solution on Azure over time compared to operating in your on-premises datacenter.

- Azure Pricing Calculator

- Azure Advisor

- Azure TCO Calculator

(Correct)

- Azure Blueprints

 

The [TCO Calculator](https://azure.microsoft.com/pricing/tco/calculator) helps you estimate the cost savings of operating your solution on Azure over time compared to operating in your on-premises datacenter.

 

The term _total cost of ownership_ is used commonly in finance. It can be hard to see all the hidden costs related to operating a technology capability on-premises. Software licenses and hardware are additional costs.

With the TCO Calculator, you'll enter the details of your on-premises workloads. Then you can review the suggested industry-average cost (which you can adjust) for related operational costs. These costs include electricity, network maintenance, and IT labor. You're then presented with a side-by-side report. Using the report, you can compare those costs with the same workloads running on Azure.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/2-compare-costs-tco-calculator](https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/2-compare-costs-tco-calculator)

#### Question 51: Correct

Yes or No:

 

All the resources residing in a Resource Group must belong to the same Region.

- No

(Correct)

- Yes

 

Azure resources deployed to a single resource group can be located in different regions. The resource group only contains metadata about the resources it contains.

 

When creating a resource group, you need to provide a location for that resource group. You may be wondering, "Why does a resource group need a location?

 

And, if the resources can have different locations than the resource group, why does the resource group location matter at all?"

The resource group stores metadata about the resources. When you specify a location for the resource group, you're specifying where that metadata is stored. For compliance reasons, you may need to ensure that your data is stored in a particular region.

 

Reference: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)

#### Question 52: Correct

What is the minimum number of Virtual Machines and minimum number of Availability Zones respectively that must be used to guarantee an SLA of 99.99%?

- 2 Virtual Machines, 1 Availability Zone

- 2 Virtual Machines ,  2 Availability Zones

(Correct)

- 1 Virtual Machine, 2 Availability Zones

- 1 Virtual Machine, 1 Availability Zone

Azure offers industry best SLAs for VMs. However, to guarantee an SLA of 99.99%, you must have 2 or more instances deployed across 2 or more Availability Zones!

 

According to the official Azure documentation : 

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_19-11-10-92b628cb4c710c19ab0eb3db737fbc4f.png)

Reference : [https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/](https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/)

#### Question 53: Correct

Yes or No:

 

A unique characteristic of Azure Files from files on a corporate file share is that you cannot access the files from anywhere in the world, it has to be from a specific location.

- No

(Correct)

- Yes

 

Azure Files offers fully managed file shares in the cloud that are accessible via the industry standard Server Message Block and Network File System (preview) protocols. Azure file shares can be mounted concurrently by cloud or on-premises deployments of Windows, Linux, and macOS.

 

One thing that distinguishes Azure Files from files on a corporate file share is that you can access the files from anywhere in the world, by using a URL that points to the file. You can also use Shared Access Signature (SAS) tokens to allow access to a private asset for a specific amount of time.

Here's an example of a service SAS URI, showing the resource URI and the SAS token:

![](https://docs.microsoft.com/en-ca/learn/azure-fundamentals/azure-storage-fundamentals/media/sas-storage-uri-037308fa.png)

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-file-storage](https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-file-storage)

#### Question 54: Correct

You have an on-premises infrastructure and would like to extend its capabilities by making use of Azure services. Which type of cloud deployment is this an example of?

- A private cloud

- A hybrid cloud

(Correct)

- An Internal cloud

- A Public Cloud

 

A hybrid cloud is a combination of a private cloud and a public cloud.

 

A hybrid cloud is a computing environment that combines a public cloud and a private cloud by allowing data and applications to be shared between them.

 

Hybrid cloud

 

- Provides the most flexibility.

- Organizations determine where to run their applications.

- Organizations control security, compliance, or legal requirements.

 

References: [https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models](https://docs.microsoft.com/en-gb/learn/modules/principles-cloud-computing/4-cloud-deployment-models)

#### Question 55: Correct

Which of the following do Azure Arc-enabled servers allow you to do?

- Manage and govern Azure Active Directory.

- Deploy virtual machines in Azure regions.

- Monitor Azure Logic Apps.

- Extend Azure Resource Manager templates to on-premises environments.

(Correct)

Azure Arc-enabled servers allow you to extend Azure Resource Manager templates to on-premises environments. This enables consistent deployment and management practices across both cloud and on-premises resources.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-arc/overview](https://learn.microsoft.com/en-us/azure/azure-arc/overview)

#### Question 56: Correct

Your team is planning to build a set of REST-based web APIs by using your choice of language and framework. The produced apps should be consumable from any HTTP or HTTPS based client.

 

Which of the following would be a great fit for this use case?

- Azure Container Instances

- Azure Kubernetes Service

- Azure App Service

(Correct)

- Azure Virtual Desktops

- Azure Functions

 

App Service enables you to build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers automatic scaling and high availability. App Service supports Windows and Linux and enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model. This platform as a service (PaaS) environment allows you to focus on the website and API logic while Azure handles the infrastructure to run and scale your web applications.

 

API apps

Much like hosting a website, you can build REST-based web APIs by using your choice of language and framework. You get full Swagger support and the ability to package and publish your API in Azure Marketplace. The produced apps can be consumed from any HTTP or HTTPS based client.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-app-services](https://docs.microsoft.com/en-ca/learn/modules/azure-compute-fundamentals/azure-app-services)

#### Question 57: Correct

True or False:

 

The Cool storage tier stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data.

- True

- False

(Correct)

 

Azure Storage offers different access tiers for your blob storage, helping you store object data in the most cost-effective manner. The available access tiers include: 

- Hot access tier: Optimized for storing data that is accessed frequently (for example, images for your website).

- Cool access tier: Optimized for data that is infrequently accessed and stored for at least 30 days (for example, invoices for your customers).

- Archive access tier: Appropriate for data that is rarely accessed and stored for at least 180 days, with flexible latency requirements (for example, long-term backups).

The following considerations apply to the different access tiers:

 

- Only the hot and cool access tiers can be set at the account level. The archive access tier isn't available at the account level.

- Hot, cool, and archive tiers can be set at the blob level, during upload or after upload.

- Data in the cool access tier can tolerate slightly lower availability, but still requires high durability, retrieval latency, and throughput characteristics similar to hot data. For cool data, a slightly lower availability service-level agreement (SLA) and higher access costs compared to hot data are acceptable trade-offs for lower storage costs.

- Archive storage stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data.

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-storage-tiers](https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-storage-tiers)

#### Question 58: Correct

Which storage redundancy option offers the highest level of durability, with a remarkable 16 nines of durability?

- Geo-redundant storage (GRS)

(Correct)

- Locally redundant storage (LRS)

- Zone-redundant storage (ZRS)

- Durable-redundant storage (DRS)

From the official documentation:

 

The storage redundancy option that provides the highest degree of durability, with 16 nines of durability, is "geo-redundant storage (GRS)." GRS copies your data synchronously within a single physical location in the primary region using locally redundant storage (LRS). It then copies your data asynchronously to a single physical location in the secondary region (the region pair) also using LRS. This combination of synchronous and asynchronous replication results in an extremely high level of durability, offering at least 16 nines (99.99999999999999%) of durability for Azure Storage data objects over a given year.

 

Also, there is no option known as DRS.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/3-redundancy)

#### Question 59: Incorrect

What is the purpose of the Azure AD Identity Protection dashboard?

- To enable administrators to manage and investigate risk events.

(Correct)

- To provide an overview of all users' activity logs.

- To show a summary of the risk level of all users.

- To allow administrators to manage users' authentication methods.

(Incorrect)

The correct answer is - To enable administrators to manage and investigate risk events.

 

The purpose of the Azure AD Identity Protection dashboard is to provide administrators with a centralized view of all risky sign-ins, vulnerabilities, and compromised identities. It allows administrators to investigate and manage risk events by providing detailed information about the users, devices, and applications involved in the event. The dashboard also provides recommendations to improve the security posture of the organization, such as enabling multi-factor authentication for at-risk users.

 

- To provide an overview of all users' activity logs: This is incorrect because the Azure AD Identity Protection dashboard focuses on risk events, not activity logs.

- To allow administrators to manage users' authentication methods: This is incorrect because managing users' authentication methods is a separate function that is not part of the Azure AD Identity Protection dashboard.

- To show a summary of the risk level of all users: This is incorrect because while the dashboard provides a risk score for each user, its primary purpose is to enable administrators to investigate and manage risk events, not to provide a summary of the risk level of all users.

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/)

#### Question 60: Correct

Which of the following is a key difference between Azure Active Directory (AAD) and Role-Based Access Control (RBAC)?

- AAD provides identity and access management services, while RBAC provides granular access control within Azure resources.

(Correct)

- AAD is only used for managing access to Microsoft applications, while RBAC is used for managing access to any Azure resource.

- AAD is a cloud-based directory service, while RBAC is a feature within the Azure portal.

- AAD is used for managing access to Azure resources, while RBAC is used for managing access to on-premises resources.

The correct option is : Azure Active Directory (AAD) provides identity and access management services, while Role-Based Access Control (RBAC) provides granular access control within Azure resources.

 

Other options:

 

- AAD is used for managing access to Azure resources, while RBAC is used for managing access to on-premises resources : This is incorrect because AAD can be used for managing access to on-premises resources as well as cloud resources.

- AAD is a cloud-based directory service, while RBAC is a feature within the Azure portal: This is incorrect because AAD is a cloud-based directory service, but RBAC is not a feature within the Azure portal. Rather, RBAC is a built-in feature of the Azure platform for managing access to Azure resources.

- AAD is only used for managing access to Microsoft applications, while RBAC is used for managing access to any Azure resource: This is incorrect because AAD can be used to manage access to both Microsoft and non-Microsoft applications, while RBAC is used only for managing access to Azure resources.

 

Overall, AAD and RBAC have different but complementary roles in managing access to Azure resources. AAD is primarily used for managing user identities and authentication, while RBAC is used for managing granular access control within Azure resources by assigning permissions to specific roles rather than individual users.

 

Reference: [https://azure.microsoft.com/en-us/products/active-directory/#faq](https://azure.microsoft.com/en-us/products/active-directory/#faq)

#### Question 61: Correct

Your company's IT department wants to ensure that its virtual machines (VMs) are highly available and have automatic failover in case of a hardware failure. Which Azure Virtual Machines feature should you use to achieve this?

- Virtual Machine Scale Sets

- Availability Zones

(Correct)

- Azure Site Recovery

- Azure Virtual Machine Resiliency

Availability Zones is the correct answer. It is an Azure service that provides high availability by replicating applications and data across multiple data-centers within a region. By using availability zones, your virtual machines are deployed in separate physical locations with independent power, cooling, and networking, ensuring that they remain available even if there is a failure in one of the zones. This feature provides automatic failover in case of a hardware failure, making it a suitable solution for ensuring highly available virtual machines.

 

Other Options:

 

 

- Virtual Machine Scale Sets: This is an Azure service that allows you to create and manage a group of identical virtual machines in Azure. This service is designed to help you scale your applications horizontally to meet increased demand, but it does not provide a solution for ensuring automatic failover in case of a hardware failure.

 

- Azure Site Recovery: This is an Azure service that allows you to replicate virtual machines from your on-premises environment to Azure or between Azure regions. While this service can help you achieve high availability and automatic failover, it is primarily designed for disaster recovery scenarios, and not for ensuring high availability in the event of a hardware failure.

 

- Azure Virtual Machine Resiliency: This is not a valid Azure service or feature. Therefore, it is not a suitable solution for ensuring highly available virtual machines.

Reference: [https://docs.microsoft.com/en-us/azure/availability-zones/az-overview](https://docs.microsoft.com/en-us/azure/availability-zones/az-overview)

#### Question 62: Incorrect

Which of the following is NOT a compute service available in Azure?

- Azure App Service

- Azure Kubernetes

- Azure Functions

(Incorrect)

- Azure CosmosDB

(Correct)

CosmosDB is a Database and not a compute option in Azure.

 

 

Azure offers a number of ways to host your application code. The term _compute_ refers to the hosting model for the computing resources that your application runs on. The following flowchart will help you to choose a compute service for your application.

If your application consists of multiple workloads, evaluate each workload separately. A complete solution may incorporate two or more compute services.

 

 

![](https://img-c.udemycdn.com/redactor/raw/2020-08-12_18-25-06-37c359df72ebc0cb66baa3b3903e9751.png)

 

Reference: [https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree](https://docs.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)

#### Question 63: Incorrect

Which of the following categories does Azure VPN Gateway belong to?

- Platform as a Service (PaaS)

(Incorrect)

- Network as a Service ( NaaS )

- Infrastructure as a Service (IaaS)

(Correct)

- Software as a Service ( SaaS )

According to the official documentation : 

 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_19-24-20-22d7a30dedadbae00297d2a30ca34514.png)

 

Reference: [https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways)

#### Question 64: Correct

How can you deploy an ARM template to Azure?

- By running the ARM template on a local machine be it Windows or Mac.

- By using Azure PowerShell, Azure CLI, or the Azure portal

(Correct)

- By submitting the ARM template to a third-party service such as Dremio.

- By manually configuring each resource through the Azure portal.

ARM templates can be deployed using various tools, including Azure PowerShell, Azure CLI, and the Azure portal. These tools interpret the template and orchestrate the resource provisioning process.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

#### Question 65: Correct

AzCopy is a command-line utility designed to copy ______________.

- Data between Azure Storage accounts

(Correct)

- Database schemas

- Virtual machines

- Data between on-premises file servers

AzCopy is a command-line utility specifically designed to copy data between Azure Storage accounts or between an on-premises location and Azure Storage. It supports Blob Storage, Table Storage, and File Storage transfers.

 

Other options -

 

- Virtual machines - AzCopy is not designed to copy virtual machines; it focuses on data transfers for Azure Storage services.

- Data between on-premises file servers - Although AzCopy can copy data between an on-premises location and Azure Storage, it is not intended for transferring data directly between on-premises file servers without involving Azure Storage.

- Database schema - AzCopy is not designed for copying database schema; it focuses on data transfers for Azure Storage services, such as Blob Storage, Table Storage, and File Storage.

Reference: [https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10](https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10)

#### Question 66: Correct

Your company has a policy that requires all Azure resources to be deployed with a specific set of tags. You want to ensure that this mandate is enforced automatically for all new resources deployed in your Azure environment. Which Azure service should you use to accomplish this?

- Azure Advisor

- Azure Security Center

- Azure Resource Manager

- Azure Policy

(Correct)

The correct answer is Azure Policy.

 

Azure Policy is the Azure service used to enforce policies for resource consistency and compliance. It allows administrators to create and enforce policies that ensure resources deployed in Azure adhere to specific rules, such as the requirement to have a specific set of tags. Azure Policy can evaluate resources against these policies and, if necessary, take actions to remediate non-compliant resources. In this scenario, Azure Policy can be used to automatically enforce the policy that requires all resources to be deployed with a specific set of tags.

 Other options -

 

Azure Security Center: This is a cloud security management service that provides visibility and control over the security of your Azure resources. While it can help enforce some security policies, it is not designed for enforcing resource tags.

 

Azure Advisor: This is a personalized cloud consultant that provides recommendations for optimizing Azure resources for high availability, security, performance, and cost. While it can provide recommendations for tagging resources, it does not enforce policies.

 

Azure Resource Manager: This is the deployment and management service for Azure that provides a way to organize and manage resources in a consistent and predictable manner. While it can be used to deploy resources with tags, it does not enforce policies.

 

Reference: [https://docs.microsoft.com/en-us/azure/governance/policy/](https://docs.microsoft.com/en-us/azure/governance/policy/)

#### Question 67: Correct

Role-based access control is applied to a _________________, which is a resource or set of resources that this access applies to.

- Scope

(Correct)

- Resource Set

- Group

- Blueprint

 

When you have multiple IT and engineering teams, how can you control what access they have to the resources in your cloud environment? It's a good security practice to grant users only the rights they need to perform their job, and only to the relevant resources.

Instead of defining the detailed access requirements for each individual, and then updating access requirements when new resources are created, Azure enables you to control access through [Azure role-based access control](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) (Azure RBAC).

Azure provides built-in roles that describe common access rules for cloud resources. You can also define your own roles. Each role has an associated set of access permissions that relate to that role. When you assign individuals or groups to one or more roles, they receive all of the associated access permissions.

 

Role-based access control is applied to a _scope_, which is a resource or set of resources that this access applies to.

Here's a diagram that shows the relationship between roles and scopes.

 

![](https://docs.microsoft.com/en-ca/learn/azure-fundamentals/build-cloud-governance-strategy-azure/media/4-role-scope-0223bfae.png)

 

Scopes include:

- A management group (a collection of multiple subscriptions).

- A single subscription.

- A resource group.

- A single resource.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/2-control-access-azure-rbac](https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/2-control-access-azure-rbac)

#### Question 68: Correct

True or False:

 

An unlimited number of resources can be added to a Subscription.

- True

- False

(Correct)

 

At the beginning of any cloud governance implementation, you identify a cloud organization structure that meets your business needs. This step often involves forming a _cloud center of excellence team_ (also called a _cloud enablement team_ or a _cloud custodian team_). This team is empowered to implement governance practices from a centralized location for the entire organization. 

Teams often start their Azure governance strategy at the subscription level.

 

Subscriptions also have some resource limitations. For example, the maximum number of network Azure ExpressRoute circuits per subscription is 10. Those limits should be considered during your design phase. If you'll need to exceed those limits, you might need to add more subscriptions. If you hit a hard limit maximum, there's no flexibility to increase it.

Management groups are also available to assist with managing subscriptions. A management group manages access, policies, and compliance across multiple Azure subscriptions. You'll learn more about management groups later in this module.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/10-create-subscription-governance-strategy](https://docs.microsoft.com/en-ca/learn/modules/build-cloud-governance-strategy-azure/10-create-subscription-governance-strategy)

#### Question 69: Correct

____________ provides disks for Azure virtual machines. Applications and other services can access and use them as needed, similar to how they would in on-premises scenarios.

- Disk Storage

(Correct)

- SSD Storage

- Blob Storage

- File Storage

 

Disk Storage provides disks for Azure virtual machines. Applications and other services can access and use these disks as needed, similar to how they would in on-premises scenarios. Disk Storage allows data to be persistently stored and accessed from an attached virtual hard disk.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-disk-storage](https://docs.microsoft.com/en-ca/learn/modules/azure-storage-fundamentals/azure-disk-storage)

#### Question 70: Correct

Yes or No:

 

A Social Insurance Number and a Fingerprint scan are valid MFA options for Azure.

- Yes

- No

(Correct)

 

The following forms of verification can be used with Azure Multi-Factor Authentication:

 

Multi-factor authentication provides additional security for your identities by requiring two or more elements to fully authenticate.

 

These elements fall into three categories:

- Something the user knows

This might be an email address and password.

- Something the user has

This might be a code that's sent to the user's mobile phone.

- Something the user is

This is typically some sort of biometric property, such as a fingerprint or face scan that's used on many mobile devices.

 

Reference: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 71: Incorrect

You have deployed Azure File Sync for your organization. One of the interns accidentally deleted some important files on the local file server. How can you recover the deleted files?

- Recover from the Azure File share using Azure Backup

(Correct)

- Restore the files from Azure Blob Storage

- Recover from the local file server's backup

- Use Azure Site Recovery to recover the files

(Incorrect)

The correct answer is Recover from the Azure File share using Azure Backup. When you deploy Azure File Sync, the data is synchronized with Azure Files, and you can create a backup of the file share using Azure Backup. In case of accidental deletion, you can restore the deleted files from the Azure File share backup.

 

Other options -

 

- Recovering from the local file server's backup may be a valid option, but it is not the best solution in the context of Azure File Sync. Azure File Sync keeps a centralized copy of the data in Azure Files, which can be backed up and restored using Azure Backup.

- Azure Site Recovery is a disaster recovery solution and is not intended for file recovery. It is designed to protect virtual machines and physical servers by replicating them to a secondary location, but it is not suitable for restoring individual files.

- Restoring the files from Azure Blob Storage is not relevant because Azure File Sync synchronizes data with Azure Files, not Azure Blob Storage.

 

Reference:  [https://docs.microsoft.com/en-us/azure/backup/backup-afs](https://docs.microsoft.com/en-us/azure/backup/backup-afs)

#### Question 72: Correct

________________ help to enforce organizational standards, to assess compliance at-scale and implementing governance for resource consistency, regulatory compliance, security and management.

 

- Resource Groups

- Resource Locks

- Policies

(Correct)

- Templates

 

Azure Policy helps to enforce organizational standards and to assess compliance at-scale. Through its compliance dashboard, it provides an aggregated view to evaluate the overall state of the environment, with the ability to drill down to the per-resource, per-policy granularity. It also helps to bring your resources to compliance through bulk remediation for existing resources and automatic remediation for new resources.

 

Common use cases for Azure Policy include implementing governance for resource consistency, regulatory compliance, security, cost, and management. Policy definitions for these common use cases are already available in your Azure environment as built-ins to help you get started.

 

Reference: [https://docs.microsoft.com/en-us/azure/governance/policy/overview](https://docs.microsoft.com/en-us/azure/governance/policy/overview)

#### Question 73: Correct

In Azure, subscriptions serve as a unit of:

- All of the above

(Correct)

- Management

- Scale

- Billing

The correct answer is All of the Above.

 

In Azure, subscriptions serve as a unit of management, billing, and scale. They help you organize your resource groups, manage access to resources, and facilitate billing for the resources used in Azure.

 

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)

#### Question 74: Correct

A startup has deployed a set of Virtual Machines which are critical for their day-to-day operations. They need to ensure their availability even if a single data center goes down. An intern suggests deploying the Virtual Machines to at least two regions.

 

Would this suggestion meet the goal?

- No

- Yes

(Correct)

 

By deploying the virtual machines to two or more regions, you are deploying the virtual machines to multiple datacenters. This will ensure that the services running on the virtual machines are available if a single data center fails.

 

Azure operates in multiple datacenters around the world. These datacenters are grouped in to geographic regions, giving you flexibility in choosing where to build your applications. You create Azure resources in defined geographic regions like 'West US', 'North Europe', or 'Southeast Asia'. You can review the list of regions and their locations.

 

Within each region, multiple datacenters exist to provide for redundancy and availability.

 

Reference: [https://docs.microsoft.com/en-us/azure/virtual-machines/windows/regions](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/regions)

#### Question 75: Incorrect

When creating a private endpoint, which of the following components needs to be configured to enable private connectivity?

- Public IP address 

(Incorrect)

- Network Security Group (NSG) 

- Private DNS zone

(Correct)

- Azure Active Directory (Azure AD)

To enable private connectivity via a private endpoint, you need to configure a Private DNS zone. This Private DNS zone allows you to resolve the hostname of the private endpoint to its private IP address within your virtual network.

 

Reference: [https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-endpoints](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-networking-endpoints)

#### Question 76: Correct

A __________________ contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources.

- Network security group (NSG)

(Correct)

- Network gateway

- Domain Name Service

- Route filter

 

You can use an Azure network security group to filter network traffic to and from Azure resources in an Azure virtual network. A network security group contains [security rules](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview#security-rules) that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources. For each rule, you can specify source and destination, port, and protocol.

 

Network security group security rules are evaluated by priority using the 5-tuple information (source, source port, destination, destination port, and protocol) to allow or deny the traffic. A flow record is created for existing connections. Communication is allowed or denied based on the connection state of the flow record. The flow record allows a network security group to be stateful. If you specify an outbound security rule to any address over port 80, for example, it's not necessary to specify an inbound security rule for the response to the outbound traffic. You only need to specify an inbound security rule if communication is initiated externally. The opposite is also true. If inbound traffic is allowed over a port, it's not necessary to specify an outbound security rule to respond to traffic over the port.

 

Reference: [https://docs.microsoft.com/en-us/azure/virtual-network/security-overview](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)

#### Question 77: Incorrect

A startup is planning to replace or supplement traditional on-premises network-attached storage (NAS) devices. More importantly, they are looking for a solution that supports multiple Operating Systems, and containerization.

 

Which of the following would you recommend?

- Azure Files

(Correct)

- Azure Container Instances

- Azure Blob Storage

- Azure Table Storage

- Azure Data Lake Storage Gen2

- Azure Kubernetes

(Incorrect)

 

Azure Files offers fully managed file shares in the cloud that are accessible via the industry standard [Server Message Block (SMB) protocol](https://docs.microsoft.com/en-us/windows/win32/fileio/microsoft-smb-protocol-and-cifs-protocol-overview), [Network File System (NFS) protocol](https://en.wikipedia.org/wiki/Network_File_System), and [Azure Files REST API](https://docs.microsoft.com/en-us/rest/api/storageservices/file-service-rest-api). Azure file shares can be mounted concurrently by cloud or on-premises deployments. SMB Azure file shares are accessible from Windows, Linux, and macOS clients. NFS Azure file shares are accessible from Linux or macOS clients. Additionally, SMB Azure file shares can be cached on Windows servers with [Azure File Sync](https://docs.microsoft.com/en-us/azure/storage/file-sync/file-sync-introduction) for fast access near where the data is being used.

 

Containerization:

 Azure file shares can be used as persistent volumes for stateful containers. Containers deliver "build once, run anywhere" capabilities that enable developers to accelerate innovation. For the containers that access raw data at every start, a shared file system is required to allow these containers to access the file system no matter which instance they run on.

 

Reference: [https://docs.microsoft.com/en-us/azure/storage/files/storage-files-introduction](https://docs.microsoft.com/en-us/azure/storage/files/storage-files-introduction)

#### Question 78: Correct

Which of the following is NOT a valid way to purchase Azure Services?

- Through an Enterprise Agreement

- Through any 3rd Party Vendor

(Correct)

- Directly from the Web

- Through a Cloud Solution Provider

 

There are three main ways to purchase services on Azure. They are:

 

- Through an Enterprise Agreement

Larger customers, known as enterprise customers, can sign an Enterprise Agreement with Microsoft. This agreement commits them to spending a predetermined amount on Azure services over a period of three years. The service fee is typically paid annually. As an Enterprise Agreement customer, you'll receive the best customized pricing based on the kinds and amounts of services you plan on using.

- Directly from the web

Here, you can purchase Azure services directly from the Azure portal website and pay standard prices. You're billed monthly, either as a credit card payment or through an invoice. This purchasing method is known as Web Direct.

- Through a Cloud Solution Provider

A Cloud Solution Provider (CSP) is a Microsoft Partner that helps you build solutions on top of Azure. Your CSP bills you for your Azure usage at a price they determine. They also answer your support #### Questions and escalate them to Microsoft, as needed.

 

Reference: [https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/4-purchase-azure-services](https://docs.microsoft.com/en-ca/learn/modules/plan-manage-azure-costs/4-purchase-azure-services)

#### Question 79: Correct

Which aspect of data management does Microsoft Purview primarily address?

- Data migration between Azure regions.

- Data discovery, classification, and governance.

(Correct)

- Data storage optimization.

- Data transformation for analytics purposes.

Microsoft Purview focuses on data discovery, classification, and governance. It helps organizations understand what data they have, where it resides, and how it's being used. It also provides tools for classifying and protecting sensitive data, ensuring compliance with data regulations.

 

Reference: [https://azure.microsoft.com/en-ca/products/purview](https://azure.microsoft.com/en-ca/products/purview)

#### Question 80: Correct

What are the basic building block of Azure?

- Resources

(Correct)

- Management groups

- Subscriptions

- Resource groups

Resources are the basic building blocks of Azure. Anything you create, provision, deploy, etc. is a resource. Virtual Machines (VMs), virtual networks, databases, cognitive services, etc. are all considered resources within Azure.

 

Other options -

 

- Resource groups are logical containers for resources deployed within an Azure subscription. They do not represent the individual components created in Azure.

- Subscriptions are a unit of management, billing, and scale in Azure. They are used to organize resource groups and facilitate billing but are not the basic building blocks themselves.

- Management groups are a higher-level organizational structure used to manage access, policies, and compliance for multiple subscriptions. They are not the basic building blocks of Azure.

Reference: [https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)

#### Question 81: Incorrect

Your IT teams need to quickly locate resources associated with specific workloads, environments, ownership groups, or other important information.  Which of the following can you recommend?

- Tags

(Correct)

- Policies

- Azure Advisor

(Incorrect)

- Azure Security Center

- Blueprints

 

Organizing cloud-based resources is a crucial task for IT, unless you only have simple deployments. Use naming and tagging standards to organize your resources for the following reasons:

 

- Resource management: Your IT teams need to quickly locate resources associated with specific workloads, environments, ownership groups, or other important information. Organizing resources is critical to assigning organizational roles and access permissions for resource management.

- Operations management: Visibility for the operations management team about business commitments and SLAs is an important aspect of ongoing operations. For operations to be managed well, tagging for [mission criticality](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/manage/considerations/criticality) is required.

- Security: Classification of data and security impact is a vital data point for the team, when breaches or other security issues arise. To operate securely, tagging for [data classification](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/govern/policy-compliance/data-classification) is required.

 

Reference: [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/resource-tagging/?toc=%2Fazure%2Fazure-resource-manager%2Fmanagement%2Ftoc.json)

#### Question 82: Correct

Which of the following best describes the relationship between an ARM template and Azure resources?

- An ARM template is a virtual machine template.

- An ARM template is a resource type in Azure.

- An ARM template is another name for Resource Groups and provides direct access to Azure data centers.

- An ARM template defines the desired state of Azure resources and their configuration.

(Correct)

An ARM template is used to declare the desired configuration of Azure resources. It defines the properties, settings, and dependencies of resources in order to achieve a specific deployment.

 

Reference: [https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/overview)

#### Question 83: Incorrect

Which of the following solutions is the BEST to store web app user data, device information and  other metadata?

- Azure Cache for Redis

- Azure Cosmos DB

(Incorrect)

- Azure SQL Database

- Azure Table Storage

(Correct)

According to the official  Azure documentation : 

![](https://img-c.udemycdn.com/redactor/raw/2020-05-29_19-01-05-4b933927820cdc634f4dd1d1fd5975e6.png)

Reference : [https://azure.microsoft.com/en-us/services/storage/tables/#overview](https://azure.microsoft.com/en-us/services/storage/tables/#overview)

#### Question 84: Correct

A startup is planning to use multiple Azure SQL Databases. Which of the following will help them to reduce costs if the databases have unpredicatable usage demands?

- Elastic Pools

(Correct)

- Azure Policies

- Azure Blueprints

- Scale Sets

Just like Azure VM Scale Sets are best friends with Azure VMs, for Azure SQL Databases, we have Azure SQL Database elastic pools . These are a simple, cost-effective solution for managing and scaling multiple databases that have varying and unpredictable usage demands. The databases in an elastic pool are on a single server and share a set number of resources at a set price.

 

Elastic pools in Azure SQL Database enable SaaS developers to optimize the price performance for a group of databases within a prescribed budget while delivering performance elasticity for each database.

 

Reference: [https://docs.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview](https://docs.microsoft.com/en-us/azure/azure-sql/database/elastic-pool-overview)

#### Question 85: Correct

Which of the following is an accurate definition of an Azure Policy Initiative?

- A type of virtual machine used for hosting policies in the Azure cloud.

- An Azure service that provides real-time monitoring of policy enforcement.

- A set of policy definitions that are applied individually for easy management and assignment.

- A way to package and deploy a collection of policy definitions as a single entity.

(Correct)

The correct answer is : A way to package and deploy a collection of policy definitions as a single entity. An initiative definition is a group of policy definitions that are designed to achieve a specific objective. The purpose of initiative definitions is to streamline the management and assignment of policy definitions by grouping them together as a single entity. An example of an initiative could be "Enable Monitoring in Microsoft Defender for Cloud," which aims to monitor all the available security recommendations in a Microsoft Defender for Cloud instance.

 

Other options -

 

- A set of policy definitions that are applied individually for easy management and assignment: This option describes the individual policy definitions, which are the building blocks of an Azure Policy initiative. However, it does not accurately describe an Azure Policy initiative as a whole.

- A type of virtual machine used for hosting policies in the Azure cloud: This option describes a virtual machine, which is not related to an Azure Policy initiative. An Azure Policy initiative is a way to package and deploy a collection of policy definitions, and is not a virtual machine.

- An Azure service that provides real-time monitoring of policy enforcement: This option describes a service for monitoring policy enforcement, which is not the same as an Azure Policy initiative. While an Azure Policy initiative can enforce policies, it is not a monitoring service.

 

Reference: [https://learn.microsoft.com/en-us/azure/governance/policy/overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview)
