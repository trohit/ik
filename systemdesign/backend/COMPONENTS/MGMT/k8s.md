# Intro
- store details related to k8s
- Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
- Kubernetes comes from Greek, and means helmsman or ship pilot. With this analogy in mind, we can think of Kubernetes as the pilot on a ship of containers.
- Kubernetes is also referred to as k8s (pronounced Kate's), as there are 8 characters between k and s.
- Kubernetes is highly inspired by the Google Borg system, a container and workload orchestrator for its global operations for more than a decade. It is an open source project written in the Go language and licensed under the Apache License, Version 2.0.
- Kubernetes was started by Google and, with its v1.0 release in July 2015, Google donated it to the Cloud Native Computing Foundation (CNCF), one of the largest sub-foundations of the Linux Foundation.
- New Kubernetes versions are released in 4 month cycles.

# History and Current Status
- K8s evolved from Borg, Google's own distributed workload manager.
- Currently k8s maintained by  Cloud Native Computing Foundation (CNCF), which currently hosts the Kubernetes project, along with other popular cloud-native projects, such as Prometheus, Fluentd, cri-o, containerd, Helm, Envoy, and Contour, just to name a few.

![image](https://github.com/trohit/ik/assets/466385/18371e20-0153-4e18-9911-300fc9a10331)

# Details
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
## Control Plane
A control plane node runs the following essential control plane components and agents:
- API Server
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




 
In addition, the control plane node runs:
- Container Runtime
- Node Agent
- Proxy
- Optional add-ons for cluster-level monitoring and logging.
  
# Courses
- https://kode.wiki/kubernetes-labs
- https://www.udemy.com/topic/kubernetes/free/
- https://medium.com/geekculture/top-5-free-kubernetes-certifications-8c86b2c5b590
## Paid
- [Intro to K8S](https://learning.edx.org/course/course-v1:LinuxFoundationX+LFS158x+1T2022/block-v1:LinuxFoundationX+LFS158x+1T2022+type@sequential+block@e10a62dcf641474c997eabd0602111cb/block-v1:LinuxFoundationX+LFS158x)

# Tutorials
- Videos
  - https://www.youtube.com/watch?v=XuSQU5Grv1g
  -  
# Lessons learnt from running k8s
- https://k8s.af/
- k8s Case studies: https://kubernetes.io/case-studies/
  
