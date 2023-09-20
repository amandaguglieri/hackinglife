---
title: Exams - Practice the AZ-900
TableOfContents: 
date: 2022-10-29T00:00:00Z
author: amandaguglieri
tags:
  - certification
  - cloud
  - azure
  - microsoft
  - az-900
---

# Exams - Practice the AZ-900
## Questions from courses

#### Question:  @@@@  is a set of tools that organizations can use to monitor, allocate, and optimize Azure costs.

- The Azure Pricing Calculator
- The TCO Calculator
- Azure Cost Management

#### Question: Organizations can use @@@@  to manage governance across multiple Azure subscriptions.

- Azure Initiatives
- Resource Groups
- Management Groups

#### Question: @@@@ are used by organizations to define performance targets (i.e. uptime) for Azure products and services.

- Support Plans
- Service Level Agreements
- Usage Meters

#### Question: A(n)  @@@@@ is a logical collection of Azure services that links to an Azure account.

- Resource Group
- Management Group
- Azure Subscription

#### Question: The @@@ support plan does not offer 24x7 access to Support Engineers by email and phone.

- Standard
- Developer
- Professional Direct


#### Question: If an organization @@@@, it can take advantage of discounted pricing through Azure Reservations offers.

- defines spending limits
- provisions at least 25 resources
- pays for resources in advance


#### Question: Which of the following give all Azure customers a chance to test beta and other pre-release features?

- General Availability
- Private Preview
- Public Preview

#### Question: When a product or feature is released to all Azure customers, it's considered to be in @@@@@.

- Public Preview
- General Preview    
- General Availability


## Exams from "Course AZ-900: Microsoft Azure Fundamentals Original Practice Tests"

Exams from the Udemy course [AZ-900: Microsoft Azure Fundamentals Original Practice Tests](https://www.udemy.com/course/az900-azure-tests/).
### Test 1
#### Question 1: Which Azure feature is specifically designed to help companies get their in-house developed code from the code repository, through automated unit testing, and onto Azure using a service called Pipelines?

- Azure Monitor
- GitHub
- Azure DevOps
- Virtual Machines

**Explanation**: Azure DevOps contains many services, one of which is Pipelines. Pipelines allows you to build an automation that moves code (and all related dependencies) through various stages from the development environment into deployment.

#### Question 2: True or false: there are no service level guarantees (SLA) when a service is in General Availability (GA)

- FALSE
- TRUE

**Explanation**: False, most Azure GA services do have service level agreements. See: [https://azure.microsoft.com/en-ca/support/legal/sla/](https://azure.microsoft.com/en-ca/support/legal/sla/)

#### Question 3: Which ways does the Azure Resource Manager model provide to deploy resources?

- CLI
- Powershell
- Azure Portal
- REST API / SDK

**Explanation**: Azure Resource Manager (ARM) is the deployment and management service for Azure. It provides a management layer that enables you to create, update, and delete resources in your Azure account. The ARM model allows you to work with resources in a consistent manner, whether through Azure portal, PowerShell, REST APIs/SDKs, or the Command-Line Interface (CLI).
 
1. Azure Portal: This is a web-based, unified console that provides an alternative to command-line tools. You can manage your Azure resources directly through a GUI.
 
2. PowerShell: Azure PowerShell is a module that provides cmdlets to manage Azure through Windows PowerShell and PowerShell Core. You can use it to build scripts for managing and automating your Azure resources.

3. REST API / SDK: Azure provides comprehensive REST APIs that can be used directly or via Azure SDKs available in multiple languages. This allows developers to integrate Azure services in their applications, services, or tools.

4. CLI: Azure CLI is a cross-platform command-line program that connects to Azure and executes administrative commands on Azure resources. It's designed to make scripting easy, authenticate with Azure platform, and quickly run commands to perform common administrative tasks or deploy to Azure.


Each of these methods supports the full set of Azure Resource Manager features, and you can choose the one that best fits your workflow. See: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

#### Question 4: What type of container is used to collect log and metric data from various Azure Resources?

- Log Analytics Workspace
- Managed Storage
- Append Blob Storage
- Azure Monitor account

**Explanation**: Log Analytics Workspace is required to collect logs and metrics. See: [https://docs.microsoft.com/en-us/azure/azure-monitor/platform/manage-access](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/manage-access)

#### Question 5: Which Azure service is meant to be a security dashboard that contains all the security and threat protection in one place?

- Azure Portal Dashboard    
- Azure Security Center
- Azure Key Vault  
- Azure Monitor

**Explanation**: Azure Security Center - unified security management and threat protection; a security dashboard inside Azure Portal. See: [https://azure.microsoft.com/en-us/services/security-center/](https://azure.microsoft.com/en-us/services/security-center/)

#### Question 6: What is a DDoS attack?

- A denial of service attack that sends so much traffic to a network that it cannot respond fast enough; legitimate users become unable to use the service
- An attempt to read the contents of a web page from another website, thereby stealing the user's private information
- An attempt to send SQL commands to the server in a way that it will execute them against the database
- An attempt to guess a user's password through brute force methods
   
**Explanation**: Distributed Denial of Service attacks (DDoS) -a type of attack that originates from the Internet that attempts to overwhelm a network with millions of packets of bad traffic that aims to prevent legitimate traffic from getting through. See: [https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview](https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview)

#### Question 7: In the context of cloud computing and Azure services, how would you define 'compute resources'?

- They include all resources listed in the Azure Marketplace.
- They are resources that execute tasks requiring CPU cycles.
- They refer exclusively to Virtual Machines.
- They encompass Virtual Machines, Storage Accounts, and Virtual Networks.

**Explanation**: The correct answer is "They are resources that execute tasks requiring CPU cycles". In cloud computing, the term "compute" refers to the amount of computational power required to process a task - essentially, it's anything that uses processing power (CPU cycles) to perform operations. This includes, but is not limited to, running applications, executing scripts, and processing data. While virtual machines (VMs) are a common type of compute resource, they are not the only type. Azure offers a wide variety of compute resources, like Azure Functions for serverless computing, Azure Kubernetes Service for container-based applications, and Azure Batch for parallel and high-performance computing tasks. So, the definition of compute resources is broader than just VMs or certain resources listed in the Azure Marketplace. It also includes more than VMs, Storage Accounts, and Virtual Networks, as these other resources (storage and networking) have distinct roles separate from the compute resources. Storage accounts deal with data storage while virtual networks are concerned with networking aspects in Azure, not with performing tasks that require CPU cycles. Therefore, "They are resources that execute tasks requiring CPU cycles" is the most accurate answer. See: [https://azure.microsoft.com/en-us/product-categories/compute/](https://azure.microsoft.com/en-us/product-categories/compute/)

#### Question 8: Which Azure Service contains pre-built machine learning models that you can use in your own code, using an API?

- Cognitive Services
- Azure Functions
- Azure Blueprints
- App Services

**Explanation**: Cognitive Services is an API that Azure provides, that gives access to a set of pre-built machine learning models including vision services, speech services, knowledge management and chat bots.

#### Question 9: In Microsoft Azure, what is the maximum number of virtual machines that can be included in a single Virtual Machine Scale Set, as per Azure's standard guidelines and capabilities?

- 10000
- 1000
- Unlimited
- 500

**Explanation**: The correct answer is 1000. Azure Virtual Machine Scale Sets are a service provided by Azure that allows you to manage, scale, and distribute large numbers of identical virtual machines. As per the limitations set by Microsoft Azure, a single Virtual Machine Scale Set can support up to 1000 VM instances. This capacity allows for high availability and network load balancing across a large number of virtual machines, providing a robust and efficient solution for applications that require heavy compute resources. However, if you are using custom VM images, this limit decreases to 600 instances. This functionality is part of Azure's Infrastructure as a Service (IaaS) offerings, providing flexibility and scalability to businesses and developers. See: [https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview)

#### Question 10: What feature within Azure will make recommendations to you about reducing cost on your account?

- Azure Service Health
- Azure Security Center
- Azure Advisor
- Azure Dashboard  

**Explanation**: Azure Advisor analyzes your account usage and makes recommendations for you based on its set rules. See: [https://docs.microsoft.com/en-us/azure/advisor/advisor-overview](https://docs.microsoft.com/en-us/azure/advisor/advisor-overview)

#### Question 11: Your organization has implemented an Azure Policy that restricts the type of Virtual Machine instances you can use. How can you create a VM that is blocked by the policy?

- Use an account that has Contributor or above permissions to the resource group
- Subscription Owners (Administrators) can create resources regardless of what the policy restricts
- The only way is to remove the policy, create the resource and add the policy back

**Explanation**:  You cannot perform a task that violates policy, so you have to remove the policy in order to perform the task. See: [https://docs.microsoft.com/en-us/azure/governance/policy/overview](https://docs.microsoft.com/en-us/azure/governance/policy/overview)

#### Question 12: You have decided to subscribe to Azure DDoS Protection at the IP Protection Tier. This provides advanced protection to defend against DDoS attacks. What type of DDoS attack does DDoS Protection NOT protect against?

- Transport (L4) level attacks
- Application (L7) level attacks
- Network (L3) level attacks

**Explanation**: The correct answer is "Application level attacks": 

- **Network-level attacks** are attacks that target the network infrastructure, such as the routers and switches that connect your Azure resources to the internet. Azure DDoS Protection IP Protection Tier can protect against network-level attacks by absorbing and rerouting excessive traffic, and by scrubbing malicious traffic.
    
- **Transport-level attacks** are attacks that target the transport layer of the network protocol stack, such as TCP and UDP. Azure DDoS Protection IP Protection Tier can protect against transport-level attacks by absorbing and rerouting excessive traffic, and by scrubbing malicious traffic.
    
- **Application-level attacks** are attacks that target the application layer of the network protocol stack, such as HTTP and DNS. Azure DDoS Protection IP Protection Tier **does not** protect against application-level attacks, because it is designed to protect against network and transport-level attacks.
    
To protect against application-level attacks, you need to use a web application firewall (WAF). A WAF is a software appliance that sits in front of your application and filters out malicious traffic. WAFs can be configured to protect against a wide variety of application-level attacks, such as SQL injection, cross-site scripting, and denial of service attacks. See: [https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview](https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview)

#### Question 13: Which of the following characteristics of a cloud-based system primarily contributes to its elasticity?

- The system's ability to recover automatically after a crash.
- The system's ability to dynamically increase and decrease capacity based on real-time demand.
- The system's ability to maintain availability while updates are being implemented.
- The system's ability to withstand denial-of-service attacks.

**Explanation**:  The correct answer is "The ability to increase and reduce capacity based on actual demand." This characteristic refers to the concept of **elasticity** in cloud computing. An elastic system **is one that can automatically adjust its resources** (compute, storage, etc.) in response to changing workloads and demands. This is done to ensure optimal performance and cost-effectiveness. When demand increases, the system can scale out by adding more resources, and when demand decreases, it can scale in by reducing resources, all without significant manual intervention. The other options, while important for overall system robustness, do not define elasticity. Withstanding denial of service attacks pertains to security, maintaining availability during updates refers to zero-downtime deployment or high availability, and self-healing after a crash refers to resilience or fault tolerance. None of these are about dynamically adjusting capacity based on demand, which is the hallmark of an elastic system. See: [https://azure.microsoft.com/en-us/overview/what-is-elastic-computing/](https://azure.microsoft.com/en-us/overview/what-is-elastic-computing/)

#### Question 14: Logic apps, functions, and service fabric are all examples of what model of compute within Azure?

- SaaS model
- App Services Model
- IaaS model
- Serverless model

**Explanation**: The correct answer is the Serverless model. Azure Logic Apps, Azure Functions, and Azure Service Fabric are all examples of serverless computing in Azure. Serverless computing is a cloud computing model where the cloud provider automatically manages the provisioning and allocation of servers, hence the term "serverless". The serverless model allows developers to focus on writing the code and business logic rather than worrying about the underlying infrastructure, its setup, maintenance, scaling, and capacity planning. 

- Azure Logic Apps is a cloud service that allows developers to build workflows that integrate apps, data, services, and systems. 
- Azure Functions is an event-driven, compute-on-demand experience that extends the existing Azure application platform with capabilities to implement code triggered by events occurring in Azure or third-party services. 
- Azure Service Fabric is a distributed systems platform that makes it easy to package, deploy, and manage scalable and reliable microservices.

In contrast, IaaS (Infrastructure as a Service) refers to cloud-based services where you rent IT infrastructure—servers and virtual machines (VMs), storage, networks, and operating systems—from a cloud provider on a pay-as-you-go basis. SaaS (Software as a Service) is a software distribution model in which a third-party provider hosts applications and makes them available to customers over the Internet, which doesn't align with the services mentioned in the question. The App Services model is a platform for hosting web applications, REST APIs, and mobile backends, but it's not strictly serverless as it doesn't auto-scale in the same way. See: [https://azure.microsoft.com/en-us/solutions/serverless/](https://azure.microsoft.com/en-us/solutions/serverless/)

#### Question 15: What is a primary benefit of opting for a consumption-based pricing model over a time-based pricing model in cloud services?

- The ability to easily predict the future cost of the service.
- It always being cheaper to pay for consumption rather than paying hourly.
- Significant cost savings when the resources aren't needed for constant use.
- A simpler and easier-to-understand pricing model.

**Explanation**: The correct answer is "Significant cost savings when the resources aren't needed for constant use". In a consumption-based pricing model, also known as pay-as-you-go, customers are billed only for the specific resources they use. This model provides cost-efficiency for workloads with variable usage patterns or for resources that aren't needed continuously.

When compared to a time-based pricing model, where resources are billed on a fixed schedule regardless of actual use (for example, hourly or monthly), consumption-based pricing can result in significant cost savings if the resources are not used often or their usage fluctuates.

While the other options can be true in certain cases, they aren't inherently beneficial aspects of the consumption-based model. The cost predictability can be challenging due to the variable nature of usage (Answer 1), it's not always cheaper (Answer 2) as it depends on the resource usage pattern, and the simplicity of the pricing model (Answer 4) depends on the specific terms and conditions of the service provider. Therefore, the most accurate and generalizable benefit is the potential for cost savings with infrequent or variable resource use. See: [https://docs.microsoft.com/en-us/azure/azure-functions/functions-consumption-costs](https://docs.microsoft.com/en-us/azure/azure-functions/functions-consumption-costs)

#### Question 16: In Microsoft Azure, which tool or service allows for the organization and management of multiple subscriptions within hierarchical structures?

- RBAC (Role-Based Access Control)
- Management Groups
- Azure Active Directory
- Resource Groups

**Explanation**:  The correct answer is **Management Groups**. In Azure, Management Groups provide a way to manage access, policies, and compliance for multiple subscriptions. They can be structured into a hierarchy for the organization's needs. All subscriptions within a Management Group automatically inherit the conditions applied to the Management Group, facilitating governance on a large scale.

**Resource Groups**, on the other hand, are containers for resources deployed on Azure. They do not provide management capabilities across multiple subscriptions.

**RBAC (Role-Based Access Control)** is a system that provides fine-grained access management to Azure resources but it doesn't inherently support the organization of subscriptions into hierarchies.

**Azure Active Directory** is a service that provides identity and access management capabilities but does not provide a direct mechanism for managing multiple subscriptions in nested hierarchies.

Hence, Management Groups is the correct answer as it directly allows for the management and organization of multiple subscriptions into nested hierarchies, which the other options do not. See: [https://docs.microsoft.com/en-us/azure/governance/management-groups/overview](https://docs.microsoft.com/en-us/azure/governance/management-groups/overview)

#### Question 17: Which feature of Azure Active Directory will require users to have their mobile phone in order to be able to log in?

- Azure Security Center
- Multi-Factor Authentication
- Azure Information Protection (AIP)
- Advanced Threat Protection (ATP)
    

**Explanation**: Multi-Factor Authentication (MFA) - the concept of having something additional to a “password” that is required to log in; passwords are find-able or guessable; but having your mobile phone on you to receive a phone call, text or run an app to get a code is harder for an unknown hacker to get. See: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 18: Who is responsible for the security of the physical servers in an Azure data center?

- Azure is responsible for securing the physical data centers
- I am responsible for securing the physical data centers

**Explanation**: Azure is responsible for physical security. See: [https://docs.microsoft.com/en-us/azure/security/fundamentals/physical-security](https://docs.microsoft.com/en-us/azure/security/fundamentals/physical-security)

#### Question 19: True or False: Azure is a public cloud, and has no private cloud offerings

- TRUE
- FALSE

**Explanation**: The correct answer is FALSE. While Azure is indeed widely recognized as a public cloud provider, offering a vast array of services accessible via the internet on a multi-tenant basis, it does also provide private cloud capabilities. One notable offering is Azure Stack, an extension of Azure that allows businesses to run apps in an on-premises environment and deliver Azure services in their datacenter. With Azure Stack, you get the flexibility of using Azure’s cloud capabilities while maintaining your own datacenter for privacy, regulatory compliance, or other requirements. Additionally, Azure offers services such as Azure Private Link, which provides private connectivity from a virtual network to Azure services, and Azure ExpressRoute, a service that enables a private, dedicated network connection to Azure. So, contrary to the statement, Azure does have private cloud offerings along with its public cloud, making the statement FALSE. See: 

- [https://azure.microsoft.com/en-us/overview/what-is-a-private-cloud/](https://azure.microsoft.com/en-us/overview/what-is-a-private-cloud/)
- [https://azure.microsoft.com/en-us/global-infrastructure/government/](https://azure.microsoft.com/en-us/global-infrastructure/government/)
- [https://azure.microsoft.com/en-us/overview/azure-stack/](https://azure.microsoft.com/en-us/overview/azure-stack/)

#### Question 20: Who is responsible for the security of your Azure Storage account access keys?

- Azure is responsible for securing the access keys
- I am responsible for securing the access keys
   

**Explanation**: Customers are responsible to secure the access keys they are given and regenerate them if they are exposed. See: [https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

#### Question 21: Which feature within Azure collects all of the logs from various resources into a central dashboard, where you can run queries, view graphs, and create alerts on certain events?

- Azure Portal Dashboard
- Azure Monitor
- Azure Security Center
- Storage Account or Event Hub


**Explanation**: Azure Monitor - a centralized dashboard that collects all the logs, metrics and events from your resources. See: [https://docs.microsoft.com/en-us/azure/azure-monitor/overview](https://docs.microsoft.com/en-us/azure/azure-monitor/overview)

#### Question 22: When establishing a Site-to-Site VPN connection with Azure, what kind of network device needs to be present or installed in your company's on-premises network infrastructure?

- An Azure Virtual Network
- An Application Gateway
- A dedicated virtual machine
- A compatible VPN Gateway device

**Explanation**: The correct answer is a compatible VPN Gateway device. In order to establish a site-to-site VPN connection with Azure, a VPN Gateway is required on your company's internal network. A VPN Gateway is a specific type of virtual network gateway that sends encrypted traffic across a public network, like the Internet. While the name might suggest it's a purely virtual entity, in practice, the term "VPN Gateway" often refers to a hardware device that's installed on-premises in your data center. This device uses Internet Protocol security (IPsec) to establish a secure, encrypted connection to the Azure VPN Gateway, which resides in the Azure virtual network. This setup allows your local network and Azure to interact as if they're directly connected. In contrast, virtual machines, virtual networks, and application gateways are other types of Azure resources, but they do not facilitate creating a site-to-site VPN connection. It's important to note that your company's internal network hardware and settings must meet specific requirements to support a VPN Gateway. See: [https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-howto-site-to-site-resource-manager-portal)

#### Question 23: Which of the following is something that Azure Cognitive Services API can currently do?

- Translate text from one language to another
- All of these! Azure can do it all!
- Speak text in an extremely realistic way
- Create text from audio
- Recognize text in an image

**Explanation**: Azure can do all of them, of course. See: [https://docs.microsoft.com/en-us/azure/cognitive-services/welcome](https://docs.microsoft.com/en-us/azure/cognitive-services/welcome)

#### Question 24: Which of the following Azure features is most likely to deliver the most immediate savings when it comes to reducing Azure costs?

- Changing your storage accounts from globally redundant (GRS) to locally redundant (LRS)
- Auto shutdown of development and QA servers over night and on weekends    
- Using Azure Reserved Instances for most of your virtual machines
- Using Azure Policy to restrict the user of expensive VM SKUs

**Explanation**:  Reserved Instances often offer 40% or more savings off of the price of pay-as-you-go virtual machines. See: [https://docs.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations](https://docs.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations)

#### Question 25: In the context of Azure's high availability solutions, what is the primary purpose of Azure Availability Zones?

- They serve as a folder structure in Azure used for organizing resources such as databases, virtual machines, and virtual networks.
- They are synonymous with an Azure region.
- They allow manual selection of data centers for virtual machine placement to achieve superior availability compared to other options.
- They represent certain server racks within individual data centers, specifically designed by Azure for higher uptime.

**Explanation**:  The correct answer is: "They allow manual selection of data centers for virtual machine placement to achieve superior availability compared to other options." 

Azure Availability Zones are a high availability offering that protects applications and data from datacenter failures. Each Azure region is composed of multiple datacenters, and each datacenter is essentially an Availability Zone. They are unique physical locations within a region, equipped with their own independent power, cooling, and networking. By placing your resources across different Availability Zones within a region, you can protect your apps and data from the failure of a single datacenter. If one datacenter goes down, the resources in the other datacenters (Availability Zones) can continue to operate, providing redundancy and increasing the overall availability of your applications. It's important to note that these zones are not the same as Azure regions (which are geographical areas containing one or more datacenters), nor are they equivalent to resource groups (which are logical containers for resources deployed on Azure). They are also not isolated to specific racks within a datacenter, but rather spread across different datacenters in a region, offering a broader scope of protection.  See: [https://docs.microsoft.com/en-us/azure/availability-zones/az-overview](https://docs.microsoft.com/en-us/azure/availability-zones/az-overview)

#### Question 26: Which of the following characteristics is essential for a system to be considered highly available in a cloud computing environment?

- The system must maintain 100% availability at all times.
- The system must be designed for resilience, with no single points of failure.
- It's impossible to create a highly available system.
- The system must operate on a minimum of two virtual machines.

**Explanation**: The correct answer is "A system specifically designed to be resilient, with no single point of failures". High availability in a system means that it is designed to operate continuously without failure for a long period of time. This is achieved by building redundancy into the system, eliminating single points of failure, and enabling rapid recovery from any failures that do occur. In other words, even if a component of the system fails, there are other components that can take over, allowing the system to continue operating seamlessly. While high availability often aims for close to 100% uptime, the claim of maintaining 100% availability is practically unrealistic due to factors like maintenance needs and unexpected failures. Also, having a minimum of two VMs may contribute to high availability but isn't a definitive requirement — it depends on the specifics of the system architecture. Finally, the assertion that it's not possible to create a highly available system is incorrect. There are established strategies and technologies for designing and operating highly available systems, and they are widely used in mission-critical applications across many industries. See: [https://docs.microsoft.com/en-us/azure/virtual-machines/windows/availability](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/availability)

#### Question 27: In the context of cloud computing, how is the benefit of 'agility' best described?

- It refers to the ability to swiftly recover from a large-scale regional failure.
- It refers to the ability to quickly respond to and drive changes in the market.
- It refers to the system's ability to easily scale up when it reaches full capacity.
- It refers to the ability to rapidly provision new resources.

**Explanation**:  The correct answer is "It refers to the ability to quickly respond to and drive changes in the market". Agility, in the context of cloud computing, refers to the ability of an organization to rapidly adapt to market and environmental changes in productive and cost-effective ways. It involves quickly adjusting and adapting strategic and operational capabilities to respond to and take advantage of changes in the business environment. The other options, while also benefits of the cloud, do not directly align with the concept of agility. Spinning up new resources quickly (Answer 2) or growing capacity easily when full (Answer 3) relate more to the cloud's scalability and elasticity. The ability to recover from a region-wide failure rapidly (Answer 4) speaks to the cloud's resilience and disaster recovery capabilities. While these aspects can contribute to overall business agility, they don't encapsulate the broader strategic meaning of agility - the capacity to quickly adjust to market changes, which can include shifts in customer demand, competitive pressures, or regulatory changes, among others. Hence, the ability to respond to and drive market change quickly is the most accurate answer. See: [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/agility-outcomes](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/agility-outcomes)

#### Question 28: If you wanted to simply use Azure as an extension of your own datacenter, not primarily hosting anything there but using it for extra storage or taking advantage of some services, what hosting model is that called?

- Public cloud
- Hybrid cloud
- Private cloud

**Explanation**: The correct answer is "Hybrid cloud." The scenario described in the question is a typical use case for a hybrid cloud model, which integrates private cloud or on-premises infrastructure with public cloud resources, such as those provided by Azure. In a hybrid cloud model, businesses can keep sensitive data or critical applications on their private cloud or on-premises datacenter for security and compliance reasons while using the public cloud's vast resources for additional storage, computational power, or specific services when necessary. This not only allows for greater flexibility and scalability, but also offers potential cost savings. In contrast, a purely public cloud model involves hosting all data and applications on a public cloud provider's infrastructure, and a purely private cloud model involves hosting everything on a business's own infrastructure or a rented, single-tenant infrastructure. The described scenario of extending an on-premises datacenter with Azure services fits best with the hybrid cloud model. See: [https://azure.microsoft.com/en-us/overview/what-is-hybrid-cloud-computing/](https://azure.microsoft.com/en-us/overview/what-is-hybrid-cloud-computing/)

#### Question 29: In the context of cloud computing, a virtual machine (VM) is primarily associated with which type of cloud hosting model?

- Software as a Service (SaaS)
- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)

**Explanation**: The correct answer is IaaS, which stands for Infrastructure as a Service. In the context of cloud computing, a virtual machine (VM) is typically provided as part of an IaaS offering. With IaaS, the provider manages the underlying physical infrastructure (like servers, network equipment, and storage), while the consumer controls the virtualized components of the infrastructure, such as the virtual machines, their operating systems, and the applications running on them. This is contrasted with the other options. In a Platform as a Service (PaaS) model, the consumer only controls the applications and possibly some configuration settings for the application-hosting environment, but does not manage the operating system, server hardware, or network infrastructure. Similarly, in a Software as a Service (SaaS) model, the consumer only uses the software and does not control any aspect of the infrastructure or platform where the application runs. Therefore, given that a virtual machine involves control over the operating system and applications within a cloud-managed infrastructure, it aligns with the IaaS hosting model. See: [https://azure.microsoft.com/en-us/overview/what-is-iaas/](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

#### Question 30: Which of the following best describes the primary benefit of a Content Delivery Network (CDN) in a cloud computing context?

- For a nominal fee, Azure will manage your virtual machine, perform OS updates, and ensure optimal performance.
- It mitigates server load for static, unchanging files like images, videos, and PDFs by distributing them across a network of servers.
- It enables temporary session information storage for web visitors, such as their login ID or name.
- It provides fast and inexpensive data retrieval for later use.

**Explanation**:  The correct answer, "It mitigates server load for static, unchanging files", is indeed the core benefit of a Content Delivery Network (CDN). A CDN stores copies of a website's static files on servers distributed globally. These static files could be anything that doesn't change frequently, like images, CSS, JavaScript, videos, etc. When a user visits the site, they are served these static files from the CDN server nearest to them geographically. This reduces the latency, as the data has a shorter distance to travel. Additionally, it reduces the load on the original server because the CDN handles a significant portion of the traffic. As a result, not only is the user experience improved due to faster load times, but the operational efficiency and performance of the original server are also enhanced. Therefore, CDNs are essential for sites serving large amounts of static content to a geographically dispersed user base. See: [https://docs.microsoft.com/en-us/azure/cdn/cdn-overview](https://docs.microsoft.com/en-us/azure/cdn/cdn-overview)

#### Question 31: What is the name of the group of services inside Azure that hosts the Apache Hadoop big data analysis tools?

- Azure Hadoop Services
- Azure Data Factory
- HDInsight
- Azure Kubernetes Services

**Explanation**:  The correct answer is HDInsight. HDInsight is Microsoft Azure's offering for hosting the Apache Hadoop big data analysis tools. Apache Hadoop is an open-source software platform that supports data-intensive distributed applications. This platform enables processing large amounts of data across clusters of computers. Azure HDInsight is a cloud distribution of the Hadoop components from the Hortonworks Data Platform. It allows Azure users to process vast amounts of data with popular open-source frameworks such as Hadoop, Hive, HBase, Storm, and others. Additionally, the HDInsight service also supports R, Python, Scala, and .NET. So, it's not just limited to traditional Hadoop tools. Options like 'Azure Hadoop Services' and 'Azure Data Factory' are incorrect as Azure doesn't have a service named 'Azure Hadoop Services' and 'Azure Data Factory' is a cloud-based data integration service. 'Azure Kubernetes Services' is a service for managing containerized applications, not specifically for Hadoop. See: [https://azure.microsoft.com/en-us/services/hdinsight/](https://azure.microsoft.com/en-us/services/hdinsight/)

#### Question 32: Within the landscape of cloud service models, how would Microsoft's Outlook 365 be best categorized?

- Infrastructure as a Service (IaaS)
- Software as a Service (SaaS)
- Platform as a Service (PaaS)

**Explanation**:  The correct answer is SaaS, which stands for Software as a Service. Outlook 365, part of Microsoft's Office 365 suite, is a cloud-based service that provides access to various applications and services, including email, calendars, and contact management, which are delivered over the internet. In a SaaS model, the service provider is responsible for the infrastructure, platform, and software, and ensures their maintenance and updates. Users simply access the services via a web browser or app, without needing to worry about the underlying infrastructure, platform, or software updates. This contrasts with Infrastructure as a Service (IaaS), where the user is responsible for managing the operating systems, middleware, and applications, and Platform as a Service (PaaS), where the user manages only the applications and data. In both these models, the users have more responsibilities compared to SaaS. Since Outlook 365 is a software application delivered over the web with all underlying infrastructure and platform taken care of by Microsoft, it falls into the SaaS hosting model. See: [https://azure.microsoft.com/en-us/overview/what-is-saas/](https://azure.microsoft.com/en-us/overview/what-is-saas/)

#### Question 33: Which major cloud provider offers the most international locations for customers to provision virtual machines and other servers?

- Microsoft Azure
- Google Cloud Platform
- Amazon AWS

**Explanation**:  Microsoft Azure offers the most extensive global coverage among major cloud providers regarding geographical regions. This allows customers to provision virtual machines, databases, and other services in various international locations closer to their user base, which can enhance performance, reduce latency, and comply with local regulations regarding data residency. While AWS (Amazon Web Services) and GCP (Google Cloud Platform) also provide many regions globally, Microsoft Azure has distinguished itself with the broadest regional availability. See: [https://azure.microsoft.com/en-us/global-infrastructure/regions/](https://azure.microsoft.com/en-us/global-infrastructure/regions/)

#### Question 34: Which Azure website tool is available for you to estimate the future costs of your Azure products and services by adding products to a shopping basket and helping you calculate the costs?

- Azure Pricing Calculator
- Microsoft Docs
- Azure Advisor

**Explanation**: Azure Pricing Calculator lets you attempt to calculate your future bill based on resources you select and your estimates of usage. See: [https://azure.microsoft.com/en-us/pricing/calculator/](https://azure.microsoft.com/en-us/pricing/calculator/)

#### Question 35: What is the name of Azure's hosted SQL database service?

- SQL Server in a VM
- Table Storage
- Cosmos DB
- Azure SQL Database

**Explanation**:  SQL Database is a SQL Server compatible option in Azure, a database as a service. See: [https://docs.microsoft.com/en-us/azure/sql-database/sql-database-technical-overview](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-technical-overview)

#### Question 36: True or false: You cannot have more than one Azure subscription per company

- TRUE
- FALSE

**Explanation**:  You can have multiple subscriptions, as a way to separate out resources between billing units, business groups, or for any reason you wish. See: [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/subscriptions/](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/decision-guides/subscriptions/)

#### Question 37: Can you give someone else access to your Azure subscription without giving them your user name and password?

- YES
- NO

**Explanation**: Yes, anyone can create their own Azure account and you can give them access to your subscription with granular control as to permissions. See: [https://docs.microsoft.com/en-us/azure/role-based-access-control/overview](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)

#### Question 38: True or false: you can create your own policies if built-in Azure Policy is not sufficient to your needs

- FALSE
- TRUE

**Explanation**:  True, you can create custom policies using JSON. See: [https://docs.microsoft.com/en-us/azure/governance/policy/tutorials/create-custom-policy-definition](https://docs.microsoft.com/en-us/azure/governance/policy/tutorials/create-custom-policy-definition)

#### Question 39: In the context of Azure's Service Level Agreement (SLA) for virtual machines, which of the following deployment strategies would offer the highest level of availability?

- Deploying two or more virtual machines across different availability zones within the same region.
- Deploying two or more virtual machines within the same data center.   
- Deploying two or more virtual machines within an availability set.
- Deploying a single virtual machine.


**Explanation**: The correct answer is "Deploying two or more virtual machines across different availability zones within the same region".

Service Level Agreement (SLA) is a commitment by a service provider on the level of service - like uptime, performance, or other key metrics - that users can expect. Azure provides an SLA for various services, including Virtual Machines. A single VM, even with premium storage, provides a lesser SLA compared to VMs deployed in an Availability Set or across Availability Zones. While using an Availability Set (two or more VMs in the same datacenter but across fault and update domains) provides a higher SLA than a single VM, the highest SLA is provided when two or more VMs are deployed across Availability Zones in the same region. Availability Zones are unique physical locations within a region. Each zone is made up of one or more datacenters equipped with independent power, cooling, and networking. They are set up to be an isolation boundary - if one zone goes down, the other continues working. This distribution of VMs across zones provides high availability and resiliency, hence offering the highest SLA. See: [https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/](https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/)

#### Question 40: What is the basic way of protecting an Azure Virtual Network subnet?

- Network Security Group
- Azure DDos Standard protection
- Azure Firewall
- Application Gateway with WAF

**Explanation**:  Network Security Group (NSG) - a fairly basic set of rules that you can apply to both inbound traffic and outbound traffic that lets you specify what sources, destinations, and ports are allowed to travel through from outside the virtual network to inside the virtual network. See: [https://docs.microsoft.com/en-us/azure/virtual-network/security-overview](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)

#### Question 41: True or false: Formal support is not included in private preview mode.

- FALSE
- TRUE

**Explanation**: True. Preview features are not fully ready and this phase does not include formal support. See: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)

#### Question 42: True or False: Azure has the responsibility to manage the hardware in the Infrastructure as a Service model

- TRUE   
- FALSE

**Explanation**:  The correct answer is TRUE. In an Infrastructure as a Service (IaaS) model, the cloud service provider, in this case Microsoft Azure, is responsible for managing the underlying physical hardware. This includes servers, storage, networking hardware, and the virtualization layer. Azure ensures that these resources are available and maintained, providing capabilities like automated backup, disaster recovery, and scaling. The customer, on the other hand, is responsible for managing the software components of the service, including the operating system, middleware, runtime, data, and applications. This arrangement allows customers to focus on their core business and application development without worrying about the physical infrastructure's procurement, management, and maintenance. It's important to remember that the division of responsibilities may change in other service models like Platform as a Service (PaaS) or Software as a Service (SaaS), where the cloud service provider manages more layers of the technology stack. But for IaaS, the provider indeed manages the hardware, making the statement TRUE. See: [https://azure.microsoft.com/en-us/overview/what-is-iaas/](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

#### Question 43: What is Single Sign-On?

- When you sign in to an application, it remembers who you are the next time you go there.
- The ability to use an existing user id and password to sign in other applications, and not have to create/memorize a new one.
- When an application outsources (federates) it's identity service to a third-party platform

**Explanation**:  Single Sign-On - the ability to use the same user id and password to log into every application that your company has; enabled by Azure AD. See: [https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on)

#### Question 44: An IT administrator has the requirement to control access to a specific app resource using multi-factor authentication. What Azure service satisfies this requirement?

- Azure Authentication
- Azure Function
- Azure AD
- Azure Authorization

**Explanation**:  You can use Azure AD to control access to your apps and your app resources, based on your business requirements. In addition, you can use Azure AD to require multi-factor authentication when accessing important organizational resources. See: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad)

#### Question 45: What is the MAIN management tool used for managing Azure resources with a graphical user interface?

- Remote Desktop Protocol (RDP)
- PowerShell
- Azure Storage Explorer
- Azure Portal

**Explanation**:  Azure Portal is the website used to manage your resources in Azure. See: [https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview](https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview)

#### Question 46: What is the default amount of credits that you are given when you first create an Azure Free account?

- The default is US$200
- You can create 1 Linux VM, 1 Windows VM, and a number of other free services for the first year.
- You are given $50 per month, for one year towards Azure services  
- Azure does not give you any free credits when you create a free account

**Explanation**: There are some other benefits to a free account, but you get US$200 to spend in the first month. See: [https://azure.microsoft.com/free](https://azure.microsoft.com/free)

#### Question 47: Azure Services can go through several phases in a Service Lifecycle. What are the three phases called?

- Preview Phase, General Availability Phase, and Unpublished
- Private Preview, Public Preview, and General Availability
- Development phase, QA phase, and Live phase
- Announced, Coming Soon, and Live 

**Explanation**:  Private Preview, Public Preview, and General Availability.

#### Question 48: What is Azure's preferred Identity/authentication service?

- Network Security Group
- Facebook Connect
- Live Connect
- Azure Active Directory

**Explanation**:  Azure Active Directory (Azure AD) - Microsoft’s preferred Identity as a Service solution. See: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis)

#### Question 49: Which tool within Azure helps you to track your compliance with various international standards and government laws?

- Microsoft Privacy Statement
- Service Trust Portal
- Compliance Manager
- Azure Government Services

**Explanation**: Compliance Manager will track your own compliance with various standards and laws. See: [https://techcommunity.microsoft.com/t5/security-privacy-and-compliance/announcing-compliance-manager-general-availability/ba-p/161922](https://techcommunity.microsoft.com/t5/security-privacy-and-compliance/announcing-compliance-manager-general-availability/ba-p/161922)

#### Question 50: Which of the following is a feature of the cool access tier for Azure Storage?

- Much cheaper to store your files than the hot access tier
- Most expensive option when it comes to bandwidth cost to access your files
- Cheapest option when it comes to bandwidth costs to access your files
- Significant delays in accessing your data, up to several hours

**Explanation**:  Cool access tier offers cost savings when you expect to store your files and not need to access them often. See: [https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-storage-tiers?tabs=azure-portal](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-storage-tiers?tabs=azure-portal)


### Test 2


#### Question 1: Which of the following scenarios would Azure Policy be a recommended method for enforcement?

- Allow only one specific roles of users to have access to a resource group
- Add an additional prompt when creating a resource without a specific tag to ask the user if they are really sure they want to continue?
- Prevent certain Azure Virtual Machine instance types from being used in a resource group
- Require a virtual machine to always update to the latest security patches

**Explanation**: Azure Policy can add restrictions on storage account SKUs, virtual machine instance types, and rules relating to tagging of resources and groups. It cannot prompt a user to ask them if they are sure. For more info: [https://docs.microsoft.com/en-us/azure/governance/policy/overview](https://docs.microsoft.com/en-us/azure/governance/policy/overview)

####  Question 2: Select the way(s) to increase the security of a traditional user id and password system?

- Use multi-factor authentication which requires an additional device (something you have) to verify identity.
- Require longer and more complex passwords.
- Do not allow users to log into an application except using a company registered device.
- Require users to change their passwords more frequently.

**Explanation**: All of these are ways to increase the security on an account. For more info:
- [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad)
- [https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy](https://docs.microsoft.com/en-us/azure/active-directory-domain-services/password-policy)
- [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-policy)

#### Question 3: Besides Azure Service Health, where else can you find out any issues that affect the Azure global network that affect you?

- Install the Azure app on your phone
- Azure will email you
- Azure Updates Blog
- Each Virtual Machine has a Resource Health blade

**Explanation**: Each Virtual Machine has a Resource Health blade. For more info: [https://docs.microsoft.com/en-us/azure/service-health/resource-health-overview](https://docs.microsoft.com/en-us/azure/service-health/resource-health-overview)

#### Question 4: What would be a good reason to have multiple Azure subscriptions?

- There is one person/credit card paying for resources, and only one person who logs into Azure to manage the resources, but you want to be able to know which resources are used for which client project.
- There is one person/credit card paying for resources, but many people who have accounts in Azure, and you need to separate out resources between clients so that there is absolutely no chance of resources being exposed between them.

**Explanation**: Having multiple subscriptions can technically be done for any reason, but it only makes sense if you have to separate billing directly, or have actual clients logging into the Portal to manage their resources. For more info: [https://docs.microsoft.com/en-us/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide](https://docs.microsoft.com/en-us/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide)

#### Question 5: Which of the following is not an example of Infrastructure as a Service? 

- Azure SQL Database 
- SQL Server in a VM
- Virtual Machine
- Virtual Machine Scale Sets
- Virtual Network

**Explanation**:  With Azure SQL Database, the infrastructure is not in your control. For more info: [https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview](https://docs.microsoft.com/en-us/azure/azure-sql/azure-sql-iaas-vs-paas-what-is-overview)

#### Question 6: Which of the following is not a feature of Azure Functions?

- Designed for backend batch applications that are continuously running
- Can trigger the function based off of Azure events such as a new file being saved to a storage account blob container
- Can possibly cost you nothing as there is a generous free tier
- Can edit the code right in the Azure Portal using a code editor

**Explanation**:  Functions are designed for short pieces of code that start and end quickly. For more info: [https://docs.microsoft.com/en-us/azure/azure-functions/](https://docs.microsoft.com/en-us/azure/azure-functions/)

#### Question 7: Within the context of privacy and compliance, what does the acronym ISO stand for, in English?

- Information Systems Officer
- Instead of
- International Organization for Standardization
- Intelligence and Security Office

**Explanation**: ISO is a standards body, International Organization for Standardization. For more info: [https://www.iso.org/about-us.html](https://www.iso.org/about-us.html)

#### Question 8: What is the minimum charge for having an Azure Account each month, even if you don't use any resources?

- $0
- $200
- $1
- Negotiated with your enterprise manager

**Explanation**: An Azure account can cost nothing if you don't use any resources or only use free resources. For more info: [https://azure.microsoft.com/en-us/pricing/](https://azure.microsoft.com/en-us/pricing/)

#### Question 9: What is a benefit of economies of scale?

- Prices of cloud servers and services are always going down. It'll be cheaper next year than it is this year.
- Big companies don't need to make a profit on every sale
- Big companies don't need to make a profit on the first product they sell you, because they will make a profit on the second
- The more you buy of something, the cheaper it is for you

**Explanation**: Economies of Scale - the more of an item that you buy, the cheaper it is per unit. For more info: [https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3b-economies-of-scale](https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3b-economies-of-scale)

#### Question 10: Application Gateway contains what additional optional security feature over a regular Load Balancer?

- Azure AD Advanced Information Protection    
- Multi-Factor Authentication    
- Web Application Firewall (o
- Advanced DDoS Protection

**Explanation**: Application Gateways also comes with an optional Web Application Firewall (or WAF) as a security benefit. For more info: [https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview)

#### Question 11: Approximately how many regions does Azure have around the world?

- 60+
- 25
- 10
- 40

**Explanation**:  There are 60+ Azure regions currently, in 10+ geographies. For more info: [https://docs.microsoft.com/en-us/azure/availability-zones/az-region](https://docs.microsoft.com/en-us/azure/availability-zones/az-region)

#### Question 12: What does it mean if a service is in Public Preview mode?

- Anyone can use the service but it must not be for production use
- Anyone can use the service for any reason
- The service is generally available for use, and Microsoft will provide support for it
- You have to apply to get selected in order to use that service

**Explanation**: Public Preview is for anyone to use, but it is not supported nor guaranteed to continue to be available. For more info: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)

#### Question 13: Which of the following cloud computing models requires the highest level of involvement in maintaining the operating system and file system by the customer?

- IaaS 
- FaaS
- PaaS
- SaaS

**Explanation**: IaaS or Infrastructure as a service requires you to keep your OS patched, close ports, and generally protect your own server. For more info: [https://azure.microsoft.com/en-us/overview/what-is-iaas/](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

#### Question 14: True or false: Azure Cloud Shell allows access to the Bash and Powershell consoles in the Azure Portal

- FALSE
- TRUE

**Explanation**:  Cloud Shell - allows access to the Bash and Powershell consoles in the Azure Portal. For more info: [https://docs.microsoft.com/en-us/azure/cloud-shell/overview](https://docs.microsoft.com/en-us/azure/cloud-shell/overview)

#### Question 15: Which of the following elements is considered part of the "perimeter" layer of security?

- Separate servers into distinct subnets by role
- Locks on the data center doors
- Keep operating systems up to date with patches
- Use a firewall

**Explanation**: Firewall is part of the perimeter security. For more information on the layered approach to network security: [https://docs.microsoft.com/en-us/learn/modules/intro-to-security-in-azure/5-network-security](https://docs.microsoft.com/en-us/learn/modules/intro-to-security-in-azure/5-network-security)

#### Question 16: What is the concept of paired regions?

- Azure employees in those regions sometimes go on picnics together.
- Each region of the world has one other region, usually in a completely separate country and geography, where it makes the most sense to place your backups. Like East US 2 is paired with South Korea.
- When you deploy your code to one region of the world, it is automatically deployed to the paired region as an emergency backup.
- Each region in the world has at least one other region in which is shares an extremely high speed connection, and where there is coordinated action by Azure not to do anything that will bring them both down at the same time.

**Explanation**: Paired regions are usually in the same geo (not always) but are the most logical place to store backups because they have a high speed connection and Azure staggers the service updates to those regions. For more info: [https://docs.microsoft.com/en-us/azure/best-practices-availability-paired-regions](https://docs.microsoft.com/en-us/azure/best-practices-availability-paired-regions)

#### Question 17: What makes estimating the cost of an unmanaged storage account difficult?

- There is no way to predict the amount of data in the account
- The cost of storage changes frequently
- You are charged for data leaving Azure, and it's difficult to predict that
- You are charged for data coming into Azure, and it's difficult to predict that

**Explanation**:  There is a cost for egress (bandwidth out) and it's hard to estimate how many bytes will be counted leaving an Azure network. For more info: [https://azure.microsoft.com/en-us/pricing/details/storage/page-blobs/](https://azure.microsoft.com/en-us/pricing/details/storage/page-blobs/)

#### Question 18: Why is a user id and password sometimes not enough to prove someone is who they say they are?

- User id and password can be used by anyone such as a co-worker, ex-employee or hacker half-way around the world
- Some people might choose the same user id and password
- Passwords must be encrypted before being stored
- Passwords are usually easy to forget

**Explanation**: The truth is that someone can find a way to get a user id and password, even guess it, and that can be used by another person. For more information on other ways to prove self-identification such as Multi-Factor Authentication: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 19: Which tool within Azure is comprised of : Azure Status, Service Health and Resource Health?

- Azure Dashboard
- Azure Monitor
- Azure Service Health
- Azure Advisor

**Explanation**: Azure Service Health - lets you know about any Azure-related service issues including region-wide downtime. For more info: [https://docs.microsoft.com/en-us/azure/service-health/](https://docs.microsoft.com/en-us/azure/service-health/)

#### Question 20: Which of the following is a good example of a Hybrid cloud?

- Your users are inside your corporate network but your applications and data are in the cloud.
- Your code is a mobile app that runs on iOS and Android phones, but it uses a database in the cloud.
- A server runs in your own environment, but places files in the cloud so that it can extend the amount of storage it has access to.
- Technology that allows you to grow living tissue on top of an exoskeleton, making Terminators impossible to spot among humans.

**Explanation**: Hybrid Cloud - A mixture between your own private networks and servers, and using the public cloud for some things. Typically used to take advantage of the unlimited, inexpensive growth benefits of the public cloud. For more info: [https://azure.microsoft.com/en-us/overview/what-is-hybrid-cloud-computing/](https://azure.microsoft.com/en-us/overview/what-is-hybrid-cloud-computing/)

#### Question 21: Where do you go within the Azure Portal to find all of the third-party virtual machine and other offers?

- Azure mobile app
- Azure Marketplace
- Choose an image when creating a VM
- Bing

**Explanation**:  Azure Marketplace contains thousands of services you can rent within the cloud. For more info: [https://azuremarketplace.microsoft.com/en-us](https://azuremarketplace.microsoft.com/en-us)

#### Question 22: What is the new data privacy and information protection regulation that took effect across Europe in May 2018?

- FedRAMP
- GDPR
- ISO 9001:2015
- PCI DSS

**Explanation**: The General Data Protection Regulation (GDPR) took effect in Europe in May 2018. For more info: [https://docs.microsoft.com/en-us/microsoft-365/compliance/gdpr?view=o365-worldwide](https://docs.microsoft.com/en-us/microsoft-365/compliance/gdpr?view=o365-worldwide)

#### Question 23: Why is Azure App Services considered Platform as a Service?

- You can decide on what type of virtual machine it runs - A-series, or D-series, or even H-series
- You are responsible for keeping the operating system up to date with the latest patches
- Azure App Services is not PaaS, it's Software as a Service.
- You give Azure the code and configuration, and you have no access to the underlying hardware

**Explanation**: You give Azure the code and configuration, and you have no access to the underlying hardware. For more info: [https://docs.microsoft.com/en-us/azure/app-service/overview](https://docs.microsoft.com/en-us/azure/app-service/overview)

#### Question 24: What two types of DDoS protection services does Azure provide? Select two.

- DDoS Premium Protection
- DDoS Advanced Protection
- DDoS Network Protection
- DDoS IP Protection

**Explanation**:  Azure DDoS Protection offers two types of DDoS protection services:

- **Network Protection** protects against volumetric attacks that target the network infrastructure. This type of protection is available for all Azure resources that are deployed in a virtual network.
    
- **IP Protection** protects against volumetric and protocol-based attacks that target specific public IP addresses. This type of protection is available for public IP addresses that are not deployed in a virtual network.

For more info: [https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview](https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview)

#### Question 25: What types of files can a Content Delivery Network speed up the delivery of?

- PDFs
- Videos
- Images
- JavaScript files

**Explanation**: All of them. Any static file that doesn't change. For more info: [https://docs.microsoft.com/en-us/azure/cdn/cdn-overview](https://docs.microsoft.com/en-us/azure/cdn/cdn-overview)

#### Question 26: What is the concept of Big Data?

- A set of Azure services that allow you to use execute code in the cloud but don’t require (or even allow) you to manage the underlying server
- A form of artificial intelligence (AI) that allows systems to automatically learn and improve from experience without being explicitly programmed.
- A small sensor or other device that constantly sends it's status and other data to the cloud
- An extremely large set of data that you want to ingest and do analysis on; traditional software like SQL Server cannot handle Big Data as efficiently as specialized products

**Explanation**: Big Data - a set of open source (Apache Hadoop) products that can do analysis on millions and billions of rows of data; current tools like SQL Server are not good for this scale

For more info: [https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/big-data](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/big-data)

#### Question 27: Select all features part of Azure AD?

- Device Management
- Log Alert Rule
- Single sign-on 
- Smart lockout
- Custom banned password list

**Explanation**: The Log Alert Rule is not a feature of Azure AD. See: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad)
#### Question 28: In which US state is the East US 2 region?

- Iowa
- Virginia
- Texas
- California

**Explanation**: East US 2 is in the Eastern state of Virginia, close to Washington DC. For more info: [https://azure.microsoft.com/en-us/global-infrastructure/data-residency/](https://azure.microsoft.com/en-us/global-infrastructure/data-residency/)

#### Question 29: Windows servers use "remote desktop protocol" (RDP) in order for administrators to get access to manage the server. Linux servers use SSH. What is the recommendation for ensuring the security of these protocols? 

- Disable RDP access using the Windows Services control panel admin tool
- Ensure strong passwords on your Windows admin accounts
- Do not enable SSH access for Linux servers
- Do not allow public Internet access over the RDP and SSH ports directly to the server. Instead use a secure server like Bastion to control access to the servers behind.

**Explanation**: You need to either control access to the RDP and SSH ports to a very specific range of IPs, enable the ports only when you are using it, or use a Bastion server/jump box to protect those servers. For more info: [https://docs.microsoft.com/en-us/azure/bastion/bastion-overview](https://docs.microsoft.com/en-us/azure/bastion/bastion-overview)

#### Question 30: What does ARM stand for in Azure?

- Account Resource Manager    
- Availability, Reliability, Maintainability  
- Advanced RISC Machine    
- Azure Resource Manager

**Explanation**: Azure Resource Manager (ARM) - this is the common resource deployment model that underlies all resource creation or modification; no matter whether you use the portal, powershell or the SDK, the Azure Resource Manager takes those commands and executes them. For more info: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

#### Question 31: In what way does Multi-Factor Authentication increase the security of a user account?

- It requires the user to possess something like their phone to read an SMS, use a mobile app, or biometric identification.
- It requires single sign-on functionality
- It doesn't. Multi-Factor Authentication is more about access and authentication than account security.
- It requires users to be approved before they can log in for the first time.
    

**Explanation**: MFA requires that the user have access to their mobile phone for using SMS or an app. For more info: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 32: What is the maximum amount of Azure Storage space a single subscription can store?

- 500 GB
- Virtually unlimited
- 5 PB
- 2 TB

**Explanation**: A single Azure subscription can have up to 250 storage accounts per region, and each storage account can store up to 5 Petabytes. That is 31 million Terabytes. This is probably 15-20 times what Google, Amazon, Microsoft and Facebook use combined. That's a lot. For more info: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#storage-limits](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#storage-limits)

#### Question 33: How do you get access to services in Private Preview mode?

- You cannot use private preview services.
- They are available in the marketplace. You simply use them.
- You must apply to use them.
- You must agree to a terms of use first.

**Explanation**: Private Preview means you must apply to use them. For more info: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)

#### Question 34: What is the concept of being able to get your applications and data running in another environment quickly?

- Business Continuity / Disaster Recovery (BC/DR)
- Azure Blueprint
- Azure Devops
- Reproducible deployments

**Explanation**: Disaster Recovery - the ability to recover from a big failure within an acceptable period of time, with an acceptable amount of data lost. For more info on Backup and Disaster Recovery: [https://azure.microsoft.com/en-us/solutions/backup-and-disaster-recovery/](https://azure.microsoft.com/en-us/solutions/backup-and-disaster-recovery/) For more info on Azure’s built-in disaster recovery as a service (DRaaS): [https://azure.microsoft.com/en-us/services/site-recovery/](https://azure.microsoft.com/en-us/services/site-recovery/)

#### Question 35: Which of the following is considered a downside to using Capital Expenditure (CapEx)?

- It does not require a lot of up front money
- You can deduct expenses as they occur
- You are not guaranteed to make a profit    
- You must wait over a period of years to depreciate that investment on your taxes

**Explanation**: One of the downsides of CapEx is that the money invested cannot be deducted immediately from your taxes. For more info: [https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3c-capex-vs-opex](https://docs.microsoft.com/en-us/learn/modules/principles-cloud-computing/3c-capex-vs-opex)

#### Question 36: What Azure resource allows you to evenly split traffic coming in and direct it to several identical virtual machines to do the work and respond to the request?

- Load Balancer or Application Gateway  
- Azure Logic Apps
- Virtual Network
- Azure App Services

**Explanation**: This is the core feature of either a Load Balancer or Application Gateway. For more info: [https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview)

#### Question 37: True or false: Azure charges for bandwidth used "inbound" to Azure

- FALSE
- TRUE

**Explanation**:  Ingress bandwidth is free. You pay for egress (outbound). For more info: [https://azure.microsoft.com/en-us/pricing/details/bandwidth/](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)

#### Question 38: Which free Azure security service checks all traffic travelling over a subnet against a set of rules before allowing it in, or out.

- Network Security Group
- Advanced Threat Protection (ARP)
- Azure Firewall
- Azure DDoS Protection

**Explanation**:  Network Security Group (NSG) - a fairly basic set of rules that you can apply to both inbound traffic and outbound traffic that lets you specify what sources, destinations and ports are allowed to travel through from outside the virtual network to inside the virtual network. For more info: [https://docs.microsoft.com/en-us/azure/virtual-network/security-overview](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview)

#### Question 39: What is the concept of Availability?

- A system must have 100% uptime to be considered available
- A system that can scale up and scale down depending on customer demand
- The percentage of time a system responds properly to requests, expressed as a percentage over time    
- A system that has a single point of failure

**Explanation**: Availability - what percentage of time does a system respond properly to requests, expressed as a percentage over time. For more information on region and availability zones see: [https://docs.microsoft.com/en-us/azure/availability-zones/az-overview](https://docs.microsoft.com/en-us/azure/availability-zones/az-overview). For more information on availability options for virtual machines see: [https://docs.microsoft.com/en-us/azure/virtual-machines/availability](https://docs.microsoft.com/en-us/azure/virtual-machines/availability). 

#### Question 40: What is the benefit of using Powershell over CLI?

- More powerful commands
- Quicker to deploy VMs
- Cheaper
- No benefit, it's the same

**Explanation**: There is no benefit, only a matter of personal choice. For more info on Azure CLI: [https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest). For more info on Azure Powershell: [https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0](https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0)

#### Question 41: How many regions does Azure have in Brazil?

- 2
- 0
- 1
- 4

**Explanation**: There is 1 region in Brazil. For more info: [https://azure.microsoft.com/en-us/global-infrastructure/geographies/](https://azure.microsoft.com/en-us/global-infrastructure/geographies/)

#### Question 42: What Azure product allows you to autoscale virtual machines from 1 to 1000 instances, and also provides load balancing services built in?

- Virtual Machine Scale Sets
- Azure App Services
- Azure Virtual Machines
- Application Gateway

**Explanation**:  Virtual Machine Scale Sets - these are a set of identical virtual machines (from 1 to 1000 instances) that are designed to auto-scale up and down based on user demand. For more info: [https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/](https://azure.microsoft.com/en-us/services/virtual-machine-scale-sets/)

#### Question 43: What does it mean if a service is in General Availability (GA) mode?

- Anyone can use the service for any reason    
- You have to apply to get selected in order to use that service
- Anyone can use the service but it must not be for production use
- The service has now reached public preview, and Microsoft will provide support for it

**Explanation**: Anyone can use a GA service. It is fully supported and can be used for production. For more info: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)

#### Question 44: Each person has their own user id and password to log into Azure. But how many subscriptions can a single account be associated with?

- 10
- 250 per region
- No limit
- One

**Explanation**:  There is not a limit to the number of subscriptions a single user can be included on.

For more info: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits)

#### Question 45: What is the Azure SLA for two or more Virtual Machines in an Availability Set?

- 100%
- 99.90%
- 99.99%
- 99.95%

**Explanation**: 99.95% For more info: [https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/](https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/)

#### Question 46: Which Azure service is the recommended Identity-as-a-Service offering inside Azure?

- Azure Active Directory (AD)
- Azure Portal
- Identity and Access Management (IAM)
- Azure Front Door

**Explanation**:  Azure AD is the identity service designed for web protocols, that you can use for your applications. For more info: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis)

#### Question 47: What is the benefit of using a command line tool like Powershell or CLI as opposed to the Azure portal?

- Quicker to deploy VMs
- Cheaper
- Automation

**Explanation**: The real benefit is automation. Being able to write a script to do something is better than having to do it manually each time. For more info on Azure CLI: [https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest](https://docs.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest). For more info on Azure Powershell: [https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0](https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0)

#### Question 48: What database service is specifically designed to be extremely fast in responding to requests for small amounts of data (called low latency)?

- SQL Database
- SQL Data Warehouse
- Cosmos DB
- SQL Server in a VM

**Explanation**: Cosmos DB - extremely low latency (fast) storage designed for smaller pieces of data quickly; SaaS. For more info: [https://docs.microsoft.com/en-us/azure/cosmos-db/](https://docs.microsoft.com/en-us/azure/cosmos-db/)

#### Question 49: If you are a US federal, state, local, or tribal government entities and their solution providers, which Azure option should you be looking to register for?

- Azure is not available for government officials
- Azure Government
- Azure Department of Defence
- Azure Public Portal

**Explanation**: Hopefully, it's clear that US Federal, State, Local and Tribal governments can use the US Government portal. For more info: [https://docs.microsoft.com/en-us/azure/azure-government/documentation-government-welcome](https://docs.microsoft.com/en-us/azure/azure-government/documentation-government-welcome)

#### Question 50: What is the service level agreement for two or more Azure Virtual Machines that have been manually placed into different Availability Zones in the same region?

- 99.95%
- 99.90%
- 99.99%
- 100%

**Explanation**: 99.99%. For more info: [https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/](https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/)

### Test 3

#### Question 1: What is the significance of the Azure region? Why is it important?

- You must select a region when creating most resources, and the region is the area of the world where those resources will be physically located.
- Once you select a region, you cannot create resources outside of that region. So selecting the right region is an important decision.
- Region is just a folder structure in which you organize resources, much like file folders on a computer.
- Even though you have to choose a region when creating resources, there's generally no consequence of what you select. You can create a network in one region and then create virtual machines for that network in another region.    

**Explanation**: The region is the area of the world where resources get created. You can create resources in any region that you have access to. But there are sometimes restrictions when creating a resource in one region that related resources like networks must also be in the same region for logical reasons. For more info: [https://azure.microsoft.com/en-us/global-infrastructure/geographies/#overview](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#overview)

#### Question 2: TRUE OR FALSE: Through Azure Active Directory one can control access to an application but not the resources of the application.

- FALSE
- TRUE

**Explanation**: Azure AD can control the access of both the apps and the app resources. See: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad)

#### Question 3: What is the name of the open source project run by the Apache foundation that maps to the HDInsight tools within Azure?

- Apache Jazz
- Apache Cayenne
- Apache Jaguar
- Apache Hadoop
- 
**Explanation**: Hadoop is open source home of the HDInsight tools. For more info: [https://docs.microsoft.com/en-us/azure/hdinsight/hadoop/apache-hadoop-introduction](https://docs.microsoft.com/en-us/azure/hdinsight/hadoop/apache-hadoop-introduction)

#### Question 4: Which tool within the Azure Portal will make specific recommendations based on your actual usage for how you can improve your use of Azure?

- Azure Monitor    
- Azure Service Health
- Azure Dashboard
- Azure Advisor

**Explanation**: Azure Advisor - a tool that will analyze your use of Azure and make you specific recommendations based on your usage across availability, security, performance and cost categories. For more info: [https://docs.microsoft.com/en-us/azure/advisor/](https://docs.microsoft.com/en-us/azure/advisor/)

#### Question 5: What does it mean that security is a "shared model" in Azure?

- Both users and Azure have responsibilities for security.
- You must keep your security keys private and ensure it doesn't get out.
- Azure takes care of security completely.
- Azure takes no responsibility for security.

**Explanation**: The shared security model means that, depending on the application model, you and Azure both have roles in ensuring a secure environment. For more info: [https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility](https://docs.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)

#### Question 6: What is the name of the collective set of APIs that provide machine learning and artificial intelligence services to your own applications like voice recognition, image tagging, and chat bot?

- Cognitive Services
- Natural Language Service, LUIS
- Azure Machine Learning Studio
- Azure Batch

**Explanation**: Azure Cognitive Services is the set of Machine Learning and AI API's. For more info: [https://docs.microsoft.com/en-us/azure/cognitive-services/](https://docs.microsoft.com/en-us/azure/cognitive-services/)

#### Question 7: What happens if Azure does not meet its own Service Level Agreement guarantee (SLA)?

- The service will be free that month
- You will be financially refunded a small amount of your monthly fee
- It's not possible. Azure will always meet it's SLA?

**Explanation**: Microsoft offers a refund of 10% or 25% depending on how badly they miss their service guarantee. For more info: [https://azure.microsoft.com/en-us/support/legal/sla/](https://azure.microsoft.com/en-us/support/legal/sla/)

#### Question 8: What software is used to synchronize your on premises AD with your Azure AD?

- Azure AD Federation Services
- Azure AD Domain Services
- LDAP
- AD Connect  

**Explanation**: AD Connect is used to synchronize your corporate AD with Azure AD. For more info: [https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/whatis-azure-ad-connect)

#### Question 9: True or false: If your feature is in the General Availability phase, then your feature will receive support from all Microsoft support channels.

- TRUE
- FALSE

**Explanation**: This is true. Do not use preview features in production apps. For more info: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/)

#### Question 10: TRUE OR FALSE: If you wanted to deploy a virtual machine to China, you would just choose the China region from the drop down.

- FALSE
- TRUE

**Explanation**: Some regions of the world require special contracts with the local provider such as Germany and China. For more info: [https://docs.microsoft.com/en-us/azure/china/overview-checklist](https://docs.microsoft.com/en-us/azure/china/overview-checklist)

#### Question 11: What is a policy initiative in Azure?

- A custom designed policy
- Requiring all resources in Azure to use tags
- The ability to group policies together
- Assigning permissions to a role in Azure

**Explanation**: The ability to group policies together. For more info: [https://docs.microsoft.com/en-us/azure/governance/policy/overview#initiative-definition](https://docs.microsoft.com/en-us/azure/governance/policy/overview#initiative-definition)

#### Question 12: Which database product offers "sub 5 millisecond" response times as a feature?

- Cosmos DB
- SQL Data Warehouse
- SQL Server in a VM
- Azure SQL Database

**Explanation**: Cosmos DB is low latency, and even offers sub 5-ms response times at some levels. For more info: [https://docs.microsoft.com/en-us/azure/cosmos-db/introduction](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction)

#### Question 13: Which of the following resources are not considered Compute resources?

- Function Apps
- Azure Batch
- Virtual Machines
- Virtual Machine Scale Sets
- Load Balancer

**Explanation**: A load balancer is a networking product, and does not execute your code.  For more info: [https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-overview). For more information on compute resources: [https://azure.microsoft.com/en-us/product-categories/compute/](https://azure.microsoft.com/en-us/product-categories/compute/)

#### Question 14: With Azure public cloud, anyone with a valid credit card can sign up and get services immediately

- FALSE
- TRUE

**Explanation**: Yes, Azure public cloud is open to the public in all countries that Azure supports. For more info: [https://docs.microsoft.com/en-us/learn/modules/create-an-azure-account/](https://docs.microsoft.com/en-us/learn/modules/create-an-azure-account/)

#### Question 15: Which Azure service can be enabled to enable Multi-Factor Authentication for administrators but not require it for regular users?

- Azure AD B2B    
- Advanced Threat Protection
- Azure Firewall
- Privileged Identity Management

**Explanation**: Privileged Identity Management can be used to ensure privileged users have to jump through additional verification because of their role. For more info: [https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure)

#### Question 16: What is an Azure Subscription?

- Each user account is associated with a unique subscription. If you need more than one subscription, you need to create multiple user accounts.
- It is the level at which services are billed. All resources created under a subscription are billed to that subscription.

**Explanation**: Subscription is the level at which things get billed. Multiple users can be associated with a subscription at various permission levels. For more info: [https://docs.microsoft.com/en-us/services-hub/health/azure_sponsored_subscription](https://docs.microsoft.com/en-us/services-hub/health/azure_sponsored_subscription)

#### Question 17: What operating systems does an Azure Virtual Machine support?

- Windows, Linux and macOS
- macOS
- Windows
- Linux
- Windows and Linux

**Explanation**: Azure Virtual Machines support Windows and Linux. For more info: [https://docs.microsoft.com/en-us/azure/virtual-machines/](https://docs.microsoft.com/en-us/azure/virtual-machines/)

#### Question 18: Which Azure management tool analyzes your usage of Azure and makes suggestions specifically targeted to help you optimize your usage of Azure regarding cost, security and performance?

- Azure Service Health
- Azure Advisor
- Azure Firewall
- Azure Mobile App

**Explanation**: Azure Advisor analyzes your specific usage of Azure and makes helpful suggestions on how it can be improved.

#### Question 19: Which feature within Azure alerts you to service issues that happen in Azure itself, not specifically related to your own resources?

- Azure Monitor
- Azure Portal Dashboard
- Azure Service Health
- Azure Security Center

**Explanation**: Azure Service Health - lets you know about any Azure-related service issues including region-wide downtime. For more info: [https://docs.microsoft.com/en-us/azure/service-health/](https://docs.microsoft.com/en-us/azure/service-health/)

#### Question 20: Which two features does Virtual Machine Scale Sets provide as part of the core product? Pick two.

- Content Delivery Network
- Firewall
- Automatic installation of supporting apps and deployment of custom code
- Load balancing between virtual machines    
- Autoscaling of virtual machines

**Explanation**: VMSS provides autoscale features and has a built in load balancer. You still need to have a way to deploy your code to the new servers, as you do with regular VMs. For more info: [https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/)

#### Question 21: Where can you go to see what standards Microsoft is in compliance with?

- Azure Service Health
- Azure Security Center
- Trust Center
- Azure Privacy Page

**Explanation**: The list of standards that Azure has been certified to meet is in the Trust Center. 
For more info: [https://www.microsoft.com/en-us/trust-center](https://www.microsoft.com/en-us/trust-center)

#### Question 22: What does it mean if a service is in Private Preview mode?

- The service is generally available for use, and Microsoft will provide support for it
- Anyone can use the service but it must not be for production use
- You have to apply to get selected in order to use that service
- Anyone can use the service for any reason

**Explanation**: Private Preview means you have to apply to use a service, and you may or may not be selected. For more info: [https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/#:~:text=Private%20preview%20%E2%80%93%20during%20this%20phase,to%20evaluate%20the%20new%20feature.)

#### Question 23: What are groups of subscriptions called?

- Azure Policy
- Subscription Groups
- ARM Groups
- Management Groups

**Explanation**: Subscriptions can be nested and placed into management groups to make managing them easier. For more info: [https://docs.microsoft.com/en-us/azure/governance/management-groups/overview](https://docs.microsoft.com/en-us/azure/governance/management-groups/overview)

#### Question 24: How do you stop your Azure account from incurring costs above a certain level without your knowledge?

- Switch to Azure Reserved Instances with Hybrid Benefit for VMs
- Only use Azure Functions which have a significant free limit
- Implement the Azure spending limit in the Account Center    
- Set up a billing alert to send you an email when it reaches a certain level

**Explanation**: If you don't want to spend over a certain amount, implement a spending limit in the account center. For more info: [https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit](https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit#:~:text=The%20spending%20limit%20is%20equal,to%20the%20amount%20of%20credit.)

#### Question 25: How does Multi-Factor Authentication make a system more secure?

- It allows the user to log in without a password because they have already previously been validated using a browser cookie
- It requires the user to have access to their verified phone in order to log in 
- It doesn't make it more secure
- It is another password that a user has to memorize, making it more secure

**Explanation**: Multi-Factor Authentication (MFA) - the concept of having something additional to a “password” that is required to log in; passwords are find-able or guessable; but having your mobile phone on you to receive a phone call, text or run an app to get a code is harder for an unknown hacker to get. For more info: [https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)

#### Question 26: How many hours are available free when using the Azure B1S General Purpose Virtual Machines under a Azure free account in the first 12 months?

- 500 hrs
- 750 hrs
- 300 hrs
- Indefinite amount of hrs

**Explanation**: Each Azure free account includes 750 hours free for Azure B1S General Purpose Virtual Machines for the first 12 months. For more info: [https://azure.microsoft.com/en-us/free/free-account-faq/](https://azure.microsoft.com/en-us/free/free-account-faq/)

#### Question 27: What is the goal of a DDoS attack?

- To extract data from a database
- To trick users into giving up personal information
- To overwhelm and exhaust application resources
- To crack the password from administrator accounts

**Explanation**: DDoS is a type of attack that tries to exhaust application resources. The goal is to affect the application’s availability and its ability to handle legitimate requests. For more info: [https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview](https://docs.microsoft.com/en-us/azure/virtual-network/ddos-protection-overview)

#### Question 28: True or false: Azure PowerShell scripts and Command Line Interface (CLI) scripts are entirely compatible with each other?

- TRUE
- FALSE

**Explanation**: No, PowerShell is it's own language, different than CLI. For more info: [https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0](https://docs.microsoft.com/en-us/powershell/azure/?view=azps-4.5.0)

#### Question 29: For tax optimization, which type of expense is preferable?

- CapEx
- OpEx

**Explanation**: Operating Expenditure is thought to be preferable because you can fully deduct expenses when they are incurred. For more info: [https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/fiscal-outcomes](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/business-outcomes/fiscal-outcomes)

#### Question 30: What is the recommended way within Azure to store secrets such as private cryptographic keys?

- Azure Advanced Threat Protection (ATP)
- In an Azure Storage account private blob container
- Within the application code
- Azure Key Vault

**Explanation**: Azure Key Vault - the modern way to store cryptographic keys, signed certificates and secrets in Azure. For more info: [https://docs.microsoft.com/en-us/azure/key-vault/](https://docs.microsoft.com/en-us/azure/key-vault/)

#### Question 31: Which of the following would be an example of an Internet of Things (IoT) device?

- A video game, installed on Windows clients around the world, that keep user scores in the cloud.
- A mobile application that is used to watch online video courses
- A refrigerator that monitors how much milk you have left and sends you a text message when you are running low
- A web application that people use to perform their banking tasks

**Explanation**: An IoT device is not a standard computing device but connects to a network to report data on a regular basis. A web server, a personal computer, or a mobile app is not an IoT device. For more info: [https://docs.microsoft.com/en-us/azure/iot-fundamentals/iot-introduction](https://docs.microsoft.com/en-us/azure/iot-fundamentals/iot-introduction)

#### Question 32: Deploying Azure App Services applications consists of what two components? Pick two.

- Database scripts
- Configuration
- Managing operating system updates
- Packaged code

**Explanation**: Azure App Services, platform as a service, consists of code and configuration. For more info: [https://docs.microsoft.com/en-us/azure/app-service/](https://docs.microsoft.com/en-us/azure/app-service/)

#### Question 33: What type of documents does the Microsoft Service Trust Portal provide?

- Documentation on the individual Azure services and solutions
- Specific recommendations about your usage of Azure and ways you can improve
- A list of standards that Microsoft follows, pen test results, security assessments, white papers, faqs, and other documents that can be used to show Microsoft's compliance efforts
- A tool that helps you manage your compliance to various standards

**Explanation**: A list of standards that Microsoft follows, pen test results, security assessments, white papers, faqs, and other documents that can be used to show Microsoft's compliance efforts. For more info: [https://servicetrust.microsoft.com/](https://servicetrust.microsoft.com/)

#### Question 34: Which of the following are one of the advantages of running your cloud in a private cloud?

- Assurance that your code, data and applications are running on isolated hardware, and on an isolated network.
- You own the hardware, so you can change private cloud hosting providers easily.   
- Private cloud is significantly cheaper than the public cloud.    

**Explanation**: Private cloud generally means that you are running your code on isolated computing, not mixed in with other companies. For more info: [https://azure.microsoft.com/en-us/overview/what-are-private-public-hybrid-clouds/](https://azure.microsoft.com/en-us/overview/what-are-private-public-hybrid-clouds/)

#### Question 35: What advantage does an Application Gateway have over a Load Balancer?

- Application Gateway is more like an enterprise-grade product. You should not use a load balancer in production.
- Application gateway understands the HTTP protocol and can interpret the URL and make decisions based on the URL.
- Application Gateway can be scaled so that two, three or more instances of the gateway can support your application.

**Explanation**: Application gateway can make load balancing decisions based on the URL path, while a load balancer can't. For more info: [https://docs.microsoft.com/en-us/azure/application-gateway/overview](https://docs.microsoft.com/en-us/azure/application-gateway/overview)

#### Question 36: If you wanted to get an alert every time a new virtual machine is created, where could you create that?

- Azure Monitor
- Azure Policy
- Subscription settings
- Azure Dashboard

**Explanation**: The best place to track events at the resource level is Azure Monitor. For more info: [https://docs.microsoft.com/en-us/azure/azure-monitor/](https://docs.microsoft.com/en-us/azure/azure-monitor/)

#### Question 37: How many minutes per month downtime is 99.99% availability?

- 4
- 1
- 40
- 100

**Explanation**: 99.99% is 4 minutes per month of downtime. For more info: [https://azure.microsoft.com/en-us/support/legal/sla/summary/](https://azure.microsoft.com/en-us/support/legal/sla/summary/)

#### Question 38: What is the service level agreement for two or more Azure Virtual Machines that have been placed into the same Availability Set in the same region?

- 100%
- 99.90%
- 99.99%
- 99.95%

**Explanation**: 99.95%. For more info: [https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/](https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/v1_9/)

#### Question 39: What is the core problem that you need to solve in order to have a high-availability application?

- You need to avoid single points of failure
- You need to ensure your server has a lot of RAM and a lot of CPUs
- You should have a backup copy of your application on standby, ready to be started up when the main application fails.    
- You need to ensure the capacity of your server exceeds your highest number of expected concurrent users

**Explanation**: You'll want to avoid single points of failure, so that any component that fails does not cause the entire application to fail. For more info: [https://docs.microsoft.com/en-us/azure/architecture/guide/design-principles/redundancy](https://docs.microsoft.com/en-us/azure/architecture/guide/design-principles/redundancy)

#### Question 40: What are resource groups?

- A folder structure in Azure in which you organize resources like databases, virtual machines, virtual networks, or almost any resource
- Automatically assigned groups of resources that all have the same type (virtual machine, app service, etc)
- Based on the tag assigned to a resource by the deployment script, it is assigned to a group
- Within Azure security model, users are organized into groups, and those groups are granted permissions to resources

**Explanation**: Resource Groups - a folder structure in Azure in which you organize resources like databases, virtual machines, virtual networks, or almost any resource. For more info: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal)

#### Question 41: Which of the following services would NOT be considered Infrastructure as a Service?

- Virtual Network Interface Card (NIC)
- Azure Functions App
- Virtual Machine
- Virtual Network

**Explanation**: Functions are small pieces of code that you give to Azure to run for you, and you have no access to the underlying infrastructure. For more info: [https://docs.microsoft.com/en-us/azure/azure-functions/](https://docs.microsoft.com/en-us/azure/azure-functions/)

#### Question 42: What two advantages does cloud computing elasticity give to you? Pick two. 

- You can do more regular backups and you won't lose as much when that backup gets restored
- You can save money.
- Servers have become a commodity and Microsoft doesn't even need to even fix servers that fail within Azure.
- You can serve users better during peak traffic periods by automatically adding more capacity.

**Explanation**: Elasticity saves you money during slow periods (over night, over the weekend, over the summer, etc) and also allows you to handle the highest peak of traffic. For more info: [https://azure.microsoft.com/en-us/overview/what-is-elastic-computing/](https://azure.microsoft.com/en-us/overview/what-is-elastic-computing/)

#### Question 43: Which of the following elements is considered part of the "network" layer of network security?

- Keeping operating systems up to date with patches
- All of the above
- Locks on the data center doors
- Separate servers into distinct subnets by role

**Explanation**: Subnets is part of network security. For more info: [https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices) and [https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model)

#### Question 44: What data format are ARM templates created in?

- JSON
- YAML
- HTML    
- XML

**Explanation**: ARM templates are created in JSON. For more info: [https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview)

#### Question 45: What does the letter R in RBAC stand for?

- Rights
- Review
- Role
- Rule

**Explanation**: RBAC is role based access control. For more info: [https://docs.microsoft.com/en-us/azure/role-based-access-control/](https://docs.microsoft.com/en-us/azure/role-based-access-control/)

#### Question 46: Which Azure service, when enabled, will automatically block traffic to or from known malicious IP addresses and domains?

- Network Security Groups
- Azure Active Directory
- Azure Firewall 
- Load Balancer

**Explanation**: Azure Firewall has a threat-intelligence option that will automatically block traffic to/from bad actors on the Internet. For more info: [https://docs.microsoft.com/en-us/azure/firewall/](https://docs.microsoft.com/en-us/azure/firewall/)

#### Question 47: TRUE OR FALSE: Azure Tenant is a dedicated and trusted instance of Azure Active Directory that's automatically created when your organization signs up for a Microsoft cloud service subscription.

- TRUE
- FALSE

**Explanation**: Yes, Azure Tenant is a dedicated and trusted instance of Azure AD that's automatically created when your organization signs up for a Microsoft cloud service subscription. See: [https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis#which-features-work-in-azure-ad)

#### Question 48: Why should you divide your application into multiple subnets as opposed to having all your web, application and database servers running on the same subnet?

- Each server type of your application requires its own subnet. It's not possible to mix web servers, database servers and application servers on the same subnet.
- Separating your application into multiple subnets allows you to have different NSG security rules for each subnet, which can make it harder for a hacker to get from one compromised server onto another.    
- There are only a limited number of IP addresses available per subnet, so you need multiple subnets over a certain number.
    
**Explanation**: For security purposes, you should not allow "port 80" web traffic to reach certain servers, and you do that by having separate NSG rules on each subnet. For more info: [https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/network-best-practices)

#### Question 49: Which style of computing is easiest when migrating an existing hosted application from your own data center into the cloud?

- PaaS
- IaaS
- FaaS
- Serverless

**Explanation**: Infrastructure as a service is the easiest to migrate into, from an existing hosted app - lift and shift. For more info: [https://azure.microsoft.com/en-us/overview/what-is-iaas/](https://azure.microsoft.com/en-us/overview/what-is-iaas/)

#### Question 50: If you have an Azure free account, with a $200 credit for the first month, what happens when you reach the $200 limit?

- Your account is automatically closed.
- Your credit card is automatically billed.
- All services are stopped and you must decide whether you want to convert to a paid account or not.
- You cannot create any more resources until you add more credits to the account.

**Explanation**: Using up the free credits causes all your resources to be stopped until you decide to get a paid account. For more info: [https://azure.microsoft.com/en-us/free/free-account-faq/](https://azure.microsoft.com/en-us/free/free-account-faq/)




## Microsoft platform

### Practice assessment 1

#### Question 1 of 50

Why is cloud computing often less expensive than on-premises datacenters? Each correct answer presents a complete solution.

- You are only billed for what you use.

Renting compute and storage services and being billed for only what you use often lowers operating expenses. Depending on the service and the type of network bandwidth, charges can be incurred. Cloud service offerings often provide functionality that can be difficult or cost-prohibitive to deploy on-premises, especially for smaller organizations. Major cloud providers offer services around the world. Making it easy and relatively inexpensive to deploy services close to where your users reside. [Describe cloud computing - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/)

#### Question 2 of 50

Select the answer that correctly completes the sentence. **[Answer choice]** refers to upfront costs incurred one time, such as hardware purchases.

- Capital expenditures

Capital expenditures are one-time expenses that can be deducted over time. Operational expenditures are billed as you use services and a do not have upfront costs.

[Describe cloud computing - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/)

#### Question 3 of 50

Which cloud deployment model are you using if you have servers physically located at your organization’s on-site datacenter, and you migrate a few of the servers to the cloud?

- hybrid cloud

A hybrid cloud is a computing environment that combines a public cloud and a private cloud by allowing data and applications to be shared between them.

[Describe cloud computing - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/)

#### Question 4 of 50

Select the answer that correctly completes the sentence.

Increasing compute capacity for an app by adding RAM or CPUs to a virtual machine is called **[answer choice]**.

- vertical scaling

You scale vertically to increase compute capacity by adding RAM or CPUs to a virtual machine. Scaling horizontally increases compute capacity by adding instances of resources, such as adding virtual machines to the configuration. Disaster recovery keeps data and other assets safe in the event of a disaster. High availability minimizes downtime when things go wrong. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 5 of 50

Select the answer that correctly completes the sentence.

Deploying and configuring cloud-based resources quickly as business requirements change is called **[answer choice]**.

- agility

Agility means that you can deploy and configure cloud-based resources quickly as app requirements change. Scalability means that you can add RAM, CPU, or entire virtual machines to a configuration. Elasticity means that you can configure cloud-based apps to take advantage of autoscaling, so apps always have the resources they need. High availability means that cloud-based apps can provide a continuous user experience with no apparent downtime, even when things go wrong. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 6 of 50

What are cloud-based backup services, data replication, and geo-distribution features of?

- a disaster recovery plan

Disaster recovery uses services, such as cloud-based backup, data replication, and geo-distribution, to keep data and code safe in the event of a disaster. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 7 of 50

What is high availability in a public cloud environment dependent on?

- the service-level agreement (SLA) that you choose

Different services have different SLAs. Sometimes different tiers of the same service will offer different SLAs, which can increase or decrease the promised availability. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 8 of 50

Select the answer that correctly completes the sentence.

An example of **[answer choice]** is automatically scaling an application to ensure that the application has the resources needed to meet customer demands.

- elasticity

Elasticity refers to the ability to scale resources as needed, such as during business hours, to ensure that an application can keep up with demand, and then reducing the available resources during off-peak hours. Agility refers to the ability to deploy new applications and services quickly. High availability refers to the ability to ensure that a service or application remains available in the event of a failure. Geo-distribution makes a service or application available in multiple geographic locations that are typically close to your users. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 9 of 50

Select the answer that correctly completes the sentence.

Increasing the capacity of an application by adding additional virtual machine is called **[answer choice]**.

- horizontal scaling

Scaling horizontally increases compute capacity by adding instances of resources, such as adding virtual machines to the configuration. You scale vertically to increase compute capacity by adding RAM or CPUs to a virtual machine. Agility refers to the ability to deploy new applications and services quickly. High availability minimizes downtime when things go wrong. [Describe the benefits of using cloud services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/)

#### Question 10 of 50

In a platform as a service (PaaS) model, which two components are the responsibility of the cloud service provider? Each correct answer presents a complete solution.

- operating system
- physical network

In PaaS, the cloud provider is responsible for the operating system, physical datacenter, physical hosts, and physical network. In PaaS, the customer is responsible for accounts and identities. 
[Describe cloud service types - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

#### Question 11 of 50

Which type of cloud service model is typically licensed through a monthly or annual subscription?

- software as a service (SaaS)

SaaS is software that is centrally hosted and managed for you and your users or customers. Usually, one version of the application is used for all customers, and it is licensed through a monthly or annual subscription. PaaS and IaaS use a consumption-based model, so you only pay for what you use. [Describe cloud service types - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

#### Question 12 of 50

In which cloud service model is the customer responsible for managing the operating system?

- Infrastructure as a service (IaaS)

IaaS consists of virtual machines and networking provided by the cloud provider. The customer is responsible for the OS and applications. The cloud provider is responsible for the OS in PaaS and SaaS. [Describe cloud service types - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

#### Question 13 of 50

What is the customer responsible for in a software as a service (SaaS) model?

- data and access

SaaS allows you to pay to use an existing application on hardware managed by a third party. You supply data and configure access. Customers are only responsible for storage in a private cloud. Customers are responsible for virtual machines and runtime in IaaS and the private cloud. [Describe cloud service types - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

#### Question 14 of 50

What uses the infrastructure as a service (IaaS) cloud service model?

- Azure virtual machines

Azure Virtual Machines is an IaaS offering. The customer is responsible for the configuration of the virtual machine as well as all operating system configurations. Azure App Services and Azure Cosmos DB are PaaS offerings. Microsoft Office 365 is a SaaS offering. [Describe cloud service types - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cloud-service-types/)

#### Question 15 of 50

Select the answer that correctly completes the sentence.

**[Answer choice]** is the logical container used to combine and organize Azure resources.

- a resource group
- 
Resources are combined into resource groups, which act as a logical container into which Azure resources like web apps, databases, and storage accounts, are deployed and managed. [Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 16 of 50

Select the answer that correctly completes the sentence.

In a region pair, a region is paired with another region in the same **[answer choice]**.

- geography

Each Azure region is always paired with another region within the same geography, such as US, Europe, or Asia, at least 300 miles away. [Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 17 of 50

What is an Azure Storage account named storage001 an example of?

- a resource

A resource is a manageable item that is available through Azure. Virtual machines, storage accounts, web apps, databases, and virtual networks are examples of resources. [Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 18 of 50

For which resource does Azure generate separate billing reports and invoices by default?

- subscriptions

Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs. Resource groups can be used to group costs, but you will not receive a separate invoice for each resource group. Management groups are used to efficiently manage access, policies, and compliance for subscriptions. You can set up billing profiles to roll up subscriptions into invoice sections, but this requires customization. [Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 19 of 50

Which resource can you use to manage access, policies, and compliance across multiple subscriptions?

- management groups

Management groups can be used in environments that have multiple subscriptions to streamline the application of governance conditions. Resource groups can be used to organize Azure resources. A inistrative units are used to delegate the administration of Azure AD resources, such as users and groups. Accounts are used to provide access to resources

[Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 20 of 50

Select the answer that correctly completes the sentence.

**[Answer choice]** is the deployment and management service for Azure.

- Azure Resource Manager (ARM)

ARM is the deployment and management service for Azure. It provides a management layer that enables you to create, update, and delete resources in an Azure subscription. You use management features, such as access control, resource locks, and resource tags, to secure and organize resources after deployment. [Describe the core architectural components of Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/)

#### Question 21 of 50

What can you use to execute code in a serverless environment?

- Azure Functions

Azure Functions allows you to run code as a service without having to manage the underlying platform or infrastructure. Azure Logic Apps is similar to Azure Functions, but uses predefined workflows instead of developing your own code. [Describe Azure compute and networking services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/)

#### Question 22 of 50

What can you use to connect Azure resources, such as Azure SQL databases, to an Azure virtual network?

- service endpoints

Service endpoints are used to expose Azure services to a virtual network, providing communication between the two. ExpressRoute is used to connect an on-premises network to Azure. NSGs allow you to configure inbound and outbound rules for virtual networks and virtual machines. Peering allows you to connect virtual networks together. [Describe Azure compute and networking services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/)

#### Question 23 of 50

Which two services can you use to establish network connectivity between an on-premises network and Azure resources? Each correct answer presents a complete solution.

- Azure VPN Gateway
- ExpressRoute

ExpressRoute connections and Azure VPN Gateway are two services that you can use to connect an on-premises network to Azure. Bastion provides a web interface to remotely administer Azure virtual machines by using SSH/RDP. Azure Firewall is a stateful firewall service used to protect virtual networks. [Azure ExpressRoute: Connectivity models | Microsoft Learn](https://learn.microsoft.com/azure/expressroute/expressroute-connectivity-models). [Describe Azure compute and networking services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/)

#### Question 24 of 50

Which storage service should you use to store thousands of files containing text and images?

- Azure Blob storage
- 
Azure Blob storage is an object storage solution that you can use to store massive amounts of unstructured data, such as text or binary data. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 25 of 50

Which Azure Blob storage tier stores data offline and offers the lowest storage costs and the highest costs to access data?

- Archive

The Archive storage tier stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data. The Hot storage tier is optimized for storing data that is accessed frequently. Data in the Cool access tier can tolerate slightly lower availability, but still requires high durability, retrieval latency, and throughput characteristics similar to hot data. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 26 of 50

Which storage service offers fully managed file shares in the cloud that are accessible by using Server Message Block (SMB) protocol?

- Azure Files

Azure Files offers fully managed file shares in the cloud with shares that are accessible by using Server Message Block (SMB) protocol. Mounting Azure file shares is just like connecting to shares on a local network. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 27 of 50

Which two scenarios are common use cases for Azure Blob storage? Each correct answer presents a complete solution.

- serving images or documents directly to a browser
- storing data for backup and restore

Low storage costs and unlimited file formats make blob storage a good location to store backups and archives. Blob storage can be reached from anywhere by using an internet connection. Azure Disk Storage provides disks for Azure virtual machines. Azure Files supports mounting file storage shares. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 28 of 50

Which Azure Blob storage service tier has the highest storage costs and the fastest access times for reading and writing data?

- Hot

The Hot tier is optimized for storing data that is accessed frequently. The Cool access tier has a slightly lower availability SLA and higher access costs compared to hot data, which are acceptable trade-offs for lower storage costs. Archive storage stores data offline and offers the lowest storage costs, but also the highest costs to rehydrate and access data. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 29 of 50

Which two protocols are used to access Azure file shares? Each correct answer presents a complete solution.

- Network File System (NFS)
- Server Message Block (SMB)

Azure Files offers fully managed file shares in the cloud that are accessible via industry-standard SMB and NFS protocols. [Describe Azure storage services - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/)

#### Question 30 of 50

What enables a user to sign in one time and use that credential to access multiple resources and applications from different providers?

- single sign-on (SSO)

SSO enables a user to sign in one time and use that credential to access multiple resources and applications from different providers. MFA is a process whereby a user is prompted during the sign-in process for an additional form of identification. Conditional Access is a tool that Azure AD uses to allow or deny access to resources based on identity signals. Azure AD supports the registration of devices. [Describe Azure identity, access, and security - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)

#### Question 31 of 50

What can you use to allow a user to manage all the resources in a resource group?

- Azure role-based access control (RBAC)

Azure RBAC allows you to assign a set of permissions to a user or group. Resource tags are used to locate and act on resources associated with specific workloads, environments, business units, and owners. Resource locks prevent the accidental change or deletion of a resource. Key Vault is a centralized cloud service for storing an application secrets in a single, central location. [Describe Azure identity, access, and security - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)

#### Question 32 of 50

Which type of strategy uses a series of mechanisms to slow the advancement of an attack that aims to gain unauthorized access to data?

- defense in depth

A defense in depth strategy uses a series of mechanisms to slow the advancement of an attack that aims to gain unauthorized access to data. The principle of least privilege means restricting access to information to only the level that users need to perform their work. A DDoS attack attempts to overwhelm and exhaust an application's resources. The perimeter layer is about protecting an organization's resources from network-based attacks. [Describe Azure identity, access, and security - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)

#### Question 33 of 50

Which two services are provided by Azure AD? Each correct answer presents a complete solution.

- authentication
- single sign-on (SSO)

Azure AD provides services for verifying identity and access to applications and resources. SSO enables you to remember a single username and password to access multiple applications and is available in Azure AD. [Describe Azure identity, access, and security - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-azure-identity-access-security/)

#### Question 34 of 50

You have an Azure virtual machine that is accessed only between 9:00 and 17:00 each day.

What should you do to minimize costs but preserve the associated hard disks and data?

- Resize the virtual machine.   **This answer is incorrect.**

- Deallocate the virtual machine. **This answer is correct.**

If you have virtual machine workloads that are used only during certain periods, but you run them every hour of every day, then you are wasting money. These virtual machines are great candidates to deallocate when not in use and start back when required to save compute costs while the virtual machines are deallocated. [Describe cost management in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/)

#### Question 35 of 50

You need to associate the costs of resources to different groups within an organization without changing the location of the resources. What should you use?

- subscriptions.  **This answer is incorrect.**

- resource tags.  **This answer is correct.**

Resource tags can be used to group billing data and categorize costs by runtime environment, such as billing usage for virtual machines running in a production environment. [Tag resources, resource groups, and subscriptions for logical organization - Azure Resource Manager | Microsoft Learn](https://learn.microsoft.com/azure/azure-resource-manager/management/tag-resources?tabs=json). [Describe the purpose of tags - Training | Microsoft Learn](https://learn.microsoft.com/training/modules/describe-cost-management-azure/7-describe-purpose-of-tags)

#### Question 36 of 50

Your organization plans to deploy several production virtual machines that will have consistent resource usage throughout the year. What can you use to minimize the costs of the virtual machines without reducing the functionality of the virtual machines?

- Azure Reservations

Azure Reservations offers discounted prices on certain Azure services. Azure Reservations can save you up to 72 percent compared to pay-as-you-go prices. To receive a discount, you can reserve services and resources by paying in advance.Spending limits can suspend a subscription when the spend limit is reached. [Describe cost management in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/)

#### Question 37 of 50

What can be applied to a resource to prevent accidental deletion?

- a resource lock

A resource lock prevents resources from being accidentally deleted or changed. Resource tags offer the custom grouping of resources. Policies enforce different rules across all resource configurations so that the configurations stay compliant with corporate standards. An initiative is a way of grouping related policies together. [Describe features and tools in Azure for governance and compliance - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/)

#### Question 38 of 50

You need to recommend a solution for Azure virtual machine deployments. The solution must enforce company standards on the virtual machines. What should you include in the recommendation?

- Azure Blueprints. **This answer is incorrect.**

- Azure Policy.   **This answer is correct.**   

Azure policies will allow you to enforce company standards on new virtual machines when combined with Azure VM Image Builder and Azure Compute Gallery. By using Azure Policy and role-based access control (RBAC) assignments, enterprises can enforce standards on Azure resources. But on virtual machines, these mechanisms only affect the control plane or the route to the virtual machine. [Describe features and tools in Azure for governance and compliance - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/)

#### Question 39 of 50

You need to ensure that multi-factor authentication (MFA) is enabled on accounts with write permissions in an Azure subscription. What should you implement?

- Azure Policy

Azure Policy is a service in Azure that enables you to create, assign, and manage policies that control or audit resources. [Describe features and tools in Azure for governance and compliance - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-azure-for-governance-compliance/)

#### Question 40 of 50

What can you use to restrict the deployment of a virtual machine to a specific location?

- Azure Policy

Azure Policy can help to create a policy for allowed regions, which enables you to restrict the deployment of virtual machines to a specific location. [Overview of Azure Policy - Azure Policy | Microsoft Learn](https://learn.microsoft.com/azure/governance/policy/overview). [Describe the purpose of Azure Policy - Training | Microsoft Learn](https://learn.microsoft.com/training/modules/describe-features-tools-azure-for-governance-compliance/3-describe-purpose-of-azure-policy)

#### Question 41 of 50

Which management layer accepts requests from any Azure tool or API and enables you to create, update, and delete resources in an Azure account?

- Azure Resource Manager (ARM)

ARM is the deployment and management service for Azure. It provides a management layer that enables you to create, update, and delete resources in an Azure account. [Describe features and tools for managing and deploying Azure resources - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/)

#### Question 42 of 50

What can you use to manage servers across cloud platforms and on-premises environments?

- Azure Arc

Azure Arc simplifies governance and management by delivering a consistent multi-cloud and on-premises management platform. [Describe features and tools for managing and deploying Azure resources - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/). [Describe the purpose of Azure Arc - Training | Microsoft Learn](https://learn.microsoft.com/training/modules/describe-features-tools-manage-deploy-azure-resources/3-describe-purpose-of-azure-arc).

#### Question 43 of 50

What provides recommendations to reduce the cost of Azure resources?

- Azure Advisor

Azure Advisor analyzes the account usage and makes recommendations based on its set and configured rules. [Describe monitoring tools in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

#### Question 44 of 50

You have a team of Linux administrators that need to manage the resources in Azure. The team wants to use the Bash shell to perform the administration. What should you recommend?

- Azure CLI

Azure CLI allows you to use the Bash shell to perform administrative tasks. Bash is used in Linux environments, so a Linux administrator will probably be more comfortable performing command-line administration from Azure CLI. [Describe features and tools for managing and deploying Azure resources - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/)

#### Question 45 of 50

You need to create a custom solution that uses thresholds to trigger autoscaling functionality to scale an app up or down to meet user demand. What should you include in the solution?

- Application insights.  **This answer is incorrect.**

- Azure Monitor.  **This answer is correct.**

Azure Monitor is a platform that collects metric and logging data, such as CPU percentages. The data can be used to trigger autoscaling. [Describe monitoring tools in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

#### Question 46 of 50

What should you proactively review and act on to avoid service interruptions, such as service retirements and breaking changes?

- Azure Monitor. **This answer is incorrect.**

- health advisories. **This answer is correct.**

Health advisories are issues that require that you take proactive action to avoid service interruptions, such as service retirements and breaking changes. Service issues are problems such as outages that require immediate actions. [Describe monitoring tools in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

#### Question 47 of 50

What can you use to get notification about an outage in a specific Azure region?

- Azure Service Health

Service Health notifies you of Azure-related service issues, such as region-wide downtime. [Describe monitoring tools in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

#### Question 48 of 50

Which Azure service can generate an alert if virtual machine utilization is over 80% for five minutes?

- Azure Monitor

Azure Monitor is a platform for collecting, analyzing, visualizing, and alerting based on metrics. Azure Monitor can log data from an entire Azure and on-premises environment. [Describe monitoring tools in Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/describe-monitoring-tools-azure/)

#### Question 49 of 50

What can you apply to an Azure virtual machine to ensure that users cannot change or delete the resource?

- a lock

[Protect your Azure resources with a lock - Azure Resource Manager | Microsoft Learn](https://learn.microsoft.com/azure/azure-resource-manager/management/lock-resources?tabs=json) [Describe features and tools in Azure for governance and compliance - Training | Microsoft Learn](https://learn.microsoft.com/training/modules/describe-features-tools-azure-for-governance-compliance/)

#### Question 50 of 50

Which feature in the Microsoft Purview governance portal should you use to manage access to data sources and datasets?

**Your Answer**: 

- Data Estate Insights. **This answer is incorrect.**

- Data Policy. **This answer is correct.**

>Incorrect: Data Catalog –– This enables data discovery.
>
>Incorrect: Data Sharing –– This shares data within and between organizations.
>
>Incorrect: Data Estate Insights –– This accesses data estate health.
>
>Correct: Data Policy –– This governs access to data.

[Introduction to Microsoft Purview governance solutions - Microsoft Purview | Microsoft Learn](https://learn.microsoft.com/azure/purview/overview). [Describe features and tools in Azure for governance and compliance - Training | Microsoft Learn](https://learn.microsoft.com/training/modules/describe-features-tools-azure-for-governance-compliance/)



