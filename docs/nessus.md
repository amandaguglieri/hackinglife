---
title: Nessus
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - reconnaissance
  - scanner
  - vulnerability assessment
---
# Nessus

Nessus has a client and a server. We use the client to configure the scans and the server to actually perform the scanning processes and report back the result to the client.

## Installation

Download .deb from: https://www.tenable.com/downloads/nessus

```bash
sudo dpkg -i Nessus-10.3.0-debian9_amdb64.deb
service nessusd start

# Another way to start the service from an unpriviledged account is:
sudo systemctl start nessusd.service
```

Now you can go to https://localhost:8834

Once installed Nessus Esentials, register in the website to generate an API key.

## Basics

 For further information on how we can customize and configure Nessus, we can consult the [Nessus documentation](https://docs.tenable.com/nessus/Content/Settings.htm).

### Policies

Nessus gives us the option to create scan policies. Essentially these are customized scans that allow us to define specific scan options, save the policy configuration, and have them available to us under Scan Templates when creating a new scan. 

This gives us the ability to create targeted scans for any number of scenarios, such as a slower, more evasive scan, a web-focused scan, or a scan for a particular client using one or several sets of credentials.

### Plugins

Nessus works with plugins written in the [Nessus Attack Scripting Language (NASL)](https://en.wikipedia.org/wiki/Nessus_Attack_Scripting_Language) and can target new vulnerabilities and CVEs.  These plugins contain information such as the vulnerability name, impact, remediation, and a way to test for the presence of a particular issue.

To exclude false positives from scan results Under the `Resources` section, we can select `Plugin Rules`. In the new plugin rule, we input the host to be excluded, along with the Plugin ID for Microsoft DirectAccess, for instance. 

### Reports

Nessus gives us the option to export scan results in a variety of report formats as well as the option to export raw Nessus scan results to be imported into other tools, archived, or passed to tools, such as [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness). Nessus  gives the option to export scans into two formats `Nessus (scan.nessus)` or `Nessus DB (scan.db)`.  The `.nessus` file is an `.xml` file and includes a copy of the scan settings and plugin outputs. The `.db` file contains the `.nessus` file and the scan's KB, plugin Audit Trail, and any scan attachments.

Scripts such as the [nessus-report-downloader](https://raw.githubusercontent.com/eelsivart/nessus-report-downloader/master/nessus6-report-downloader.rb) can be used to quickly download scan results in all available formats from the CLI using the Nessus REST API:

```shell-session
./nessus_downloader.rb 
```


### Troubleshooting: firewall Issues

**1.** Some firewalls will cause us to receive scan results showing either all ports open or no ports open. If this happens, a quick fix is often to configure an Advanced Scan and disable the `Ping the remote host` option.

**2.** Adjust `Performance Options` and modify `Max Concurrent Checks Per Host` if the target host is often under heavy load, such as a widely used web application.

**3.** Unless specifically requested, we should never perform Denial of Service checks. The "safe checks" setting allows Nessus users to enable a set of plugins within Nessus' library of vulnerability checks which Tenable feels can have negative effects on the network, device or application being tested. 

**4.** It is also essential to keep in mind the potential impact of vulnerability scanning on a network, especially on low bandwidth or congested links. This can be measured using [vnstat](https://humdi.net/vnstat/).

```shell-session
sudo vnstat -l -i eth0
```
