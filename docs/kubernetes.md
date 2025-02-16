---
title: Kubernetes
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - kubernetes
  - containers
---
# Kubernetes

[See Pentesting Kubernetes](pentesting-kubernetes.md).

## **1. Introduction to Kubernetes**

Kubernetes, also known as K8s, is an open-source container orchestration platform that has transformed the deployment and management of applications. Originally developed by Google, Kubernetes leverages over a decade of experience in handling large-scale workloads and has since been donated to the Cloud Native Computing Foundation (CNCF), becoming the industry standard for managing containerized applications.

By automating deployment, scaling, and operations of application containers across clusters of machines, Kubernetes provides a highly resilient and scalable infrastructure that supports microservices architectures, cloud-native development, and hybrid cloud environments.

## **2. Core Concepts and Architecture**

Kubernetes follows a **master-worker architecture**, comprising two main sets of components:

### **A. Control Plane (Master Node)**

The Control Plane is responsible for managing the entire Kubernetes cluster. It ensures that workloads run as expected by scheduling, monitoring, and controlling their lifecycle.

#### **Control Plane Components:**

1. **API Server (kube-apiserver):** The main entry point for all Kubernetes management commands and external interactions. It exposes the Kubernetes API and processes RESTful requests.
2. **Scheduler (kube-scheduler):** Determines which worker node should run a newly created pod based on resource availability and constraints.
3. **Controller Manager (kube-controller-manager):** Ensures the cluster's desired state is maintained by monitoring objects and taking corrective actions when necessary.
4. **etcd:** A distributed key-value store that persists cluster state, configuration, and metadata.
5. **Kubelet API (port 10250):** The interface for interacting with worker nodes and managing pods.

### **B. Worker Nodes (Minions/Instances)**

Worker nodes execute the actual application workloads and run containerized applications.

#### **Worker Node Components:**

6. **Kubelet:** The primary agent on each worker node that ensures pods are running as expected and communicates with the API server.
7. **Container Runtime:** The software that runs containers. Popular options include Docker and containerd.
8. **Kube Proxy:** Maintains network rules to enable communication between pods and services within the cluster.

## **3. Kubernetes Object Model**

Kubernetes organizes workloads using a layered model:

9. **Pod:** The smallest deployable unit in Kubernetes, consisting of one or more containers that share storage and networking.
10. **Node:** A single machine (physical or virtual) that runs pods.
11. **Cluster:** A collection of worker nodes managed by the control plane.
12. **Service:** A stable abstraction that provides network access to a set of pods.
13. **Namespace:** A mechanism for logically partitioning resources within a cluster.
14. **Deployment:** A higher-level abstraction that defines how many replicas of a pod should run and manages rolling updates.

## **4. Kubernetes API and Security Measures**

The core of Kubernetes architecture is its API, which serves as the main point of contact for all internal and external interactions.  The kube-apiserver is responsible for hosting the API, which handles and verifies RESTful requests for modifying the system's state. These requests can involve creating, modifying, deleting, and retrieving information related to various resources within the system. Overall, the Kubernetes API plays a crucial role in facilitating seamless communication and control within the Kubernetes cluster.


Within the Kubernetes framework, an API resource serves as an endpoint that houses a specific collection of API objects. These objects pertain to a particular category and include essential elements such as Pods, Services, and Deployments, among others.


| **Request** | **Description**                                                |
| ----------- | -------------------------------------------------------------- |
| `GET`       | Retrieves information about a resource or a list of resources. |
| `POST`      | Creates a new resource.                                        |
| `PUT`       | Updates an existing resource.                                  |
| `PATCH`     | Applies partial updates to a resource.                         |
| `DELETE`    | Removes a resource.                                            |


### **A. API Interaction and Access Control**

Kubernetes enforces authentication and authorization through multiple mechanisms:

- **Authentication:** Supports methods such as client certificates, bearer tokens, and OIDC.
- **Authorization:** Uses **Role-Based Access Control (RBAC)** to define user permissions.
- **Admission Controllers:** Validate and modify requests before they reach the API server.

### **B. Kubernetes Security Layers**

Security in Kubernetes is divided into different domains:

15. **Cluster Infrastructure Security:** Ensuring the underlying nodes and network are protected.
16. **Cluster Configuration Security:** Managing RBAC policies, API access, and network policies.
17. **Application Security:** Implementing container security best practices.
18. **Data Security:** Ensuring encrypted communication and storage mechanisms.

## **5. Kubernetes Networking and Communication**

Networking in Kubernetes follows a flat model, allowing pods to communicate across nodes without requiring manual configuration. Kubernetes provides multiple networking models:

- **Cluster Networking:** Enables communication between pods.
- **Service Networking:** Provides stable endpoints to expose workloads.
- **Ingress Controller:** Manages external access to services using HTTP/HTTPS.

## **6. Comparing Kubernetes and Docker**

While Docker is primarily a containerization platform, Kubernetes serves as a container orchestration system.

|Feature|Docker|Kubernetes|
|---|---|---|
|Primary Function|Containerization|Orchestration of containers|
|Scaling|Manual|Automatic scaling|
|Networking|Single network|Complex networking with policies|
|Storage|Volumes|Persistent storage solutions|
