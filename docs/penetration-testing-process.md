---
title: Pentesting Notes
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - CPTS
  - eWPT
---

# Penetration Testing Process: A General *Approach* to the Profession


??? abstract "Sources for these notes"
    - [Hack The Box: Penetration Testing Learning Path](https://academy.hackthebox.com/path/preview/penetration-tester)
    - [INE eWPT2 Preparation course](https://my.ine.com/CyberSecurity/courses/87d3a24a/introduction-to-web-application-security-testing)

Resources:

- [https://pentestreports.com/](https://pentestreports.com/)


## Types of Penetration Testing

| **Type**         | **Information Provided**                                                                                                                                                                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Blackbox`       | `Minimal`. Only the essential information, such as IP addresses and domains, is provided.                                                                                                                                                                             |
| `Greybox`        | `Extended`. In this case, we are provided with additional information, such as specific URLs, hostnames, subnets, and similar.                                                                                                                                        |
| `Whitebox`       | `Maximum`. Here everything is disclosed to us. This gives us an internal view of the entire structure, which allows us to prepare an attack using internal information. We may be given detailed configurations, admin credentials, web application source code, etc. |
| `Red-Teaming`    | May include physical testing and social engineering, among other things. Can be combined with any of the above types.                                                                                                                                                 |
| `Purple-Teaming` | It can be combined with any of the above types. However, it focuses on working closely with the defenders.                                                                                                                                                            |

### Types of Testing Environments

Apart from the test method and the type of test, another consideration is what is to be tested, which can be summarized in the following categories:

|         |         |                   |                   |               |
| ------- | ------- | ----------------- | ----------------- | ------------- |
| Network | Web App | Mobile            | API               | Thick Clients |
| IoT     | Cloud   | Source Code       | Physical Security | Employees     |
|  Hosts  | Server  | Security Policies | Firewalls         | IDS/IPS       |

## Phases

### Pre-engagement

The pre-engagement phase of a penetration testing is a crucial step that lays the foundation for a successful and well-planned security assessment.
It involves preliminary preparations, understanding project requirements, and obtaining necessary authorizations before initiating the actual testing.
During the pre-engagement phase, the penetration tester and the client must discuss and agree upon a number of legal and technical details pertinent to the execution and outcomes of the security assessment.

This can be one or more documents with the objective to define the following:

- Objectives:: Clearly define the objectives and goals of the penetration test. Understand what the stakeholders aim to achieve through the testing process. 
- Scope of the engagement: Identify the scope of the penetration test, including the specific web applications, URLs, and functionalities to be tested. Define the scope boundaries and limitations, such as which systems or networks are out-of-scope for testing.
- Timeline & milestones
- Liabilities & responsibility: Obtain proper authorization from the organization's management or application owners to conduct the penetration test. Ensure that the testing activities comply with any legal or regulatory requirements, and that all relevant permissions are secured.
- Rules of Engagement (RoE): Establish a set of Rules of Engagement that outline the specific rules, constraints, and guidelines for the testing process. Include details about the testing schedule, testing hours, communication channels, and escalation procedures.
- Communication and Coordination: Establish clear communication channels with key stakeholders, including IT personnel, development teams, and management. Coordinate with relevant personnel to ensure minimal disruption to the production environment during testing.
- Expectations and deliverables
- Statement of work
- The Scoping Meeting: Conduct a scoping meeting with key stakeholders to discuss the testing objectives, scope, and any specific concerns or constraints. Use this meeting to clarify expectations and ensure everyone is aligned with the testing approach.
- List of documents so far:


| **Document**                                                                       | **Timing for Creation**                         |     |
| ---------------------------------------------------------------------------------- | ----------------------------------------------- | --- |
| Non-Disclosure Agreement (NDA)                                                     | After Initial Contact                           |     |
| Scoping Questionnaire                                                              | Before the Pre-Engagement Meeting               |     |
| Scoping Document                                                                   | During the Pre-Engagement Meeting               |     |
| [Penetration Testing Proposal (Contract/Scope of Work (SoW))](#contract-checklist) | During the Pre-engagement Meeting               |     |
| [Rules of Engagement (RoE)](#rules-of-engagement)                                  | Before the Kick-Off Meeting                     |     |
| [Contractors Agreement (Physical Assessments)](#contractors-agreement)             | Before the Kick-Off Meeting                     |     |
| Reports                                                                            | During and after the conducted Penetration Test |     |

- Risk Assessment and Acceptance: Perform a risk assessment to understand the potential impact of the penetration test on the web application and the organization. Obtain management's acceptance of any risks associated with the testing process.
-  Engagement Kick-off: Officially kick-off the penetration test, confirming the start date and timeline with the organization's stakeholders. Share the RoE and any other relevant details with the testing team.



### Information gathering

We could tell 4 categories:

-   Open-Source Intelligence
-   Infrastructure Enumeration
-   Service Enumeration
-   Host Enumeration

A different way to approach to footprinting is considering the following layers:

| **Layer**                | **Description**                                                                                        | **Information Categories**                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `1. Internet Presence`   | Identification of internet presence and externally accessible infrastructure.                          | Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures      |
| `2. Gateway`             | Identify the possible security measures to protect the company's external and internal infrastructure. | Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare                  |
| `3. Accessible Services` | Identify accessible interfaces and services that are hosted externally or internally.                  | Service Type, Functionality, Configuration, Port, Version, Interface                               |
| `4. Processes`           | Identify the internal processes, sources, and destinations associated with the services.               | PID, Processed Data, Tasks, Source, Destination                                                    |
| `5. Privileges`          | Identification of the internal permissions and privileges to the accessible services.                  | Groups, Users, Permissions, Restrictions, Environment                                              |
| `6. OS Setup`            | Identification of the internal components and systems setup.                                           | OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files |


#### Cloud resources

Often cloud storage is added to the DNS list when used for administrative purposes by other employees.

```shell-session
for i in $(cat subdomainlist);do host $i | grep "has address" | grep example.com | cut -d" " -f1,4;done
```

More ways to find cloud storage:

**google dork**:

```
# Google search for AWS
intext: example.com inurl:amazonaws.com

# Google search for Azure
intext: example.com inurl:blob.core.windows.net
```

**Source code from the application**: For instance

```
<link rel='dns-prefetch' href="//example.blob.core.windows.net">
```

[domain.glass](https://domain.glass) service also provides cloud search services for a passive reconnaissance.

[GrayHatWarfare](https://buckets.grayhatwarfare.com) is also noticeable. With this tool you can filter private and public keys leaked.


### Vulnerability assessment

During the `vulnerability assessment` phase, we examine and analyze the information gathered during the information gathering phase.
In `Vulnerability Research`, we look for known vulnerabilities, exploits, and security holes that have already been discovered and reported.
After that, we should mirror the target system locally as precisely as possible to replicate our testing locally.

The purpose of a `Vulnerability Assessment` is to understand, identify, and categorize the risk for the more apparent issues present in an environment without actually exploiting them to gain further access.

Types of tests: black box, gray box and white box.

Specializations: 

- Application pentesters.
- Network or infraestructure pentesters.
- Physical pentesters.
- Social engineering pentesters.


Types of Security assessments:

- Vulnerability assessment.
- Penetration test.
- Security audits.
- Bug bounties. 
- Red team assessments.
- Purple team assessments.

`Vulnerability Assessments` and Penetration Tests are two completely different assessments. Vulnerability assessments look for vulnerabilities in networks without simulating cyber attacks. `Penetration tests`, depending on their type, evaluate the security of different assets and the impact of the issues present in the environment. 

![penetration testing vs. vulnerability assessment](img/vulnerabilityassessment-diagram.png)
[Source: HTB Academy and predatech.co.uk](https://predatech.co.uk/wp-content/uploads/2021/01/Vulnerability-Assessment-vs-Penetration-Testing-min-2.png)

Compliance standards

- Payment Card Industry Data Security Standard (PCI DSS).
- Health Insurance Portability and Accountability Act (HIPAA).
- Federal Information Security Management Act (FISMA).
- ISO 27001.
- The `NIST` (`National Institute of Standards and Technology`) is well known for their [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework).
- `OWASP` stands for the [Open Web Application Security Project](https://owasp.org):
	-  [Web Security Testing Guide (WSTG)](https://owasp.org/www-project-web-security-testing-guide/)
	- [Mobile Security Testing Guide (MSTG)](https://owasp.org/www-project-mobile-security-testing-guide/)
	- [Firmware Security Testing Methodology](https://github.com/scriptingxss/owasp-fstm)


Frameworks for Pentesting:

-  [Penetration Testing Execution Standard](http://www.pentest-standard.org/index.php/Main_Page) (`PTES`). 
- `Open Source Security Testing Methodology Manual` ([OSSTMM](https://www.isecom.org/OSSTMM.3.pdf)).
- [Common Vulnerability Scoring System (CVSS)](cvss-common-vulnerability-scoring-system.md).
- [Common Vulneravilities and Exposures](cve-common-vulnerabilities-and-exposures.md).

**Scanners**: [OpenVAS](openvas.md), [Nessus](nessus.md), Nexpose, and Qualys.


### Exploitation

Once we have set up the system locally and installed known components to mirror the target environment as closely as possible, we can start preparing the exploit by following the steps described in the exploit. Then we test this on a locally hosted VM to ensure it works and does not damage significantly.

- [Transferring File Techniques: Linux](transferring-files-techniques-linux.md).
- [Transferring File Techniques: Windows](transferring-files-techniques-windows.md)
- [Transferring files with code](transferring-files-techniques-code.md).
- [File Encryption: windows and linux ](file-encryption.md).
- [LOLbins - "Living off the land" binaries: LOLbas and GTFObins](lolbins-lolbas-gtfobins.md).
- [Evading detection in file transfers](transferring-files-evading-detection.md).


### Post-exploitation

The `Post-Exploitation` stage aims to obtain sensitive and security-relevant information from a local perspective and business-relevant information that, in most cases, requires higher privileges than a standard user. This stage includes the following components:

- Evasive Testing: watch out with running commands such as net user or whoami that is often monitored by EDR systems and flagged as anomalous activity. Three methods: Evasive, Hybrid evasive, and Non-evasive.
- Information Gathering. The information gathering stage starts all over again from the local perspective. We also enumerate the local network and local services such as printers, database servers, virtualization services, etc.
- Pillaging. Pillaging is the stage where we examine the role of the host in the corporate network. We analyze the network configurations, including but not limited to: Interfaces, Routing, DNS, ARP, Services, VPN, IP Subnets, Shares, Network Traffic.
- Vulnerability Assessment: it is essential to distinguish between exploits that can harm the system and attacks against the services that do not cause any disruption.
- Privilege Escalation 
- Persistence 
- Data Exfiltration: During the `Information Gathering` and `Pillaging` stage, we will often be able to find, among other things, considerable personal information and customer data. Some clients will want to check whether it is possible to exfiltrate these types of data. This means we try to transfer this information from the target system to our own.


### Lateral movement

In this stage, we want to test how far we can move manually in the entire network and what vulnerabilities we can find from the internal perspective that might be exploited. In doing so, we will again run through several phases:

1.  Pivoting
2.  Evasive Testing: There are many ways to protect against lateral movement, including network (micro) `segmentation`, `threat monitoring`, `IPS`/`IDS`, `EDR`, etc. To bypass these efficiently, we need to understand how they work and what they respond to. Then we can adapt and apply methods and strategies that help avoid detection.
3.  Information Gathering
4.  Vulnerability Assessment
5.  (Privilege) Exploitation
6.  Post-Exploitation


###  Proof-Of-Concept

`Proof of Concept` (`PoC`) or `Proof of Principle` is a project management term. In project management, it serves as proof that a project is feasible in principle.

A `PoC` can have many different representations. For example, `documentation` of the vulnerabilities found can also constitute a PoC. The more practical version of a PoC is a `script` or `code` that automatically exploits the vulnerabilities found. This demonstrates the flawless exploitation of the vulnerabilities. This variant is straightforward for an administrator or developer because they can see what steps our script takes to exploit the vulnerability.

### Post-Engagement

#### Cleanup

**Cleanup**: Once testing is complete, we should perform any necessary cleanup, such as deleting tools/scripts uploaded to target systems, reverting any (minor) configuration changes we may have made, etc. We should have detailed notes of all of our activities, making any cleanup activities easy and efficient. 

#### Reporting

**Documentation and Reporting**: Before completing the assessment and disconnecting from the client's internal network or sending "stop" notification emails to signal the end of testing, we must make sure to have adequate documentation for all findings that we plan to include in our report. This includes command output, screenshots, a listing of affected hosts, and anything else specific to the client environment or finding.

Typical parts of a report:

- **Executive Summary**: The report typically begins with an executive summary, which is a high-level overview of the key findings and the overall security posture of the web application. It highlights the most critical vulnerabilities, potential risks, and the impact they may have on the business. This section is designed for management and non-technical stakeholders to provide a quick understanding of the test results.
- **Scope and Methodology**: This section provides a clear description of the scope of the penetration test, including the target application, its components, and the specific testing activities performed. It also outlines the methodologies and techniques used during the assessment to ensure transparency and understanding of the testing process.
- **Findings and Vulnerabilities**: The core of the penetration test report is the detailed findings section. Each identified vulnerability is listed, along with a comprehensive description of the issue, the steps to reproduce it, and its potential impact on the application and organization. The vulnerabilities are categorized based on their severity level (e.g., critical, high, medium, low) to prioritize remediation efforts. 
- **Proof of Concept (PoC)**: For each identified vulnerability, the penetration tester includes a proof of concept (PoC) to demonstrate its exploitability. The PoC provides concrete evidence to support the validity of the findings and helps developers understand the exact steps required to reproduce the vulnerability.
- **Risk Rating and Recommendations**: In this section, the vulnerabilities are further analyzed to determine their risk rating and potential impact on the organization. The risk rating takes into account factors such as likelihood of exploitation, ease of exploit, potential data exposure, and business impact. Additionally, specific recommendations and best practices are provided to address and mitigate each vulnerability. 
- **Remediation Plan**: The report should include a detailed remediation plan outlining the steps and actions required to fix the identified vulnerabilities. This plan helps guide the development and IT teams in prioritizing and addressing the security issues in a systematic manner.
- **Additional Recommendations**: In some cases, the report may include broader recommendations for improving the overall security posture of the web application beyond the identified vulnerabilities. These may include implementing security best practices, enhancing security controls, and conducting regular security awareness training.
- **Appendices and Technical Details**: Supporting technical details, such as HTTP requests and responses, server configurations, and logs, may be included in appendices to  provide additional context and evidence for the identified vulnerabilities.

Resources:

- [https://pentestreports.com/](https://pentestreports.com/)


####  Report Review Meeting

**Report Review Meeting**: Once the draft report is delivered, and the client has had a chance to distribute it internally and review it in-depth, it is customary to hold a report review meeting to walk through the assessment results.


#### Deliverable Acceptance

**Deliverable Acceptance**: Once the client has submitted feedback (i.e., management responses, requests for clarification/changes, additional evidence, etc.) either by email or (ideally) during a report review meeting, we can issue them a new version of the report marked `FINAL`

**Post-Remediation Testing**: Most engagements include post-remediation testing as part of the project's total cost. In this phase, we will review any documentation provided by the client showing evidence of remediation or just a list of remediated findings.

Since a penetration test is essentially an audit, we must remain impartial third parties and not perform remediation on our findings (such as fixing code, patching systems, or making configuration changes in Active Directory). After a penetration test concludes, we will have a considerable amount of client-specific data such as scan results, log output, credentials, screenshots, and more. We should retain evidence for some time after the penetration test in case questions arise about specific findings or to assist with retesting "closed" findings after the client has performed remediation activities. Any data retained after the assessment should be stored in a secure location owned and controlled by the firm and encrypted at rest.


## Anex

### Contractors Agreement

**Checklist for Physical Assessments**

|**Checkpoint**|**Contents**|
|---|---|
|`☐ Introduction`|Description of this document.|
|`☐ Contractor`|Company name, contractor full name, job title.|
|`☐ Penetration Testers`|Company name, pentesters full name.|
|`☐ Contact Information`|Mailing addresses, e-mail addresses, and phone numbers of all client parties and penetration testers.|
|`☐ Purpose`|Description of the purpose for the conducted penetration test.|
|`☐ Goals`|Description of the goals that should be achieved with the penetration test.|
|`☐ Scope`|All IPs, domain names, URLs, or CIDR ranges.|
|`☐ Lines of Communication`|Online conferences or phone calls or face-to-face meetings, or via e-mail.|
|`☐ Time Estimation`|Start and end dates.|
|`☐ Time of the Day to Test`|Times of the day to test.|
|`☐ Penetration Testing Type`|External/Internal Penetration Test/Vulnerability Assessments/Social Engineering.|
|`☐ Penetration Testing Locations`|Description of how the connection to the client network is established.|
|`☐ Methodologies`|OSSTMM, PTES, OWASP, and others.|
|`☐ Objectives / Flags`|Users, specific files, specific information, and others.|
|`☐ Evidence Handling`|Encryption, secure protocols|
|`☐ System Backups`|Configuration files, databases, and others.|
|`☐ Information Handling`|Strong data encryption|
|`☐ Incident Handling and Reporting`|Cases for contact, pentest interruptions, type of reports|
|`☐ Status Meetings`|Frequency of meetings, dates, times, included parties|
|`☐ Reporting`|Type, target readers, focus|
|`☐ Retesting`|Start and end dates|
|`☐ Disclaimers and Limitation of Liability`|System damage, data loss|
|`☐ Permission to Test`|Signed contract, contractors agreement|

### Contract Checklist

| **Checkpoint**                       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `☐ NDA`                              | Non-Disclosure Agreement (NDA) refers to a secrecy contract between the client and the contractor regarding all written or verbal information concerning an order/project. The contractor agrees to treat all confidential information brought to its attention as strictly confidential, even after the order/project is completed. Furthermore, any exceptions to confidentiality, the transferability of rights and obligations, and contractual penalties shall be stipulated in the agreement. The NDA should be signed before the kick-off meeting or at the latest during the meeting before any information is discussed in detail. |
| `☐ Goals`                            | Goals are milestones that must be achieved during the order/project. In this process, goal setting is started with the significant goals and continued with fine-grained and small ones.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `☐ Scope`                            | The individual components to be tested are discussed and defined. These may include domains, IP ranges, individual hosts, specific accounts, security systems, etc. Our customers may expect us to find out one or the other point by ourselves. However, the legal basis for testing the individual components has the highest priority here.                                                                                                                                                                                                                                                                                              |
| `☐ Penetration Testing Type`         | When choosing the type of penetration test, we present the individual options and explain the advantages and disadvantages. Since we already know the goals and scope of our customers, we can and should also make a recommendation on what we advise and justify our recommendation accordingly. Which type is used in the end is the client's decision.                                                                                                                                                                                                                                                                                  |
| `☐ Methodologies`                    | Examples: OSSTMM, OWASP, automated and manual unauthenticated analysis of the internal and external network components, vulnerability assessments of network components and web applications, vulnerability threat vectorization, verification and exploitation, and exploit development to facilitate evasion techniques.                                                                                                                                                                                                                                                                                                                  |
| `☐ Penetration Testing Locations`    | External: Remote (via secure VPN) and/or Internal: Internal or Remote (via secure VPN)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `☐ Time Estimation`                  | For the time estimation, we need the start and the end date for the penetration test. This gives us a precise time window to perform the test and helps us plan our procedure. It is also vital to explicitly ask how time windows the individual attacks (Exploitation / Post-Exploitation / Lateral Movement) are to be carried out. These can be carried out during or outside regular working hours. When testing outside regular working hours, the focus is more on the security solutions and systems that should withstand our attacks.                                                                                             |
| `☐ Third Parties`                    | For the third parties, it must be determined via which third-party providers our customer obtains services. These can be cloud providers, ISPs, and other hosting providers. Our client must obtain written consent from these providers describing that they agree and are aware that certain parts of their service will be subject to a simulated hacking attack. It is also highly advisable to require the contractor to forward the third-party permission sent to us so that we have actual confirmation that this permission has indeed been obtained.                                                                              |
| `☐ Evasive Testing`                  | Evasive testing is the test of evading and passing security traffic and security systems in the customer's infrastructure. We look for techniques that allow us to find out information about the internal components and attack them. It depends on whether our contractor wants us to use such techniques or not.                                                                                                                                                                                                                                                                                                                         |
| `☐ Risks`                            | We must also inform our client about the risks involved in the tests and the possible consequences. Based on the risks and their potential severity, we can then set the limitations together and take certain precautions.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `☐ Scope Limitations & Restrictions` | It is also essential to determine which servers, workstations, or other network components are essential for the client's proper functioning and its customers. We will have to avoid these and must not influence them any further, as this could lead to critical technical errors that could also affect our client's customers in production.                                                                                                                                                                                                                                                                                           |
| `☐ Information Handling`             | HIPAA, PCI, HITRUST, FISMA/NIST, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `☐ Contact Information`              | For the contact information, we need to create a list of each person's name, title, job title, e-mail address, phone number, office phone number, and an escalation priority order.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `☐ Lines of Communication`           | It should also be documented which communication channels are used to exchange information between the customer and us. This may involve e-mail correspondence, telephone calls, or personal meetings.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `☐ Reporting`                        | Apart from the report's structure, any customer-specific requirements the report should contain are also discussed. In addition, we clarify how the reporting is to take place and whether a presentation of the results is desired.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `☐ Payment Terms`                    | Finally, prices and the terms of payment are explained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Rules of Engagement 

**Checklist**

|**Checkpoint**|**Contents**|
|---|---|
|`☐ Introduction`|Description of this document.|
|`☐ Contractor`|Company name, contractor full name, job title.|
|`☐ Penetration Testers`|Company name, pentesters full name.|
|`☐ Contact Information`|Mailing addresses, e-mail addresses, and phone numbers of all client parties and penetration testers.|
|`☐ Purpose`|Description of the purpose for the conducted penetration test.|
|`☐ Goals`|Description of the goals that should be achieved with the penetration test.|
|`☐ Scope`|All IPs, domain names, URLs, or CIDR ranges.|
|`☐ Lines of Communication`|Online conferences or phone calls or face-to-face meetings, or via e-mail.|
|`☐ Time Estimation`|Start and end dates.|
|`☐ Time of the Day to Test`|Times of the day to test.|
|`☐ Penetration Testing Type`|External/Internal Penetration Test/Vulnerability Assessments/Social Engineering.|
|`☐ Penetration Testing Locations`|Description of how the connection to the client network is established.|
|`☐ Methodologies`|OSSTMM, PTES, OWASP, and others.|
|`☐ Objectives / Flags`|Users, specific files, specific information, and others.|
|`☐ Evidence Handling`|Encryption, secure protocols|
|`☐ System Backups`|Configuration files, databases, and others.|
|`☐ Information Handling`|Strong data encryption|
|`☐ Incident Handling and Reporting`|Cases for contact, pentest interruptions, type of reports|
|`☐ Status Meetings`|Frequency of meetings, dates, times, included parties|
|`☐ Reporting`|Type, target readers, focus|
|`☐ Retesting`|Start and end dates|
|`☐ Disclaimers and Limitation of Liability`|System damage, data loss|
|`☐ Permission to Test`|Signed contract, contractors agreement|
