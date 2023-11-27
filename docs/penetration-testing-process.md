---
title: Pentesting Notes
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - pentesting
  - CPTS
---

# Penetration Testing Process: A General Approach to the Profession



## Phases

### Pre-engagement

| **Document** | **Timing for Creation** |
| ----------- | ---------------------- |
| Non-Disclosure Agreement (NDA) | After Initial Contact  | 
|  Scoping Questionnaire | Before the Pre-Engagement Meeting | 
| Scoping Document  | During the Pre-Engagement Meeting | 
| Penetration Testing Proposal (Contract/Scope of Work (SoW)) | During the Pre-engagement Meeting | 
| Rules of Engagement (RoE) |  Before the Kick-Off Meeting | 
| Contractors Agreement (Physical Assessments) | Before the Kick-Off Meeting |
|  Reports | During and after the conducted Penetration Test | 


### Information gathering

We could tell 4 categories:

-   Open-Source Intelligence
-   Infrastructure Enumeration
-   Service Enumeration
-   Host Enumeration

A different way to approach to footprinting is considering the following layers:

|**Layer**|**Description**|**Information Categories**|
|---|---|---|
|`1. Internet Presence`|Identification of internet presence and externally accessible infrastructure.|Domains, Subdomains, vHosts, ASN, Netblocks, IP Addresses, Cloud Instances, Security Measures|
|`2. Gateway`|Identify the possible security measures to protect the company's external and internal infrastructure.|Firewalls, DMZ, IPS/IDS, EDR, Proxies, NAC, Network Segmentation, VPN, Cloudflare|
|`3. Accessible Services`|Identify accessible interfaces and services that are hosted externally or internally.|Service Type, Functionality, Configuration, Port, Version, Interface|
|`4. Processes`|Identify the internal processes, sources, and destinations associated with the services.|PID, Processed Data, Tasks, Source, Destination|
|`5. Privileges`|Identification of the internal permissions and privileges to the accessible services.|Groups, Users, Permissions, Restrictions, Environment|
|`6. OS Setup`|Identification of the internal components and systems setup.|OS Type, Patch Level, Network config, OS Environment, Configuration files, sensitive private files|


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

- Application petesters.
- Network or infraestructure pentesters.
- Physical pentesters.
- Social engineering pentesters.


Types os Security assessments:

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

**Cleanup**: Once testing is complete, we should perform any necessary cleanup, such as deleting tools/scripts uploaded to target systems, reverting any (minor) configuration changes we may have made, etc. We should have detailed notes of all of our activities, making any cleanup activities easy and efficient. 

**Documentation and Reporting**: Before completing the assessment and disconnecting from the client's internal network or sending "stop" notification emails to signal the end of testing, we must make sure to have adequate documentation for all findings that we plan to include in our report. This includes command output, screenshots, a listing of affected hosts, and anything else specific to the client environment or finding.

**Report Review Meeting**: Once the draft report is delivered, and the client has had a chance to distribute it internally and review it in-depth, it is customary to hold a report review meeting to walk through the assessment results.

**Deliverable Acceptance**: Once the client has submitted feedback (i.e., management responses, requests for clarification/changes, additional evidence, etc.) either by email or (ideally) during a report review meeting, we can issue them a new version of the report marked `FINAL`

**Post-Remediation Testing**: Most engagements include post-remediation testing as part of the project's total cost. In this phase, we will review any documentation provided by the client showing evidence of remediation or just a list of remediated findings.

Since a penetration test is essentially an audit, we must remain impartial third parties and not perform remediation on our findings (such as fixing code, patching systems, or making configuration changes in Active Directory). After a penetration test concludes, we will have a considerable amount of client-specific data such as scan results, log output, credentials, screenshots, and more. We should retain evidence for some time after the penetration test in case questions arise about specific findings or to assist with retesting "closed" findings after the client has performed remediation activities. Any data retained after the assessment should be stored in a secure location owned and controlled by the firm and encrypted at rest.