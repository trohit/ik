# Intro
- Kubernetes is an open-source "Container orchestration engine" for automating deployment, scaling, and management of containerized applications.
  - Other cometing Container orchestration engines are Docker swarm and mesos.
  - Container orchestration engines are responsible for (CSS):
    - Clustering 
    - Scheduling
    - Scalability
    - Load Balancing
- Kubernetes comes from Greek, and means helmsman or ship pilot. With this analogy in mind, we can think of Kubernetes as the pilot on a ship of containers.
- Kubernetes is also referred to as k8s (pronounced Kate's), as there are 8 characters between k and s.
- Kubernetes is highly inspired by the Google Borg system, a container and workload orchestrator for its global operations for more than a decade. It is an open source project written in the Go language and licensed under the Apache License, Version 2.0.
- Kubernetes was started by Google and, with its v1.0 release in July 2015, Google donated it to the Cloud Native Computing Foundation (CNCF), one of the largest sub-foundations of the Linux Foundation.
- New Kubernetes versions are released in 4 month cycles.
- At a hi-level, Kubernetes is a cluster of compute systems categorized by their distinct roles:
  - One or more control plane nodes
  - One or more worker nodes (optional, but recommended).

 ## K8s Cmds
-  https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands


# History and Current Status
- K8s evolved from Borg, Google's own distributed workload manager.
- Currently k8s maintained by  Cloud Native Computing Foundation (CNCF), which currently hosts the Kubernetes project, along with other popular cloud-native projects, such as Prometheus, Fluentd, cri-o, containerd, Helm, Envoy, and Contour, just to name a few.

![image](https://github.com/trohit/ik/assets/466385/18371e20-0153-4e18-9911-300fc9a10331)

# Concepts
- Containers are an application-centric method to deliver high-performing, scalable applications on any infrastructure of your choice. Containers are best suited to deliver microservices by providing portable, isolated virtual environments for applications to run without interference from other running applications.
  -  container runtimes like runC, containerd, or cri-o can use pre-packaged images as a source to create and run one or more containers. These runtimes are capable of running containers on a single host, however, in practice, we would like to have a fault-tolerant and scalable solution, achieved by building a single controller/management unit, a collection of multiple hosts connected together. This controller/management unit is generally referred to as a container orchestrator.
  -  Containers encapsulate microservices and their dependencies but do not run them directly. Containers run container images.
  -  A container image bundles the application along with its runtime, libraries, and dependencies, and it represents the source of a container deployed to offer an isolated executable environment for the application. Containers can be deployed from a specific image on many platforms, such as workstations, Virtual Machines, public cloud, etc
-  Microservices are lightweight applications written in various modern programming languages, with specific dependencies, libraries and environmental requirements. To ensure that an application has everything it needs to run successfully it is packaged together with its dependencies.
- Container orchestrators are tools which group systems together to form clusters where containers' deployment and management is automated at scale.
  - Container orchestrators meet production requirements like:
    - Fault-tolerance
    - On-demand scalability
    - Optimal resource usage
    - Auto-discovery to automatically discover and communicate with each other
    - Accessibility from the outside world
    - Seamless updates/rollbacks without any downtime.
  - Examples of container orchestration tools
    - Amazon Elastic Container Service: Amazon Elastic Container Service (ECS) is a hosted service provided by Amazon Web Services (AWS) to run containers at scale on its infrastructure.
    - Azure Container Instances: Azure Container Instance (ACI) is a basic container orchestration service provided by Microsoft Azure.
    - Azure Service Fabric: Azure Service Fabric is an open source container orchestrator provided by Microsoft Azure.
    - Kubernetes: Kubernetes is an open source orchestration tool, originally started by Google, today part of the Cloud Native Computing Foundation (CNCF) project.
    - Marathon: Marathon is a framework to run containers at scale on Apache Mesos and DC/OS.
    - Nomad:Nomad is the container and workload orchestrator provided by HashiCorp.
    - Docker Swarm:  container orchestrator provided by Docker, Inc. It is part of Docker Engine.
  - Capabilities offered by container orchestrators
    -  Group hosts together while creating a cluster.
    -  Schedule containers to run on hosts in the cluster based on resources availability.
    -  Enable containers in a cluster to communicate with each other regardless of the host they are deployed to in the cluster.
    -  Bind containers and storage resources.
    -  Group sets of similar containers and bind them to load-balancing constructs to simplify access to containerized applications by creating an interface, a level of abstraction between the containers and the client.
    -  Manage and optimize resource usage.
    -  Allow for implementation of policies to secure access to applications running inside containers.
  - Container orchestrators can be deployed on the infrastructure of our choice - on bare metal, Virtual Machines, on-premises, on public and hybrid clouds. Kubernetes, for example, can be deployed on a workstation, with or without an isolation layer such as a local hypervisor or container runtime, inside a company's data center, in the cloud on AWS Elastic Compute Cloud (EC2) instances, Google Compute Engine (GCE) VMs, DigitalOcean Droplets, OpenStack, etc.       

# Terminology
- A Pod is the smallest scheduling work unit in Kubernetes. It is a logical collection of one or more containers scheduled together, and the collection can be started, stopped, or rescheduled as a single unit of work.
- The kubelet is an agent running on each node, control plane and workers, and communicates with the control plane. It receives Pod definitions, primarily from the API Server, and interacts with the container runtime on the node to run containers associated with the Pod. It also monitors the health and resources of Pods running containers.
  
# K8s Architecture

## Control Plane
- The control plane node provides a running environment for the control plane agents responsible for managing the state of a Kubernetes cluster, and it is the brain behind all operations inside the cluster.
- The control plane components are agents with very distinct roles in the cluster's management. In order to communicate with the Kubernetes cluster, users send requests to the control plane via a Command Line Interface (CLI) tool, a Web User-Interface (Web UI) Dashboard, or an Application Programming Interface (API).
- CP HA:  While only one of the control plane nodes is dedicated to actively managing the cluster, the control plane components stay in sync across the control plane node replicas. This type of configuration adds resiliency to the cluster's control plane, should the active control plane node fail.  While only one of the control plane nodes is dedicated to actively managing the cluster, the control plane components stay in sync across the control plane node replicas. This type of configuration adds resiliency to the cluster's control plane, should the active control plane node fail.
- To persist the Kubernetes cluster's state, all cluster configuration data is saved to a distributed key-value store which only holds cluster state related data, no client workload generated data. The key-value store may be configured on the control plane node (stacked topology), or on its dedicated host (external topology) to help reduce the chances of data store loss by decoupling it from the other control plane agents.
- A control plane node runs the following essential control plane components and agents: (ASCK) API Server, Scheduler, Controller Managers, Key-Value Data Store.
- In addition, the control plane node runs: CNPO Container Runtime, Node Agent, Proxy, Optional add-ons for cluster-level monitoring and logging.
- CP components in detail
  - API Server
    - All the administrative tasks are coordinated by the kube-apiserver, a central control plane component running on the control plane node.
    - The API Server intercepts RESTful calls from users, administrators, developers, operators and external agents, then validates and processes them.
    - During processing the API Server reads the Kubernetes cluster's current state from the key-value store, and after a call's execution, the resulting state of the Kubernetes cluster is saved in the key-value store for persistence.
    - The API Server is the only control plane component to talk to the key-value store, both to read from and to save Kubernetes cluster state information - acting as a middle interface for any other control plane agent inquiring about the cluster's state.
    - The API Server is highly configurable and customizable. It can scale horizontally, but it also supports the addition of custom secondary API Servers, a configuration that transforms the primary API Server into a proxy to all secondary, custom API Servers, routing all incoming RESTful calls to them based on custom defined rules.
 
  - Scheduler
    - kube-scheduler is to assign new workload objects, such as pods encapsulating containers, to nodes - typically worker nodes. During the scheduling process, decisions are made based on current Kubernetes cluster state and new workload object's requirements. The scheduler obtains from the key-value store, via the API Server, resource usage data for each worker node in the cluster. The scheduler also receives from the API Server the new workload object's requirements which are part of its configuration data.
    - The scheduler also takes into account Quality of Service (QoS) requirements, data locality, affinity, anti-affinity, taints, toleration, cluster topology, etc.
    - The outcome of the decision process is communicated back to the API Server, which then delegates the workload deployment with other control plane agents.
    - The scheduler is highly configurable and customizable through scheduling policies, plugins, and profiles. Additional custom schedulers are also supported, then the object's configuration data should include the name of the custom scheduler expected to make the scheduling decision for that particular object; if no such data is included, the default scheduler is selected instead. 
  - Controller Managers
    - controller managers are components of the control plane node running controllers or operator processes to regulate the state of the Kubernetes cluster.
    - Controllers are watch-loop processes continuously running and comparing the cluster's desired state (provided by objects' configuration data) with its current state (obtained from the key-value store via the API Server).
      - kube-controller-manager runs controllers or operators responsible to act when nodes become unavailable, to ensure container pod counts are as expected, to create endpoints, service accounts, and API access tokens.
      - The cloud-controller-manager runs controllers or operators responsible to interact with the underlying infrastructure of a cloud provider when nodes become unavailable, to manage storage volumes when provided by a cloud service, and to manage load balancing and routing. 
    - In case of a mismatch, corrective action is taken in the cluster until its current state matches the desired state. 
  - Key-Value Data Store.
    - etcd is an open source project under the Cloud Native Computing Foundation (CNCF).
    - etcd is a strongly consistent, distributed key-value data store used to persist a Kubernetes cluster's state.
    - New data is written to the data store only by appending to it, data is never replaced in the data store.
    - Obsolete data is compacted (or shredded) periodically to minimize the size of the data store.
    - Out of all the control plane components, only the API Server is able to communicate with the etcd data store.
    - etcd's CLI management tool - etcdctl, provides snapshot save and restore capabilities which come in handy especially for a single etcd instance Kubernetes cluster, common in Development and learning environments.
    - However, in Stage and Production environments, it is extremely important to replicate the data stores in HA mode, for cluster configuration data resiliency.
    - Some Kubernetes cluster bootstrapping tools, such as kubeadm, by default, provision stacked etcd control plane nodes, where the data store runs alongside and shares resources with the other control plane components on the same control plane node.
    - For data store isolation from the control plane components, the bootstrapping process can be configured for an external etcd topology, where the data store is provisioned on a dedicated separate host, thus reducing the chances of an etcd failure.
    - ![image](https://github.com/trohit/ik/assets/466385/6e86d866-cb3c-4341-8053-b251ff86dd87)
    - ![image](https://github.com/trohit/ik/assets/466385/aa868c72-2899-421f-ba84-71d8f27b382e)
    - Both stacked and external etcd topologies support HA configurations. etcd is based on the Raft Consensus Algorithm which allows a collection of machines to work as a coherent group that can survive the failures of some of its members. At any given time, one of the nodes in the group will be the leader, and the rest of them will be the followers. etcd gracefully handles leader elections and can tolerate node failure, including leader node failures. Any node can be treated as a leader.
    - ![image](https://github.com/trohit/ik/assets/466385/30ba3cb6-a519-40dd-9d9b-9511aee00f5f)
    - etcd is written in the Go programming language. In Kubernetes, besides storing the cluster state, etcd is also used to store configuration details such as subnets, ConfigMaps, Secrets, etc.

# Data Plane
## Worker Node Overview
- A worker node provides a running environment for client applications. These applications are microservices running as application containers.
- In Kubernetes the application containers are encapsulated in Pods, controlled by the cluster control plane agents running on the control plane node.
- Pods are scheduled on worker nodes, where they find required compute, memory and storage resources to run, and networking to talk to each other and the outside world. A Pod is the smallest scheduling work unit in Kubernetes.
- It is a logical collection of one or more containers scheduled together, and the collection can be started, stopped, or rescheduled as a single unit of work. 
- Also, in a multi-worker Kubernetes cluster, the network traffic between client users and the containerized applications deployed in Pods is handled directly by the worker nodes, and is not routed through the control plane node.
- A worker node has the following components:CNPA Container Runtime,Node Agent - kubelet,Proxy - kube-proxy, Add-ons for DNS, Dashboard user interface, cluster-level monitoring and logging.
  - Container Runtime : Although Kubernetes is described as a "container orchestration engine", it lacks the capability to directly handle and run containers. In order to manage a container's lifecycle, Kubernetes requires a container runtime on the node where a Pod and its containers are to be scheduled. Runtimes are required on all nodes of a Kubernetes cluster, both control plane and worker. Kubernetes supports several container runtimes:
    - [CRI-O](https://cri-o.io/):(Backed by RedHat): A lightweight container runtime for Kubernetes, supporting quay.io and Docker Hub image registries. New default
    - containerd: A simple, robust, and portable container runtime.
    - Docker Engine: A popular and complex container platform which uses containerd as a container runtime.
    - Mirantis Container Runtime: Formerly known as the Docker Enterprise Edition. 
  - Node Agent - kubelet
    - The kubelet is an agent running on each node, control plane and workers, and communicates with the control plane. It receives Pod definitions, primarily from the API Server, and interacts with the container runtime on the node to run containers associated with the Pod. It also monitors the health and resources of Pods running containers.
    - The kubelet connects to container runtimes through a plugin based interface - the Container Runtime Interface (CRI). The CRI consists of protocol buffers, gRPC API, libraries, and additional specifications and tools. In order to connect to interchangeable container runtimes, kubelet uses a CRI shim, an application which provides a clear abstraction layer between kubelet and the container runtime.
    - ![image](https://github.com/trohit/ik/assets/466385/0dfae30a-c5aa-46c3-a6c6-809991c66209)
    - the kubelet acting as grpc client connects to the CRI shim acting as grpc server to perform container and image operations. The CRI implements two services: ImageService and RuntimeService. The ImageService is responsible for all the image-related operations, while the RuntimeService is responsible for all the Pod and container-related operations.
      - kubelet - CRI shims : Originally the kubelet agent supported only a couple of container runtimes, first the Docker Engine followed by rkt, through a unique interface model integrated directly in the kubelet source code. However, this approach was not intended to last forever even though it was especially beneficial for Docker. In time, Kubernetes started migrating towards a standardized approach to container runtime integration by introducing the CRI. Kubernetes adopted a decoupled and flexible method to integrate with various container runtimes without the need to recompile its source code. Any container runtime that implements the CRI could be used by Kubernetes to manage containers.
      - Shims are Container Runtime Interface (CRI) implementations, interfaces or adapters, specific to each container runtime supported by Kubernetes. Below we present some examples of CRI shims:
        - cri-containerd: cri-containerd allows containers to be directly created and managed with containerd at kubelet's request
          - ![image](https://github.com/trohit/ik/assets/466385/52add489-e169-4876-bde0-7c31523d0d44)
        - CRI-O: CRI-O enables the use of any Open Container Initiative (OCI) compatible runtime with Kubernetes, such as runC
          - ![image](https://github.com/trohit/ik/assets/466385/766e174a-86ce-4f7a-b131-f0e8cac80971)
        - dockershim and cri-dockerd: Before Kubernetes release v1.24 the dockershim allowed containers to be created and managed by invoking the Docker Engine and its internal runtime containerd. Due to Docker Engine's popularity, this shim has been the default interface used by kubelet. However, starting with Kubernetes release v1.24, the [dockershim is no longer being maintained by the Kubernetes project](https://kubernetes.io/blog/2022/02/17/dockershim-faq/), its specific code is removed from kubelet source code, thus will no longer be supported by the kubelet node agent of Kubernetes. As a result, Docker, Inc., and Mirantis have agreed to introduce and maintain a replacement adapter, cri-dockerd that would ensure that the Docker Engine will continue to be a container runtime option for Kubernetes, in addition to the Mirantis Container Runtime (MCR). The introduction of cri-dockerd also ensures that both Docker Engine and MCR follow the same standardized integration method as the CRI-compatible runtimes.
          - ![image](https://github.com/trohit/ik/assets/466385/475b2484-0123-4f80-8126-d24a6cc83c7e) 
  - Proxy - kube-proxy
    -  kube-proxy is the network agent which runs on each node, control plane and workers, responsible for dynamic updates and maintenance of all networking rules on the node. It abstracts the details of Pods networking and forwards connection requests to the containers in the Pods.
    - The kube-proxy is responsible for TCP, UDP, and SCTP stream forwarding or random forwarding across a set of Pod backends of an application, and it implements forwarding rules defined by users through Service API objects. 
  - Add-ons for DNS, Dashboard user interface, cluster-level monitoring and logging. (DDML)
    - Add-ons are cluster features and functionality not yet available in Kubernetes, therefore implemented through 3rd-party pods and services.
      - DNS: Cluster DNS is a DNS server required to assign DNS records to Kubernetes objects and resources.
      - Dashboard: A general purpose web-based user interface for cluster management.
      - Monitoring: Collects cluster-level container metrics and saves them to a central data store.
      - Logging: Collects cluster-level container logs and saves them to a central log store for analysis.
- Networking challenges : Decoupled microservices based applications rely heavily on [networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/) in order to mimic the tight-coupling once available in the monolithic era. 
  - Container-to-Container communication inside Pods
    - Making use of the underlying host operating system's kernel virtualization features, a container runtime creates an isolated network space for each container it starts. On Linux, this isolated network space is referred to as a network namespace. A network namespace can be shared across containers, or with the host operating system.
    - When a grouping of containers defined by a Pod is started, a special infrastructure Pause container is initialized by the Container Runtime for the sole purpose of creating a network namespace for the Pod. All additional containers, created through user requests, running inside the Pod will share the Pause container's network namespace so that they can all talk to each other via localhost.
  - Pod-to-Pod communication on the same node and across cluster nodes
    - In a Kubernetes cluster Pod, groups of containers, are scheduled on nodes in a nearly unpredictable fashion. Regardless of their host node, Pods are expected to be able to communicate with all other Pods in the cluster, all this without the implementation of Network Address Translation (NAT). This is a fundamental requirement of any networking implementation in Kubernetes.
    - The Kubernetes network model aims to reduce complexity, and it treats Pods as VMs on a network, where each VM is equipped with a network interface - thus each Pod receiving a unique IP address. This model is called "IP-per-Pod" and ensures Pod-to-Pod communication, just as VMs are able to communicate with each other on the same network.
    - Let's not forget about containers though. They share the Pod's network namespace and must coordinate ports assignment inside the Pod just as applications would on a VM, all while being able to communicate with each other on localhost - inside the Pod. However, containers are integrated with the overall Kubernetes networking model through the use of the Container Network Interface (CNI) supported by CNI plugins. CNI is a set of specifications and libraries which allow plugins to configure the networking for containers. While there are a few core plugins, most CNI plugins are 3rd-party Software Defined Networking (SDN) solutions implementing the Kubernetes networking model. In addition to addressing the fundamental requirement of the networking model, some networking solutions offer support for Network Policies. Flannel, Weave, Calico are only a few of the SDN solutions available for Kubernetes clusters.
    - The container runtime offloads the IP assignment to CNI, which connects to the underlying configured plugin, such as Bridge or MACvlan, to get the IP address. Once the IP address is given by the respective plugin, CNI forwards it back to the requested container runtime.
    - ![image](https://github.com/trohit/ik/assets/466385/d2f02df6-803b-48a5-918b-258b554ac967)
  - External-to-Pod communication: A successfully deployed containerized application running in Pods inside a Kubernetes cluster may require accessibility from the outside world. Kubernetes enables external accessibility through Services, complex encapsulations of network routing rule definitions stored in iptables on cluster nodes and implemented by kube-proxy agents. By exposing services to the external world with the aid of kube-proxy, applications become accessible from outside the cluster over a virtual IP address and a dedicated port number.
 
  - Service-to-Pod communication within the same namespace and across cluster namespaces
  - External-to-Service communication for clients to access applications in a cluster 
 
In addition, the control plane node runs:
- Container Runtime
- Node Agent
- Proxy
- Optional add-ons for cluster-level monitoring and logging.

## K8S deployment config options
- Kubernetes can be installed using different cluster configurations. K8S best practices recommend multi-host environments that support High-Availability control plane setups and multiple worker nodes for client workload for production purposes. The major installation types are described below:
  - All-in-One Single-Node Installation: In this setup, all the control plane and worker components are installed and running on a single-node. While it is useful for learning, development, and testing, it is not recommended for production purposes.
  - Single-Control Plane and Multi-Worker Installation: In this setup, we have a single-control plane node running a stacked etcd instance. Multiple worker nodes can be managed by the control plane node.
  - Single-Control Plane with Single-Node etcd, and Multi-Worker Installation: In this setup, we have a single-control plane node with an external etcd instance. Multiple worker nodes can be managed by the control plane node.
  - Multi-Control Plane and Multi-Worker Installation: In this setup, we have multiple control plane nodes configured for High-Availability (HA), with each control plane node running a stacked etcd instance. The etcd instances are also configured in an HA etcd cluster and multiple worker nodes can be managed by the HA control plane.
  - Multi-Control Plane with Multi-Node etcd, and Multi-Worker Installation: In this setup, we have multiple control plane nodes configured in HA mode, with each control plane node paired with an external etcd instance. The external etcd instances are also configured in an HA etcd cluster, and multiple worker nodes can be managed by the HA control plane. This is the most advanced cluster configuration recommended for production environments. 

### K8S infra for install
- Once installation type is chosen, we need to decide on the infrastructure. Infrastructure related decisions are typically guided by the desired environment type, either learning or production environment. For infrastructure, we need to decide on the following:
- Should we set up Kubernetes on bare metal, public cloud, private, or hybrid cloud?
- Which underlying OS should we use? Should we choose a Linux distribution - Red Hat-based or Debian-based, or Windows?
- Which networking solution (CNI) should we use?
- See [k8s setup](https://kubernetes.io/docs/setup/) for details.

#### K8S Local learning clusters
- Minikube :Single- and multi-node local Kubernetes cluster, recommended for a learning environment deployed on a single host.
- Kind :Multi-node Kubernetes cluster deployed in Docker containers acting as Kubernetes nodes, recommended for a learning environment.
- Docker Desktop:Including a local Kubernetes cluster for Docker users. 
- MicroK8s :Local and cloud Kubernetes cluster for developers and production, from Canonical.
- K3S :Lightweight Kubernetes cluster for local, cloud, edge, IoT deployments, originally from Rancher, currently a CNCF project.

#### K8S Production cluster deployment options
- See https://github.com/kelseyhightower/kubernetes-the-hard-way
- production deployment options
  - kubeadm is a first-class citizen of the Kubernetes ecosystem. It is a secure and recommended method to bootstrap a multi-node production ready Highly Available Kubernetes cluster, on-premises or in the cloud. kubeadm can also bootstrap a single-node cluster for learning. It has a set of building blocks to set up the cluster, but it is easily extendable to add more features. Please note that kubeadm does not support the provisioning of hosts - they should be provisioned separately with a tool of our choice.
  - kubespray (formerly known as kargo) allows us to install Highly Available production ready Kubernetes clusters on AWS, GCP, Azure, OpenStack, vSphere, or bare metal. kubespray is based on Ansible, and is available on most Linux distributions. It is a Kubernetes Incubator project.
  - [kops](https://github.com/kubernetes/kops/) enables us to create, upgrade, and maintain production-grade, Highly Available Kubernetes clusters from the command line. It can provision the required infrastructure as well. Currently, AWS is officially supported. Support for DigitalOcean and OpenStack is in beta, Azure and GCE is in alpha support, and other platforms are planned for the future.
- Win: Since Kubernetes v1.14, Windows was successfully introduced as a supported production ready operating system only for worker nodes of a Kubernetes cluster. 

 ##### K8s hosted solutions
- Hosted Solutions providers fully manage the provided software stack, while the user pays hosting and management charges. Popular vendors providing hosted solutions for Kubernetes are (listed in alphabetical order):
- Alibaba Cloud Container Service for Kubernetes (ACK)
- Amazon Elastic Kubernetes Service (EKS)
- Azure Kubernetes Service (AKS)
- DigitalOcean Kubernetes
- Google Kubernetes Engine (GKE)
- IBM Cloud Kubernetes Service
- Oracle Container Engine for Kubernetes (OKE)
- Platform9 Managed Kubernetes (PMK)
- Red Hat OpenShift
- VMware Tanzu Kubernetes Grid 

# Certification
- https://www.cncf.io/training/certification/cka/
  
# Courses
- https://kubernetes.io/docs/home/
- https://kode.wiki/kubernetes-labs
- https://kubernetes.io/docs/
- https://github.com/kubernetes
- https://kubernetes.io/blog/
- https://www.udemy.com/topic/kubernetes/free/
- https://medium.com/geekculture/top-5-free-kubernetes-certifications-8c86b2c5b590

## Paid
- [Intro to K8S](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/block-v1:LinuxFoundationX+LFS158x+1T2022+type@sequential+block@e10a62dcf641474c997eabd0602111cb/block-v1:LinuxFoundationX+LFS158x)
## Github
- https://github.com/alijahnas/CKA-practice-exercises
- https://petermd.github.io/kubernetes-the-hard-way/
- https://github.com/kodekloudhub/certified-kubernetes-administrator-course
- https://github.com/alifiroozi80/CKA
- https://github.com/leandrocostam/cks-preparation-guide
- https://github.com/AdilKhan1117/CKA-Exam-Study-Walkthrough/tree/main
# Tutorials
- Videos
  - https://www.youtube.com/watch?v=XuSQU5Grv1g
  - https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/?couponCode=ST12MT030524

# Learning k8s hands-on 
- https://www.reddit.com/r/kubernetes/comments/be0415/k3s_minikube_or_microk8s/
- https://microk8s.io/compare
  
# Lessons learnt from running k8s
- https://k8s.af/
- k8s Case studies: https://kubernetes.io/case-studies/
  
