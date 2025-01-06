# how can i create a pod foo that has a unique id everytime it spawns

- various options
## option A : Pod
- Pod can be created via simple yaml
- example
```
cat > pod.yaml<<EOF
apiVersion: v1
kind: Pod
metadata:
  name: dummypod
  namespace: dummyns
spec:
  containers:
  - name: dummy-container1
    image: quay.io/prometheus/busybox:latest
    command: ["/bin/sh", "-c"]
    args:
    - |
      while true; do
        echo "$(date) - Generating log message..."
      done
EOF

kubectl create namespace dummyns
kubectl apply -f pod.yaml
kubectl get pods -n dummyns
kubectl delete ns dummyns

NOTE: if namespace isnt specified, default namespace is used.
```

## Option B : Use StatefulSet / Deployment / Job