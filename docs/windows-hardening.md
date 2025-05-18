


## Secure Clean OS Installation

You can find copies of Windows Operating systems [here](https://www.microsoft.com/en-us/software-download/) or pull them using the Microsoft Media Creation Tool.

## Updates and Patching

[Microsoft's Update Orchestrator](https://docs.microsoft.com/en-us/windows/deployment/update/how-windows-update-works) will run updates for you in the background based on your configured settings. For most, this means it will download and install the most recent updates for you behind the scenes.

1. Windows Update Orchestrator will check in with the Microsoft Update servers or your own WSUS server to find new updates needed.
    - This will happen at random intervals so that your hosts don't flood the update server with requests all at once.
    - The Orchestrator will then check that list against your host configuration to pull the appropriate updates.
2. Once the Orchestrator decides on applicable updates, it will kick off the downloads in the background.
    - The updates are stored in the temp folder for access. The manifests for each download are checked, and only the files needed to apply it are pulled.
3. Update Orchestrator will then call the installer agent and pass it the necessary action list.
4. From here, the installer agent applies the updates.
    - Note that updates are not yet finalized.
5. Once updates are done, Orchestrator will finalize them with a reboot of the host.
    - This ensures any modification to services or critical settings takes effect.


These actions can be managed by [Windows Server Update Services](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus), `WSUS` or through Group Policy.


## Configuration Management

In Windows, configuration management can easily be achieved through the use of Group Policy.

This can be achieved by using the Group Policy Management Console (GPMC) or via Powershell.


## User Management

- Limiting the number of user and admin accounts on each system and ensuring that login attempts (valid/invalid) are logged and monitored can go a long way for system hardening and monitoring potential problems.
- It is also good to enforce a strong password policy and two-factor authentication, rotate passwords periodically and restrict users from reusing old passwords by using the `Password Policy` settings in Group Policy.

>These settings can be found using GPMC in the path `Computer Configuration\Windows Settings\Security Settings\Account Policies\Password Policy`.


- We should also check that users are not placed into groups that give them excessive rights unnecessary for their day-to-day tasks (a regular user having Domain Admin rights, for example) and enforce login restrictions for administrator accounts.
- Two Factor Authentication can help prevent fraudulent logins as well.


## Audit

Perform periodic security and configuration checks of all systems.

There are several security baselines such as the DISA [Security Technical Implementation Guides (STIGs)](https://public.cyber.mil/stigs/) or Microsoft's [Security Compliance Toolkit](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-configuration-framework/security-compliance-toolkit-10) that can be followed to set a standard for security in your environment.

## Logging

[Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) is a tool built by Microsoft and included in the Sysinternals Suite that enhances the logging and event collection capability in Windows.

Any logs Sysmon writes will be stored in the hive: `Applications and Service Logs\Microsoft\Windows\Sysmon\Operational`. You can view these by utilizing the event viewer application and drilling into the hive.

## Network and Host Logs

Tools like [PacketBeat](https://www.elastic.co/beats/packetbeat), IDS\IPS implementations such as Security Onion sensors, and other network monitoring solutions can help complete the picture for your administrators. They collect and ship network traffic logs to your monitoring solutions and SIEMS.


## Key Hardening Measures

This is by no means an exhaustive list, but some simple hardening measures are:

- Secure boot and disk encryption with BitLocker should be enabled and in use.
- Audit writable files and directories and any binaries with the ability to launch other apps.
- Ensure that any scheduled tasks and scripts running with elevated privileges specify any binaries or executables using the absolute path.
- Do not store credentials in cleartext in world-readable files on the host or in shared drives.
- Clean up home directories and PowerShell history.
- Ensure that low-privileged users cannot modify any custom libraries called by programs.
- Remove any unnecessary packages and services that potentially increase the attack surface.
- Utilize the Device Guard and Credential Guard features built-in by Microsoft to Windows 10 and most new Server Operating Systems.
- Utilize Group Policy to enforce any configuration changes needed to company systems.

