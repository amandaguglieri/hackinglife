---
title: AWS cli
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - amazon
  - s3
  - aws
---


# AWS cli

Tool to list S3 objects. S3 is an object storage service in the AWS cloud service. With S3, you can store objects in buckets. Files stored in an Amazon S3 bucket are called S3 objects.

## Installation

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Update version:
```bash
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

To access you will need access key. You generate access keys in AWS Dashboard.

```bash
aws configure  
AWS Access Key ID [None]: a  
AWS Secret Access Key [None]: a  
Default region name [None]: <region>  
Default output format [None]: text

#######################
###### Where
#######################
# - _AWS Access Key ID_ & _AWS Secret Access Key can be any random strings at least one character long,_
# - _Default region name_ can be any region from [AWS’s region list](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/),
# - _Default output format_ can be `json`, `yaml`, `yaml-stream`, `table` or `text`. As we are not expecting enormous amount of data, `text` should do just fine.
```


## Basic commands

```
# Check version
aws --version

# List IAM users (if you have permissions)
aws iam list-users --region <region>
# --region is optional


```



Uploaded the file _shell.php_ to the S3 bucket _thetoppers.htb_.

```
aws --endpoint=http://s3.thetoppers.htb s3 cp simpleshell.php s3://thetoppers.htb
```


```bash
aws [service-name] [command] [args] [--flag1] [--flag2]
```