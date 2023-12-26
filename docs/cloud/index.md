---
title: Pentesting cloud
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud pentesting
---


# Pentesting cloud

## Basics about cloud

There are many "clouds". But these three cloud providers are the big three players in the market:

- Azure: [Fundamentals](azure/az-900-preparation.md) | [Security Engineer Level](azure/az-500-preparation.md).
- Amazon Web Service (AWS): [AWS essentials](aws/aws-essentials.md)
- Google Cloud: [GCP essentials](gcp/gcp-essentials.md)

## Cloud services matrix

|   | Azure | AWS | GCP |
| -- | -- | -- | -- | 
| Available Regions | [Azure Regions](azure/az-900-preparation.md#azure-region) | AWS Regions and Zones | [Google Compute Regions & Zones](gcp/gcp-essentials.md#basic-numbers) |
| Compute Services | [Virtual Machines](azure/az-900-preparation.md#1-azure-virtual-machines) | [Elastic Compute Cloud (EC2)](aws/aws-essentials.md#elastic-computer-cloud-ec2) | [Compute Engine](gcp/gcp-essentials.md#22-compute-engine-gce) |
| App Hosting |[Azure App Service](azure/az-900-preparation.md#6-azure-app-service) | [Amazon Elastic Beanstalk](aws/aws-essentials.md#amazon-elastic-beanstalk) | [Google App Engine](gcp/gcp-essentials.md#21-app-engine) |
| Serverless Computing | [Azure Functions](azure/az-900-preparation.md#4-azure-functions-serverless-computing) | [AWS Lambda](aws/aws-essentials.md#lambda) |  [Google Cloud Functions](gcp/gcp-essentials.md#24-cloud-functions) |
| Container Support | [Azure Container Service](azure/az-900-preparation.md#3-azure-container-instances) | [EC2 Container Service](aws/aws-essentials.md#elastic-container-service-ecs)  | [Google Computer Engine (GCE)](gcp/gcp-essentials.md#22-compute-engine-gce)  |
| Scaling Options | Azure Autoscale |  Auto Scaling | Autoscaler |
| Object Storage | [Azure Blob Storage](azure/az-900-preparation.md#azure-blobs) | [Amazon Simple Storage (S3)](aws/aws-essentials.md#amazon-simple-storage-services-s3) | [Google Cloud Storage](gcp/gcp-essentials.md#31-google-cloud-storage) |
| Block Storage | [Azure Disks](azure/az-900-preparation.md#azure-disks) | [Amazon Elastic Block Store](aws/aws-essentials.md#amazon-elastic-block-store-ebs) | [Persistent Disk](gcp/gcp-essentials.md#32-persistent-disks) |
| Content Delivery Network (CDN) | Azure CDN | [Amazon CloudFront](aws/aws-essentials.md#amazon-cloudfront) | Cloud CDN |
| SQL Database Options | [Azure SQL Database](azure/az-900-preparation.md#azure-sql-database) | [Amazon RDS](aws/aws-essentials.md#relational-database-service-amazon-rds) | [Google Cloud SQL](gcp/gcp-essentials.md#61-google-cloud-sql) |
| NoSQL Database Options | [Azure CosmosDB](azure/az-900-preparation.md#cosmos-db) | [AWS DynamoDB](aws/aws-essentials.md#dynamodb) | [Google Cloud Bigtable](gcp/gcp-essentials.md#62-google-clod-bigtable) |
| Virtual Network | [Azure Virtual Network](azure/az-900-preparation.md#7-azure-virtual-networking) | Amazon VPC | Cloud Virtual Network |
| Private Connectivity | [Azure ExpressRoute](azure/az-900-preparation.md#9-azure-expressroute) | AWS Direct Connect | [Cloud Interconnect](gcp/gcp-essentials.md#43-hybrid-connectivity) |
| DNS Services | [Azure DNS](azure/az-900-preparation.md#10-azure-dns) | [Amazon Route S3](aws/aws-essentials.md#amazon-route-53) | Cloud DNS |
| Log Monitoring | [Azure Log Analytics](azure/az-900-preparation.md#azure-log-analytics) | Amazon CloudTrail | Cloud Logging |
| Performance Monitoring | [Azure Application Insights](azure/az-900-preparation.md#application-insights) | Amazon CloudWatch | Stackdriver Monitoring |
| Administration and Security | Azure Entra ID | AWS Identity and Access Management | [Cloud Identity and Access Management](gcp/gcp-essentials.md#5-identity-access-management) |
| Compliance | Azure Trust Center | AWS CloudHSM | Google Cloud Platform Security |
| Analytics  | [Azure Monitor](azure/az-900-preparation.md#azure-monitor)  | [Amazon Kinesis](aws/aws-essentials.md#amazon-kinesis) | [Cloud Dataflow](gcp/gcp-essentials.md#72-google-cloud-dataflow) |
| Automation | Azure Automation | AWS Opsworks | Compute Engine Management |
| Management Services & Options | [Azure Resource Manager](azure/az-900-preparation.md#azure-resource-manager-arm-and-azure-arm-templates) | [Amazon Cloudformation](aws/aws-essentials.md#aws-cloudformation) | Cloud Deployment Manager |
| Notifications | Azure Notification Hub | [Amazon Simple Notification Service (SNS)](aws/aws-essentials.md#amazon-sns) | None |
| Load Balancing | Load Balancing for Azure | Elastic Load Balancing | [Load Balancer](gcp/gcp-essentials.md#41-load-balancers) |


## Pentesting cloud

- [Pentesting Azure](azure/pentesting-azure.md).
- [Pentesting AWS](aws/pentesting-aws.md).
- [Pentesting docker](containers/pentesting-docker.md).

