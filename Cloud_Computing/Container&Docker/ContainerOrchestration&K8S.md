# Container Orchestration

Everyone’s container journey starts with one container. At first the growth is easy to handle, but soon you have many applications, many instances… And that is why we have Container orchestration.

![](assets/Container_orchestration.png)

## Container Orchestration Functionality

* Scheduling

* Cluster Management

* Service Discovery

* Provisoning

* Monitoring

* Configuration Management

  ![container_orchestration_functionality.png](assets/container_orchestration_functionality.png)

## Container ecosystem layers

![container_ecosystem_layers.png](assets/container_ecosystem_layers.png)

## What is container orchestration?

* Container orchestration
  * Manages the deployment, placement, and lifecycle of workload containers

* Cluster management
  * Federates multiple hosts into one target

* Scheduling
  * Distributes containers across nodes

* Service discovery
  * Knows where the containers are located
  * Distributes client requests across the containers

* Replication
  * Ensures the right number of nodes and containers

* Health management
  * Replaces unhealthy containers and nodes

![](assets/container_orchestration_2.png)

# Kubernetes

## What is Kubernetes?

* **Container orchestrator**
  * Runs and manages containers
  * Unified API for deploying web applications, batch jobs, and databases
  * Maintains and tracks the global view of the cluster 
  * Supports multiple cloud and bare-metal environments

* **Manage applications, not machines**
  * Rolling updates, canary deploys, and blue-green deployments 

* **Designed for extensibility**
  * Rich ecosystem of plug-ins for scheduling, storage, networking

* **Open source project managed by the Linux Foundation**
  * Inspired and informed by Google's experiences and internal systems
  * 100% open source, written in Go

### Kubernetes Strengths

* **Kubernetes has a clear governance model** managed by the Linux Foundation. Google is actively driving the product features and roadmap, while allowing the rest of the ecosystem to participate. 

* **A growing and vibrant Kubernetes ecosystem** provides confidence to enterprises about its long-term viability.  IBM, Huawei, Intel, and Red Hat are some of the companies making prominent contributions to the project. 

* **The commercial viability of Kubernetes makes it an interesting choice for vendors.**  We expect to see new offerings announced over the next several months. 

* **Despite the expected growth in commercial distributions, Kubernetes avoids dependency and vendor lock-in** through active community participation and ecosystem support. 

* **Kubernetes supports a wide range of deployment options.** Customers can choose between bare metal, virtualization, private, public, and hybrid cloud deployments. It enjoys a wide range of delivery models across on-premises and cloud-based services. 

* **The design of Kubernetes is more operations-centric** than developer-orientated, which makes it the first choice of DevOps teams.

### Kubernetes Certified Service Providers(KCSP)
The KCSP program is a vetted tier of service providers who have deep experience helping enterprises successfully adopt Kubernetes. KCSP partners offer Kubernetes support, consulting, professional services and training for organizations embarking on their Kubernetes journey.

* KCSP is managed by the Cloud Native Computing Foundation

* IBM is a KCSP Partner
  * IBM Container Service is a managed k8s environment with built-in cluster security and isolation while leveraging services including Waston, IoT, Weather, etc.

### Kubernets featurea

* Intelligent Scheduling
* Self-healing
* Horizontal scaling
* Service discovery & load balancing
* Automated rollouts and rollbacks
* Secret and configuration management

## Architecture Overview

Kubernetes Cluster Architecture 

![](assets/architecture_cluster.png)

* **Master node**
  * Node that manages the cluster
  * Scheduling, replication & control
  * Multiple nodes for HA

* **Worker nodes**
  * Node where pods are run
  * Docker engine
  * kubelet agent accepts & executes commands from the master to manage pods
  * cAdvisor – Container Advisor provides resource usage and performance statistics
  * kube-proxy – routes inbound or ingress traffic

  ### Master Node Components

  **Etcd**

  –A highly-available key value store

  –All cluster data is stored here

  **API Server**

  –Exposes API for managing Kubernetes

  –Used by kubectrl CLI

  **Controller manager**

  –Daemon that runs controllers, which are the background threads that handle routine tasks in the cluster

  –Node Controller – Responsible for noticing and responding when nodes go down

  –Replication Controller – Replaced by ReplicaSet

  –Endpoints Controller – Populates the Endpoints object (that is, joins services and pods)

  –Service Account & Token Controllers – Create default accounts and API access tokens for new namespaces

  **Scheduler**

  –Selects the worker node each pods runs in

## Kubernetes Concepts

### Pods

A group of co-located containers

* Smallest deployment unit – runs containers

* Each pod has its own IP

* Shares a PID namespace, network, and hostname

### Services

A service defines a set of pods and a means by which to access them, such as single stable IP address and corresponding DNS name.

* Collection of pods exposed as an endpoint
  * state and networking info propagated to all worker nodes

* Types of service exposure
  * ClusterIP – Exposes cluster-internal IP
  * NodePort – Exposes the service on each Node’s IP at a static port
  * LoadBalancer – Exposes externally using a cloud provider’s load balancer
  * ExternalName – Maps to an external name (such as foo.bar.example.com)

  ![](assets/services.png)

### Volumes

A volume is a directory, possibly with some data in it, which is accessible to a Container as part of

its  filesystem.

### Labels

A label is a key/value pair that is attached to a resource, such as a pod, to convey a user-defined

identifying attribute.

### Replication Controller

A replication controller ensures that a specified number of pod replicas are running at any one time.

### Kubernetes StatefulSet

A StatefulSet is a Controller that provides a unique identity to its Pods. It provides guarantees about the ordering of deployment and scaling.

## Security

## Networking
## Core Objects and API

## Storage

# Resources

Kubernetes tutorial –https://kubernetes.io/docs/tutorials/kubernetes-basics/

Introduction to container orchestration –https://www.exoscale.ch/syslog/2016/07/26/container-orch/

 TNS Research: The Present State of Container Orchestration –https://thenewstack.io/tns-research-present-state-container-orchestration/

Large-scale cluster management at Google with Borg –https://research.google.com/pubs/pub43438.html