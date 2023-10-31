---
title: AZ-500 Microsoft Azure Active Directory- Data and applications
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

# III. Data and applications

??? abstract "Sources of this notes:"
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


Cheatsheets: **[Azure-CLI](azure-cli.md)**  **|** **[Azure PowerShell](azure-powershell.md)**  

[100 questions you should pass for the AZ-500 certificate](az-500-exams.md)

--- 

## 1.  Azure Key Vault

Azure Key Vault helps safeguard cryptographic keys and secrets that cloud applications and services use. Key Vault streamlines the key management process and enables you to maintain control of keys that access and encrypt your data.  Developers can create keys for development and testing in minutes, and then migrate them to production keys. Security administrators can grant (and revoke) permission to keys, as needed. You can use Key Vault to create multiple secure containers, called vaults. Vaults help reduce the chances of accidental loss of security information by centralizing application secrets storage. Key vaults also control and log the access to anything stored in them.

Azure Key Vault helps address the following issues:

- **Secrets management**. You can use Azure Key Vault to securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets.
- **Key management**. You use Azure Key Vault as a key management solution, making it easier to create and control the encryption keys used to encrypt your data.
- **Certificate management**. Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private SSL/TLS certificates for use with Azure and your internal connected resources.
- **Store secrets backed by hardware security modules (HSMs)**. The secrets and keys can be protected either by software, or FIPS 140-2 Level 2 validates HSMs.

Key Vault is not intended as storage for user passwords.

Access to a key vault is controlled through two separate interfaces: management plane, and data plane. The management plane and data plane access controls work independently. Use RBAC to control what users have access to. For example, if you want to grant an application access to use keys in a key vault, you only need to grant data plane access permissions by using key vault access policies, and no management plane access is needed for this application. Conversely, if you want a user to be able to read vault properties and tags but not have any access to keys, secrets, or certificates, you can grant this user read access by using RBAC, and no access to the data plane is required. 

>If a user has contributor permissions (RBAC) to a key vault management plane, they can grant themselves access to the data plane by setting a key vault access policy. We recommend that you tightly control who has contributor access to your key vaults, to ensure that only authorized persons can access and manage your key vaults, keys, secrets, and certificates.

Azure Resource Manager can securely deploy certificates stored in Azure Key Vault to Azure VMs when the VMs are deployed. By setting appropriate access policies for the key vault, you also control who gets access to your certificate. Another benefit is that you manage all your certificates in one place in Azure Key Vault.

Deletion of key vaults or key vault objects can be either inadvertent or malicious. Enable the soft delete and purge protection features of Key Vault, particularly for keys that are used to encrypt data at rest. Deletion of these keys is equivalent to data loss, so you can recover deleted vaults and vault objects if needed. Practice Key Vault recovery operations on a regular basis.

Azure Key Vault is offered in two service tiers—standard and premium. The main difference between Standard and Premium is that Premium supports HSM-protected keys.

### 1.1. Configure Key Vault access

Access to a key vault is controlled through two interfaces: the management plane, and the data plane. The management plane is where you manage Key Vault itself. Operations in this plane include creating and deleting key vaults, retrieving Key Vault properties, and updating access policies. The data plane is where you work with the data stored in a key vault. You can add, delete, and modify keys, secrets, and certificates from here.

![key vault access](img/az-500_26.png)

To access a key vault in either plane, all callers (users or applications) must have proper authentication and authorization. Authentication establishes the identity of the caller. Authorization determines which operations the caller can execute.

Both planes use Microsoft Entra ID for authentication. For authorization, the management plane uses RBAC, and the data plane can use either **newly added RBAC** or a Key Vault access policy.

When you create a key vault in an Azure subscription, its automatically associated with the Microsoft Entra tenant of the subscription. Applications can access Key Vault in two ways:

- **User plus application access**. The application accesses Key Vault on behalf of a signed-in user. Examples of this type of access include Azure PowerShell and the Azure portal. User access is granted in two ways. They can either access Key Vault from any application, or they must use a specific application (referred to as compound identity).
- **Application-only access**. The application runs as a daemon service or background job. The application identity is granted access to the key vault.

For both types of access, the application authenticates with Microsoft Entra ID. The model of a single mechanism for authentication to both planes has several benefits:

- Organizations can centrally control access to all key vaults in their organization.
- If a user leaves, they instantly lose access to all key vaults in the organization.
- Organizations can customize authentication by using the options in Microsoft Entra ID, such as to enable multifactor authentication for added security.


|**Role**|**Management plane permissions**|**Data plane permissions**|
|---|---|---|
|Security team|Key Vault Contributor|Keys: backup, create, delete, get, import, list, restore. Secrets: all operations|
|Developers and operators|Key Vault deploy permission **Note**: This permission allows deployed VMs to fetch secrets from a key vault.|None|
|Auditors|None|Keys: list Secrets: list. **Note**: This permission enables auditors to inspect attributes (tags, activation dates, expiration dates) for keys and secrets not emitted in the logs.|
|Application|None|Keys: sign Secrets: get|

>The three team roles need access to other resources along with Key Vault permissions. To deploy VMs (or the Web Apps feature of Azure App Service), developers and operators need Contributor access to those resource types. Auditors need read access to the Storage account where the Key Vault logs are stored.


Some built-in RBAC in Azure:

|Built-in role|Description|ID|
|---|---|---|
|Key Vault Administrator|Perform all data plane operations on a key vault and all objects in it, including certificates, keys, and secrets. Cannot manage key vault resources or manage role assignments. Only works for key vaults that use the 'Azure role-based access control' permission model.|00482a5a-887f-4fb3-b363-3b7fe8e74483|
|Key Vault Certificates Officer|Perform any action on the certificates of a key vault, except manage permissions. Only works for key vaults that use the 'Azure role-based access control' permission model.|a4417e6f-fecd-4de8-b567-7b0420556985|
|Key Vault Crypto Officer|Perform any action on the keys of a key vault, except manage permissions. Only works for key vaults that use the 'Azure role-based access control' permission model.|14b46e9e-c2b7-41b4-b07b-48a6ebf60603|
|Key Vault Crypto Service Encryption User|Read metadata of keys and perform wrap/unwrap operations. Only works for key vaults that use the 'Azure role-based access control' permission model.|e147488a-f6f5-4113-8e2d-b22465e65bf6|
|Key Vault Crypto User|Perform cryptographic operations using keys. Only works for key vaults that use the 'Azure role-based access control' permission model.|12338af0-0e69-4776-bea7-57ae8d297424|
|Key Vault Reader|Read metadata of key vaults and its certificates, keys, and secrets. Cannot read sensitive values such as secret contents or key material. Only works for key vaults that use the 'Azure role-based access control' permission model.|21090545-7ca7-4776-b22c-e363652d74d2|
|Key Vault Secrets Officer|Perform any action on the secrets of a key vault, except manage permissions. Only works for key vaults that use the 'Azure role-based access control' permission model.|b86a8fe4-44ce-4948-aee5-eccb2c155cd7|
|Key Vault Secrets User|Read secret contents including secret portion of a certificate with private key. Only works for key vaults that use the 'Azure role-based access control' permission model.|4633458b-17de-408a-b874-0445c86b69e6|

 
### 1.2. Deploy and manage Key Vault certificates

Key Vault certificates support provides for management of your x509 certificates and enables:

- A certificate owner to create a certificate through a Key Vault creation process or through the import of an existing certificate. Includes both self-signed and CA-generated certificates.
- A Key Vault certificate owner to implement secure storage and management of X509 certificates without interaction with private key material.
- A certificate owner to create a policy that directs Key Vault to manage the life-cycle of a certificate.
- Certificate owners to provide contact information for notification about lifecycle events of expiration and renewal of certificate.
- Automatic renewal with selected issuers - Key Vault partner X509 certificate providers and CAs.

When a Key Vault certificate is created, an addressable key and secret are also created with the same name. The Key Vault key allows key operations and the Key Vault secret allows retrieval of the certificate value as a secret. A Key Vault certificate also contains public x509 certificate metadata.

When a Key Vault certificate is created, it can be retrieved from the addressable secret with the private key in either PFX or PEM format. However, the policy used to create the certificate must indicate that the key is exportable. If the policy indicates non-exportable, then the private key isn't a part of the value when retrieved as a secret.

The addressable key becomes more relevant with non-exportable Key Vault certificates. The addressable Key Vault key’s operations are mapped from the `keyusage` field of the Key Vault certificate policy used to create the Key Vault certificate. If a Key Vault certificate expires, it’s addressable key and secret become inoperable.

Two types of key are supported – RSA or RSA HSM with certificates. Exportable is only allowed with RSA, and is not supported by RSA HSM.


**Certificate policy**

A certificate policy contains information on how to create and manage the Key Vault certificate lifecycle. When a certificate with private key is imported into the Key Vault, a default policy is created by reading the x509 certificate. When a Key Vault certificate is created from scratch, a policy needs to be supplied. This policy specifies how to create the Key Vault certificate version, or the next Key Vault certificate version. At a high level, a certificate policy contains the following information:

- X509 certificate properties. Contains subject name, subject alternate names, and other properties used to create an x509 certificate request.
- Key Properties. Contains key type, key length, exportable, and reuse key fields. These fields instruct key vault on how to generate a key.
- Secret properties. Contains secret properties such as content type of addressable secret to generate the secret value, for retrieving certificate as a secret.
- Lifetime Actions. Contains lifetime actions for the Key Vault certificate. Each lifetime action contains:
    - Trigger, which specifies via days before expiry or lifetime span percentage.
    - Action, which specifies the action type: emailContacts, or autoRenew.
- Issuer: Contains the parameters about the certificate issuer to use to issue x509 certificates.
- Policy attributes: Contains attributes associated with the policy.


**Certificate Issuer**

Before you can create a certificate issuer in a Key Vault, the following two prerequisite steps must be completed successfully:

1. Onboard to CA providers: An organization administrator must onboard their company with at least one CA provider.
2. Admin creates requester credentials for Key Vault to enroll (and renew) SSL certificates: Provides the configuration to be used to create an issuer object of the provider in the key vault.


**Certificate contacts**

Certificate contacts contain contact information to send notifications triggered by certificate lifetime events. The contacts information is shared by all the certificates in the key vault. If a certificate's policy is set to auto renewal, then a notification is sent for the following events:

- Before certificate renewal
- After certificate renewal, and stating if the certificate was successfully renewed, or if there was an error, requiring manual renewal of the certificate
- When it’s time to renew a certificate for a certificate policy that is set to manually renew (email only)


**Certificate access control**

The Key Vault that contains certificates manages access control for those same certificates. he access control policy for certificates is distinct from the access control policies for keys and secrets in the same Key Vault. Users might create one or more vaults to hold certificates, to maintain scenario appropriate segmentation and management of certificates.

- Permissions for certificate management operations:
    - get: Get the current certificate version, or any version of a certificate.
    - list: List the current certificates, or versions of a certificate.
    - update: Update a certificate.
    - create: Create a Key Vault certificate.
    - import: Import certificate material into a Key Vault certificate.
    - delete: Delete a certificate, its policy, and all of its versions.
    - recover: Recover a deleted certificate.
    - backup: Back up a certificate in a key vault.
    - restore: Restore a backed-up certificate to a key vault.
    - `managecontacts`: Manage Key Vault certificate contacts.
    - `manageissuers`: Manage Key Vault certificate authorities/issuers.
    - `getissuers`: Get a certificate's authorities/issuers.
    - `listissuers`: List a certificate's authorities/issuers.
    - `setissuers`: Create or update a Key Vault certificate's authorities/issuers.
    - `deleteissuers`: Delete a Key Vault certificate's authorities/issuers.
- Permissions for privileged operations:
    - purge: Purge (permanently delete) a deleted certificate.


### 1.3. Create Key Vault keys

Cryptographic keys in Key Vault are represented as **JSON Web Key (JWK)** objects. There are two types of keys, depending on how they were created.

- **Soft keys**: A key processed in software by Key Vault, but is encrypted at rest using a system key that is in a **Hardware Security Module (HSM)**. Clients may import an existing RSA or EC (Elliptic Curve) key, or request that Key Vault generates one.
- **Hard keys**: A key processed in an HSM (Hardware Security Module). These keys are protected in one of the Key Vault HSM Security Worlds (there's one Security World per geography to maintain isolation). Clients may import an RSA or EC key, in soft form or by exporting from a compatible HSM device. Clients may also request Key Vault to generate a key.

**Key operations. -** Key Vault supports many operations on key objects. Here are a few:

- **Create**: Allows a client to create a key in Key Vault. The value of the key is generated by Key Vault and stored, and isn't released to the client. Asymmetric keys may be created in Key Vault.
- **Import**: Allows a client to import an existing key to Key Vault. Asymmetric keys may be imported to Key Vault using many different packaging methods within a JWK construct.
- **Update**: Allows a client with sufficient permissions to modify the metadata (key attributes) associated with a key previously stored within Key Vault.
- **Delete**: Allows a client with sufficient permissions to delete a key from Key Vault

**Cryptographic operations. -** Once a key has been created in Key Vault, the following cryptographic operations may be performed using the key. For best application performance, verify that operations are performed locally.

- **Sign and Verify**: Strictly, this operation is "sign hash" or "verify hash", as Key Vault doesn't support hashing of content as part of signature creation. Applications should hash the data to be signed locally, then request that Key Vault signs the hash. Verification of signed hashes is supported as a convenience operation for applications that may not have access to [public] key material.
- **Key Encryption / Wrapping**: A key stored in Key Vault may be used to protect another key, typically a symmetric **content encryption key (CEK)**. When the key in Key Vault is asymmetric, key encryption is used. When the key in Key Vault is symmetric, key wrapping is used.
- **Encrypt and Decrypt**: A key stored in Key Vault may be used to encrypt or decrypt a single block of data. The size of the block is determined using the key type and selected encryption algorithm. The Encrypt operation is provided for convenience, for applications that may not have access to [public] key material.

Apps hosted in App Service and Azure Functions can now define a reference to a secret managed in Key Vault as part of their application settings.

**Configure a hardware security module key-generation solution. -** 

For added assurance, when you use Azure Key Vault, you can import or generate keys in hardware security modules (HSMs) that never leave the HSM boundary. This scenario is often referred to as Bring Your Own Key (BYOK). The HSMs are FIPS 140-2 Level 2 validated. Azure Key Vault uses Thales nShield family of HSMs to protect your keys. (This functionality isn't available for Azure China.) **Generating and transferring an HSM-protected key over the Internet**:

- You generate the key from an offline workstation, which reduces the attack surface.
- The key is encrypted with a **Key Exchange Key (KEK)**, which stays encrypted until transferred to the Azure Key Vault HSMs. Only the encrypted version of your key leaves the original workstation.
- The toolset sets properties on your tenant key that binds your key to the Azure Key Vault security world. After the Azure Key Vault HSMs receive and decrypt your key, only these HSMs can use it. Your key can't be exported. This binding is enforced using the Thales HSMs.
- The KEK that encrypts your key is generated inside the Azure Key Vault HSMs, and isn't exportable. The HSMs enforce that there can be no clear version of the KEK outside the HSMs. In addition, the toolset includes attestation from Thales that the KEK isn't exportable and was generated inside a genuine HSM manufactured by Thales.
- The toolset includes attestation from Thales that the Azure Key Vault security world was also generated on a genuine HSM manufactured by Thales.
- Microsoft uses separate KEKs and separate security worlds in each geographical region. This separation ensures that your key can be used only in data centers in the region in which you encrypted it. For example, a key from a European customer can't be used in data centers in North American or Asia.

### 1.4. Manage customer managed keys

Once, you have created your Key Vault and have populated it with keys and secrets. The next step is to set up a rotation strategy for the values you store as Key Vault secrets. Secrets can be rotated in several ways:

- As part of a manual process
- Programmatically by using REST API calls
- Through an Azure Automation script

**Example of storage service encryption with customer-managed Keys. -** This service uses Azure Key Vault that provides highly available and scalable secure storage for RSA cryptographic keys backed by FIPS 140-2 Level 2 validated HSMs (Hardware Security Modules). Key Vault streamlines the key management process and enables customers to maintain control of keys that are used to encrypt data, manage, and audit their key usage, in order to protect sensitive data as part of their regulatory or compliance needs, HIPAA and BAA compliant.

![az service encryption](img/az-500_27.png)

Customers can generate/import their RSA key to Azure Key Vault and enable Storage Service Encryption. Azure Storage handles the encryption and decryption in a fully transparent fashion using envelope encryption in which data is encrypted using an AES-based key, which in turn is protected using the Customer-Managed Key stored in Azure Key Vault.

Customers can rotate their key in Azure Key Vault as per their compliance policies. When they rotate their key, Azure Storage detects the new key version and re-encrypts the Account Encryption Key for that storage account. Key rotation doesn't result in re-encryption of all data and there's no other action required from user.

Customers can also revoke access to the storage account by revoking access on their key in Azure Key Vault. There are several ways to revoke access to your keys. Revoking access effectively blocks access to all blobs in the storage account as the Account Encryption Key is inaccessible by Azure Storage.

Customers can enable this feature on all available redundancy types of Azure Blob storage including premium storage and can toggle from using Microsoft managed to using customer-managed keys. There's no extra charge for enabling this feature.

You can enable this feature on any Azure Resource Manager storage account using the Azure portal, Azure PowerShell, Azure CLI, or the Microsoft Azure Storage Resource Provider API.

### 1.5. Key vault secrets

Key Vault provides secure storage of secrets, such as passwords and database connection strings. From a developer's perspective, Key Vault APIs accept and return secret values as strings. Internally, Key Vault stores and manages secrets as sequences of octets (8-bit bytes), with a maximum size of 25k bytes each. The Key Vault service doesn't provide semantics for secrets. It merely accepts the data, encrypts it, stores it, and returns a secret identifier ("ID"). The identifier can be used to retrieve the secret at a later time.

Key Vault also supports a contentType field for secrets. Clients may specify the content type of a secret to assist in interpreting the secret data when it's retrieved. The maximum length of this field is 255 characters. There are no pre-defined values. The suggested usage is as a hint for interpreting the secret data. For instance, an implementation may store both passwords and certificates as secrets, then use this field to differentiate.

![az service encryption](img/az-500_28.png)

As shown above, the values for Key Vault Secrets are:

- Name-value pair - **Name must be unique in the Vault**
- Value can be any **Unicode Transformation Format (UTF-8)** string - max of 25 KB in size
- Manual or certificate creation
- Activation date
- Expiration date

**Encryption. -** All secrets in your Key Vault are stored encrypted. Key Vault encrypts secrets at rest with a hierarchy of encryption keys, with all keys in that hierarchy are protected by modules that are Federal Information Processing Standards (FIPS) 140-2 compliant. This encryption is transparent, and requires no action from the user. The Azure Key Vault service encrypts your secrets when you add them, and decrypts them automatically when you read them. The encryption leaf key of the key hierarchy is unique to each key vault. The encryption root key of the key hierarchy is unique to the security world, and its protection level varies between regions:

- China: root key is protected by a module that is validated for FIPS 140-2 Level 1.
- Other regions: root key is protected by a module that is validated for FIPS 140-2 Level 2 or higher.

**Secret attributes. -** In addition to the secret data, the following attributes may be specified:

- _**exp**_: IntDate, optional, **default is forever**. The **_exp_ (expiration time)** attribute identifies the expiration time on or after which the secret data **SHOULD NOT** be retrieved, except in particular situations. This field is for informational purposes only as it informs users of key vault service that a particular secret may not be used. Its value MUST be a number containing an IntDate value.
- _**nbf**_: IntDate, optional, **default is now**. The **_nbf_ (not before)** attribute identifies the time before which the secret data **SHOULD NOT** be retrieved, except in particular situations. This field is for informational purposes only. Its value **MUST** be a number containing an IntDate value.
- _**enabled**_: boolean, optional, **default is true**. This attribute specifies whether the secret data can be retrieved. The enabled attribute is used with _nbf_ and _exp_ when an operation occurs between _nbf_ and _exp_, it will only be permitted if enabled is set to true. Operations outside the _nbf_ and _exp_ window are automatically disallowed, except in particular situations.

There are more read-only attributes that are included in any response that includes secret attributes:

- _**created**_: IntDate, optional. The created attribute indicates when this version of the secret was created. This value is null for secrets created prior to the addition of this attribute. Its value must be a number containing an IntDate value.
- _**updated**_: IntDate, optional. The updated attribute indicates when this version of the secret was updated. This value is null for secrets that were last updated prior to the addition of this attribute. Its value must be a number containing an IntDate value.

**Secret access control. -**  Access Control for secrets managed in Key Vault, is provided at the level of the Key Vault that contains those secrets. The following permissions can be used, on a per-principal basis, in the secrets access control entry on a vault, and closely mirror the operations allowed on a secret object:

- Permissions for secret management operations
    
    - _**get**_: Read a secret
    - _**list**_: List the secrets or versions of a secret stored in a Key Vault
    - _**set**_: Create a secret
    - _**delete**_: Delete a secret
    - _**recover**_: Recover a deleted secret
    - _**backup**_: Back up a secret in a key vault
    - _**restore**_: Restore a backed up secret to a key vault
- Permissions for privileged operations
    
    - _**purge**_: Purge (**permanently delete**) a deleted secret

You can specify more application-specific metadata in the form of tags. Key Vault supports up to 15 tags, each of which can have a 256 character name and a 256 character value.

#### Configure key rotation

Once you have keys and secrets stored in the key vault it's important to think about a rotation strategy. There are several ways to rotate the values:

- As part of a manual process
- Programmatically by using API calls
- Through an Azure Automation script

This diagram shows how Event Grid and Function Apps can be used to automate the process.

![key rotation](img/az-500_29.png)

1. Thirty days before the expiration date of a secret, Key Vault publishes the "near expiry" event to Event Grid.
2. Event Grid checks the event subscriptions and uses HTTP POST to call the function app endpoint subscribed to the event.
3. The function app receives the secret information, generates a new random password, and creates a new version for the secret with the new password in Key Vault.
4. The function app updates SQL Server with the new password.


### 1.6. Manage Key Vault safety and recovery features

Key Vault's soft-delete feature allows recovery of the deleted vaults and deleted key vault objects (for example, keys, secrets, certificates), known as soft-delete. This safeguard offer the following protections:

- Once a secret, key, certificate, or key vault is deleted, it remains recoverable for a configurable period of 7 to 90 calendar days. If no configuration is specified, the default recovery period is set to 90 days. Users are provided with sufficient time to notice an accidental secret deletion and respond.
- When creating a new key vault, soft-delete is on by default. Once soft-delete is enabled on a key vault, it can't be disabled.  Once set, the retention policy interval can't be changed.
- The soft-delete feature is available through the REST API, the Azure CLI, PowerShell, .NET/C# interfaces, and ARM templates.
- The purge protection retention policy uses the same interval (7-90 days).  Once set, the retention policy interval can't be changed.
- You can't reuse the name of a key vault that has been soft-deleted until the retention period has passed.
- Permanently deleting, purging, a key vault is possible via a POST operation on the proxy resource and requires special privileges. Generally, only the subscription owner is able to purge a key vault. The POST operation triggers the immediate and irrecoverable deletion of that vault. Exceptions are:
	
	- When the Azure subscription has been marked as _undeletable_. In this case, only the service may then perform the actual deletion, and does so as a scheduled process.
	- When the--enable-purge-protection argument is enabled on the vault itself. In this case, Key Vault waits for 90 days from when the original secret object was marked for deletion to permanently delete the object.
	
- To purge a secret in the soft-deleted state, a service principal must be granted another "purge" access policy permission. The purge access policy permission isn't granted by default to any service principal including key vault and subscription owners and must be deliberately set. By requiring an elevated access policy permission to purge a soft-deleted secret, it reduces the probability of accidentally deleting a secret.

**Key vault recovery. -** Upon deleting a key vault object, the service will place the object in a deleted state, making it inaccessible to any retrieval operations. During the soft-delete retention interval, the following apply:

- You may list all of the key vaults and key vault objects in the soft-delete state for your subscription as well as access deletion and recovery information about them. Only users with special permissions can list deleted vaults. We recommend that our users create a custom role with these special permissions for handling deleted vaults.
- A key vault with the same name can't be created in the same location; correspondingly, a key vault object can't be created in a given vault if that key vault contains an object with the same name and which is in a deleted state.
- Only a privileged user may restore a key vault or key vault object by issuing a recover command on the corresponding proxy resource. The user, member of the custom role, who has the privilege to create a key vault under the resource group can restore the vault.
- Only a privileged user may forcibly delete a key vault or key vault object by issuing a delete command on the corresponding proxy resource.

Unless a key vault or key vault object is recovered, at the end of the retention interval the service performs a purge of the soft-deleted key vault or key vault object and its content. Resource deletion may not be rescheduled.

**Billing. -** In general, when an object (a key vault or a key or a secret) is in deleted state, there are only two operations possible: 'purge' and 'recover'. All the other operations fail. Therefore, even though the object exists, no operations can be performed and hence no usage will occur, so no bill. However there are following exceptions:

- 'purge' and 'recover' actions count towards normal key vault operations and billed.
- If the object is an HSM-key, the 'HSM Protected key' charge per key version per month charge applies if a key version has been used in last 30 days. After that, since the object is in deleted state no operations can be performed against it, so no charge will apply.

**Soft-deleted protection by default from February 2025. -**  If a secret is deleted and the key vault doesn't have soft-deleted protection, it's deleted permanently. Although users can currently opt out of soft-delete during key vault creation, this ability is deprecated. In February 2025, Microsoft enables soft-delete protection on all key vaults, and users are no longer be able to opt out of or turn off soft-delete. This, protect secrets from accidental or malicious deletion by a user.

![Deleting a key](img/az-500_30.png)


**Key vault backup. -** Back up secrets only if you have a critical business justification. Backing up secrets in your key vault may introduce operational challenges such as maintaining multiple sets of logs, permissions, and backups when secrets expire or rotate. Key Vault maintains availability in disaster scenarios and will automatically fail over requests to a paired region without any intervention from a user. If you want protection against accidental or malicious deletion of your secrets, configure soft-delete and purge protection features on your key vault.

>Key Vault does not support the ability to backup more than 500 past versions of a key, secret, or certificate object. Attempting to backup a key, secret, or certificate object may result in an error. It is not possible to delete previous versions of a key, secret, or certificate.

Key Vault doesn't currently provide a way to back up an entire key vault in a single operation. Any attempt to use the commands listed in this document to do an automated backup of a key vault may result in errors and not supported by Microsoft or the Azure Key Vault team.

When you back up a key vault object, such as a secret, key, or certificate, the backup operation downloads the object as an encrypted blob. This blob can't be decrypted outside of Azure. **To get usable data from this blob, you must restore the blob into a key vault within the same Azure subscription and Azure geography**. To back up a key vault object, you must have:

- Contributor-level or higher permissions on an Azure subscription.
- A primary key vault that contains the secrets you want to back up.
- A secondary key vault where secrets are restored.

Azure Dedicated HSM is most suitable for “lift-and-shift” scenarios that require direct and sole access to HSM devices. Examples include:

- Migrating applications from on-premises to Azure Virtual Machines
- Migrating applications from Amazon AWS EC2 to virtual machines that use the AWS Cloud HSM Classic service
- Running shrink-wrapped software such as Apache/Ngnix SSL Offload, Oracle TDE, and ADCS in Azure Virtual Machines

>Azure Dedicated HSM is not a good fit for the following type of scenario: Microsoft cloud services that support encryption with customer-managed keys (such as Azure Information Protection, Azure Disk Encryption, Azure Data Lake Store, Azure Storage, Azure SQL Database, and Customer Key for Office 365) that are not integrated with Azure Dedicated HSM.


## 2. Application Security features

### 2.1. Microsoft Identity Platform 

![Microsoft Identity platforms](img/az-500_31.png)

Some acronyms:

- Azure AD Authentication Library (ADAL)
- Microsoft Authentication Library (MSAL)
- Microsoft Secure Development Lifecycle (SDL)

Microsoft identity platform is an evolution of the Azure Active Directory (Azure AD) developer platform. The Microsoft identity platform supports industry-standard protocols such as OAuth 2.0 and OpenID Connect. With this unified Microsoft identity platform (v2.0), you can write code once and authenticate any Microsoft identity into your application.

The fully supported open-source Microsoft Authentication Library (MSAL) is recommended for use against the identity platform endpoints. MSAL...
 - is simple to use
 - provides great single sign-on (SSO) experiences for your users
 - helps you achieve high reliability and performance, 
 - and is developed using Microsoft Secure Development Lifecycle (SDL).


With the Microsoft identity platform, one can expand their reach to these kinds of users:

- Work and school accounts (Microsoft Entra ID provisioned accounts)
- Personal accounts (such as Outlook.com or Hotmail.com)
- Your customers who bring their own email or social identity (such as LinkedIn, Facebook, and Google) via MSAL and Azure AD Business-to-Consumer (B2C)

The Microsoft identity platform has two endpoints (v1.0 and v2.0); however, when developing a new application, consider it's highly recommended that you use the v2.0 (default) endpoint to benefit from the latest features and capabilities:


The Microsoft Authentication Library or MSAL can be used in many application scenarios, including the following:

- Single-page applications (JavaScript)
- Web app signing in users
- Web application signing in a user and calling a web API on behalf of the user
- Protecting a web API so only authenticated users can access it
- Web API calling another downstream Web API on behalf of the signed-in user
- Desktop application calling a web API on behalf of the signed-in user
- Mobile application calling a web API on behalf of the user who's signed in interactively.
- Desktop/service daemon application calling web API on behalf of itself

**Languages and frameworks**

|**Library**|**Supported platforms and frameworks**|
|---|---|
|MSAL for Android|Android|
|MSAL Angular|Single-page apps with Angular and Angular.js frameworks|
|MSAL for iOS and macOS|iOS and macOS|
|MSAL Go (Preview)|Windows, macOS, Linux|
|MSAL Java|Windows, macOS, Linux|
|MSAL.js|JavaScript/TypeScript frameworks such as Vue.js, Ember.js, or Durandal.js|
|MSAL.NET|.NET Framework, .NET Core, Xamarin Android, Xamarin iOS, Universal Windows Platform|
|MSAL Node|Web apps with Express, desktop apps with Electron, Cross-platform console apps|
|MSAL Python|Windows, macOS, Linux|
|MSAL React|Single-page apps with React and React-based libraries (Next.js, Gatsby.js)|


**Migrate apps that use ADAL to MSAL. -** Active Directory Authentication Library (ADAL) integrates with the Azure AD for developers (v1.0) endpoint, where MSAL integrates with the Microsoft identity platform. The v1.0 endpoint supports work accounts but not personal accounts. The v2.0 endpoint is unifying Microsoft personal accounts and works accounts into a single authentication system. Additionally, with MSAL, you can also get authentications for Azure AD B2C.

#### The Application Model

For an identity provider to know that a user has access to a particular app, both the user and the application must be registered with the identity provider. When you register your application with **Microsoft Entra ID**, you're providing an identity configuration for your application that allows it to integrate with the Microsoft identity platform. Registering the app also allows you to:

- Customize the branding of your application in the sign-in dialog box.
- Decide if you want to allow users to sign in only if they belong to your organization. This architecture is known as a single-tenant application. Or, you can allow users to sign in by using any work or school account, which is known as a multi-tenant application. 
- Request scope permissions. For example, you can request the "**user.read**" scope, which grants permission to read the profile of the signed-in user.
- Define scopes that define access to your web **application programming interface (API)**. 
- Share a secret with the Microsoft identity platform that proves the app's identity.

After the app is registered, it's given a unique identifier that it shares with the Microsoft identity platform when it requests tokens. If the app is a confidential client application, it will also share the secret or the public key depending on whether certificates or secrets were used. The Microsoft identity platform represents applications by using a model that fulfills two main functions:

- Identify the app by the authentication protocols it supports.
- Provide all the identifiers, **Uniform Resource Locators (URLs)**, secrets, and related information that are needed to authenticate.

The Microsoft identity platform:

- Holds all the data required to support authentication at runtime.
- Holds all the data for deciding what resources an app might need to access, and under what circumstances a given request should be fulfilled.
- Provides infrastructure for implementing app provisioning within the app developer's tenant, and to any other Microsoft Entra tenant.
- Handles user consent during token request time and facilitates the dynamic provisioning of apps across tenants.


**Flow in multi-tenant apps**

![identity](img/az-500_32.jpg)

In this provisioning flow:

1. A user from tenant B attempts to sign in with the app. The authorization endpoint requests a token for the application.
2. The user credentials are acquired and verified for authentication.
3. The user is prompted to provide consent for the app to gain access to tenant B.
4. The Microsoft identity platform uses the application object in tenant A as a blueprint for creating a service principal in tenant B.
5. The user receives the requested token.

You can repeat this process for more tenants. Tenant A retains the blueprint for the **app (application object)**. Users and admins of all the other tenants where the app is given consent keep control over what the application is allowed to do via the corresponding service principal object in each tenant.

### 2.2.  Register an application with App Registration

Before your app can get a token from the Microsoft identity platform, it must be registered in the Azure portal. Registration integrates your app with the Microsoft identity platform and establishes the information that it uses to get tokens, including:

- **Application ID**: A unique identifier assigned by the Microsoft identity platform.
- **Redirect URI/URL**: One or more endpoints at which your app will receive responses from the Microsoft identity platform. (For native and mobile apps, this is a URI assigned by the Microsoft identity platform.)
- **Application Secret**: A password or a public/private key pair that your app uses to authenticate with the Microsoft identity platform. (Not needed for native or mobile apps.)

Like most developers, you will probably use authentication libraries to manage your token interactions with the Microsoft identity platform. Authentication libraries abstract many protocol details, like validation, cookie handling, token caching, and maintaining secure connections, away from the developer and let you focus your development on your app. Microsoft publishes open-source client libraries and server middleware.

### 2.3. Configure Microsoft Graph permissions

Microsoft Graph exposes granular permissions that control the access that apps have to resources, like users, groups, and mail.

Microsoft Graph has two types of permissions:

- **Delegated permissions** are used by apps that have a signed-in user present. For these apps, either the user or an administrator consents to the permissions that the app requests, and the app can act as the signed-in user when making calls to Microsoft Graph. Some delegated permissions can be consented by non-administrative users, but some higher-privileged permissions require administrator consent.
- **Application permissions** are used by apps that run without a signed-in user present; for example, apps that run as background services or daemons. Application permissions can only be consented by an administrator.

Effective permissions are the permissions that your app will have when making requests to Microsoft Graph. It is important to understand the difference between the delegated and application permissions that your app is granted and its effective permissions when making calls to Microsoft Graph.

For example, assume your app has been granted the User.ReadWrite.All delegated permission. This permission nominally grants your app permission to read and update the profile of every user in an organization. If the signed-in user is a global administrator, your app will be able to update the profile of every user in the organization. However, if the signed-in user is not in an administrator role, your app will be able to update only the profile of the signed-in user

**Microsoft Graph API. -**  The Microsoft Graph Security API is an intermediary service (or broker) that provides a single programmatic interface to connect multiple Microsoft Graph Security providers (also called security providers or providers). The Microsoft Graph Security API federates requests to all providers in the Microsoft Graph Security ecosystem.

![flow of microsoft Graph Api](img/az-500_33.png)

The following is a description of the flow:

1. The application user signs in to the provider application to view the consent form from the provider. This consent form experience or UI is owned by the provider and applies to non-Microsoft providers only to get explicit consent from their customers to send requests to Microsoft Graph Security API.
2. The client consent is stored on the provider side.
3. The provider consent service calls the Microsoft Graph Security API to inform consent approval for the respective customer.
4. The application sends a request to the Microsoft Graph Security API.
5. The Microsoft Graph Security API checks for the consent information for this customer mapped to various providers.
6. The Microsoft Graph Security API calls all those providers the customer has given explicit consent to via the provider consent experience.
7. The response is returned from all the consented providers for that client.
8. The result set response is returned to the application.
9. If the customer has not consented to any provider, no results from those providers are included in the response.


**Why use the Microsoft Graph Security API?**

- Write code – Find code samples in C#, Java, NodeJS, and more.
- Connect using scripts – Find PowerShell samples.
- Drag and drop into workflows and playbooks – Use Microsoft Graph Security connectors for Azure Logic Apps, Microsoft Flow, and PowerApps.
- Get data into reports and dashboards – Use the Microsoft Graph Security connector for Power BI.
- Connect using Jupyter notebooks – Find Jupyter notebook samples.
- *Unify and standardize alert tracking*:  Connect once to integrate alerts from any Microsoft Graph-integrated security solution and keep alert status and assignments in sync across all solutions. You can also stream alerts to security information and event management (SIEM) solutions, such as Splunk using Microsoft Graph Security API connectors.
- *Correlate security alerts to improve threat protection and response*: Correlate alerts across security solutions more easily with a unified alert schema.
- *Update alert tags, status, and assignments*: Tag alerts with additional context or threat intelligence to inform response and remediation. Ensure that comments and feedback on alerts are captured for visibility to all workflows. Keep alert status and assignments in sync so that all integrated solutions reflect the current state. Use webhook subscriptions to get notified of changes.
- *Unlock security context to drive investigation*: Dive deep into related security-relevant inventory (like users, hosts, and apps), then add organizational context from other Microsoft Graph providers (Microsoft Entra ID, Microsoft Intune, Microsoft 365) to bring business and security contexts together and improve threat response.

### 2.4. Enable managed identities

**Managed Identities** for Azure resources is the new name for the service formerly known as Managed Service Identity (MSI) for Azure resources feature in Microsoft Entra provides Azure services with an automatically managed identity in Microsoft Entra ID. You can use the identity to authenticate to any service that supports Microsoft Entra authentication, including Key Vault, without any credentials in your code. The managed identities for Azure resources feature is free with Microsoft Entra ID for Azure subscriptions. There's no additional cost.

**Terminology. -** The following terms are used throughout the managed identities for Azure resources documentation set:

- **Client ID** - a unique identifier generated by Microsoft Entra ID that is tied to an application and service principal during its initial provisioning.
- **Principal ID** - the object ID of the service principal object for your managed identity that is used to grant role-based access to an Azure resource.
- **Azure Instance Metadata Service (IMDS)** - a REST endpoint accessible to all IaaS VMs created via the Azure Resource Manager. The endpoint is available at a well-known non-routable IP address (169.254.169.254) that can be accessed only from within the VM.


**How managed identities for Azure resources works. -** There are two types of managed identities:

- **A system-assigned managed identity** is enabled directly on an Azure service instance. When the identity is enabled, Azure creates an identity for the instance in the Microsoft Entra tenant that's trusted by the subscription of the instance. After the identity is created, the credentials are provisioned onto the instance. The lifecycle of a system-assigned identity is directly tied to the Azure service instance that it's enabled on. If the instance is deleted, Azure automatically cleans up the credentials and the identity in Microsoft Entra ID.
- **A user-assigned managed identity** is created as a standalone Azure resource. Through a create process, Azure creates an identity in the Microsoft Entra tenant that's trusted by the subscription in use. After the identity is created, the identity can be assigned to one or more Azure service instances. The lifecycle of a user-assigned identity is managed separately from the lifecycle of the Azure service instances to which it's assigned.


The following table shows the differences between the two types of managed identities:

|Property|System-assigned managed identity|User-assigned managed identity|
|---|---|---|
|Creation|Created as part of an Azure resource (for example, Azure Virtual Machines or Azure App Service).|Created as a stand-alone Azure resource.|
|Life cycle|Shared life cycle with the Azure resource that the managed identity is created with.   <br>When the parent resource is deleted, the managed identity is deleted as well.|Independent life cycle.  <br>Must be explicitly deleted.|
|Sharing across Azure resources|Can’t be shared.  <br>It can only be associated with a single Azure resource.|Can be shared.  <br>The same user-assigned managed identity can be associated with more than one Azure resource.|
|Common use cases|Workloads contained within a single Azure resource.  <br>Workloads needing independent identities.  <br>For example, an application that runs on a single virtual machine.|Workloads that run on multiple resources and can share a single identity.  <br>Workloads needing pre-authorization to a secure resource, as part of a provisioning flow.  <br>Workloads where resources are recycled frequently, but permissions should stay consistent.  <br>For example, a workload where multiple virtual machines need to access the same resource.|



**Credential rotation. -** Credential rotation is controlled by the resource provider that hosts the Azure resource. The default rotation of the credential occurs every 46 days. It's up to the resource provider to call for new credentials, so the resource provider could wait longer than 46 days. The following diagram shows how managed service identities work with Azure virtual machines (VMs):

![credential rotation](img/az-500_34.png)

1. Azure Resource Manager receives a request to enable the system-assigned managed identity on a VM.
2. Azure Resource Manager creates a service principal in Microsoft Entra ID for the identity of the VM. The service principal is created in the Microsoft Entra tenant that's trusted by the subscription.
3. Azure Resource Manager configures the identity on the VM by updating the Azure Instance Metadata Service identity endpoint with the service principal client ID and certificate.
4. After the VM has an identity, use the service principal information to grant the VM access to Azure resources. To call Azure Resource Manager, use role-based access control (RBAC) in Microsoft Entra ID to assign the appropriate role to the VM service principal. To call Key Vault, grant your code access to the specific secret or key in Key Vault.
5. Your code that's running on the VM can request a token from the Azure Instance Metadata service endpoint, accessible only from within the VM: [http://169.254.169.254/metadata/identity/oauth2/token](http://169.254.169.254/metadata/identity/oauth2/token)
    - The resource parameter specifies the service to which the token is sent. To authenticate to Azure Resource Manager, use resource=https://management.azure.com/.
    - API version parameter specifies the IMDS version, use api-version=2018-02-01 or greater.
6. A call is made to Microsoft Entra ID to request an access token (as specified in step 5) by using the client ID and certificate configured in step 3. Microsoft Entra ID returns a JSON Web Token (JWT) access token.
7. Your code sends the access token on a call to a service that supports Microsoft Entra authentication


### 2.5. Azure App Services

_**Azure App Service**_ is an HTTP-based service for **hosting web applications**, **REST APIs**, and **mobile backends**. You can develop in your favorite language, be it .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. Applications run and scale with ease on both Windows and Linux-based environments. Azure App Service is a fully managed platform as a service (PaaS) offering for developers. Here are some key features of App Service:

- Multiple languages and frameworks - App Service has first-class support for ASP.NET, ASP.NET Core, Java, Ruby, Node.js, PHP, or Python. You can also run PowerShell and other scripts or executables as background services.
- Managed production environment - App Service automatically patches and maintains the OS and language frameworks for you. 
- Containerization and Docker - Dockerize your app and host a custom Windows or Linux container in App Service. Run multi-container apps with Docker Compose. 
- DevOps optimization - Set up continuous integration and deployment with Azure DevOps, GitHub, BitBucket, Docker Hub, or Azure Container Registry. 
- Global scale with high availability - Scale up or out manually or automatically.
- Connections to SaaS platforms and on-premises data - Choose from more than 50 connectors for enterprise systems (such as SAP), SaaS services (such as Salesforce), and internet services (such as Facebook). Access on-premises data using Hybrid Connections and Azure Virtual Networks.
- Security and compliance - The App Service is ISO, SOC, and PCI compliant. Authenticate users with Microsoft Entra ID, Google, Facebook, Twitter, or Microsoft account. Create IP address restrictions and manage service identities. Prevent subdomain takeovers.
- Application templates - Choose from an extensive list of application templates in the Azure Marketplace, such as WordPress, Joomla, and Drupal.
- Visual Studio and Visual Studio Code integration - Dedicated tools in Visual Studio and Visual Studio Code streamline the work of creating, deploying, and debugging.
- API and mobile features - App Service provides turn-key CORS support for RESTful API scenarios and simplifies mobile app scenarios by enabling authentication, offline data sync, push notifications, and more.
- Serverless code - Run a code snippet or script on-demand without having to explicitly provision or manage infrastructure and pay only for the compute time your code actually uses.

### 2.6. App Service Environment

An **App Service Environment** is an Azure App Service feature that provides a fully isolated and dedicated environment for running App Service apps securely at high scale. An App Service Environment can host:

- Windows web apps
- Linux web apps
- Docker containers (**Windows** and **Linux**)
- Functions
- Logic apps (Standard)

App Service Environments have many use cases, including:

- Internal line-of-business applications.
- Applications that need more than 30 App Service plan instances.
- Single-tenant systems to satisfy internal compliance or security requirements.
- Network-isolated application hosting.
- Multi-tier applications.

There are many networking features that enable apps in a multi-tenant App Service to reach network-isolated resources or become network-isolated themselves. These features are enabled at the application level. With an App Service Environment, no added configuration is required for the apps to be on a virtual network. The apps are deployed into a network-isolated environment that's already on a virtual network. If you really need a complete isolation story, you can also deploy your App Service Environment onto dedicated hardware.

**Dedicated environment. -** An App Service Environment is a single-tenant deployment of Azure App Service that runs on your virtual network:

- Applications are hosted in App Service plans (which are a provisioning profile for an application host.)
- App Service plans  are created in an App Service Environment. 

**Scaling out an App Service plan**: you create more application hosts with all the apps in that App Service plan on each host. 


- A single App Service Environment v3 can have up to 200 total App Service plan instances across all the App Service plans combined.
- A single App Service Isolated v2 (Iv2) plan can have up to 100 instances by itself.
- When you're deploying onto dedicated hardware (hosts), you're limited in scaling across all App Service plans to the number of cores in this type of environment. An App Service Environment that's deployed on dedicated hosts has 132 vCores available. I1v2 uses two vCores, I2v2 uses four vCores, and I3v2 uses eight vCores per instance.

### 2.7. Azure App Service plan

An app service always runs in an _**App Service**_ plan. In addition, Azure Functions also has the option of running in an App Service plan. An App Service plan defines a set of compute resources for a web app to run. These compute resources are analogous to the server farm in conventional web hosting. One or more apps can be configured to run on the same computing resources (or in the same App Service plan).

 Each App Service plan defines:

- Operating System (Windows, Linux)
- Region (West US, East US, etc.)
- Number of VM instances
- Size of VM instances (Small, Medium, Large)
- Pricing tier (Free, Shared, Basic, Standard, Premium, PremiumV2, PremiumV3, Isolated, IsolatedV2). This determines what App Service features you get and how much you pay for the plan. 

When you create an App Service plan in a certain region (for example, West Europe), a set of compute resources is created for that plan in that region. Whatever apps you put into this App Service plan run on these compute resources as defined by your App Service plan.

The pricing tiers available to your App Service plan depend on the operating system selected at creation time. There are a few categories of pricing tiers:

- **Shared compute**: Free and Shared, the two base tiers, runs an app on the same Azure VM as other App Service apps, including apps of other customers. These tiers allocate CPU quotas to each app that runs on the shared resources, and the resources cannot scale out.
- **Dedicated compute**: The Basic, Standard, Premium, PremiumV2, and PremiumV3 tiers run apps on dedicated Azure VMs. Only apps in the same App Service plan share the same compute resources. The higher the tier, the more VM instances are available to you for scale-out.
- **Isolated**: This Isolated and IsolatedV2 tiers run dedicated Azure VMs on dedicated Azure Virtual Networks. It provides network isolation on top of compute isolation to your apps. It provides the maximum scale-out capabilities.

### 2.8. App Service Environment networking

App Service Environment is a single-tenant deployment of Azure App Service that hosts Windows and Linux containers, web apps, API apps, logic apps, and function apps. When you install an App Service Environment, you pick the Azure virtual network that you want it to be deployed in. All of the inbound and outbound application traffic is inside the virtual network you specify. You deploy into a single subnet in your virtual network, and nothing else can be deployed into that subnet.

**Subnet requirements. -** You must delegate the subnet to Microsoft.Web/hostingEnvironments, and the subnet must be empty. The size of the subnet can affect the scaling limits of the App Service plan instances within the App Service Environment. It's a good idea to use a /24 address space (256 addresses) for your subnet to ensure enough addresses to support production scale.

>Windows Containers uses an additional IP address per app for each App Service plan instance, and you need to size the subnet accordingly. If your App Service Environment has, for example, 2 Windows Container App Service plans, each with 25 instances and each with 5 apps running, you will need 300 IP addresses and additional addresses to support horizontal (up/down) scale.

The minimal size of your subnet is a /27 address space (32 addresses). Any particular subnet has five addresses reserved for management purposes. In addition to the management addresses, App Service Environment dynamically scales the supporting infrastructure and uses between 4 and 27 addresses, depending on the configuration and load. You can use the remaining addresses for instances in the App Service plan.

If you run out of addresses within your subnet, you can be restricted from scaling out your App Service plans in the App Service Environment. Another possibility is that you can experience increased latency during intensive traffic load if Microsoft can't scale the supporting infrastructure.

App Service Environment has the following network information at creation:

|**Address type**|**Description**|
|---|---|
|App Service Environment virtual network|The virtual network deployed into.|
|App Service Environment subnet|The subnet deployed into.|
|Domain suffix|The domain suffix that is used by the apps made.|
|Virtual IP (VIP)|The VIP type is used. The two possible values are internal and external.|
|Inbound address|The inbound address is the address at which your apps are reached. If you have an internal VIP, it's an address in your App Service Environment subnet. If the address is external, it's a public-facing address.|
|Default outbound addresses|The apps use this address, by default, when making outbound calls to the internet.|

![Screenshot showing App Service Environment IP address page.](img/az-500_35.png)

As you scale your App Service plans in your App Service Environment, you'll use more addresses from your subnet. Apps in the App Service Environment don't have dedicated addresses in the subnet. The specific addresses an app uses in the subnet will change over time.

### 2.9. Availability Zone Support for App Service Environments

Azure App Service Environment can be deployed across **availability zones (AZ)** to help you achieve resiliency and reliability for your business-critical workloads. This architecture is also known as zone redundancy.

When you configure it to be zone redundant, the platform automatically spreads the instances of the Azure App Service plan across three zones in the selected region. This means that the minimum App Service Plan instance count will always be three. If you specify a capacity larger than three, and the number of instances is divisible by three, the instances are spread evenly. Otherwise, **instance counts beyond 3*N** are spread across the remaining one or two zones.

- You configure availability zones when you create your App Service Environment.
- You can only specify availability zones when creating a new App Service Environment, not later.
- Availability zones are **only supported in a subset of regions**.

Since you can't convert pre-existing App Service Environments to use availability zones, migration will consist of a side-by-side deployment where you'll create a new App Service Environment with availability zones enabled. For more information on App Service Environment migration options, see App Service Environment migration.


### 2.10. App Service Environment Certificates

**Azure App Service** provides a highly scalable, self-patching web hosting service. Once the certificate is added to your App Service app or function app, you can secure a **custom Domain Name System (DNS)** name with it or use it in your application code.

>A certificate uploaded into an app is stored in a deployment unit that is bound to the app service plan's resource group and region combination (**internally called a webspace**). This makes the certificate accessible to other apps in the same resource group and region combination.

The following lists are options for adding certificates in App Service:

- **Create a free App Service managed certificate**: A private certificate that's free of charge and easy to use if you just need to secure your custom domain in App Service.
- **Purchase an App Service certificate**: A private certificate that's managed by Azure. It combines the simplicity of automated certificate management and the flexibility of renewal and export options.
- **Import a certificate from Key Vault**: Useful if you use Azure Key Vault to manage your **Public-Key Cryptography Standards #12 (PKCS12)** certificates.
- **Upload a private certificate**: If you already have a private certificate from a third-party provider, you can upload it.
- **Upload a public certificate**: Public certificates are not used to secure custom domains, but you can load them into your code if you need them to access remote resources.

**Prerequisites: **

- Create an App Service app.
- For a private certificate, make sure that it satisfies all requirements from App Service.
- Free certificate only:
    - Map the domain you want a certificate for to App Service.
    - For a root domain (**like contoso.com**), make sure your app doesn't have any IP restrictions configured. Both certificate creation and its periodic renewal for a root domain depends on your app being reachable from the internet.


## 3. Storage Security

### 3.1. Data sovereignty

Data sovereignty is the concept that information, which has been converted and stored in binary digital form, is subject to the laws of the country or region in which it is located. We recommend that you configure business continuity and disaster recovery (BCDR) across regional pairs to benefit from Azure’s isolation and VM policies.

### 3.2. Configure Azure storage access

Options for authorizing requests to Azure Storage include:

- **Microsoft Entra ID** - Azure Storage provides integration with Microsoft Entra ID for identity-based authorization of requests to the Blob and Queue services.  When you use Microsoft Entra ID to authorize requests make from your applications, you avoid having to store your account access key with your code, as you do with Shared Key authorization. While you can continue to use Shared Key authorization with your blob and queue applications, Microsoft recommends moving to Microsoft Entra ID where possible.
- **Microsoft Entra Domain Services authorization** for Azure Files. Azure Files supports identity-based authorization over Server Message Block (SMB) through Microsoft Entra Domain Services. You can use RBAC for fine-grained control over a client's access to Azure Files resources in a storage account
- **Shared Key** - Shared Key authorization relies on your account access keys and other parameters to produce an encrypted signature string that is passed on via the request in the Authorization header.
- **Shared Access Signatures** - A shared access signature (SAS) is a URI that grants restricted access rights to Azure Storage resources. You can provide a shared access signature to clients who should not be trusted with your storage account key but to whom you wish to delegate access to certain storage account resources. By distributing a shared access signature URI to these clients, you can grant them access to a resource for a specified period of time, with a specified set of permissions. The URI query parameters comprising the SAS token incorporate all of the information necessary to grant controlled access to a storage resource. A client who is in possession of the SAS can make a request against Azure Storage with just the SAS URI, and the information contained in the SAS token is used to authorize the request.
- **Anonymous access to containers and blobs** - You can enable anonymous, public read access to a container and its blobs in Azure Blob storage. By doing so, you can grant read-only access to these resources without sharing your account key, and without requiring a shared access signature (SAS). 


### 3.3. Deploy shared access signatures

As a best practice, you shouldn't share storage account keys with external third-party applications. For untrusted clients, use a **shared access signature** (SAS). 

>A shared access signature is a string that contains a security token that can be attached to a URI. Use a shared access signature to delegate access to storage objects and specify constraints, such as the permissions and the time range of access.

- **Service-level** shared access signature allows access to specific resources in a storage account. You'd use this type of shared access signature, for example, to allow an app to retrieve a list of files in a file system or to download a file. It  is used to delegate access to a resource in either Blob storage, Queue storage, Table storage, or Azure Files.
- **Account-level** shared access signature allows access to anything that a service-level shared access signature can allow, plus additional resources and abilities. For example, you can use an account-level shared access signature to allow the ability to create file systems.
- **User delegation SAS**, introduced with version 2018-11-09, is secured with Microsoft Entra credentials. This type of SAS is supported for the Blob service only and can be used to grant access to containers and blobs.

One would typically use a shared access signature for a service where users read and write their data to your storage account. Accounts that store user data have two typical designs:

- Clients upload and download data through a front-end proxy service, which performs authentication. This front-end proxy service has the advantage of allowing validation of business rules. But if the service must handle large amounts of data or high-volume transactions, you might find it complicated or expensive to scale this service to match demand.
    
    ![Screenshot of clients upload and download data through a front-end proxy service, which performs authentication.](https://learn.microsoft.com/en-us/training/wwl-azure/storage-security/media/az500-shared-access-signature-1-0af67054.png)
    
- A lightweight service authenticates the client as needed. Then it generates a shared access signature. After receiving the shared access signature, the client can access storage account resources directly. The shared access signature defines the client's permissions and access interval. The shared access signature reduces the need to route all data through the front-end proxy service.
    
    ![Screenshot of a lightweight service authenticates the client as needed. Then it generates a shared access signature.](https://learn.microsoft.com/en-us/training/wwl-azure/storage-security/media/az500-shared-access-signature-2-3672ac29.png)


### 3.4. Manage Microsoft Entra storage authentication

Azure Storage provides integration with Microsoft Entra ID for identity-based authorization of requests to the Blob and Queue services. With Microsoft Entra ID, you can use Azure role-based access control (Azure RBAC) to grant permissions to a security principal, which may be a user, group, or application service principal. The security principal is authenticated by Microsoft Entra ID to return an OAuth 2.0 token. The token can then be used to authorize a request against the Blob service.

Authorization with Microsoft Entra ID is available for all general-purpose and Blob storage accounts in all public regions and national clouds. Only storage accounts created with the Azure Resource Manager deployment model support Microsoft Entra authorization. Blob storage additionally supports creating shared access signatures (SAS) that is signed with Microsoft Entra credentials.

When a security principal (a user, group, or application) attempts to access a queue resource, the request must be authorized. With Microsoft Entra ID, access to a resource is a two-step process. First, the security principal's identity is authenticated, and an OAuth 2.0 token is returned. Next, the token is passed as part of a request to the Queue service and used by the service to authorize access to the specified resource. The authentication step requires that an application request an OAuth 2.0 access token at runtime. If an application is running from within an Azure entity, such as an Azure VM, a Virtual Machine Scale Set, or an Azure Functions app, it can use a managed identity to access queues.

The authorization step requires one or more Azure roles to be assigned to the security principal. Native and web applications that request the Azure Queue service can also authorize access with Microsoft Entra ID.


### 3.5. Implement storage service encryption

- All data (including metadata) written to Azure Storage is automatically encrypted using Storage Service Encryption (SSE).
- Microsoft Entra ID and Role-Based Access Control (RBAC) are supported for Azure Storage for both resource management operations and data operations, as follows:
    - You can assign RBAC roles scoped to the storage account to security principals and use Microsoft Entra ID to authorize resource management operations such as key management.
    - Microsoft Entra integration is supported for blob and queue data operations. You can assign RBAC roles scoped to a subscription, resource group, storage account, or an individual container or queue to a security principal or a managed identity for Azure resources.
- Data can be secured in transit between an application and Azure by using Client-Side Encryption, HTTPS, or SMB 3.0.
- OS and data disks used by Azure virtual machines can be encrypted using Azure Disk Encryption.
- Delegated access to the data objects in Azure Storage can be granted using a shared access signature.

**Azure Storage Service Encryption (SSE) for data at rest. -** 

- When a new storage account is provisioned, Azure Storage Encryption is automatically enabled for it and it cannot be disabled. Storage accounts are encrypted regardless of their performance tier (standard or premium) or deployment model (Azure Resource Manager or classic). All Azure Storage redundancy options support encryption, and all copies of a storage account are encrypted. All Azure Storage resources are encrypted, including blobs, disks, files, queues, and tables. All object metadata is also encrypted.
- Data in Azure Storage is encrypted and decrypted transparently using 256-bit AES encryption, one of the strongest block ciphers available, and is FIPS 140-2 compliant. 
- Azure Storage encryption is similar to BitLocker encryption on Windows.
- Encryption does not affect Azure Storage performance. There is no additional cost for Azure Storage encryption.

**Encryption key management**

You can rely on Microsoft-managed keys for the encryption of your storage account, or you can manage encryption with your own keys. If you choose to manage encryption with your own keys, you have two options:

- You can specify a _customer-managed_ key to use for encrypting and decrypting all data in the storage account. A customer-managed key is used to encrypt all data in all services in your storage account.
- You can specify a _customer-provided_ key on Blob storage operations. A client making a read or write request against Blob storage can include an encryption key on the request for granular control over how blob data is encrypted and decrypted.

The following table compares key management options for Azure Storage encryption.

|  | **Microsoft-managed keys** | **Customer-managed keys** | **Customer-provided keys** |
|---|---|---|---|
| Encryption/decryption operations|Azure|Azure|Azure|
| Azure Storage services supported|All|Blob storage, Azure Files|Blob storage|
| Key storage|Microsoft key store|Azure Key Vault|Azure Key Vault or any other key store|
| Key rotation responsibility|Microsoft|Customer|Customer|
| Key usage|Microsoft|Azure portal, Storage Resource Provider REST API, Azure Storage management libraries, PowerShell, CLI|Azure Storage REST API (Blob storage), Azure Storage client libraries|
| Key access|Microsoft only|Microsoft, Customer|Customer only|


### 3.6. Configure blob data retention policies

**Immutable storage in Azure blob storage:*

Immutable storage for Azure Blob storage enables users to store business-critical data objects in a WORM (Write Once, Read Many) state. Immutable storage is available for general-purpose v2 and Blob storage accounts in all Azure regions.

*Time-based retention policy support*: Users can set policies to store data for a specified interval. When a time-based retention policy is set, blobs can be created and read, but not modified or deleted. After the retention period has expired, blobs can be deleted but not overwritten. When a time-based retention policy is applied on a container, all blobs in the container will stay in the immutable state for the duration of the effective retention period. The effective retention period for blobs is equal to the difference between the blob's creation time and the user-specified retention interval. Because users can extend the retention interval, immutable storage uses the most recent value of the user-specified retention interval to calculate the effective retention period.

*Legal hold policy support*: If the retention interval is not known, users can set legal holds to store immutable data until the legal hold is cleared. When a legal hold policy is set, blobs can be created and read, but not modified or deleted. Each legal hold is associated with a user-defined alphanumeric tag (such as a case ID, event name, etc.) that is used as an identifier string. Legal holds are temporary holds that can be used for legal investigation purposes or general protection policies. Each legal hold policy needs to be associated with one or more tags. Tags are used as a named identifier, such as a case ID or event, to categorize and describe the purpose of the hold.

*Support for all blob tiers*: WORM policies are independent of the Azure Blob storage tier and apply to all the tiers: hot, cool, and archive. Users can transition data to the most cost-optimized tier for their workloads while maintaining data immutability.

*Container-level configuration*: Users can configure time-based retention policies and legal hold tags at the container level. By using simple container-level settings, users can create and lock time-based retention policies, extend retention intervals, set and clear legal holds, and more. These policies apply to all the blobs in the container, both existing and new.

*Audit logging support*: Each container includes a policy audit log. It shows up to seven time-based retention commands for locked time-based retention policies and contains the user ID, command type, time stamps, and retention interval. For legal holds, the log contains the user ID, command type, time stamps, and legal hold tags. This log is retained for the lifetime of the policy, in accordance with the SEC 17a-4(f) regulatory guidelines. The Azure Activity Log shows a more comprehensive log of all the control plane activities; while enabling Azure Resource Logs retains and shows data plane operations. It is the user's responsibility to store those logs persistently, as might be required for regulatory or other purposes.

>A container can have both a legal hold and a time-based retention policy at the same time. All blobs in that container stay in the immutable state until all legal holds are cleared, even if their effective retention period has expired. Conversely, a blob stays in an immutable state until the effective retention period expires, even though all legal holds have been cleared.

### 3.7. Storage Account Keys
Generated by Azure when creating the storage account. Azure generates 2 keys of 512-BITS. You use these keys to authorize access to data that resides in your storage account via Shared Key authorization. Azure KeyVault simplefies this process and allows your to perform the rotation of keys without  interrupting the applications.

### 3.8. Configure Azure files authentication

Azure Files supports identity-based authentication over Server Message Block (SMB) through on-premises Active Directory Domain Services (AD DS) and Microsoft Entra Domain Services (Microsoft Entra Domain Services).  With RBAC, the credentials you use for file access should be available or synced to Microsoft Entra ID.

Azure Files enforces authorization on user access to both the share and the directory/file levels.

At the directory/file level, Azure Files supports preserving, inheriting, and enforcing Windows DACLs just like any Windows file servers. You can choose to keep Windows DACLs when copying data over SMB between your existing file share and your Azure file shares. Whether you plan to enforce authorization or not, you can use Azure file shares to back up ACLs along with your data.

**Benefits of Identity-based authentication over using Shared Key authentication:**

- Extend the traditional identity-based file share access experience to the cloud with on-premises AD DS and Microsoft Entra Domain Services.
- Enforce granular access control on Azure file shares.
- Back up Windows ACLs (also known as NTFS) along with your data. You can copy ACLs on a directory or file to Azure file shares using either Azure File Sync or common file movement toolsets. For example, you can use robocopy with the /copy:s flag to copy data as well as ACLs to an Azure file share. ACLs are preserved by default, you are not required to enable identity-based authentication on your storage account to preserve ACLs.

**How it works:**

![Diagram of how identity-based authentication works or Azure files.](https://learn.microsoft.com/en-us/training/wwl-azure/storage-security/media/az500-azure-files-authentication-6d7a7c7d.png)


### 3.9. Enable the secure transfer required property

You can configure your storage account to accept requests from secure connections only by setting the Secure transfer required property for the storage account. When you require secure transfer, any requests originating from an insecure connection are rejected. Microsoft recommends that you always require secure transfer for all of your storage accounts.

Connecting to an Azure File share over SMB without encryption fails when secure transfer is required for the storage account. Examples of insecure connections include those made over SMB 2.1, SMB 3.0 without encryption, or some versions of the Linux SMB client. Azure Files connections require encryption (SMB)

**By default, the Secure transfer required property is enabled when you create a storage account**. Azure Storage doesn't support HTTPS for **custom domain names**, this option is not applied when you're using a custom domain name.



## 4. SQL database security

### 4.1. SQL database authentication

A user is authenticated using one of the following two authentication methods:

- **SQL authentication** - With this authentication method, the user submits a user account name and associated password to establish a connection. This password is stored in the master database for user accounts linked to a login or stored in the database containing the user accounts not linked to a login.
- **Microsoft Entra authentication** - With this authentication method, the user submits a user account name and requests that the service use the credential information stored in Microsoft Entra ID.

You can create user accounts in the master database, and grant permissions in all databases on the server, or you can create them in the database itself (called contained database users). By using contained databases, you obtain enhance portability and scalability.

**Logins and users**: In Azure SQL, a user account in a database can be associated with a login that is stored in the master database or can be a user name that is stored in an individual database.

- A **login** is an individual account in the master database, to which a user account in one or more databases can be linked. With a login, the credential information for the user account is stored with the login.
- A **user account** is an individual account in any database that may be but does not have to be linked to a login. With a user account that is not linked to a login, the credential information is stored with the user account.

**Authorization** to access data and perform various actions are managed using database roles and explicit permissions.  Authorization is controlled by your user account's database role memberships and object-level permissions.

Best practices:
- you should grant users the least privileges necessary.
- your application should use a dedicated account to authenticate.
- Recommendation: to create a contained database user, which allows your app to authenticate directly to the database.

>Use Microsoft Entra authentication to centrally manage identities of database users and as an alternative to SQL Server authentication.

![swl authentication](img/az-500_36.png)


### 4.2. Configure SQL database firewalls

Azure SQL Database and Azure Synapse Analytics, previously SQL Data Warehouse, (both referred to as SQL Database in this lesson) provide a relational database service for Azure and other internet-based applications. 

Initially, all access to your Azure SQL Database is blocked by the SQL Database firewall.

The firewall grants access to databases based 
- on the originating IP address of each request.
- on  virtual network rules based on virtual network service endpoints. Virtual network rules might be preferable to IP rules in some cases.

Azure SQL Firewall  IP Rules: 
- *Server-level IP firewall rules* allow clients to access the entire Azure SQL server, which includes all databases hosted in it. The master database holds these rules. You can configure a maximum of 128 server-level IP firewall rules for an Azure SQL server. You can configure server-level IP firewall rules using the Azure portal, PowerShell, or by using Transact-SQL statements. To create server-level IP firewall rules using the Azure portal or PowerShell, you must be the subscription owner or a subscription contributor. To create a server-level IP firewall rule using Transact-SQL, you must connect to the SQL Database instance as the server-level principal login or the Microsoft Entra administrator (which means that a server-level IP firewall rule must have first been created by a user with Azure-level permissions).
- Database-level IP firewall rules are used to allow access to specific databases on a SQL Database server. You can create them for each database, included the master database. Also, there is a maximum of 128 rules. ou can only create and manage database-level IP firewall rules for master databases and user databases by using Transact-SQL statements, and only after you have configured the first server-level firewall.


>Azure Synapse Analytics only supports server-level IP firewall rules, and not database-level IP firewall rules.

Data-level Firewall rules get evaluated first:

![firewall rules for SQL databases](img/az-500_37.png)


To allow applications from Azure to connect to your Azure SQL Database, Azure connections must be enabled. When an application from Azure attempts to connect to your database server, the firewall verifies that Azure connections are allowed. A firewall setting with starting and ending addresses equal to 0.0.0.0 indicates Azure connections are allowed. This option configures the firewall to allow all connections from Azure including connections from the subscriptions of other customers. When selecting this option, make sure your sign-in and user permissions limit access to authorized users only.

>Whenever possible, as a best practice, use database-level IP firewall rules to enhance security and to make your database more portable. Use server-level IP firewall rules for administrators and when you have several databases with the same access requirements, and you don't want to spend time configuring each database individually.


### 4.3. Enable and monitor database auditing

Auditing for Azure SQL Database and Azure Synapse Analytics tracks database events and writes them to an audit log in your Azure storage account, Log Analytics workspace or Event Hubs.

Auditing also:

- Helps you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that could indicate business concerns or suspected security violations.
- Enables and facilitates adherence to compliance standards, although it **doesn't guarantee compliance**.

You can use SQL database auditing to:

- **Retain** an audit trail of selected events. You can define categories of database actions to be audited.
- **Report** on database activity. You can use pre-configured reports and a dashboard to get started quickly with activity and event reporting.
- **Analyze** reports. You can find suspicious events, unusual activity, and trends.

**In auditing, server-level auditing policies take precedence over database-label auditing policies**. This means that:  

- A server policy applies to all existing and newly created databases on the server.
- If server auditing is enabled, it always applies to the database. The database will be audited, regardless of the database auditing settings.
- Enabling auditing on the database or data warehouse, in addition to enabling it on the server, does not override or change any of the settings of the server auditing. Both audits will exist side by side. In other words, the database is audited twice in parallel; once by the server policy and once by the database policy.

### 4.4. Implement data discovery and classification

Data discovery and classification provides advanced capabilities built into Azure SQL Database for discovering, classifying, labeling and protecting sensitive data (such as business, personal data, and financial information) in your databases. Discovering and classifying this data can play a pivotal role in your organizational information protection stature. It can serve as infrastructure for:

- Helping meet data privacy standards and regulatory compliance requirements.
- Addressing various security scenarios such as monitoring, auditing, and alerting on anomalous access to sensitive data.
- Controlling access to and hardening the security of databases containing highly sensitive data.

Data exists in one of three basic states: at **rest**, in **process**, and in **transit**. All three states require unique technical solutions for data classification, but the applied principles of data classification should be the same for each. Data that is classified as confidential needs to stay confidential when at rest, in process, or in transit.

Data can also be either **structured** or **unstructured**. Typical classification processes for structured data found in databases and spreadsheets are less complex and time-consuming to manage than those for unstructured data such as documents, source code, and email. Generally, organizations will have more unstructured data than structured data.

**Protect data at rest**

|**Best practice**|**Solution**|
|---|---|
|Apply disk encryption to help safeguard your data.|Use Microsoft Azure Disk Encryption, which enables IT administrators to encrypt both Windows infrastructure as a service (IaaS) and Linux IaaS virtual machine (VM) disks. Disk encryption combines the industry-standard BitLocker feature and the Linux DM-Crypt feature to provide volume encryption for the operating system (OS) and the data disks. ‎Azure Storage and Azure SQL Database encrypt data at rest by default, and many services offer encryption as an option. You can use Azure Key Vault to maintain control of keys that access and encrypt your data.|
|Use encryption to help mitigate risks related to unauthorized data access.|Encrypt your drives before you write sensitive data to them.|

**Protect data in transit**

We generally recommend that you always use SSL/TLS protocols to exchange data across different locations. . In some circumstances, you might want to isolate the entire communication channel between your on-premises and cloud infrastructures by using a VPN. For data moving between your on-premises infrastructure and Azure, consider appropriate safeguards such as HTTPS or VPN. When sending encrypted traffic between an Azure virtual network and an on-premises location over the public internet, use Azure VPN Gateway.

|**Best practice**|**Solution**|
|---|---|
|Secure access from multiple workstations located on-premises to an Azure virtual network|Use site-to-site VPN.|
|Secure access from an individual workstation located on-premises to an Azure virtual network|Use point-to-site VPN.|
|Move larger data sets over a dedicated high-speed wide area network (WAN) link|Use Azure ExpressRoute. If you choose to use ExpressRoute, you can also encrypt the data at the application level by using SSL/TLS or other protocols for added protection.|
|Interact with Azure Storage through the Azure portal|All transactions occur via HTTPS. You can also use Storage REST API over HTTPS to interact with Azure Storage and Azure SQL Database.|


Data discovery and classification is part of the **Advanced Data Security offering**, which is a unified package for advanced Microsoft SQL Server security capabilities. You access and manage data discovery and classification via the central **SQL Advanced Data Security portal**.

- **Discovery and recommendations** - The classification engine scans your database and identifies columns containing potentially sensitive data. It then provides you with an easier way to review and apply the appropriate classification recommendations via the Azure portal.
- **Labeling** - Sensitivity classification labels can be persistently tagged on columns using new classification metadata attributes introduced into the SQL Server Engine. This metadata can then be utilized for advanced sensitivity-based auditing and protection scenarios.
- **Information Types** - These provide additional granularity into the type of data stored in the column.
- **Query result set sensitivity** - The sensitivity of the query result set is calculated in real time for auditing purposes.
- **Visibility** - You can view the database classification state in a detailed dashboard in the Azure portal. Additionally, you can download a report (in Microsoft Excel format) that you can use for compliance and auditing purposes, in addition to other needs.

SQL data discovery and classification comes with a built-in set of sensitivity labels and information types, and discovery logic. You can now customize this taxonomy and define a set and ranking of classification constructs specifically for your environment. Definition and customization of your classification taxonomy takes place in one central location for your entire Azure Tenant. That location is in Microsoft Defender for Cloud, as part of your Security Policy. Only a user with administrative rights on the Tenant root management group can perform this task.

### 4.5. Microsoft Defender for SQL

Applies to: **Azure SQL Database** | **Azure SQL Managed Instance** | **Azure Synapse Analytics**

Microsoft Defender for SQL includes functionality for surfacing and mitigating potential database vulnerabilities and detecting anomalous activities that could indicate a threat to your database. It provides a single go-to location for enabling and managing these capabilities.

Microsoft Defender for SQL provides: 

- *Vulnerability Assessment* is an easy-to-configure service that can discover, track, and help you remediate potential database vulnerabilities. It provides visibility into your security state, and it includes actionable steps to resolve security issues and enhance your database fortifications.
- *Advanced Threat Protection* detects anomalous activities indicating unusual and potentially harmful attempts to access or exploit your database. It continuously monitors your database for suspicious activities, and it provides immediate security alerts on potential vulnerabilities, Azure SQL injection attacks, and anomalous database access patterns. Advanced Threat Protection alerts provide details of suspicious activity and recommend action on how to investigate and mitigate the threat.

Enabling or managing Microsoft Defender for SQL settings requires belonging to the SQL security manager role or one of the database or server admin roles.

#### Vulnerability assessment for SQL Server

Applies to: Azure SQL Database | Azure SQL Managed Instance | Azure Synapse Analytics

- Vulnerability assessment is a scanning service built into Azure SQL Database.
- The service employs a knowledge base of rules that flag security vulnerabilities.
- These rules cover database-level issues and server-level security issues, like server firewall settings and server-level permissions. - Permission configurations. - Feature configurations. - Database settings
- The results of the scan include actionable steps to resolve each issue and provide customized remediation scripts where applicable.
- Vulnerability assessment is part of Microsoft Defender for Azure SQL, which is a unified package for advanced SQL security capabilities. Vulnerability assessment can be accessed and managed from each SQL database resource in the Azure portal.

**SQL vulnerability assessment express and classic configurations. -** You can configure vulnerability assessment for your SQL databases with either:

- Express configuration (preview) – The default procedure that lets you configure vulnerability assessment without dependency on external storage to store baseline and scan result data.
- Classic configuration – The legacy procedure that requires you to manage an Azure storage account to store baseline and scan result data.

![sql vulnerability assessment express and classic configurations comparison](img/az-500_38.png)

### 4.6. SQL Advanced Threat Protection

Applies to: Azure SQL Database | Azure SQL Managed Instance | Azure Synapse Analytics | SQL Server on Azure Virtual Machines | Azure Arc-enabled SQL Server

- SQL Advanced Threat Protection detects anomalous activities indicating unusual and potentially harmful attempts to access or exploit databases.
- Users receive an alert upon suspicious database activities, potential vulnerabilities, and SQL injection attacks, as well as anomalous database access and queries patterns.
- Advanced Threat Protection integrates alerts with Microsoft Defender for Cloud.
- For a full investigation experience, it is recommended to enable auditing, which writes database events to an audit log in your Azure storage account.
- **Click** the **Advanced Threat Protection alert** to launch the Microsoft Defender for Cloud alerts page and get an overview of active SQL threats detected on the database.
- Advanced Threat Protection is part of the Microsoft Defender for SQL offering, which is a unified package for advanced SQL security capabilities. Advanced Threat Protection can be accessed and managed via the central Microsoft Defender for SQL portal.

### 4.7. SQL Database Dynamic Data Masking (DDM) 

Dynamic data masking helps prevent unauthorized access to sensitive data by enabling customers to designate how much of the sensitive data to reveal with minimal impact on the application layer. You set up a dynamic data masking policy in the Azure portal by selecting the dynamic data masking operation in your SQL Database configuration blade or settings blade. This feature cannot be set by using portal for Azure Synapse

**Configuring DDM policy. -**

- **SQL users excluded from masking** - A set of SQL users or Microsoft Entra identities that get unmasked data in the SQL query results. Users with administrator privileges are always excluded from masking, and view the original data without any mask.
- **Masking rules** - A set of rules that define the designated fields to be masked and the masking function that is used. The designated fields can be defined using a database schema name, table name, and column name.
- **Masking functions** - A set of methods that control the exposure of data for different scenarios.

The DDM recommendations engine, flags certain fields from your database as potentially sensitive fields, which may be good candidates for masking. In the Dynamic Data Masking blade in the portal, you can review the recommended columns for your database. All you need to do is click **Add Mask** for one or more columns and then **Save** to apply a mask for these fields.

### 4.8. Implement Transparent Data Encryption (TDE)

- Applies to Azure SQL Database | Azure SQL Managed Instance |  Synapse SQL in Azure Synapse Analytics.
- To configure TDE through the Azure portal, you must be connected as the Azure Owner, Contributor, or SQL Security Manager.
- Encrypts data at rest. 
- It performs real-time encryption and decryption of the database, associated backups, and transaction log files at rest without requiring changes to the application.
- **By default, TDE is enabled for all newly deployed Azure SQL databases** and needs to be manually enabled for older databases of Azure SQL Database, Azure SQL Managed Instance, or Azure Synapse.
- It cannot be used to encrypt the logical master database because this db contains objects that TDE needs to perform the encrypt/decrypt operations. 
-  TDE encrypts the storage of an entire database by using a symmetric key called the Database Encryption Key (DEK).
- DEK is protected by the TDE protector. Where is this TDE protector set?:
	- *At the logical SQL server level*: For Azure SQL Database and Azure Synapse, the TDE protector is set at the logical SQL server level and is inherited by all databases associated with that server. 
	- *At the instance level*: For Azure SQL Managed Instance (BYOK feature in preview), the TDE protector is set at the instance level and it is inherited by all encrypted databases on that instance.


TDE protector is either a service-managed certificate (service-managed transparent data encryption) or an asymmetric key stored in Azure Key Vault (customer-managed transparent data encryption)

-  The default setting for TDE is that the DEK is protected by a built-in server certificate. 
	- If two databases are connected to the same server, they also share the same built-in certificate.
	- The built-in server certificate is unique for each server and the encryption algorithm used is AES 256.
	- Microsoft automatically rotates these certificates. Additionally, Microsoft seamlessly moves and manages the keys as needed for geo-replication and restores.
	- the root key is protected by a Microsoft internal secret store. 
- With Customer-managed TDE or Bring Your Own Key (BYOK),  the TDE Protector that encrypts the DEK is a customer-managed asymmetric key, which is stored in a customer-owned and managed Azure Key Vault (Azure's cloud-based external key management system) and never leaves the key vault.
	-  The TDE Protector can be generated by the key vault or transferred to the key vault from an on premises hardware security module (HSM) device. 
	- SQL Database needs to be granted permissions to the customer-owned key vault to decrypt and encrypt the DEK. 
	- With TDE with Azure Key Vault integration, users can control key management tasks including key rotations, key vault permissions, key backups, and enable auditing/reporting on all TDE protectors using Azure Key Vault functionality.

Turn on and off TDE from Azure portal.

Except for Azure SQL Managed Instance, there you need to use T-SQL to turn TDE on and off on a database.

>Transact-SQL (T-SQL) is an extension of the standard SQL (Structured Query Language) used for querying and managing relational databases, particularly in the context of Microsoft SQL Server and Azure SQL Database. It is needed and used for the following reasons:
>1. **Procedural Capabilities**: T-SQL includes procedural programming constructs such as variables, loops, and conditional statements, which are not part of standard SQL.
>2. **SQL Server Specific Functions**: T-SQL includes functions and features that are specific to SQL Server and may not be supported by other database management systems.
>3. **System Management**: T-SQL provides commands and procedures for managing SQL Server instances, databases, and security, which are not part of the standard SQL language.
>4. **Error Handling**: T-SQL has error handling mechanisms like TRY...CATCH blocks, which are not part of the standard SQL syntax.


### 4.9. Azure SQL Always Encrypted

Always Encrypted helps protect sensitive data at rest on the server, during movement between client and server, and while the data is in use. Always Encrypted ensures that sensitive data never appears as plaintext inside the database system. After you configure data encryption, only client applications or app servers that have access to the keys can access plaintext data. Always Encrypted uses the AEAD_AES_256_CBC_HMAC_SHA_256 algorithm to encrypt data in the database.

Always Encrypted allows clients to encrypt sensitive data inside client applications and never reveal the encryption keys to the Database Engine (SQL Database or SQL Server).

> **An example:** *Client On-Premises with Data in Azure* __ A customer has an on-premises client application at their business location. The application operates on sensitive data stored in a database hosted in Azure (SQL Database or SQL Server running in a virtual machine on Microsoft Azure). The customer uses Always Encrypted and stores Always Encrypted keys in a trusted key store hosted on-premises, to ensure Microsoft cloud administrators have no access to sensitive data.
> *Client and Data in Azure* __ A customer has a client application, hosted in Microsoft Azure (for example, in a worker role or a web role), which operates on sensitive data stored in a database hosted in Azure (SQL Database or SQL Server running in a virtual machine on Microsoft Azure). Although Always Encrypted does not provide complete isolation of data from cloud administrators, as both the data and keys are exposed to cloud administrators of the platform hosting the client tier, the customer still benefits from reducing the security attack surface area (the data is always encrypted in the database).

The Always Encrypted-enabled driver automatically encrypts and decrypts sensitive data in the client application before sending the data off to the SQL server. Always Encrypted supports two types of encryption: randomized encryption and deterministic encryption.

- **Deterministic encryption** always generates the same encrypted value for any given plain text value. Using deterministic encryption allows point lookups, equality joins, grouping and indexing on encrypted columns. However, it may also allow unauthorized users to guess information about encrypted values by examining patterns in the encrypted column, especially if there is a small set of possible encrypted values, such as True/False, or North/South/East/West region. Deterministic encryption must use a column collation with a binary2 sort order for character columns.
- **Randomized encryption** uses a method that encrypts data in a less predictable manner. Randomized encryption is more secure, but prevents searching, grouping, indexing, and joining on encrypted columns.

Available is all editions of Azure SQL Database starting with SQL Server 2016.

**Deploy an always encrypted implementation. -** 

The initial setup of Always Encrypted in a database involves generating Always Encrypted keys, creating key metadata, configuring encryption properties of selected database columns, and/or encrypting data that may already exist in columns that need to be encrypted.

Some of these tasks aren't supported in Transact-SQL. You can use SQL Server Management Studio (SSMS) or PowerShell to accomplish such tasks.


|**Task**|**SSMS**|**PowerShell**|**SQL**|
|---|---|---|---|
|Provisioning column master keys, column encryption keys and encrypted column encryption keys with their corresponding column master keys|Yes|Yes|No|
|Creating key metadata in the database|Yes|Yes|Yes|
|Creating new tables with encrypted columns|Yes|Yes|Yes|
|Encrypting existing data in selected database columns|Yes|Yes|No|

When setting up encryption for a column, you specify the information about the encryption algorithm and cryptographic keys used to protect the data in the column. Always Encrypted uses two types of keys: column encryption keys and column master keys. A column encryption key is used to encrypt data in an encrypted column. A column master key is a key-protecting key that encrypts one or more column encryption keys.

The Database Engine stores encryption configuration for each column in database metadata. Note, however, the Database Engine never stores or uses the keys of either type in plaintext. It only stores encrypted values of column encryption keys and the information about the location of column master keys, which are stored in external trusted key stores, such as Azure Key Vault, Windows Certificate Store on a client machine, or a hardware security module.

To access data stored in an encrypted column in plaintext, an application must use an Always Encrypted enabled client driver. When an application issues a parameterized query, the driver transparently collaborates with the Database Engine to determine which parameters target encrypted columns and, thus, should be encrypted. For each parameter that needs to be encrypted, the driver obtains the information about the encryption algorithm and the encrypted value of the column encryption key for the column, the parameter targets, as well as the location of its corresponding column master key.

Next, the driver contacts the key store, containing the column master key, in order to decrypt the encrypted column encryption key value and then, it uses the plaintext column encryption key to encrypt the parameter. The resultant plaintext column encryption key is cached to reduce the number of round trips to the key store on subsequent uses of the same column encryption key. The driver substitutes the plaintext values of the parameters targeting encrypted columns with their encrypted values, and it sends the query to the server for processing.

The server computes the result set, and for any encrypted columns included in the result set, the driver attaches the encryption metadata for the column, including the information about the encryption algorithm and the corresponding keys. The driver first tries to find the plaintext column encryption key in the local cache, and only makes a round to the column master key if it can't find the key in the cache. Next, the driver decrypts the results and returns plaintext values to the application.

A client driver interacts with a key store, containing a column master key, using a column master key store provider, which is a client-side software component that encapsulates a key store containing the column master key. Providers for common types of key stores are available in client-side driver libraries from Microsoft or as standalone downloads. You can also implement your own provider. Always Encrypted capabilities, including built-in column master key store providers vary by a driver library and its version.






