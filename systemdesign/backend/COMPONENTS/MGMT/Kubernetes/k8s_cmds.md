# Ref
- https://kubernetes.io/docs/reference/kubectl/
- https://kubernetes.io/docs/reference/kubectl/conventions/
- https://kubectl.docs.kubernetes.io/guides/
- https://helm.sh/docs/intro/cheatsheet/

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

## count the number of pods that match bu=finance, so dont display the header
k get pods --selector bu=finance --no-headers | wc -l

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
