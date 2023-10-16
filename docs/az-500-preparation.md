---
title: AZ-500 Microsoft Azure Security Technologies Certificate
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - azure
  - az-500
  - course
  - certification
---

# AZ-500 Microsoft Azure Security Technologies Certificate


!!! abstract "Sources of this notes:"
    - [The Microsoft e-learn platform](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-500/).
    - Book:  ["Microsoft Certified - MCA Microsoft Certified Associate Azure Security Engineer Study Guide: Exam AZ-500](https://www.amazon.es/Microsoft-Certified-Associate-Security-ngineer/dp/1119870372/). 
    - Udemy course:  [AZ-500 Microsoft Azure Security Technologies Exam Prep](https://eylearning.udemy.com/course/az500-azure/).
    - Udemy course: [Azure Security: AZ-500 (updated July 2023)](https://eylearning.udemy.com/course/azure-security-associate-az-500/)

## Introduction

These are some of the requirements for facing the az-500 highlighted by some experts:

- Have previously taken the Azure Administrator: AZ-103/104 course.
- A minimum of 1 year experience with Azure.
- Understand concepts of virtual machines, resource groups and Azure AD.

Since I only have two vouchers for azure certifications and I've already spent one on the [AZ-900](az-900-preparation.md), and I really want to focus on the AZ-500, I will complete the AZ-104 trainings like I was going to pass their exam and later on proceed to AZ-500 even though I don't have the official certificate for the AZ-104. [These are my notes for this AZ-104 not-certificated learning](az-104-preparation.md).


## Differences between the AZ-500 and the SC-900 certification

The [Exam AZ-500: Microsoft Azure Security Technologies](https://learn.microsoft.com/en-us/certifications/exams/az-500/ "learn.microsoft.com") is focused on Azure Security Engineer implements, manages, and monitors security for resources in Azure, multi-cloud, and hybrid environments as part of an end-to-end infrastructure. This Certification contains security components and configurations to protect identity & access, data, applications, and networks.

Regarding the [Exam SC-900: Microsoft Security, Compliance, and Identity Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/sc-900/ "learn.microsoft.com") is targeted to those looking to familiarize themselves with the fundamentals of security, compliance, and identity (SCI) across cloud-based and related Microsoft services. This is a broad audience that may include business stakeholders, new or existing IT professionals, or students who have an interest in Microsoft security, compliance, and identity solutions.


## Azure Active Directory 

**Azure Active Directory** (Azure AD) is a cloud-based identity and access management service.


### Azure Active Directory licenses

- **Azure Active Directory Free.** Provides user and group management, on-premises directory synchronization, basic reports, self-service password change for cloud users, and single sign-on across Azure, Microsoft 365, and many popular SaaS apps.
- **Azure Active Directory Premium P1.** In addition to the Free features, P1 lets your hybrid users access both on-premises and cloud resources. It also supports advanced administration, such as dynamic groups, self-service group management, Microsoft Identity Manager, and cloud write-back capabilities, which allow self-service password reset for your on-premises users.
- **Azure Active Directory Premium P2.** In addition to the Free and P1 features, P2 also offers Azure Active Directory Identity Protection to help provide risk-based Conditional Access to your apps and critical company data and Privileged Identity Management to help discover, restrict, and monitor administrators and their access to resources and to provide just-in-time access when needed.
- **"Pay as you go"** feature licenses. You also get additional feature licenses, such as Azure Active Directory Business-to-Customer (B2C). B2C can help you provide identity and access management solutions for your customer-facing apps.


### **Azure Active Directory Domain Services (Azure AD DS)** 

There are **two ways** to provide Active Directory Domain Services in the cloud:

- A _**managed domain**_ that you create using Azure Active Directory Domain Services (Azure AD DS). Microsoft creates and manages the required resources. **Azure AD DS**  deploys, manages, patches, and secures the active directory domain service  infrastructure for you. It's a managed domain experience. Azure AD DS provides a smaller subset of features to traditional self-managed AD DS environment, which reduces some of the design and management complexity. For example, there are no AD forests, domains, sites, and replication links to design and maintain. Also it guarantees access to traditional authentication mechanisms such as Kerberos or NTLM.
- A _**self-managed**_ domain that you create and configure using traditional resources such as virtual machines (VMs), Windows Server guest OS, and Active Directory Domain Services (AD DS). You then continue to administer these resources. You're then able to do additional tasks, such as extending the schema or create forest trust. Common deployment models in a self-managed domain are:
	- Standalone cloud-only AD DS: Azure VMs are configured as domain controllers, and a separate, cloud-only AD DS environment is created. This AD DS environment doesn't integrate with an on-premises AD DS environment. A different set of credentials is used to sign in and administer VMs in the cloud.
	- **Resource forest deployment** - Azure VMs are configured as domain controllers, and an AD DS domain that's part of an existing forest is created. A trust relationship is then configured to an on-premises AD DS environment. Other Azure VMs can domain-join this resource forest in the cloud. User authentication runs over a VPN / ExpressRoute connection to the on-premises AD DS environment.
	- **Extend on-premises domain to Azure** - An Azure virtual network connects to an on-premises network using a VPN / ExpressRoute connection. Azure VMs connect to this Azure virtual network, which lets them domain-join to the on-premises AD DS environment. An alternative is to create Azure VMs and promote them as replica domain controllers from the on-premises AD DS domain. These domain controllers replicate over a VPN / ExpressRoute connection to the on-premises AD DS environment. The on-premises AD DS domain is effectively extended into Azure.


The following table outlines some of the features you may need for your organization and the differences between a managed Azure AD DS domain or a self-managed AD DS domain:

|**Feature**|**Azure Active Directory Services (Azure AD DS)**|**Self-managed AD DS**|
|---|---|---|
|Managed service|✓|✕|
|Secure deployments|✓|The administrator secures the deployment|
|Domain Name System (DNS) server|✓ (managed service)|✓|
|Domain or Enterprise administrator privileges|✕|✓|
|Domain join|✓|✓|
|Domain authentication using New Technology LAN Manager (NTLM) and Kerberos|✓|✓|
|Kerberos constrained delegation|Resource-based|Resource-based & account-based|
|Custom organizational unit (OU) structure|✓|✓|
|Group Policy|✓|✓|
|Schema extensions|✕|✓|
|Active Directory domain/forest trusts|✓ (one-way outbound forest trusts only)|✓|
|Secure Lightweight Directory Access Protocols (LDAPs)|✓|✓|
|Lightweight Directory Access Protocol (LDAP) read|✓|✓|
|Lightweight Directory Access Protocol (LDAP) write|✓ (within the managed domain)|✓|
|Geographical-distributed (Geo-distributed) deployments|✓|✓|


### Signing devices to Azure Active Directory

Azure AD lets you manage the identity of devices used by the organization and control access to corporate resources from those devices. Users can also register their personal device (a bring-your-own (BYO) model) with Azure AD, which provides the device with an identity. Azure AD then authenticates the device when a user signs in to Azure AD and uses the device to access secured resources. The device can be managed using Mobile Device Management (MDM) software like Microsoft Intune. This management ability lets you restrict access to sensitive resources to managed and policy-compliant devices.


Azure AD joined devices give you the following benefits:

- Single sign-on (SSO) to applications secured by Azure AD.
- Enterprise policy-compliant roaming of user settings across devices.
- Access to the Windows Store for Business using corporate credentials.
- Windows Hello for Business.
- Restricted access to apps and resources from devices compliant with corporate policy.

The following table outlines common device ownership models and how they would typically be joined to a domain:

|**Type of device**|**Device platforms**|**Mechanism**|
|---|---|---|
|Personal devices|Windows 10, iOS, Android, macOS|Azure AD registered|
|Organization-owned device not joined to on-premises AD DS|Windows 10|Azure AD joined|
|Organization-owned device joined to an on-premises AD DS|Windows 10|Hybrid Azure AD joined|


The following table outlines differences in how the devices are represented and can authenticate themselves against the directory:

|**Aspect**|**Azure AD-joined**|**Azure AD DS-joined**|
|---|---|---|
|Device controlled by|Azure AD|Azure AD Domain Services managed domain|
|Representation in the directory|Device objects in the Azure AD directory|Computer objects in the Azure AD DS managed domain|
|Authentication|Open Authorization OAuth / OpenID Connect-based protocols. These protocols are designed to work over the internet, so are great for mobile scenarios where users access corporate resources from anywher|Kerberos and NTLM protocols, so it can support legacy applications migrated to run on Azure VMs as part of a lift-and-shift strategy|
|Management|Mobile Device Management (MDM) software like Intune|Group Policy|
|Networking|Works over the internet|Must be connected to, or peered with, the virtual network where the managed domain is deployed|
|Great for...|End-user mobile or desktop devices|Server VMs deployed in Azure|


>If on-premises AD DS and Azure AD are configured for federated authentication using Active Directory Federation Services (ADFS), then there's no (current/valid) password hash available in Azure DS. Azure AD user accounts created before fed auth was implemented might have an old password hash that doesn't match a hash of their on-premises password. Hence Azure AD DS won't validate the user's credentials.


### Roles in Azure Active Directory

Azure AD built-in roles differ in where they can be used, which fall into the following **three broad categories**.

1. **Azure AD-specific roles**: These roles grant permissions to manage resources within Azure AD only. For example, **User Administrator**, **Application Administrator**, and **Groups Administrator** all grant permissions to manage resources that live in Azure AD.
2. **Service-specific roles**: For major Microsoft 365 services (non-Azure AD), we have built service-specific roles that grant permissions to manage all features within the service. 
3. **Cross-service roles**: There are some roles that span services. We have two global roles - Global Administrator and Global Reader. All Microsoft 365 services honor these two roles. Also, there are some security-related roles like Security Administrator and Security Reader that grant access across multiple security services within Microsoft 365. **For example, using Security Administrator roles in Azure AD, you can manage Microsoft 365 Defender portal, Microsoft Defender Advanced Threat Protection, and Microsoft Defender for Cloud Apps**. 

The following table is offered as an aid to understanding these role categories. The categories are named arbitrarily and aren't intended to imply any other capabilities beyond the documented Azure AD role permissions.

|Category|Role|
|---|---|
|Azure AD-specific roles|Application Administrator  <br>Application Developer  <br>Authentication Administrator  <br>Business to consumer (B2C) Identity Experience Framework (IEF) Keyset Administrator  <br>Business to consumer (B2C) Identity Experience Framework (IEF) Policy Administrator  <br>Cloud Application Administrator  <br>Cloud Device Administrator  <br>Conditional Access Administrator  <br>Device Administrators  <br>Directory Readers  <br>Directory Synchronization Accounts  <br>Directory Writers  <br>External ID User Flow Administrator  <br>External ID User Flow Attribute Administrator  <br>External Identity Provider Administrator  <br>Groups Administrator  <br>Guest Inviter  <br>Helpdesk Administrator  <br>Hybrid Identity Administrator  <br>License Administrator  <br>Partner Tier1 Support  <br>Partner Tier2 Support  <br>Password Administrator  <br>Privileged Authentication Administrator  <br>Privileged Role Administrator  <br>Reports Reader  <br>User Administrator|
|Cross-service roles|Global Administrator  <br>Compliance Administrator  <br>Compliance Data Administrator  <br>Global Reader  <br>Security Administrator  <br>Security Operator  <br>Security Reader  <br>Service Support Administrator|
|Service-specific roles|Azure DevOps Administrator  <br>Azure Information Protection Administrator  <br>Billing Administrator  <br>Customer relationship management (CRM) Service Administrator  <br>Customer Lockbox Access Approver  <br>Desktop Analytics Administrator  <br>Exchange Service Administrator  <br>Insights Administrator  <br>Insights Business Leader  <br>Intune Service Administrator  <br>Kaizala Administrator  <br>Lync Service Administrator  <br>Message Center Privacy Reader  <br>Message Center Reader  <br>Modern Commerce User  <br>Network Administrator  <br>Office Apps Administrator  <br>Power BI Service Administrator  <br>Power Platform Administrator  <br>Printer Administrator  <br>Printer Technician  <br>Search Administrator  <br>Search Editor  <br>SharePoint Service Administrator  <br>Teams Communications Administrator  <br>Teams Communications Support Engineer  <br>Teams Communications Support Specialist  <br>Teams Devices Administrator  <br>Teams Administrator|


Additionally you have Azure AD built-in roles. These are all of them:

|**Role**|**Description**|
|---|---|
|**Application Administrator**|Users in this role can create and manage all aspects of enterprise applications, application registrations, and application proxy settings.  <br>Users assigned to this role aren't added as owners when creating new application registrations or enterprise applications.  <br>This role also grants the ability to consent for delegated permissions and application permissions, except for application permissions for Microsoft Graph.|
|Application Developer|Can create application registrations when the **Users can register applications** setting is set to No.|
|Attack Payload Author|Users in this role can create attack payloads but not actually launch or schedule them. Attack payloads are then available to all administrators in the tenant, who can use them to create a simulation.|
|Attack Simulation Administrator|Users in this role can create and manage all aspects of attack simulation creation, launch/scheduling of a simulation, and the review of simulation results. Members of this role have this access for all simulations in the tenant.|
|Attribute Assignment Administrator|Users with this role can assign and remove custom security attribute keys and values for supported Azure AD objects such as users, service principals, and devices. By default, Global Administrator and other administrator roles don't have permissions to read, define, or assign custom security attributes. To work with custom security attributes, you must be assigned one of the custom security attribute roles.|
|Attribute Assignment Reader|Users with this role can read custom security attribute keys and values for supported Azure AD objects. By default, Global Administrator and other administrator roles don't have permissions to read, define, or assign custom security attributes. You must be assigned one of the custom security attribute roles to work with custom security attributes.|
|Attribute Definition Administrator|Users with this role can define a valid set of custom security attributes that can be assigned to supported Azure AD objects. This role can also activate and deactivate custom security attributes. By default, Global Administrator and other administrator roles don't have permissions to read, define, or assign custom security attributes. To work with custom security attributes, you must be assigned one of the custom security attribute roles.|
|**Authentication Administrator**|Assign the Authentication Administrator role to users who need to do the following:  <br>  <br>-Set or reset any authentication method (including passwords) for nonadministrators and some roles.  <br>-Require users who are nonadministrators or assigned to some roles to re-register against existing nonpassword credentials (for example, **Multifactor authentication (MFA)** or **Fast ID Online (FIDO)**, and can also revoke remember MFA on the device, which prompts for MFA on the next sign-in.  <br>-Perform sensitive actions for some users.  <br>-Create and manage support tickets in Azure and the Microsoft 365 admin center.  <br>  <br>Users with this role can't do the following tasks:  <br>  <br>-Can't change the credentials or reset MFA for members and owners of a role-assignable group.  <br>-Can't manage MFA settings in the legacy MFA management portal or Hardware OATH tokens. The same functions can be accomplished using the Set-MsolUser commandlet Azure AD PowerShell module.|
|Authentication Policy Administrator|Assign the Authentication Policy Administrator role to users who need to do the following:  <br>  <br>-Configure the authentication methods policy, tenant-wide MFA settings, and password protection policy that determine which methods each user can register and use.  <br>-Manage Password Protection settings: smart lockout configurations and updating the custom banned passwords list.  <br>-Create and manage verifiable credentials.  <br>-Create and manage Azure support tickets.  <br>  <br>Users with this role can't do the following tasks:  <br>  <br>-Can't update sensitive properties.  <br>-Can't delete or restore users.  <br>-Can't manage MFA settings in the legacy MFA management portal or Hardware OATH tokens.|
|Azure AD Joined Device Local Administrator|This role is available for assignment only as another local administrator in Device settings. Users with this role become local machine administrators on all Windows 10 devices that are joined to Azure Active Directory. They don't have the ability to manage device objects in Azure Active Directory.|
|Azure DevOps Administrator|Users with this role can manage all enterprise Azure DevOps policies applicable to all Azure DevOps organizations backed by the Azure AD.  <br>Users in this role can manage these policies by navigating to any Azure DevOps organization that is backed by the company's Azure AD.  <br>Users in this role can claim ownership of orphaned Azure DevOps organizations. This role grants no other Azure DevOps-specific permissions (for example, Project Collection Administrators) inside any of the Azure DevOps organizations backed by the company's Azure AD organization.|
|Azure Information Protection Administrator|Users with this role have all permissions in the Azure Information Protection service. This role allows configuring labels for the Azure Information Protection policy, managing protection templates, and activating protection. This role doesn't grant any permissions in Identity Protection Center, Privileged Identity Management, Monitor Microsoft 365 Service Health, or Office 365 Security and compliance center.|
|Business-to-Consumer (B2C) Identity Experience Framework (IEF) Keyset Administrator|Users can create and manage policy keys and secrets for token encryption, token signatures, and claim encryption/decryption.  <br>By adding new keys to existing key containers, this limited administrator can roll over secrets as needed without impacting existing applications.  <br>This user can see the full content of these secrets and their expiration dates even after their creation.|
|Business-to-Consumer (B2C) Identity Experience Framework (IEF) Policy Administrator|Users in this role have the ability to create, read, update, and delete all custom policies in Azure AD B2C and therefore have full control over the Identity Experience Framework in the relevant Azure AD B2C organization. By editing policies, this user can establish direct federation with external identity providers, change the directory schema, change all user-facing content HyperText Markup Language (HTML), Cascading Style Sheets (CSS), JavaScript), change the requirements to complete authentication, create new users, send user data to external systems including full migrations, and edit all user information including sensitive fields like passwords and phone numbers. Conversely, this role can't change the encryption keys or edit the secrets used for federation in the organization.|
|Billing Administrator|Makes purchases, manages subscriptions, manages support tickets, and monitors service health.|
|Cloud App Security Administrator|Users with this role have full permissions in Defender for Cloud Apps. They can add administrators, add Microsoft Defender for Cloud Apps policies and settings, upload logs, and perform governance actions.|
|Cloud Application Administrator|Users in this role have the same permissions as the Application Administrator role, excluding the ability to manage application proxy. This role grants the ability to create and manage all aspects of enterprise applications and application registrations. Users assigned to this role aren't added as owners when creating new application registrations or enterprise applications. This role also grants the ability to consent for delegated permissions and application permissions, except for application permissions for Microsoft Graph.|
|Cloud Device Administrator|Users in this role can enable, disable, and delete devices in Azure AD and read Windows 10 BitLocker keys (if present) in the Azure portal. The role doesn't grant permissions to manage any other properties on the device.|
|Compliance Administrator|Users with this role have permissions to manage compliance-related features in the Microsoft Purview compliance portal, Microsoft 365 admin center, Azure, and Office 365 Security and compliance center. Assignees can also manage all features within the Exchange admin center and create support tickets for Azure and Microsoft 365.|
|Compliance Data Administrator|Users with this role have permissions to track data in the Microsoft Purview compliance portal, Microsoft 365 admin center, and Azure. Users can also track compliance data within the Exchange admin center, Compliance Manager, and Teams and Skype for Business admin center and create support tickets for Azure and Microsoft 365.|
|**Conditional Access Administrator**|Users with this role have the ability to manage Azure Active Directory Conditional Access settings.|
|Customer Lockbox Access Approver|Manages Microsoft Purview Customer Lockbox requests in your organization. They receive email notifications for Customer Lockbox requests and can approve and deny requests from the Microsoft 365 admin center. They can also turn the Customer Lockbox feature on or off. Only Global Administrators can reset the passwords of people assigned to this role.|
|Desktop Analytics Administrator|Users in this role can manage the Desktop Analytics service, including viewing asset inventory, creating deployment plans, and viewing deployment and health status.|
|Directory Readers|Users in this role can read basic directory information. This role should be used for:  <br>  <br>-Granting a specific set of guest users read access instead of granting it to all guest users.  <br>-Granting a specific set of nonadmin users access to the Azure portal when "**Restrict access to Azure AD portal to admins only**" is set to "**Yes**".  <br>-Granting service principals access to the directory where Directory.Read.All isn't an option.|
|Directory Synchronization Accounts|Don't use. This role is automatically assigned to the Azure AD Connect service and isn't intended or supported for any other use.|
|Directory Writers|Users in this role can read and update basic information of users, groups, and service principals.|
|Domain Name Administrator|Users with this role can manage (**read**, **add**, **verify**, **update**, and **delete**) domain names. They can also read directory information about users, groups, and applications, as these objects possess domain dependencies. For on-premises environments, users with this role can configure domain names for federation so that associated users are always authenticated on-premises. These users can then sign into Azure AD-based services with their on-premises passwords via single sign-on. Federation settings need to be synced via Azure AD Connect so users also have permissions to manage Azure AD Connect.|
|Dynamics 365 Administrator|Users with this role have global permissions within Microsoft Dynamics 365 Online when the service is present, and the ability to manage support tickets and monitor service health.|
|Edge Administrator|Users in this role can create and manage the enterprise site list required for Internet Explorer mode on Microsoft Edge. This role grants permissions to create, edit, and publish the site list and additionally allows access to manage support tickets.|
|Exchange Administrator|Users with this role have global permissions within Microsoft Exchange Online, when the service is present. Also has the ability to create and manage all Microsoft 365 groups, manage support tickets, and monitor service health.|
|Exchange Recipient Administrator|Users with this role have read access to recipients and write access to the attributes of those recipients in Exchange Online.|
|External ID User Flow Administrator|Users with this role can create and manage user flows (also called "**built-in**" policies) in the Azure portal. These users can customize HTML/CSS/JavaScript content, change MFA requirements, select claims in the token, manage API connectors and their credentials, and configure session settings for all user flows in the Azure AD organization. On the other hand, this role doesn't include the ability to review user data or make changes to the attributes that are included in the organization schema. Changes to Identity Experience Framework policies (also known as custom policies) are also outside the scope of this role.|
|External ID User Flow Attribute Administrator|Users with this role add or delete custom attributes available to all user flows in the Azure AD organization.  <br>Users with this role can change or add new elements to the end-user schema and impact the behavior of all user flows, and indirectly result in changes to what data may be asked of end users and ultimately sent as claims to applications. This role can't edit user flows.|
|External Identity Provider Administrator|This administrator manages federation between Azure AD organizations and external identity providers. With this role, users can add new identity providers and configure all available settings (for example, authentication path, service ID, assigned key containers). This user can enable the Azure AD organization to trust authentications from external identity providers. The resulting impact on end-user experiences depends on the type of organization:  <br>  <br>-Azure AD organizations for employees and partners: The addition of a federation (for example, with Gmail) immediately impacts all guest invitations not yet redeemed. See Adding Google as an identity provider for B2B guest users.  <br>  <br>-Azure Active Directory B2C organizations: The addition of a federation (for example, with Facebook, or with another Azure AD organization) doesn't immediately impact end-user flows until the identity provider is added as an option in a user flow (also called a built-in policy).|
|**Global Administrator**|Users with this role have access to all administrative features in Azure Active Directory, and services that use Azure Active Directory identities like the Microsoft 365 Defender portal, the Microsoft Purview compliance portal, Exchange Online, SharePoint Online, and Skype for Business Online. Furthermore, Global Administrators can elevate their access to manage all Azure subscriptions and management groups. This allows Global Administrators to get full access to all Azure resources using the respective Azure AD Tenant. The person who signs up for the Azure AD organization becomes a Global Administrator. There can be more than one Global Administrator at your company. Global Administrators can reset the password for any user and all other administrators.|
|**Global Administrator**|As a best practice, Microsoft recommends that you assign the Global Administrator role to **fewer than five people** in your organization.|
|Global Reader|Users in this role can read settings and administrative information across Microsoft 365 services but can't take management actions. Global Reader is the read-only counterpart to Global Administrator. Assign Global Reader instead of Global Administrator for planning, audits, or investigations. Use Global Reader in combination with other limited admin roles like Exchange Administrator to make it easier to get work done without the assigning the Global Administrator role. Global Reader works with Microsoft 365 admin center, Exchange admin center, SharePoint admin center, Teams admin center, Security center, compliance center, Azure AD admin center, and Device Management admin center.  <br>  <br>Users with this role can't do the following tasks:  <br>  <br>-Can't access the Purchase Services area in the Microsoft 365 admin center.|
|**Groups Administrator**|Users in this role can create/manage groups and its settings like naming and expiration policies. It's important to understand that assigning a user to this role gives them the ability to manage all groups in the organization across various workloads like Teams, SharePoint, Yammer in addition to Outlook. Also the user is able to manage the various groups settings across various admin portals like Microsoft admin center, Azure portal, and workload specific ones like Teams and SharePoint admin centers.|
|Guest Inviter|Users in this role can manage Azure Active Directory B2B guest user invitations when the Members can invite user setting is set to **No**.|
|Helpdesk Administrator|Users with this role can change passwords, invalidate refresh tokens, create and manage support requests with Microsoft for Azure and Microsoft 365 services, and monitor service health. Invalidating a refresh token forces the user to sign in again. Whether a Helpdesk Administrator can reset a user's password and invalidate refresh tokens depends on the role the user is assigned.  <br>  <br>Users with this role **can't** do the following:  <br>  <br>-Can't change the credentials or reset MFA for members and owners of a **role-assignable group**.|
|Hybrid Identity Administrator|Users in this role can create, manage and deploy provisioning configuration setup from AD to Azure AD using Cloud Provisioning and manage Azure AD Connect, Pass-through Authentication (PTA), Password hash synchronization (PHS), Seamless single sign-on (Seamless SSO), and federation settings. Users can also troubleshoot and monitor logs using this role.|
|Identity Governance Administrator|Users with this role can manage Azure AD identity governance configuration, including access packages, access reviews, catalogs and policies, ensuring access is approved and reviewed and guest users who no longer need access are removed.|
|Insights Administrator|Users in this role can access the full set of administrative capabilities in the Microsoft Viva Insights app. This role has the ability to read directory information, monitor service health, file support tickets, and access the Insights Administrator settings aspects.|
|Insights Analyst|Assign the Insights Analyst role to users who need to do the following tasks:  <br>  <br>-Analyze data in the Microsoft Viva Insights app, but can't manage any configuration settings  <br>-Create, manage, and run queries  <br>-View basic settings and reports in the Microsoft 365 admin center  <br>-Create and manage service requests in the Microsoft 365 admin center|
|Insights Business Leader|Users in this role can access a set of dashboards and insights via the Microsoft Viva Insights app. This includes full access to all dashboards and presented insights and data exploration functionality. Users in this role don't have access to product configuration settings, which is the responsibility of the Insights Administrator role.|
|Intune Administrator|Users with this role have global permissions within Microsoft Intune Online, when the service is present. Additionally, this role contains the ability to manage users and devices to associate policy and create and manage groups. This role can create and manage all security groups. However, Intune Administrator doesn't have admin rights over Office groups. That means the admin can't update owners or memberships of all Office groups in the organization. However, you can manage the Office group that's created, which comes as a part of end-user privileges. So, any Office group (not security group) that you create should be counted against your quota of 250.|
|Kaizala Administrator|Users with this role have global permissions to manage settings within Microsoft Kaizala, when the service is present and the ability to manage support tickets and monitor service health. Additionally, the user can access reports related to adoption and usage of Kaizala by Organization members and business reports generated using the Kaizala actions.|
|Knowledge Administrator|Users in this role have full access to all knowledge, learning and intelligent features settings in the Microsoft 365 admin center. They have a general understanding of the suite of products, licensing details and have responsibility to control access. Knowledge Administrator can create and manage content, like topics, acronyms and learning resources. Additionally, these users can create content centers, monitor service health, and create service requests.|
|Knowledge Manager|Users in this role can create and manage content, like topics, acronyms and learning content. These users are primarily responsible for the quality and structure of knowledge. This user has full rights to topic management actions to confirm a topic, approve edits, or delete a topic. This role can also manage taxonomies as part of the term store management tool and create content centers.|
|License Administrator|Users in this role can add, remove, and update license assignments on users, groups (using group-based licensing), and manage the usage location on users. The role doesn't grant the ability to purchase or manage subscriptions, create or manage groups, or create or manage users beyond the usage location. This role has no access to view, create, or manage support tickets.|
|Lifecycle Workflows Administrator|Assign the Lifecycle Workflows Administrator role to users who need to do the following tasks:  <br>  <br>-Create and manage all aspects of workflows and tasks associated with Lifecycle Workflows in Azure AD  <br>-Check the execution of scheduled workflows  <br>-Launch on-demand workflow runs  <br>-Inspect workflow execution logs|
|Message Center Privacy Reader|Users in this role can monitor all notifications in the Message Center, including data privacy messages. Message Center Privacy Readers get email notifications including those related to data privacy and they can unsubscribe using Message Center Preferences. Only the Global Administrator and the Message Center Privacy Reader can read data privacy messages. Additionally, this role contains the ability to view groups, domains, and subscriptions. This role has no permission to view, create, or manage service requests.|
|Message Center Reader|Users in this role can monitor notifications and advisory health updates in Message center for their organization on configured services such as Exchange, Intune, and Microsoft Teams. Message Center Readers receive weekly email digests of posts, updates, and can share message center posts in Microsoft 365. In Azure AD, users assigned to this role will only have read-only access on Azure AD services such as users and groups. This role has no access to view, create, or manage support tickets.|
|Microsoft Hardware Warranty Administrator|Assign the Microsoft Hardware Warranty Administrator role to users who need to do the following tasks:  <br>  <br>-Create new warranty claims for Microsoft manufactured hardware, like Surface and HoloLens  <br>-Search and read opened or closed warranty claims  <br>-Search and read warranty claims by serial number  <br>-Create, read, update, and delete shipping addresses  <br>-Read shipping status for open warranty claims  <br>-Create and manage service requests in the Microsoft 365 admin center  <br>-Read Message center announcements in the Microsoft 365 admin center|
|Microsoft Hardware Warranty Specialist|Assign the Microsoft Hardware Warranty Specialist role to users who need to do the following tasks:  <br>  <br>-Create new warranty claims for Microsoft manufactured hardware, like Surface and HoloLens  <br>-Read warranty claims that they created  <br>-Read and update existing shipping addresses  <br>-Read shipping status for open warranty claims they created  <br>-Create and manage service requests in the Microsoft 365 admin center|
|Modern Commerce User|**Don't use**. This role is automatically assigned from Commerce, and isn't intended or supported for any other use.  <br>The Modern Commerce User role gives certain users permission to access Microsoft 365 admin center and see the left navigation entries for Home, Billing, and Support. The content available in these areas is controlled by commerce-specific roles assigned to users to manage products that they bought for themselves or your organization. This might include tasks like paying bills, or for access to billing accounts and billing profiles. Users with the Modern Commerce User role typically have administrative permissions in other Microsoft purchasing systems, but don't have Global Administrator or Billing Administrator roles used to access the admin center.|
|**Network Administrator**|Users in this role can review network perimeter architecture recommendations from Microsoft that are based on network telemetry from their user locations. Network performance for Microsoft 365 relies on careful enterprise customer network perimeter architecture, which is generally user location specific. This role allows for editing of discovered user locations and configuration of network parameters for those locations to facilitate improved telemetry measurements and design recommendations|
|Office Apps Administrator|Users in this role can manage Microsoft 365 apps' cloud settings. This includes managing cloud policies, self-service download management and the ability to view Office apps related report. This role additionally grants the ability to manage support tickets, and monitor service health within the main admin center. Users assigned to this role can also manage communication of new features in Office apps.|
|Organizational Messages Writer|Assign the Organizational Messages Writer role to users who need to do the following tasks:  <br>**  <br>-Write**, **publish**, and **delete** organizational messages using Microsoft 365 admin center or Microsoft Endpoint Manager  <br>**-Manage** organizational message delivery options using Microsoft 365 admin center or Microsoft Endpoint Manager  <br>**-Read** organizational message delivery results using Microsoft 365 admin center or Microsoft Endpoint Manager  <br>**-View** usage reports and most settings in the Microsoft 365 admin center, but can't make changes|
|Partner Tier1 Support|**Don't use**. This role has been deprecated and will be removed from Azure AD in the future. This role is intended for use by a few Microsoft resale partners, and isn't intended for general use.|
|Partner Tier2 Support|**Don't use**. This role has been deprecated and will be removed from Azure AD in the future. This role is intended for use by a few Microsoft resale partners, and isn't intended for general use.|
|**Password Administrator**|Users with this role have limited ability to manage passwords. This role doesn't grant the ability to manage service requests or monitor service health. Whether a Password Administrator can reset a user's password depends on the role the user is assigned.Users with this role **can't** do the following tasks:  <br>  <br>-Can't change the credentials or reset MFA for members and owners of a role-assignable group.|
|Permissions Management Administrator|Assign the Permissions Management Administrator role to users who need to do the following tasks:  <br>**  <br>-Manage** all aspects of Entra Permissions Management, when the service is present|
|Power Business Intelligence (BI) Administrator|Users with this role have global permissions within Microsoft Power BI, when the service is present and the ability to manage support tickets and monitor service health.|
|Power Platform Administrator|Users in this role can create and manage all aspects of environments, Power Apps, Flows, Data Loss Prevention policies. Additionally, users with this role have the ability to manage support tickets and monitor service health.|
|Printer Administrator|Users in this role can register printers and manage all aspects of all printer configurations in the Microsoft Universal Print solution, including the Universal Print Connector settings. They can consent to all delegated print permission requests. Printer Administrators also have access to print reports.|
|Printer Technician|Users with this role can register printers and manage printer status in the Microsoft Universal Print solution. They can also read all connector information. Key task a Printer Technician can't do is set user permissions on printers and sharing printers.|
|Privileged Authentication Administrator|Assign the Privileged Authentication Administrator role to users who need to do the following tasks:  <br>**  <br>-Set** or **reset** any authentication method (including passwords) for any user, including Global Administrators.  <br>**  <br>-Delete** or **restore** any users, including Global Administrators. For more information, see Who can perform sensitive actions.  <br>  <br>-Force users to re-register against existing nonpassword credential (such as MFA or FIDO) and revoke remember MFA on the device, prompting for MFA on the next sign-in of all users.  <br>**  <br>-Update** sensitive properties for all users. For more information, see Who can perform sensitive actions.  <br>**  <br>-Create** and **manage** support tickets in Azure and the Microsoft 365 admin center.  <br>  <br>Users with this role can't do the following tasks:  <br>  <br>-Can't manage per-user MFA in the legacy MFA management portal. The same functions can be accomplished using the Set-MsolUser commandlet Azure AD PowerShell module.|
|Privileged Role Administrator|Users with this role can manage role assignments in Azure Active Directory and within Azure AD Privileged Identity Management. They can create and manage groups that can be assigned to Azure AD roles. In addition, this role allows management of all aspects of Privileged Identity Management and administrative units.|
|**Privileged Role Administrator**|**This role grants the ability to manage assignments for all Azure AD roles including the Global Administrator role**. This role doesn't include any other privileged abilities in Azure AD like creating or updating users. However, users assigned to this role can grant themselves or others another privilege by assigning extra roles.|
|Reports Reader|Users with this role can view usage reporting data and the reports dashboard in Microsoft 365 admin center and the adoption context pack in Power Business Intelligence (Power BI). Additionally, the role provides access to all sign-in logs, audit logs, and activity reports in Azure AD and data returned by the Microsoft Graph reporting API. A user assigned to the Reports Reader role can access only relevant usage and adoption metrics. They don't have any admin permissions to configure settings or access the product-specific admin centers like Exchange. This role has no access to view, create, or manage support tickets.|
|Search Administrator|Users in this role have full access to all Microsoft Search management features in the Microsoft 365 admin center. Additionally, these users can view the message center, monitor service health, and create service requests.|
|Search Editor|Users in this role can create, manage, and delete content for Microsoft Search in the Microsoft 365 admin center, including bookmarks, questions and answers, and locations.|
|Security Administrator|Users with this role have permissions to manage security-related features in the Microsoft 365 Defender portal, Azure Active Directory Identity Protection, Azure Active Directory Authentication, Azure Information Protection, and Office 365 Security and compliance center.|
|Security Operator|Users with this role can manage alerts and have global read-only access on security-related features, including all information in Microsoft 365 security center, Azure Active Directory, Identity Protection, Privileged Identity Management and Office 365 Security & compliance center.|
|Security Reader|Users with this role have global read-only access on security-related feature, including all information in Microsoft 365 security center, Azure Active Directory, Identity Protection, Privileged Identity Management, and the ability to read Azure Active Directory sign-in reports and audit logs, and in Office 365 Security and compliance center.|
|Service Support Administrator|Users with this role can create and manage support requests with Microsoft for Azure and Microsoft 365 services, and view the service dashboard and message center in the Azure portal and Microsoft 365 admin center.|
|SharePoint Administrator|Users with this role have global permissions within Microsoft SharePoint Online, when the service is present, and the ability to create and manage all Microsoft 365 groups, manage support tickets, and monitor service health.|
|Skype for Business Administrator|Users with this role have global permissions within Microsoft Skype for Business, when the service is present, and manage Skype-specific user attributes in Azure Active Directory. Additionally, this role grants the ability to manage support tickets and monitor service health, and to access the Teams and Skype for Business admin center. The account must also be licensed for Teams or it can't run Teams PowerShell cmdlets.|
|Teams Administrator|Users in this role can manage all aspects of the Microsoft Teams workload via the Microsoft Teams and Skype for Business admin center and the respective PowerShell modules. This includes, among other areas, all management tools related to telephony, messaging, meetings, and the teams themselves. This role additionally grants the ability to create and manage all Microsoft 365 groups, manage support tickets, and monitor service health.|
|Teams Communications Administrator|Users in this role can manage aspects of the Microsoft Teams workload related to voice and telephony. This includes the management tools for telephone number assignment, voice and meeting policies, and full access to the call analytics toolset.|
|Teams Communications Support Engineer|Users in this role can troubleshoot communication issues within Microsoft Teams and Skype for Business using the user call troubleshooting tools in the Microsoft Teams and Skype for Business admin center. Users in this role can view full call record information for all participants involved. This role has no access to view, create, or manage support tickets.|
|Teams Communications Support Specialist|Users in this role can troubleshoot communication issues within Microsoft Teams and Skype for Business using the user call troubleshooting tools in the Microsoft Teams and Skype for Business admin center. Users in this role can only view user details in the call for the specific user they've looked up. This role has no access to view, create, or manage support tickets.|
|Teams Devices Administrator|Users with this role can manage Teams-certified devices from the Teams admin center. This role allows viewing all devices at single glance, with ability to search and filter devices. The user can check details of each device including logged-in account, make and model of the device. The user can change the settings on the device and update the software versions. This role doesn't grant permissions to check Teams activity and call quality of the device.|
|Tenant Creator|Assign the Tenant Creator role to users who need to do the following tasks:  <br>**  <br>-Create** both Azure Active Directory and Azure Active Directory B2C tenants even if the tenant creation toggle is turned off in the user settings|
|Usage Summary Reports Reader|Users with this role can access tenant level aggregated data and associated insights in Microsoft 365 admin center for Usage and Productivity Score but can't access any user level details or insights. In Microsoft 365 admin center for the two reports, we differentiate between tenant level aggregated data and user level details. This role gives an extra layer of protection on individual user identifiable data, which was requested by both customers and legal teams.|
|**User Administrator**|Assign the User Administrator role to users who need to do the following tasks:  <br>  <br>-Create users  <br>  <br>-Update most user properties for all users, including all administrators  <br>  <br>-Update sensitive properties (including user principal name) for some users  <br>  <br>-Disable or enable some users  <br>  <br>-Delete or restore some users  <br>  <br>-Create and manage user views  <br>  <br>-Create and manage all groups  <br>  <br>-Assign licenses for all users, including all administrators  <br>  <br>-Reset passwords  <br>  <br>-Invalidate refresh tokens  <br>  <br>-Update (FIDO) device keys  <br>  <br>-Update password expiration policies  <br>  <br>-Create and manage support tickets in Azure and the Microsoft 365 admin center  <br>  <br>-Monitor service healthUsers with this role **can't** do the following tasks:  <br>  <br>-Can't manage MFA.  <br>  <br>-Can't change the credentials or reset MFA for members and owners of a role-assignable group.  <br>  <br>-Can't manage shared mailboxes|
|**User Administrator**|Users with this role can **change passwords** for people who may have access to sensitive or private information or critical configuration inside and outside of Azure Active Directory. Changing the password of a user may mean the ability to assume that user's identity and permissions.  <br>  <br>For example:  <br>**  <br>-Application Registration and Enterprise Application owners**, who can manage credentials of apps they own. Those apps may have privileged permissions in Azure AD and elsewhere not granted to User Administrators. Through this path, a User Administrator may be able to assume the identity of an application owner and then further assume the identity of a privileged application by updating the credentials for the application.  <br>**  <br>-Azure subscription owners**, who may have access to sensitive or private information or critical configuration in Azure.  <br>**  <br>-Security Group and Microsoft 365 group owners**, who can manage group membership. Those groups may grant access to sensitive or private information or critical configuration in Azure AD and elsewhere.  <br>**  <br>-Administrators in other services outside of Azure AD like Exchange Online**, Office Security and compliance center, and human resources systems.  <br>**  <br>-Nonadministrators** like executives, legal counsel, and human resources employees who may have access to sensitive or private information.|
|Virtual Visits Administrator|Users with this role can do the following tasks:  <br>  <br>-Manage and configure all aspects of Virtual Visits in Bookings in the Microsoft 365 admin center, and in the Teams Electronic Health Record (EHR) connector  <br>  <br>-View usage reports for Virtual Visits in the Teams admin center, Microsoft 365 admin center, and Power BI  <br>  <br>-View features and settings in the Microsoft 365 admin center, but can't edit any settings|
|Windows 365 Administrator|Users with this role have global permissions on Windows 365 resources, when the service is present. Additionally, this role contains the ability to manage users and devices in order to associate policy and create and manage groups.  <br>This role can create and manage security groups, but doesn't have administrator rights over Microsoft 365 groups. That means administrators can't update owners or memberships of Microsoft 365 groups in the organization. However, they can manage the Microsoft 365 group they create, which is a part of their end-user privileges. So, any Microsoft 365 group (not security group) they create is counted against their quota of 250.  <br>Assign the Windows 365 Administrator role to users who need to do the following tasks:  <br>  <br>-Manage Windows 365 Cloud PCs in Microsoft Endpoint Manager  <br>-Enroll and manage devices in Azure AD, including assigning users and policies  <br>-Create and manage security groups, but not role-assignable groups  <br>-View basic properties in the Microsoft 365 admin center  <br>-Read usage reports in the Microsoft 365 admin center  <br>-Create and manage support tickets in Azure and the Microsoft 365 admin center|
|Windows Update Deployment Administrator|Users in this role can create and manage all aspects of Windows Update deployments through the Windows Update for Business deployment service. The deployment service enables users to define settings for when and how updates are deployed, and specify which updates are offered to groups of devices in their tenant. It also allows users to monitor the update progress.|
|Yammer Administrator|Assign the Yammer Administrator role to users who need to do the following tasks:  <br>**  <br>-Manage** all aspects of Yammer  <br>**-Create**, **manage**, and **restore** Microsoft 365 Groups, but not role-assignable groups  <br>-View the hidden members of Security groups and Microsoft 365 groups, including role assignable groups  <br>**-Read usage reports** in the Microsoft 365 admin center  <br>**-Create** and **manage** service requests in the Microsoft 365 admin center  <br>**-View announcements** in the Message center, but not security announcements  <br>**-View** service health|



### Deploy Azure Active Directory Domain Services

Azure Active Directory Domain Services (Azure AD DS) provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/New Technology LAN Manager (NTLM) authentication. You use these domain services without the need to deploy, manage, and patch domain controllers (DCs) in the cloud.

Azure AD DS integrates with your existing Azure AD tenant. This integration lets users sign in to services and applications connected to the managed domain using their existing credentials.

When you create an Azure AD DS managed domain, you define a unique namespace. This namespace is the domain name, such as _aaddscontoso.com_. Two Windows Server domain controllers (DCs) are then deployed into your selected Azure region. This deployment of DCs is known as a replica set. You can expand a managed domain to have more than one replica set per Azure AD tenant. Replica sets can be added to any peered virtual network in any Azure region that supports Azure AD DS. You don't need to manage, configure, or update these DCs. The Azure platform handles the DCs as part of the managed domain, including backups and encryption at rest using Azure Disk Encryption.

Azure AD DS replicates identity information from Azure AD, so it works with Azure AD tenants that are cloud-only or synchronized with an on-premises AD DS environment. Azure AD DS performs a one-way synchronization from Azure AD to provide access to a central set of users, groups, and credentials. You can create resources directly in the managed domain (Azure ADDS), but they aren't synchronized back to Azure AD.

![Azure ADDS](img/az-500_1.png)




5. **Azure Active Directory (Azure AD) - Cloud-based** identity and mobile device management that provides user account and authentication services for resources such as Microsoft 365, the Azure portal, or SaaS applications.
    - Azure AD can be synchronized with an on-premises AD DS environment to provide a single identity to users that works natively in the cloud.
6. **Active Directory Domain Services (AD DS)** - **Enterprise-ready lightweight directory access protocol (LDAP) server** that provides key features such as identity and authentication, computer object management, group policy, and trusts.
    - AD DS is a central component in many organizations with an on-premises IT environment and provides core user account authentication and computer management features.
7. **Azure Active Directory Domain Services (Azure AD DS)** - **Provides managed domain services** with a subset of fully compatible traditional AD DS features such as domain join, group policy, LDAP, and Kerberos / New Technology LAN Manager (NTLM) authentication.
    - Azure AD DS integrates with Azure AD, which can synchronize with an on-premises AD DS environment. This ability extends central identity use cases to traditional web applications that run in Azure as part of a lift-and-shift strategy.


### Create and manage Azure AD users
	
Note for deleted users:

The user is deleted and no longer appears on the **Users** - **All users** page. The user can be seen on the **Deleted users** page for the next **30 days** and can be restored during that time. When a user is deleted, any licenses consumed by the user are made available for other users.

To update the identity, contact information, or job information for users whose source of authority is Windows Server Active Directory, you must use Windows Server Active Directory. After you complete the update, you must wait for the next synchronization cycle to complete before you see the changes.


### Manage users with Azure AD groups

Azure AD lets you use groups to manage access to applications, data, and resources. Resources can be:

- Part of the Azure AD organization, such as permissions to manage objects through roles in Azure AD
- External to the organization, such as for Software as a Service (SaaS) apps
- Azure services
- SharePoint sites
- On-premises resources

There are **two group types** and **three group membership types**.

**Group types**:
- **Security**: Used to manage user and computer access to shared resources.
- **Microsoft 365**: Provides collaboration opportunities by giving group members access to a shared mailbox, calendar, files, SharePoint sites, and more.

**Membership types**:

- **Assigned**: Lets you add specific users as members of a group and have unique permissions.
- **Dynamic user**: Lets you use dynamic membership rules to automatically add and remove members. If a member's attributes change, the system looks at your dynamic group rules for the directory to see if the member meets the rule requirements (is added), or no longer meets the rules requirements (is removed).
- **Dynamic device**: Lets you use dynamic group rules to automatically add and remove devices. If a device's attributes change, the system looks at your dynamic group rules for the directory to see if the device meets the rule requirements (is added), or no longer meets the rules requirements (is removed).

You can create a dynamic group for either devices or users but not for both. You can't create a device group based on the device owners' attributes. Device membership rules can only reference device attributions.

### Configure Azure AD administrative units

 An administrative unit can contain only users and groups. Administrative units restrict permissions in a role to any portion of your organization that you define. You could, for example, use administrative units to delegate the Helpdesk Administrator role to regional support specialists

## Available roles

|**Role**|**Description**|
|---|---|
|Authentication Administrator|Has access to view, set, and reset authentication method information for any non-admin user in the assigned administrative unit only.|
|Groups Administrator|Can manage all aspects of groups and groups settings, such as naming and expiration policies, in the assigned administrative unit only.|
|Helpdesk Administrator|Can reset passwords for non-administrators and Helpdesk administrators in the assigned administrative unit only.|
|License Administrator|Can assign, remove, and update license assignments within the administrative unit only.|
|Password Administrator|Can reset passwords for non-administrators and Password Administrators within the assigned administrative unit only.|
|User Administrator|Can manage all aspects of users and groups, including resetting passwords for limited admins within the assigned administrative unit only.|



### Pawordless authentication

 Microsoft global Azure and Azure Government offer the following **three** passwordless authentication options that integrate with Azure Active Directory (Azure AD):

1. Windows Hello for Business: Windows Hello for Business is ideal for information workers that have their own designated Windows PC. The biometric and PIN credentials are directly tied to the user's PC, which prevents access from anyone other than the owner. With public key infrastructure (PKI) integration and built-in support for single sign-on (SSO), Windows Hello for Business provides a convenient method for seamlessly accessing corporate resources on-premises and in the cloud.
2. Microsoft Authenticator: You can also allow your employee's phone to become a passwordless authentication method. You may already be using the Authenticator app as a convenient multi-factor authentication option in addition to a password. You can also use the Authenticator App as a passwordless option.
3. Fast Identity Online2 (**FIDO2**) security keys: The FIDO (Fast IDentity Online) Alliance helps to promote open authentication standards and reduce the use of passwords as a form of authentication. FIDO2 is the latest standard that incorporates the web authentication (WebAuthn) standard. Users can register and then select a FIDO2 security key at the sign-in interface as their main means of authentication. These FIDO2 security keys are typically USB devices but could also use Bluetooth or Near-Field Communication (NFC).

### Azure storage security

**Azure Storage Service Encryption**
When a new storage account is provisioned, Azure Storage Encryption is automatically enabled for it and it cannot be disabled. With 256-BIT AES ENCRYPTION. All storage accounts are encrypted with no distinction or cost.

**Shared access signatures**
Three types: 
- User delegation SAS: applies to blog storage only. It's secured with Azure AD credentials and by the permissions specified for the SAS.
- Service SAS is secured with the storage account key and is used to delegate access to a resource in either Blob storage, Queue storage, Table storage, or Azure Files.
- Account SAS is secured with the storage account key. It delegates access to resources in one o more of the storage services
Recomended: Azure AD credentials

**Storage Account Keys**
Generated by Azure when creating the storage account. Azure generates 2 keys of 512-BITS. You use these keys to authorize access to data that resides in your storage account via Shared Key authorization. Azure KeyVault simplefies this process and allows your to perform the rotation of keys without  interrupting the applications

**Storage Analytics**


### Azure Database Security

Azure SQL Firewall Rules: 
- *Server-level IP firewall rules* allow clients to access the entire Azure SQL server, which includes all databases hosted in it. The master database holds these rules. You can configure a mazimum of 128 server-level IP firewall rules for an Azure SQL server.
- Database-level IP firewall rules are used to allow access to specific databases on a SQL Database server. You can create them for each database, included the master database. Also, there is a maximum of 128 rules.
- 

**Azure SQL Always Encrypted**
Protect sensitive data in an Azure SQL Database or even in a traditional SQL Server database.
Azure SQL Transparent Data Encryption. Clients can encrypt sensibive data inside the client applications without revealing the encryption keys to the SQL Server.
The Always Encrypted-enabled driver automatically encrypts and decrypts sensitive data in the client application before sending the data off to the SQL server. 
Available is all editions of Azure SQL Database starting weith SQL Server 2016.

**Azure SQL TRansparent Data Encryption (TDE)**
is used to protect Azure SQL databases, Azure SQL Managed Instances, and Azure Synapse from malicious offline activities. It encrypts the data at rest. TDE perform real-time encryption and decryption of the database, associated backups , and the transaction log files at rest. It cannot be used to encrypt the logical master database because this db contains objects that TDE needs to perform the encrypt/decrypt operations. In new databases this is automatically done. In old ones, you need to enable it manually

Azure SQL Database Auditing
You can enable server blob auditing and database blob auditing


Dynamic Data Masking Policy

Azure Active Directory Domain Services (Azure ADDS)



