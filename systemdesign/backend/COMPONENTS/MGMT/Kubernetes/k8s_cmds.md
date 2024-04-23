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
- kubectl create pod nginx-pod --image=nginx --dry-run=client -o yaml
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
