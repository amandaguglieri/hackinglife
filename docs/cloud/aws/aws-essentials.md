---
title: Amazon Web Services (AWS) Essentials
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - aws
  - amazon web services 
  - public cloud
---


# Amazon Web Services (AWS) Essentials


## AWS Compute

### Elastic Computer Cloud (EC2)

An EC2 instance is a Virtual Server running on AWS. You deploy your EC2 instances into a virtual private cloud or VPC. You can deploy them into public or private subnets.

You can choose: OS, CPU, RAM, Storage space, network card, firewall rules (security group), and bootstrap script (configure at fisrt launch, and which is called EC2 User Data). Concept of bootstrap: bootstrapping means launching commands when a machine starts. That script is only run once, at first start. You can: install updates, software, common files from the internet,...

Public subnets have a public IP address and can be accessed from the Internet. Private subnets are isolated. They can only communicate with each other within the VPC (unless you install a gateway.

Some instance types: t2.micro, t2.xlarge, c5d.4xlarge, r516xlarge, m5.8xlarge,... t2.micro is part of the AWS free tier with up to 750 hours per month. This is the name convention for instances:

```
m5.2xlarge
# m: instance class
# 5: generation of the instance 
# 2xlarge: size within the instance class
```

There are general purpose instances, storage optimized, network optimized, or memory optimized, for instance.

The security groups only have allow rules (because the default is deny).By default, all inbound traffic is blocked and all outbound traffic is authorized. An instance can have multiple security groups. You can attach to your firewall rules security groups. 


Default user for connecting to EC2 via ssh is ec2-user. So ssh connection would be:

```bash
ssh -i access-key.pem ec2-user@<IP>
```


#### AMI

AMI stands for Amazon Machine Image and they represent a customization of an EC2 instance. It's similar to the concept of OVA in VirtualBox.

#### EC2 Image Builder

EC2 Image Builder is used to automate the creation of VM or container images. It automates the creation, maintain, validate, and test EC2 AMIs. It can be run on a schedule. It's a free service.



## AWS Storage

### Amazon Elastic Block Store (EBS)

Block Storage Device, it's a virtual hard drive in the cloud. The OS reads/writes at the block level. Disks can be internal, or Network attached. The OS sees volumes that can be partitioned and formatted. Use cases:

- Use by Amazon EC2 instances.
- Relational and non-relational databases.
- Enterprises applications.
- Containerized applications.
- Big data analytics.
- File systems.

The free tier has 30GB of free EBS storage of type General Purpose (SSD) or Magnetic per month. 

A definition for EBS would be that they are network drives (not physical drives). They use the network to communicate the instance. They can be detached from an EC2 instance and attached to another very quickly. They are locked to an Availability Zone. 

They don't need to be attached to any instance. They have also a delete on termination attribute. By default is not deleted. This feature can be triggered from [aws-cli](../../aws-cli.md).

### EBS Snapshots

It makes a backup (snapshot) of your EBS volume at a point in time. Not necessary to detach volume to do snapshot, but recommended. Snapshot are useful to replicate EBS in different regions. By copying snapshot to a different region you can migrate EBS attached to another in a different region.

There is a EBS Snapshot Archive service, that allows you to move a snapshot to an archive tier that is 75% cheaper.

Also there is a service of a Recycle Bin, that allows you to retain snapshot. You can define the retain policy for it.

### EC2 Instance Store

EBS volumes are network drives with good but limited performance. If you need a high-performance hardware disk, you have EC2 Instance Store.

EC2 Instance Store is good for buffer / cache /scratch data / and temporary content, but not long term.

### Amazon Elastic File System (EFS)

It uses File Storage, in which a filesystem is mounted to the OS using a network share. A filesystem can be shared by many users. Use cases:

- Corporate home directories.
- Corporate shared directories.
- Big data analytics.
- Lift & Shift enterprise applications.
- Web serving.
- Content management.

EFS works only with Linux EC2 instances in multi-AZ.

EFS Infrequent Access (EFS-IA) is a storage class cost-optimized for files that you don't access very often. It saves up to 92% of cost compared to EFS Standard. You can have EFS-IA integrated with a Lifecycle policy. 

### Amazon FSx 

Amazon FSx is a managed service to get third party high-performance file system on AWS. 

It's fully managed. There are 3 services:

- FSx for Lustre: High Performance Computing. For machine learning, analytics, video processing, finantial modelling...
- FSx for Windows File Server: support SMB and NTFS. Built on Windows File Server. Integrated with Windows Active Directory,
- FSx for NetApp ONTAP



### Amazon Simple Storage Services (S3)

It uses Object Storage Containers. They are usually on-premises. There is no hierarchy of objects in the container. It's used for backup and storage, along with disaster recovery, archive, media hosting, hybrid cloud storage...  It uses REST API. Use cases:

- Websites.
- Mobile applications.
- Backup and archiving.
- IoT devices.
- Big data analytics.

As benefits, it has very low-cost object storage, a high durability and multiple storage classes. 

In S3 you have  buckets. A bucket is a container into which you put your objects. You can have those objects inside your bucket public or private to the Internet. Buckets must have an unique name. They are define at the region level. 

A key is the full path to the file: s3://my-bucket/my-folder/my-file.txt It's composed by a prefix and an object name. Max object size is 5TB (5000 GB).

There are S3 Buckets Policies to allow public access. There are also IAM permissions that you can assign to users. You can also have EC Instance Role to grant access to EC2 instances. Additionally, in the Bucket settings you can block public access (this can be also set at an account level).

Cool tool: [Amazon policy generator](https://awspolicygen.s3.amazonaws.com/policygen.html)

#### Creating a static website

This would be the url: http://bucketname.s3-website-aws-region.amazonaws.com

#### Storage classes

![aws storage classes](../../img/aws_01.png)


## Amazon Network 

### Amazon Elastic Load Balancing (ELB)

A load balancer is a server that will forward  the internet traffic down to multiple servers downstream. And for then there will be EC2 instances. They're also called the backend EC2 instances.

Elastic load balancing is something that is managed by AWS. 

Benefits:

- ELB can spread the load across multiple downstream instances.
- ELB allows you to expose a single point of access, DNS host name, for your application.
- ELB can seamlessly handle the failures of downstream instances. 
- EBL can do regular health checks on them and if one of them is failing, then the load balancer will not direct traffic to that instance.
- It provides SSL termination (HTPPS) for your websites.

There are 4 kinds:
- Application Load Balancer (HTTP/HTTPs only) - Layer 7
- Network Load Balancer (ultra high performance, allows for TCP) - Layer 4
- Gateway Load Balancer - Layer 3.
- Classic Load Balancer (retired in 2023) - Layer 4 and 7.

### Auto Scaling Groups (ASG)

The goal of an auto scaling group is to scale out. That means add EC2 instances to match an increased load or scale in, that means remove EC2 instances to match a decreased load. With this we can ensure that we have, also as well, a minimum, and a maximum number of machines running at any point of time and once the auto scaling group does create, or remove EC2 instances we can make sure that these instances will be registered, or de registered into our load balancer.

You can define a minimum size, a maximum size, and a desired capacity.


## Amazon migration tools

### AWS Snow 

- Snowball Edge Storage Optimized & Snowball Edge Compute Optimized
- AWS Snowcone & Snowcone SSD
- AWS Snowmobile (the truck). 100 PB of capacity.

![aws Snow](../../img/aws_02.png)
### Edge Computing

Edge Computing is when you process data while it's being created at an edge location. You can use the Snow Family to run EC2 instances and Lambda functions to do this.


### AWS OpsHub

OpsHub which is a software that you install on your computer or laptop, so, it's not something you use on the cloud, it's something that you download on your computer. And then once it's connected, it's going to give you a graphical interface to connect to your Snow devices, and configure them and use them.


## AWS Databases

AWS has an offer of managed databases. As benefits, AWS performs quick provisioning, high availability, vertical and horizontal scaling, automated backup, and restore, operations, upgrades, patchings, monitoring, alerting...

You can always have an EC" instance and install a database server, but by using AWS managed database you won't need to configure and mantain all the features from previous paragraph. 
### Relational Database Service (Amazon RDS)

It's a relational datababase which uses SQL as a query language. 

- Postgres
- MySQL
- MAriaDB
- Oracle
- Microsoft SQL Server
- Aurora (AWS Proprietary Database).

>Note: You can NOT ssh into your instance.

#### RDS Deployments: Read Replicas, Multi-AZ

**RDS Read Replica**

- A Replica is a copy of your database. Creating one is a way to scale the read workload. Say you have an application that performs read operations on your database. If you need to scale the workload, you create Read Replica, which are copies of your RDS Database. This will allows your applications to read also from your Replicas. Therefore  you're distributing the reads to many different RDS databases.
- You can create up to  Read  Replicas. 
- Data is only written to the one only central RDS tatabase.

**Multi-AZ**

- Used for failover in case of AZ outage. In case your RDS crashes, AWS will trigger the replication in a different Availability Zone. 

**Multi-Region**

Same as Multi-AZ but for different regions. This is usually part of a disater recovery strategy or a plan to have less latency.

#### Amazon Aurora

- Aurora is a proprietary technology from AWS, not open source.
- Aurora DB supports Postgres and MySQL.
- Aurora is "AWS Cloud optimized" and claims 5x performance improvement over MySQL on RDS, over 3x the performance of Postgres on RDS.
- Aurora storage aumatically grows in increments of 10 GB, up to 128TB.
- Aurora costs more than RDS (20%more) but it's more efficient.
- Not in the free tier

RDS and Aurora are going to be the two ways for you to create relational databases on AWS. They're both managed and Aurora is going to be more cloud-native, whereas RDS is going to be running the technologies you know, directly as a managed service.

#### Amazon Aurora Serverless

Amazon Aurora Serverless is a Serverless option for Amazon Aurora where the database instantiation is going to be automated.

- Auto-scaling is provided based on actual usage of the database.
- Postgres and MySQL are supported as engines of Aurora Serverless database.
- No capacity planning needed.
- No management needed.
- Pay per second, most cost-effective. 

#### Amazon ElastiCache

- Elasticache is to get managed Redis or Memcached.
- Caches are in-memory databases with high performance, and low latency.

### DynamoDB

- Fully managed highly available with replication across 3 AZ
- NoSQL database.
- Scales to massive workloads, distributed serverless database.
- Millions of requests per seconds: low latency.
- Integrated with IAM for security, authorization and administration.
- Low cost and auto-scaling capabilities.
- Standard and Infrequent Access Table Class.

#### DynamoDB Accelerator (DAX)

- Fully managed in-memory cache for DynamoDB (for the frequently read objects).
- 10x performance improvement.
- DAX is only used for and is integrated with DynamoDB, while ElastiCache can be used for other databases.


#### DynamoDB Global Tables

It makes a DynamoDB table accesible with low latency in multiple-regions. It's a feature of DynamoDB.

### Redshift 

- It's a database on PostgresSQL, but it's not used for Online Transaction Processing (OLTP).
- Redshift is Online Analytical Processing (OLAP), used for analytics and data warehousing.
- Load data onve every hour.
- Columnar storage of data (instead of row based).
- Has a SQL interface for performing queries. 
- Massiverly Parallel Query Execution (MPP).
- Bi tools such as AWS Quicksigh or Tableau integrated in it.

It has a feature for Serverless: Redshift Serverless.

### Amazon Elastic MapReduce (EMR)

- EMR helps creating Hadoop cluster (Big Data) to analyze and process vast amount of data.
- Also supports Apache Spark, HBase, Presto, Flink.

### Amazon Athena

- Amazon Athena is a serverless query service to perform analytics againts S3 objects.
- It uses SQL language. 
- Supports CVS, JSON, ORC, Avro, and Parquet. 
- Use columnar data.

### Amazon QuickSight

Amazon QuickSight is a serverless machine learning-powered business intelligence service to create interactive dashboards.

### DocumentDB 

- If Aurora is an AWS implementation of Postgres/MySQL, DocumentDB is the same for MongoDB (which is a NoSQL database).
- MongoDB is used to store, query and index JSON.
- Fully managed database, with replication across AZ. 
- Automatically scaling.

### Amazon Neptune

Fully managed graph database.
A popular graph dataset would be a social network.
Highly available acroos 3 AZ, with up to 15 read replicas.
Can store up to billios orelations and query the graph with milliseconds of latency.

### Amazon Quantum Ledger Database (QLDB)

- A ledger is a book recording financial transactions. QLDB is going to be just to have a ledger of financial transactions.
- It's a fully managed database, it's serverless, highly available, and has replication of data across three AZ.
- Used to review history of all the changes made to your application data over time.
- Inmutable system: no entry can be removed or modified, cryptographically verifiable.
- Difference with Amazon Managed Blockchain: no decentralization component.  QLDB has a central authority component and it's a ledger, whereas managed blockchain is going to have a de-centralization component as well.

### Amazon Managed Blockchain

Managed Blockchain by Amazon is a service to join a public Blockchain networks or create your own scalable private Blockchain network within AWS. And it's compatible with two Blockchain so far, the framework Hyperledger Fabric, and the framework Ethereum.

### Amazon Glue

Glue is a managed extract, transform, and load service, or ETL. Fully serverless service.

ETL is very helpful when you have some datasets but they're not exactly in the right form, to do your analytics on them. ETL service prepares and transforms that data.

#### Glue Data Catalog

is a catalog of your datasets in your Alias infrastructure, and so this Glue Data Catalog will have a alert reference of everything, the column names, the field names, the field types, et cetera, et cetera.

### Database Migration Service (DMS)

DMS provides  quick and secure database migration into AWS that's going to be resilient and self healing.

Supports: Homogeneous migrations and heterogeneous migration.


## Amazon Compute Services

### Elastic Container Service (ECS)

It's the way to launch containers in AWS. You must provision and maintain the ingrastructure (EC2 instances). It has integrations with the Application Load Balancer.

### Fargate

It's also used to launch containers in AWS, but you don't need to provision the ingrastructure (no EC2 instances to manage).
### Elastic Container Registry (ECR)

It's a private docker registry on AWS.  The is where you store your docker images.

### Lambda

- It's a serverless compute service that allows you to run functions in the cloud.  We have virtual functions, limited by time and they will run on-demand. You pay per request and compute time. 
- Lambda is event-driven: functions get invoked by AWS when needed. 
- It supports many languages.  
- Lambda can be run as a Lambda Container Image.

Api Gateway feature can expose Lambda functions as HTTP API.

### Amazon Batch

Run batch jobs on AWS across EC2 managed instances.

## Amazon: Deployments and managing infrastructure

### AWS CloudFormation

- Infrastuture as a Service. 
- It creates the architecture and give you the diagram.
- In CloudFormation you rceate an Stack, select template (that generates a yaml), some other configurations, IAM permissions, costs. 

### Amazon Cloud Development Kit (CDK) 

It allows you to define your cloud infrastructure using a familiar language. Code is compiled into a CloudFormation template.

### Amazon Elastic Beanstalk

Elastic Beanstalk is a developer centric view of deploying an application on AWS. 

It's PaaS. 

It has a full monitoring suite. Health agent pushes metrics to CloudWatch. Check for app health, publishes health events.

### CodeDeploy

CodeDeploy deploys your application automatically.

Hybrid service because it works with ECT and On-premise severs. 

### AWS CodeCommit

It's AWS version control code repository. 

### AWS CodeBuild

It's a Code building service in the cloud. It compiles source code, run test, and produces packages that are ready to be deployed.

### AWS CodePipeline

CodePipeline orchestrate the different steps to have the code automatically pushed to production. Basis for CICD (Continuous Integration and Continuous Delivery).

### AWS CodeArtefact

It's a service used to store and retrieve all software packages dependencies to be built. It works with common dependency management tools such as maven, gradle, npm, twine, pip, nuGet.
It's an artefact management system.

### AWS CodeStar

Unified UI to easily manage software development activities in one place. It can edit the code in the cloud directly using AWS Cloud9.

### AWS Cloud9

AWS Cloud9 is a cloud IDE for writing, running and debugging code directly in the cloud.

Code collaboration in real time.


## Amazon Global Applications

### Amazon Route 53

Managed DNS by AWS. It has A, AAA, or CNAME record.

- Simple routing policy (no health checks).
- Weighted routing policy (with percentages). 
- Latency routing policies (based on lacency between users and servers).
- Failover routing policy (for disaster recovery).

### Amazon CloudFront

It's the Content Delivery Network. So far it has 216 points of presence. It has DDoS protection. Improve read performance, since content is cached at the edge.

Origins: S3 (protected with OAC Origin Access Control, that replaces OAI Origin Access Identity), Custom Origin HTTP.

Files are cached for a TTL.

### S3 Transfer Acceleration

Increase transfer speed among S3 across regions by using the AWS global network.

### AWS Global Accelerator

Improve global application availability and performance using the AWS global network.

### AWS Outpost

AWS Outposts are "server racks that offer the same AWS infrastructure, service, APIs & tools to build your own applications on-premises just as in the cloud. This allows you to extent your on-premises services to AWS. 

### AWS WaveLength 

AWS WaveLength Zones are infrastructure deployments embedded within the telecommunications providers's datacenters at the edge of 5G networks. It brings AZS services to the edge of the 5G networks. Traffic never leaves the Communication Service Provider (CSP) networks.


## Amazon Cloud integrations

### Amazon SQS

It's a simple Queue Service. Two types:

- Standard Queue is the oldest AWS offering. It's fully managed service. 
- FIFO queues. 

It allows us to decouple 

### Amazon Kinesis

It's a real time big data streaming.

### Amazon SNS

Amazon SNS stands for Simple Notification Service. It creates a set of notifications about certain events. Event publishers only sends one message to one SNS topic. Each subscriber to the topic will get all the messages.  It's a pub/sub service.

### Amazon MQ

Amazon MQ is  a managed message broker service for two technologies, for RabbitMQ and for ActiveMQ. 

SQS and SNS are cloud-native services because they are proprietary protocols from AWS. They use their own sets of APIs.

If you are running traditional application on-premises, you may use open protocols such as MQTT, AMQP, STOMP, Openwire, WSS. And when you're migrating your application to the cloud, you may not want to re-engineer your application to use the SQS and the SNS protocols or APIs. So instead, you wanna use the traditional protocols you used to, such as MQTT, AMQP, and so on. And  for this, we can use Amazon MQ.


## Amazon Cloud Monitoring


