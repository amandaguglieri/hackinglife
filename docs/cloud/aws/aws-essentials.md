

# Amazon Web Services (AWS) Essentials


## AWS Compute

### Elastic Computer Cloud (EC2)

An EC2 instance is a Virtual Server running on AWS. You deploy your EC2 instances into a virtual private cloud or VPC. You can deploy them into public or private subnets.

Public subnets have a public IP address and can be accessed from the Internet. Private subnets are isolated. They can only communicate with each other within the VPC (unless you install a gateway).


## AWS Storage

### Amazon Elastic Block Store (EBS)

Block Storage Device, it's a virtual hard drive in the cloud. The OS reads/writes at the block level. Disks can be internal, or Network attached. The OS sees volumes that can be partitioned and formatted. Use cases:

- Use by Amazon EC2 instances.
- Relational and non-relational databases.
- Enterprises applications.
- Containerized applications.
- Big data analytics.
- File systems.

### Amazon Elastic File System (EFS)

It uses File Storage, in which a filesystem is mounted to the OS using a network share. A filesystem can be shared by many users. Use cases:

- Corporate home directories.
- Corporate shared directories.
- Big data analytics.
- Lift & Shift enterprise applications.
- Web serving.
- Content management.

### Amazon Simple Storage Services (S3)

It uses Object Storage Containers. They are usually on-premises. There is no hierarchy of objects in the container.  It uses REST API. Use cases:

- Websites.
- Mobile applications.
- Backup and archiving.
- IoT devices.
- Big data analytics.

As benefits, it has very low-cost object storage, a high durability and multiple storage classes. 

In S3 you have  buckets. A bucket is a container into which you put your objects. You can have those objects inside your bucket public or private to the Internet.




