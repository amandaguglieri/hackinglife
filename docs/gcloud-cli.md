---
title: gcloud CLI
author: amandaguglieri
draft: false
TableOfContents: true
tags:
  - cloud
  - google cloud platform
  - gcp
---

# gcloud CLI



```
# Get a list of images 
gcloud compute images list 


# PROJECT=<PROJECT> # Replace this with your project id 
# ZONE=<zone>   # Replace this with a GCP zone of your choice 

# Launch a GCE instance 
gcloud compute instances create gcp-lab1 \ 
 --project=$PROJECT \ 
 --zone=$ZONE \ 
 --machine-type=f1-micro \ 
 --tags=http-server \ 
 --image=ubuntu-1804-bionic-v20190722a \ 
 --image-project=ubuntu-os-cloud 

# Get a list of instances
gcloud compute instances list

# Filter instances by zone 
gcloud compute instances list --zone=<zone>



# SSH into the VM. This commands create the pair of keys and all ssh infrastructure needed for the connection
gcloud compute ssh <instance> --zone=<zone-of-instance> 
 
 
# Open port 80 for HTTP access 
gcloud compute firewall-rules create default-allow-http \ 
 --project=$PROJECT \ 
 --direction=INGRESS \ 
 --action=ALLOW \ 
 --rules=tcp:80 \ 
 --source-ranges=0.0.0.0/0 \ 
 --target-tags=http-server 

 
# Run these commands within the VM 
sudo apt-get install -y apache2 
sudo systemctl start apache2 
 
 
# Access Apache through the public IP 
# Terminate the instance 
gcloud compute instances delete gcp-lab1 --zone $ZONE 


# Connect to Google Cloud SQL
gcloud sql connect <nameOfDatabase>

 
 ```



### Add an image to GCP Container Registry

In GCP Dashboard go yo Container Registry. First time it will be empty. 

```bash
# Run the below commands in Google Cloud Shell 
 
gcloud services enable containerregistry.googleapis.com 
 
export PROJECT_ID=<PROJECT ID> # Replace this with your GCP Project ID 
 
docker pull busybox 
docker images 
```

``` 
cat <<EOF >>Dockerfile 
from busybox:latest 
CMD ["date"] 
EOF 
```

``` 
# Build your own instance of busybox and name it mybusybox
docker build . -t mybusybox 

# Tag your image with the convention stated by GCP
docker tag mybusybox gcr.io/$PROJECT_ID/mybusybox:latest 
# When listing images with docker images, you will see it renamed.

# Run your image
docker run gcr.io/$PROJECT_ID/mybusybox:latest 
```

```
# Associate gcp credentials with docker CLI  
gcloud auth configure-docker 

# Take our mybusybox image available in the environment and pushes it to the Container Registry.
docker push gcr.io/$PROJECT_ID/mybusybox:latest 
```


###  Demo of Anthos

```bash
# Run the below commands in the macOS Terminal 
 
export PROJECT_ID=<PROJECT ID> # Replace this with your GCP project ID 
export REGION=<REGION ID> # Replace this with a valid GCP region 
 
gcloud config set project $PROJECT_ID 
gcloud config set compute/region $REGION 
 
# Enable APIs 
gcloud services enable \ 
 container.googleapis.com \ 
 gkeconnect.googleapis.com \ 
 gkehub.googleapis.com \ 
 cloudresourcemanager.googleapis.com 
 
# Launch GKE Cluster 
gcloud container clusters create cloud-cluster \ 
    --machine-type=n1-standard-1 \ 
    --num-nodes=1 
 
# Launch Minikube. Refer to the docs at https://minikube.sigs.k8s.io/docs/  
minikube start 
 
# Create GCP Service Account 
gcloud iam service-accounts create anthos-hub 

# Add IAM Role to Service Account 
gcloud projects add-iam-policy-binding $PROJECT_ID \ 
 --member="serviceAccount:anthos-hub@$PROJECT_ID.iam.gserviceaccount.com" \ 
 --role="roles/gkehub.connect" 
 
# Download the Service Account JSON Key 
gcloud iam service-accounts keys create "./anthos-hub-svc.json" \ 
  --iam-account="anthos-hub@$PROJECT_ID.iam.gserviceaccount.com" \ 
  --project=$PROJECT_ID 
 
# Register cluster with Anthos 
URI='gcloud container clusters list --filter='name=cloud-cluster' --uri'
 
gcloud container hub memberships register cloud-cluster \ 
        --gke-uri=$URI \ 
        --service-account-key-file=./anthos-hub-svc.json 
 
# List Membership 
gcloud container hub memberships list 
 
# Register Minikube with Anthos 
gcloud container hub memberships register local-cluster \ 
 --service-account-key-file=./anthos-hub-svc.json \ 
 --kubeconfig=~/.kube/config \ 
 --context=minikube 
 
# List Membership 
gcloud container hub memberships list 

# Create Kubernetes Role 
 
kubectl config use-context minikube 
```

``` 
cat <<EOF > cloud-console-reader.yaml 
kind: ClusterRole 
apiVersion: rbac.authorization.k8s.io/v1 
metadata: 
  name: cloud-console-reader 
rules: 
- apiGroups: [""] 
  resources: ["nodes", "persistentvolumes"] 
  verbs: ["get", "list", "watch"] 
- apiGroups: ["storage.k8s.io"] 
  resources: ["storageclasses"] 
  verbs: ["get", "list", "watch"] 
EOF 
```

```
kubectl apply -f cloud-console-reader.yaml 
 
# Create RoleBinding 
kubectl create serviceaccount local-cluster 
 
kubectl create clusterrolebinding local-cluster-anthos-view \ 
 --clusterrole view \ 
 --serviceaccount default:local-cluster 
 
kubectl create clusterrolebinding cloud-console-reader-binding \ 
 --clusterrole cloud-console-reader \ 
 --serviceaccount default:local-cluster 

# Get the Token 
SECRET_NAME=$(kubectl get serviceaccount local-cluster -o jsonpath='{$.secrets[0].name}') 
 
# Copy the secret and paste it in the console 
kubectl get secret ${SECRET_NAME} -o jsonpath='{$.data.token}' | base64 --decode  
 
# Delete Membership 
gcloud container hub memberships delete cloud-cluster 
gcloud container hub memberships delete local-cluster 
  
# Clean up  
gcloud container clusters delete cloud-cluster --project=${PROJECT_ID} 
gcloud iam service-accounts delete anthos-hub@${PROJECT_ID}.iam.gserviceaccount.com 
minikube delete 

```