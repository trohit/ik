  * [Create an NGINX Pod](#create-an-nginx-pod)
  * [Deploy a redis pod using the redis:alpine image with the labels set to tier=db.](#deploy-a-redis-pod-using-the-redis-alpine-image-with-the-labels-set-to-tier-db)
  * [Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)](#generate-pod-manifest-yaml-file---o-yaml--don-t-create-it---dry-run-)
  * [Create a deployment](#create-a-deployment)
  * [Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)](#generate-deployment-yaml-file---o-yaml--don-t-create-it---dry-run-)
  * [Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file.](#generate-deployment-yaml-file---o-yaml--don-t-create-it--dry-run--and-save-it-to-a-file)
  * [Make necessary changes to the file (for example, adding more replicas) and then create the deployment.](#make-necessary-changes-to-the-file--for-example--adding-more-replicas--and-then-create-the-deployment)
  * [Expose a port](#expose-a-port)
  * [Edit a deployment](#edit-a-deployment)
    + [non-persistent live obj edit](#non-persistent-live-obj-edit)
    + [persistent edit](#persistent-edit)
  * [Scale a deployment](#scale-a-deployment)
  * [set image for deployment](#set-image-for-deployment)
  * [update a pod](#update-a-pod)
  * [delete a pod](#delete-a-pod)
  * [see all pods but without the headers](#see-all-pods-but-without-the-headers)
  * [see all the labels of all the pods in Kubernetes](#see-all-the-labels-of-all-the-pods-in-kubernetes)
  * [see all pods that match a selector 'env=dev'](#see-all-pods-that-match-a-selector--env-dev-)
  * [count the number of pods that match env=prod,bu=finance and tier=frontend so dont display the header](#count-the-number-of-pods-that-match-env-prod-bu-finance-and-tier-frontend-so-dont-display-the-header)
  * [delete all pods that have a label starting with "app-"](#delete-all-pods-that-have-a-label-starting-with--app--)
  * [Ways to create a namespace](#ways-to-create-a-namespace)
  * [To set a persistent namespace context](#to-set-a-persistent-namespace-context)
- [Service](#service)
  * [Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379](#create-a-service-named-redis-service-of-type-clusterip-to-expose-pod-redis-on-port-6379)
  * [Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:](#create-a-service-named-nginx-of-type-nodeport-to-expose-pod-nginx-s-port-80-on-port-30080-on-the-nodes-)
  * [patch a running deployment with a different image](#patch-a-running-deployment-with-a-different-image)
- [Ref](#ref)
  * [Help](#help)
- [Kickstart](#kickstart)
- [Cmds](#cmds)
  * [OR](#or)
- [whats the image used to create the new pods](#whats-the-image-used-to-create-the-new-pods)
- [which node is this pod running on ?](#which-node-is-this-pod-running-on--)
- [how many containers are part of the pod webapp](#how-many-containers-are-part-of-the-pod-webapp)
- [what images are used in the new webapp pod ?](#what-images-are-used-in-the-new-webapp-pod--)
- [what is the state of container agentx in pod webapp?](#what-is-the-state-of-container-agentx-in-pod-webapp-)
- [why do you think comtainer agentx in pod webapp is in err ?](#why-do-you-think-comtainer-agentx-in-pod-webapp-is-in-err--)
- [del the pod webapp](#del-the-pod-webapp)
- [create a new pod redis with image redis123](#create-a-new-pod-redis-with-image-redis123)
- [Now change the image on this pod to redis.](#now-change-the-image-on-this-pod-to-redis)
  * [OR](#or-1)
  * [OR](#or-2)
- [Deploy a pod named nginx-pod using the nginx:alpine image.](#deploy-a-pod-named-nginx-pod-using-the-nginx-alpine-image)
- [Deploy a redis pod using the redis:alpine image with the labels set to tier=db.](#deploy-a-redis-pod-using-the-redis-alpine-image-with-the-labels-set-to-tier-db-1)
- [Create a pod redis that runs ith image redis:alpine and label tier=db](#create-a-pod-redis-that-runs-ith-image-redis-alpine-and-label-tier-db)
- [Create a service redis-service to expose the redis application within the cluster on port 6379.](#create-a-service-redis-service-to-expose-the-redis-application-within-the-cluster-on-port-6379)
- [Create a deployment named webapp using the image kodekloud/webapp-color with 3 replicas.](#create-a-deployment-named-webapp-using-the-image-kodekloud-webapp-color-with-3-replicas)
- [Create a new pod called custom-nginx using the nginx image and expose it on container port 8080.](#create-a-new-pod-called-custom-nginx-using-the-nginx-image-and-expose-it-on-container-port-8080)
- [Create a new namespace called dev-ns.](#create-a-new-namespace-called-dev-ns)
- [Create a new deployment called redis-deploy in the dev-ns namespace with the redis image. It should have 2 replicas.](#create-a-new-deployment-called-redis-deploy-in-the-dev-ns-namespace-with-the-redis-image-it-should-have-2-replicas)
- [Create a pod called httpd using the image httpd:alpine in the default namespace.](#create-a-pod-called-httpd-using-the-image-httpd-alpine-in-the-default-namespace)
- [Next, create a service of type ClusterIP by the same name (httpd). The target port for the service should be 80.](#next--create-a-service-of-type-clusterip-by-the-same-name--httpd--the-target-port-for-the-service-should-be-80)
- [Deploy a pod named nginx-pod using the nginx:alpine image.](#deploy-a-pod-named-nginx-pod-using-the-nginx-alpine-image-1)
- [Deploy a redis pod using the redis:alpine image with the labels set to tier=db.](#deploy-a-redis-pod-using-the-redis-alpine-image-with-the-labels-set-to-tier-db-2)
- [Create a pod redis that runs ith image redis:alpine and label tier=db](#create-a-pod-redis-that-runs-ith-image-redis-alpine-and-label-tier-db-1)
- [Create a service redis-service to expose the redis application within the cluster on port 6379.](#create-a-service-redis-service-to-expose-the-redis-application-within-the-cluster-on-port-6379-1)
- [Create a deployment named webapp using the image kodekloud/webapp-color with 3 replicas.](#create-a-deployment-named-webapp-using-the-image-kodekloud-webapp-color-with-3-replicas-1)
- [Create a new pod called custom-nginx using the nginx image and expose it on container port 8080.](#create-a-new-pod-called-custom-nginx-using-the-nginx-image-and-expose-it-on-container-port-8080-1)
- [Create a new namespace called dev-ns.](#create-a-new-namespace-called-dev-ns-1)
- [Create a new deployment called redis-deploy in the dev-ns namespace with the redis image. It should have 2 replicas.](#create-a-new-deployment-called-redis-deploy-in-the-dev-ns-namespace-with-the-redis-image-it-should-have-2-replicas-1)
  * [Create a pod called httpd using the image httpd:alpine in the default namespace.](#create-a-pod-called-httpd-using-the-image-httpd-alpine-in-the-default-namespace-1)
  * [Next, create a service of type ClusterIP by the same name (httpd). The target port for the service should be 80.](#next--create-a-service-of-type-clusterip-by-the-same-name--httpd--the-target-port-for-the-service-should-be-80-1)
- [Delete and recreate a pod in one go](#delete-and-recreate-a-pod-in-one-go)
- [get k8s pods status periodically](#get-k8s-pods-status-periodically)
- [Taints and Tolerations](#taints-and-tolerations)
  * [Taint a node with a taint effect](#taint-a-node-with-a-taint-effect)
- [Network](#network)
  * [get a list of all ips and ports being used in k8s](#get-a-list-of-all-ips-and-ports-being-used-in-k8s)
- [Custom k8s cmds](#custom-k8s-cmds)
  * [podname, status, node](#podname--status--node)
  * [list podname, poduid](#list-podname--poduid)
  * [nodename, podname, svc_account](#nodename--podname--svc-account)
  * [PodName,PodIP,NodeName,hostIp](#podname-podip-nodename-hostip)
  * [get custom headers](#get-custom-headers)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

![image](https://github.com/trohit/ik/assets/466385/bb806ae4-2eac-455d-8448-600b5664600f)
# Ref
- https://kubernetes.io/docs/reference/kubectl/
- https://kubernetes.io/docs/reference/kubectl/conventions/
- https://kubectl.docs.kubernetes.io/guides/
- https://helm.sh/docs/intro/cheatsheet/

## imp k8s files
- /var/lib/kubelet/config.yaml
- /etc/kubernetes/manifests
  - each kubelet monitors this path for new or changed yamls and applies the reconcile loop accordingly 

## Create an NGINX Pod

    kubectl run nginx-pod --image=nginx:alpine

## Deploy a redis pod using the redis:alpine image with the labels set to tier=db.
kubectl run pod redis --image=redis:alpine -l tier=db

OR

kubectl run redis -l tier=db --image=redis:alpine --dry-run=client -o yaml > redis-pod.yaml

kubectl create -f redis-pod.yaml

## Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)
kubectl run nginx --image=nginx --dry-run=client -o yaml

## Create a deployment
kubectl create deployment --image=nginx nginx

## Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml

## Generate Deployment YAML file (-o yaml). Don’t create it(–dry-run) and save it to a file.
kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml

## Make necessary changes to the file (for example, adding more replicas) and then create the deployment.
kubectl create -f nginx-deployment.yaml

## Expose a port
kubectl expose deployment nginx --port 80

## Edit a deployment
### non-persistent live obj edit
kubectl edit deployment nginx

_changes will only apply on live object_<br>
kubectl scale --replicas=3 <object_type> <object_name>
OR

kubectl patch <object_type> <object_name> --patch '{"spec": {"replicas": 3}}'

### persistent edit
vim deployment-definition.yaml

_will open the specified YAML file in your default editor, and any changes you make will be applied to the live object._<br>_also any changes will be recorded as part of change review process_<br>kubectl replace -f deployment-definition.yaml

_will completely delete and recreate object_<br>kubectl replace --force -f deployment-definition.yaml

Or

_declarative way, will always work_<br>kubectl apply --edit -f <resource_file.yaml>

kubectl apply -f <resource_file.yaml>

_will apply all files in the dir at once_<br>kubectl apply -f /path/to/config-files

## Scale a deployment
kubectl scale deployment nginx --replicas=5

## set image for deployment
kubectl set image deployment nginx mycontainer=nginx:latest

## update a pod
kubectl replace -f nginx.yaml

## delete a pod
kubectl delete -f nginx.yaml

## see all pods but without the headers
_--no-headers equivalent to sed 1d_
k get pods --no-headers

## see all the labels of all the pods in Kubernetes
k get pod --show-labels

## see all pods that match a selector 'env=dev'
k get pods --selector env=dev

## count the number of pods that match env=prod,bu=finance and tier=frontend so dont display the header
k get pods --selector env=prod,bu=finance,tier=frontend --no-headers | wc -l

## delete all pods that have a label starting with "app-"
k delete pods -l app-

## Ways to create a namespace

k create namespace mynamespace

## To set a persistent namespace context
k config set-config $(kubectl config current-context) --namespace=dev

OR
```
cat > namespace-definition.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mynamespace
k create -f namespace-definition.yaml
```

# Service
## Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379

_(This will **automatically** use the pod's labels as selectors)_<br>kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml

_(This will **not use** the pods labels as selectors, instead it will assume selectors as app=redis._<br>_You cannot pass in selectors as an option. So it does not work very well if your pod has a different label set._<br>_So generate the file and modify the selectors before creating the service)_<br>kubectl create service clusterip redis --tcp=6379:6379 --dry-run=client -o yaml 

## Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:
_(This will **automatically** use the pod's labels as selectors, but you cannot specify the node port. You have to generate a definition file and then add the node port in manually before creating the service with the pod.)_<br>kubectl expose pod nginx --type=NodePort --port=80 --name=nginx-service --dry-run=client -o yaml

Or
_(This will **not use** the pods labels as selectors)_<br>kubectl create service nodeport nginx --tcp=80:80 --node-port=30080 --dry-run=client -o yaml

## patch a running deployment with a different image
kubectl patch deployment <deployment-name> -p '{"spec":{"template":{"spec":{"containers":[{"name":"<container-name>","image":"<new-image>"}]}}}}'


# Ref
- https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
- https://kubernetes.io/docs/reference/kubectl/conventions/

## Help
```
kubectl controls the Kubernetes cluster manager.

## Find more information at: https://kubernetes.io/docs/reference/kubectl/

Basic Commands (Beginner):
  create          Create a resource from a file or from stdin
  expose          Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
  run             Run a particular image on the cluster
  set             Set specific features on objects

Basic Commands (Intermediate):
  explain         Get documentation for a resource
  get             Display one or many resources
  edit            Edit a resource on the server
  delete          Delete resources by file names, stdin, resources and names, or by resources and label selector

Deploy Commands:
  rollout         Manage the rollout of a resource
  scale           Set a new size for a deployment, replica set, or replication controller
  autoscale       Auto-scale a deployment, replica set, stateful set, or replication controller

Cluster Management Commands:
  certificate     Modify certificate resources
  cluster-info    Display cluster information
  top             Display resource (CPU/memory) usage
  cordon          Mark node as unschedulable
  uncordon        Mark node as schedulable
  drain           Drain node in preparation for maintenance
  taint           Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe        Show details of a specific resource or group of resources
  logs            Print the logs for a container in a pod
  attach          Attach to a running container
  exec            Execute a command in a container
  port-forward    Forward one or more local ports to a pod
  proxy           Run a proxy to the Kubernetes API server
  cp              Copy files and directories to and from containers
  auth            Inspect authorization
  debug           Create debugging sessions for troubleshooting workloads and nodes
  events          List events

Advanced Commands:
  diff            Diff the live version against a would-be applied version
  apply           Apply a configuration to a resource by file name or stdin
  patch           Update fields of a resource
  replace         Replace a resource by file name or stdin
  wait            Experimental: Wait for a specific condition on one or many resources
  kustomize       Build a kustomization target from a directory or URL

Settings Commands:
  label           Update the labels on a resource
  annotate        Update the annotations on a resource
  completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

Subcommands provided by plugins:

Other Commands:
  api-resources   Print the supported API resources on the server
  api-versions    Print the supported API versions on the server, in the form of "group/version"
  config          Modify kubeconfig files
  plugin          Provides utilities for interacting with plugins
  version         Print the client and server version information

Usage:
  kubectl [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).

```
# Kickstart
```
To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/
  
To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/
  
To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

```

# Cmds
- kubectl get pods --namespace=default --no-headers
- kubectl run nginx-pod --image=nginx --dry-run=client -o yaml > nginx-pod.yaml
- kubectl apply -f nginx-pod.yaml
## OR
- kubectl run nginx --image=nginx
- List all kind of workloads
  - k get deployment,replicasets,statefulsets,daemonset,job,cronjob -A
- get list of namespaces
  - k get ns
- get pods from all namespaces
  - k get pods -A
  - k get pods --all-namespaces
- get a pods yaml
  - k get pod $podname -o yaml -n $namespace
- get pvc list
  - k get pvc -A  


# whats the image used to create the new pods
for i in `kubectl get pods --no-headers | awk {'print$1'}` ; do   kubectl describe pod $i | grep -i image; done

# which node is this pod running on ?
- kubectl get pods -o wide
- kubectl describe pod <podname> | grep -i Node

# how many containers are part of the pod webapp
- kubectl describe pod webapp  | grep 'Container ID' | wc -l

# what images are used in the new webapp pod ?
- kubectl describe pod webapp | grep 'Image:'

# what is the state of container agentx in pod webapp?
- kubectl describe pod webapp | grep State

# why do you think comtainer agentx in pod webapp is in err ?
- kubectl describe webapp

# del the pod webapp
- kubectl delete pod webapp

# create a new pod redis with image redis123
- kubectl run redis --image=redis123 --dry-run=client -o yaml > redis-pod.yaml
- kubectl apply -f redis-pod.yaml
OR
- kubectl run redis --image=redis123

# Now change the image on this pod to redis.
- kubectl set image pod redis redis=redis
## OR
- vim edit redis-pod.yaml 
- kubectl apply -f redis-pod.yaml
## OR
- kubectl edit redis -o yaml --save-config

# Deploy a pod named nginx-pod using the nginx:alpine image.
k run pod nginx-pod --image=nginx:alpine --dry-run=client -o yaml

k run nginx-pod --image=nginx:alpine 



# Deploy a redis pod using the redis:alpine image with the labels set to tier=db.
k run redis --image=redis:alpine -l tier=db


# Create a pod redis that runs ith image redis:alpine and label tier=db
 k run redis --image=redis:alpine -l tier=db

# Create a service redis-service to expose the redis application within the cluster on port 6379.
k expose pod redis --name=redis-service --port=6379
k expose pod redis --name redis-service --port 6379 (skipping '=' is also valid)

# Create a deployment named webapp using the image kodekloud/webapp-color with 3 replicas.
k create deployment webapp --image=kodekloud/webapp-color --replicas=3

# Create a new pod called custom-nginx using the nginx image and expose it on container port 8080.
k run custom-nginx --image=nginx --port=8080

# Create a new namespace called dev-ns.
k create ns dev-ns

# Create a new deployment called redis-deploy in the dev-ns namespace with the redis image. It should have 2 replicas.
k create deployment redis-deploy -n dev-ns --image=redis --replicas=2
kubectl create deployment redis-deploy --image=redis --replicas=2 -n dev-ns

# Create a pod called httpd using the image httpd:alpine in the default namespace. 
one: k create httpd --image=httpd:alpine -n default (cant specify image here) 

# Next, create a service of type ClusterIP by the same name (httpd). The target port for the service should be 80.
two: k create service clusterip httpd --tcp=80:80

OR do one and two together
kubectl run httpd --image=httpd:alpine --port=80 --expose


# Deploy a pod named nginx-pod using the nginx:alpine image.
k run pod nginx-pod --image=nginx:alpine --dry-run=client -o yaml

k run nginx-pod --image=nginx:alpine 



# Deploy a redis pod using the redis:alpine image with the labels set to tier=db.
k run redis --image=redis:alpine -l tier=db


# Create a pod redis that runs ith image redis:alpine and label tier=db
 k run redis --image=redis:alpine -l tier=db

# Create a service redis-service to expose the redis application within the cluster on port 6379.
k expose pod redis --name=redis-service --port=6379
k expose pod redis --name redis-service --port 6379 (skipping '=' is also valid)

# Create a deployment named webapp using the image kodekloud/webapp-color with 3 replicas.
k create deployment webapp --image=kodekloud/webapp-color --replicas=3

# Create a new pod called custom-nginx using the nginx image and expose it on container port 8080.
k run custom-nginx --image=nginx --port=8080

# Create a new namespace called dev-ns.
k create ns dev-ns

# Create a new deployment called redis-deploy in the dev-ns namespace with the redis image. It should have 2 replicas.
k create deployment redis-deploy -n dev-ns --image=redis --replicas=2
kubectl create deployment redis-deploy --image=redis --replicas=2 -n dev-ns

## Create a pod called httpd using the image httpd:alpine in the default namespace. 
one: k create httpd --image=httpd:alpine -n default (cant specify image here) 

## Next, create a service of type ClusterIP by the same name (httpd). The target port for the service should be 80.
two: k create service clusterip httpd --tcp=80:80

OR do one and two together
kubectl run httpd --image=httpd:alpine --port=80 --expose

# Delete and recreate a pod in one go
k replace --force -f nginx.yaml

# get k8s pods status periodically
k get pods --watch

# Taints and Tolerations
## Taint a node with a taint effect
_<taint-effect> can have 3 possible values: NoSchedule | PreferNoSchedule | NoExecute_ 

k taint nodes node-name key=value:<taint-effect> 

```
cat > pod-with-taint-definition.yaml
--
apiVersion: v1
kind: Pod
metadata:
spec:
  containers:
  - name: nginx-container
    image: nginx
	
  tolerations:
  - key: "app"
    operator: "Equal"
	value: "blue"
	effect: "NoSchedule"
```

# Network
## get a list of all ips and ports being used in k8s
k get svc -A -o wide

k get endpoints -A

kubectl get endpointslices -l kubernetes.io/service-name=my-nginx

# Custom k8s cmds
## podname, status, node

kubectl get pod -o=custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName --all-namespaces

## list podname, poduid
kubectl getpods -n kube-system-o custom-columns=PodName:.metadata.name,PodUID:.metadata.uid

## nodename, podname, svc_account
kubectl getpods -n kube-system -o custom-columns=NodeName:.spec.nodeName,PodName:.metadata.name,ServiceAccount:spec.serviceAccountName

## PodName,PodIP,NodeName,hostIp

kubectl get pods --all-namespaces -o custom-columns=PodName:.metadata.name,PodIP:.status.podIP,NodeName:.spec.nodeName,hostIp:.status.hostIP

## NodeName, PodName
    kubectl get pods --all-namespaces -o custom-columns=NodeName:.spec.nodeName,PodName:.metadata.name

## get custom headers
```
$ cat pods.fmt
NAMESPACE NAME
metadata.namespace metadata.name

kubectl get pods -A -o custom-columns-file=pods.fmt
```

# Taints and tolerations
## Create a taint on node01 with key of spray, value of mortein and effect of NoSchedule
    k taint nodes node01 spray=mortein:NoSchedule

## Create a new pod with the nginx image and pod name as mosquito.
    k run mosquito --image=nginx
    
```
option2 :
cat > mosquito-pod-definition.yaml<EOF
api: v1
kind: Pod
metadata:
  name: mosquito
spec:
  containers:
  - name: mosquito
    image: nginx
EOF
k apply -f mosquito-pod-definition.yaml
```

## get all taints on node node01 
    k describe node node01 | grep -i taint

## track status of a pod
    k get pod --watch

## determine why a pod called 'mosquito' isnt running
    k describe pods/mosquito

## Create another pod named bee with the nginx image, which has a toleration set to the taint mortein.
```
cat > bee-pod-definition.yaml<<EOF
---
apiVersion: v1
kind: Pod
metadata:
  name: bee
spec:
  containers:
  - name: bee
    image: nginx

  tolerations:
  - key: "spray"
    operator: "Equal"
    value: "mortein"
    effect: "NoSchedule"
EOF	  
```
## get taints on controlplane node
k describe node controlplane | grep -i taint

## Remove the taint on controlplane, which currently has the taint effect of NoSchedule.

### first get the taint on node controlplane1
   k describe node controlplane | grep -i taint | awk {'print $2'}
   node-role.kubernetes.io/control-plane:NoSchedule

   k taint nodes controlplane node-role.kubernetes.io/control-plane::NoSchedule-

# Limits and Requests
## A pod called rabbit is deployed. Identify the CPU requirements set on the Pod
    k describe pod rabbit | grep -E "Limit|CPU|Request" -A1

## Delete the rabbit Pod. Once deleted, wait for the pod to fully terminate.
    k delete pod rabbit --wait=true

## The elephant pod runs a process that consumes 15Mi of memory. Increase the limit of the elephant pod to 20Mi.
    k get pod elephant -o yaml > elephant.yaml
    k replace -f elephant.yaml --force

## Delete the elephant Pod. Once deleted, wait for the pod to fully terminate.
    k delete pod elephant --wait=true

# Monitoring

## equivalent of docker stats --no-stream
- needs k8s metrics to be enabled
    k top pod
    k top node
    
## track status of a pod
    k get pod --watch

# DaemonSets
## list all DaemonSets
    k get ds -A

## On how many nodes are the pods scheduled by the DaemonSet kube-proxy?
    kubectl describe daemonset kube-proxy --namespace=kube-system | grep -i nodes

## What is the image used by the POD deployed by the kube-flannel-ds DaemonSet?
     k describe ds kube-flannel-ds -n kube-flannel | grep -i image

## Deploy a DaemonSet for FluentD Logging.
```
Name: elasticsearch
Namespace: kube-system
Image: registry.k8s.io/fluentd-elasticsearch:1.20
```
    k create deployment elasticsearch --image=registry.k8s.io/fluentd-elasticsearch:1.20 -n kube-system --dry-run=client -o yaml > elastic-ds.yaml

- Next, remove the replicas, strategy and status fields from the YAML file using a text editor. Also, change the kind from Deployment to DaemonSet.
- Finally, create the Daemonset by running 
    k create -f fluentd.yaml

# Static pods
## How many static pods exist in this cluster in all namespaces?
    k get po -A | grep '\-controlplane'

## On which nodes are the static pods created currently?
    k get po -A -o wide | grep '\-controlplane'

## What is the docker image used to deploy the kube-api server as a static pod?
    TODO

## Create a static pod named static-busybox that uses the busybox image and the command sleep 1000
```
Name: static-busybox
Image: busybox
```
    kubectl run --restart=Never --image=busybox static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml

## Edit the image on the static pod to use busybox:1.28.4
    kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml

## We just created a new static pod named static-greenbox. Find it and delete it.

- first determine which node this pod runs on by 
   k get po -A -o wide
- then ssh to that node and 
   ps -ef | grep kubelet
- cd to the config filepath and  cat it. this replaces /etc/kubernetes/manifests path
- cd to the config dir
   grep static /var/lib/kubelet/config.yaml
- then delete the greenbox.yaml there.

# Scheduling
- can deploy your own custom scheduler alongside the default kube scheduler, so that it only applies to certian pods
-  to use the custom sceduler in the pod yaml, set key:value as schedulerName:your-custom-sched-name
- to see sched logs use cmd
     k logs my-custom-scheduler --name-space=kube-system



