---
title: AZ-500 Microsoft Azure Active Directory-  Manage Identity and Access
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

# I. Manage Identity and Access

??? abstract "Sources of this notes"
    - [The Microsoft e-learn platform](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-500/).
    - Book:  ["Microsoft Certified - MCA Microsoft Certified Associate Azure Security Engineer Study Guide: Exam AZ-500](https://www.amazon.es/Microsoft-Certified-Associate-Security-ngineer/dp/1119870372/). 
    - Udemy course:  [AZ-500 Microsoft Azure Security Technologies Exam Prep](https://www.udemy.com/course/az500-azure/).
    - Udemy course: [Azure Security: AZ-500 (updated July 2023)](https://www.udemy.com/course/azure-security-associate-az-500/)

??? note "Summary: AZ-500 Microsoft Azure Security Engineer Certification"
	- [About the certificate](az-500-preparation.md)
	- [I. Manage Identity and Access](az-500-ad-1-identity-and-access.md)
	- [II. Platform protection](az-500-ad-2-platform-protection.md)
	- [III. Data and applications](az-500-ad-3-data-and-applications.md)
	- [IV. Security operations](az-500-ad-4-security-operations.md)
	- [AZ-500 and more: keep learning](az-500-keep-learning.md)


Cheatsheets: **[Azure-CLI](../../azure-cli.md)**  **|** **[Azure PowerShell](../../azure-powershell.md)**  

[100 questions you should pass for the AZ-500 certificate](az-500-exams.md) 

--- 


**Azure Active Directory** (Azure AD) is a cloud-based identity and access management service.
## 1. Microsoft Entra ID 

### 1.1. Microsoft Entra ID licenses

- **Azure Active Directory Free.** Provides user and group management, on-premises directory synchronization, basic reports, self-service password change for cloud users, and single sign-on across Azure, Microsoft 365, and many popular SaaS apps.
- **Azure Active Directory Premium P1.** In addition to the Free features, P1 lets your hybrid users access both on-premises and cloud resources. It also supports advanced administration, such as dynamic groups, self-service group management, Microsoft Identity Manager, and cloud write-back capabilities, which allow self-service password reset for your on-premises users.
- **Azure Active Directory Premium P2.** In addition to the Free and P1 features, P2 also offers Azure Active Directory Identity Protection to help provide risk-based Conditional Access to your apps and critical company data and Privileged Identity Management to help discover, restrict, and monitor administrators and their access to resources and to provide just-in-time access when needed.
- **"Pay as you go"** feature licenses. You also get additional feature licenses, such as Azure Active Directory Business-to-Customer (B2C). B2C can help you provide identity and access management solutions for your customer-facing apps.


### 1.2. **Azure Active Directory Domain Services (Azure AD DS)** 

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

Azure Active Directory Domain Services (Azure AD DS) provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/New Technology LAN Manager (NTLM) authentication. You use these domain services without the need to deploy, manage, and patch domain controllers (DCs) in the cloud.


### 1.3. Signing devices to Azure Active Directory

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


### 1.4. Roles in Azure Active Directory

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


These are all of the Azure AD built-in roles:

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


### 1.5. Deploy Azure Active Directory Domain Services

Azure Active Directory Domain Services (Azure AD DS) provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/New Technology LAN Manager (NTLM) authentication. You use these domain services without the need to deploy, manage, and patch domain controllers (DCs) in the cloud.

Azure AD DS integrates with your existing Azure AD tenant. This integration lets users sign in to services and applications connected to the managed domain using their existing credentials.

When you create an Azure AD DS managed domain, you define a unique namespace. This namespace is the domain name, such as _aaddscontoso.com_. Two Windows Server domain controllers (DCs) are then deployed into your selected Azure region. This deployment of DCs is known as a replica set. You can expand a managed domain to have more than one replica set per Azure AD tenant. Replica sets can be added to any peered virtual network in any Azure region that supports Azure AD DS. You don't need to manage, configure, or update these DCs. The Azure platform handles the DCs as part of the managed domain, including backups and encryption at rest using Azure Disk Encryption.

Azure AD DS replicates identity information from Azure AD, so it works with Azure AD tenants that are cloud-only or synchronized with an on-premises AD DS environment. Azure AD DS performs a one-way synchronization from Azure AD to provide access to a central set of users, groups, and credentials. You can create resources directly in the managed domain (Azure ADDS), but they aren't synchronized back to Azure AD.

![Azure ADDS](../../img/az-500_1.png)



**Concepts:**

> **Azure Active Directory (Azure AD) - Cloud-based** identity and mobile device management that provides user account and authentication services for resources such as Microsoft 365, the Azure portal, or SaaS applications.
>
>Azure AD can be synchronized with an on-premises AD DS environment to provide a single identity to users that works natively in the cloud.
>
>**Active Directory Domain Services (AD DS)** - **Enterprise-ready lightweight directory access protocol (LDAP) server** that provides key features such as identity and authentication, computer object management, group policy, and trusts.
  >
  >AD DS is a central component in many organizations with an on-premises IT environment and provides core user account authentication and computer management features.
>
>**Azure Active Directory Domain Services (Azure AD DS)** - **Provides managed domain services** with a subset of fully compatible traditional AD DS features such as domain join, group policy, LDAP, and Kerberos / New Technology LAN Manager (NTLM) authentication.
>
> Azure AD DS integrates with Azure AD, which can synchronize with an on-premises AD DS environment. This ability extends central identity use cases to traditional web applications that run in Azure as part of a lift-and-shift strategy.


### 1.6. Create and manage Azure AD users
	
Note for deleted users:

The user is deleted and no longer appears on the **Users** - **All users** page. The user can be seen on the **Deleted users** page for the next **30 days** and can be restored during that time. When a user is deleted, any licenses consumed by the user are made available for other users.

To update the identity, contact information, or job information for users whose source of authority is Windows Server Active Directory, you must use Windows Server Active Directory. After you complete the update, you must wait for the next synchronization cycle to complete before you see the changes.


### 1.7. Manage users with Azure AD groups

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

### 1.8. Configure Azure AD administrative units

 An administrative unit can contain only users and groups. Administrative units restrict permissions in a role to any portion of your organization that you define. You could, for example, use administrative units to delegate the Helpdesk Administrator role to regional support specialists.

> To use administrative units, you need an Azure Active Directory Premium license for each administrative unit admin, and Azure Active Directory Free licenses for administrative unit members.

**Available roles for Azure AD administrative units**

|**Role**|**Description**|
|---|---|
|Authentication Administrator|Has access to view, set, and reset authentication method information for any non-admin user in the assigned administrative unit only.|
|Groups Administrator|Can manage all aspects of groups and groups settings, such as naming and expiration policies, in the assigned administrative unit only.|
|Helpdesk Administrator|Can reset passwords for non-administrators and Helpdesk administrators in the assigned administrative unit only.|
|License Administrator|Can assign, remove, and update license assignments within the administrative unit only.|
|Password Administrator|Can reset passwords for non-administrators and Password Administrators within the assigned administrative unit only.|
|User Administrator|Can manage all aspects of users and groups, including resetting passwords for limited admins within the assigned administrative unit only.|

### 1.9. Passwordless authentication

 Microsoft global Azure and Azure Government offer the following **three** passwordless authentication options that integrate with Azure Active Directory (Azure AD):

1. Windows Hello for Business: Windows Hello for Business is ideal for information workers that have their own designated Windows PC. The biometric and PIN credentials are directly tied to the user's PC, which prevents access from anyone other than the owner. With public key infrastructure (PKI) integration and built-in support for single sign-on (SSO), Windows Hello for Business provides a convenient method for seamlessly accessing corporate resources on-premises and in the cloud.
2. Microsoft Authenticator: You can also allow your employee's phone to become a passwordless authentication method. You may already be using the Authenticator app as a convenient multi-factor authentication option in addition to a password. You can also use the Authenticator App as a passwordless option.
3. Fast Identity Online2 (**FIDO2**) security keys: The FIDO (Fast IDentity Online) Alliance helps to promote open authentication standards and reduce the use of passwords as a form of authentication. FIDO2 is the latest standard that incorporates the web authentication (WebAuthn) standard. Users can register and then select a FIDO2 security key at the sign-in interface as their main means of authentication. These FIDO2 security keys are typically USB devices but could also use Bluetooth or Near-Field Communication (NFC).



## 2. Implement Hybrid Identity

Hybrid Identity is the process of connecting your on-premises Active Directory with your Azure Active Directory. 

### 2.1. Deploy Azure AD connect

Azure AD Connect will integrate your on-premises directories with Azure Active Directory.

Azure AD Connect provides the following features:

- **Password hash synchronization**. A sign-in method that synchronizes a hash of a users on-premises AD password with Azure AD.
- **Pass-through authentication**. A sign-in method that allows users to use the same password on-premises and in the cloud, but doesn't require the additional infrastructure of a federated environment.
- **Federation integration**. Federation is an optional part of Azure AD Connect and can be used to configure a hybrid environment using an on-premises AD FS infrastructure. It also provides AD FS management capabilities such as certificate renewal and additional AD FS server deployments.
- **Synchronization**. Responsible for creating users, groups, and other objects. As well as, making sure identity information for your on-premises users and groups is matching the cloud. This synchronization also includes password hashes.
- **Health Monitoring**. Azure AD Connect Health can provide robust monitoring and provide a central location in the Azure portal to view this activity.

**Azure Active Directory (Azure AD) Connect Health** provides robust monitoring of your on-premises identity infrastructure. It enables you to maintain a reliable connection to Microsoft 365 and Microsoft Online Services. With Azure AD Connect the key data you need is easily accessible. You can view and act on alerts, setup email notifications for critical alerts, and view performance data. *Using AD Connect Health works by installing an agent on each of your on-premises sync servers.*


### 2.3 Introduction to Authentication

Identity is the new control plane of IT security. When the Azure AD hybrid identity solution is your new control plane, authentication is the foundation of cloud access. All the other advanced security and user experience features in Azure AD depends on your authentication method.

Azure AD supports the following authentication methods for hybrid identity solutions:

#### Cloud authentication

Azure AD handles users' sign-in process.  Coupled with seamless single sign-on (SSO), users can sign in to cloud apps without having to reenter their credentials.

**Option 1: Azure AD password hash synchronization.** The simplest way to enable authentication for on-premises directory objects in Azure AD.

**Option 2:** **Azure AD Pass-through Authentication.** Provides a simple password validation for Azure AD authentication services by using a software agent that runs on one or more on-premises servers. The servers validate the users directly with your on-premises Active Directory, which ensures that the password validation doesn't happen in the cloud. Companies with a security requirement to immediately enforce on-premises user account states, password policies, and sign-in hours might use this authentication method.

#### Federal authentication

Azure AD hands off the authentication process to a separate trusted authentication system, such as on-premises Active Directory Federation Services (AD FS), to validate the user’s password. The authentication system can provide additional advanced authentication requirements. Examples are smartcard-based authentication or third-party multifactor authentication.

So, which one is more appropiate for your organization? See this decision tree:

![Decision tree](../../img/az-500_4.png)


### 2.4. Azure AD Password Hash Synchronization (PHS)

**Password hash synchronization** (PHS) is a feature used to synchronize user passwords from an on-premises Active Directory instance to a cloud-based Azure AD instance. Use this feature to sign in to Azure AD services like Microsoft 365, Microsoft Intune, CRM Online, and Azure Active Directory Domain Services (Azure AD DS). You sign in to the service by using the same password you use to sign in to your on-premises Active Directory instance. 

*How does syncronization work?* In the background, the password synchronization component takes the user’s password hash from on-premises Active Directory, encrypts it, and passes it as a string to Azure. Azure decrypts the encrypted hash and stores the password hash as a user attribute in Azure AD. When the user signs in to an Azure service, the sign-in challenge dialog box generates a hash of the user’s password and passes that hash back to Azure. Azure then compares the hash with the one in that user’s account. If the two hashes match, then the two passwords must also match and the user receives access to the resource. The dialog box provides the facility to save the credentials so that the next time the user accesses the Azure resource, the user will not be prompted.

>It is important to understand that this is **same sign-in**, not single sign-on. The user still authenticates against two separate directory services, albeit with the same user name and password. This solution provides a simple alternative to an AD FS implementation.

![Azure AD PHS](../../img/az-500_2.png)

### 2.5. Azure AD Pass-through Authentication (PTA)

**Azure AD Pass-through Authentication** (PTA) allows users to sign in to both on-premises and cloud-based applications using the same user account and passwords. When users sign-in using Azure AD, Pass-through authentication validates the users’ passwords directly against an organization's on-premise Active Directory. Benefits:

- Supports user sign-in into all web browser-based applications and into Microsoft Office client applications that use modern authentication.
- Sign-in usernames can be either the on-premises default username (userPrincipalName) or another attribute configured in Azure AD Connect (known as Alternate ID).
- Works seamlessly with conditional access features such as Azure Active Directory Multi-Factor Authentication to help secure your users.
- Integrated with cloud-based self-service password management, including password writeback to on-premises Active Directory and password protection by banning commonly used passwords.
- Multi-forest environments are supported if there are forest trusts between your AD forests and if name suffix routing is correctly configured.
- PTA is a free feature, and you don't need any paid editions of Azure AD to use it.
- PTA can be enabled via Azure AD Connect.
- PTA uses a lightweight on-premises agent that listens for and responds to password validation requests.
- Installing multiple agents provides high availability of sign-in requests.
- PTA protects your on-premises accounts against brute force password attacks in the cloud.

![Azure AD PTA](../../img/az-500_3.png)


### 2.6. Azure AD Federation

Federation is a collection of domains that have established trust. The level of trust may vary, but typically includes authentication and almost always includes authorization. A typical federation might include a number of organizations that have established trust for shared access to a set of resources. You can federate your on-premises environment with Azure AD and use this federation for authentication and authorization. This sign-in method ensures that all user authentication occurs on-premises. This method allows administrators to implement more rigorous levels of access control.

>If you decide to use Federation with Active Directory Federation Services (AD FS), you can optionally set up password hash synchronization as a backup in case your AD FS infrastructure fails.


### 2.7. Configure password writeback

**Password writeback** is a feature enabled with Azure AD Connect that allows password changes in the cloud to be written back to an existing on-premises directory in real time.

>To use **self-service password reset (SSPR)** you must have already configured Azure AD Connect in your environment.

Password writeback provides:

- **Enforcement of on-premises Active Directory Domain Services password policies**. When a user resets their password, it is checked to ensure it meets your on-premises Active Directory Domain Services policy before committing it to that directory. This review includes checking the history, complexity, age, password filters, and any other password restrictions that you have defined in local Active Directory Domain Services.
- **Zero-delay feedback**. Password writeback is a synchronous operation. Your users are notified immediately if their password did not meet the policy or could not be reset or changed for any reason.
- **Supports password changes from the access panel and Microsoft 365**. When federated or password hash synchronized users come to change their expired or non-expired passwords, those passwords are written back to your local Active Directory Domain Services environment.
- **Supports password writeback when an admin resets them from the Azure portal**. Whenever an admin resets a user’s password in the Azure portal, if that user is federated or password hash synchronized, the password is written back to on-premises. This functionality is currently not supported in the Office admin portal.
- **Doesn’t require any inbound firewall rules**. Password writeback uses an Azure Service Bus relay as an underlying communication channel. All communication is outbound over port 443.

![Password writeback](../../img/az-500_5.png)



## 3. Microsoft Entra ID Protection (Identity Protection)

Risk detections in Azure AD Identity Protection include any identified suspicious actions related to user accounts in the directory. The signals generated that are fed to Identity Protection, can be further fed into tools like Conditional Access to make access decisions, or fed back to a security information and event management (SIEM) tool for further investigation based on your organization's enforced policies.

For your organization to be protected you can have:

- **Azure AD Identity Protection policies** can automatically block a sign-in attempt or require additional action, such as requiring a password change or prompt for Azure AD Multi-Factor Authentication. 
- These policies work with existing **Azure AD Conditional Access policies** as an extra layer of protection for your organization.

Some of the following actions may trigger Azure AD Identity Protection risk detection:

- Users with leaked credentials.
- Sign-ins from anonymous IP addresses.
- Impossible travel to atypical locations.
- Sign-ins from infected devices.
- Sign-ins from IP addresses with suspicious activity.

Azure Active Directory Identity Protection includes three default policies that administrators can choose to enable: 


The insight you get for a detected risk detection is tied to your Azure AD subscription.  

- **MFA registration policy** -  Identity Protection can help organizations roll out Azure Multi-Factor Authentication using a Conditional Access policy requiring registration at sign-in.  Makes sure users are registered for Azure AD Multi-Factor Authentication. If a sign-in risk policy prompts for MFA, the user must already be registered for Azure AD Multi-Factor Authentication.
- **Sign-in risk policy** - Identity Protection analyzes signals from each sign-in, both real-time and offline, and calculates a risk score based on the probability that the sign-in wasn't performed by the user. Administrators can decide based on this risk score signal to enforce organizational requirements. Administrators can choose to block access, allow access, or allow access but require multi-factor authentication. Administrators can also choose to create a custom Conditional Access policy, including sign-in risk as an assignment condition.
- **User risk policy** - Identifies and responds to user accounts that may have compromised credentials. Can prompt the user to create a new password.

![Azure AD identity protection: default policies](../../img/az-500_6.png)


When you enable a policy user or sign-in risk policy, you can also choose the threshold for risk level - _**low and above**_, _medium and above_, or _**high**_. This flexibility lets you decide how aggressive you want to be in enforcing any controls for suspicious sign-in events.

### 3.1. Implement user risk policy

Identity Protection can calculate what it believes is normal for a user's behavior and use that to base decisions for their risk. User risk is a calculation of probability that an identity has been compromised. Administrators can decide based on this risk score signal to enforce organizational requirements. Administrators can choose to block access, allow access, or allow access but require a password change using Azure AD self-service password reset.

The risky users report includes these data: 

- Which users are at risk, have had risk remediated, or have had risk dismissed?
- Details about detections
- History of all risky sign-ins
- Risk history

Administrators can then choose to act on these events. Administrators can choose to:

- Reset the user password
- Confirm user compromise
- Dismiss user risk
- Block user from signing in
- Investigate further using Azure ATP

### 3.2. Implement sign-in risk policy

Sign-in risk represents the probability that a given authentication request isn't authorized by the identity owner. For users of Azure Identity Protection, sign-in risk can be evaluated as part of a Conditional Access policy. Sign-in Risk Policy supports the following conditions:

- **Location**: When configuring location as a condition, organizations can choose to include or exclude locations.  These named locations may include the public IPv4 network information, country or region, or even unknown areas that don't map to specific countries or regions.
- **Client apps**: Conditional Access policies by default apply to browser-based applications and applications that utilize modern authentication protocols. In addition to these applications, administrators can choose to include Exchange ActiveSync clients and other clients that utilize legacy protocols.
- **Risky sign-ins**: The risky sign-ins report contains filterable data for up to the past 30 days (1 month). With the information provided by the risky sign-ins report, administrators can find:
	- Which sign-ins are classified as at risk, confirmed compromised, confirmed safe, dismissed, or remediated. 
	- Real-time and aggregate risk levels associated with sign-in attempts.
	- Detection types triggered.
	- Conditional Access policies applied
	- MFA details
	- Device information
	- Application information
	- Location information

Administrators can then choose to take action on these events. Administrators can choose to:

- Confirm sign-in compromise
- Confirm sign-in safe

### 3.3. Deploy multifactor authentication in Azure

For organizations that need to be compliant with industry standards, such as the Payment Card Industry (PCI) Data Security Standard (DSS) version 3.2, MFA is a must have capability to authenticate users. Beyond being compliant with industry standards, enforcing MFA to authenticate users can also help organizations to mitigate credential theft attacks.

**Methods**

*Call to phone*: Places an automated voice call. The user answers the call and presses # in the phone keypad to authenticate. The phone number is not synchronized to on-premises Active Directory. A voice call to phone is important because it persists through a phone handset upgrade, allowing the user to register the mobile app on the new device.

*Text message to phone*: Sends a text message that contains a verification code. The user is prompted to enter the verification code into the sign-in interface. This process is called one-way SMS. Two-way SMS means that the user must text back a particular code. Two-way SMS is deprecated and not supported after November 14, 2018. Users who are configured for two-way SMS are automatically switched to call to phone verification at that time.

*Notification through mobile app*: Sends a push notification to your phone or registered device. The user views the notification and selects Approve to complete verification. The Microsoft Authenticator app is available for Windows Phone, Android, and iOS. Push notifications through the mobile app provide the best user experience.

*Verification code from mobile app*: The Microsoft Authenticator app generates a new OATH verification code every 30 seconds. The user enters the verification code into the sign-in interface. The Microsoft Authenticator app is available for Windows Phone, Android, and iOS. Verification code from mobile app can be used when the phone has no data connection or cellular signal.


**Settings**

- *Account lockout*: The account lockout settings let you specify how many failed attempts to allow before the account becomes locked out for a period of time.  The account lockout settings are only applied when a pin code is entered for the MFA prompt. The following settings are available: Number of MFA denials to trigger account lockout, Minutes until account lockout counter is reset, Minutes until account is automatically unblocked. 
- *Block and unblock users*: If a user's device has been lost or stolen, you can block authentication attempts for the associated account.
- *Fraud alerts*: Configure the fraud alert feature so that your users can report fraudulent attempts to access their resources. Code to report fraud during initial greeting: When users receive a phone call to perform two-step verification, they normally press # to confirm their sign-in. To report fraud, the user enters a code before pressing #. This code is 0 by default, but you can customize it.
- *Notification*: Email notifications can be configured when users report fraud alerts.
- *OATH tokens*: Azure AD supports the use of OATH-TOTP SHA-1 tokens that refresh codes every 30 or 60 seconds. Customers can purchase these tokens from the vendor of their choice.
- *Trusted IPs*:  Trusted IPs is a feature to allow federated users or IP address ranges to bypass two-step authentication. Notice there are two selections in this screenshot.
	- **Managed tenants**. For managed tenants, you can specify IP ranges that can skip MFA. 
	- **Federated tenants**. For federated tenants, you can specify IP ranges and you can also exempt AD FS claims users.


**How to deploy MFA**

To enable MFA, go to the User Properties in Azure Active Directory, and then the Multi-Factor Authentication option. From there, you can select the users that you want to modify and enable for MFA. You can also bulk enable groups of users with PowerShell. User's states can be **Enabled**, **Enforced**, or **Disabled**.


Azure AD Multi-Factor Authentication is included free of charge for global administrator security. Enabling MFA for global administrators provides an added level of security when managing and creating Azure resources like virtual machines, managing storage, or using other Azure services. Secondary authentication includes phone call, text message, and the authenticator app. Remember, you can only enable MFA for organizational accounts stored in Azure Active Directory. These are also called work or school accounts.


### 3.4. Azure AD Conditional Access

Conditional Access is the tool used by Azure Active Directory to bring signals together, to make decisions, and enforce organizational policies. Conditional Access policies at their simplest are if-then statements, if a user wants to access a resource, then they must complete an action. Conditional Access policies are enforced after the first-factor authentication has been completed. Conditional Access is not intended as an organization's first line of defense for scenarios like denial-of-service (DoS) attacks but can use signals from these events to determine access.

> Conditional Access is at the heart of the new **identity driven control plane**. Identity as a Service—the new control plane

Conditional access comes with six conditions: user/group, cloud application, device state, location (IP range), client application, and sign-in risk.

![Azure AD Conditional access](../../img/az-500_7.png)

With access controls, you can either Block Access altogether or Grant Access with more requirements: 

- Require MFA from Azure AD or an on-premises MFA (combined with AD FS).
- Grant access to only trusted devices.
- Require a domain-joined device.
- Require mobile devices to use Intune app protection policies.


### 3.5. Azure Active Directory (Azure AD) access reviews 

Navigate to **Azure Active Directory (or Microsoft Entra ID) > Identity Governance**. Select Access reviews.

Azure Active Directory (Azure AD) access reviews enable organizations to efficiently manage group memberships, access to enterprise applications, and role assignments.

Use access reviews in the following cases:

- **Too many users in privileged roles**: It's a good idea to check how many users have administrative access, how many of them are Global Administrators, and if there are any invited guests or partners that have not been removed after being assigned to do an administrative task. You can recertify the role assignment users in Azure AD roles such as Global Administrators, or Azure resources roles such as User Access Administrator in the Azure AD Privileged Identity Management (PIM) experience.
- **When automation is infeasible**: You can create rules for dynamic membership on security groups or Microsoft 365 Groups, but what if the HR data is not in Azure AD or if users still need access after leaving the group to train their replacement? You can then create a review on that group to ensure those who still need access should have continued access.
- **When a group is used for a new purpose**: If you have a group that is going to be synced to Azure AD, or if you plan to enable a sales management application for everyone in the Sales team group, it would be useful to ask the group owner to review the group membership prior to the group being used in a different risk content.
- **Business critical data access**: for certain resources, it might be required to ask people outside of IT to regularly sign out and give a justification on why they need access for auditing purposes.
- **To maintain a policy's exception list**: In an ideal world, all users would follow the access policies to secure access to your organization's resources. However, sometimes there are business cases that require you to make exceptions. As the IT admin, you can manage this task, avoid oversight of policy exceptions, and provide auditors with proof that these exceptions are reviewed regularly.
- **Ask group owners to confirm they still need guests in their groups**: Employee access might be automated with some on premises IAM, but not invited guests. If a group gives guests access to business sensitive content, then it's the group owner's responsibility to confirm the guests still have a legitimate business need for access.
- **Have reviews recur periodically**: You can set up recurring access reviews of users at set frequencies such as weekly, monthly, quarterly or annually, and the reviewers will be notified at the start of each review. Reviewers can approve or deny access with a friendly interface and with the help of smart recommendations.


## 4. Microsoft Entra Privileged Identity Management (PIM)

Using this feature requires Azure AD Premium P2 licenses. Azure AD Privileged Identity Management (PIM) allows you to manage, control, and monitor access to the most important resources in your organization. You can give just-in-time access and just-enough-access to users to allow them to do their tasks.
Privileged Identity Management provides time-based and approval-based role activation to mitigate the risks of excessive, unnecessary, or misused access permissions on resources you care about. Here are some of the key features of Privileged Identity Management:

- Provide just-in-time privileged access to Azure AD and Azure resources
- Assign time-bound access to resources using start and end dates
- Require approval to activate privileged roles
- Enforce multi-factor authentication to activate any role
- Use justification to understand why users activate
- Get notifications when privileged roles are activated
- Conduct access reviews to ensure users still need roles
- Download audit history for internal or external audit
- Prevents removal of the last active Global Administrator and Privileged Role Administrator role assignments


**Zero Trust model principles**: 

- **Verify explicitly** - Always authenticate and authorize based on all available data points.
- **Use least privilege access** - Limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection.
- **Assume breach** - Minimize blast radius and segment access. Verify end-to-end encryption and use analytics to get visibility, drive threat detection, and improve defenses.

**Zero Trust model Architecture**: 

The primary components of this process are Intune for device management and device security policy configuration, Azure AD conditional access for device health validation, and Azure AD for user and device inventory. The system works with Intune, pushing device configuration requirements to the managed devices. The device then generates a statement of health, which is stored in Azure AD. When the device user requests access to a resource, the device health state is verified as part of the authentication exchange with Azure AD.


**How does Privileged Identity Management work?**

Once you set up Privileged Identity Management, you'll see Tasks, Manage, and Activity options in the left navigation menu. As an administrator, you'll choose between options such as managing Azure AD roles, managing Azure resource roles, or PIM for Groups. When you choose what you want to manage, you see the appropriate set of options for that option.

Azure AD roles:

- Can manage Azure AD: Privileged Role Administrator, and Global Administrator roles.
- Can read  Azure AD roles:  Global Administrators, Security Administrators, Global Readers, and Security Readers roles

Azure AD resources:
- can be managed by:  Subscription Administrator, Resource Owner, and Resource User Access Administrator roles. 
- **can not** even be read by: Privileged Role Administrators, Security Administrators, or Security Readers roles 

> Make sure there are always at least two users in a Privileged Role Administrator role, in case one user is locked out or their account is deleted.

When creating an assignment, something that I didn't know in the setting up:
- Type of the assignment
    - Eligible assignments require the member of the role to perform an action to use the role. Actions might include activation or requesting approval from designated approvers.
    - Active assignments don't require the member to perform any action to use the role. Members assigned as active have the privileges assigned to the role.

How activates a role?  If users have been made eligible for a role, then they must activate the role assignment before using the role. To activate the role, users select a specific activation duration within the maximum (configured by administrators) and the reason for the activation request. If the role requires approval to activate, a notification will appear in the upper right corner of the user's browser, informing them the request is pending approval. If approval isn't required, the member can start using the role. Delegated approvers receive email notifications when a role request is pending their approval. Approvers can view, approve or deny these pending requests in PIM. After the request has been approved, the member can start using the role. For example, if a user or a group was assigned with Contribution role to a resource group, they'll be able to manage that particular resource group.

To extend or  renew assignments, it's required approval from a Global Administrator or Privileged Role Administrator. Notifications can be sent to Admins, Requestors, and Approvers.

**Privileged Role Administrator permissions**

- Enable approval for specific roles
- Specify approver users or groups to approve requests
- View request and approval history for all privileged roles

**Approver permissions**

- View pending approvals (requests)
- Approve or reject requests for role elevation (single and bulk)
- Provide justification for my approval or rejection

**Eligible role user permissions**

- Request activation of a role that requires approval
- View the status of your request to activate
- Complete your task in Azure AD if activation was approved


**Assignment settings**: 

- **Allow permanent eligible assignment**. Global admins and Privileged role admins can assign permanent eligible assignment. They can also require that all eligible assignments have a specified start and end date.
- **Allow permanent active assignment**. Global admins and Privileged role admins can assign active eligible assignment. They can also require that all active assignments have a specified start and end date.


**Implement a privileged identity management workflow**

By configuring Azure AD PIM to manage our elevated access roles in Azure AD, we now have JIT access for more than 28 configurable privileged roles. We can also monitor access, audit account elevations, and receive additional alerts through a management dashboard in the Azure portal.


## 5. Design an Enterprise Governance strategy: Azure Resource Manager

Regardless of the deployment type, **you always retain responsibility for the following:**

- Data
- Endpoints
- Accounts
- Access management


**Azure Resource Manager** is the deployment and management service for Azure. It provides a consistent management layer that allows you to create, update, and delete resources in your Azure subscription. You can use its access control, auditing, and tagging features to help secure and organize your resources after deployment.

### 5.1. **Resource Groups** 

**Resource Groups** -  There are some important factors to consider when defining your resource group:

- All the resources in your group should share the same lifecycle. You deploy, update, and delete them together. If one resource, such as a database server, needs to exist on a different deployment cycle it should be in another resource group.
- Each resource can only exist in one resource group.
- You can add or remove a resource to a resource group at any time.
- You can move a resource from one resource group to another group.
- A resource group can contain resources that are located in different regions.
- A resource group can be used to scope access control for administrative actions.
- A resource can interact with resources in other resource groups. This interaction is common when the two resources are related but don't share the same lifecycle (for example, web apps connecting to a database).
- If the resource group's region is temporarily unavailable, you can't update resources in the resource group because the metadata is unavailable. The resources in other regions will still function as expected, but you can't update them.

###  5.2. **Management Groups**

- Provide user access to multiple subscriptions
- Allows for new organizational models and logically grouping of resources.
- Allows for single assignment of controls that applies to all subscriptions.
- Provides aggregated views above the subscription level.

Mirror your organization's structure
- Create a flexible hierarchy that can be updated quickly.
- The hierarchy does not need to model the organization's billing hierarchy.
- The structure can easily scale up or down depending on your needs.

Apply policies or access controls to any service
- Create one RBAC assignment on the management group, which will inherit that access to all the subscriptions.
- Use Azure Resource Manager integrations that allow integrations with other Azure services: Azure Cost Management, Privileged Identity Management, and Microsoft Defender for Cloud.

### 5.3. Azure policies 

**Configure Azure policies** - Azure Policy is a service you use to create, assign, and manage policies. These policies enforce different rules and effects over your resources so that those resources stay compliant with your corporate standards and service level agreements.

![Azure policies](../../img/az-500_8.png)

The **first pillar** is around **real-time enforcement and compliance assessment**.

The **second pillar** of policy is **applying policies at scale** by leveraging Management Groups. There also is the concept called **policy initiative** that allows you to group policies together so that you can view the aggregated compliance result. At the initiative level there's also a concept called exclusion where one can exclude either the child management group, subscription, resource group, or resources from the policy assignment.

The **third pillar** of your policy is **remediation by leveraging a remediation policy** that will automatically remediate the non-compliant resource so that your environment always stays compliant. For existing resources, they will be flagged as non-compliant but they won't automatically be changed because there can be impact to the environment.

Some built-in roles in Azure Policy resources:

- Resource Policy Owner
- Resource Policy Contributor
- Resource Policy Reader

There are two resource providers for Azure Policy operations (or permissions):

- Microsoft.Authorization
- Microsoft.PolicyInsights

If a custom policy is needed these are the steps:

- Identify your business requirements
- Map each requirement to an Azure resource property
- Map the property to an alias
- Determine which effect to use
- Compose the policy definition

Let's do it:

- **Policy definition** - Every policy definition has conditions under which it's enforced. And, it has a defined effect that takes place if the conditions are met.
- **Policy assignment** - A policy definition that has been assigned to take place within a specific scope. This scope could range from a management group to an individual resource. The term scope refers to all the resources, resource groups, subscriptions, or management groups that the policy definition is assigned to.
- **Policy parameters** - They help simplify your policy management by reducing the number of policy definitions you must create. You can define parameters when creating a policy definition to make it more generic.

In order to easily track compliance for multiple resources, create and assign an **Initiative definition**.

All Policy objects, including definitions, initiatives, and assignments, will be readable to all roles over its scope. For example, a Policy assignment scoped to an Azure subscription will be readable by all role holders at the subscription scope and below.

A **contributor** may trigger resource remediation but can't create or update definitions and assignments. **User Access Administrator** is necessary to grant the managed identity on **deployIfNotExists** or **modify** the assignment's necessary permissions.

Each policy definition in Azure Policy has a single effect. That effect determines what happens when the policy rule is evaluated to match. The effects behave differently if they are for a new resource, an updated resource, or an existing resource.

These effects are currently supported in a policy definition:

- [Append](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#append)
- [Audit](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#audit)
- [AuditIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#auditifnotexists)
- [Deny](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#deny)
- [DenyAction](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#denyaction)
- [DeployIfNotExists](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#deployifnotexists)
- [Disabled](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#disabled)
- [Manual](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#manual)
- [Modify](https://learn.microsoft.com/en-us/azure/governance/policy/concepts/effects#modify)


### 5.4. Enable Role-Based Access Control (RBAC)

RBAC is an authorization system built on Azure Resource Manager that provides fine-grained access management of Azure resources. **Each Azure subscription is associated with one Azure AD directory**. Users, groups, and applications in that directory can manage resources in the Azure subscription. Grant access by assigning the appropriate RBAC role to users, groups, and applications at a certain scope. The scope of a role assignment can be a subscription, a resource group, or a single resource.

Note that a subscription is associated with only one Azure AD tenant. Also note that a resource group can have multiple resources but is associated with only one subscription. Lastly, a resource can be bound to only one resource group.

The four general built-in roles are:

|**Built-in Role**|**Description**|
|---|---|
|**Contributor**|Grants full access to manage all resources, but does not allow you to assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries.|
|**Owner**|Grants full access to manage all resources, including the ability to assign roles in Azure RBAC.|
|**Reader**|View all resources, but does not allow you to make any changes.|
|**User Access Administrator**|Lets you manage user access to Azure resources.|

If the built-in roles for Azure resources don't meet the specific needs of your organization, you can create your own custom roles. Just like built-in roles, you can assign custom roles to users, groups, and service principals at management group, subscription, and resource group scopes.

Limits for custom roles.

- Each directory can have up to **5000** custom roles.
- Azure Germany and Azure China 21Vianet can have up to 2000 custom roles for each directory.
- You cannot set AssignableScopes to the root scope ("/").
- You can only define one management group in AssignableScopes of a custom role. Adding a management group to AssignableScopes is currently in preview.
- Custom roles with DataActions cannot be assigned at the management group scope.
- Azure Resource Manager doesn't validate the management group's existence in the role definition's assignable scope.

### 5.5. Enable resource locks

You can set the lock level to **CanNotDelete or ReadOnly**. In the portal, the locks are called **Delete and Read-only** respectively.

- **CanNotDelete** means authorized users can still read and modify a resource, but they can't delete the resource.
- **ReadOnly** means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the Reader role.

To create or delete management locks, you must have access to **`Microsoft.Authorization/*`**or `Microsoft.Authorization/locks/*` actions. Of the built-in roles, only **Owner** and **User Access Administrator** are granted those actions.

### 5.6. Deploy Azure blueprints

Blueprints are a declarative way to orchestrate the deployment of various resource templates and other artifacts, such as:

- Role Assignments
- Policy Assignments
- Azure Resource Manager templates
- Resource Groups

The Azure Blueprints service is supported by the globally distributed Azure Cosmos Data Base. Blueprint objects are replicated in multiple Azure regions. This replication provides **low latency**, **high availability**, and **consistent access** to your blueprint objects, regardless of which region Blueprints deploys your resources to.

The Azure Resource Manager template gets used for deployments of one or more Azure resources, but once those resources deploy, there's no active connection or relationship to the template. Blueprints save the relationship between the blueprint definition and the blueprint assignment. This connection supports improved tracking and auditing of deployments. Each blueprint can consist of zero or more Resource Manager template artifacts. This support means that previous efforts to develop and maintain a library of Resource Manager templates are reusable in Blueprints.


**Blueprint definition** - A blueprint is composed of _**artifacts**_. Azure Blueprints currently supports the following resources as artifacts:

|**Resource**|**Hierarchy options**|**Description**|
|---|---|---|
|Resource Groups|Subscription|Create a new resource group for use by other artifacts within the blueprint. These placeholder resource groups enable you to organize resources exactly how you want them structured and provide a scope limiter for included policy and role assignment artifacts and ARM templates.|
|ARM template|Subscription, Resource Group|Templates, including nested and linked templates, are used to compose complex environments. Example environments: a SharePoint farm, Azure Automation State Configuration, or a Log Analytics workspace.|
|Policy Assignment|Subscription, Resource Group|Allows assignment of a policy or initiative to the subscription the blueprint is assigned to. The policy or initiative must be within the scope of the blueprint definition location. If the policy or initiative has parameters, these parameters are assigned at the creation of the blueprint or during blueprint assignment.|
|Role Assignment|Subscription, Resource Group|Add an existing user or group to a built-in role to make sure the right people always have the right access to your resources. Role assignments can be defined for the entire subscription or nested to a specific resource group included in the blueprint.|


**Blueprint definition locations** - When creating a blueprint definition, you'll define where the blueprint is saved. Blueprints can be saved to a **management group** or **subscription** that you have **Contributor access** to. If the location is a management group, the blueprint is available to assign to any child subscription of that management group.

**Blueprint parameters** - Blueprints can pass parameters to either a **policy/initiative** or an **ARM template**. When adding either _**artifact**_ to a blueprint, the author decides to provide a defined value for each blueprint assignment or to allow each blueprint assignment to provide a value at assignment time.

>Assigning a blueprint definition to a management group means the assignment object exists in the management group. The deployment of artifacts still targets a subscription. To perform a management group assignment, the **Create** Or **Update REST API** must be used, and the request body must include a value for **properties.scope** to define the target subscription.


### 5.7. Design an Azure subscription management plan

 Capturing subscription requirements and designing target subscriptions include several factors which are based on:

- environment type
- ownership and governance model
- organizational structure
- application portfolios

**Organization and governance design considerations**

- Subscriptions serve as boundaries for Azure Policy assignments. - For example, in the Payment Card Industry.
- Subscriptions serve as a scale unit so component workloads can scale within platform subscription limits. 
- Subscriptions provide a management boundary for governance and isolation that clearly separates concerns.
- Create separate platform subscriptions for management (monitoring), connectivity, and identity when they're required.
- Use manual processes to limit Azure AD tenants to only Enterprise Agreement enrollment subscriptions.
- See the Azure subscription and reservation transfer hub for subscription transfers between Azure billing offers.

**Quota and capacity design considerations**

Azure regions might have a finite number of resources. As a result, available capacity and Stock-keeping units (SKUs) should be tracked for Azure adoptions involving a large number of resources.


- Consider limits and quotas within the Azure platform for each service your workloads require.
- Consider the availability of required SKUs within your chosen Azure regions. 
- Consider that subscription quotas aren't capacity guarantees and are applied on a per-region basis.
- Consider reusing unused or decommissioned subscriptions.

**Tenant transfer restriction design considerations**

- Each Azure subscription is linked to a single Azure AD tenant, which acts as an identity provider (IdP) for your Azure subscription. The Azure AD tenant is used to authenticate users, services, and devices.
- The Azure AD tenant linked to your Azure subscription can be changed by any user with the required permissions.

>Transferring to another Azure AD tenant is not supported for Azure Cloud Solution Provider (CSP) subscriptions.

- With Azure landing zones, you can set requirements to prevent users from transferring subscriptions to your organization's Azure AD tenant. **Review the process in Manage Azure subscription policies**. Configure your subscription policy by providing a list of exempted users. Exempted users are permitted to bypass restrictions set in the policy. An exempted users list is not an Azure Policy. You can only specify individual user accounts as exempted users, not Azure AD groups.
- Consider whether users with Visual Studio/MSDN Azure subscriptions should be allowed to transfer their subscription to or from your Azure AD tenant.
- Tenant transfer settings are only configurable by users with the Azure AD Global Administrator role assigned. 

- All users with access to Azure can view the policy defined for your Azure AD tenant.
    
    - Users can't view your exempted users list.
    - Users can view the global administrators within your Azure AD tenant.

- Azure subscriptions transferred into an Azure AD tenant are placed into the default management group for that tenant.
- If approved by your organization, your application team can define a process to allow Azure subscriptions to be transferred to or from an Azure AD tenant.


**Establish cost management design considerations**

- Cost transparency is a critical management challenge every large enterprise organization faces. T
- Chargeback models, like Azure App Service Environment and Azure Kubernetes Service, might need to be shared to achieve higher density. Shared **platform as a service (PaaS)** resources can be affected by Chargeback models.
- Use a shutdown schedule for nonproduction workloads to optimize costs.
- Use Azure Advisor to check recommendations for optimizing costs.
- Establish a charge back model for better distribution of cost across your organization.
- Implement policy to prevent the deployment of resources not authorized to be deployed in your organization's environment.
- Establish a regular schedule and cadence to review cost and right size resources for workloads.


**Organization and governance recommendations**

- Treat subscriptions as a unit of management aligned with your business needs and priorities.
- Make subscription owners aware of their roles and responsibilities.
    - Do a quarterly or yearly access review for Azure AD Privileged Identity Management to ensure that privileges don't proliferate as users move within your organization.
    - Take full ownership of budget spending and resources.
    - Ensure policy compliance and remediate when necessary.
- Reference the following principles as you identify requirements for new subscriptions:
    - **Scale limits**: Subscriptions serve as a scale unit for component workloads to scale within platform subscription limits. Large specialized workloads like **high-performance computing**, **Internet of Things (IoT)**, and **System Analysis Program Development (SAP)** should use separate subscriptions to avoid running up against these limits.
    - **Management boundary**: Subscriptions provide a management boundary for governance and isolation, allowing a clear separation of concerns. Different environments, such as development, test, and production, are often removed from a management perspective.
    - **Policy boundary**: Subscriptions serve as a boundary for the Azure Policy assignments. For example, secure workloads like PCI typically require other policies in order to achieve compliance. The other overhead doesn't get considered if you use a separate subscription. Development environments have more relaxed policy requirements than production environments.
    - **Target network topology**: You can't share virtual networks across subscriptions, but you can connect them with different technologies like **virtual network peerin**g or **Azure ExpressRoute**. When deciding if you need a new subscription, consider which workloads need to communicate with each other.
- Group subscriptions together under management groups, which are aligned with your management group structure and policy requirements. Grouping subscriptions ensures that subscriptions with the same set of policies and Azure role assignments all come from a management group.
- Establish a dedicated management subscription in your **Platform** management group to support global management capabilities like Azure Monitor Log Analytics workspaces and Azure Automation runbooks.
- Establish a dedicated identity subscription in your **Platform** management group to host Windows Server Active Directory domain controllers when necessary.
- Establish a dedicated connectivity subscription in your **Platform** management group to host an **Azure Virtual WAN hub**, **private Domain Name System (DNS)**, **ExpressRoute circuit**, and other networking resources. A dedicated subscription ensures that all your foundation network resources are billed together and isolated from other workloads.
- Avoid a rigid subscription model. Instead, use a set of flexible criteria to group subscriptions across your organization. 


**Quota and capacity recommendations**

- Use subscriptions as scale units, and scale out resources and subscriptions as required. Your workload can then use the required resources for scaling out without hitting subscription limits in the Azure platform.
- Use reserved instances to manage capacity in some regions. Your workload can then have the required capacity for high demand resources in a specific region.
- Establish a dashboard with custom views to monitor used capacity levels, and set up alerts if capacity is approaching critical levels (90 percent CPU usage).
- Raise support requests for quota increases under subscription provisioning, such as for total available VM cores within a subscription. Ensure that your quota limits are set before your workloads exceed the default limits.
- Ensure that any required services and features are available within your chosen deployment regions.

**Automation recommendations**

- Build a Subscription vending process to automate the creation of Subscriptions for application teams via a request workflow as described in **Subscription vending**.

**Tenant transfer restriction recommendations**

- Configure the following settings to prevent users from transferring Azure subscriptions to or from your Azure AD tenant:
    - Set Subscription leaving Azure AD directory to Permit no one.
    - Set Subscription entering Azure AD directory to Permit no one.
- Configure a limited list of exempted users.
    - Include members from an Azure PlatformOps (platform operations) team.
    - Include break-glass accounts in the list of exempted users.

